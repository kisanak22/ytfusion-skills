import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import uuid

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/hds-home-production/scripts/inspect_hds.py"
SPEC = importlib.util.spec_from_file_location("inspect_hds", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class InspectHdsTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.app = self.root / "app"
        self.write(self.app / "src/app.py", "# fixture, never imported")
        self.write(self.app / "src/distribution.py", "EDITION = 'shared'\n")

    def write(self, path, value):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(value, encoding="utf-8")

    def obj(self, path, value):
        self.write(path, json.dumps(value))

    def collection(self, name):
        folder = self.root / name
        identity = str(uuid.uuid4())
        self.obj(folder / ".hds-collection.json", {"id": identity})
        return folder, identity

    def snapshot(self):
        return {
            str(path.relative_to(self.root)): path.read_bytes()
            for path in self.root.rglob("*")
            if path.is_file()
        }

    def test_new_device_does_not_create_master_or_default_directory(self):
        before = self.snapshot()
        result = MODULE.inspect(self.app)
        self.assertTrue(result["ok"])
        self.assertEqual(result["collection"]["status"], "missing")
        self.assertFalse((self.app / "user_data/hds").exists())
        self.assertEqual(self.snapshot(), before)

    def test_independent_shared_collection_reports_counts_without_contents(self):
        folder, identity = self.collection("production")
        self.obj(folder / "channel_profiles/profile_1/profile.json", {"name": "PRIVATE NAME"})
        self.obj(folder / "batch_projects/stock_1/batch.json", {
            "id": "stock_1", "status": "idle",
            "rows_input": [{"title": "PRIVATE TITLE ONE"}, {"title": "PRIVATE TITLE TWO"}],
        })
        self.obj(folder / "batch_projects/stock_1/projects/one/plan.json", {"private": "CONTENT"})
        before = self.snapshot()
        result = MODULE.inspect(self.app, folder)
        observed = result["collection"]
        self.assertEqual(result["edition_marker"], "shared")
        self.assertEqual(observed["collection_id"], identity)
        self.assertEqual(observed["profile_files"], 1)
        self.assertEqual(observed["title_allocations_observed"], 2)
        self.assertEqual(observed["project_folders"], 1)
        self.assertEqual(observed["plan_files"], 1)
        self.assertFalse(observed["native_readiness_checked"])
        self.assertNotIn("PRIVATE", json.dumps(result))
        self.assertNotIn("CONTENT", json.dumps(result))
        self.assertEqual(self.snapshot(), before)

    def test_invalid_selection_and_wrong_identity_never_fall_back(self):
        default = self.app / "user_data/hds"
        self.obj(default / ".hds-collection.json", {"id": str(uuid.uuid4())})
        selection = self.app / "user_data/hds_source.json"
        self.obj(selection, {"schema": 1, "mode": "custom", "path": "relative"})
        result = MODULE.inspect(self.app)
        self.assertFalse(result["ok"])
        self.assertIsNone(result["collection"])
        folder, _ = self.collection("selected")
        self.obj(selection, {
            "schema": 1, "mode": "custom", "path": str(folder),
            "collection_id": str(uuid.uuid4()),
        })
        result = MODULE.inspect(self.app)
        self.assertEqual(result["collection"]["status"], "identity_mismatch")
        self.assertNotIn("profile_files", result["collection"])

    def test_partial_batch_metadata_is_visible_without_claiming_readiness(self):
        folder, _ = self.collection("partial")
        self.write(folder / "batch_projects/broken/batch.json", "{")
        self.obj(folder / "batch_projects/renamed/batch.json", {
            "id": "old", "status": "stopped", "rows_input": [{"title": "example"}],
        })
        result = MODULE.inspect(self.app, folder)["collection"]
        self.assertEqual(result["batch_folders"], 2)
        self.assertEqual(result["malformed_batch_metadata"], 1)
        self.assertEqual(result["batch_id_mismatches"], 1)
        self.assertEqual(result["title_allocations_observed"], 1)
        self.assertFalse(result["native_readiness_checked"])

    def test_hidden_runtime_folders_are_not_projects(self):
        folder, _ = self.collection("runtime-only")
        self.obj(folder / "single_projects/.provider_jobs/state.json", {"running": False})
        self.obj(folder / "single_projects/.scratch/plan.json", {"temporary": True})
        self.obj(folder / "batch_projects/.worker_cache/batch.json", {"temporary": True})
        result = MODULE.inspect(self.app, folder)["collection"]
        self.assertEqual(result["project_folders"], 0)
        self.assertEqual(result["plan_files"], 0)
        self.assertEqual(result["batch_folders"], 0)


if __name__ == "__main__":
    unittest.main()
