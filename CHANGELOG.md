# Changelog

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
