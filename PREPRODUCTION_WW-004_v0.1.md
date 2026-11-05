# PRE-PRODUCTION DOSSIER — WW-004
## v0.1 — DRAFT / RIGHTS & STIMULUS VALIDATION HOLD

- Artifact ID: PREPROD-WW-004
- Production ID: WW-004
- Idea ID: IDEA-20261105-01
- Approved story: STORY-WW-004 v0.1
- Research: RESEARCH_IDEA-20261105-01.md
- Branch target: feat/v3.2-character-reference-system
- Working title: Gambar yang Sama, Tapi Kini Terlihat Berbeda
- Pillar: HUMAN BODY & MIND
- Stage: PRE-PRODUCTION
- Status: DRAFT — ASSET/RIGHTS GATES OPEN
- Owner: AI Creative Director / Prompt & Asset Engineer
- Human Producer / Google Flow operator: user (manual)
- Created: 2026-11-05 (Asia/Jakarta)
- Format: 9:16 vertical; 58 seconds target
- Editorial label: CURRENT_VERIFIED (scientific phenomenon; not a platform-trend assertion)
- Change note: First pre-production plan. No media assets have been generated, rendered, inspected, or rights-cleared by this artifact.

## 1. Production brief

### Creative objective
Let viewers experience the recognition contrast themselves: ambiguous two-tone image → matching intact grayscale photograph → the exact same two-tone image returns. Explain the effect without suggesting that the pixels or physical image changed.

### Production strategy
- Make one original grayscale photograph specifically for WW-004.
- Derive one high-contrast two-tone image from that exact photograph using a deterministic threshold operation in an image editor. Do not ask an image/video generator to recreate the two-tone image.
- Reuse the exact same two-tone file at the opening, reveal, and ending. The editor must use the same file/asset reference, not three regenerated versions.
- Use restrained editorial backgrounds and graphic overlays. Research numbers are typography added in editing, not generated text.
- No recurring character, recurring location, or character reference profile is needed. No AST-CHAR ID is assigned.
- Default sound: separate VO; no generated dialogue, no music, no synthetic brain sound effects. Per-shot Flow audio prompts explicitly request silence. Music, if later selected, is a separate rights-reviewed master track in edit.

### Stimulus subject decision
**Proposed source photograph:** an ordinary black dog sitting in side profile on a pale, simple outdoor ground, facing left, with the entire body, legs, ears and tail visible. The silhouette should be distinctive but not cartoonish.

Rationale: one familiar object with a clear global outline is easier to cue than a complex scene. The dog is a proposed creative stimulus, not a stimulus from any cited paper. It must pass a phone-size ambiguity test before it is locked.

### Required stimulus construction
1. Generate or create one naturalistic grayscale photograph using the master prompt in Section 4.
2. Save the selected source as `WW-004_AST-REF-001_source-grayscale_v001.png`.
3. Create a two-tone derivative by converting to grayscale if needed, applying a single documented luminance threshold to pure black and pure white, and preserving exact canvas dimensions, crop, orientation and subject geometry. No edge restoration, sharpening, object removal, generative fill, or AI re-creation.
4. Save as `WW-004_AST-IMAGE-001_mooney-two-tone_v001.png`.
5. Record SHA-256 for both files and the threshold value/tool/version in the asset record.
6. Use the exact `AST-IMAGE-001` file at 00:00–00:08, 00:14–00:22 and 00:49–00:58. The three occurrences must be byte-identical source assets. Any scaling/crop in the edit must be identical at all three occurrences.
7. If the initial image is already obvious to nearly everyone or impossible to identify after cueing, revise the source photograph and create a new version; do not fake the audience response.

### Scientific/rights boundaries
- This is an original demonstration inspired by a published perceptual-learning paradigm, not a replication of the study protocol.
- Do not use Nature Neuroscience, bioRxiv, iScience or PNAS study stimuli, figures, patient imagery, or screenshots unless the exact item license/permission has been checked.
- Generated image terms are not presumed commercially cleared. Record the exact provider terms that apply to the user's account and intended use. Until checked, rights remain PENDING.
- Do not portray generated scenes as footage from the actual 2026 study or show identifiable patients/researchers.
- Neural evidence may be represented with restrained abstract editorial graphics only; never depict a literal neuron “switching on”, instant rewiring, or a proven causal pathway.

