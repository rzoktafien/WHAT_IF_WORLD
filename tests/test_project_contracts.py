import copy
import json
import subprocess
import sys
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"tools"))
from validate_manifest import validate

class ProjectContracts(unittest.TestCase):
 def setUp(self):
  self.manifest=json.loads((ROOT/"examples/production_manifest.example.json").read_text(encoding="utf-8"))

 def test_project_instructions_under_8000_chars(self):
  self.assertLessEqual(len((ROOT/"01_INSTRUKSI_PROJECT.md").read_text(encoding="utf-8")),8000)

 def test_required_documents_and_workflow_exist(self):
  for name in ["AGENTS.md","02A_MODULE_ARCHITECTURE.md","03A_CHARACTER_REFERENCE_BIBLE.md",
               "07_SOURCE_AND_CLAIM_LEDGER.md","10_ASSET_AND_SHOT_REGISTER.md",
               "11_QA_AND_RELEASE_PROTOCOL.md",".github/workflows/validate.yml","requirements-dev.txt"]:
   self.assertTrue((ROOT/name).is_file(),name)

 def test_all_schemas_are_valid_json_schema(self):
  for path in (ROOT/"schemas").glob("*.json"):
   schema=json.loads(path.read_text(encoding="utf-8"))
   self.assertEqual(schema["$schema"],"https://json-schema.org/draft/2020-12/schema")
   Draft202012Validator.check_schema(schema)

 def test_example_manifest_conforms_to_production_schema(self):
  schema_dir=ROOT/"schemas"
  resources=[]
  for path in schema_dir.glob("*.schema.json"):
   item=json.loads(path.read_text(encoding="utf-8"))
   item["$id"]=path.resolve().as_uri()
   resources.append((path.resolve().as_uri(),Resource.from_contents(item)))
  root=json.loads((schema_dir/"production_manifest.schema.json").read_text(encoding="utf-8"))
  root["$id"]=(schema_dir/"production_manifest.schema.json").resolve().as_uri()
  registry=Registry().with_resources(resources)
  Draft202012Validator(root,registry=registry).validate(self.manifest)

 def test_example_manifest_passes_format_validation(self):
  errors,blockers=validate(self.manifest)
  self.assertEqual(errors,[]); self.assertTrue(blockers)

 def test_release_gate_blocks_unverified_critical_claim(self):
  errors,blockers=validate(self.manifest,release_gate=True)
  self.assertEqual(errors,[])
  self.assertTrue(any("critical claim" in b for b in blockers))
  self.assertTrue(any("human release approval" in b for b in blockers))

 def test_duplicate_ids_are_rejected(self):
  data=copy.deepcopy(self.manifest)
  data["claims"]=[{"id":"CLM-001","status":"SUPPORTED"},{"id":"CLM-001","status":"SUPPORTED"}]
  errors,_=validate(data)
  self.assertTrue(any("duplicate claims ID" in e for e in errors))

 def test_dangling_source_reference_is_rejected(self):
  data=copy.deepcopy(self.manifest); data["claims"][0]["source_ids"]=["SRC-999"]
  errors,_=validate(data)
  self.assertTrue(any("unknown source SRC-999" in e for e in errors))

 def test_dangling_character_reference_is_rejected(self):
  data=copy.deepcopy(self.manifest)
  data["shots"]=[{"id":"SH-001","production_id":"WW-003","duration_seconds":5,
                  "character_ids":["AST-CHAR-999"],"status":"PLANNED"}]
  errors,_=validate(data)
  self.assertTrue(any("unknown character AST-CHAR-999" in e for e in errors))

 def test_approved_character_requires_canonical_reference(self):
  data=copy.deepcopy(self.manifest)
  data["character_references"]=[{"id":"AST-CHAR-001","status":"APPROVED","rights_status":"CLEARED"}]
  errors,_=validate(data)
  self.assertTrue(any("no canonical_reference" in e for e in errors))

 def test_valid_character_and_shot_link(self):
  data=copy.deepcopy(self.manifest)
  data["character_references"]=[{"id":"AST-CHAR-001","status":"APPROVED","rights_status":"NOT_REQUIRED",
    "canonical_reference":{"kind":"prompt","prompt":"Original character reference prompt."}}]
  data["shots"]=[{"id":"SH-001","production_id":"WW-003","duration_seconds":6,
    "character_ids":["AST-CHAR-001"],"status":"PLANNED"}]
  errors,_=validate(data); self.assertEqual(errors,[])

 def test_repository_validator_passes(self):
  result=subprocess.run([sys.executable,str(ROOT/"tools/validate_project.py")],capture_output=True,text=True)
  self.assertEqual(result.returncode,0,result.stdout+result.stderr)

if __name__=="__main__": unittest.main()
