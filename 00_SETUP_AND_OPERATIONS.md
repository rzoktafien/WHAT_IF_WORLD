# WHAT IF WORLD — Setup & Operations V3.2

## A. One-time setup
1. Open ChatGPT Project WHAT IF WORLD HQ.
2. Copy 01_INSTRUKSI_PROJECT.md into Project Instructions.
3. Upload operating documents: 02, 02A, 03, 03A, 05, 06, 07, 08, 09, 10, and 11.
4. Read AGENTS.md before asking a coding agent to modify this repository.
5. Ensure web research is available; otherwise mark research blocked.
6. Install dev checks with python -m pip install -r requirements-dev.txt.
7. Run python tools/validate_project.py and python -m unittest discover -s tests -v.

No legacy dossier is assumed to exist in this repository. Preserve external legacy files separately; do not treat them as validated releases.

## B. Session commands
- MULAI — validate latest intelligence report, perform fresh research when required, internally deduplicate, then present 3–5 qualified ideas when evidence permits (fewer are valid).
- PILIH 1 — select candidate 1 and start the research gate.
- STATUS WW-XXX — report current stage, blockers, and next action.
- LANJUT — continue only the currently authorized stage.
- REVISI WW-XXX — diagnose supplied render/artifact and open rework.
- AUDIT WW-XXX — audit evidence, continuity, and QA.
- ARSIPKAN WW-XXX — archive only after release decision and evidence capture.

A command is a request, not proof that a gate passed. If governing documents conflict, HOLD the affected operation and report the conflict.

## C. Daily Intelligence
Check the latest completed report's date/time, observation window, completion status, source freshness/accessibility, coverage across five discovery lanes, source attribution, and truncation. If missing, failed, materially truncated, or older than 7 days, perform fresh research. Internally compare against 05_ARSIP_KONTEN.md and 09_IDEA_BACKLOG.md without exposing internal titles/IDs/comparison. Map findings to HUMAN BODY & MIND, EARTH & COSMOS, or CIVILIZATION & FUTURE. Target 3–5 qualified ideas; fewer are acceptable if evidence is insufficient. Preserve claim-to-source provenance; never claim persistence without a confirmed write.

## D. Character reference workflow
1. Follow 03A_CHARACTER_REFERENCE_BIBLE.md and schemas/character_reference.schema.json.
2. Assign permanent AST-CHAR-### ID.
3. Store canonical image or exact prompt with provenance and rights status.
4. Keep new profiles DRAFT until explicit human approval.
5. Link shots through character_ids and record the exact profile version in character_reference_versions.
6. If canonical reference changes, mark dependent shots STALE and re-review them.

## E. Licensing and commercial readiness
1. Read LICENSING_DECISION_RECORD.md. The selected direction is source-available commercial; this is not a published license.
2. Do not add generic or placeholder license text, and do not claim open-source or commercial-use clearance.
3. Complete ownership/contributor and third-party rights inventory for code, documentation, schemas, prompts, examples, dependencies, media, fonts, music, models, datasets, and research excerpts.
4. Obtain jurisdiction-aware legal drafting and review for the actual license and customer/enterprise agreements.
5. Obtain explicit repository-owner approval of final terms before publishing a LICENSE file or offering commercial permissions.
6. Keep unresolved or uncleared materials out of commercial distributions.

## F. Responsibility split
AI: research synthesis, claim-ledger draft, story, prompts, timing, asset naming, QA checklist, package assembly, and engineering changes on the authorized feature branch.
Human: strategic decisions, idea approval, factual-risk exceptions, rights clearance, canonical character approval, generation operation, render inspection, final edit approval, and publication. No automatic publishing is implied.

## G. Recovery and change control
Retain disappeared-source metadata and seek independent sources. Preserve failed prompts/renders and failure notes. Resume from last persisted approved artifact. If premise or canonical character changes, increment version and reopen affected science, story, continuity, and QA gates.
For repository work, change only the authorized feature branch, inspect diffs, run validators/tests/CI, and verify main remains unchanged. Update docs, schemas, examples, validators, tests, and CHANGELOG together when a machine contract changes.