## 2. Continuity and design bible

### Stimulus continuity
- `AST-REF-001`: original grayscale source photograph; master stimulus source.
- `AST-IMAGE-001`: deterministic two-tone derivative; immutable image used for all three reveal/return moments.
- Same subject direction, crop, canvas, scale, and orientation throughout.
- The original grayscale cue must be visibly derived from the same source as the two-tone image.
- The stimulus itself must not animate, morph, sharpen, gain details, or change shape between appearances.
- If an image is placed inside a designed frame, use the same frame geometry and exact image transform at each repeat.

### Visual language
- Realistic cinematic/documentary restraint; clean editorial composition.
- Palette: neutral charcoal, off-white, grayscale, with one restrained warm accent only if needed for data hierarchy.
- High legibility on a phone; large central stimulus; no busy background.
- Camera language: locked-off/static for stimulus and research cards. Avoid parallax, zoom, rack focus or motion that could alter perceived stimulus geometry.
- No logo opener, no slow establishing shot, no decorative brain graphics.
- No character continuity system required.

### Location / character / prop registry
- Characters: none required.
- Locations: none required; use neutral editorial plates only.
- Props: no recurring physical prop.
- Reference assets: AST-REF-001 source photograph; AST-IMAGE-001 two-tone derivative.
- All reference assets remain DRAFT/PENDING until actual output, inspection and rights review.

## 3. Timeline and shot register

Total target runtime: 58 seconds. VO and overlay timings may be refined in edit after a timed read-through. Do not accelerate the initial observation window to force VO.

| Shot | Timecode | Duration | Story beat / VO | Visual execution | Asset IDs (planned) | Risk |
|---|---:|---:|---|---|---|---|
| SH-001 | 00:00–00:08 | 8s | Anomaly + VO-01 | Full-screen two-tone stimulus, no label for first 2 seconds; then a small instruction “Perhatikan gambar ini” | AST-KF-001 / AST-VIDEO-001 / AST-AUDIO-001; uses AST-IMAGE-001 | stimulus readability |
| SH-002 | 00:08–00:14 | 6s | Cue + VO-02 | Show the original grayscale source photograph full-frame; minimal transition, no extra interpretation | AST-KF-002 / AST-VIDEO-002 / AST-AUDIO-002; uses AST-REF-001 | source image must match |
| SH-003 | 00:14–00:22 | 8s | Recognition return + VO-03 | Return to the exact AST-IMAGE-001 file, same crop and scale as SH-001 | AST-KF-003 / AST-VIDEO-003 / AST-AUDIO-003; uses AST-IMAGE-001 | pixel identity / edit continuity |
| SH-004 | 00:22–00:34 | 12s | Experiment evidence + VO-04 | Simple three-step graphic: ambiguous two-tone → original grayscale cue → same two-tone again. Add labels in edit, not generated text | AST-KF-004 / AST-VIDEO-004 / AST-AUDIO-004 | must not imply universal success |
| SH-005 | 00:34–00:49 | 15s | Neural evidence + VO-05 | Restrained evidence card: “13 pasien” / “1.104 neuron” / “34 sesi”. Add qualifier “pasien yang menjalani pemantauan epilepsi”. Use no fake patient footage or literal neuron activation | AST-KF-005 / AST-VIDEO-005 / AST-AUDIO-005 | clinical sample context |
| SH-006 | 00:49–00:58 | 9s | Payoff + VO-06 | Reuse exact AST-IMAGE-001; overlay “GAMBARNYA TETAP SAMA” then “PETUNJUKNYA YANG BERTAMBAH” | AST-KF-006 / AST-VIDEO-006 / AST-AUDIO-006; uses AST-IMAGE-001 | same-file proof; text legibility |

