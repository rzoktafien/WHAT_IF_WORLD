# AGENTS.md — WHAT IF WORLD

## 1. Project identity
WHAT IF WORLD is a document-driven, stage-gated production system for Indonesian short-form cinematic science and hypothetical content. The default editorial style is realistic cinematic/documentary. This repository is a production blueprint and workflow record; do not claim that external video generation, editing, or publishing has occurred unless an integration or human confirmation proves it.

## 2. Source-of-truth hierarchy
Before changing project behavior, read the relevant repository documents. Use this order:
1. `02A_MODULE_ARCHITECTURE.md` for module boundaries, stage contracts, state transitions, IDs, and recovery rules.
2. `01_INSTRUKSI_PROJECT.md` for operating instructions and hard editorial constraints.
3. The relevant domain document (`02_PANDUAN_PRODUKSI_UTAMA.md`, `03_TEMPLATE_PRODUKSI.md`, `05_ARSIP_KONTEN.md`, `06_DAILY_INTELLIGENCE_PROTOCOL.md`, `07_SOURCE_AND_CLAIM_LEDGER.md`, `08_IDEA_SCORING_SYSTEM.md`, `09_IDEA_BACKLOG.md`, `10_ASSET_AND_SHOT_REGISTER.md`, `11_QA_AND_RELEASE_PROTOCOL.md`).
4. `README.md`, `00_SETUP_AND_OPERATIONS.md`, and `CHANGELOG.md` for setup, navigation, and release history.
5. JSON Schemas, examples, tools, and tests for machine-enforced contracts.

If documents conflict, do not silently choose or rewrite the canonical rule. Identify the conflict, explain its impact, and propose a documented resolution. Preserve historical records.

## 3. Change-control rules
- Never commit directly to `main` for feature work, broad edits, or structural changes. Create a focused branch from the current `main`.
- Keep changes scoped, reviewable, and reversible. Do not bundle unrelated refactors.
- Do not overwrite released dossiers or historical evidence. Create a new version and preserve the previous version.
- Update `CHANGELOG.md` for user-visible behavior, workflow, schema, or documentation changes.
- Update schemas, examples, validators, tests, and documentation together when a contract changes.
- Do not claim a branch, commit, push, test, render, or release succeeded until the relevant tool or command confirms it.
- Do not add credentials, API keys, tokens, private user data, or secrets to the repository.

## 4. Character and visual reference continuity
For every recurring or identity-critical character:
- Create or maintain a stable character asset record with a unique `AST-###` ID in the asset/shot register or the designated character-reference document.
- Record only approved, continuity-relevant attributes: approximate age range, facial structure, hair, distinguishing features, wardrobe, body proportions, voice traits (if used), and prohibited identity drift.
- Maintain a canonical visual reference image or a clearly identified reference prompt when an image cannot be stored. Record provenance, rights status, version, and storage location.
- Separate invariant identity traits from scene-specific changes such as expression, pose, lighting, damage, or wardrobe changes.
- Link every shot featuring the character to the same asset ID and the applicable reference version.
- Do not invent a canonical character, backstory, or appearance and present it as approved. Mark proposed references as DRAFT until the human producer approves them.
- For one-off background people, avoid unnecessary character dossiers; apply the full protocol when continuity or narrative identity matters.

## 5. Production and scientific integrity
- Preserve the pipeline: MONITOR → TRIAGE → RESEARCH → STORY → PRE-PRODUCTION → GENERATE → EDIT → QA → RELEASE → ARCHIVE.
- Respect explicit stage gates and human approvals. A user command is not proof that a gate passed.
- Distinguish verified facts, extrapolations, and fictional assumptions. Every critical claim must be traceable to evidence or removed/qualified.
- Never fabricate sources, measurements, tool capabilities, generation settings, test results, or rights clearance.
- Keep prompts tool-specific. If model, mode, duration, aspect ratio, or account capability is unknown, mark it as undetermined and verify before use.
- Treat render quality as unverified until the actual generated asset is inspected. Plan QA is not render QA.
- Do not bypass mandatory blockers or human release approval.

## 6. Engineering and validation
- Prefer the repository's existing dependency-free Python validation tools and established conventions.
- Run `python tools/validate_project.py` and the relevant test suite after changes to repository contracts or production records.
- For manifest changes, run `python tools/validate_manifest.py <path>`; use `--release-gate` only when evaluating an actual release candidate.
- Keep JSON valid and conformant to the schema. Do not weaken validation merely to make an invalid record pass.
- If a test cannot be run, state exactly why; do not report it as passed.
- Keep GitHub Actions validation green; diagnose failures rather than suppressing checks.

## 7. Documentation and communication
- Write user-facing operational documentation in Indonesian unless an existing document's language or audience calls for English.
- Use consistent IDs, version numbers, status labels, and ISO 8601 timestamps with timezone.
- Record decisions, assumptions, unresolved questions, and migration impact explicitly.
- Keep changes understandable to a human producer who may not be a software engineer.

## 8. Definition of done
A change is complete only when:
1. The intended files are changed on the correct feature branch.
2. Related documentation, schemas, examples, and tests are aligned.
3. Relevant validation/tests pass, or unrun checks are clearly reported.
4. The diff is scoped and contains no secrets or accidental generated artifacts.
5. The commit and branch state are verified on GitHub.
6. No unapproved change has been applied to `main`.
