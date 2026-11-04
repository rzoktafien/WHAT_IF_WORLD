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
Every shot uses SH-### and records story beat, narrative purpose, duration/frame rate, start state, one principal action, camera move, end state, location/character/prop IDs, claim IDs, prompt/tool/mode, attempts, acceptance criteria, actual inspection, Plan B, and defect IDs. Use shots[].character_ids to link character profiles. Production cross-references are checked by tools/validate_manifest.py.

## 5. Continuity invariants
Track face identity, hair, build, wardrobe phase, prop orientation, geography, screen direction, eyeline, time, weather, light direction, and environmental state. Assign permitted state changes to shot/timecode. If an upstream reference changes, mark dependent shots STALE.

## 6. File naming
- WW-003_SH-004_GEN-02_model-mode_9x16_8s_v001.mp4
- WW-003_AST-CHAR-001_REF_v003.png
- WW-003_AST-AUDIO-VO_v002.wav

Use safe filenames, no spaces, stable IDs, and increment versions/attempts. Never overwrite failed attempts.

## 7. Rights
No asset is release-approved until commercial/publishing rights are known. Record license URL and exact terms; "found online" is not a license.
