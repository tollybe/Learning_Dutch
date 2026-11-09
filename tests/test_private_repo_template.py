"""Check that the private repository starter mirrors only explicitly public files."""
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

    def test_incomplete_public_source_cannot_partially_sync(self):
        with tempfile.TemporaryDirectory() as tmp:
            source, private = Path(tmp) / "public", Path(tmp) / "private"
            source.mkdir()
            private.mkdir()
            (source / "README.md").write_text("only one file", encoding="utf-8")
            with self.assertRaises(FileNotFoundError):
                module.sync(source, private, "a" * 40)
            self.assertFalse((private / "public_reference").exists())

    def test_invalid_commit_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                module.sync(Path(tmp), Path(tmp), "not-a-sha")

if __name__ == "__main__":
    unittest.main()
