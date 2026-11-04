# WHAT IF WORLD — SOURCE & CLAIM LEDGER

## 1. Source record
Every source receives `SRC-###` and records:
- exact title and publisher/author;
- URL and access date;
- publication date;
- event date or data collection period;
- primary/secondary/tertiary classification;
- region/population/system covered;
- exact claim(s) supported;
- limitations, conflicts, and possible bias;
- whether source was opened and inspected or only surfaced in search.

A search-result snippet is discovery evidence only; inspect the underlying source before relying on it for a critical claim.

## 2. Claim record
Every material factual sentence receives `CLM-###` and records:
- exact draft claim;
- class: `FACT`, `EXTRAPOLATION`, `FICTIONAL_ASSUMPTION`;
- supporting source IDs;
- confidence: high / medium / low;
- status: `SUPPORTED`, `QUALIFIED`, `UNVERIFIED`, `REJECTED`;
- safe on-screen/VO wording;
- scope, units, timescale, and caveat.

## 3. Source quality rubric
A: primary data, official technical report, peer-reviewed paper, or direct documentation.
B: reputable secondary reporting that cites primary evidence.
C: expert commentary or review with transparent sources.
D: social post, forum, aggregator, or unattributed claim.
D may surface questions but cannot independently support a critical science claim.

## 4. Claim acceptance
- Critical mechanism/number: A preferred; otherwise two independent B sources and qualify.
- Non-critical context: B/C may be acceptable with clear wording.
- D only: do not state as fact.
- Conflicting evidence: document the disagreement; lower confidence; avoid false resolution.
- Extrapolation: show assumptions and uncertainty range where meaningful.
- Fictional assumption: disclose it as a scenario rule.

## 5. Red-team checks
Ask:
1. Does the source directly support the sentence, or merely mention the topic?
2. Are units, denominator, geography, and dates compatible?
3. Is this correlation or causation?
4. Is the number observed, modeled, projected, or illustrative?
5. Does the wording overstate certainty?
6. Is there a more recent correction or contradictory source?
7. Could a viewer mistake the fictional premise for a real event?

## 6. On-screen numbers
A number may appear only if its claim record is `SUPPORTED` or appropriately `QUALIFIED`, includes unit and basis, and is readable at mobile size. Otherwise remove it or convert to a non-quantitative explanation.
