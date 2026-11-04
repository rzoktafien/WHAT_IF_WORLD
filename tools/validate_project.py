#!/usr/bin/env python3
"""Dependency-free contract checks for WHAT IF WORLD Production Module V3."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MAX_INSTRUCTION_CHARS = 8000

REQUIRED_FILES = [
    "01_INSTRUKSI_PROJECT.md", "02_PANDUAN_PRODUKSI_UTAMA.md",
    "02A_MODULE_ARCHITECTURE.md", "03_TEMPLATE_PRODUKSI.md",
    "05_ARSIP_KONTEN.md", "06_DAILY_INTELLIGENCE_PROTOCOL.md",
    "07_SOURCE_AND_CLAIM_LEDGER.md", "08_IDEA_SCORING_SYSTEM.md",
    "09_IDEA_BACKLOG.md", "10_ASSET_AND_SHOT_REGISTER.md",
    "11_QA_AND_RELEASE_PROTOCOL.md"
]

def check():
    errors, warnings = [], []
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).is_file():
            errors.append(f"Missing required file: {rel}")

    instruction_path = ROOT / "01_INSTRUKSI_PROJECT.md"
    if instruction_path.exists():
        instruction = instruction_path.read_text(encoding="utf-8")
        count = len(instruction)
        print(f"01_INSTRUKSI_PROJECT.md: {count}/{MAX_INSTRUCTION_CHARS} characters")
        if count > MAX_INSTRUCTION_CHARS:
            errors.append(f"Project instructions exceed limit by {count-MAX_INSTRUCTION_CHARS} characters")
        for phrase in ("IDEASI BERBASIS PEMANTAUAN", "ALUR PRODUKSI", "STANDAR KERAS"):
            if phrase not in instruction:
                errors.append(f"Project instructions missing required section: {phrase}")

    for schema_path in sorted((ROOT / "schemas").glob("*.json")):
        try:
            schema = json.loads(schema_path.read_text(encoding="utf-8"))
            if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
                errors.append(f"{schema_path.name}: unexpected JSON Schema version")
            if schema.get("type") != "object" or not schema.get("required"):
                errors.append(f"{schema_path.name}: schema must define object + required fields")
        except Exception as exc:
            errors.append(f"{schema_path.name}: invalid JSON ({exc})")

    manifest = ROOT / "examples" / "production_manifest.example.json"
    if manifest.exists():
        try:
            data = json.loads(manifest.read_text(encoding="utf-8"))
            if not re.fullmatch(r"WW-\d{3,}", data.get("production_id", "")):
                errors.append("Example manifest has invalid production_id")
            if data.get("state") not in {
                "IDEA_CANDIDATE","IDEA_APPROVED","RESEARCH","STORY","PREPRODUCTION",
                "GENERATION","EDITING","QA","RELEASE_APPROVED","PUBLISHED","ARCHIVED",
                "HOLD","REWORK","REJECTED"
            }:
                errors.append("Example manifest has invalid state")
        except Exception as exc:
            errors.append(f"Example manifest invalid JSON ({exc})")

    if not (ROOT / "tests" / "test_project_contracts.py").exists():
        errors.append("Automated contract test file missing")
    if not (ROOT / ".github" / "workflows" / "validate.yml").exists():
        warnings.append("GitHub Actions workflow missing")

    for warning in warnings:
        print("WARN:", warning)
    for error in errors:
        print("FAIL:", error)
    if errors:
        print(f"RESULT: FAIL ({len(errors)} errors)")
        return 1
    print("RESULT: PASS")
    return 0

if __name__ == "__main__":
    sys.exit(check())
