# WHAT IF WORLD — PRODUCTION DOSSIER TEMPLATE V3

> One dossier per `WW-###`. Version every material change. Do not mark a gate PASS without evidence.

## 0. Control record
- Production ID / version:
- Working title:
- Current state:
- Producer / reviewer:
- Created / updated (ISO 8601):
- Approved idea reference:
- Daily Intelligence report ID/date:
- Editorial label: aktual-terverifikasi / aktual-terbatas / evergreen / orisinal-editorial:
- Change note:

## 1. Creative brief
- Pillar:
- Audience hypothesis:
- Platform / aspect / duration:
- Core question:
- One-sentence hypothetical premise:
- Variable changed:
- Variables held constant:
- Emotional objective:
- Unique angle versus archive:
- Intended takeaway:
- What this video is NOT claiming:

## 2. Intelligence provenance
| Signal ID | Topic | Source | Publication/event date | Region | Observed metric | Freshness | Limitation |
|---|---|---|---|---|---|---|---|

## 3. Claim ledger
| Claim ID | Exact claim | Class | Source IDs | Confidence | Safe wording | Status |
|---|---|---|---|---|---|---|
Class: FACT / EXTRAPOLATION / FICTIONAL_ASSUMPTION. Status: SUPPORTED / QUALIFIED / UNVERIFIED / REJECTED. Critical UNVERIFIED claims block STORY approval.

## 4. Scientific model
- Baseline system:
- Changed variable:
- Held-constant assumptions:
- Mechanism:
- Immediate effects:
- Delayed effects:
- Spatial scope:
- Time horizon:
- Feedback loops / secondary effects:
- Known unknowns:
- Alternative explanations:
- Units and calculations:
- Red-team questions:
- Claims removed after review:

## 5. Story architecture
| Beat | Time range | Audience question | New evidence | Consequence | Emotion | Shot IDs |
|---|---|---|---|---|---|---|
Required: anomaly → question/premise → evidence → mechanism → consequence → nuance/payoff. Hook must work with sound off.

## 6. Voice-over
| Segment | In | Out | Text (Indonesian) | Word count | Claim IDs |
|---|---|---|---|---:|---|
- Total words:
- Effective speaking rate:
- Pause budget:
- Pronunciation notes:
- TTS voice/model/settings:
- TTS output filename and checksum:

## 7. Continuity bible
**Character registry:** ID, face, age range, hair, skin tone, build, wardrobe by phase, accessories, behavior.
**Location registry:** ID, geometry, landmarks, direction, time, weather, lighting, environmental state.
**Prop registry:** ID, appearance, scale, position, narrative function, shots used.
**Continuity invariants:** what must never change.
**Allowed state changes:** what changes and at which shot/time.
**Screen direction / eyeline / geography:**
**Visual palette and lens language:**

## 8. Asset and rights register
| Asset ID | Type | Filename/URI | Source/creator | License/rights | Model/version | Prompt/ref | Status | Used by |
|---|---|---|---|---|---|---|---|---|

## 9. Shot register
| Shot ID | Beat | Duration | Start state | Single action | Camera move | End state | Asset IDs | Claim IDs | Risk |
|---|---|---:|---|---|---|---|---|---|---|

### Shot packet — duplicate per shot
- Shot ID / version:
- Narrative purpose:
- Acceptance criteria:
- Tool/model/version/mode:
- Aspect ratio / duration / resolution:
- Asset refs (max supported by selected tool):
- Keyframe prompt (English):
```text
[Prompt]
```
- Video prompt (English):
```text
[Prompt]
```
- Negative constraints:
- Plan B:
- Generation attempts and output filenames:
- Selected take and reason:
- Failure notes:
- Generation operator: Human Producer (manual Google Flow)
- Execution mode: MANUAL_USER
- Model / model version / mode (exact displayed value; otherwise belum ditentukan):
- Submitted timestamp (if known):
- Actual aspect ratio / duration / resolution:
- Seed / settings (only if exposed; otherwise null/blank):
- Returned output filename / URI (only after supplied and accessible):
- Generation attempt status: REQUESTED / SUBMITTED / RUNNING / SUCCEEDED / FAILED / CANCELLED
- Human inspection: PASS / REWORK / HOLD:

