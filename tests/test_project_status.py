"""Deterministic, dependency-free regression checks for project docs."""
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("project_status", ROOT / "scripts" / "update_status.py")
status_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(status_module)


class ProjectStatusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.state = json.loads((ROOT / "progress" / "project-state.json").read_text(encoding="utf-8"))

    def test_source_of_truth_has_unique_tasks(self):
        status_module.validate(self.state)
        task_ids = [t["id"] for p in self.state["phases"] for t in p["tasks"]]
        self.assertEqual(len(task_ids), len(set(task_ids)))

    def test_status_is_deterministic(self):
        first = status_module.render(self.state)
        self.assertEqual(first, status_module.render(self.state))
        self.assertIn("not** a Dutch proficiency score", first)

    def test_generated_report_matches_source(self):
        expected = status_module.render(self.state)
        actual = (ROOT / "docs" / "STATUS.md").read_text(encoding="utf-8")
        self.assertEqual(actual, expected)

    def test_verified_tasks_need_evidence(self):
        changed = json.loads(json.dumps(self.state))
        task = next(t for p in changed["phases"] for t in p["tasks"] if t["status"] == "verified")
        task["evidence"] = None
        with self.assertRaises(ValueError):
            status_module.validate(changed)

    def test_no_mastery_labels_in_project_state(self):
        self.assertNotIn("mastered", json.dumps(self.state).lower())


if __name__ == "__main__":
    unittest.main()
