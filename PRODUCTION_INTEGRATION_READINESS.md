# WHAT IF WORLD — Production Integration Readiness

**Document ID:** PIR-001  
**Audit snapshot:** 2026-11-05  
**Status:** PHASE 1 ENGINEERING BASELINE VERIFIED; MEDIA EXECUTION INTEGRATIONS NOT IMPLEMENTED

## 1. Executive finding
The repository implements a document-driven production blueprint: stage contracts, JSON Schemas, semantic validators, regression tests and GitHub Actions CI. It does not currently implement or prove external video generation, TTS rendering, editing, platform analytics or publishing. This boundary is explicit in 02A_MODULE_ARCHITECTURE.md and README.md.

Do not describe WHAT IF WORLD as end-to-end automated media production until adapters are built, connected to authorized accounts, tested with real outputs and accepted by a human producer.

## 2. Capability inventory

| Capability | Current evidence | Status | Acceptance evidence still required |
|---|---|---|---|
| Manifest and stage state machine | JSON Schema + semantic validator + regression tests | IMPLEMENTED | Continue contract regression testing |
| Character profile and shot continuity | Character schema, reciprocal shot links, version references, semantic gates | IMPLEMENTED | Real approved reference asset and profile review |
| Rights/release blockers | Validator blocks unresolved linked asset/character rights in generation/downstream states | IMPLEMENTED | Asset-level evidence and human rights disposition |
| GitHub CI | Python 3.11/3.12/3.13 matrix, schema/contract checks, tests, negative release-gate test | IMPLEMENTED | Monitor future CI |
| Asset storage and immutable media versioning | No integrated object store or asset service evidenced | NOT IMPLEMENTED | Provider, access controls, immutable IDs, checksums, retention and backup test |
| Google Flow / Veo | No authenticated provider adapter or API workflow evidenced | MANUAL / NOT INTEGRATED | Confirm account/API capability, terms, model/mode, output retrieval and usage rights |
| TTS | No TTS adapter, voice consent ledger or render log evidenced | NOT IMPLEMENTED | Provider, licensed voice, pronunciation tests, audio export and provenance |
| Editing / FFmpeg / Remotion / OTIO | No executable editing pipeline evidenced | NOT IMPLEMENTED | Versioned edit spec, media probes, audio mix, subtitle burn-in, export preset and render QA |
| TikTok publishing | README specifies manual publishing; no publishing adapter or credential flow evidenced | MANUAL | Authorized app/scopes, disclosure workflow, upload test and confirmed public post URL |
| Platform analytics | No authorized TikTok/Google analytics integration evidenced | NOT IMPLEMENTED | Approved connector/API, definitions, refresh and provenance records |

## 3. Recommended adapter contracts

### 3.0 Machine-readable execution records (V3.2 contract increment)
The repository now defines JSON Schema contracts for `generation_attempts`, `media_assets`, and `edit_timeline`, and exposes them as optional fields on the production manifest. A successful generation attempt must reference an output asset; media assets require a SHA-256 checksum, URI, MIME type, provenance, and rights disposition; edit clips are frame-addressed and reference stable media asset IDs. These contracts validate records only: they do not call a provider, store media, probe a file, render a timeline, or prove that a URI is retrievable. Semantic cross-record checks and a real storage/provider adapter remain future work.



### 3.1 Generation adapter
Inputs: production_id, shot_id, generation_attempt_id, approved prompt/version, canonical reference URIs, character profile versions, actual provider/model/mode, duration, aspect ratio, rights disposition and disclosure flags.

Outputs: provider job ID, execution timestamp, actual model/version/mode, prompt hash, reference hashes, seed/settings if exposed, output URI, MIME type, dimensions, duration, checksum, status, failure code and retry lineage.

A request or accepted job is not a completed render. Only a retrievable output with verified metadata can be recorded as GENERATED. Human pilot approval remains a separate transition.

### 3.2 Audio adapter
Keep TTS, music and SFX as separate asset records. Record provider/model, voice identity and authorization, script version, language, pronunciation overrides, output URI/checksum, license and commercial scope. Do not clone or imitate a real person's voice without documented authority.

### 3.3 Editing adapter
Consume approved media assets and a versioned edit decision list. Prefer an interchange format such as OTIO plus a deterministic render profile. Record source asset IDs, in/out timecodes, tracks/layers, transitions, subtitle version, audio mix, encoder, dimensions, frame rate, loudness checks, export checksum and failure notes.

### 3.4 Publishing adapter
Treat publishing as a separately authorized action. Use least-privilege OAuth scopes, secret storage, explicit human release approval and disclosure checks. Record platform post ID, canonical URL and publish timestamp only after platform confirmation.

## 4. Security and operational controls
- Store credentials only in an approved secret manager or GitHub Actions secrets; never in repository files, prompts, logs or manifests.
- Use least-privilege tokens and rotate/revoke credentials on suspected exposure.
- CI actions are pinned to immutable, GitHub-signature-verified upstream commits; the corresponding upstream MIT license files were inspected. Review security advisories and refresh pins through tested changes.
- Generate a resolved dependency SBOM for the supported environment; review direct and transitive licenses.
- Preserve immutable attempt records and hashes; never overwrite prior outputs.
- Record provider terms, model versions, account-tier limitations and asset restrictions.
- Disable external calls until corresponding rights and approval gates pass.

## 5. Implementation sequence and exit criteria

### Phase 1 — Documented workflow and machine contracts
**Status: IMPLEMENTED / CI VERIFIED.** Evidence: schemas, semantic validators, regression tests, protected branches and required CI checks.

### Phase 2 — Asset and execution records
**Status: PARTIAL.** Remaining: choose storage, define upload/retention/backup policy, attach checksums and immutable URIs, create generation-attempt/render-probe records, and test recovery.

### Phase 3 — Provider adapters
**Status: NOT STARTED.** Build one provider at a time after account/API capability and rights are verified. Start with one pilot shot and one TTS sample; no batch run before human inspection.

### Phase 4 — Orchestration
**Status: DEFERRED.** Introduce orchestration only after manual adapter workflows stabilize and bottlenecks are measured.

## 6. Release-readiness rule
Green CI proves repository contracts and tests only. It does not prove provider connection, shot generation, edit render, master inspection, rights clearance or publication. Until Phases 2–3 are implemented and a real production passes human gates, automated end-to-end production remains HOLD. Manual production remains possible when artifacts, rights and approvals are recorded.
