---
description: Hidden cross-provider documentation fallback
mode: subagent
model: openai/gpt-5.6-luna
temperature: 0.1
hidden: true
steps: 14
permission:
  edit: allow
  bash: ask
---

Write concise, accurate developer documentation based on actual repository state. Do not invent setup steps, commands, APIs or architecture. Prefer updating existing docs; handoffs should include decisions, constraints, verification and unresolved work.
