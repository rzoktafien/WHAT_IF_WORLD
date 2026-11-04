# WHAT IF WORLD — MODULE ARCHITECTURE & CONTRACTS

## 1. Module boundary
The production module owns the editorial-to-release workflow and records proving what happened. It does not own external rendering services, platform analytics, social credentials, or publication execution unless a future integration is explicitly built and approved.

## 2. Pipeline graph
```text
DAILY_INTELLIGENCE
       |
       v
IDEA_TRIAGE --reject--> BACKLOG/REJECTED
       |
   human approval
       v
RESEARCH_AND_CLAIM_LEDGER --evidence failure--> HOLD/RESEARCH
       |
       v
STORY_DESIGN --causality/story failure--> REWORK
       |
       v
PREPRODUCTION (assets + shot plan + rights)
       |
       v
PILOT_GENERATION --pilot fail--> PLAN_B / REWORK
       |
       v
BATCH_GENERATION
       |
       v
EDIT_ASSEMBLY
       |
       v
QA (blocker? yes -> REWORK; unresolved rights/science -> HOLD)
       |
 human release approval
       v
RELEASE_PACKAGE -> PUBLISHED -> ARCHIVED
```

## 3. Stage contracts
| Stage | Required inputs | Output artifact | Exit criteria | Approval |
|---|---|---|---|---|
| Intelligence | dated report, source coverage | intelligence brief | evidence dates/limits recorded | AI may compile |
| Idea triage | brief + archive + backlog | idea cards + scores | no duplicate; premise feasible | Human selects |
| Research | selected idea | claim ledger + source register | critical claims supported; uncertainty explicit | AI drafts; human reviews high-risk |
| Story | approved claims | beat sheet + VO draft | causal chain coherent; word/time fit | Human if premise materially changes |
| Preproduction | story | bible, assets, shotlist, rights log | every shot traceable to assets and claims | AI drafts |
| Pilot | prompts + references | pilot renders + failure log | pilot meets shot acceptance criteria | Human inspects |
| Generation | approved pilot plan | all shot renders + generation log | all required shots accounted for | Human operates generator |
| Editing | approved renders + audio | edit timeline + master candidate | sync, timing, export spec pass | Human editor |
| QA | master candidate + dossier | QA report + blockers | score threshold and zero blockers | Human review |
| Release | QA report + rights + metadata | release package | approval, disclosure, metadata complete | Human final approval |
| Archive | released package | immutable archive record | versions, links, lessons stored | Human confirms |

## 4. State transition rules
- IDEA_CANDIDATE → IDEA_APPROVED: only explicit user selection.
- RESEARCH → STORY: all critical claims are SUPPORTED/QUALIFIED or removed; no critical claim remains UNVERIFIED.
- STORY → PREPRODUCTION: premise, causal chain, duration, VO budget, and risk framing accepted.
- PREPRODUCTION → PILOT_GENERATION: every shot has ID, purpose, prompt, asset references, duration, Plan B, and rights status.
- PILOT_GENERATION → BATCH_GENERATION: pilot inspected and approved; never infer approval from file existence.
- EDITING → QA: planned shots are used, intentionally omitted, or marked failed; timeline and audio map complete.
- QA → RELEASE_APPROVED: zero blockers, score ≥85, rights cleared, disclosure prepared, human approval.
- RELEASE_APPROVED → PUBLISHED: only after actual platform publication is confirmed.
- PUBLISHED → ARCHIVED: capture URL, publish date, final master checksum, metadata, and performance snapshot if available.

## 5. Required stable IDs
- Production: WW-###
- Idea candidate: IDEA-YYYYMMDD-NN
- Claim: CLM-###
- Source: SRC-###
- Character: AST-CHAR-###
- Location: AST-LOC-###
- Prop: AST-PROP-###
- Reference: AST-REF-###
- Keyframe: AST-KF-###
- Video: AST-VIDEO-###
- Audio: AST-AUDIO-###
- Master: AST-MASTER-###
- Shot: SH-###
- Generation attempt: GEN-SH-###-NN
- Defect: BUG-###
- Release: REL-WW-###-vX.Y

IDs remain stable across revisions and are never recycled. Do not use generic AST-### for typed assets. Revisions increment artifact versions; they do not reuse IDs for different semantic objects.

## 6. Artifact contract
Every artifact records id, production_id or idea_id, version, status, created_at, updated_at, owner, source_refs, approval, and change_note where applicable. Dates use ISO 8601 with timezone. Timecodes use integer frames or HH:MM:SS.mmm; do not mix decimal comma and decimal point.

Execution provenance is represented by `schemas/generation_attempt.schema.json`, `schemas/media_asset.schema.json`, and `schemas/edit_timeline.schema.json`, referenced from optional `generation_attempts`, `media_assets`, and `edit_timeline` manifest fields. A generation success record must point to an output asset; an asset must carry a checksum and provenance; timeline clips reference media IDs and frame ranges. Schema validity is not proof of completed rendering or media availability.


Every artifact records id, production_id or idea_id, version, status, created_at, updated_at, owner, source_refs, approval, and change_note where applicable. Dates use ISO 8601 with timezone. Timecodes use integer frames or HH:MM:SS.mmm; do not mix decimal comma and decimal point.

## 7. Role boundaries
- AI Researcher: collect and compare evidence; no source invention.
- Science Reviewer: challenge mechanisms, units, timescales, and causal claims.
- Creative Director: select narrative angle and pacing.
- Prompt/Asset Engineer: translate shot intent into tool-specific prompts and references.
- Editor: assemble media and audio.
- QA Reviewer: inspect deliverables against evidence-based checklists.
- Human Producer: approve idea, risk exceptions, canonical characters, and release.
One AI may perform multiple roles, but records must show which checks actually occurred. Do not simulate independent review by changing role labels.

## 8. Recovery and idempotency
- A retry creates a new generation attempt ID; never overwrite prior output.
- If an accepted upstream artifact changes, mark downstream artifacts STALE and list revalidation needs.
- Do not rerun completed research solely because an unrelated shot failed.
- Preserve rejected/failed attempts with failure reasons.
- If interrupted, resume from last saved artifact/state; if unknown, reconcile before proceeding.
- Never mark an action complete from request or intention alone.

## 9. Minimum viable implementation
Phase 1: documents + JSON records + validator + manual gates.
Phase 2: asset storage conventions, shot/render log, automated metadata checks, CI.
Phase 3: optional adapters for ComfyUI/API workflows, TTS, FFmpeg/Remotion, and OTIO interchange.
Phase 4: orchestration with n8n/LangGraph only if manual operations become a bottleneck.
Do not adopt infrastructure before workflow and record contracts stabilize.

## 10. Machine-enforced release check
Run python tools/validate_manifest.py path/to/manifest.json --release-gate before release. It blocks unresolved critical claims, uncleared asset rights, unapproved shots, missing human approval, missing final master checksum, or missing caption/disclosure. This structural gate does not replace human viewing/listening or scientific review.
