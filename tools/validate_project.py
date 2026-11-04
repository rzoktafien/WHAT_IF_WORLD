#!/usr/bin/env python3
"""Repository contract and JSON Schema validation for WHAT IF WORLD."""
from pathlib import Path
import json
import subprocess
import sys

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

ROOT=Path(__file__).resolve().parents[1]
MAX_INSTRUCTION_CHARS=8000
REQUIRED=[
 "AGENTS.md","README.md","00_SETUP_AND_OPERATIONS.md","01_INSTRUKSI_PROJECT.md",
 "02_PANDUAN_PRODUKSI_UTAMA.md","02A_MODULE_ARCHITECTURE.md","03_TEMPLATE_PRODUKSI.md",
 "03A_CHARACTER_REFERENCE_BIBLE.md","05_ARSIP_KONTEN.md","06_DAILY_INTELLIGENCE_PROTOCOL.md",
 "07_SOURCE_AND_CLAIM_LEDGER.md","08_IDEA_SCORING_SYSTEM.md","09_IDEA_BACKLOG.md",
 "10_ASSET_AND_SHOT_REGISTER.md","11_QA_AND_RELEASE_PROTOCOL.md","12_GITHUB_REFERENCE_REVIEW.md",
 "LICENSING_DECISION_RECORD.md","RIGHTS_AND_PROVENANCE_REGISTER.md",
 "schemas/claim.schema.json","schemas/idea.schema.json","schemas/shot.schema.json",
 "schemas/character_reference.schema.json","schemas/production_manifest.schema.json",
 "schemas/generation_attempt.schema.json","schemas/media_asset.schema.json","schemas/edit_timeline.schema.json",
 "examples/production_manifest.example.json","tools/validate_manifest.py",
 "tests/test_project_contracts.py","requirements-dev.txt",".github/workflows/validate.yml"]

def check():
 errors=[]
 for rel in REQUIRED:
  if not (ROOT/rel).is_file(): errors.append(f"Missing required file: {rel}")
 ip=ROOT/"01_INSTRUKSI_PROJECT.md"
 if ip.is_file():
  content=ip.read_text(encoding="utf-8"); count=len(content)
  print(f"01_INSTRUKSI_PROJECT.md: {count}/{MAX_INSTRUCTION_CHARS} characters")
  if count>MAX_INSTRUCTION_CHARS: errors.append(f"Project instructions exceed limit by {count-MAX_INSTRUCTION_CHARS}")
  for section in ("IDEASI BERBASIS PEMANTAUAN","ALUR PRODUKSI","STANDAR KERAS"):
   if section not in content: errors.append(f"Project instructions missing section: {section}")
 schema_dir=ROOT/"schemas"
 resources=[]
 schemas={}
 for path in sorted(schema_dir.glob("*.schema.json")):
  try:
   schema=json.loads(path.read_text(encoding="utf-8"))
   Draft202012Validator.check_schema(schema)
   schema["$id"]=path.resolve().as_uri()
   schemas[path.name]=schema
   resources.append((path.resolve().as_uri(),Resource.from_contents(schema)))
  except Exception as exc:
   errors.append(f"{path.relative_to(ROOT)}: invalid JSON Schema ({exc})")
 registry=Registry().with_resources(resources)
 for name,schema in schemas.items():
  try:
   Draft202012Validator(schema,registry=registry,format_checker=FormatChecker())
  except Exception as exc:
   errors.append(f"{name}: validator construction failed ({exc})")
 manifest=ROOT/"examples/production_manifest.example.json"
 if manifest.is_file() and "production_manifest.schema.json" in schemas:
  try:
   data=json.loads(manifest.read_text(encoding="utf-8"))
   schema=schemas["production_manifest.schema.json"]
   validator=Draft202012Validator(schema,registry=registry,format_checker=FormatChecker())
   for error in validator.iter_errors(data):
    location="/".join(str(part) for part in error.absolute_path) or "<root>"
    errors.append(f"Example manifest schema error at {location}: {error.message}")
  except Exception as exc:
   errors.append(f"Example manifest schema validation failed: {exc}")
 validator_script=ROOT/"tools/validate_manifest.py"
 if manifest.is_file() and validator_script.is_file():
  result=subprocess.run([sys.executable,str(validator_script),str(manifest)],capture_output=True,text=True)
  if result.returncode: errors.append("Example manifest fails semantic validation: "+result.stdout+result.stderr)
 for error in errors: print("FAIL:",error)
 if errors: print(f"RESULT: FAIL ({len(errors)} errors)"); return 1
 print(f"Validated {len(schemas)} JSON Schemas and example manifest (including format checks).")
 print("RESULT: PASS"); return 0

if __name__=="__main__": sys.exit(check())
