## [Unreleased] — Connected provider capability audit (2026-11-06)
- Recorded the connected Runway workspace as image-generation capable only: no video, speech, music/SFX models or saved workflows were exposed; recent images were not mapped to project assets.
- Recorded the Canva design inventory and the current plan/trial restriction returned for video production; no project video timeline or render was verified.
- Kept Phase 2 PARTIAL, Phase 3 NOT STARTED, and Phase 4 DEFERRED; no media generation, editing, or publication was executed.

## [Unreleased] — Repository audit and TikTok delivery contract
- Added a mandatory TikTok cover-image prompt, exact Indonesian cover overlay, caption/description, hashtags, pinned comment and CTA to the production template and WW-005 delivery artifacts.
- Required the complete prompt and metadata package to be delivered directly in chat; GitHub remains the canonical archive, not a user-facing prompt retrieval task.
- Updated README and compact Project Instructions to match the approval-driven handoff.
- Removed the stale root validation snapshot tied to an older feature-branch commit; GitHub Actions runs on the current branch/PR are the authoritative engineering evidence.

## [Unreleased] — CI remediation for approval-driven handoff
- Moved detailed auto-advance rules into `APPROVAL_DRIVEN_PRODUCTION_HANDOFF.md` to keep `01_INSTRUKSI_PROJECT.md` within the repository's 8,000-character contract limit.
- Kept the short mandatory progression summary in Project Instructions and linked the detailed contract from setup and AGENTS.

## [Unreleased] — Approval-driven production handoff
- STORY approval now automatically advances the AI through the complete PRE-PRODUCTION work package and copy-ready prompt pack; no extra LANJUT or PRE-PRODUCTION approval prompt is required.
- Assigned prompt writing, continuity/asset/shot documentation, supporting original still/reference generation when tools permit, subtitles/timecodes, edit instructions, and QA/release checklists to ChatGPT.
- Kept Google Flow execution manual for the Human Producer and retained all required human approval, rights, safety, pilot, media-inspection, and final-release gates.
- Distinguished prompt-pack readiness from generation authorization and completed renders; unavailable tools or unresolved rights remain explicit blockers.

# Changelog

## [Unreleased] — WW-005 STORY approval and pre-production
- Recorded explicit Human Producer approval of WW-005 STORY and VO master (2026-11-05T17:08:00+07:00).
- Added the complete eight-shot pre-production plan, typed keyframe/video/audio asset allocations, continuity and rights registers, subtitle map, and provisional edit timeline.
- Added separate copy-ready Google Flow keyframe, video, and per-shot audio prompts with Plan B for all eight shots.
- Kept Google Flow execution manual; no generation, render, audio output, editing, or rights clearance is claimed.
- Pilot generation is limited to SH-001 and SH-003; batch generation remains gated on returned render inspection and explicit producer approval.

## [Unreleased] — START GitHub-first session bootstrap
- Added START as the one-word alias of MULAI for new Project chats.
- Required repository/active-branch verification and source-of-truth reads before Daily Intelligence.
- Required latest-report inspection, fresh five-lane discovery, internal archive/backlog deduplication, official scoring, three qualified ideas when evidence permits, one recommendation, and an explicit human selection stop.
- Added a HOLD path when GitHub/branch/source documents cannot be verified; the scheduled freshness monitor is explicitly not treated as a research agent.


## [Unreleased] — Google Flow manual generation handoff
- Documented the responsibility split: ChatGPT prepares per-shot prompt packs and Plan B; the Human Producer manually operates Google Flow and returns renders for inspection.
- Clarified that Google Flow has no assumed API/connector, Runway is optional, and TTS/music/editing are not claimed as automated.
- Extended generation-attempt records with manual execution mode, aspect ratio, duration, references, submission timestamp, and returned output metadata.
- Added regression coverage for prompt-ready, submitted, and completed manual generation attempts.

## [Unreleased]

### Added
- Machine-readable generation-attempt, media-asset, and frame-addressed edit-timeline schemas, wired into the production manifest.
- Regression tests for successful-render output references, media checksums/provenance, and timeline clip frame ranges.

### Notes
- These are execution-record contracts, not provider, storage, or rendering integrations.

 — V3.2 CI supply-chain hardening
- Pinned GitHub Actions checkout/setup-python to immutable, GitHub-signature-verified upstream commits after inspecting their MIT license files.
- Recorded preliminary dependency and CI-action provenance evidence; full transitive SBOM and project ownership review remain open.