### Shot acceptance criteria (all shots)
- Exact timecode/duration and 9:16 crop; no unintended letterboxing.
- No generated or accidental text, logo, watermark, UI, or subtitle in source plates.
- Every factual overlay maps to the approved claim ledger.
- Stimulus frames in SH-001, SH-003 and SH-006 use the same source asset and same image transform.
- Video does not introduce extra objects, morph the stimulus, or invent a scene presented as research footage.
- No music or VO embedded in per-shot audio.
- A prompt existing is PLAN_QA evidence only; no asset is PASS until returned and inspected.

## 4. Copy-ready master stimulus prompt (English)

Use this once to create the original grayscale source photograph. Do not use this prompt to generate the two-tone derivative.

```text
Create one original, photorealistic documentary-style grayscale photograph for a visual perception demonstration. Subject: an ordinary medium-sized black dog sitting in a clear side profile, facing left, with the complete head, ears, torso, all four legs, and tail visible. The dog is naturally posed on a simple pale, lightly textured outdoor ground with a quiet, uncluttered mid-gray background. Use soft natural overcast daylight, realistic fur texture, authentic canine anatomy, a clear readable outer silhouette, and moderate tonal separation between the dog and background. Compose the dog centrally with generous negative space around the entire silhouette. Camera at the dog's body height, 50mm documentary photography look, crisp focus, neutral exposure, no dramatic shadows, no shallow-focus blur, no motion blur. Grayscale only, natural photographic realism, vertical 4:5 composition preferred so it can be consistently cropped for a 9:16 mobile layout. No people, no leash, no collar, no toys, no other animals, no scenery clutter, no text, no logos, no watermark, no frame, no border, no illustration, no cartoon styling, no artificial anatomy.
```

**Post-process instruction (not a generative prompt):** create the two-tone derivative from the selected source photograph in an image editor using one fixed luminance threshold. Preserve canvas dimensions and geometry exactly. Record editor name/version and threshold. Do not use an AI image-to-image operation for this transformation.

## 5. Google Flow shot packets — prompts in English

All prompts below are plans, not evidence of submission or generation. Use the exact selected keyframe as the reference for its same-shot video. If the current Google Flow account/mode does not support a field, record the limitation and use the stated fallback. Keep VO and music out of Flow.

### SH-001 — First encounter (00:00–00:08; 8 seconds)
**Narrative purpose:** create an immediate visual anomaly; give the viewer time to inspect.

**Keyframe image prompt**
```text
Create a clean, premium documentary-editorial vertical 9:16 still plate. Use a perfectly uniform deep charcoal background with a large, precisely centered empty rectangular image area occupying approximately 82 percent of the frame width and 66 percent of the frame height. The image area must be a flat neutral off-white field reserved for an image that will be composited later in editing. Keep generous safe margins. Straight-on orthographic composition, no perspective, no texture inside the reserved image area, restrained studio lighting, crisp edges, realistic clean graphic-design finish. Do not generate any picture, animal, object, text, letters, numbers, logo, watermark, border ornament or UI inside the reserved area.
```

**Video prompt**
```text
Animate the selected keyframe as a completely locked-off static 8-second vertical 9:16 plate. No camera movement, no zoom, no parallax, no flicker, no lighting change, no object motion, and no scene transition. Preserve the exact dimensions and edges of the empty central image area from the keyframe for later editorial compositing. Do not add content, text, symbols, or objects.
```

**Audio prompt**
```text
Silence only. Generate no ambience, no sound effects, no music, no speech, no voice, and no tonal bed.
```

**Editorial composite:** place AST-IMAGE-001 in the reserved area. Keep the first 2 seconds free of labels. At 00:02, optional small overlay: “Perhatikan gambar ini”.

**Plan B:** create the charcoal plate directly in the editor; do not use generative video if the central rectangle drifts.

### SH-002 — Original grayscale cue (00:08–00:14; 6 seconds)
**Narrative purpose:** reveal the intact source photograph that supplies the visual cue.

