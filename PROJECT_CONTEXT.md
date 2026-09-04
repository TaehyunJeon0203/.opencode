# Project Context — Taehyun OpenCode Harness

## Read this first
This is the handoff document for any agent continuing development of this harness. It is not an application; it is a reusable personal OpenCode configuration intended for `~/.config/opencode/`.

## Current operating decisions
- Active project path: `/Users/taehyunjeon/taehyun/dev/project/taehyun-opencode-harness-v2`.
- Treat requests made in this project as project-local changes first.
- After a project-local configuration change, ask whether the equivalent global change should be applied; never apply it automatically.
- Keep `kr/` synchronized as the Korean reference mirror whenever active text or configuration changes.
- `question: allow` is enabled in both project and global configuration; `deep-interview` prefers OpenCode's arrow-key/Enter question UI.
- The similarly named `/Users/taehyunjeon/taehyun/dev/project/opencode` directory is not this harness and must not be used as the target.

## Owner goal
Build a personal coding-agent harness that separates product requirements, implementation, verification, and Figma analysis, uses existing subscriptions efficiently, stays understandable, and ships a Korean reference mirror.

## Known user provider pools
The user supplied `opencode models` on 2026-08-19.

### OpenAI / ChatGPT Plus-integrated models observed
`openai/gpt-5.3-codex-spark`, `openai/gpt-5.4`, `openai/gpt-5.4-fast`, `openai/gpt-5.4-mini`, `openai/gpt-5.4-mini-fast`, `openai/gpt-5.5`, `openai/gpt-5.5-fast`, `openai/gpt-5.6-luna`, `openai/gpt-5.6-luna-fast`, `openai/gpt-5.6-sol`, `openai/gpt-5.6-sol-fast`, `openai/gpt-5.6-terra`, `openai/gpt-5.6-terra-fast`.

### OpenCode Go models observed
`opencode-go/deepseek-v4-flash`, `opencode-go/deepseek-v4-pro`, `opencode-go/glm-5.1`, `opencode-go/glm-5.2`, `opencode-go/glm-5.3`, `opencode-go/gpt-5.6-luna`, `opencode-go/grok-4.5`, `opencode-go/hy3`, `opencode-go/kimi-k2.6`, `opencode-go/kimi-k2.7-code`, `opencode-go/kimi-k3`, `opencode-go/mimo-v2.5`, `opencode-go/mimo-v2.5-pro`, `opencode-go/minimax-m2.7`, `opencode-go/minimax-m3`, `opencode-go/qwen3.6-plus`, `opencode-go/qwen3.7-max`, `opencode-go/qwen3.7-plus`, `opencode-go/qwen3.8-max`.

Free `opencode/*` models were visible too, but v2 does not rely on them for critical fallback.

## Work history
### v1
Created global engineering rules, safe permissions, architect/coder/debugger/reviewer agents, feature/fix/review commands, React/Django/Docker/Git skills, and a `kr/` mirror. v1 did not assign models.

### Why v2
The user required role-specific model assignment and subscription-usage balancing.

## Official OpenCode findings verified for v2
Checked current official docs on 2026-08-19:
1. Agents support one `model` override in `provider/model-id` format.
2. Primary and subagents are first-class.
3. Primary agents can invoke subagents through Task.
4. `permission.task` can restrict named subagents with glob patterns.
5. Hidden subagents remain callable through Task.
6. `default_agent` must be primary.
7. `subagent_depth` controls nested subagents.
8. Commands can select one agent and one model.
9. Official Agents/Config/Models docs did not document an ordered model fallback array.

## Architecture
```text
User
  -> orchestrator (Go Luna, primary)
       -> PM
       -> FE
       -> BE
       -> QA
      -> figma-analyzer
```

`orchestrator-plus` is an alternate OpenAI Luna primary for provider-wide Go failure/exhaustion.

## Important limitation
Primary switching is manual, not transport-layer automatic failover. If the current primary orchestrator cannot generate a response because its provider is unavailable or exhausted, the user must select the alternate primary. Do not describe that manual switch as automatic fallback.

## Routing philosophy
- Go: orchestration, product requirements, backend implementation, verification, Figma analysis, and most repeated calls.
- OpenAI Sol: implementation.
- OpenAI Luna: manually selected alternate orchestrator.

See `MODEL_ROUTING.md` for exact routes.

## Files
- `opencode.json`: global safety/defaults.
- `AGENTS.md`: global engineering behavior.
- `agents/`: two primary orchestrators and four leaf subagents.
- `commands/`: common workflows.
- `skills/`: reusable stack guidance.
- `MODEL_ROUTING.md`: model routing design.
- `PROJECT_CONTEXT.md`: this handoff.
- `kr/`: structural Korean reference mirror.

## Rules for future agents modifying this harness
1. Read this file, `MODEL_ROUTING.md` and `README.md` first.
2. Verify new OpenCode config keys against current official docs.
3. Use only user-confirmed model IDs unless the user provides a newer list.
4. Re-check OpenCode Go pricing/limits when changing routing; they can change.
5. Update the matching `kr/` file whenever an active text/config file changes.
6. Keep translated agents/skills under `kr/` so they are not discovered as active duplicates.
7. Preserve safe Git/shell permissions.
8. Never call manual provider switching automatic fallback.

## Next work queue
Prioritize these items in order when starting a new session:
1. Establish a telemetry baseline from real usage with `/report`; record at least one week of aggregate results without storing prompts or session contents.
2. Standardize agent handoffs with a compact template covering findings, decisions, changed files, risks, verification, and next action. (Completed: `/handoff` now defines the required format.)
3. Add task-complexity routing (`tiny`, `standard`, `complex`) so small tasks stay with the primary agent and delegation is reserved for work that benefits from specialization.
4. Use baseline data to tune model routing and document before/after cost, cycle-time, and QA-rework results.
5. Investigate an OpenCode plugin for automatic local telemetry and loop detection only after verifying the current plugin API.
6. Package the result for the portfolio: architecture diagram, install instructions, measured case study, demo, and privacy/safety limitations.

The first implementation slice is complete: `scripts/opencode-report.py` and `/report` read the local OpenCode SQLite database in read-only mode and aggregate session, cost, token, duration, agent, and model data without printing prompts or session contents. The global copies live under `~/.config/opencode/`.

## Not yet implemented
- dynamic routing from real remaining subscription usage,
- verified transport-level plugin fallback,
- automated usage/cost telemetry baseline,
- additional specialist agents,
- repository-specific model benchmarking.

Only add these after verifying current OpenCode capabilities.
