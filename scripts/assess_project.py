#!/usr/bin/env python3
"""Evidence-only repo audit. Does not assess human language proficiency."""
import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "progress/project-state.json"
readme_path = ROOT / "README.md"
readme = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""
numbered_words = len(re.findall(r"^\|\s*\d+\s*\|", readme, re.MULTILINE))
checks = {
    "P0-03": (numbered_words >= 56, f"README.md: {numbered_words} numbered word entries (automated audit)"),
    "P0-04": ("2–8 November 2026" in readme, "README.md: 2–8 November 2026 weekly archive (automated audit)"),
    "P1-01": ((ROOT / "docs/LEARNING_PLAN.md").is_file(), "docs/LEARNING_PLAN.md (automated file check)"),
    "P1-02": ((ROOT / "docs/AI_AGENT.md").is_file(), "docs/AI_AGENT.md (automated file check)"),
    "P1-03": ((ROOT / "scripts/update_status.py").is_file(), "scripts/update_status.py (automated file check)"),
}
data = json.loads(STATE.read_text(encoding="utf-8"))
changed = False
for phase in data["phases"]:
    for task in phase["tasks"]:
        if task["id"] not in checks:
            continue
        passed, evidence = checks[task["id"]]
        new_status = "verified" if passed else "not_evidenced"
        new_evidence = evidence if passed else None
        if task["status"] != new_status or task.get("evidence") != new_evidence:
            task["status"] = new_status
            task["evidence"] = new_evidence
            changed = True
if changed:
    data["reviewed_at"] = date.today().isoformat()
    STATE.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Refreshed objective project evidence.")
else:
    print("No objective project evidence changes.")
