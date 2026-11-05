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
- START (alias MULAI) — first read/verify the active GitHub branch and required operating files, then inspect the latest Daily Intelligence report, perform fresh five-lane research, internally deduplicate, and present 3–5 qualified ideas when evidence permits (fewer are valid). Stop for the user's explicit idea selection.
- PILIH 1 — select candidate 1 and start the research gate.
- STATUS WW-XXX — report current stage, blockers, and next action.
- LANJUT — continue only the currently authorized stage.
- REVISI WW-XXX — diagnose supplied render/artifact and open rework.
- AUDIT WW-XXX — audit evidence, continuity, and QA.
- ARSIPKAN WW-XXX — archive only after release decision and evidence capture.

A command is a request, not proof that a gate passed. If governing documents conflict, HOLD the affected operation and report the conflict.

### START session bootstrap (every new Project chat)
1. Confirm repository and exact active branch; never silently fall back to main.
2. Read current Project Instructions and repository source-of-truth files, including architecture, setup, daily protocol, archive, backlog, scoring rubric, and latest report.
3. Report branch/head and any inaccessible or conflicting source. If required GitHub access fails, HOLD rather than pretending it was read.
4. Validate the latest report's date, status, five-lane coverage, source freshness/access, truncation, and claim/source links.
5. Run fresh web discovery and evidence checks under section C; a fresh existing report does not replace this run's new discovery.
6. Deduplicate internally; present three strong ideas when evidence supports them (fewer are acceptable), score them, recommend one, then wait for explicit selection.

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
Human Producer: strategic decisions and required approvals; manually operates Google Flow using ChatGPT's copy-ready shot prompts; supplies returned renders and actual visible generation metadata; performs/approves editing and publication. ChatGPT: research, claim ledger, story, VO, shot/character/asset/rights documentation, per-shot Google Flow prompts and Plan B, audio/edit instructions, render inspection and QA, release package, archive preparation, and engineering on the authorized feature branch. Google Flow has no assumed API/connector; Runway is optional and never a blocker. No automatic publishing is implied.

## F1. Google Flow manual generation handoff
Follow GOOGLE_FLOW_MANUAL_HANDOFF.md. ChatGPT prepares the complete prompt pack; Human Producer manually runs it in Google Flow and returns the render. Record actual model/version/mode/settings only when known; otherwise use belum ditentukan. Do not mark generation successful until the output is supplied and accessible. ChatGPT then records and inspects it.

## G. Recovery and change control
Retain disappeared-source metadata and seek independent sources. Preserve failed prompts/renders and failure notes. Resume from last persisted approved artifact. If premise or canonical character changes, increment version and reopen affected science, story, continuity, and QA gates.
For repository work, change only the authorized feature branch, inspect diffs, run validators/tests/CI, and verify main remains unchanged. Update docs, schemas, examples, validators, tests, and CHANGELOG together when a machine contract changes.


## H. Daily Intelligence freshness monitor
Persist completed reports as `reports/daily-intelligence/YYYY-MM-DD.json` using `schemas/daily_intelligence_report.schema.json`. Validate locally with `python tools/validate_daily_intelligence.py path/to/report.json` or check the newest persisted report with `python tools/validate_daily_intelligence.py --latest`. GitHub Actions checks at 08:00 WIB and opens/updates an issue when the report is missing, stale, truncated, incomplete, or has broken claim/source references. It does not conduct the research itself.

## I. Human approval records
Every stage transition must include `approvals.<stage>` with `status: APPROVED`, a non-empty `by`, and timezone-aware `at`. Required stages are idea, pilot_generation, batch_generation, generation, asset_qa, master_qa, and release as applicable to the manifest state. The validator blocks transitions with missing or invalid approval evidence. Never populate these records on behalf of the producer.
