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


---

## Daily research provenance — DI-20261105-01

- Run date/time: 2026-11-05 08:02 WIB (Asia/Jakarta).
- Observation window: 2026-10-29 through 2026-11-05.
- Audience/region: Indonesia.
- Research mode: fresh public-web research; source pages opened and inspected.
- Internal deduplication: canonical archive and idea backlog read from this branch. No archive or backlog mutation performed.
- User-facing output: exactly three candidates; no production dossier created.

### Platform access log

- TikTok Creative Center: the requested trends page redirected to a login-only Creative Center shell; no Indonesian hashtag/video trend metrics were exposed.
- Google Trends Indonesia: the requested trending-search URL was inaccessible in this session; no current search-volume or ranking claim is made.
- TikTok account analytics: no connected account analytics were available.
- Third-party trend trackers were not treated as native TikTok/Google evidence and were not used to support a trend claim.

### Source records

#### SRC-001 — NASA Swift re-entry confirmation
- Exact title: “NASA’s Swift Observatory Re-Entered Atmosphere”.
- Publisher: NASA Science / Goddard Space Flight Center.
- URL: https://science.nasa.gov/blogs/swift/2026/11/02/nasas-swift-observatory-to-re-enter-atmosphere/
- Publication: original page 2026-11-02; editor update confirming re-entry 2026-11-04.
- Event: 2026-11-04, 7:39 a.m. EST / 12:39 UTC / 19:39 WIB.
- Classification: primary official agency source.
- Scope: Neil Gehrels Swift Observatory; re-entry over North Sumatra, Indonesia, approximately 3.4° N, 98.6° E.
- Claims: CLM-001, CLM-002.
- Limitation: NASA says most of the spacecraft was expected to burn up and some components may have survived; this page does not establish a ground impact.

#### SRC-002 — Independent Swift re-entry reporting
- Exact title: “NASA's 22-year-old Swift satellite telescope falls from orbit in fiery finale”.
- Publisher: Reuters; reporter Steve Gorman.
- URL: https://www.reuters.com/science/nasas-22-year-old-swift-satellite-telescope-falls-orbit-fiery-finale-2026-11-04/
- Publication: 2026-11-04.
- Event: 2026-11-04.
- Classification: secondary reporting; independent cross-check of NASA/US Space Force confirmation.
- Scope: Swift re-entry over North Sumatra; Reuters reports no damage or injuries on the ground.
- Claims: CLM-001, CLM-002.
- Limitation: secondary report; no independent ground survey of every possible fragment.

#### SRC-003 — ESA Space Environment Report 2026
- Exact title: “ESA Space Environment Report 2026”.
- Publisher: European Space Agency.
- URL: https://www.esa.int/articles/esa-space-environment-report-2026
- Publication: 2026-09-14.
- Data period: through 2025-12-31.
- Classification: primary institutional technical report.
- Scope: global Earth orbital environment.
- Claims: CLM-003, CLM-004.
- Limitations: not a live November 2026 count. Its average of more than three intact satellites or rocket bodies re-entering per day and around ten payloads launched per day describes the report's 2025 data basis. Collision-cascade projections are long-term scenarios, not an imminent event forecast.

#### SRC-004 — Satellite Earth-observation applications
- Exact title: “ESA for Earth”.
- Publisher: European Space Agency.
- URL: https://www.esa.int/Applications/Observing_the_Earth/ESA_for_Earth
- Publication date: not displayed; accessed 2026-11-05.
- Classification: official institutional explainer.
- Scope: Earth-observation satellite applications.
- Claims: CLM-005.
- Limitations: examples include weather forecasting, agriculture, maritime safety, and disaster response; the page does not establish that loss of any single satellite would disable those services in Indonesia.

#### SRC-005 — BMKG weekly forecast and hotspot monitoring
- Exact title: “Prakiraan Cuaca Indonesia Sepekan Periode 3–10 November 2026: Hujan Berpeluang Terjadi di Sejumlah Wilayah, Panas dan Kering Masih Bertahan di Wilayah Lain”.
- Publisher: BMKG.
- URL: https://www.bmkg.go.id/cuaca/potensi-hujan-sepekan/prakiraan-cuaca-indonesia-sepekan-periode-3-10-november-2026-hujan-berpeluang-terjadi-di-sejumlah-wilayah-panas-dan-kering-masih-bertahan-di-wilayah-lain
- Publication: 2026-11-05.
- Data periods: maximum daily temperatures 2026-10-29 to 2026-11-01; hotspot observations during the preceding 10 days.
- Classification: primary official meteorological agency source.
- Scope: Indonesia; high-confidence hotspots reported in Papua Selatan (685), Sumatera Selatan (168), and Sulawesi Tenggara (167); smoke observed in parts of Jambi, Kalimantan Tengah, Maluku, and Papua Selatan.
- Claims: CLM-006.
- Limitations: BMKG explicitly states hotspots do not always represent an actual fire. Temperature and rainfall figures are regional observations, not national uniform conditions.