## [Unreleased] — V3.2 character schema and generation gates
- Enforced character identity invariants, production ownership, canonical-reference kind/payload, wardrobe variants, rights status, and timezone-aware timestamps in semantic validation.
- Blocked pilot/batch generation and downstream stages when shot-linked character approval or asset/character rights are unresolved.
- Added regression tests for incomplete character profiles and stage-specific generation blockers.

## [Unreleased] — V3.2 semantic manifest validation
- Enforced production-manifest required fields, claim/source shape, and the full required shot contract in the semantic validator.
- Rejected invalid shot states and collisions between typed asset IDs and character IDs.
- Added regression tests for incomplete shots, invalid shot states, and cross-namespace ID collisions.


## [Unreleased] — V3.2 generation-stage state alignment
- Added explicit PILOT_GENERATION and BATCH_GENERATION manifest states to match the documented stage transitions and semantic validator.

## [Unreleased] — V3.2 character metadata contract
- Require character profile owner, created/updated timestamps, linked-shot array, and canonical-reference creator/source provenance in the schema and semantic validator.
- Add regression coverage for required profile metadata and canonical provenance.

## [Unreleased] — V3.2 validation hardening
- Upgraded repository validation to execute Draft 2020-12 schema validation with format checking and resolved local schema references, in addition to structural checks.
- Added regression coverage for malformed approval timestamps and refreshed the validation report to identify the exact post-merge commit and CI evidence.


## [Unreleased] — V3.2 contract hardening
- Expressed official idea-scoring weights explicitly as percentages to satisfy the unchanged scoring-contract test.
- Unified Project Instructions, Daily Intelligence, and setup guidance around a two-layer interaction/evidence contract.
- Aligned the repository's default short-form duration with active Project Instructions (9:16, 45–60 seconds).
- Standardized the 3–5 qualified-candidate target while allowing fewer when evidence is insufficient; removed quota pressure.
- Distinguished three strategic editorial pillars from five daily discovery lanes and documented their mapping.
- Clarified daily source attribution versus full research/audit provenance; prohibited claims of persistence without confirmed writes.
- Standardized typed asset IDs across architecture and asset register; removed generic AST-### ambiguity.
- Preserved human approval, rights blockers, scientific integrity, and stage-gated release requirements.

## [Unreleased] — V3.2 foundation
- Added a dedicated character-reference bible and machine-readable character profile schema.
- Added a production-manifest schema and shot-to-character linkage with exact character-profile version locking.
- Standardized category-specific asset IDs and character approval/rights states.
- Strengthened manifest validation for duplicate IDs, dangling references, profile-version mismatches, character canonical references, rights, and release blockers.
- Added GitHub Actions CI for Python 3.11, 3.12, and 3.13, including JSON Schema meta-validation and manifest-schema validation.
- Reconciled setup/README with repository contents and removed the unsupported legacy-file assumption.
- Replaced stale validation claims with GitHub Actions as the authoritative execution record.
- Recorded the owner-selected source-available commercial licensing direction; final license text, rights inventory, legal review, and publication remain pending.

## 3.0.0 — 2026-11-04
- Reframed WHAT IF WORLD as a stage-gated production module.
- Added lifecycle state machine, artifact contracts, role boundaries, retry/recovery semantics.
- Added intelligence provenance, source/claim ledger, stable IDs, asset rights, continuity, and failure taxonomy.
- Split plan QA, asset QA, and master QA; defined non-compensatory blockers.
- Added JSON Schemas, dependency-free validators, tests, and architecture reference review.
- Preserved WW-001/WW-002 as legacy archive entries; no claim that their videos are rendered or published.


## [Unreleased] — UAT P0 remediation
- Refreshed the connected-provider readiness snapshot on 2026-11-11: Runway exposes image models and `sam3` background removal only, with no video/speech/music/SFX models or saved workflows; the 14 recent gallery items are images and are not project-ingested; Canva folder/design and video-guide checks remain limited.

- Enforced stage-specific, timestamped human approvals for idea selection, pilot, batch, generation, asset QA, master QA, and release transitions.
- Corrected the example manifest to remain an unapproved IDEA_CANDIDATE rather than implying producer approval.
- Integrated the 2026-11-05 Daily Intelligence source and claim provenance into the active development line.
- Added a machine-readable Daily Intelligence report schema, freshness/provenance validator, and scheduled GitHub issue monitor. The monitor detects missing/stale/incomplete reports; it does not perform research or claim trend discovery.
