# Taehyun OpenCode Harness v2

Personal OpenCode harness with role-specific models, subscription-aware routing, and documented fallback subagents.

## v2 additions
- exact models from the user's current `opencode models` output,
- ChatGPT Plus vs OpenCode Go balancing,
- default orchestrator plus emergency alternate primary,
- hidden fallback subagents,
- explorer/tester/docs roles,
- `PROJECT_CONTEXT.md` for handoff,
- `kr/` mirror translations.

## OpenCode fallback constraint
Current official docs describe one `model` per agent/command and do not document an ordered native model fallback list. v2 therefore uses documented primary/subagent + Task + hidden-agent features. The orchestrator retries another subagent only when the specialist fails because of provider/model availability or quota/rate-limit issues.

## Install
```bash
cp -R ~/.config/opencode ~/.config/opencode.backup
mkdir -p ~/.config/opencode
cp -R ./taehyun-opencode-harness-v2/. ~/.config/opencode/
```
Merge existing config instead of blindly overwriting it.

## Primary agents
- `orchestrator`: default, `opencode-go/gpt-5.6-luna`
- `orchestrator-plus`: manual emergency primary, `openai/gpt-5.6-luna`

If Go cannot run the primary orchestrator at all, switch to `orchestrator-plus`. Prompt-level fallback cannot execute before the current primary model responds.

## Commands
`/feature`, `/fix`, `/review`, `/test`, `/handoff`

Read `MODEL_ROUTING.md` for routing and `PROJECT_CONTEXT.md` before changing this harness.
