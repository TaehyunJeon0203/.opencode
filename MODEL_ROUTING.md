# Model Routing

Verified against the user's `opencode models` output on 2026-08-19.

| Agent | Mode | Model | Responsibility |
|---|---|---|---|
| `orchestrator` | primary (default) | `opencode-go/gpt-5.6-luna` | Routing and small direct tasks |
| `orchestrator-plus` | primary (manual switch) | `openai/gpt-5.6-luna` | Alternate Plus-backed orchestration |
| `PM` | subagent | `opencode-go/glm-5.2` | Requirements, scope, and acceptance criteria |
| `FE` | subagent | `openai/gpt-5.6-sol` | Frontend implementation and code changes |
| `BE` | subagent | `opencode-go/deepseek-v4-pro` | Backend, API, and data-layer implementation |
| `QA` | subagent | `opencode-go/kimi-k2.7-code` | Verification, regression testing, and review |
| `figma-analyzer` | subagent | `opencode-go/gpt-5.6-luna` | Read-only Figma and design-system analysis |

## Usage rationale
OpenCode Go limits are value based: 5-hour $12, weekly $30, monthly $60. At build time the official typical-use estimates were approximately: Luna 10,250 requests/month, GLM-5.2 4,300, and Kimi K2.7 Code 6,750. These are estimates, not guaranteed request quotas.

Therefore routine requirements, verification, and Figma analysis use Go models. OpenAI Sol is reserved for implementation work where stronger coding capability has the most value.

## Primary switching
`orchestrator-plus` is a manual primary-agent switch, not an automatic fallback. If the default orchestrator cannot respond because its provider is unavailable or exhausted, the user must select `orchestrator-plus`.
