# WHAT IF WORLD — Rights & Provenance Register

**Register ID:** RPR-001  
**Audit snapshot:** 2026-11-05  
**Status:** OPEN — NO GLOBAL RIGHTS CLEARANCE CLAIMED  
**Related decision:** LICENSING_DECISION_RECORD.md (LDR-001)

## Purpose and decision rule
Track ownership, provenance, license evidence, attribution, restrictions, and commercial-use clearance. This is an operational evidence register, not a warranty of ownership or permission. No project-wide commercial clearance is established by this audit.

## Repository audit snapshot
Inspected the repository root, requirements-dev.txt, README, AGENTS, architecture, licensing record, CI workflow and current Git history.

- The root tree contains project documentation, schemas, examples, Python validators/tests, a development requirements file, and one GitHub Actions validation workflow.
- No root LICENSE file exists, consistent with LDR-001; no custom license has been issued.
- requirements-dev.txt directly pins jsonschema==4.26.0 and rfc3339-validator==0.1.4. PyPI project metadata identifies both as MIT-licensed. This is preliminary direct-dependency evidence only: jsonschema has transitive runtime dependencies, and no fully resolved lockfile/SBOM is present.
- .github/workflows/validate.yml now pins actions/checkout to d23441a48e516b6c34aea4fa41551a30e30af803 (v6.0.1) and actions/setup-python to ece7cb06caefa5fff74198d8649806c4678c61a1 (v6). Both upstream commits have GitHub-verified signatures; both upstream LICENSE files were inspected and state MIT. This closes the mutable-tag issue for the current workflow revision; ongoing security/update review remains required.
- Git commit attribution demonstrates repository activity, not copyright assignment, employment/contractor ownership or contributor consent.
- Research excerpts, generated media, fonts, music, voices, likenesses, model terms and production assets require item-level review.

## Initial inventory and current disposition

| ID | Material class | Inspected scope / finding | Status | Evidence required to close |
|---|---|---|---|---|
| RPR-001 | Repository code | Python validators, tests, schemas and project code; no signed assignment/contributor chain supplied. | HOLD | Confirm authorship/ownership for all contributors; retain agreements or written grants. |
| RPR-002 | Documentation | README, operating manuals, architecture, templates, character bible; no exhaustive copied-material audit. | HOLD | Review copied/adapted text and third-party excerpts; confirm author/commission agreements. |
| RPR-003 | Prompts and examples | Manifest examples and prompt-bearing documents; no item-level third-party provenance dossier. | HOLD | Record prompt creator, source references, embedded material and generator terms per item. |
| RPR-004 | Dependencies | Direct pins jsonschema 4.26.0 (MIT) and rfc3339-validator 0.1.4 (MIT), per PyPI metadata; transitive set not locked here. | IN_REVIEW | Generate resolved SBOM; capture exact versions, license texts, notices and compatibility for all transitive packages. |
| RPR-005 | CI actions and tooling | checkout pinned to d23441a48e516b6c34aea4fa41551a30e30af803; setup-python pinned to ece7cb06caefa5fff74198d8649806c4678c61a1. Both upstream commit signatures verified by GitHub; upstream LICENSE files inspected (MIT). | IN_REVIEW | Retain MIT notices when distributing action code; periodically review upstream security advisories and update pins through CI. |
| RPR-006 | Research and references | Research/editorial documents contain external references; no exhaustive quotation/source-terms review completed. | HOLD | Inventory each source and excerpt; review terms, quotation scope, attribution and permitted use. |
| RPR-007 | Media and creative assets | No complete production media asset inventory or asset-level rights evidence attached to this snapshot. | HOLD | Record provenance, exact terms, consent and commercial scope for every image, video, audio, music, font, voice, model and dataset. |
| RPR-008 | Brand and identity | No trademark clearance/search report attached for WHAT IF WORLD name, logo and visual identity. | HOLD | Conduct jurisdiction-appropriate clearance search and confirm ownership/registration strategy with counsel. |
| RPR-009 | Contributions | Commit metadata does not establish a complete contributor agreement or assignment chain. | HOLD | Identify contributors, employees, contractors and collaborators; obtain and retain appropriate grants/assignments. |

## Dependency evidence reviewed
- jsonschema 4.26.0: https://pypi.org/project/jsonschema/ — PyPI metadata reports MIT.
- rfc3339-validator 0.1.4: https://pypi.org/project/rfc3339-validator/ — PyPI metadata reports MIT.

These identify the package license metadata only. They do not replace review of actual distributed license/notice files, transitive dependencies, compatibility obligations or legal interpretation. requirements-dev.txt is not a complete production SBOM.

## Disposition states
- **PENDING:** not yet reviewed or evidence incomplete.
- **IN_REVIEW:** evidence collected; compatibility and scope being assessed.
- **CLEARED:** documented evidence supports the intended use and a reviewer recorded the decision.
- **RESTRICTED:** usable only under stated conditions.
- **EXCLUDED:** remove from the relevant distribution.
- **HOLD:** ownership, provenance, permission or compatibility unresolved.

Only mark CLEARED when the exact intended distribution and commercial use have been evaluated. A dependency license does not clear unrelated project assets.

## Review gates
1. Inventory all repository files and embedded third-party material.
2. Verify contributor and ownership chain for original project material.
3. Resolve every direct and transitive dependency and review exact license texts/notices.
4. Review research quotations, external references, generated media and production assets.
5. Obtain permission, replace or exclude unclear/incompatible material.
6. Obtain qualified legal review of final license and customer terms.
7. Record reviewer decision and evidence for every item before commercial distribution.

## Current disposition
The two direct development dependencies have preliminary license metadata recorded as IN_REVIEW. Ownership, source-material, research, media, brand and contribution categories remain HOLD. No item is represented as globally cleared. The source-available commercial direction is selected, but rights clearance and final legal terms remain open. This register is not proof of ownership or a commercial-use warranty.
