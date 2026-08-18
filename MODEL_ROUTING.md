# Model Routing and Fallback Policy

Verified against the user's `opencode models` output on 2026-08-19.

| Role | Primary | Fallback 1 | Fallback 2 |
|---|---|---|---|
| Orchestrator | `opencode-go/gpt-5.6-luna` | manually switch to `openai/gpt-5.6-luna` primary | — |
| Explorer | `opencode-go/gpt-5.6-luna` | `openai/gpt-5.6-luna` | — |
| Architect | `openai/gpt-5.6-terra` | `opencode-go/glm-5.2` | — |
| Coder | `openai/gpt-5.6-sol` | `opencode-go/kimi-k2.7-code` | `opencode-go/deepseek-v4-pro` |
| Debugger | `openai/gpt-5.6-sol` | `opencode-go/glm-5.3` | `opencode-go/deepseek-v4-pro` |
| Tester | `opencode-go/kimi-k2.7-code` | `opencode-go/deepseek-v4-flash` | `openai/gpt-5.6-luna` |
| Reviewer | `opencode-go/glm-5.3` | `openai/gpt-5.6-terra` | `opencode-go/qwen3.7-max` |
| Docs | `opencode-go/mimo-v2.5-pro` | `openai/gpt-5.6-luna` | — |

## Usage rationale
OpenCode Go limits are value based: 5-hour $12, weekly $30, monthly $60. At build time the official typical-use estimates were approximately: Luna 10,250 requests/month, GLM-5.3 1,080, GLM-5.2 4,300, Kimi K2.7 Code 6,750, DeepSeek V4 Pro 5,200, DeepSeek V4 Flash 37,800, MiMo V2.5 Pro 16,300 and Qwen3.7 Max 1,690. These are estimates, not guaranteed request quotas.

Therefore high-volume tasks use cheaper Go models, while GLM-5.3 is reserved for reviewer/debug fallback. Sol is reserved for primary coding and difficult diagnosis.

## Failure semantics
Fallback only for quota/rate-limit/provider/model/auth/connection execution errors. Preserve context and prior findings when retrying.

Provider-wide primary failure is not fully automatic: if `orchestrator` itself cannot respond, manually switch to `orchestrator-plus`.
