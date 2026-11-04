import copy
import json
import subprocess
import sys
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker
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
  schema_dir=ROOT/"schemas"; resources=[]
  for path in schema_dir.glob("*.schema.json"):
   item=json.loads(path.read_text(encoding="utf-8")); item["$id"]=path.resolve().as_uri()
   resources.append((path.resolve().as_uri(),Resource.from_contents(item)))
  root=json.loads((schema_dir/"production_manifest.schema.json").read_text(encoding="utf-8"))
  root["$id"]=(schema_dir/"production_manifest.schema.json").resolve().as_uri()
  Draft202012Validator(root,registry=Registry().with_resources(resources),format_checker=FormatChecker()).validate(self.manifest)

 def test_character_profile_schema_accepts_valid_profile(self):
  schema=json.loads((ROOT/"schemas/character_reference.schema.json").read_text(encoding="utf-8"))
  profile={"id":"AST-CHAR-001","production_id":"WW-003","version":"1.0.0","name":"Protagonis","owner":"WHAT IF WORLD team","created_at":"2026-11-05T00:00:00Z","updated_at":"2026-11-05T00:00:00Z",
   "status":"DRAFT","identity":{"face_shape":"oval","hair":"short black hair","invariant_traits":["small scar above left eyebrow"]},
   "canonical_reference":{"kind":"prompt","prompt":"Photorealistic fictional character reference.","provenance":"Original project prompt","creator":"WHAT IF WORLD team","source":"Original project generation"},
   "wardrobe_variants":[],"rights_status":"NOT_REQUIRED","linked_shots":[]}
  Draft202012Validator(schema,format_checker=FormatChecker()).validate(profile)


 def test_character_profile_schema_requires_owner_timestamps_and_provenance(self):
  schema=json.loads((ROOT/"schemas/character_reference.schema.json").read_text(encoding="utf-8"))
  profile={"id":"AST-CHAR-001","production_id":"WW-003","version":"1.0.0","name":"Protagonis",
   "owner":"WHAT IF WORLD team","created_at":"2026-11-05T00:00:00Z","updated_at":"2026-11-05T00:00:00Z",
   "status":"DRAFT","identity":{"face_shape":"oval","hair":"short black hair","invariant_traits":["scar"]},
   "canonical_reference":{"kind":"prompt","prompt":"Reference prompt","provenance":"Original","creator":"WHAT IF WORLD team","source":"Original project generation"},
   "wardrobe_variants":[],"rights_status":"NOT_REQUIRED","linked_shots":[]}
  Draft202012Validator(schema,format_checker=FormatChecker()).validate(profile)
  for field in ("owner","created_at","updated_at","linked_shots"):
   invalid=copy.deepcopy(profile); invalid.pop(field)
   with self.assertRaises(Exception): Draft202012Validator(schema,format_checker=FormatChecker()).validate(invalid)
  invalid=copy.deepcopy(profile); invalid["canonical_reference"].pop("creator")
  with self.assertRaises(Exception): Draft202012Validator(schema,format_checker=FormatChecker()).validate(invalid)
  invalid=copy.deepcopy(profile); invalid["canonical_reference"].pop("source")
  with self.assertRaises(Exception): Draft202012Validator(schema,format_checker=FormatChecker()).validate(invalid)

 def test_character_profile_schema_rejects_missing_identity_invariant(self):
  schema=json.loads((ROOT/"schemas/character_reference.schema.json").read_text(encoding="utf-8"))
  profile={"id":"AST-CHAR-001","production_id":"WW-003","version":"1.0.0","name":"Protagonis","owner":"WHAT IF WORLD team","created_at":"2026-11-05T00:00:00Z","updated_at":"2026-11-05T00:00:00Z",
   "status":"DRAFT","identity":{"face_shape":"oval","hair":"short black hair","invariant_traits":[]},
   "canonical_reference":{"kind":"prompt","prompt":"Reference prompt","provenance":"Original","creator":"WHAT IF WORLD team","source":"Original project generation"},
   "wardrobe_variants":[],"rights_status":"NOT_REQUIRED","linked_shots":[]}
  with self.assertRaises(Exception): Draft202012Validator(schema).validate(profile)

 def test_example_manifest_passes_format_validation(self):
  errors,blockers=validate(self.manifest)
  self.assertEqual(errors,[]); self.assertTrue(blockers)

 def test_generation_substages_are_valid_manifest_states(self):
  schema_dir=ROOT/"schemas"; resources=[]
  for path in schema_dir.glob("*.schema.json"):
   item=json.loads(path.read_text(encoding="utf-8")); item["$id"]=path.resolve().as_uri()
   resources.append((path.resolve().as_uri(),Resource.from_contents(item)))
  root=json.loads((schema_dir/"production_manifest.schema.json").read_text(encoding="utf-8"))
  root["$id"]=(schema_dir/"production_manifest.schema.json").resolve().as_uri()
  validator=Draft202012Validator(root,registry=Registry().with_resources(resources),format_checker=FormatChecker())
  for state in ("PILOT_GENERATION","BATCH_GENERATION"):
   data=copy.deepcopy(self.manifest); data["state"]=state
   validator.validate(data)
   errors,_=validate(data)
   self.assertEqual(errors,[],state)

 def test_validator_rejects_shot_missing_required_narrative_fields(self):
  data=copy.deepcopy(self.manifest)
  data["shots"]=[{"id":"SH-001","production_id":"WW-003","duration_seconds":6,
   "start_state":"Initial state","action":"A single action","camera_move":"Slow push in","end_state":"Final state","status":"PLANNED"}]
  errors,_=validate(data)
  self.assertTrue(any("missing valid required field purpose" in e for e in errors))

 def test_validator_rejects_invalid_shot_status(self):
  data=copy.deepcopy(self.manifest)
  data["shots"]=[{"id":"SH-001","production_id":"WW-003","purpose":"Test shot purpose","duration_seconds":6,
   "start_state":"Initial state","action":"A single action","camera_move":"Slow push in","end_state":"Final state","status":"DONE"}]
  errors,_=validate(data)
  self.assertTrue(any("has invalid status" in e for e in errors))

 def test_validator_rejects_asset_character_id_collision(self):
  data=copy.deepcopy(self.manifest)
  data["assets"]=[{"id":"AST-CHAR-001","rights_status":"NOT_REQUIRED"}]
  data["character_references"]=[{"id":"AST-CHAR-001","production_id":"WW-003","name":"Protagonis","identity":{"face_shape":"oval","hair":"short black hair","invariant_traits":["distinctive scar"]},"wardrobe_variants":[],"owner":"WHAT IF WORLD team","created_at":"2026-11-05T00:00:00Z",
   "updated_at":"2026-11-05T00:00:00Z","status":"DRAFT","rights_status":"NOT_REQUIRED","version":"1.0.0",
   "canonical_reference":{"kind":"prompt","prompt":"Original reference prompt","provenance":"Original","creator":"WHAT IF WORLD team","source":"Original generation"},"linked_shots":[]}]
  errors,_=validate(data)
  self.assertTrue(any("asset ID collides with character ID" in e for e in errors))

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
  data["shots"]=[{"id":"SH-001","production_id":"WW-003","purpose":"Test shot purpose","start_state":"Initial state","action":"A single action","camera_move":"Slow push in","end_state":"Final state","duration_seconds":5,
                  "character_ids":["AST-CHAR-999"],"status":"PLANNED"}]
  errors,_=validate(data)
  self.assertTrue(any("unknown character AST-CHAR-999" in e for e in errors))

 def test_approved_character_requires_canonical_reference(self):
  data=copy.deepcopy(self.manifest)
  data["character_references"]=[{"id":"AST-CHAR-001","production_id":"WW-003","name":"Protagonis","identity":{"face_shape":"oval","hair":"short black hair","invariant_traits":["distinctive scar"]},"wardrobe_variants":[],"owner":"WHAT IF WORLD team","created_at":"2026-11-05T00:00:00Z","updated_at":"2026-11-05T00:00:00Z","status":"APPROVED","rights_status":"CLEARED","version":"1.0.0"}]
  errors,_=validate(data)
  self.assertTrue(any("no canonical_reference" in e for e in errors))

 def test_character_reference_version_is_required_and_matches(self):
  data=copy.deepcopy(self.manifest)
  data["character_references"]=[{"id":"AST-CHAR-001","production_id":"WW-003","name":"Protagonis","identity":{"face_shape":"oval","hair":"short black hair","invariant_traits":["distinctive scar"]},"wardrobe_variants":[],"owner":"WHAT IF WORLD team","created_at":"2026-11-05T00:00:00Z","updated_at":"2026-11-05T00:00:00Z","status":"APPROVED","rights_status":"NOT_REQUIRED","version":"1.0.0",
   "canonical_reference":{"kind":"prompt","prompt":"Original prompt","provenance":"Original","creator":"WHAT IF WORLD team","source":"Original project generation"},"approval":{"by":"Producer","at":"2026-11-05T01:00:00Z"},"linked_shots":["SH-001"]}]
  data["shots"]=[{"id":"SH-001","production_id":"WW-003","purpose":"Test shot purpose","start_state":"Initial state","action":"A single action","camera_move":"Slow push in","end_state":"Final state","duration_seconds":6,
   "character_ids":["AST-CHAR-001"],"character_reference_versions":{"AST-CHAR-001":"1.0.0"},"status":"PLANNED"}]
  errors,_=validate(data); self.assertEqual(errors,[])
  data["shots"][0]["character_reference_versions"]["AST-CHAR-001"]="2.0.0"
  errors,_=validate(data)
  self.assertTrue(any("mismatched character reference version" in e for e in errors))

 def test_valid_character_and_shot_link(self):
  data=copy.deepcopy(self.manifest)
  data["character_references"]=[{"id":"AST-CHAR-001","production_id":"WW-003","name":"Protagonis","identity":{"face_shape":"oval","hair":"short black hair","invariant_traits":["distinctive scar"]},"wardrobe_variants":[],"owner":"WHAT IF WORLD team","created_at":"2026-11-05T00:00:00Z","updated_at":"2026-11-05T00:00:00Z","status":"APPROVED","rights_status":"NOT_REQUIRED","version":"1.0.0",
    "canonical_reference":{"kind":"prompt","prompt":"Original character reference prompt.","provenance":"Original","creator":"WHAT IF WORLD team","source":"Original project generation"},"approval":{"by":"Producer","at":"2026-11-05T01:00:00Z"},"linked_shots":["SH-001"]}]
  data["shots"]=[{"id":"SH-001","production_id":"WW-003","purpose":"Test shot purpose","start_state":"Initial state","action":"A single action","camera_move":"Slow push in","end_state":"Final state","duration_seconds":6,
    "character_ids":["AST-CHAR-001"],"character_reference_versions":{"AST-CHAR-001":"1.0.0"},"status":"PLANNED"}]
  errors,_=validate(data); self.assertEqual(errors,[])

 def test_repository_validator_passes(self):
  result=subprocess.run([sys.executable,str(ROOT/"tools/validate_project.py")],capture_output=True,text=True)
  self.assertEqual(result.returncode,0,result.stdout+result.stderr)


 def test_daily_intelligence_contract_matches_project_instructions(self):
  instructions=(ROOT/"01_INSTRUKSI_PROJECT.md").read_text(encoding="utf-8")
  daily=(ROOT/"06_DAILY_INTELLIGENCE_PROTOCOL.md").read_text(encoding="utf-8")
  setup=(ROOT/"00_SETUP_AND_OPERATIONS.md").read_text(encoding="utf-8")
  for text in (instructions,daily,setup):
   self.assertIn("3–5",text)
   self.assertIn("HUMAN BODY & MIND",text)
   self.assertIn("EARTH & COSMOS",text)
   self.assertIn("CIVILIZATION & FUTURE",text)
  self.assertIn("Satu atau dua kandidat tetap sah",instructions)
  self.assertIn("Satu atau dua kandidat dapat diterima",daily)
  self.assertIn("fewer are valid",setup)
  self.assertIn("Jangan memenuhi kuota dengan ide lemah",daily)
  self.assertIn("HOLD",instructions)

 def test_daily_discovery_lanes_are_not_editorial_pillars(self):
  daily=(ROOT/"06_DAILY_INTELLIGENCE_PROTOCOL.md").read_text(encoding="utf-8")
  self.assertIn("Lima lane discovery",daily)
  self.assertIn("Tiga pilar editorial",daily)
  self.assertIn("bukan pilar utama baru",daily)

 def test_official_scoring_weights_are_unchanged_and_sum_to_100(self):
  scoring=(ROOT/"08_IDEA_SCORING_SYSTEM.md").read_text(encoding="utf-8")
  expected=["10%","25%","15%","20%","15%","10%","5%"]
  for weight in expected: self.assertIn(weight,scoring)
  self.assertIn("Formula:",scoring)

 def test_asset_identifier_contract_is_typed(self):
  architecture=(ROOT/"02A_MODULE_ARCHITECTURE.md").read_text(encoding="utf-8")
  register=(ROOT/"10_ASSET_AND_SHOT_REGISTER.md").read_text(encoding="utf-8")
  for token in ["AST-CHAR-###","AST-LOC-###","AST-PROP-###","AST-REF-###","AST-KF-###","AST-VIDEO-###","AST-AUDIO-###","AST-MASTER-###"]:
   self.assertIn(token,architecture)
   self.assertIn(token,register)
  self.assertNotIn("Asset: AST-###",architecture)

 def test_persistence_and_human_approval_are_explicit(self):
  instructions=(ROOT/"01_INSTRUKSI_PROJECT.md").read_text(encoding="utf-8")
  daily=(ROOT/"06_DAILY_INTELLIGENCE_PROTOCOL.md").read_text(encoding="utf-8")
  self.assertIn("Percakapan bukan bukti persistensi",instructions)
  self.assertIn("Jangan mengklaim GitHub/Project Files diperbarui tanpa konfirmasi",daily)
  self.assertIn("persetujuan eksplisit",instructions.lower())

 def test_approved_character_requires_explicit_approval_metadata(self):
  schema=json.loads((ROOT/"schemas/character_reference.schema.json").read_text(encoding="utf-8"))
  profile={"id":"AST-CHAR-001","production_id":"WW-003","version":"1.0.0","name":"Protagonis","owner":"WHAT IF WORLD team","created_at":"2026-11-05T00:00:00Z","updated_at":"2026-11-05T00:00:00Z",
   "status":"APPROVED","identity":{"face_shape":"oval","hair":"short black hair","invariant_traits":["scar"]},
   "canonical_reference":{"kind":"prompt","prompt":"Original reference","provenance":"Original project prompt","creator":"WHAT IF WORLD team","source":"Original project generation"},
   "wardrobe_variants":[],"rights_status":"NOT_REQUIRED","linked_shots":[]}
  with self.assertRaises(Exception): Draft202012Validator(schema,format_checker=FormatChecker()).validate(profile)
  profile["approval"]={"by":"Producer","at":"2026-11-05T01:00:00Z"}
  Draft202012Validator(schema,format_checker=FormatChecker()).validate(profile)
  profile["approval"]["at"]="not-a-date-time"
  with self.assertRaises(Exception): Draft202012Validator(schema,format_checker=FormatChecker()).validate(profile)

 def test_validator_rejects_character_missing_invariant_identity(self):
  data=copy.deepcopy(self.manifest)
  data["character_references"]=[{"id":"AST-CHAR-001","production_id":"WW-003","name":"Protagonis","identity":{"face_shape":"oval","hair":"short black hair","invariant_traits":[]},"wardrobe_variants":[],"owner":"WHAT IF WORLD team","created_at":"2026-11-05T00:00:00Z","updated_at":"2026-11-05T00:00:00Z","status":"DRAFT","rights_status":"NOT_REQUIRED","version":"1.0.0",
   "canonical_reference":{"kind":"prompt","prompt":"Original reference prompt","provenance":"Original","creator":"WHAT IF WORLD team","source":"Original generation"},"linked_shots":[]}]
  errors,_=validate(data)
  self.assertTrue(any("invariant_traits" in e for e in errors))

 def test_validator_blocks_unapproved_character_before_batch_generation(self):
  data=copy.deepcopy(self.manifest); data["state"]="BATCH_GENERATION"
  data["character_references"]=[{"id":"AST-CHAR-001","production_id":"WW-003","name":"Protagonis","identity":{"face_shape":"oval","hair":"short black hair","invariant_traits":["distinctive scar"]},"wardrobe_variants":[],"owner":"WHAT IF WORLD team","created_at":"2026-11-05T00:00:00Z","updated_at":"2026-11-05T00:00:00Z","status":"DRAFT","rights_status":"NOT_REQUIRED","version":"1.0.0",
   "canonical_reference":{"kind":"prompt","prompt":"Original reference prompt","provenance":"Original","creator":"WHAT IF WORLD team","source":"Original generation"},"linked_shots":["SH-001"]}]
  data["shots"]=[{"id":"SH-001","production_id":"WW-003","purpose":"Character continuity shot","duration_seconds":6,
   "start_state":"Initial state","action":"A single action","camera_move":"Slow push in","end_state":"Final state",
   "character_ids":["AST-CHAR-001"],"character_reference_versions":{"AST-CHAR-001":"1.0.0"},"status":"PLANNED"}]
  errors,blockers=validate(data)
  self.assertEqual(errors,[])
  self.assertTrue(any("not APPROVED for generation" in b for b in blockers))

 def test_validator_blocks_unresolved_asset_rights_before_pilot(self):
  data=copy.deepcopy(self.manifest); data["state"]="PILOT_GENERATION"
  data["assets"]=[{"id":"AST-VIDEO-001","rights_status":"PENDING"}]
  data["shots"]=[{"id":"SH-001","production_id":"WW-003","purpose":"Asset rights gate shot","duration_seconds":6,
   "start_state":"Initial state","action":"A single action","camera_move":"Slow push in","end_state":"Final state",
   "asset_ids":["AST-VIDEO-001"],"status":"PLANNED"}]
  errors,blockers=validate(data)
  self.assertEqual(errors,[])
  self.assertTrue(any("asset AST-VIDEO-001 rights are unresolved" in b for b in blockers))

 def test_validator_rejects_approved_character_without_approval_metadata(self):
  data=copy.deepcopy(self.manifest)
  data["character_references"]=[{"id":"AST-CHAR-001","production_id":"WW-003","name":"Protagonis","identity":{"face_shape":"oval","hair":"short black hair","invariant_traits":["distinctive scar"]},"wardrobe_variants":[],"owner":"WHAT IF WORLD team","created_at":"2026-11-05T00:00:00Z","updated_at":"2026-11-05T00:00:00Z","status":"APPROVED","rights_status":"NOT_REQUIRED","version":"1.0.0",
   "canonical_reference":{"kind":"prompt","prompt":"Original reference","provenance":"Original","creator":"WHAT IF WORLD team","source":"Original project generation"}}]
  errors,_=validate(data)
  self.assertTrue(any("missing approval.by or approval.at" in e for e in errors))

 def test_validator_rejects_non_reciprocal_shot_to_character_link(self):
  data=copy.deepcopy(self.manifest)
  data["character_references"]=[{"id":"AST-CHAR-001","production_id":"WW-003","name":"Protagonis","identity":{"face_shape":"oval","hair":"short black hair","invariant_traits":["distinctive scar"]},"wardrobe_variants":[],"owner":"WHAT IF WORLD team","created_at":"2026-11-05T00:00:00Z","updated_at":"2026-11-05T00:00:00Z","status":"DRAFT","rights_status":"NOT_REQUIRED","version":"1.0.0",
   "canonical_reference":{"kind":"prompt","prompt":"Original reference","provenance":"Original","creator":"WHAT IF WORLD team","source":"Original project generation"},"linked_shots":[]}]
  data["shots"]=[{"id":"SH-001","production_id":"WW-003","purpose":"Test shot purpose","start_state":"Initial state","action":"A single action","camera_move":"Slow push in","end_state":"Final state","duration_seconds":6,"character_ids":["AST-CHAR-001"],
   "character_reference_versions":{"AST-CHAR-001":"1.0.0"},"status":"PLANNED"}]
  errors,_=validate(data)
  self.assertTrue(any("character linked_shots does not include the shot" in e for e in errors))

if __name__=="__main__": unittest.main()