**Keyframe image prompt**
```text
Create a minimal vertical 9:16 documentary presentation plate: a warm-neutral off-white background with one large, perfectly centered, empty 4:5 portrait image window. The window is a clean flat placeholder reserved for a real photograph to be composited later. Straight-on view, symmetrical margins, subtle realistic paper-like surface only outside the image window, soft even light, premium restrained editorial design. Do not generate a subject or photograph in the window. No text, labels, icons, logos, watermark, borders or UI.
```

**Video prompt**
```text
Create a locked-off 6-second hold of the selected keyframe. Preserve the empty portrait image window, its exact position, dimensions and rectangular geometry. No camera movement, no zoom, no parallax, no transition, no lighting change, no animated elements, and no new objects. Leave the image window completely unchanged for editorial insertion of the original grayscale source photograph.
```

**Audio prompt**
```text
Silence only. No music, no speech, no voice, no ambience and no sound effects.
```

**Editorial composite:** place AST-REF-001 in the window. It must be the source photograph used to create AST-IMAGE-001.

**Plan B:** use the source photograph full-screen with a hard cut; do not create a second version of the photograph.

### SH-003 — Same image returns (00:14–00:22; 8 seconds)
**Narrative purpose:** let the viewer test whether the same ambiguous image is now easier to recognize.

**Keyframe image prompt**
```text
Create a clean, premium documentary-editorial vertical 9:16 still plate matching the SH-001 composition exactly: perfectly uniform deep charcoal background and a large, precisely centered empty rectangular image area with identical dimensions, position, edges, and neutral off-white fill. Straight-on orthographic composition, no perspective, no texture inside the reserved area, no camera angle variation, no decorative elements. This plate will receive the exact same two-tone image file used earlier in post-production. No animal, no photograph, no text, no symbols, no logo, no watermark, no border, no UI.
```

**Video prompt**
```text
Hold the selected keyframe completely static for 8 seconds. Match the SH-001 plate geometry exactly: same central image-area dimensions, position, scale, background tone and straight-on alignment. No camera movement, zoom, crop change, parallax, flicker, morphing, added detail or transition. Preserve a stable empty area for the exact same source image to be composited in editing.
```

**Audio prompt**
```text
Silence only. No music, no speech, no voice, no ambience and no sound effects.
```

**Editorial composite:** reinsert the exact AST-IMAGE-001 file used in SH-001. Verify identical SHA-256 source and identical scale/crop/position. Never regenerate the stimulus.

**Plan B:** duplicate the SH-001 edit clip and replace only the timecode; do not create a new plate.

### SH-004 — How the experiment works (00:22–00:34; 12 seconds)
**Narrative purpose:** explain the experimental sequence without implying that every viewer or image responds identically.

**Keyframe image prompt**
```text
Create a restrained scientific-documentary vertical 9:16 infographic background plate. Deep charcoal matte background, three evenly spaced empty rectangular panels arranged vertically with clean thin off-white outlines and generous spacing. Each panel must be blank and flat, reserved for editorial insertion of three existing image assets. Add no arrows, no labels, no text, no icons, no images, no numbers, no logo, no watermark, and no decorative neural graphics. Front-facing orthographic layout, precise grid alignment, high contrast, premium editorial design, phone-readable negative space.
```

**Video prompt**
```text
Hold the selected infographic keyframe static for 12 seconds. Keep all three empty panel frames perfectly fixed with no camera movement, zoom, parallax, animation, lighting changes, transitions or added elements. Preserve the exact panel geometry so the editor can insert the original two-tone image, its matching grayscale source, and the same two-tone image again. Do not generate or alter any of those images.
```

**Audio prompt**
```text
Silence only. No music, no speech, no voice, no ambience and no sound effects.
```

**Editorial composite:** top-to-bottom sequence: AST-IMAGE-001 → AST-REF-001 → AST-IMAGE-001. Add labels “GAMBAR AMBIGU”, “FOTO ASLI”, “GAMBAR YANG SAMA”. These are editorial overlays, not generator text.

