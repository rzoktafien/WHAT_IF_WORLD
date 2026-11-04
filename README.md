# WHAT IF WORLD — Production Module

**Development line:** V3.2 foundation (feature branch)  
**Baseline documented release:** V3.0.0  
**Target:** Indonesian short-form cinematic science/hypothetical content  
**Primary platform:** TikTok (manual publishing)

## What this module is
WHAT IF WORLD is a repeatable production system turning monitored questions and verified evidence into cinematic, scientifically responsible short-video packages. It is a document-driven blueprint/MVP; it does not claim to automatically render or publish video.

## Quick start
1. Read AGENTS.md and 00_SETUP_AND_OPERATIONS.md.
2. Copy 01_INSTRUKSI_PROJECT.md into ChatGPT Project Instructions.
3. Upload operating documents listed in the setup guide.
4. Install development checks with `python -m pip install -r requirements-dev.txt`.
5. Run `python tools/validate_project.py`.
6. Run `python -m unittest discover -s tests -v`.
7. Validate a production record with `python tools/validate_manifest.py path/to/manifest.json`.
8. Never pass a stage gate without evidence and human approval.

## Core operating model
`MONITOR → TRIAGE → RESEARCH → STORY → PRE-PRODUCTION → GENERATE → EDIT → QA → RELEASE → ARCHIVE`

## Repository map
- AGENTS.md — coding-agent instructions.
- 01_INSTRUKSI_PROJECT.md — compact project instructions (8,000-character limit).
- 02_PANDUAN_PRODUKSI_UTAMA.md — production/editorial standards.
- 02A_MODULE_ARCHITECTURE.md — lifecycle, contracts, roles, recovery.
- 03_TEMPLATE_PRODUKSI.md — production dossier.
- 03A_CHARACTER_REFERENCE_BIBLE.md — character identity, reference, approval, continuity.
- 05–09 — archive, intelligence, claim ledger, idea scoring, backlog.
- 10_ASSET_AND_SHOT_REGISTER.md — asset and shot IDs.
- 11_QA_AND_RELEASE_PROTOCOL.md — quality and release gates.
- 12_GITHUB_REFERENCE_REVIEW.md — architecture references.
- schemas/ — JSON Schema contracts.
- examples/ — sample manifest.
- tools/ — dependency-free operational validators.
- tests/ — automated contract and JSON Schema tests.
- requirements-dev.txt — pinned development-only schema validation dependency.
- .github/workflows/validate.yml — CI on push, pull request, and manual dispatch.

## Not automated
Google Flow/Veo generation, TTS rendering, editing, TikTok publishing, account-level trend analytics, third-party rights clearance, and actual rendered-media inspection remain manual or require separately approved integrations.

## Licensing and commercial use
No LICENSE file is granted by this development branch. Do not assume third-party references, assets, fonts, music, models, or source code are cleared for commercial use. The repository owner must select and review a distribution/license policy before public redistribution or commercial packaging.

## Versioning
MAJOR: incompatible workflow/schema changes. MINOR: new stages/artifacts/capabilities. PATCH: non-breaking clarifications and QA improvements. See CHANGELOG.md.
