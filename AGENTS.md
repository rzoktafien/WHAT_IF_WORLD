# AGENTS.md — WHAT IF WORLD

## Project identity
WHAT IF WORLD is a document-driven, stage-gated production system for Indonesian short-form cinematic science/hypothetical content. This repository is a production blueprint, not proof that external rendering, editing, or publishing occurred.

## Source of truth
Read 02A_MODULE_ARCHITECTURE.md and 01_INSTRUKSI_PROJECT.md first, then relevant domain documents. Character identity and continuity are governed by 03A_CHARACTER_REFERENCE_BIBLE.md and 10_ASSET_AND_SHOT_REGISTER.md. Machine contracts live in schemas/, examples/, tools/, and tests/. Identify conflicts; do not silently resolve them.

## Change control
- Feature work uses a branch from current main; never commit feature work directly to main.
- Keep changes scoped, reversible, and reviewable.
- Preserve released dossiers and historical evidence; version revisions.
- Update docs, schemas, examples, validators, tests, and CHANGELOG.md together when contracts change.
- Never claim actions/tests/renders/uploads/releases succeeded without tool evidence.
- Never add credentials, tokens, secrets, or private user data.

## Character reference
- Use permanent AST-CHAR-### IDs; never generic AST-### for a character.
- Profiles follow schemas/character_reference.schema.json and 03A_CHARACTER_REFERENCE_BIBLE.md.
- Separate identity invariants from wardrobe, pose, expression, lighting, and scene state.
- Keep new references DRAFT/REVIEW until explicit human approval.
- Link shots through shots[].character_ids and record the profile version used.
- Canonical reference changes invalidate dependent continuity checks; mark affected shots STALE.
- Record provenance and rights. Do not use real-person likeness/voice without documented authority.

## Scientific and production integrity
- Preserve MONITOR → TRIAGE → RESEARCH → STORY → PRE-PRODUCTION → GENERATE → EDIT → QA → RELEASE → ARCHIVE.
- Separate FACT, EXTRAPOLATION, and FICTIONAL_ASSUMPTION.
- Critical claims need traceable sources; unsupported claims must be qualified, removed, or held.
- Do not invent tool capabilities, evidence, metrics, rights clearance, or test results.
- Plan QA is not render QA. Human approval is mandatory at required gates and final publication.

## Engineering and validation
Run `python tools/validate_project.py`, `python -m unittest discover -s tests -v`, and `python tools/validate_manifest.py path/to/manifest.json`. The release gate blocks unresolved critical claims, unknown references, uncleared rights, unapproved shots/characters, missing human approval, and missing final-master evidence. Do not weaken tests to make a build green.

## Definition of done
Correct feature branch; consistent docs/schema/code; tests and CI verified; no secrets; branch/commit verified; main unchanged until reviewed and merged.
