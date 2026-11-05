# Google Flow Manual Generation Handoff — V3.2

**Decision:** Google Flow is the project's user-operated, manual video-generation tool. WHAT IF WORLD does not assume a Google Flow API, connector, authenticated adapter, browser automation, or automatic output retrieval.

## Responsibility contract

| Work | Responsible | Evidence / handoff |
|---|---|---|
| Research, claim ledger, story, VO, storyboard | ChatGPT | Reviewed production dossier |
| Character continuity, asset plan, shotlist | ChatGPT | Character/asset/shot registers |
| Final per-shot keyframe/video prompts and Plan B | ChatGPT | Copy-ready prompt pack in English |
| Tool execution in Google Flow | Human Producer | User confirms submission or returns renders |
| Generation settings/model metadata capture | Human Producer supplies what Flow displays; ChatGPT records it | Generation attempt record |
| Render inspection and continuity/science QA | ChatGPT, with human viewing/approval where required | Asset QA evidence and defects |
| Editing execution | Human Producer/editor; ChatGPT supplies EDL, timing and instructions | Edit evidence / master supplied for QA |
| Release decision and publication | Human Producer | Explicit approval and confirmed publication URL |

ChatGPT must not ask the producer to perform research, write prompts, build shotlists, or prepare the production dossier when those tasks can be completed by ChatGPT. The producer's manual generation action is intentional, not a missing prerequisite to automate.

## Handoff sequence

1. **PROMPT PACK READY (ChatGPT):** deliver one prompt packet per shot, with shot ID, narrative purpose, acceptance criteria, exact English prompt, negative constraints, references, duration, aspect ratio, and Plan B. Default target is 9:16; actual duration and supported settings are stated per shot, not assumed.
2. **MANUAL GENERATION (Human Producer):** copy prompts into Google Flow and generate. No automated submission is implied.
3. **RENDER RETURNED (Human Producer):** upload/share the generated file or otherwise provide a retrievable output. A filename typed in chat alone is not proof that a media file is accessible.
4. **RECORD & INSPECT (ChatGPT):** record actual metadata that is visible or supplied, inspect the returned render, note defects, and recommend ACCEPT / REWORK / HOLD. A successful generation attempt requires an actual returned output asset; do not infer success from prompt submission.
5. **PILOT GATE:** producer inspects and explicitly approves the pilot before batch generation. ChatGPT then prepares the remaining shot prompts.
6. **EDIT / QA:** ChatGPT prepares edit instructions and QA criteria. The producer/editor performs the actual edit unless an explicitly authorized editing tool is available and used. ChatGPT reviews the supplied master.
7. **RELEASE:** producer explicitly approves publication. ChatGPT prepares metadata and archive records; publication is not claimed until confirmed.

## Minimum generation handoff record

For each shot/attempt, record:

- provider: Google Flow
- execution_mode: MANUAL_USER
- operator: Human Producer
- model and model_version: exact value displayed by the user's Flow session; use "belum ditentukan" when unknown
- mode: exact mode displayed; use "belum ditentukan" when unknown
- aspect_ratio, duration_seconds, and resolution: actual requested/returned values
- prompt version and SHA-256; reference URIs and hashes when available
- seed and settings only when Flow exposes them; otherwise leave null/empty and do not claim reproducibility
- requested/submitted/completed timestamps when known
- output filename/URI and output asset ID only after the render is returned and recorded
- failure note and retry lineage; never overwrite failed attempts

Do not fabricate a provider job ID, seed, model name, setting, output URI, checksum, or timestamp. "belum ditentukan" is an acceptable explicit value for unknown model/version/mode metadata.

## Scope exclusions

- No Google Flow API or connector is assumed or to be fabricated.
- Runway is optional and is not a dependency, required subscription, or production gate.
- TTS, music, SFX, and editing remain separately sourced/manual unless a real authorized tool is explicitly selected and verified. ChatGPT supplies scripts, audio maps, prompts/instructions, and edit timelines; it does not claim to render audio or video without tool evidence.
- Automated work focuses on research workflow, records, prompt-pack preparation, continuity, rights, validation, QA checklists, release preparation, and repository tests.

## State semantics

The manifest's existing PILOT_GENERATION, BATCH_GENERATION, and GENERATION stages remain. They describe production workflow stages, not API job states. Generation-attempt statuses mean:
- REQUESTED: ChatGPT has prepared the prompt/handoff packet.
- SUBMITTED: the producer confirms manual submission to Google Flow.
- RUNNING: the producer confirms Flow is processing the request.
- SUCCEEDED: a render has been returned and recorded as a media asset.
- FAILED / CANCELLED: the producer reports failure/cancellation; preserve the attempt and notes.

Human approval remains separate from these statuses. Prompt readiness, submission, or a generated file does not automatically approve a pilot, character, asset rights, QA, or release.
