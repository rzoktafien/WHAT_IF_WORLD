# WHAT IF WORLD — Production Integration Readiness

**Document ID:** PIR-001  
**Audit snapshot:** 2026-11-25  
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
| Runway MCP (workspace snapshot 2026-11-25) | Authenticated workspace `B4R4K4`; current `whoami` exposes seven image models and `sam3` background removal; video, speech, music, sound-effect, listed video-tool, and mesh model lists are empty; mesh generation reports `feature_unavailable`; zero saved workflows. The last voice-library search (2026-11-22) returned 20 records on its first page with a continuation cursor (total unknown); voice search is not speech generation. The 2026-11-25 `list_recent(limit=20)` query returned 15 recent items, all images, with no video/audio in the returned set; none is verified as project-ingested or canonically approved | IMAGE GENERATION AVAILABLE; NO VIDEO/TTS ADAPTER | Keep project asset provenance and rights outside the provider gallery; verify each output and store it in project-controlled immutable storage |
| Canva connector (workspace snapshot 2026-11-25) | Search found one existing WHAT IF WORLD YouTube Channel Banner design and no matching project folder; video production guide returned `upgrade_required` with `alternative_model_available: false`; no project video timeline/render verified | DESIGN ACCESS; VIDEO GUIDE RESTRICTED BY CONNECTOR RESPONSE | Recheck actual capability before any video test; design-level editing tools do not establish a deterministic video-edit/export adapter |
| TTS | The 2026-11-25 Runway `whoami` response has an empty `availableSpeechModels` list; the last voice-library search on 2026-11-22 returned 20 records on its first page with a continuation cursor (total unknown); no speech generation job, TTS render, voice-consent ledger, or render log was verified | VOICE SEARCH ONLY; TTS ADAPTER NOT IMPLEMENTED | Verify speech generation with an explicitly authorized sample, licensed voice, pronunciation tests, audio export, and provenance before accepting an adapter |
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
**Status: PARTIAL.** Remaining: choose storage, define upload/retention/backup policy, attach checksums and immutable URIs, create generation-attempt/render-probe records, and test recovery. The 20 most recent Runway gallery items returned by the limit-20 query (all images; no videos or audio) are not counted as project assets because no project-controlled immutable URI, checksum, production/shot mapping, rights record, retention policy, or backup evidence was verified. The newest gallery item is a generated TikTok cover thumbnail created 2026-11-14 14:41 UTC; two earlier entries created 2026-11-08 UTC were named as location-master and character-master references. Their names do not establish project identity, canonical approval, or ingest.

### Phase 3 — Provider adapters
**Status: NOT STARTED.** The 2026-11-25 Runway `whoami` exposes seven image models and `sam3` background removal; `seedream-5-pro` appeared in the 2026-11-22 snapshot but is absent from the current available-image list, and the reason is not established. The connected workspace returned empty lists for video, speech, music, sound-effect, and all listed video-tool models; mesh generation reports `feature_unavailable`. The last Eleven v4 voice-library search (2026-11-22) returned 20 voice records on the first page with a continuation cursor (total library size not established), but voice search is not speech generation and no TTS job or audio output was executed. Zero saved workflows were found. The 2026-11-25 limit-20 gallery query returned 15 recent images and no videos or audio in the returned set; none was verified as ingested into the project asset register. Canva design access is available, but its video production guide returned `upgrade_required` with no alternative model. No tested video-generation, TTS, or editing adapter exists. Build one provider adapter at a time after capability and rights are verified; start with one pilot shot and one TTS sample only after the relevant generation capability is verified. No batch run before human inspection.

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


## 8. Connected-provider audit snapshot (2026-11-22)

These are workspace-scoped observations from read-only capability checks. They are not guarantees about every provider plan, workspace, or future model release.

### Runway MCP
- Authentication: confirmed for the connected workspace.
- Image models exposed: `nano-banana-pro`, `nano-banana-2.1`, `nano-banana-2`, `nano-banana-2-lite`, `seedream-5-pro`, `p-image-ideogram`, `gen-4`, and `gen-4-image-turbo`.
- Video, speech, music, and sound-effect model lists: empty; all listed video-tool model arrays are also empty.
- Saved workflows: zero.
- Background-removal models exposed: `sam3`; this does not establish video generation, TTS, audio, or editing capability.
- 3D mesh generation: unavailable in this workspace; `availableMeshModels` is empty and the workspace reports `feature_unavailable`.
- Recent gallery: the limit-20 query returned 20 generated image assets and no videos or audio. The newest is a TikTok cover thumbnail created 2026-11-14 14:41 UTC; two earlier entries from 2026-11-08 UTC were named as location-master and character-master references. The metadata did not establish a WHAT IF WORLD production ID, shot ID, canonical-reference approval, checksum in the project register, or rights disposition; none is counted as a project production asset.
- Gallery query scope: the connector returned the 20 most recent items because the request limit was 20; this is a bounded recent-page result, not a complete workspace inventory. All 20 returned items were images; no video or audio appeared in that page.
- Eleven v4 voice-library search returned 20 voice records on the first page with a continuation cursor (total library size not established). `availableSpeechModels`, `availableMusicModels`, and `availableSoundEffectModels` were empty; no speech-generation job was run and no audio output is claimed.
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
## 9. Connected-provider recheck (2026-11-25)

