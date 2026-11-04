# WHAT IF WORLD — QA & RELEASE PROTOCOL V3

## 1. Separate QA layers
- `PLAN_QA`: evaluates research, script, shot plan, prompts, and expected execution. Never call it render QA.
- `ASSET_QA`: inspects individual generated images, clips, and audio.
- `MASTER_QA`: inspects the assembled final video and release metadata.

## 2. Weighted score (100)
| Category | Weight | Evidence required |
|---|---:|---|
| Hook and clarity | 15 | First 2 seconds reviewed; premise legible |
| Story causality and suspense | 15 | Beat sheet and master timeline |
| Scientific integrity | 20 | Claim ledger and wording audit |
| Visual continuity | 15 | Reference/shot comparison |
| Shot execution | 10 | Actual rendered shot inspection |
| Audio and VO | 10 | Listening check and sync |
| Editing/readability | 10 | Mobile preview, timing, safe zones |
| Ending/framing/CTA | 5 | Final seconds and hypothetical disclosure |

Score each category with observable evidence; do not invent scores. `≥85` is required for release consideration, not automatic approval.

## 3. Mandatory blockers
Any one blocks release:
- unsupported/false critical claim;
- premise/visual contradiction that changes meaning;
- no clear hypothetical framing;
- rights/license unresolved for any included asset;
- severe continuity defect or malformed render;
- unintended speech/text/watermark;
- unreadable/mistimed subtitles or material audio defect;
- wrong export spec or corrupted file;
- AI disclosure/platform metadata unresolved;
- no human release approval.

## 4. Asset inspection
For each shot inspect first frame, middle, final frame, identity, anatomy, physics, motion, unwanted text, artifacts, crop, and audio. A generated file existing is not evidence of quality.

## 5. Master inspection
Watch the full video:
- once with sound;
- once muted (story comprehension and subtitle legibility);
- once on a phone-sized preview;
- spot-check every factual overlay against claim IDs.
Check frame rate, resolution, codec, audio sync, peak/clipping, safe zones, caption, cover, disclosure, and rights.

## 6. Release gate
Required: zero blockers, score ≥85, all claim records resolved, all asset rights cleared, final master checksum, final caption/cover, human approval timestamp. Only then `RELEASE_APPROVED`.

`PUBLISHED` requires actual URL/date confirmation. `ARCHIVED` requires dossier, source ledger, prompts, assets, final master reference/checksum, QA, release metadata, and lessons.
