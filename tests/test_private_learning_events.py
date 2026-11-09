"""Validate private event handling without collecting personal responses."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "templates/private-repo/scripts/learning_events.py"
spec = importlib.util.spec_from_file_location("learning_events", SCRIPT)
events = importlib.util.module_from_spec(spec)
spec.loader.exec_module(events)


def sample():
    return {
        "schema_version": "1.0.0",
        "event_id": "testevent_001",
        "event_date": "2026-11-09",
        "event_type": "exercise_responded",
        "source": "explicit_user_action",
        "lesson_id": "word_001",
        "modality": "writing",
        "evidence_level": "prompted_use",
    }


class LearningEventTests(unittest.TestCase):
    def test_valid_event(self):
        self.assertEqual(events.validate(sample())["event_type"], "exercise_responded")

    def test_disallow_arbitrary_private_text(self):
        record = sample()
        record["message"] = "My personal conversation"
        with self.assertRaises(ValueError):
            events.validate(record)

    def test_no_fake_read_receipts(self):
        record = sample()
        record["event_type"] = "lesson_viewed"
        with self.assertRaises(ValueError):
            events.validate(record)

    def test_acknowledgement_requires_explicit_source(self):
        record = sample()
        record["event_type"] = "lesson_acknowledged"
        record["source"] = "task_run_metadata"
        with self.assertRaises(ValueError):
            events.validate(record)

    def test_generation_requires_provenance(self):
        record = sample()
        record["event_type"] = "lesson_generated"
        record["source"] = "explicit_user_action"
        with self.assertRaises(ValueError):
            events.validate(record)

    def test_quiet_period_does_not_imply_failure(self):
        report = events.render_report([])
        self.assertIn("No data does not mean no Dutch learning", report)
        self.assertNotIn("missed", report.lower())

    def test_record_id_matches_filename_and_idempotent(self):
        with tempfile.TemporaryDirectory() as folder:
            p = Path(folder) / "testevent_001.json"
            p.write_text(json.dumps(sample()), encoding="utf-8")
            self.assertEqual(len(events.read_events(Path(folder))), 1)
            self.assertEqual(events.read_events(Path(folder)), events.read_events(Path(folder)))
            with self.assertRaises(ValueError):
                events.validate(sample(), Path(folder) / "another.json")


if __name__ == "__main__":
    unittest.main()
