# WHAT IF WORLD — Global Media & Production System

**Development line:** V3.2 foundation plus global media launch strategy  
**Baseline documented release:** V3.0.0  
**Brand promise:** Explore the Impossible. Understand the Real.  
**Market:** Indonesia first; global-ready editorial packaging  
**Channels:** TikTok, YouTube Shorts/long-form, Instagram Reels, website  
**Business tracks:** digital media, production studio, original IP

## What this project is

WHAT IF WORLD is an evidence-led cinematic science, mystery, and future documentary brand supported by a repeatable production system. It turns questions into researched stories, production-ready packages, multi-platform adaptations, and a searchable content library.

The repository is a document-driven blueprint and MVP. It does not claim that video generation, audio rendering, editing, social publishing, website deployment, or account analytics are automatically integrated.

## Quick start

1. Read AGENTS.md and 00_SETUP_AND_OPERATIONS.md.
2. Copy 01_INSTRUKSI_PROJECT.md into the dedicated ChatGPT Project Instructions.
3. Upload the operating and strategy documents listed in the setup guide.
4. Install development checks with `python -m pip install -r requirements-dev.txt`.
5. Run `python tools/validate_project.py`.
6. Run `python -m unittest discover -s tests -v`.
7. Validate a production record with `python tools/validate_manifest.py path/to/manifest.json`.
8. Never pass a stage gate without evidence and human approval.

## Core operating model

`MONITOR → TRIAGE → RESEARCH → STORY → PRE-PRODUCTION → GENERATE → EDIT → QA → RELEASE → ARCHIVE`

## Repository map

- AGENTS.md — coding-agent instructions.
- 01_INSTRUKSI_PROJECT.md — compact project instructions.
- 02_PANDUAN_PRODUKSI_UTAMA.md — production/editorial standards.
- 02A_MODULE_ARCHITECTURE.md — lifecycle, contracts, roles, recovery.
- 03_TEMPLATE_PRODUKSI.md — production dossier.
- 03A_CHARACTER_REFERENCE_BIBLE.md — character identity, reference, approval, continuity.
- 05–09 — archive, intelligence, claim ledger, idea scoring, backlog.
- 10_ASSET_AND_SHOT_REGISTER.md — asset and shot IDs.
- 11_QA_AND_RELEASE_PROTOCOL.md — quality and release gates.
- 12_GITHUB_REFERENCE_REVIEW.md — architecture references.
- 13_GLOBAL_EDITORIAL_STRATEGY_2026_2030.md — brand, audience, editorial pillars, franchises.
- 14_90_DAY_LAUNCH_AND_REVENUE_PLAN.md — execution phases, publishing cadence, monetization.
- 15_PLATFORM_DISTRIBUTION_AND_ANALYTICS.md — channel roles, website architecture, analytics, release checklist.
- LICENSING_DECISION_RECORD.md — owner-selected licensing direction and remaining release gates; not a license grant.
- RIGHTS_AND_PROVENANCE_REGISTER.md — ownership and third-party rights audit work queue; no item is pre-cleared.
- schemas/ — JSON Schema contracts.
- examples/ — sample manifest.
- tools/ — dependency-free operational validators.
- tests/ — automated contract and JSON Schema tests.
- requirements-dev.txt — pinned development-only schema validation dependency.
- .github/workflows/validate.yml — CI on push, pull request, and manual dispatch.

## Not yet integrated

Google Flow/Veo generation, TTS rendering, video editing, TikTok/YouTube/Instagram publishing, website hosting/deployment, account-level analytics, third-party rights clearance, and actual rendered-media inspection remain manual or require separately authorized integrations. Do not claim otherwise.

## Licensing and commercial use

**Selected direction: source-available commercial.** This is a product/licensing direction recorded in LICENSING_DECISION_RECORD.md, not a published license grant. No LICENSE file or custom license terms are issued by this branch. Do not describe this repository as open source, commercially licensed, or cleared for unrestricted commercial use. Public source visibility is not a substitute for explicit license terms. Complete ownership/contributor and third-party provenance review, jurisdiction-aware legal drafting, and explicit owner approval before a license is published or commercial permissions are offered. Third-party code, assets, fonts, music, models, datasets, and references remain subject to their own terms.

## Versioning

MAJOR: incompatible workflow/schema changes. MINOR: new stages/artifacts/capabilities. PATCH: non-breaking clarifications and QA improvements. See CHANGELOG.md.
