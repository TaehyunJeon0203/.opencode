---
description: Generate a privacy-preserving local OpenCode usage report
agent: orchestrator
subtask: false
---

Run `python3 scripts/opencode-report.py $ARGUMENTS` to report local session count, recorded cost, token usage, duration, agent breakdown, and model breakdown. The report reads the OpenCode database read-only and does not print prompts or session contents.

Optional filters: `--since YYYY-MM-DD`, `--directory /path/to/project`, and `--db /path/to/opencode.db`.
