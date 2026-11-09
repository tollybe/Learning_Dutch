#!/usr/bin/env python3
"""Mirror an allowlist of merged public files into a private repository.

No network access, private data reads, or code execution from the public source.
"""
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
    "docs/TELEMETRY_AND_SYNC.md",
    "docs/CHATGPT_INTEGRATION.md",
)
MANDATORY = {"README.md"}
MAX_BYTES = 500_000


def sync(source: Path, private_root: Path, commit_sha: str) -> list[str]:
    """Copy public-only documents; leave all private data untouched."""
    if not re.fullmatch(r"[0-9a-f]{40}", commit_sha):
        raise ValueError("Source commit SHA must be 40 lowercase hexadecimal characters")
    source = source.resolve(strict=True)
    dest = private_root / "public_reference"
    if dest.is_symlink():
        raise ValueError("The public_reference directory must not be a symlink")

    payload = {}
    # Check every eligible source before any writes. Public main may not yet
    # contain proposed docs until the separate documentation PR is merged.
    for rel in ALLOWED:
        path = source / rel
        if path.is_symlink():
            raise ValueError(f"Refusing symlink source: {rel}")
        if not path.exists():
            if rel in MANDATORY:
                raise FileNotFoundError(f"Missing mandatory public file: {rel}")
            continue
        if not path.is_file():
            raise ValueError(f"Source is not a regular file: {rel}")
        data = path.read_bytes()
        if len(data) > MAX_BYTES:
            raise ValueError(f"Public source exceeds size limit: {rel}")
        data.decode("utf-8")
        payload[rel] = data

    changed = []
    for rel, data in payload.items():
        target = dest / rel
        if target.is_symlink() or target.parent.is_symlink():
            raise ValueError(f"Refusing symlink destination: {target}")
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists() or target.read_bytes() != data:
            target.write_bytes(data)
            changed.append(rel)

    # Remove stale copies only inside the approved public mirror.
    for rel in ALLOWED:
        if rel not in payload:
            target = dest / rel
            if target.is_symlink():
                raise ValueError(f"Refusing symlink destination: {target}")
            if target.is_file():
                target.unlink()
                changed.append(rel + " (removed)")

    manifest = {
        "source_repository": "tollybe/Learning_Dutch",
        "source_branch": "main",
        "source_commit": commit_sha,
        "imported_paths": list(payload),
    }
    manifest_path = dest / "SOURCE.json"
    content = json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"
    if manifest_path.is_symlink():
        raise ValueError("Refusing symlink manifest")
    if not manifest_path.exists() or manifest_path.read_text(encoding="utf-8") != content:
        manifest_path.write_text(content, encoding="utf-8")
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
