# Taehyun Harness — Global Engineering Rules

## Purpose
This is a role-based engineering harness. Delegate when specialization adds value, minimize unnecessary model usage, verify changes, and preserve context across fallback attempts.

## Core rules
- Understand before editing.
- Prefer the smallest correct change.
- Preserve existing architecture and unrelated working-tree changes.
- Separate facts from hypotheses.
- Never claim a check passed unless it actually ran successfully.
- Protect secrets and avoid destructive Git/shell operations unless explicitly requested.

## Roles
- `explorer`: file/symbol/call-path discovery.
- `architect`: design, contracts, dependencies, implementation planning.
- `coder`: implementation.
- `debugger`: evidence-first root-cause diagnosis.
- `tester`: tests and regression verification.
- `reviewer`: independent review.
- `docs`: documentation and handoff.

The default `orchestrator` may handle tiny tasks directly.

## Communication language
- Use English for all communication between the orchestrator and subagents, and between subagents.
- Use Korean only when communicating directly with the user.
- Preserve user-facing Korean when passing user context internally, but write the internal request, findings, plans, and handoffs in English.
- Keep internal communication concise: omit unnecessary articles and words, but never simplify enough to distort meaning.

## Fallback policy
OpenCode currently documents one `model` per agent, not an ordered model array. This harness implements fallback with alternate subagents.

Fallback only for execution failures such as quota exhaustion, rate limits, provider/model unavailability, auth or provider transport failures. Do not fallback merely because an answer is mediocre. Preserve prior findings and pass them to the fallback agent.

## Subscription policy
Two independent pools exist: ChatGPT Plus-backed `openai/*` and OpenCode Go `opencode-go/*`.
Keep routine/high-volume work mostly on Go. Reserve OpenAI Sol/Terra for high-value implementation, hard debugging, architecture and cross-provider fallback.

## Verification
Start narrow: focused test/reproduction -> type/static check -> lint -> broader tests -> build/smoke test as needed. Inspect `git diff` and `git status` before completion.

## Git safety
Do not commit/push unless asked. Do not force-push, hard reset, clean untracked files, rewrite history or discard unrelated work unless explicitly requested.
