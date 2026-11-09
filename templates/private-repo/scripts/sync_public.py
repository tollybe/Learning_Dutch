#!/usr/bin/env python3
"""Copy only preapproved public text to the private repository. No network or telemetry."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = (
    "README.md",
    "docs/LEARNING_PLAN.md",
    "docs/QUALITY_AND_EVIDENCE.md",
    "docs/ROADMAP.md",
    "docs/AI_AGENT.md",
)
MAX_BYTES = 500_000

def sync(source: Path, private_root: Path, commit_sha: str) -> list[str]:
    """Mirror allowlisted files; never read, modify or publish private telemetry."""
    if not re.fullmatch(r"[0-9a-f]{40}", commit_sha):
        raise ValueError("Source commit SHA must be 40 lowercase hexadecimal characters.")
    source = source.resolve(strict=True)
    destination = private_root / "public_reference"
    payload = {}
    # Check all files before writing anything, including symlink and size checks.
    for rel in ALLOWED:
        source_path = source / rel
        if source_path.is_symlink() or not source_path.is_file():
            raise FileNotFoundError(f"Missing or symlinked approved public file: {rel}")
        data = source_path.read_bytes()
        if len(data) > MAX_BYTES:
            raise ValueError(f"Public source exceeds limit: {rel}")
        data.decode("utf-8")
        payload[rel] = data

    changed = []
    for rel, data in payload.items():
        target = destination / rel
        if target.is_symlink():
            raise ValueError(f"Refusing to write symlink destination: {target}")
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists() or target.read_bytes() != data:
            target.write_bytes(data)
            changed.append(rel)

    manifest = {
        "source_repository": "tollybe/Learning_Dutch",
        "source_branch": "main",
        "source_commit": commit_sha,
        "imported_paths": list(ALLOWED),
    }
    manifest_path = destination / "SOURCE.json"
    manifest_content = json.dumps(manifest, indent=2) + "\n"
    if not manifest_path.exists() or manifest_path.read_text(encoding="utf-8") != manifest_content:
        manifest_path.write_text(manifest_content, encoding="utf-8")
        changed.append("SOURCE.json")
    return changed

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--commit", required=True)
    args = parser.parse_args()
    changed = sync(args.source, ROOT, args.commit)
    print(f"Approved public material synced; {len(changed)} changed file(s).")

if __name__ == "__main__":
    main()
