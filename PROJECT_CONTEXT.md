# Project Context — Taehyun OpenCode Harness

## Read this first
This is the handoff document for any agent continuing development of this harness. It is not an application; it is a reusable personal OpenCode configuration intended for `~/.config/opencode/`.

## Owner goal
Build a personal coding-agent harness that separates engineering responsibilities, uses existing subscriptions efficiently, survives individual model/provider quota or availability failures where OpenCode permits, stays understandable, and ships a Korean reference mirror.

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
The user required role-specific model assignment plus fallback and subscription-usage balancing.

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

Therefore do not invent unsupported syntax such as a YAML list under `model`. Each fallback is a real alternate subagent with a different model.

## Architecture
```text
User
  -> orchestrator (Go Luna, primary)
      -> explorer
      -> architect
      -> coder
      -> debugger
      -> tester
      -> reviewer
      -> docs
          -> on specialist execution failure, retry documented fallback subagent
```

`orchestrator-plus` is an alternate OpenAI Luna primary for provider-wide Go failure/exhaustion.

## Important limitation
This is prompt/Task-level failover, not a guaranteed transport-layer automatic failover. If the CURRENT primary orchestrator cannot generate any response because its provider is unavailable or exhausted, the user must switch to the alternate primary. Do not describe that manual switch as automatic fallback.

## Routing philosophy
- Go: orchestration, exploration, tests, docs, independent review and most repeated calls.
- OpenAI Sol: primary implementation and hard debugging.
- OpenAI Terra: architecture and strong cross-provider reviewer fallback.
- OpenAI Luna: inexpensive cross-provider fallback/emergency orchestrator.

See `MODEL_ROUTING.md` for exact routes.

## Files
- `opencode.json`: global safety/defaults.
- `AGENTS.md`: global engineering behavior.
- `agents/`: primary, specialist and hidden fallback agents.
- `commands/`: common workflows.
- `skills/`: reusable stack guidance.
- `MODEL_ROUTING.md`: model/fallback design.
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
8. Document fallback semantics and limitations precisely.
9. Never call manual provider switching automatic fallback.

## Not yet implemented
- dynamic routing from real remaining subscription usage,
- verified transport-level plugin fallback,
- usage/cost telemetry,
- security/performance specialist agents,
- repository-specific model benchmarking.

Only add these after verifying current OpenCode capabilities.
