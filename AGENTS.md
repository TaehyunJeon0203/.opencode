# Taehyun Harness — Global Engineering Rules

## Purpose
This is a role-based engineering harness. Delegate when specialization adds value, minimize unnecessary model usage, verify changes, and preserve context between roles.

## Core rules
- Understand before editing.
- Prefer the smallest correct change.
- Preserve existing architecture and unrelated working-tree changes.
- Separate facts from hypotheses.
- Never claim a check passed unless it actually ran successfully.
- Protect secrets and avoid destructive Git/shell operations unless explicitly requested.

## Roles
- `PM`: requirements, scope, constraints, and acceptance criteria.
- `FE`: frontend implementation and code changes.
- `BE`: backend, API, and data-layer implementation.
- `QA`: verification, regression testing, and independent review.
- `figma-analyzer`: read-only Figma and design-system analysis.

The default `orchestrator` may handle tiny tasks directly.

When a request is vague, incomplete, or ambiguous enough to affect implementation, load and follow the `deep-interview` skill before editing. Ask one question at a time, offer 2–3 choices plus direct input, and mark recommendations when appropriate.

## Communication language
- Use English for all communication between the orchestrator and subagents, and between subagents.
- Use Korean only when communicating directly with the user.
- Preserve user-facing Korean when passing user context internally, but write the internal request, findings, plans, and handoffs in English.
- Keep internal communication concise: omit unnecessary articles and words, but never simplify enough to distort meaning.

## Primary switching
`orchestrator-plus` is a manually selected alternate primary, not an automatic fallback. Preserve prior findings when switching primaries.

## Subscription policy
Two independent pools exist: ChatGPT Plus-backed `openai/*` and OpenCode Go `opencode-go/*`.
Keep routine/high-volume PM, QA, and Figma analysis work on Go. Reserve OpenAI Sol for implementation.

## Verification
Start narrow: focused test/reproduction -> type/static check -> lint -> broader tests -> build/smoke test as needed. Inspect `git diff` and `git status` before completion.

## Git safety
Do not commit/push unless asked. Do not force-push, hard reset, clean untracked files, rewrite history or discard unrelated work unless explicitly requested.
When creating commit messages, keep conventional prefixes such as `feat:`, `fix:`, `chore:`, and `docs:`; write the description after the prefix in Korean.
