# WHAT IF WORLD — GITHUB REFERENCE REVIEW

Research date: 2026-11-04. References were inspected for architecture patterns, not copied wholesale. Recheck upstream documentation before implementation because repositories evolve.

## 1. LangGraph — stateful workflow orchestration
Repository: https://github.com/langchain-ai/langgraph
Useful pattern: long-running workflows with durable execution, human-in-the-loop checkpoints, state, and traceable transitions.
Adopt: explicit production state, persisted artifacts, human approvals, resume/retry rules.
Do not adopt yet: a full agent runtime before the manual process and contracts are stable.

## 2. ComfyUI — modular generative workflows
Repository: https://github.com/Comfy-Org/ComfyUI
Useful pattern: reusable node graphs/subgraphs, workflow JSON, API endpoints, partial execution, and model/asset configuration.
Adopt: preserve generation workflow definitions, tool/model versions, prompts, references, seeds/settings when available, and output IDs.
Do not assume: every model/mode supports the same inputs, durations, audio, or reproducibility.

## 3. Remotion — programmatic video composition/rendering
Repository: https://github.com/remotion-dev/remotion
Useful pattern: video composition as code, parameterized assets, reusable design systems, batch rendering, and rendering APIs.
Adopt later: deterministic titles, captions, lower thirds, branded graphics, repeatable exports.
Caution: inspect Remotion licensing before commercial use; its terms are not equivalent to a generic MIT tool.

## 4. Pydantic — structured data validation
Repository: https://github.com/pydantic/pydantic
Useful pattern: validate typed data at boundaries rather than relying only on prose instructions.
Adopt now: JSON Schemas and a dependency-free repository validator; consider Pydantic if a Python application is built.

## 5. OpenTimelineIO — editorial interchange
Repository: https://github.com/AcademySoftwareFoundation/OpenTimelineIO
Useful pattern: represent clips, timing, tracks, transitions, markers, metadata, and external media references in an interchange format.
Adopt later: export an OTIO timeline if the editing application and workflow support it. OTIO is not a media container.

## 6. n8n — modular automation and error paths
Documentation/repository: https://github.com/n8n-io/n8n and https://docs.n8n.io/
Useful pattern: split complex work into reusable sub-workflows, route conditions, wait/resume, and explicit error workflows.
Adopt: separate daily intelligence, idea triage, production status, and notification workflows. Preserve failure states and avoid silent retries.

## 7. Architectural decisions
| Need | Adopted pattern | First implementation |
|---|---|---|
| Stage progression | LangGraph-like state machine | Markdown contract + status field |
| Evidence traceability | Pydantic-like schema validation | JSON Schema + validator |
| Generation provenance | ComfyUI-like workflow records | generation log and asset register |
| Reusable motion graphics | Remotion-like components | future optional renderer |
| Timeline portability | OTIO interchange | future optional export |
| Scheduled monitoring | n8n-like modular workflows | existing daily automation + report contract |

## 8. License and dependency policy
Before adopting code, models, workflows, nodes, fonts, audio, or templates:
- inspect LICENSE and commercial-use restrictions;
- check model cards and third-party dependencies;
- pin version/commit where reproducibility matters;
- record source and license in the asset register;
- do not copy substantial source code without confirming license compatibility.
