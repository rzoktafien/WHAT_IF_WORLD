# WHAT IF WORLD — Setup & Operations V3.2

## A. One-time setup
1. Open ChatGPT Project WHAT IF WORLD HQ.
2. Copy 01_INSTRUKSI_PROJECT.md into Project Instructions.
3. Upload operating documents present in this repository: 02, 02A, 03, 03A, 05, 06, 07, 08, 09, 10, and 11.
4. Read AGENTS.md before asking a coding agent to modify this repository.
5. Ensure web research is available; otherwise mark research blocked.
6. Install dev checks with `python -m pip install -r requirements-dev.txt`.
7. Run `python tools/validate_project.py` and `python -m unittest discover -s tests -v`.

No legacy dossier is assumed to exist in this repository. Preserve any external legacy file separately; do not treat it as a validated release.

## B. Session commands
- MULAI — current intelligence intake, archive comparison, then 3–5 qualified ideas.
- PILIH 1 — select candidate 1 and start the research gate.
- STATUS WW-XXX — report current stage, blockers, and next action.
- LANJUT — continue current stage.
- REVISI WW-XXX — diagnose supplied render/artifact and open rework.
- AUDIT WW-XXX — audit evidence, continuity, and QA.
- ARSIPKAN WW-XXX — archive only after release decision and evidence capture.

A command is a request, not proof that a gate passed.

## C. Daily Intelligence
Retrieve the latest completed report; check report date, evidence dates, source coverage, and truncation. If older than 7 days, missing, failed, or materially truncated, perform fresh research. Compare against 05_ARSIP_KONTEN.md and 09_IDEA_BACKLOG.md.

## D. Character reference workflow
1. Follow 03A_CHARACTER_REFERENCE_BIBLE.md and schemas/character_reference.schema.json.
2. Assign permanent AST-CHAR-### ID.
3. Store canonical image or exact prompt with provenance and rights status.
4. Keep new profiles DRAFT until explicit human approval.
5. Link shots through character_ids and record the exact profile version in character_reference_versions.
6. If canonical reference changes, mark dependent shots STALE and re-review them.

## E. Licensing and commercial readiness
1. Read LICENSING_DECISION_RECORD.md. The selected direction is source-available commercial; this is not yet a published license.
2. Do not add generic or placeholder license text, and do not claim open-source or commercial-use clearance.
3. Complete an ownership/contributor and third-party rights inventory for code, documentation, schemas, prompts, examples, dependencies, media, fonts, music, models, datasets, and research excerpts.
4. Obtain jurisdiction-aware legal drafting and review for the actual license and any customer/enterprise agreements.
5. Obtain explicit repository-owner approval of the final terms before publishing a LICENSE file or offering commercial permissions.
6. Keep unresolved or uncleared materials out of commercial distributions.

## F. Responsibility split
AI: research synthesis, claim-ledger draft, story, prompts, timing, asset naming, QA checklist, package assembly.
Human: idea approval, factual-risk exceptions, rights clearance, generation operation, render inspection, final edit approval, publication. No automatic publishing is implied.

## G. Recovery
Retain disappeared-source metadata and seek independent sources. Preserve failed prompts/renders and failure notes. Resume from last persisted approved artifact. If premise or canonical character changes, increment version and reopen affected science, story, continuity, and QA gates.
