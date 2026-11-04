# WHAT IF WORLD — DAILY INTELLIGENCE PROTOCOL V3

## Objective
Find evidence-backed questions worth investigating. Trend signals guide discovery; they do not dictate science or editorial conclusions.

## Source lanes
1. TikTok: native Creative Center/search insights when accessible; otherwise identify the third-party tracker and its coverage date. Never present proxy data as native platform analytics.
2. Search: Google Trends or a named alternative; record geography, date window, query, comparison set, and displayed metric.
3. News/events: primary authority/operator first; reputable media for context and discovery.
4. Science: peer-reviewed literature, official scientific bodies, technical reports, universities, and primary datasets.
5. Public discussion: use as a signal of audience questions, not proof of scientific claims.

## Freshness labels
- `FRESH_0_7D`: publication or measured signal within 0–7 days.
- `CONTEXT_8_30D`: useful context from 8–30 days.
- `EVERGREEN`: no current-trend claim.
Separate event date from article publication date and data collection period.

## Daily process
1. Set report timestamp in Asia/Jakarta and UTC.
2. Record which sources were actually accessed and which were inaccessible.
3. Capture source URL, publisher, title, publication date, event/data date, region, metric, and limitations.
4. Cluster repeated signals; a single post/article is not a trend.
5. Search primary sources for scientific mechanisms and relevant official context.
6. Compare with `05_ARSIP_KONTEN.md` and `09_IDEA_BACKLOG.md`.
7. Create 3–5 candidates with evidence labels and scorecard.
8. Recommend one candidate; include a clear trade-off.
9. Ask user to select. Do not auto-generate final script, prompts, or production dossier.

## Candidate mix
Aim for a mix of current and evergreen/original ideas. Prefer Indonesian relevance when evidence supports it. If there is no reliable current trend, state that plainly and do not force one.

## Daily report schema
- Report ID, date/time, region, coverage, source access status.
- TikTok signal summary.
- Search signal summary.
- News/public-interest summary.
- Scientific discovery/context.
- 3–5 idea cards with evidence, risk, sources, score.
- Best recommendation and trade-off.
- User decision: pending / selected / rejected / deferred.

## Integrity rules
- Never invent rankings, views, growth, search volume, publication dates, quotes, or sources.
- No “viral” or “best posting time” claim without account-level analytics.
- Do not infer national interest from local sample data.
- Avoid stale article repackaging as current news.
- If the report is truncated, missing key sources, or failed, refresh research before using it.
- Automation completion does not equal evidence verification or human approval.
