# WHAT IF WORLD — Production Integration Readiness

**Document ID:** PIR-001  
**Audit snapshot:** 2026-11-12  
**Status:** PHASE 1 ENGINEERING BASELINE VERIFIED; GOOGLE FLOW REMAINS MANUAL; CONNECTED RUNWAY/CANVA CAPABILITIES ARE LIMITED (SEE SECTION 8)

## 1. Executive finding
The repository implements a document-driven production blueprint: stage contracts, JSON Schemas, semantic validators, regression tests and GitHub Actions CI. Video generation is intentionally performed manually by the Human Producer in Google Flow after ChatGPT prepares copy-ready per-shot prompts. The repository does not implement a Google Flow API/connector, automatic generation submission, or output retrieval. TTS rendering, editing, platform analytics and publishing are also not claimed as automated.

Describe WHAT IF WORLD accurately as an AI-assisted, human-operated production workflow: ChatGPT prepares and QA-checks production artifacts; the Human Producer manually generates in Google Flow and returns renders. Do not describe external media execution as automated.

## 2. Capability inventory

| Capability | Current evidence | Status | Acceptance evidence still required |
|---|---|---|---|
| Manifest and stage state machine | JSON Schema + semantic validator + regression tests | IMPLEMENTED | Continue contract regression testing |
| Character profile and shot continuity | Character schema, reciprocal shot links, version references, semantic gates | IMPLEMENTED | Real approved reference asset and profile review |
| Rights/release blockers | Validator blocks unresolved linked asset/character rights in generation/downstream states | IMPLEMENTED | Asset-level evidence and human rights disposition |
| GitHub CI | Python 3.11/3.12/3.13 matrix, schema/contract checks, tests, negative release-gate test | IMPLEMENTED | Monitor future CI |
| Asset storage and immutable media versioning | No integrated object store or asset service evidenced | NOT IMPLEMENTED | Provider, access controls, immutable IDs, checksums, retention and backup test |
| Google Flow / Veo | Copy-ready prompt pack + manual handoff and render-return procedure documented; no API/connector assumed | INTENDED MANUAL WORKFLOW | Human Producer runs prompts, supplies actual render and visible metadata; rights and render QA remain required |
| Runway MCP (workspace snapshot 2026-11-12) | Authenticated; eight image models and `sam3` background removal exposed; no video/speech/music/SFX models; zero saved workflows; 14 recent gallery items are images and are not linked to production/shot IDs or project rights records | IMAGE-ONLY ACCESS; NO VIDEO/AUDIO ADAPTER | Keep project asset provenance and rights outside the provider gallery; verify each output and store it in project-controlled immutable storage |
| Canva connector (workspace snapshot 2026-11-12) | One existing WHAT IF WORLD YouTube Channel Banner found; no project folder; video production guide returned the message that advanced AI features are unavailable on the current plan or trial; no project video timeline/render verified | DESIGN ACCESS; VIDEO GENERATION RESTRICTED BY CONNECTOR RESPONSE | Recheck actual capability before any video test; design-level editing tools do not establish a deterministic video-edit/export adapter |
| TTS | No TTS adapter, voice consent ledger or render log evidenced | NOT IMPLEMENTED | Provider, licensed voice, pronunciation tests, audio export and provenance |
| Editing / FFmpeg / Remotion / OTIO | No executable editing pipeline evidenced | NOT IMPLEMENTED | Versioned edit spec, media probes, audio mix, subtitle burn-in, export preset and render QA |
| TikTok publishing | README specifies manual publishing; no publishing adapter or credential flow evidenced | MANUAL | Authorized app/scopes, disclosure workflow, upload test and confirmed public post URL |
| Platform analytics | No authorized TikTok/Google analytics integration evidenced | NOT IMPLEMENTED | Approved connector/API, definitions, refresh and provenance records |

## 3. Recommended adapter contracts

### 3.0 Machine-readable execution records (V3.2 contract increment)
The repository now defines JSON Schema contracts for `generation_attempts`, `media_assets`, and `edit_timeline`, and exposes them as optional fields on the production manifest. A successful generation attempt must reference an output asset; media assets require a SHA-256 checksum, URI, MIME type, provenance, and rights disposition; edit clips are frame-addressed and reference stable media asset IDs. These contracts validate records only: they do not call a provider, store media, probe a file, render a timeline, or prove that a URI is retrievable. Semantic cross-record checks and a real storage/provider adapter remain future work.



### 3.1 Generation adapter (optional; not required for Google Flow manual workflow)
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
**Status: PARTIAL.** Remaining: choose storage, define upload/retention/backup policy, attach checksums and immutable URIs, create generation-attempt/render-probe records, and test recovery. The 14 recent Runway gallery items (all images; no videos) are not counted as project assets because no project-controlled immutable URI, checksum, production/shot mapping, rights record, retention policy, or backup evidence was verified. Two newly returned generated images were named as location-master and character-master references, but their names do not establish project identity, canonical approval, or ingest.