These are read-only observations from the currently connected workspaces. They supersede the 2026-11-22 provider snapshot only where explicitly stated; they do not establish capabilities for other accounts or plans.

### Runway MCP
- Authentication: confirmed; pinned workspace `B4R4K4`; no alternate workspaces reported.
- Current `availableImageModels`: `nano-banana-pro`, `nano-banana-2.1`, `nano-banana-2`, `nano-banana-2-lite`, `p-image-ideogram`, `gen-4`, and `gen-4-image-turbo` (seven models).
- `seedream-5-pro` was present in the 2026-11-22 snapshot but is absent from the 2026-11-25 response. The reason is not established; no retirement, deprecation, or plan restriction is inferred.
- `availableVideoModels`, `availableSpeechModels`, `availableMusicModels`, `availableSoundEffectModels`, and all listed `availableVideoToolModels` arrays are empty. `availableMeshModels` is empty and mesh generation reports `feature_unavailable`. Background-removal model `sam3` is exposed.
- `list_workflows` returned zero saved workflows.
- `list_recent(limit=20)` returned 15 recent items, all images; no video or audio appeared in the returned set. This is a recent-gallery result, not a project asset registry or proof of a complete inventory. The newest returned item is the generated TikTok cover thumbnail (asset `44e27bbe-1fdf-4f45-a71d-69a7231853b7`, task `80105454-b231-47d1-8d2c-90c91d8a5597`, created 2026-11-14 14:41:27 UTC). The location and character master references remain provider-gallery items; no project production/shot mapping, project checksum, rights disposition, or canonical approval was verified.
- The last Eleven v4 voice-library search (2026-11-22) returned 20 first-page records with a continuation cursor; total library size is unknown. The current empty `availableSpeechModels` list means voice search is not evidence of TTS generation capability. No TTS job or audio output was run.

### Canva connector
- Folder search returned no matching WHAT IF WORLD folder.
- Design search returned one existing design: `WHAT IF WORLD — YouTube Channel Banner` (design ID `DAHZ-ecP__Y`, one page).
- The current video production guide failed with `upgrade_required`; `alternative_model_available` is false. No video generation was attempted, and no project video timeline, export, or render was verified.

### Operational consequence
- Google Flow remains a manual Human Producer handoff; no API or connector is assumed.
- Runway image-model access can support only an explicitly authorized still/reference task, subject to rights and provenance capture. It does not establish video, TTS, SFX, music, editing, or publishing readiness.
- Canva design access does not establish a deterministic video-edit/export adapter.
- Phase 2 remains PARTIAL, Phase 3 remains NOT STARTED, and Phase 4 remains DEFERRED. No provider generation, editing, upload, rights clearance, or publication was performed.

## 10. Connected-provider recheck (2026-11-28)

These are read-only observations from the currently connected Runway and Canva workspaces. They are workspace-scoped and do not establish capabilities for other accounts or plans.

### Runway MCP
- Authentication: confirmed for workspace `B4R4K4`; model availability response was marked fresh; no alternate workspace was reported.
- Current image models: `nano-banana-pro`, `nano-banana-2.1`, `nano-banana-2`, `nano-banana-2-lite`, `p-image-ideogram`, `gen-4`, and `gen-4-image-turbo` (seven).
- `availableVideoModels`, `availableSpeechModels`, `availableMusicModels`, `availableSoundEffectModels`, and all listed `availableVideoToolModels` arrays are empty.
- `availableMeshModels` is empty and mesh generation reports `feature_unavailable`; `sam3` remains exposed for image background removal.
- `list_workflows` returned zero saved workflows.
- Eleven v4 voice-library search returned 20 records on the first page with a continuation cursor. This confirms voice-catalog search only; the empty `availableSpeechModels` list does not establish TTS generation capability. No speech-generation job or audio output was run.
- No image, video, speech, music, sound-effect, editing, or upload job was initiated during this recheck.

### Canva connector
- Folder search returned no matching WHAT IF WORLD folder.
- Design search returned one existing design: `WHAT IF WORLD — YouTube Channel Banner` (design ID `DAHZ-ecP__Y`).
- The video production guide returned `upgrade_required` with `alternative_model_available: false`. No video generation was attempted; no project video timeline, export, or render was verified.

### Operational consequence
- Google Flow remains a manual Human Producer handoff; no API or connector is assumed.
- Runway exposes image-generation models and voice-catalog search, but no video, speech-generation, music, sound-effect, listed video-tool, or mesh models in this workspace response. Voice search is not a TTS adapter.
- Canva design access does not establish a video-generation or deterministic editing/export adapter.
- Phase 2 remains PARTIAL, Phase 3 remains NOT STARTED, and Phase 4 remains DEFERRED. No provider generation, editing, upload, rights clearance, or publication was performed.

