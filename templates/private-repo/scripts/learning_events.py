#!/usr/bin/env python3
"""Validate minimal opt-in Dutch-learning events; no ChatGPT API or external telemetry."""
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVENTS = ROOT / "data" / "events"
REPORT = ROOT / "docs" / "LEARNING_ACTIVITY.md"

TYPES = {"lesson_generated", "lesson_acknowledged", "exercise_responded",
         "practice_self_reported", "delayed_transfer_reported"}
SOURCES = {"task_run_metadata", "explicit_user_action", "consented_manual_entry", "consented_integration"}
MODALITIES = {"reading", "writing", "listening", "speaking", "mixed"}
LEVELS = {"exposed", "recognized", "prompted_use", "independent_use",
          "delayed_transfer", "insufficient_evidence"}
REQUIRED = {"schema_version", "event_id", "event_date", "event_type", "source"}
OPTIONAL = {"lesson_id", "modality", "evidence_level"}

def validate(event, path=None):
    if not isinstance(event, dict):
        raise ValueError("Event must be a JSON object")
    if not REQUIRED <= event.keys() or event.keys() - (REQUIRED | OPTIONAL):
        raise ValueError("Event fields do not match the minimal schema")
    if event["schema_version"] != "1.0.0":
        raise ValueError("Unsupported event schema version")
    for key, regex in (("event_id", r"[A-Za-z0-9_-]{8,80}"),
                       ("lesson_id", r"[A-Za-z0-9_-]{1,80}")):
        if key in event and (not isinstance(event[key], str) or not re.fullmatch(regex, event[key])):
            raise ValueError(f"Invalid {key}")
    value = event["event_date"]
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise ValueError("Invalid date format")
    try:
        if date.fromisoformat(value).isoformat() != value:
            raise ValueError("Non-canonical date")
    except ValueError as exc:
        raise ValueError("Invalid event date") from exc
    for name, choices in (("event_type", TYPES), ("source", SOURCES),
                          ("modality", MODALITIES), ("evidence_level", LEVELS)):
        if name in event and (not isinstance(event[name], str) or event[name] not in choices):
            raise ValueError(f"Invalid {name}")
    if event["event_type"] == "lesson_acknowledged" and event["source"] not in {"explicit_user_action", "consented_integration"}:
        raise ValueError("Acknowledgements must be intentional and sourced")
    if event["event_type"] == "lesson_generated" and event["source"] not in {"task_run_metadata", "consented_integration"}:
        raise ValueError("Generated lessons need real task-run evidence")
    if path is not None and path.stem != event["event_id"]:
        raise ValueError("Event filename must equal event_id.json")
    return event

def read_events(directory=EVENTS):
    events = []
    if not directory.exists():
        return events
    seen = set()
    for path in sorted(directory.glob("*.json")):
        e = validate(json.loads(path.read_text(encoding="utf-8")), path)
        if e["event_id"] in seen:
            raise ValueError("Duplicate event_id: " + e["event_id"])
        seen.add(e["event_id"])
        events.append(e)
    return events

def render_report(events):
    counts = Counter(e["event_type"] for e in events)
    names = {
        "lesson_generated": "Known generated lessons",
        "lesson_acknowledged": "Explicit acknowledgements",
        "exercise_responded": "Voluntary exercise responses",
        "practice_self_reported": "Voluntary real-world practice reports",
        "delayed_transfer_reported": "Voluntary delayed-transfer reports",
    }
    lines = ["# Private learning activity", "",
             "> AUTO-GENERATED from optional minimal events in the **private repository**.",
             "",
             "These counts describe **recorded evidence only**. No data does not mean no Dutch learning; a generated lesson does not imply it was opened or read.",
             "",
             f"Total explicitly recorded events: **{len(events)}**.", ""]
    for event_type, label in names.items():
        lines.append(f"- {label}: **{counts[event_type]}**")
    lines.extend(["", "No streaks, open-rate estimates, engagement scores, or claims about language proficiency are calculated.",
                  "Raw ChatGPT messages, private dialogues and voice recordings must not be recorded here.", ""])
    return "\n".join(lines)

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    report = render_report(read_events())
    if args.check:
        if not REPORT.is_file() or REPORT.read_text(encoding="utf-8") != report:
            raise SystemExit("Learning activity report is stale.")
        print("Minimal event report is valid.")
    else:
        REPORT.parent.mkdir(parents=True, exist_ok=True)
        REPORT.write_text(report, encoding="utf-8")
        print("Updated private learning activity report.")

if __name__ == "__main__":
    main()