**Plan B:** build the three-panel layout directly in the editor using the same assets.

### SH-005 — Neural evidence (00:34–00:49; 15 seconds)
**Narrative purpose:** ground the story in the 2026 peer-reviewed neural recording study while preserving its clinical sample limitation.

**Keyframe image prompt**
```text
Create a restrained, photorealistic scientific-documentary editorial background plate in vertical 9:16. A dark neutral research-display environment with a single softly illuminated, empty central data-display panel. The panel must contain no waveform, no graph, no labels, no numbers, no medical imagery, and no readable text; it is reserved for verified editorial typography. The environment should feel calm, precise and credible, not futuristic or sensational. No patient, no doctor, no identifiable researcher, no hospital bed, no surgical scene, no brain illustration, no neuron illustration, no glowing synapses, no logos, no watermark. Static straight-on composition, high legibility, restrained contrast.
```

**Video prompt**
```text
Animate the selected keyframe as a restrained 15-second static documentary plate. Keep the camera locked off. The empty display panel remains blank and geometrically stable for factual text to be added in editing. No animated neural network, no firing neurons, no brain scan, no waveform, no numbers, no labels, no patient or researcher, no scene transition, no camera move, and no new objects.
```

**Audio prompt**
```text
Silence only. No music, no speech, no voice, no ambience and no sound effects.
```

**Editorial composite:** show:
- “13 PASIEN” (patients undergoing epilepsy monitoring)
- “1.104 NEURON”
- “34 SESI”
- small qualifier: “Perekaman pada pasien dengan epilepsi yang sulit dikendalikan; bukan sampel populasi umum.”

Use CLM-023. The 1,104 figure is neurons, not people. Do not animate or imply that all neurons changed identically.

**Plan B:** use a flat dark card with large typography only; this is preferable to an inaccurate brain visualization.

### SH-006 — Final payoff (00:49–00:58; 9 seconds)
**Narrative purpose:** close on the exact same stimulus and the core takeaway.

**Keyframe image prompt**
```text
Create a minimal vertical 9:16 closing editorial plate matching the SH-001 and SH-003 charcoal composition exactly: uniform deep charcoal background, one large centered empty rectangular image area with identical dimensions, position, scale and neutral off-white fill. Reserve clear negative space below the image area for two short lines of editorial text to be added later. No text, no animal, no image, no symbols, no logo, no watermark, no frame ornament, no perspective and no decorative effects. Straight-on, locked, clean documentary design.
```

**Video prompt**
```text
Hold the selected keyframe completely static for 9 seconds. Match the geometry and tone of SH-001 and SH-003 exactly. No camera movement, no zoom, no parallax, no flicker, no transition, no object motion and no changes to the reserved image area. Keep the lower text-safe area empty and unobstructed for editorial typography.
```

**Audio prompt**
```text
Silence only. No music, no speech, no voice, no ambience and no sound effects.
```

**Editorial composite:** insert the exact AST-IMAGE-001 file again. Add text in two stages: “GAMBARNYA TETAP SAMA” then “PETUNJUKNYA YANG BERTAMBAH”. Do not alter the stimulus image.

**Plan B:** duplicate the SH-001 plate and composite the final overlay in the editor.

## 6. Asset register (planned; not generated)

