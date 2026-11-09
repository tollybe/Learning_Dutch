"""Tests for the one-way private repository mirror."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "templates" / "private-repo"
spec = importlib.util.spec_from_file_location("private_sync", TEMPLATE / "scripts" / "sync_public.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class PrivateRepoTemplateTests(unittest.TestCase):
    def test_copy_only_allowlisted_public_files_and_keep_private_data(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source, private = root / "public", root / "private"
            source.mkdir()
            private.mkdir()
            for rel in module.ALLOWED:
                path = source / rel
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("Public example: " + rel, encoding="utf-8")
            (source / "private-notes.txt").write_text("DO NOT COPY", encoding="utf-8")
            (private / "data").mkdir()
            (private / "data" / "private-event.jsonl").write_text("PRIVATE", encoding="utf-8")

            sha = "a" * 40
            changed = module.sync(source, private, sha)
            self.assertEqual(len(changed), len(module.ALLOWED) + 1)
            self.assertFalse((private / "public_reference" / "private-notes.txt").exists())
            self.assertEqual((private / "data/private-event.jsonl").read_text(), "PRIVATE")
            self.assertEqual(module.sync(source, private, sha), [])
            manifest = json.loads((private / "public_reference/SOURCE.json").read_text())
            self.assertEqual(manifest["source_commit"], sha)
            self.assertEqual(manifest["imported_paths"], list(module.ALLOWED))

    def test_public_main_can_omit_unmerged_optional_docs(self):
        with tempfile.TemporaryDirectory() as tmp:
            source, private = Path(tmp) / "public", Path(tmp) / "private"
            source.mkdir()
            private.mkdir()
            (source / "README.md").write_text("One public word", encoding="utf-8")
            changed = module.sync(source, private, "a" * 40)
            self.assertEqual(set(changed), {"README.md", "SOURCE.json"})
            manifest = json.loads((private / "public_reference/SOURCE.json").read_text())
            self.assertEqual(manifest["imported_paths"], ["README.md"])
            self.assertEqual(module.sync(source, private, "a" * 40), [])

    def test_missing_mandatory_readme_cannot_partially_sync(self):
        with tempfile.TemporaryDirectory() as tmp:
            source, private = Path(tmp) / "public", Path(tmp) / "private"
            source.mkdir()
            private.mkdir()
            (source / "docs").mkdir()
            (source / "docs/ROADMAP.md").write_text("Draft", encoding="utf-8")
            with self.assertRaises(FileNotFoundError):
                module.sync(source, private, "a" * 40)
            self.assertFalse((private / "public_reference").exists())

    def test_invalid_commit_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                module.sync(Path(tmp), Path(tmp), "not-a-sha")

    def test_obsolete_approved_file_removed_but_private_data_preserved(self):
        with tempfile.TemporaryDirectory() as tmp:
            source, private = Path(tmp) / "public", Path(tmp) / "private"
            source.mkdir()
            private.mkdir()
            (source / "README.md").write_text("Public lessons", encoding="utf-8")
            extra = source / "docs/LEARNING_PLAN.md"
            extra.parent.mkdir(parents=True)
            extra.write_text("Public plan", encoding="utf-8")
            module.sync(source, private, "a" * 40)
            (private / "data").mkdir()
            (private / "data/notes.txt").write_text("never delete", encoding="utf-8")
            extra.unlink()
            changed = module.sync(source, private, "b" * 40)
            self.assertIn("docs/LEARNING_PLAN.md (removed)", changed)
            self.assertEqual((private / "data/notes.txt").read_text(), "never delete")


if __name__ == "__main__":
    unittest.main()
