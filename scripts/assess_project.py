#!/usr/bin/env python3
"""Audit objective repository evidence only; never grade Dutch learning."""
import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "progress" / "project-state.json"
README = ROOT / "README.md"
readme = README.read_text(encoding="utf-8") if README.exists() else ""
numbered_words = len(re.findall(r"^\|\s*\d+\s*\|", readme, re.MULTILINE))

def file_exists(path):
    return (ROOT / path).is_file()

workflow_path = ROOT / ".github/workflows/project-status.yml"
workflow = workflow_path.read_text(encoding="utf-8") if workflow_path.is_file() else ""
checks = {
    "P0-03": (numbered_words >= 56, f"README.md: {numbered_words} numbered word entries (automated audit)"),
    "P0-04": ("2–8 November 2026" in readme, "README.md: 2–8 November 2026 weekly archive (automated audit)"),
    "P1-01": (file_exists("docs/LEARNING_PLAN.md"), "docs/LEARNING_PLAN.md (automated file check)"),
    "P1-02": (file_exists("docs/AI_AGENT.md"), "docs/AI_AGENT.md (automated file check)"),
    "P1-03": (file_exists("scripts/update_status.py"), "scripts/update_status.py (automated file check)"),
    "P1-06": (file_exists("docs/QUALITY_AND_EVIDENCE.md"), "docs/QUALITY_AND_EVIDENCE.md (automated file check)"),
    "P1-07": (file_exists("tests/test_project_status.py"), "tests/test_project_status.py (automated file check)"),
    "P1-09": (file_exists("docs/TELEMETRY_AND_SYNC.md"), "docs/TELEMETRY_AND_SYNC.md (automated file check)"),
    "P1-10": (
        file_exists("templates/private-repo/scripts/sync_public.py")
        and file_exists("tests/test_private_repo_template.py"),
        "templates/private-repo/scripts/sync_public.py + tests/test_private_repo_template.py (automated file check)",
    ),
    "P1-11": (file_exists("docs/CHATGPT_INTEGRATION.md"), "docs/CHATGPT_INTEGRATION.md (automated file check)"),
    "P1-12": (
        file_exists("templates/private-repo/scripts/learning_events.py")
        and file_exists("tests/test_private_learning_events.py"),
        "templates/private-repo/scripts/learning_events.py + tests/test_private_learning_events.py (automated file check)",
    ),
    "P1-08": (
        file_exists(".github/workflows/project-status.yml") and "peter-evans/create-pull-request@" in workflow,
        ".github/workflows/project-status.yml (automated file check; execution unverified)",
    ),
}
data = json.loads(STATE.read_text(encoding="utf-8"))
changed = False
for phase in data["phases"]:
    for task in phase["tasks"]:
        result = checks.get(task["id"])
        if result is None:
            continue
        passed, evidence = result
        status = "verified" if passed else "not_evidenced"
        evidence = evidence if passed else None
        if task["status"] != status or task.get("evidence") != evidence:
            task["status"], task["evidence"] = status, evidence
            changed = True
if changed:
    data["evidence_updated_at"] = date.today().isoformat()
    STATE.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Updated objective project evidence; no learner proficiency assessed.")
else:
    print("Objective project evidence unchanged.")