#### SRC-006 — BMKG Papua Selatan fire response
- Exact title: “BMKG Dukung Penanganan Karhutla dan Antisipasi Banjir di Papua Selatan”.
- Publisher: BMKG.
- URL: https://www.bmkg.go.id/berita/bmkg-dukung-penanganan-karhutla-dan-antisipasi-banjir-di-papua-selatan
- Publication: 2026-11-02.
- Event: coordination in Merauke on 2026-10-31; weather-modification operation described for 2026-10-22 through 2026-11-05.
- Classification: primary official agency source.
- Scope: Papua Selatan.
- Claims: CLM-006, CLM-007.
- Limitations: operational update for a defined region; not evidence that all high-confidence hotspots across Indonesia are confirmed fires.

#### SRC-007 — GAMBUT peat-fire field experiment
- Exact title: “GAMBUT field experiment of peatland wildfires in Sumatra: from ignition to spread and suppression”.
- Authors: Muhammad A. Santoso, Eirik G. Christensen, Hafiz M. F. Amin, Pither Palamba, Yuqi Hu, et al.
- Journal: International Journal of Wildland Fire, 2022, volume 31, issue 10, pages 949–966.
- DOI: https://doi.org/10.1071/WF21135
- Institutional record: https://dara.ui.ac.id/research-output/879d54fe-9982-4d95-a2e8-434fb9db60ea
- Publication: 2022.
- Data period: field experiment monitored over 4–10 days and nights, including three major rainfall events.
- Classification: peer-reviewed primary field research.
- Scope: degraded peatland in Sumatra.
- Claims: CLM-008.
- Limitations: experimental findings are site- and condition-specific. The 4–10-day observation window must not be presented as a universal duration for peat fires. The paper reports smouldering combustion and lethal biological-system effects in peat to 30 cm depth at the experimental site.

#### SRC-008 — Oxford summary of seabird clock-shift study
- Exact title: “Study finds that long-distance flights can throw seabirds' internal clocks out of sync, causing navigation errors”.
- Publisher: University of Oxford.
- URL: https://www.ox.ac.uk/news/2026-10-26-study-finds-that-long-distance-flights-can-throw-seabirds-internal-clocks-out-of
- Publication: 2026-10-30.
- Research data: 20 years of GPS tracking, 1,045 Manx shearwaters, 3,688 foraging trips.
- Classification: primary institutional research communication from the lead university.
- Scope: Manx shearwaters (Puffinus puffinus) breeding on islands off the UK and Ireland; Atlantic foraging and homing flights.
- Claims: CLM-009.
- Limitations: findings are species- and route-specific. The release reports navigational deviations up to approximately 15° and a possible internal-clock lag up to around one hour. Health, feeding, and survival consequences were not established.

#### SRC-009 — Peer-reviewed seabird navigation paper
- Exact title: “Rapid longitudinal flights cause time shifts and Sun compass error”.
- Authors: Patrick Lewin, Joe Wynn, Joe Morford, et al.
- Journal: Science, volume 394, issue 6823, pages 520–524.
- Publication: 2026-10-29.
- DOI: https://doi.org/10.1126/science.adz2542
- Classification: peer-reviewed primary research.
- Scope: Manx shearwater GPS navigation study.
- Claims: CLM-009.
- Inspection status: Science full-text page returned HTTP 403 in this session; metadata/abstract were surfaced, while the lead-university summary and independent Reuters report were opened and inspected.

#### SRC-010 — Independent seabird study reporting
- Exact title: “Long-distance flights can interfere with the internal clocks of seabirds”.
- Publisher: Reuters; reporter Marta Serafinko.
- URL: https://www.reuters.com/science/long-distance-flights-can-interfere-with-internal-clocks-seabirds-2026-10-30/
- Publication: 2026-10-30.
- Classification: secondary independent reporting.
- Scope: Manx shearwaters and Atlantic homing flights.
- Claims: CLM-009.
- Limitations: reports that effects on feeding, rest, and broader health have not yet been investigated.

#### SRC-011 — Indonesia migratory-waterbird context
- Exact title: “Jenis”.
- Publisher: Wetlands International Indonesia.
- URL: https://indonesia.wetlands.org/id/pendekatan-kami/likungan-lahan-basah-yang-sehat/jenis/
- Publication date: not displayed; accessed 2026-11-05.
- Classification: institutional conservation explainer.
- Scope: Indonesian waterbirds and the East Asian–Australasian Flyway.
- Claims: CLM-010.
- Limitations: contextual evidence only. It does not show that Manx shearwater clock-shift findings have been observed in Indonesian migratory species.

