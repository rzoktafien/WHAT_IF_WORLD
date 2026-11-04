# WHAT IF WORLD — Setup & Operations V3

## A. One-time setup

1. Open ChatGPT Project **WHAT IF WORLD HQ**.
2. Replace Project Instructions with the complete contents of `01_INSTRUKSI_PROJECT.md`.
3. Upload the operating documents `02`, `02A`, `03`, `05`, `06`, `07`, `08`, `09`, `10`, and `11`.
4. Keep `04_WW-001_PAKET_PRODUKSI_V2.md` as a legacy reference/example; it is not a validated rendered release.
5. Ensure web research is available. If unavailable, mark research as blocked; do not invent evidence.
6. Run the repository validator if working from GitHub/local files: `python tools/validate_project.py`.

## B. Session commands

- `MULAI` — run current intelligence intake, archive comparison, then offer 3–5 qualified ideas.
- `PILIH 1` — approve candidate 1 and start the research gate.
- `STATUS WW-XXX` — report the production record's current stage, blockers, and next action.
- `LANJUT` — continue the current stage without restarting earlier work.
- `REVISI WW-XXX` — diagnose a supplied render or artifact and open a rework cycle.
- `AUDIT WW-XXX` — run the evidence, continuity, and QA audit.
- `ARSIPKAN WW-XXX` — archive only after release decision and evidence capture.

A command is a user request, not proof that the requested stage has passed.

## C. Daily Intelligence

The scheduled daily automation is an input source. It is not itself an approval gate. At the beginning of an ideation session:
1. Retrieve the latest completed report.
2. Check report date, evidence dates, source coverage, and any truncated output.
3. If older than 7 days, missing, failed, or truncated in a material section, perform fresh research.
4. Compare candidates with production archive and backlog.
5. Preserve report/source IDs and URLs in the idea record.

## D. Working files and versions

Every production uses a stable ID `WW-###` and version `vMAJOR.MINOR.PATCH`. Never overwrite the only copy of a released dossier. Save revisions as a new version and preserve the previous release candidate.

Suggested folder layout:
```text
WHAT_IF_WORLD/
  intelligence/YYYY-MM-DD/
  productions/WW-003/
    dossier/
    research/
    references/
    keyframes/
    renders/
    audio/
    edit/
    qa/
    release/
  archive/
  schemas/
```

## E. Responsibility split

AI: research synthesis, evidence ledger draft, story, prompt drafting, timing calculations, asset naming, QA checklist, package assembly.
Human: idea approval, source-risk exceptions, rights clearance, generation tool selection, render review, final edit approval, TikTok upload and publication.
A person must explicitly approve publication. No automatic publishing is implied.

## F. Recovery

If a source disappears, retain the citation metadata and mark it unavailable; seek an independent source.
If a prompt/render fails, retain the failed output and log the failure; do not silently replace it.
If a stage is interrupted, resume from the last persisted approved artifact; do not regenerate accepted stages without a reason.
If the premise changes, increment the dossier version and re-open affected science, story, continuity, and QA gates.
