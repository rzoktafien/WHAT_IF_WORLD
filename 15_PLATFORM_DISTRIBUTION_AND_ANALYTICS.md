# WHAT IF WORLD — Platform Distribution & Analytics Operations

**Status:** Approved operating blueprint  
**Primary launch market:** Indonesia  
**Global packaging:** enabled from the start  
**Channels:** TikTok, YouTube, Instagram, website

## 1. Channel architecture

Use one verified research and production master as the source of truth. Each platform receives a deliberate adaptation.

| Channel | Primary job | Main formats | Primary success signals |
|---|---|---|---|
| TikTok | Discovery and search-led short video | 9:16 short-form, series | Hold, watch time, completion, shares, saves, search discovery |
| YouTube Shorts | Discovery and entry to long-form | 9:16 Shorts | Engaged views, retention, subscribers, long-form transitions |
| YouTube long-form | Durable documentary library | 6–12 minute initial target; longer only when justified | Watch time, returning viewers, search, satisfaction signals |
| Instagram Reels | Visual discovery and community | Reels, Stories, selected carousels | Reach, shares, saves, profile actions, meaningful replies |
| Website | Owned home and conversion | Explainers, source notes, portfolio, enquiry pages | Search impressions/clicks, newsletter signups, enquiries |

## 2. Account setup checklist

For each social account:
- Use the official brand identity and consistent handle where available.
- Use a brand-controlled email and recovery method.
- Enable two-factor authentication.
- Confirm owner/admin access and recovery contacts.
- Complete profile image, banner, bio, category, contact method, and link.
- Set account type appropriately for each platform's current features.
- Record account URL, handle, owner, creation date, access roles, and policy status in a private register.
- Never store passwords, recovery codes, or one-time codes in the repository.

Recommended short bio:
**Explore the impossible. Understand the real. Cinematic science, mysteries, and futures — grounded in evidence.**

## 3. Website MVP

Recommended information architecture:
1. Home — brand promise, featured episodes, latest work.
2. Watch — embedded video library organized by editorial pillar.
3. Stories — written companion explainers with source notes and update dates.
4. About — editorial mission, production approach, and team/AI disclosure as appropriate.
5. Editorial Standards — fact / extrapolation / fictional premise policy and corrections contact.
6. Studio — production services, sample work, process, and enquiry CTA.
7. Contact / Business Enquiries — professional contact channel.
8. Privacy and terms — publish only after the correct owner and jurisdiction details are supplied and reviewed.

Start with a small, fast, mobile-first site. WordPress is a practical default for a content-led site; domain ownership, hosting, privacy language, and account connection still require owner-controlled setup.

## 4. Master content package

Every episode should have:
- Unique content ID and working title.
- Approved research dossier and claim ledger.
- Audience question and intended viewer takeaway.
- Hook variants and opening visual.
- Final narration and subtitle file.
- Shot list, prompts, generated assets, and continuity references.
- Music / sound / voice provenance and license record.
- Master vertical export and platform-specific variants.
- TikTok / Shorts / Reels title, caption, hashtags, and CTA variants.
- AI disclosure decision and commercial disclosure decision.
- QA record, release approval, publication URLs, and performance record.
- Website companion brief where the topic merits search depth.

## 5. Publishing specifications

### Vertical short master
- Aspect ratio: 9:16.
- Target resolution: 1080 × 1920 where source quality permits.
- Initial duration: 35–60 seconds; extend only when narrative value justifies it.
- Burned-in captions must be legible and kept clear of platform interface zones.
- Mix voice for intelligibility on mobile speakers.
- No platform watermark on cross-posted master exports.
- Export clean master before adding platform-native overlays or music.

### YouTube long-form
- Use a documentary structure, not a stretched short.
- Build a clear title promise, opening sequence, chapters where useful, thumbnail, description, sources/notes, and end-screen pathway.
- Long-form production must have its own evidence and narrative review.
- Do not use misleading thumbnails or titles that promise a different video.

## 6. Metadata and search

For each upload:
- Identify the real question a viewer may type.
- Put the primary topic naturally in title and opening narration.
- Use concise, accurate captions/descriptions.
- Use a small number of relevant hashtags; do not keyword-stuff.
- Use platform search suggestions and Creator Search Insights only when actually accessible.
- Do not claim search volume, trend rank, or keyword demand without a valid data source.
- Maintain an internal keyword/topic map to prevent repetitive packaging.

## 7. Cross-platform adaptation

The core story remains consistent; the packaging changes:
- TikTok: immediate question, fast context, native caption and comment prompt.
- Shorts: standalone clarity and an appropriate path to a related long-form episode.
- Reels: strong visual identity, concise caption, save/share value, community context.
- YouTube long-form: deeper mechanisms, evidence, caveats, and satisfying resolution.
- Website: readable explanation, source provenance, correction/update date, and related videos.

Do not upload a video with another platform's watermark. Do not assume music rights transfer across platforms; use music cleared for each destination or an owned/licensed track.

## 8. Analytics data model

Capture a row per post per platform. Do not merge unlike platform metrics into a single total.

Suggested fields:
- content_id, platform, post_url, published_at, timezone.
- pillar, franchise, topic, language, duration_seconds.
- hook_type, opening_visual, CTA_type, caption_version.
- views, reach, impressions, engaged_views where defined by platform.
- average_watch_seconds, retention_curve, completion_rate where available.
- likes, comments, shares, saves, profile_visits, follows.
- search_views / traffic_source / search_terms where available.
- production_hours, direct_cost, paid_distribution_spend.
- sponsorship / affiliate disclosure status.
- AI disclosure status, rights status, QA status.
- notes, hypothesis, next test.

Store source exports or screenshots privately where needed. Do not commit private account analytics, personal information, access tokens, or payout data to the public repository.

## 9. Weekly decision framework

Every week:
1. Review platform-native analytics separately.
2. Compare each post to the channel's own recent baseline and to comparable duration / format groups.
3. Identify retention drop-offs and comment questions.
4. Note which pillar, hook, and narrative format produced meaningful engagement.
5. Check whether a result is repeatable across more than one post.
6. Decide: repeat, iterate, pause, or investigate.
7. Record one learning and one test for the next cycle.

A high view count alone does not establish business value. Include follows, returning viewers, saves, shares, enquiries, and audience quality.

## 10. Release checklist

Before publication:
- [ ] Research and claim ledger approved.
- [ ] Fictional assumptions are explicit.
- [ ] No unsupported scientific, medical, or current-event claims.
- [ ] Visuals match the narration and continuity rules.
- [ ] Music, footage, fonts, voices, and model assets have documented rights.
- [ ] AI disclosure applied where required.
- [ ] Commercial disclosure applied when promoting a brand, product, or service.
- [ ] Captions, spelling, pronunciation, and subtitles checked.
- [ ] Platform-specific metadata checked.
- [ ] Human owner approved release.
- [ ] Publication URL and timestamp captured after actual posting.

## 11. Access and integration boundary

Publishing and analytics are not considered connected until the relevant platform account is explicitly authorized through an available connector and the connection is confirmed. Until then, AI can prepare publication-ready assets and analyze metrics the owner supplies, but must not claim to post, schedule, or read account analytics.

