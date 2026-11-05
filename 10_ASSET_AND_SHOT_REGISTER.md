# WHAT IF WORLD — ASSET & SHOT REGISTER

## 1. Stable asset IDs
- Character: AST-CHAR-###
- Location: AST-LOC-###
- Prop: AST-PROP-###
- Reference: AST-REF-###
- Keyframe: AST-KF-###
- Video: AST-VIDEO-###
- Audio: AST-AUDIO-###
- Master: AST-MASTER-###

Never recycle IDs. Revisions increment asset versions and preserve historical sources.

## 2. Asset record
Record ID, production ID, version, type, filename/URI, checksum, creator/source, license/permission, attribution, rights status, generation tool/model/version/mode, prompt version, seed/settings where available, parent references, status, used-by shots, and inspection notes.

## 3. Character identity
Recurring or identity-critical characters require a profile governed by 03A_CHARACTER_REFERENCE_BIBLE.md and schemas/character_reference.schema.json. Use AST-CHAR-###. A profile is not canonical until the human producer approves it. Separate identity invariants from wardrobe, pose, expression, lighting, and scene state.

## 4. Shot identity
Every shot uses SH-### and records story beat, narrative purpose, duration/frame rate, start state, one principal action, camera move, end state, location/character/prop IDs, claim IDs, prompt/tool/mode, attempts, acceptance criteria, actual inspection, Plan B, and defect IDs. Link characters with character_ids and lock the exact profile version in character_reference_versions, for example {"AST-CHAR-001":"1.0.0"}. The validator rejects missing or mismatched versions and dangling links.

## 5. Continuity invariants
Track face identity, hair, build, wardrobe phase, prop orientation, geography, screen direction, eyeline, time, weather, light direction, and environmental state. Assign permitted state changes to shot/timecode. If an upstream reference changes, mark dependent shots STALE.

## 6. File naming
- WW-003_SH-004_GEN-02_model-mode_9x16_8s_v001.mp4
- WW-003_AST-CHAR-001_REF_v003.png
- WW-003_AST-AUDIO-VO_v002.wav

Use safe filenames, no spaces, stable IDs, and increment versions/attempts. Never overwrite failed attempts.

## 7. Rights
No asset is release-approved until commercial/publishing rights are known. Record license URL and exact terms; "found online" is not a license.

## 8. Google Flow three-prompt asset contract (V3.2)
Each generated shot must link three distinct assets and prompt records:
- AST-KF-###: still keyframe image and its exact prompt/reference provenance.
- AST-VIDEO-###: video generated from that same shot's selected keyframe; record the keyframe parent reference.
- AST-AUDIO-###: per-shot diegetic ambience/SFX generated separately from the video prompt when supported by the active Google Flow mode.

The keyframe is the visual anchor for its shot. Video acceptance compares first/middle/final frames against it. Audio acceptance checks correspondence with visible action/environment and excludes unintended speech/music. Music master and VO are separate editorial assets, not per-shot ambience assets.

Record actual tool/model/version/mode, feature availability, prompt version, output filename/URI, checksum, rights, and inspection result only when verified. If the active Flow mode lacks audio generation, retain the audio prompt, record AUDIO_GENERATION_UNAVAILABLE, and link a rights-cleared manual SFX fallback. Never mark a prompt as a generated asset.

## 9. WW-003 planned asset allocation
| Shot | Keyframe | Video | Audio | Duration | Status |
|---|---|---|---|---:|---|
| SH-001 | AST-KF-001 | AST-VIDEO-001 | AST-AUDIO-001 | 4s | PROMPT_READY |
| SH-002 | AST-KF-002 | AST-VIDEO-002 | AST-AUDIO-002 | 6s | PROMPT_READY |
| SH-003 | AST-KF-003 | AST-VIDEO-003 | AST-AUDIO-003 | 8s | PROMPT_READY |
| SH-004 | AST-KF-004 | AST-VIDEO-004 | AST-AUDIO-004 | 9s | PROMPT_READY |
| SH-005 | AST-KF-005 | AST-VIDEO-005 | AST-AUDIO-005 | 7s | PROMPT_READY |
| SH-006 | AST-KF-006 | AST-VIDEO-006 | AST-AUDIO-006 | 11s | PROMPT_READY |
| SH-007 | AST-KF-007 | AST-VIDEO-007 | AST-AUDIO-007 | 10s | PROMPT_READY |

Prompt-ready is not render success. Generation attempt IDs and returned assets are added only after the Human Producer runs Google Flow and supplies accessible outputs.