#### SRC-012 — Mars hydrogen-chloride research communication
- Exact title: “Хлороводород в атмосфере Марса может быть признаком действующего вулканизма” (Hydrogen chloride in Mars' atmosphere may be a sign of ongoing volcanism).
- Publisher: Space Research Institute of the Russian Academy of Sciences (IKI RAN).
- URL: https://iki.cosmos.ru/news/2026/11/04/khlorovodorod-v-atmosfere-marsa-mozhet-byt-priznakom-deystvuyuschego-vulkanizma
- Publication: 2026-11-04.
- Classification: institutional research communication from an instrument/research institute involved in the study.
- Scope: hydrogen-chloride observations by the ACS instrument aboard ExoMars Trace Gas Orbiter, localized near Alba Mons.
- Claims: CLM-011, CLM-012.
- Limitations: possible magmatic source is an interpretation. No observed lava flow or eruption is reported.

#### SRC-013 — Independent Mars research reporting
- Exact title: “Pungent gas above Martian fissures hints at ongoing volcanism”.
- Publisher: Reuters; reporter Will Dunham.
- URL: https://www.reuters.com/science/pungent-gas-above-martian-fissures-hints-ongoing-volcanism-2026-11-04/
- Publication: 2026-11-04.
- Classification: secondary independent reporting.
- Scope: hydrogen chloride above fissures near Alba Mons.
- Claims: CLM-011, CLM-012.
- Limitations: supports the interpretation as a possibility, not a confirmed eruption or evidence of life.

### Claim records

#### CLM-001 — Swift re-entry location and timing
- Draft claim: NASA and the U.S. Space Force confirmed that the Neil Gehrels Swift Observatory re-entered the atmosphere on 2026-11-04 at 7:39 a.m. EST (12:39 UTC; 19:39 WIB) over North Sumatra, approximately 3.4° N, 98.6° E.
- Class: FACT.
- Sources: SRC-001, SRC-002.
- Confidence: high.
- Status: SUPPORTED.
- Safe wording: “Satelit observatorium Swift kembali memasuki atmosfer di atas wilayah Sumatera Utara pada 4 November 2026.”
- Scope/caveat: re-entry region is approximate; do not infer a precise ground impact point.

#### CLM-002 — Re-entry burn-up and ground outcome
- Draft claim: most of Swift was expected to burn up during atmospheric re-entry; some components may have survived, while Reuters reported no ground damage or injuries.
- Class: FACT.
- Sources: SRC-001, SRC-002.
- Confidence: high for NASA's expectation and Reuters' reported ground outcome.
- Status: QUALIFIED.
- Safe wording: “Sebagian besar diperkirakan terbakar; beberapa komponen mungkin bertahan. Tidak ada kerusakan atau korban di darat yang dilaporkan.”
- Caveat: avoid claiming every fragment's fate is known.

#### CLM-003 — Orbital traffic and re-entry baseline
- Draft claim: ESA's 2026 report, using data through the end of 2025, reports an average of more than three intact satellites or rocket bodies re-entering per day and around ten new payloads launched daily.
- Class: FACT.
- Sources: SRC-003.
- Confidence: high.
- Status: SUPPORTED.
- Safe wording: “Laporan ESA berbasis data 2025 mencatat lebih dari tiga objek utuh kembali memasuki atmosfer per hari secara rata-rata.”
- Caveat: historical annual average, not a live count for 2026-11-05.

#### CLM-004 — Orbital collision cascade
- Draft claim: collisions can create fragments that trigger further collisions; without mitigation and active debris removal, some orbital regions could become increasingly unsafe or unusable over the long term.
- Class: EXTRAPOLATION grounded in an ESA technical scenario.
- Sources: SRC-003.
- Confidence: medium-high.
- Status: QUALIFIED.
- Safe wording: “Dalam skenario jangka panjang, tabrakan berantai dapat membuat sebagian orbit semakin sulit digunakan.”
- Caveat: not imminent, not inevitable, and not equivalent to all satellites failing simultaneously.

#### CLM-005 — Human uses of satellite observation
- Draft claim: satellite observations support weather forecasting, agricultural decisions, maritime safety, and disaster response.
- Class: FACT.
- Sources: SRC-004.
- Confidence: high.
- Status: SUPPORTED.
- Safe wording: “Data satelit membantu pemantauan cuaca, pertanian, keselamatan maritim, dan respons bencana.”
- Caveat: do not imply that losing one satellite would disable these services.

#### CLM-006 — BMKG heat, hotspot, and smoke observations
- Draft claim: BMKG's 2026-11-05 outlook reports maximum daily temperatures above 37°C in five named provinces during 2026-10-29 to 2026-11-01; high-confidence hotspot detections during the preceding ten days were highest in Papua Selatan (685), Sumatera Selatan (168), and Sulawesi Tenggara (167); smoke was observed in parts of Jambi, Kalimantan Tengah, Maluku, and Papua Selatan.
- Class: FACT.
- Sources: SRC-005, SRC-006.
- Confidence: high for what BMKG reported.
- Status: SUPPORTED.
- Safe wording: cite the exact observation period and say “hotspot terdeteksi”, not “kebakaran terkonfirmasi”.
- Caveat: BMKG explicitly says a hotspot does not always indicate an actual fire; regional rainfall and temperature conditions differ.

#### CLM-007 — Current Papua Selatan response context
- Draft claim: BMKG reported ongoing support for karhutla response and flood preparedness in Papua Selatan, with weather-modification operations and a shift toward increased rainfall potential.
- Class: FACT.
- Sources: SRC-006.
- Confidence: high.
- Status: SUPPORTED.
- Safe wording: “Papua Selatan menghadapi kebutuhan penanganan karhutla sekaligus kesiapsiagaan terhadap hujan dan banjir.”
- Caveat: specific to Papua Selatan and the operational dates in the report.

#### CLM-008 — Peat smouldering mechanism
- Draft claim: peat fires can smoulder without visible flames, persist below the surface, release carbon and toxic gases, and damage peat biological systems at depth. A Sumatra field experiment measured severe thermal effects down to 30 cm in the experimental peat.
- Class: FACT.
- Sources: SRC-007.
- Confidence: high for the experimental site and observed mechanism.
- Status: QUALIFIED.
- Safe wording: “Api gambut dapat membara tanpa nyala besar di permukaan; kedalaman dan lamanya bergantung pada kondisi gambut, air, dan cuaca.”
- Caveat: do not universalize the experiment's 4–10-day observation window or 30 cm measurement to every peat fire.

#### CLM-009 — Manx shearwater clock-shift and Sun-compass error
- Draft claim: rapid eastward homing flights can leave Manx shearwaters' internal clocks behind local solar time by up to around one hour, producing systematic Sun-compass errors; the study reports deviations up to approximately 15°.
- Class: FACT.
- Sources: SRC-008, SRC-009, SRC-010.
- Confidence: high for the studied species and routes.
- Status: SUPPORTED.
- Safe wording: “Pada Manx shearwater yang diteliti, pergeseran jam biologis saat terbang cepat ke timur berkaitan dengan kesalahan arah kompas Matahari.”
- Caveat: do not generalize to all bird species or claim measured health/survival effects.

#### CLM-010 — Indonesian flyway context
- Draft claim: Indonesia is part of the East Asian–Australasian Flyway and supports a large diversity of waterbirds, including migratory species.
- Class: FACT.
- Sources: SRC-011.
- Confidence: high for the institutional context statement.
- Status: SUPPORTED.
- Safe wording: “Indonesia berada di jalur migrasi burung air Asia Timur–Australasia.”
- Caveat: this does not prove the Manx shearwater clock-shift mechanism occurs in Indonesian species.

#### CLM-011 — Mars hydrogen-chloride detection
- Draft claim: the ExoMars Trace Gas Orbiter's ACS instrument detected hydrogen chloride with an unusual seasonal and geographic pattern near Alba Mons.
- Class: FACT.
- Sources: SRC-012, SRC-013.
- Confidence: high for the reported detection.
- Status: SUPPORTED.
- Safe wording: “Peneliti melaporkan pola gas hidrogen klorida yang terlokalisasi di atas wilayah Alba Mons.”
- Caveat: detection is not itself a direct observation of an eruption.

#### CLM-012 — Possible present-day magmatic activity on Mars
- Draft claim: researchers interpret the localized hydrogen-chloride signal and nearby fissures as potentially consistent with magmatic gas seepage from below the surface.
- Class: EXTRAPOLATION.
- Sources: SRC-012, SRC-013.
- Confidence: medium.
- Status: QUALIFIED.
- Safe wording: “Temuan ini mengisyaratkan kemungkinan sumber magmatik di bawah permukaan Mars.”
- Caveat: no active lava flow or eruption was observed; no evidence of life was found.

### Candidate mapping and editorial scores

Scoring order: freshness/relevance, scientific foundation, human stakes, visual originality, story potential, novelty, Indonesian relevance. Each dimension is rated 0–5 and converted using the official weights.

- Candidate DI-20261105-01-A, orbital debris/collision cascade: 5 / 4.5 / 4 / 5 / 4.5 / 4 / 5 = 91/100. Evidence label CURRENT_VERIFIED for the current re-entry signal; the collision scenario remains a qualified long-term extrapolation. Sources CLM-001–CLM-005.
- Candidate DI-20261105-01-B, underground peat smouldering: 5 / 4.5 / 5 / 4.5 / 4.5 / 4.5 / 5 = 93/100. Evidence label CURRENT_LIMITED because current hotspots are not confirmed fires; mechanism is peer-reviewed. Sources CLM-006–CLM-008.
- Candidate DI-20261105-01-C, migratory-bird jet lag: 5 / 5 / 3 / 4.5 / 4.5 / 4.5 / 3.5 = 88/100. Evidence label CURRENT_VERIFIED for the Manx shearwater study; application to Indonesian species remains unverified. Sources CLM-009–CLM-010.

### Editorial disposition
- Main recommendation: DI-20261105-01-B, underground peat smouldering, due to strong Indonesian relevance, clear human stakes, and a distinctive visual/scientific mechanism.
- No final script, voice-over, Google Flow prompt, caption, or production dossier created.
- No content archive or idea backlog record created or modified; approval is still required before a candidate becomes an approved production concept.


---

## Research provenance — WW-005 / IDEA-20261105-05

- Research dossier: `RESEARCH_IDEA-20261105-05.md`
- Research run: `DI-20261105-03` (candidate IDE 02 selected by Human Producer on 2026-11-05).
- Research timestamp: 2026-11-05 16:38:24 WIB (Asia/Jakarta).
- Observation/current-data focus: 2026 Antarctic ozone-hole season; supporting treaty, model, and scientific assessment sources.
- Internal deduplication: archive and backlog read on active feature branch. The selected question is not present as a production in the canonical archive; no equivalent ozone scenario appears in the current backlog.
- Research status: draft complete; producer science review required. No STORY or production prompts created.

### Source records

#### SRC-033 — NOAA/NASA 2026 ozone-hole measurement release
- Title: “NOAA, NASA release measurements of 2026 ozone hole”.
- Publisher: NOAA; joint NOAA/NASA analysis; named experts Paul Newman and Amy Butler.
- URL: https://www.noaa.gov/news-release/noaa-nasa-release-measurements-of-2026-ozone-hole
- Published: 2026-11-04.
- Data: seasonal mean 2026-09-07 to 2026-10-13; maximum area 2026-09-18; South Pole minimum ozone 2026-10-17.
- Accessed: 2026-11-05.
- Type/scope: primary institutional science-agency summary; Antarctic ozone satellite monitoring and balloon/ozonesonde observations.
- Claims: CLM-033–CLM-037.
- Inspection: full release opened; metrics, named expert statements, and mechanism explanation inspected.
- Limits: not a fresh raw-data reprocessing; 1–2 million square mile counterfactual is an attributed estimate. NASA/NOAA release is joint reporting, not two independent datasets.

#### SRC-034 — NASA 2026 ozone-hole explainer
- Title: “NASA, NOAA Track 2026 Antarctic Ozone Hole”; Sally Younger, NASA Science.
- URL: https://science.nasa.gov/earth/2026-ozone-hole/
- Published: 2026-11-04; accessed: 2026-11-05.
- Type/scope: primary institutional science-agency communication using joint NASA/NOAA data.
- Claims: CLM-033–CLM-036.
- Inspection: full page opened.
- Limits: shares the underlying joint analysis with SRC-033; not independent replication.

#### SRC-035 — Peer-reviewed no-regulation model
- Title: “What would have happened to the ozone layer if chlorofluorocarbons (CFCs) had not been regulated?”
- Authors: Newman et al.
- Journal: Atmospheric Chemistry and Physics 9, 2113–2128 (2009).
- DOI: 10.5194/acp-9-2113-2009.
- URL: https://acp.copernicus.org/articles/9/2113/2009/
- Published: 2009-03-23; accessed: 2026-11-05.
- Type/scope: peer-reviewed primary coupled radiation-chemical-dynamical modelling study.
- Claims: CLM-038, CLM-039.
- Inspection: publisher full-text page and abstract opened.
- Limits: scenario assumes no regulation and 3% annual ODS production growth; outcomes are modelled, not observations or deterministic forecasts.

#### SRC-036 — WMO Scientific Assessment of Ozone Depletion 2022
- Publisher: WMO, GAW Report No. 278.
- URL: https://csl.noaa.gov/assessments/ozone/2022/executivesummary/
- Published: 2022; accessed: 2026-11-05.
- Type/scope: authoritative international scientific assessment of ozone chemistry, observed changes, and future projections.
- Claims: CLM-037, CLM-039–CLM-041.
- Inspection: full executive summary and Antarctic future-evolution section opened.
- Limits: projections depend on emissions and climate assumptions; recovery date is a model benchmark with range.

#### SRC-037 — UN Treaty Collection: Montreal Protocol status
- Publisher: United Nations Office of Legal Affairs, Treaty Section.
- URL: https://treaties.un.org/Pages/ViewDetails.aspx?chapter=27&clang=_en&mtdsg_no=XXVII-2-a&src=TREATY
- Status page: 2026-11-03; treaty adopted 1987-09-16; entered into force 1989-01-01; accessed 2026-11-05.
- Type/scope: primary legal registry.
- Claims: CLM-042.
- Inspection: treaty status and metadata page opened.
- Limits: party count is a time-stamped legal registry snapshot.

#### SRC-038 — UNEP Ozone Secretariat treaty overview
- Publisher: UNEP Ozone Secretariat.
- URL: https://ozone.unep.org/treaties/montreal-protocol
- Accessed: 2026-11-05; publication date not displayed.
- Type/scope: official treaty explainer on ODS production/consumption phase-out.
- Claims: CLM-042.
- Inspection: official page text inspected.
- Limits: overview, not a compliance audit.

#### SRC-039 — NASA Ozone Watch data definition
- Publisher: NASA Goddard Space Flight Center.
- Title: “2026 Antarctic OMPS and MERRA-2 Ozone”.
- URL: https://ozonewatch.gsfc.nasa.gov/meteorology/SH.html
- Data period: 2026; accessed: 2026-11-05.
- Type/scope: primary agency data portal for Antarctic total-column ozone and area statistics.
- Claims: CLM-034.
- Inspection: portal definition and daily progression description inspected.
- Limits: raw time-series were not downloaded or independently recalculated.

### Claim records

- CLM-033 FACT — 2026 seasonal mean area about 25 million km², seventh-largest in 48 years; SRC-033, SRC-034; HIGH/SUPPORTED.
- CLM-034 FACT — 2026 one-day maximum 27.1 million km² on 18 Sep; area definition below 220 DU south of 40°S; SRC-033, SRC-034, SRC-039; HIGH/SUPPORTED.
- CLM-035 FACT — unusually strong/large polar vortex and weak planetary-wave activity contributed to favourable ozone-loss conditions in 2026; SRC-033, SRC-034; HIGH/SUPPORTED.
- CLM-036 EXTRAPOLATION — Paul Newman estimated 2026 area could be 1–2 million square miles larger if ODS levels matched their 2000 peak; SRC-033, SRC-034; MEDIUM/QUALIFIED.
- CLM-037 FACT — chlorine/bromine activation on polar stratospheric cloud surfaces and catalytic ozone destruction after sunlight returns; SRC-033, SRC-034, SRC-036; HIGH/SUPPORTED.
- CLM-038 EXTRAPOLATION — 2009 coupled model with no regulation and 3% annual ODS production growth projected global column-ozone losses of 17% by 2020 and 67% by 2065 versus 1980; SRC-035; HIGH for model output, MEDIUM for real counterfactual/QUALIFIED.
- CLM-039 EXTRAPOLATION — same model projected year-round polar depletion and >2× erythemal UV in northern summer mid-latitudes by 2060; SRC-035, SRC-036; MEDIUM/QUALIFIED.
- CLM-040 FACT — chlorine/bromine participate in catalytic cycles and are regenerated; SRC-036; HIGH/SUPPORTED.
- CLM-041 EXTRAPOLATION — Antarctic total-column ozone projected to return to 1980 value around 2066, model range 2049–2077, under continued compliance; SRC-036; MEDIUM/QUALIFIED.
- CLM-042 FACT — Montreal Protocol adopted 1987-09-16, entered into force 1989-01-01, 198 parties on 2026-11-03 registry; SRC-037, SRC-038; HIGH/SUPPORTED.


---

## Research provenance — DI-20261105-02 / IDEA-20261105-02 / WW-006

- Research run: 2026-11-05; public sources inspected during the current RESEARCH stage.
- Selected candidate: IDEA-20261105-02 — “Bisakah Batu Venus Menyimpan Jejak Air Purba?”
- Selection mapping: the preceding user-facing shortlist called this “IDE 01”; the canonical Daily Intelligence report records it as candidate IDEA-20261105-02. The canonical report ID is retained to avoid inventing a second idea identity.
- Production ID: WW-006 (next available after WW-003, WW-004, and WW-005 in the active branch).
- Branch: feat/v3.2-character-reference-system.
- Scope: mineral alteration under simulated present-day Venus surface conditions and the conditional value of fluorinated hydrous minerals as possible indicators of an earlier water-rich period.
- Evidence label: CURRENT_VERIFIED for the newly published peer-reviewed experimental study and traceable supporting literature; this label does not mean minerals have been detected on Venus or that the topic is trending on social platforms.
- Archive/backlog: inspected; no matching production entry found in the canonical production register. No archive/backlog mutation performed at RESEARCH stage.
- Platform analytics: TikTok Creative Center, Google Trends, and private TikTok account analytics were not accessed in this research pass.

### Source records

#### SRC-040 — Primary experimental study
- Title: “New Insights into Venus’s Volatile Cycles Revealed by the Formation of Magnesite and Fluoro–Micas”
- Authors: Sara Taeko Port, Maitrayee Bose, Jean-Philippe Harvey, Dorothy Lukco, Tibor Kremic, Gary Hunter.
- Journal: The Planetary Science Journal 7, 247 (2026); published 2026-10-30.
- DOI: https://doi.org/10.3847/PSJ/aea909
- URL: https://iopscience.iop.org/article/10.3847/PSJ/aea909
- Accessed: 2026-11-05.
- Type/scope: peer-reviewed primary laboratory research; six minerals tested in NASA Glenn Research Center’s GEER under simulated Venus surface conditions.
- Method: 60 days at 460 ± 0 °C and 93 ± 1 bar; simulated atmospheric gas mixture; XRD, XPS, microscopy/spectroscopy and thermodynamic calculations.
- Inspection: publisher-indexed article content exposed abstract, methods, results, discussion and summary excerpts. Direct DOI/publisher-page retrieval failed in this session; complete publisher HTML and supplementary dataset were not independently downloaded.
- Claims: CLM-044–CLM-047.
- Limitations: laboratory simulation, selected starting minerals and finite experimental duration; does not establish natural abundance, in-situ occurrence or geological-timescale rates on Venus. Magnesite formation from brucite is not by itself proof of ancient surface liquid water.

#### SRC-041 — Peer-reviewed Venus surface mineralogy review
- Title: “Mineralogy of the Venus Surface”
- Authors: Martha S. Gilmore, M. Darby Dyar, Nils Mueller, Jérémy Brossier, Alison R. Santos, Mikhail Ivanov, Richard Ghail, Justin Filiberto, Jörn Helbert, et al.
- Journal: Space Science Reviews 219, article 52 (2023); published 2023-09-20.
- DOI: https://doi.org/10.1007/s11214-023-00988-6
- URL: https://link.springer.com/article/10.1007/s11214-023-00988-6
- Accessed: 2026-11-05.
- Type/scope: peer-reviewed synthesis of lander measurements, remote sensing, laboratory experiments and thermodynamic modelling.
- Inspection: full open-access article page opened; abstract and relevant mineralogy/measurement statements inspected.
- Claims: CLM-043, CLM-047, CLM-048.
- Limitations: synthesis of limited landed measurements and remote-sensing proxies; not a new in-situ mineral survey.

#### SRC-042 — NASA planetary reference
- Title: “Venus: Facts”; NASA Science.
- URL: https://science.nasa.gov/venus/venus-facts/
- Accessed: 2026-11-05.
- Type/scope: official reference for Venus surface temperature, pressure and atmosphere.
- Inspection: page opened.
- Claims: CLM-043.
- Limitations: rounded reference values; conditions vary with elevation.

#### SRC-043 — Primary ancient-Venus climate model
- Title: “Was Venus the first habitable world of our solar system?”
- Authors: M. J. Way, Anthony D. Del Genio, Nancy Y. Kiang, Linda E. Sohl, David H. Grinspoon, Igor Aleinov, Maxwell Kelley, Thomas Clune.
- Journal: Geophysical Research Letters 43(16), 8376–8383 (2016); published 2016-08-11.
- DOI: https://doi.org/10.1002/2016GL069790
- URL: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/2016GL069790
- Accessed: 2026-11-05.
- Type/scope: peer-reviewed primary 3-D climate modelling of selected ancient-Venus scenarios.
- Inspection: publisher PDF opened; abstract and introduction inspected.
- Claims: CLM-049, CLM-050.
- Limitations: depends on assumed early atmosphere, ocean inventory, topography, solar input and rotation; not observation or proof of an ancient ocean.

#### SRC-044 — Primary Venus atmospheric isotope measurement
- Title: “Venus was wet: a measurement of the ratio of deuterium to hydrogen”
- Authors: T. M. Donahue, J. H. Hoffman, R. R. Hodges Jr., A. J. Watson.
- Journal: Science 216(4546), 630–633 (1982); published 1982-05-07.
- DOI: https://doi.org/10.1126/science.216.4546.630
- URL: https://pubmed.ncbi.nlm.nih.gov/17783310/
- Accessed: 2026-11-05.
- Type/scope: primary atmospheric isotope measurement using Pioneer Venus probe data.
- Inspection: PubMed record and abstract opened; full Science article not inspected.
- Claims: CLM-049.
- Limitations: indirect inference; depends on assumptions about sources, sinks and escape.

#### SRC-045 — Alternative interpretation of Venus D/H
- Title: “Was venus wet? Deuterium reconsidered”
- Author: David H. Grinspoon.
- Journal: Science 238(4834), 1702–1704 (1987); published 1987-12-18.
- DOI: https://doi.org/10.1126/science.238.4834.1702
- URL: https://pubmed.ncbi.nlm.nih.gov/17737672/
- Accessed: 2026-11-05.
- Type/scope: peer-reviewed alternative interpretation of Venus atmospheric isotope evidence.
- Inspection: PubMed record and abstract opened; full Science article not inspected.
- Claims: CLM-049.
- Limitations: alternative interpretation, not definitive disproof of past water.

#### SRC-046 — Venus evolution and mission science review
- Title: “Venus Evolution Through Time: Key Science Questions, Selected Mission Concepts and Future Investigations”
- Lead authors: Thomas Widemann, Suzanne E. Smrekar, James B. Garvin, et al.
- Journal: Space Science Reviews 219, article 56 (2023); published 2023-10-03.
- DOI: https://doi.org/10.1007/s11214-023-00992-w
- URL: https://link.springer.com/article/10.1007/s11214-023-00992-w
- Accessed: 2026-11-05.
- Type/scope: peer-reviewed multi-author synthesis of Venus evolution questions and future mission investigations.
- Inspection: full open-access article page opened; relevant sections on tesserae, mineral composition and unresolved interpretations inspected.
- Claims: CLM-048, CLM-050.
- Limitations: identifies open questions and candidate interpretations; does not establish that tesserae are felsic, hydrated or evidence of an ocean.

### Claim records

- CLM-043 FACT — Venus surface reference conditions are approximately 460–467 °C and 92–93 bar; SRC-040, SRC-041, SRC-042; HIGH/SUPPORTED. Safe wording: “Permukaan Venus bersuhu sekitar 460 derajat Celsius, dengan tekanan sekitar 92–93 kali tekanan udara di permukaan laut Bumi.” Conditions vary with elevation.
- CLM-044 FACT — six selected minerals were exposed for 60 days in GEER at 460 ± 0 °C and 93 ± 1 bar under a simulated Venus gas mixture; SRC-040; HIGH/SUPPORTED. Safe wording: “Enam jenis mineral diuji selama 60 hari dalam kondisi laboratorium yang meniru suhu dan tekanan permukaan Venus.” This is a controlled laboratory test, not a stay on Venus or a simulation of every geological process.
- CLM-045 FACT — brucite partly transformed; XRD identified magnesite and periclase while residual brucite remained; SRC-040; HIGH/SUPPORTED. Safe wording: “Brucite berubah sebagian dan menghasilkan magnesite dalam eksperimen simulasi Venus.” Do not claim this reaction was observed on Venus or that it proves an ancient ocean.
- CLM-046 FACT — phlogopite and muscovite reacted with HF to form fluorine-bearing mica phases through partial OH-to-F substitution; SRC-040; HIGH/SUPPORTED. Safe wording: “Fluor menggantikan sebagian gugus hidroksil pada dua jenis mika dalam eksperimen.” This is a laboratory result, not an in-situ detection.
- CLM-047 EXTRAPOLATION — fluorination may increase thermal stability; future detection plus geological context could help test a past water-richer origin; SRC-040, SRC-041; MEDIUM/QUALIFIED. Safe wording: “Jika mineral mika berfluor seperti ini ditemukan di Venus, mineral itu mungkin menjadi petunjuk sejarah air planet tersebut.” Detection alone would not prove oceans, habitability or life.
- CLM-048 FACT — as of the 2023 review, comprehensive in-situ mineralogical confirmation of Venus surface assemblages was not available; interpretations rely on limited lander data, remote sensing, experiments and models; SRC-041, SRC-046; HIGH/QUALIFIED. Safe wording: “Komposisi mineral permukaan Venus masih belum dipetakan secara langsung dan menyeluruh.” Recheck mission updates before STORY and release.
- CLM-049 FACT + EXTRAPOLATION — published D/H measurements and interpretations differ; past water loss is one interpretation, while a steady-state alternative has been proposed; SRC-043, SRC-044, SRC-045; HIGH for existence of disagreement, MEDIUM for water-history inference/QUALIFIED. Safe wording: “Isotop hidrogen memberi petunjuk, tetapi sejarah air Venus masih diperdebatkan.” D/H alone is not proof of a large ancient ocean.
- CLM-050 EXTRAPOLATION — one 3-D climate model found moderate early-Venus conditions under selected assumptions; SRC-043, SRC-046; MEDIUM/QUALIFIED. Safe wording: “Sebagian model mengusulkan Venus mungkin pernah lebih sejuk, tetapi skenario itu belum terkonfirmasi.” Not a consensus conclusion or direct observation.

### Research red-team conclusions
1. The 2026 paper demonstrates mineral reactions under a simulated environment, not discovery of those minerals on Venus.
2. Magnesite formed from brucite in the experiment; the result alone does not establish ancient liquid water.
3. The stronger proposed past-water clue is conditional: hydrous micas may have formed during a water-richer period, fluorination may help preserve them, and future detection plus geological context could test that history.
4. D/H evidence is not simple proof; published interpretations differ.
5. Ancient climate models are scenario-dependent and must not be presented as direct evidence.
6. No claim of ancient life, a confirmed ocean, or a proven habitable Venus is allowed.
7. Use generated scientific reconstructions unless exact source-media rights are verified; journal sample photographs are not automatically cleared for reuse.


#### SRC-047 — University research news / institutional corroboration
- Title: “UT San Antonio research offers new clues to Venus’ past and future exploration”
- Author: Ryan Schoensee; publisher: UT San Antonio Today.
- Published: 2026-11-04.
- URL: https://news.utsa.edu/2026/11/ut-san-antonio-research-offers-new-clues-to-venus-past-and-future-exploration/
- Accessed: 2026-11-05.
- Type/scope: institutional research news summarizing the Port et al. 2026 mineral-exposure study and quoting the conditional interpretation of fluorine-bearing minerals as possible clues if found on Venus.
- Claims/context: supports editorial context for CLM-046–CLM-047; not independent primary evidence.
- Inspection: full article text surfaced in search results and was inspected.
- Limitations: university news release, not a peer-reviewed independent replication; experimental claims remain sourced to SRC-040.

#### SRC-048 — NASA DAVINCI engineering update
- Title: “NASA’s DAVINCI Beats Heat in Preparation for Blistering Venus Descent”
- Publisher/author: NASA Science, Ashley Balzer.
- Published: 2026-09-24.
- URL: https://science.nasa.gov/blogs/davinci/2026/09/24/nasas-davinci-beats-heat-in-preparation-for-blistering-venus-descent/
- Accessed: 2026-11-05.
- Type/scope: official NASA mission engineering update; reports thermal testing of a DAVINCI engineering development unit at Venus-like temperatures.
- Claims/context: contextualizes future mission preparation only; no new mineral detection claim.
- Inspection: full article text surfaced in search results and was inspected.
- Limitations: engineering test update, not evidence that the mission has launched, arrived at Venus, or detected surface minerals.