| Asset ID | Type | Filename / planned role | Origin | Rights status | Parent / provenance | Used by | Current state |
|---|---|---|---|---|---|---|---|
| AST-REF-001 | REFERENCE | WW-004_AST-REF-001_source-grayscale_v001.png | GENERATED or EDITED; confirm actual route | PENDING | Original stimulus source; tool terms to be checked | SH-002, SH-004 | NOT CREATED |
| AST-IMAGE-001 | IMAGE | WW-004_AST-IMAGE-001_mooney-two-tone_v001.png | EDITED | PENDING | Deterministic threshold derivative of AST-REF-001 | SH-001, SH-003, SH-004, SH-006 | NOT CREATED |
| AST-KF-001 | KEYFRAME | SH-001 charcoal plate | GENERATED if Flow used | PENDING | Prompt SH-001 | SH-001 | PROMPT DRAFT |
| AST-VIDEO-001 | VIDEO | SH-001 static plate | GENERATED if Flow used | PENDING | AST-KF-001 | SH-001 | PROMPT DRAFT |
| AST-AUDIO-001 | AUDIO | SH-001 silence decision | NOT GENERATED | NOT_REQUIRED if silence is used | Silence | SH-001 | PLANNED |
| AST-KF-002 | KEYFRAME | SH-002 grayscale presentation plate | GENERATED if Flow used | PENDING | Prompt SH-002 | SH-002 | PROMPT DRAFT |
| AST-VIDEO-002 | VIDEO | SH-002 static plate | GENERATED if Flow used | PENDING | AST-KF-002 | SH-002 | PROMPT DRAFT |
| AST-AUDIO-002 | AUDIO | SH-002 silence decision | NOT GENERATED | NOT_REQUIRED if silence is used | Silence | SH-002 | PLANNED |
| AST-KF-003 | KEYFRAME | SH-003 charcoal plate | GENERATED if Flow used | PENDING | Prompt SH-003 | SH-003 | PROMPT DRAFT |
| AST-VIDEO-003 | VIDEO | SH-003 static plate | GENERATED if Flow used | PENDING | AST-KF-003 | SH-003 | PROMPT DRAFT |
| AST-AUDIO-003 | AUDIO | SH-003 silence decision | NOT GENERATED | NOT_REQUIRED if silence is used | Silence | SH-003 | PLANNED |
| AST-KF-004 | KEYFRAME | SH-004 three-panel plate | GENERATED if Flow used | PENDING | Prompt SH-004 | SH-004 | PROMPT DRAFT |
| AST-VIDEO-004 | VIDEO | SH-004 static plate | GENERATED if Flow used | PENDING | AST-KF-004 | SH-004 | PROMPT DRAFT |
| AST-AUDIO-004 | AUDIO | SH-004 silence decision | NOT GENERATED | NOT_REQUIRED if silence is used | Silence | SH-004 | PLANNED |
| AST-KF-005 | KEYFRAME | SH-005 research evidence plate | GENERATED if Flow used | PENDING | Prompt SH-005 | SH-005 | PROMPT DRAFT |
| AST-VIDEO-005 | VIDEO | SH-005 static plate | GENERATED if Flow used | PENDING | AST-KF-005 | SH-005 | PROMPT DRAFT |
| AST-AUDIO-005 | AUDIO | SH-005 silence decision | NOT GENERATED | NOT_REQUIRED if silence is used | Silence | SH-005 | PLANNED |
| AST-KF-006 | KEYFRAME | SH-006 closing plate | GENERATED if Flow used | PENDING | Prompt SH-006 | SH-006 | PROMPT DRAFT |
| AST-VIDEO-006 | VIDEO | SH-006 static plate | GENERATED if Flow used | PENDING | AST-KF-006 | SH-006 | PROMPT DRAFT |
| AST-AUDIO-006 | AUDIO | SH-006 silence decision | NOT GENERATED | NOT_REQUIRED if silence is used | Silence | SH-006 | PLANNED |

Do not create generation-attempt records until the Human Producer actually submits a prompt. If Flow is not used for static plates, mark them as editor-created assets instead; do not fabricate Flow provenance. For any actual media asset, record exact tool/model/mode, prompt hash, dimensions, duration, checksum, source asset IDs and rights status only after the file is returned and accessible.

## 7. Audio map

| Track | Source | Time | Decision | Rights / state |
|---|---|---|---|---|
| VO | Separate TTS or recorded voice, not yet selected | 00:02–00:58 | Use approved STORY VO; separate recording/mix | TTS model/voice/settings not selected |
| Per-shot ambience/SFX | None by default | All shots | Explicit silence | No generated audio claimed |
| Music | None in current plan | All shots | No music; add only if a rights-cleared track is later selected | Not selected; rights not assessed |

