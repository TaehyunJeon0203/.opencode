---
description: Produce a concise continuation handoff for another agent
agent: orchestrator
---

Create a concise continuation handoff in English using this format:

## Handoff: <one-line goal>

- **Goal**: State the purpose of this session or task in one sentence.
- **Findings**: Record verified facts with `file:line` references where useful. Label hypotheses or assumptions explicitly. Include architecture/context only when it differs from established project context.
- **Completed work**: Summarize work actually performed.
- **Decisions**: Record decisions that affect continuation, with brief rationale.
- **Changed files**: List each changed path and its purpose, based on `git status`/`git diff`. Identify unrelated pre-existing working-tree changes separately.
- **Risks & open issues**: List known risks, unresolved defects, and assumptions requiring confirmation.
- **Verification**: List commands actually run and their results. Mark checks not run as `not run`; never claim unexecuted checks passed.
- **Next action**: State one concrete next step and suggest the responsible role (`PM`, `FE`, `BE`, `QA`, or `figma-analyzer`).

Always include **Goal**, **Verification**, and **Next action**. Omit other sections only when there is nothing to report. Preserve facts versus assumptions and do not invent information. Output the handoff in chat; do not rewrite `PROJECT_CONTEXT.md` unless project-level decisions changed.
