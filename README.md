# WHAT IF WORLD — Production Module V3

**Status:** Production-system blueprint + document-driven MVP  
**Target:** Indonesian short-form cinematic science/hypothetical content  
**Primary platform:** TikTok (manual publishing)  
**Version:** 3.0.0

## What this module is

WHAT IF WORLD is a repeatable production system that turns monitored questions and verified evidence into a cinematic, scientifically responsible short video package. It is not just a prompt library, nor does this repository claim to automatically render or publish video.

The module separates editorial intelligence, scientific verification, creative development, pre-production, generation, post-production, quality assurance, release, and archival memory. Every stage has explicit inputs, outputs, acceptance criteria, and a state transition.

## Quick start

1. Copy `01_INSTRUKSI_PROJECT.md` into ChatGPT Project Instructions.
2. Upload the Markdown operating documents (`02` through `11`) to Project Files.
3. Read `00_SETUP_AND_OPERATIONS.md`.
4. Run `python tools/validate_project.py` to validate repository contracts.
5. For a new idea session, require the latest Daily Intelligence report and compare against the archive before ideation.
6. For a selected idea, create a production record from `03_TEMPLATE_PRODUKSI.md`.
7. Do not pass a stage gate without the required evidence and human approval.

## Core operating model

`MONITOR → TRIAGE → RESEARCH → STORY → PRE-PRODUCTION → GENERATE → EDIT → QA → RELEASE → ARCHIVE`

A stage can end in `APPROVED`, `REWORK`, `HOLD`, or `REJECTED`. Human approval is mandatory at idea selection, factual-risk exceptions, and final publication.

## Repository map

- `01_INSTRUKSI_PROJECT.md` — compact system instructions (hard limit 8,000 characters).
- `02_PANDUAN_PRODUKSI_UTAMA.md` — production standard and editorial rules.
- `02A_MODULE_ARCHITECTURE.md` — lifecycle, contracts, roles, states, failure handling.
- `03_TEMPLATE_PRODUKSI.md` — per-video production dossier.
- `05_ARSIP_KONTEN.md` — canon and editorial archive.
- `06_DAILY_INTELLIGENCE_PROTOCOL.md` — daily research protocol.
- `07_SOURCE_AND_CLAIM_LEDGER.md` — evidence, source quality, claim traceability.
- `08_IDEA_SCORING_SYSTEM.md` — idea evaluation and decision thresholds.
- `09_IDEA_BACKLOG.md` — unresearched idea queue.
- `10_ASSET_AND_SHOT_REGISTER.md` — continuity and media asset registry.
- `11_QA_AND_RELEASE_PROTOCOL.md` — objective gates and release checklist.
- `12_GITHUB_REFERENCE_REVIEW.md` — design references and adoption decisions.
- `schemas/` — JSON Schemas for machine-readable records.
- `examples/` — sample production manifest.
- `tools/validate_project.py` — dependency-free repository validator.\n- `tools/validate_manifest.py` — production-record and release-gate validator.
- `tests/` — automated contract tests.
- `.github/workflows/validate.yml` — CI validation on pushes and pull requests.

## What is intentionally not automated yet

- Google Flow/Veo generation, ElevenLabs/TTS rendering, CapCut editing, TikTok publishing.
- Trend platform access that requires a logged-in account or proprietary analytics.
- Claims that a rendered asset passed visual QA without inspecting the actual render.
- License/rights clearance for third-party footage, music, voices, fonts, and models.

These remain explicit manual or integration steps. The module records their status rather than pretending they occurred.

## Versioning

- `MAJOR`: incompatible workflow or record schema changes.
- `MINOR`: new stage, artifact, schema field, or optional production capability.
- `PATCH`: clarifications, typo fixes, and non-breaking QA improvements.

See `CHANGELOG.md`.