## 9A. Manual Google Flow handoff
- ChatGPT supplies copy-ready English prompts and Plan B per shot.
- Human Producer manually runs prompts in Google Flow; no API/connector is assumed.
- Record actual model/mode/settings only when visible; unknown values are belum ditentukan.
- A render counts as returned only when the file is supplied and accessible for inspection.
- Runway is optional, not a dependency. TTS/music/SFX are separate manual/optional workflows unless an authorized tool is actually used.

## 10. Audio plan
| Track ID | Type | Source | Start/end | Level/processing | Rights | Filename |
|---|---|---|---|---|---|---|
Tracks: VO, music, ambience, SFX. Include no-audio/silence decisions explicitly.

## 11. Subtitle and overlay map
| Start frame/time | End frame/time | Text | Type | Position | Claim ID | Safe-zone check |
|---|---|---|---|---|---|---|

## 12. Edit decision list
| Order | Shot/asset | Source in | Source out | Timeline in | Timeline out | Transition | Notes |
|---|---|---|---|---|---|---|---|
- Timeline frame rate:
- Audio sample rate:
- Master resolution:
- Codec/container:
- Color pipeline:
- Export preset:
- Project file path:
- Optional interchange file (OTIO/EDL/XML):

## 13. TikTok package
- Cover title (exact Indonesian overlay text):
- Cover image prompt (English; copy-ready; generate image without embedded typography):
- Cover composition / focal subject / contrast / negative space:
- Cover safe-zone and crop check (9:16; TikTok UI clearance):
- Cover output spec and asset ID/status (do not mark generated until file is returned):
- Caption / description (Indonesian; state the hypothetical framing and distinguish evidence from scenario):
- Hashtags (relevant, limited, no misleading factual tag):
- Pinned comment (source/model caveat where needed):
- CTA:
- Posting-time hypothesis and basis (omit if no reliable account analytics):
- AI-content disclosure check:
- Thumbnail/cover file URI and rights status:

## 14. QA report
| Check | Type | Pass/fail | Evidence/file/timecode | Defect ID | Owner |
|---|---|---|---|---|---|
Types: science, story, visual, continuity, audio, edit, rights, platform.
- PLAN_QA score:
- RENDER_QA score:
- Blockers:
- Rework actions:
- Reviewer:
- Approval timestamp:

## 15. Release & archive
- Release ID:
- Final master filename / checksum:
- Final dossier version:
- Rights review:
- Disclosure/caption review:
- Human release approval:
- Published URL/date (leave blank until confirmed):
- Performance snapshot (only measured data):
- Lessons learned:
- Archive row:

### Shot packet addendum — mandatory Google Flow fields V3.2
Every shot must contain these three independent fields:
- **Keyframe image prompt (English):** exact still-image generation prompt; specify subject, setting, composition, camera angle/lens, lighting, texture, realism, and exclusions.
- **Video prompt (English):** explicitly animate the selected keyframe; state duration/aspect ratio when supported, one main action, one camera move, start/end state, continuity locks, and negative constraints.
- **Audio prompt (English):** separate diegetic ambience/SFX prompt for this shot; state sound source, perspective, intensity, texture, and exclusions. Default no music and no VO.
- **Plan B:** a simpler composition/motion/audio fallback if generation is unstable.
- **Keyframe selected URI/filename + checksum:** fill only after actual output is supplied and accessible.
- **Google Flow actual model/mode/features:** record only what the Human Producer sees in the UI; otherwise mark belum ditentukan.

### Google Flow audio and music separation
Google Flow audio is used per shot when the active account/mode supports it. The operator pastes the video prompt and the separate audio prompt into the corresponding supported fields. Do not assume feature availability or silently merge the prompts. Keep music as a separate master track selected during editing or TikTok posting. Keep VO separate from generated ambience/SFX. If a mode does not support audio generation, record AUDIO_GENERATION_UNAVAILABLE and provide a manual SFX fallback.
