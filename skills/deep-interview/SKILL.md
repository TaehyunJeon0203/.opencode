---
name: deep-interview
description: Clarifies vague, incomplete, or ambiguous requests through a focused Socratic interview before implementation. Use when goals, scope, constraints, required information, or completion criteria are unclear; do not use for already-specific requests or trivial changes.
---

# Deep Interview

Do not implement an ambiguous request immediately. Convert it into actionable requirements first.

Ask one question at a time. Resolve the highest-impact uncertainty first. Prefer inspecting the codebase over asking the user questions that repository evidence can answer.

## Decision axes

Choose the least clear axis, in this order:

1. Goal
2. Scope and exclusions
3. Constraints
4. Completion criteria
5. Existing context and impact

## Interview rules

- Ask only when ambiguity could materially change implementation, scope, risk, or acceptance.
- Summarize the current understanding before each question.
- State the blocked decision explicitly.
- Always provide 2–3 concrete choices when asking the user to decide.
- Always include `- (Other: enter directly)` as the final choice.
- If useful, mark one choice as `(Recommended: brief reason)`. Recommendation is guidance, not a decision.
- Never recommend a choice for strategy, budget, security, external exposure, operational impact, or irreversible decisions.
- Do not force a multiple-choice answer when examples would narrow the user's intent incorrectly; still include the direct-input option.
- Keep questions concise. Explain why only when needed, in one sentence maximum.
- Carry the user's answer into the next question's current understanding.
- Preserve uncertainty rather than inventing requirements.

## Interaction method

- Prefer OpenCode's `question` tool when it is available so the user can move through choices with the arrow keys and confirm with Enter.
- Keep the tool's direct-input option available for answers outside the listed choices.
- Fall back to the text format below when the `question` tool is unavailable or cannot represent the question clearly.

## Question format

Use the user's language for the user-facing interview. For Korean users, use this fallback structure:

```text
현재 이해: {concise summary of the request and decisions so far}
막힌 결정: {highest-impact unresolved decision}
질문: {one question}
선택지:
- A. {choice} (Recommended: {brief reason})
- B. {choice}
- (Other: enter directly)
```

Omit the recommendation when no safe recommendation exists. Keep exactly one unresolved decision per question.

## Completion criteria

Stop interviewing when these are clear:

- Goal
- Included and excluded scope
- Constraints
- Acceptance/completion criteria
- Remaining open questions

Then summarize decisions and open questions only. Do not reproduce the full transcript. Ask for confirmation before implementation when a remaining decision could materially change the result.
