# Changelog

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
- Enforced stage-specific, timestamped human approvals for idea selection, pilot, batch, generation, asset QA, master QA, and release transitions.
- Corrected the example manifest to remain an unapproved IDEA_CANDIDATE rather than implying producer approval.
- Integrated the 2026-11-05 Daily Intelligence source and claim provenance into the active development line.
- Added a machine-readable Daily Intelligence report schema, freshness/provenance validator, and scheduled GitHub issue monitor. The monitor detects missing/stale/incomplete reports; it does not perform research or claim trend discovery.
