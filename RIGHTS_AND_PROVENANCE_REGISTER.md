# WHAT IF WORLD — Rights & Provenance Register

**Register ID:** RPR-001  
**Date opened:** 2026-11-04  
**Status:** OPEN — NO GLOBAL RIGHTS CLEARANCE CLAIMED  
**Related decision:** LICENSING_DECISION_RECORD.md (LDR-001)

## Purpose

Track ownership, provenance, license evidence, attribution, restrictions, and commercial-use clearance for materials proposed for inclusion in WHAT IF WORLD source distributions or commercial products.

This is a blank operational register. A category appearing here is not evidence that the underlying material is owned, licensed, or cleared.

## Required record fields

For every material item, record:

- unique register ID and material name;
- material type and repository path / asset identifier;
- creator, author, supplier, and date obtained;
- source URL or contract/document reference;
- copyright owner and evidence of ownership or permission;
- exact license / agreement name and version;
- whether modification, redistribution, sublicensing, SaaS use, and commercial use are permitted;
- attribution, notice, source-disclosure, copyleft, or pass-through obligations;
- territory, duration, expiry, and termination conditions;
- restrictions, exceptions, and incompatible obligations;
- reviewer, review date, evidence location, and final disposition.

Do not infer permission from public availability, a search result, an AI output, or the fact that a dependency installs successfully.

## Initial inventory work queue

| ID | Material class | Initial scope to inspect | Status | Required evidence |
|---|---|---|---|---|
| RPR-001 | Repository code | Python validators, tests, CI configuration, schemas | PENDING | Authorship and contributor/contractor ownership trail |
| RPR-002 | Documentation | README, operating manuals, architecture, templates, character bible | PENDING | Authorship and any copied/adapted material audit |
| RPR-003 | Prompts and examples | Production manifest, prompt text, examples, sample content | PENDING | Creator/source and any third-party text or asset provenance |
| RPR-004 | Dependencies | requirements-dev.txt and transitive development dependencies | PENDING | Exact version, license text, notices, and compatibility review |
| RPR-005 | CI actions and tooling | GitHub Actions referenced by workflow and external tools | PENDING | Action/tool licenses, terms, and version/pinning review |
| RPR-006 | Research and references | URLs and material summarized or quoted in project documents | PENDING | Source terms, quotation scope, attribution, and permitted use |
| RPR-007 | Media and creative assets | Images, audio, music, fonts, video, models, datasets, generated assets | PENDING | Asset-level provenance, rights, consent, and commercial permissions |
| RPR-008 | Brand and identity | WHAT IF WORLD name, logo, marks, visual identity | PENDING | Ownership/search review and registration strategy |
| RPR-009 | Contributions | All external, employee, contractor, collaborator, and community contributions | PENDING | Contributor agreements, assignment, or documented license grant |

## Disposition states

- **PENDING:** not yet reviewed or evidence incomplete.
- **IN_REVIEW:** evidence collected; compatibility and scope being assessed.
- **CLEARED:** documented evidence supports the intended use and a reviewer recorded the decision.
- **RESTRICTED:** usable only under stated conditions; restrictions must be preserved.
- **EXCLUDED:** remove from the relevant source or commercial distribution.
- **HOLD:** ownership, provenance, permission, or license compatibility is unresolved.

Only mark an item CLEARED when the exact intended distribution and commercial use have been evaluated. A dependency license does not clear unrelated project assets.

## Review gates

1. Inventory all repository files and embedded third-party material.
2. Verify contributor and ownership chain for original project material.
3. Review direct and transitive dependency licenses and required notices.
4. Review research quotations, external references, generated media, and all production assets.
5. Resolve incompatible or unclear materials by obtaining permission, replacing, or excluding them.
6. Obtain qualified legal review of the final license and customer terms.
7. Record the reviewer's decision and evidence for every item before commercial distribution.

## Current disposition

No item is marked CLEARED by this initial register. The source-available commercial direction is selected, but rights clearance is still pending. Do not use this register as proof of ownership or as a commercial-use warranty.
