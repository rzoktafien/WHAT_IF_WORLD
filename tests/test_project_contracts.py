import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class ProjectContracts(unittest.TestCase):
    def test_project_instructions_under_8000_chars(self):
        text = (ROOT / "01_INSTRUKSI_PROJECT.md").read_text(encoding="utf-8")
        self.assertLessEqual(len(text), 8000)

    def test_required_stage_and_qa_docs_exist(self):
        for name in [
            "02A_MODULE_ARCHITECTURE.md", "07_SOURCE_AND_CLAIM_LEDGER.md",
            "10_ASSET_AND_SHOT_REGISTER.md", "11_QA_AND_RELEASE_PROTOCOL.md"
        ]:
            self.assertTrue((ROOT / name).is_file(), name)

    def test_schemas_are_valid_json(self):
        for path in (ROOT / "schemas").glob("*.json"):
            obj = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(obj["type"], "object")
            self.assertTrue(obj["required"])

    def test_example_manifest_has_valid_identity(self):
        obj = json.loads((ROOT / "examples/production_manifest.example.json").read_text(encoding="utf-8"))
        self.assertRegex(obj["production_id"], r"^WW-\d{3,}$")

    def test_release_gate_blocks_unverified_critical_claim(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "tools/validate_manifest.py"),
             str(ROOT / "examples/production_manifest.example.json"), "--release-gate"],
            capture_output=True, text=True
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("BLOCKER:", result.stdout)

    def test_validator_passes(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "tools/validate_project.py")],
            capture_output=True, text=True
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

if __name__ == "__main__":
    unittest.main()
