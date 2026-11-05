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
PREPRODUCTION (assets + shot plan + rights + copy-ready prompts)
       |
       v
PILOT_GENERATION (manual Google Flow handoff + render return) --pilot fail--> PLAN_B / REWORK
       |
       v
BATCH_GENERATION (manual Google Flow handoff + render return)
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
| Pilot | prompts + references | ChatGPT prompt pack → Human Producer manually runs Google Flow → returned pilot render + attempt log | actual render inspected; pilot explicitly approved | Human operates Flow and approves pilot |
| Generation | approved pilot plan + ChatGPT prompt pack | Human Producer manually runs Google Flow; returned renders + generation log | each required shot accounted for; only returned files count as generated | Human operates Flow; ChatGPT records and inspects returned renders |
| Editing | approved renders + audio | edit timeline + master candidate | sync, timing, export spec pass | Human editor |
| QA | master candidate + dossier | QA report + blockers | score threshold and zero blockers | Human review |
| Release | QA report + rights + metadata | release package | approval, disclosure, metadata complete | Human final approval |
| Archive | released package | immutable archive record | versions, links, lessons stored | Human confirms |

## 4. State transition rules
- IDEA_CANDIDATE → IDEA_APPROVED: only explicit user selection.
- RESEARCH → STORY: all critical claims are SUPPORTED/QUALIFIED or removed; no critical claim remains UNVERIFIED.
- STORY → PREPRODUCTION: premise, causal chain, duration, VO budget, and risk framing accepted.
- PREPRODUCTION → PILOT_GENERATION: every shot has ID, purpose, copy-ready Google Flow prompt, asset references, duration, Plan B, and rights status. ChatGPT prepares prompts; Human Producer manually operates Flow.
- PILOT_GENERATION → BATCH_GENERATION: returned pilot render is inspected and explicitly approved; never infer submission, success, or approval from prompt readiness or file existence.
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
Phase 3: optional adapters for genuinely authorized API workflows, TTS, FFmpeg/Remotion, and OTIO interchange. Google Flow manual generation is an intentional supported operating mode and does not require an adapter.
Phase 4: orchestration with n8n/LangGraph only if manual operations become a bottleneck.
Do not adopt infrastructure before workflow and record contracts stabilize.

## 10. Machine-enforced release check
Run python tools/validate_manifest.py path/to/manifest.json --release-gate before release. It blocks unresolved critical claims, uncleared asset rights, unapproved shots, missing human approval, missing final master checksum, or missing caption/disclosure. This structural gate does not replace human viewing/listening or scientific review.

## 11. Google Flow prompt and audio contract (V3.2)
Every visual shot packet must contain three independent copy-ready prompt fields: keyframe_image_prompt, video_prompt, and audio_prompt. The keyframe prompt establishes the still-image composition and becomes the same-shot visual reference for video generation. The video prompt animates that reference with one principal action and one camera move. The audio prompt specifies diegetic ambience/SFX for that shot only; music and VO are separate editorial tracks by default.

The Human Producer manually operates Google Flow. The system must not assume that every account, model, or mode exposes identical image, video, or audio features. Record the exact UI-displayed model/mode/settings when available. If audio generation is unavailable, retain the audio prompt and record the limitation plus a manual SFX fallback; do not mark audio as generated.

Preproduction exit criteria now require: (a) a keyframe prompt for every shot, (b) video prompt referencing the selected same-shot keyframe, (c) separate audio prompt or explicit silence decision, (d) Plan B, (e) continuity and rights status, and (f) measurable acceptance criteria. Pilot gate remains unchanged: inspect actual returned keyframe/video/audio outputs and obtain explicit human pilot approval before batch generation.

Music selection is deferred to edit/posting as one coherent master track or deliberate cues; it is not embedded in per-shot Google Flow audio prompts. VO is recorded/generated separately and mixed in edit.


## 12. START interaction contract (V3.2)
START is the single-command alias of MULAI and is the entry point for every new Project chat. Its deterministic order is: (1) verify repository identity and read the active development branch ref/head; (2) read current Project Instructions plus the required source-of-truth documents (AGENTS, setup, architecture, daily protocol, archive, backlog, scoring rubric); (3) fetch and validate the latest persisted Daily Intelligence report; (4) perform fresh five-lane web discovery and source/claim checks; (5) internally deduplicate against archive/backlog; (6) produce three qualified idea cards when evidence permits, fewer if quality threshold is not met; (7) recommend one with trade-offs and stop for explicit human selection.

GitHub access is a hard startup dependency for repository-state claims. If the connector is unavailable, the target branch cannot be read, or required files are missing/conflicting, report HOLD with the exact limitation; do not silently use main, stale conversation context, or pretend the repository was read. START does not approve an idea or authorize research-to-story progression. A command triggers the workflow; only evidence and explicit approvals advance gates.

The persisted report freshness monitor is a separate scheduled validator. It does not perform discovery. Every START run performs fresh discovery as required by 06_DAILY_INTELLIGENCE_PROTOCOL.md even when the persisted report is current.