### Phase 3 — Provider adapters
**Status: NOT STARTED.** A Runway connection is available for image generation and `sam3` background removal only in the checked workspace; no video, speech, music, or SFX models were exposed and no saved workflows were found. The latest gallery returned 14 image assets and no videos; none was verified as ingested into the project asset register. Canva design access is available, but its video production guide returned a message that advanced AI features are unavailable on the current plan or trial. Neither connection is a tested generation, TTS, or editing adapter. Build one provider at a time after capability and rights are verified; start with one pilot shot and one TTS sample only after those capabilities are actually available. No batch run before human inspection.

### Phase 4 — Orchestration
**Status: DEFERRED.** Introduce orchestration only after manual adapter workflows stabilize and bottlenecks are measured. The checked Runway workspace had zero saved workflows; no provider event integration, durable job state, idempotent retry/recovery, or end-to-end orchestration was verified.

## 6. Release-readiness rule
Green CI proves repository contracts and tests only. It does not prove provider connection, shot generation, edit render, master inspection, rights clearance or publication. Until Phases 2–3 are implemented and a real production passes human gates, automated end-to-end production remains HOLD. Manual production remains possible when artifacts, rights and approvals are recorded.


## 6. UAT P0 remediation — automated Daily Intelligence freshness control
A scheduled GitHub Actions monitor validates the newest persisted JSON report under `reports/daily-intelligence/`. The report schema requires run timestamp, observation window, five discovery lanes, source records, claim-to-source links, candidate evidence labels/scores, platform-access limitations, and truncation status. The validator checks schema, freshness (maximum seven days), completion, all five lanes, reciprocal source/claim references, critical-claim support, and candidate references.

**Boundary:** this monitor is a freshness/provenance guard, not an automated research agent. It does not crawl the web, access private TikTok/Google analytics, verify scientific truth, score trends from platform telemetry, or approve ideas. When a report is missing or invalid, GitHub Actions opens or updates one issue for follow-up. A real research provider integration remains unimplemented until an authorized provider and credentials are selected and tested.

## 7. Stage-specific human approval enforcement
The semantic manifest validator requires timestamped `APPROVED` records with a non-empty approver for each state transition: idea, pilot, batch, generation, asset QA, master QA, and release. This data-contract gate is separate from GitHub code review. The repository ruleset's PR approval count remains zero and must not be represented as mandatory human code-review approval.


**Activation constraint:** GitHub scheduled workflows execute from the repository's default branch. This monitor is present and testable in the V3.2 feature PR, but its daily cron will not become active until the repository owner deliberately merges the workflow to the default branch. This remediation does not modify `main`; before that merge, report freshness can be checked by the validation command and CI on the feature branch.


## 8. Connected-provider audit snapshot (2026-11-12)

These are workspace-scoped observations from read-only capability checks. They are not guarantees about every provider plan, workspace, or future model release.

### Runway MCP
- Authentication: confirmed for the connected workspace.
- Image models exposed: `nano-banana-pro`, `nano-banana-2.1`, `nano-banana-2`, `nano-banana-2-lite`, `seedream-5-pro`, `p-image-ideogram`, `gen-4`, and `gen-4-image-turbo`.
- Video models: none exposed. Speech, music, and sound-effect model lists were also empty.
- Saved workflows: zero.
- Background-removal models exposed: `sam3`; this does not establish video generation, TTS, audio, or editing capability.
- Recent gallery: 14 generated image assets were returned and no videos. Two newest entries, created 2026-11-08 UTC, were named as location-master and character-master references. The metadata did not establish a WHAT IF WORLD production ID, shot ID, canonical-reference approval, checksum in the project register, or rights disposition; none is counted as a project production asset.
- No image, video, speech, music, or sound-effect generation was initiated during this audit.

### Canva connector
- Project search found one existing design named `WHAT IF WORLD — YouTube Channel Banner`; no matching project folder was found.
- The video production guide returned a current plan/trial restriction. No video generation was attempted.
- Design-level search/read/edit tools are exposed, but no WHAT IF WORLD video timeline, export, or completed render was found or verified. This is not accepted as a tested video-editing adapter.

### Operational consequence
- Google Flow remains a manual Human Producer handoff; no API/connector is assumed.
- Runway image-model access can support an explicitly authorized still/reference task, subject to rights and provenance capture. It does not establish video, TTS, SFX, music, editing, or publishing readiness.
- Canva design access does not remove the current video-generation restriction and does not establish a deterministic editing/export pipeline.
- Phase 2 remains PARTIAL, Phase 3 remains NOT STARTED, and Phase 4 remains DEFERRED. Provider connection alone is not adapter acceptance evidence.
