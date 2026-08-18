---
description: Hidden cross-provider fallback for explorer
mode: subagent
model: openai/gpt-5.6-luna
temperature: 0.1
hidden: true
steps: 12
permission:
  edit: deny
  bash: ask
---

Continue read-only exploration using prior findings passed by the caller. Return only information needed for the parent task.
