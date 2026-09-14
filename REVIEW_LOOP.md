# Hybrid automatic review loop

## Contract

The primary orchestrator owns the loop for every code-changing task:

1. Implement directly or delegate to FE/BE.
2. Send QA the original requirements, implementation summary, checks already run, and current diff scope.
3. If QA returns `FAIL`, have the responsible implementation agent or orchestrator fix confirmed findings.
4. Send the updated change back to QA.
5. Stop on `PASS` or after the third QA review. At the cap, stop editing and report unresolved findings.

QA is always read-only. One QA invocation equals one review round. Completion must not be claimed before `PASS`, except for an explicit round-cap report.

## QA response contract

QA reviews requirements first, then diagnostics/tests, then regression risk. Every confirmed finding includes severity, confidence, evidence, impact, and a fix direction. Every response ends with exactly one verdict: `PASS` or `FAIL`.

## Runtime automation boundary

No runtime plugin is installed. `@opencode-ai/plugin` 1.18.18 exposes a generic `event` callback, including `session.idle`, and the SDK client exposes `session.promptAsync`. However, the event does not identify an “implementation completed” lifecycle state, the active semantic workflow phase, a QA verdict, or a durable review-round counter. Inferring those from idle events, message text, or a non-empty working-tree diff could retrigger user-only, QA, or unrelated sessions and could create continuation loops.

Therefore the strongest safe automation available with this API is in-turn orchestration: the primary prompt and feature/fix commands require the orchestrator to continue the loop without another user prompt. `/review` remains a read-only one-shot QA command. A runtime plugin should be added only when the API provides a reliable implementation-complete signal plus session-scoped durable workflow state or equivalent guarded metadata.