If the actual Google Flow mode does not support audio generation, record AUDIO_GENERATION_UNAVAILABLE; silence remains the planned output, so no manual SFX replacement is required.

## 8. Subtitle and overlay map (draft)

| Start | End | Text | Type | Claim |
|---:|---:|---|---|---|
| 00:02 | 00:08 | Coba perhatikan gambar ini. Kamu melihat sesuatu, atau hanya pola hitam-putih? | Subtitle VO | CLM-020 |
| 00:08 | 00:14 | Ini foto aslinya. Sekarang, lihat lagi gambar hitam-putih yang tadi. | Subtitle VO | CLM-020, CLM-026 |
| 00:14 | 00:22 | Gambarnya sama persis. Tapi, apakah sekarang bentuknya lebih mudah kamu kenali? | Subtitle VO | CLM-021, CLM-026 |
| 00:22 | 00:34 | Dalam eksperimen, peserta melihat gambar dua-warna yang ambigu, lalu foto aslinya. Saat gambar dua-warna yang sama ditampilkan lagi, pengenalan dapat meningkat tajam. | Subtitle VO | CLM-021, CLM-022 |
| 00:34 | 00:49 | Studi tahun 2026 juga merekam aktivitas neuron pada 13 pasien yang menjalani pemantauan epilepsi. Setelah belajar mengenali gambar, respons di sejumlah wilayah otak berubah. | Subtitle VO | CLM-023 |
| 00:49 | 00:58 | Peneliti menduga informasi baru membantu otak membaca pola yang sebelumnya sulit dikenali. Bukan gambarnya yang berubah—petunjuknya yang bertambah. | Subtitle VO | CLM-024, CLM-026 |

- Subtitle must be split into readable phrases during editing; do not place full paragraphs on screen.
- Keep text inside platform safe zones; test on phone preview.
- Evidence card overlays are separate from subtitles and remain visible long enough to read.
- No numerical percentage is planned for the 2026 recognition result.

## 9. Edit assembly plan

1. Create a 9:16, 58-second timeline.
2. Place the same AST-IMAGE-001 file in SH-001, SH-003 and SH-006; verify the media source and transform are identical.
3. Place AST-REF-001 as the cue in SH-002.
4. Build SH-004 three-panel experiment sequence using AST-IMAGE-001 → AST-REF-001 → AST-IMAGE-001.
5. Build SH-005 as a typographic evidence card. Preserve “13 patients undergoing epilepsy monitoring” qualifier; show “1,104 neurons” and “34 sessions” with correct units.
6. Add VO as a separate track after timed read-through. Do not embed VO in Flow outputs.
7. Add subtitles and evidence overlays as separate tracks.
8. Use silence unless a later rights-reviewed music decision is made.
9. Review full timeline muted to verify the visual explanation works without sound.
10. Export settings, frame rate, codec, audio sample rate and master resolution remain UNSET until the editor/project environment is selected.

## 10. Rights and provenance register (WW-004 assets)

| Asset / class | Intended source | Current status | Required evidence before pilot/release |
|---|---|---|---|
| AST-REF-001 grayscale stimulus | Original generated/created for WW-004 | HOLD / PENDING | Exact generator/editor terms, account mode, commercial-use scope, output provenance |
| AST-IMAGE-001 two-tone derivative | Deterministic edit of AST-REF-001 | HOLD / PENDING | Parent file, editor/version, threshold operation, checksum; verify derivative rights follow source terms |
| SH-001..SH-006 plates | Original project prompts and possible Flow output | PENDING | Actual output provenance, exact Flow terms, commercial scope, checksum |
| VO | Human recording or selected TTS | NOT SELECTED | Voice consent/ownership or TTS terms, provider/model/voice ID, commercial-use terms |
| Music | None selected | NOT USED | If introduced, exact track, license, attribution, territory, commercial/social platform rights |
| Fonts | Editor default/system font or licensed font | NOT SELECTED | Exact font name/version/license; avoid assuming bundled font is cleared |
| Research references | SRC-020..SRC-022 | CITED / NOT REUSED AS MEDIA | Attribution in project notes; no figures/stimuli reused without permission |

