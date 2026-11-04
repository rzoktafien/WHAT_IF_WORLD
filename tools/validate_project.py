#!/usr/bin/env python3
"""Dependency-free repository contract checks for WHAT IF WORLD."""
from pathlib import Path
import json
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
MAX_INSTRUCTION_CHARS=8000
REQUIRED=[
 "AGENTS.md","README.md","00_SETUP_AND_OPERATIONS.md","01_INSTRUKSI_PROJECT.md",
 "02_PANDUAN_PRODUKSI_UTAMA.md","02A_MODULE_ARCHITECTURE.md","03_TEMPLATE_PRODUKSI.md",
 "03A_CHARACTER_REFERENCE_BIBLE.md","05_ARSIP_KONTEN.md","06_DAILY_INTELLIGENCE_PROTOCOL.md",
 "07_SOURCE_AND_CLAIM_LEDGER.md","08_IDEA_SCORING_SYSTEM.md","09_IDEA_BACKLOG.md",
 "10_ASSET_AND_SHOT_REGISTER.md","11_QA_AND_RELEASE_PROTOCOL.md","12_GITHUB_REFERENCE_REVIEW.md",
 "schemas/claim.schema.json","schemas/idea.schema.json","schemas/shot.schema.json",
 "schemas/character_reference.schema.json","schemas/production_manifest.schema.json",
 "examples/production_manifest.example.json","tools/validate_manifest.py",
 "tests/test_project_contracts.py",".github/workflows/validate.yml"]

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
 for path in sorted((ROOT/"schemas").glob("*.json")):
  try:
   schema=json.loads(path.read_text(encoding="utf-8"))
   if schema.get("$schema")!="https://json-schema.org/draft/2020-12/schema": errors.append(f"{path.relative_to(ROOT)}: unsupported schema draft")
   if schema.get("type")!="object" or not schema.get("required"): errors.append(f"{path.relative_to(ROOT)}: schema must define object and required fields")
  except Exception as exc: errors.append(f"{path.relative_to(ROOT)}: invalid JSON ({exc})")
 manifest=ROOT/"examples/production_manifest.example.json"; validator=ROOT/"tools/validate_manifest.py"
 if manifest.is_file() and validator.is_file():
  result=subprocess.run([sys.executable,str(validator),str(manifest)],capture_output=True,text=True)
  if result.returncode: errors.append("Example manifest fails format validation: "+result.stdout+result.stderr)
 for error in errors: print("FAIL:",error)
 if errors: print(f"RESULT: FAIL ({len(errors)} errors)"); return 1
 print("RESULT: PASS"); return 0

if __name__=="__main__": sys.exit(check())
