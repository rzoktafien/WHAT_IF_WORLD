# WHAT IF WORLD — Licensing Decision Record

**Decision ID:** LDR-001  
**Date:** 2026-11-04  
**Applies to:** WHAT IF WORLD repository and V3.2 development line  
**Status:** DIRECTION SELECTED — LEGAL INSTRUMENT NOT YET APPROVED

## 1. Owner decision

The repository owner selected a **source-available commercial** licensing direction for WHAT IF WORLD.

The intended model is to make source materials inspectable while reserving commercial permissions, redistribution, derivative-work rights, deployment rights, and other uses for explicit terms to be defined in a separate license instrument.

This is a licensing strategy decision. It is **not** the final license text and does not itself grant or withdraw any specific permission.

## 2. Meaning and boundary

- Source-available is not automatically open source and must not be labelled OSI-approved.
- Public visibility on GitHub must not be presented as permission for unrestricted commercial use, redistribution, sublicensing, or creation of competing products.
- No permissive open-source license (such as MIT or Apache-2.0) is selected by this decision.
- No custom source-available license is being issued by this record.
- Until a separate license is approved and published, do not advertise the repository as commercially licensed or claim that customers have a granted commercial license.
- Do not add a generic `LICENSE` file with guessed or placeholder legal terms.

## 3. Intended commercial structure

The proposed structure for legal and business review is:

1. **Public source inspection:** repository source may remain publicly viewable for evaluation and technical review, subject to applicable law and the eventual license.
2. **Commercial permission:** production, deployment, modification, redistribution, sublicensing, SaaS/service operation, and customer delivery are to be governed by explicit written terms.
3. **Commercial offers:** customer, enterprise, reseller, OEM, and partner permissions may be offered under separate agreements.
4. **Brand and marks:** WHAT IF WORLD name, logo, and associated marks should be addressed separately from copyright permissions.
5. **Third-party materials:** dependencies, fonts, music, images, models, datasets, references, and externally sourced content retain their own licenses and restrictions; this project decision cannot relicense them.

These are intended business requirements, not currently enforceable license clauses.

## 4. Terms that must be decided before publishing a license

The final instrument requires explicit decisions on:

- permitted personal, educational, evaluation, internal business, and production use;
- commercial use, production deployment, and hosted/SaaS operation;
- modification, derivative works, and publication of modified source;
- redistribution, sublicensing, resale, OEM, and white-label rights;
- customer seats, entities, affiliates, contractors, and deployment limits;
- territory, duration, renewal, termination, and post-termination obligations;
- attribution, notices, source disclosure, and trademark restrictions;
- warranty disclaimer, liability limitations, indemnity, and support obligations;
- governing law, dispute forum, and language precedence;
- contributor ownership, assignment, inbound contributions, and rights to all existing materials.

No default values for these terms are approved by LDR-001.

## 5. Rights and provenance audit required

The operational audit is tracked in [RIGHTS_AND_PROVENANCE_REGISTER.md](RIGHTS_AND_PROVENANCE_REGISTER.md). Its initial entries are all PENDING and it does not assert ownership or commercial clearance.

Before a public commercial license or paid distribution is announced, verify:

- authorship and ownership of repository code, documentation, schemas, prompts, and original examples;
- employee, contractor, commissioned, and collaborator contributions, with supporting agreements where required;
- third-party dependencies and their license obligations;
- external research excerpts, quotations, images, audio, fonts, datasets, model outputs, and other referenced assets;
- trademarks, names, logos, and any third-party likeness or voice rights.

Items with unclear provenance or permissions must be excluded, replaced, or held pending clearance. A dependency's license does not automatically cover project assets, and this repository's future license cannot override third-party rights.

## 6. Release gates

The following gates apply:

- **G1 — Direction:** source-available commercial strategy selected by repository owner. COMPLETE.
- **G2 — Rights inventory:** ownership and third-party provenance audit, recorded in the register. PENDING.
- **G3 — Legal drafting:** jurisdiction-aware license and, if needed, commercial customer agreement drafted by qualified counsel. PENDING.
- **G4 — Owner approval:** final text and commercial permissions explicitly approved by repository owner. PENDING.
- **G5 — Publication:** approved license, notices, and README wording published together. BLOCKED until G2–G4 pass.

V3.2 may continue technical review on its feature branch. This record does not authorize merging, publishing a license, or representing licensing clearance as complete.

## 7. Change control

Any change from source-available commercial to open source, proprietary-only, dual licensing, or another model requires a new owner decision record. Do not silently change this direction or infer additional permissions from a marketing statement.

## 8. Legal note

This record is an engineering and product decision artifact, not legal advice and not a substitute for a drafted, jurisdiction-appropriate license. Obtain qualified legal review before issuing license terms, taking payment for licensed access, or making claims about enforceable restrictions.
