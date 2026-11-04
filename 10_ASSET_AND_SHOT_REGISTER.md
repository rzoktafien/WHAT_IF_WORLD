# WHAT IF WORLD — ASSET & SHOT REGISTER

## Asset identity
Use stable IDs: `AST-CHAR-###`, `AST-LOC-###`, `AST-PROP-###`, `AST-REF-###`, `AST-KF-###`, `AST-VIDEO-###`, `AST-AUDIO-###`, `AST-MASTER-###`.

Every asset record contains:
- ID, production ID, version, asset type, filename/URI, checksum;
- creator/source, license/permission, attribution;
- generation tool/model/version/mode, prompt version, seed/settings if available;
- parent/reference assets and transformations;
- status: planned / generated / selected / rejected / approved / stale;
- used by shot IDs and inspection note.

## Shot identity
Every shot uses `SH-###` and records:
- story beat and narrative purpose;
- duration and frame rate;
- start state, one principal action, camera move, end state;
- location/character/prop asset IDs;
- claim IDs illustrated or narrated;
- prompt version, tool/mode, attempts;
- acceptance criteria and actual inspection result;
- Plan B and defect IDs.

## Continuity invariants
Track invariants explicitly: face identity, costume, prop orientation, geography, screen direction, time of day, weather, light direction, and environmental state. State changes must be assigned to a specific shot/timecode. If an upstream reference changes, mark dependent shots `STALE`.

## File naming
`WW-003_SH-004_GEN-02_model-mode_9x16_8s_v001.mp4`
`WW-003_AST-CHAR-001_REF_v003.png`
`WW-003_AST-AUDIO-VO_v002.wav`
Use lowercase safe filenames, no spaces, stable IDs, and increment version/attempt. Do not overwrite failed attempts.

## Rights
No asset is approved for release until commercial/publishing rights are known. Record license URL and exact terms; “found online” is not a license.