Global repository rights are not cleared; this production must make item-level decisions. Any unresolved included asset blocks pilot approval or release as applicable.

## 11. Pilot and generation handoff

### Pilot recommendation
Because this concept is dominated by one exact stimulus and static editorial graphics, first validate:
- the source grayscale photograph;
- the thresholded two-tone derivative;
- the phone-size ambiguity/readability;
- byte-identical reuse and consistent crop;
- one representative static background plate only if Google Flow is needed.

Do not batch-generate six clips before the stimulus pair passes. If a Flow-generated plate changes the reserved image window, replace it with a native editor graphic.

### Manual operator protocol
- Operator: Human Producer.
- Execution mode: MANUAL_USER.
- Tool: Google Flow, exact active account UI mode to be recorded by operator.
- Model/version/mode, duration, aspect ratio, resolution, audio feature availability, seed/settings: NOT YET VERIFIED; do not invent.
- For each actual submission, create a new generation attempt ID and preserve failures; do not overwrite.
- A render is returned only when the file is supplied and accessible for inspection.
- No API/connector submission is assumed.

## 12. PRE-PRODUCTION PLAN_QA

| Check | Status | Evidence / note |
|---|---|---|
| Approved STORY input | PASS | User explicitly approved STORY WW-004. |
| Claim mapping | PASS | VO and overlays map to CLM-020..026. |
| Story duration plan | PASS — PROVISIONAL | 58-second timeline; final timed VO read pending. |
| Stimulus strategy | PASS — DESIGN ONLY | Single original source and deterministic derivative specified. |
| Exact-image continuity | PASS — DESIGN ONLY | Same AST-IMAGE-001 reused three times; checksum still pending. |
| Stimulus asset exists | HOLD | No image file has been created or returned yet. |
| Phone-size ambiguity test | HOLD | Must be tested with actual stimulus and small informal test; no test evidence yet. |
| Rights/tool terms | HOLD | Exact generator/account terms and asset rights not yet verified. |
| Character bible | NOT REQUIRED | No recurring character in this concept. |
| Shot register and prompt fields | PASS — DRAFT | Six planned shots with separate keyframe/video/audio prompts and Plan B. |
| Audio separation | PASS — PLAN | Silence per shot; VO separate; no music selected. |
| Google Flow model/mode | NOT VERIFIED | Must be recorded from actual UI only. |
| Returned keyframes/video/audio | NOT STARTED | No generation submission or output received. |
| Asset QA / pilot approval | NOT STARTED | Cannot score without actual outputs. |

**Provisional PLAN_QA:** 87/100 (planning-only estimate, not asset QA, render QA, master QA, or release score). Rights, stimulus readability, and actual tool-mode verification are blockers for pilot authorization.

## 13. Gate decision

- STORY: APPROVED by explicit Human Producer instruction on 2026-11-05.
- PRE-PRODUCTION dossier: DRAFT COMPLETE.
- Prompt pack: DRAFT COMPLETE.
- Stimulus master and derivative: NOT CREATED.
- Rights review: OPEN / HOLD.
- Character profile: NOT REQUIRED.
- Asset register: planned IDs reserved in this dossier; no generated assets claimed.
- Shot register: DRAFT COMPLETE.
- Pilot generation: NOT AUTHORIZED until stimulus feasibility and rights checks are resolved and this pre-production gate is explicitly accepted.
- Batch generation: NOT AUTHORIZED.
- Editing/QA/release: NOT AUTHORIZED.

**Current disposition: HOLD_PENDING_STIMULUS_AND_RIGHTS_VALIDATION.**

**Human Producer handoff:** create the proposed grayscale source photograph using the master prompt, derive the two-tone version without generative alteration, return both files for inspection, and provide the exact Google Flow account mode/terms visible in the UI. The next review will test stimulus readability, source/derivative identity, rights evidence, and VO timing before authorizing a pilot.
