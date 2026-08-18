# 모델 라우팅 및 Fallback 정책

2026-08-19 사용자의 `opencode models` 출력 기준.

| 역할 | Primary | Fallback 1 | Fallback 2 |
|---|---|---|---|
| Orchestrator | `opencode-go/gpt-5.6-luna` | `openai/gpt-5.6-luna` primary로 수동 전환 | — |
| Explorer | `opencode-go/gpt-5.6-luna` | `openai/gpt-5.6-luna` | — |
| Architect | `openai/gpt-5.6-terra` | `opencode-go/glm-5.2` | — |
| Coder | `openai/gpt-5.6-sol` | `opencode-go/kimi-k2.7-code` | `opencode-go/deepseek-v4-pro` |
| Debugger | `openai/gpt-5.6-sol` | `opencode-go/glm-5.3` | `opencode-go/deepseek-v4-pro` |
| Tester | `opencode-go/kimi-k2.7-code` | `opencode-go/deepseek-v4-flash` | `openai/gpt-5.6-luna` |
| Reviewer | `opencode-go/glm-5.3` | `openai/gpt-5.6-terra` | `opencode-go/qwen3.7-max` |
| Docs | `opencode-go/mimo-v2.5-pro` | `openai/gpt-5.6-luna` | — |

Go 공식 한도는 5시간 $12, 주 $30, 월 $60 가치 기준이다. 고빈도 작업은 저렴한 Go 모델을 쓰고 GLM-5.3은 reviewer/디버깅 fallback처럼 가치가 큰 호출에 집중한다. fallback은 실행 실패에만 적용한다. 현재 orchestrator 자체 provider가 실패하면 `orchestrator-plus`로 수동 전환해야 하므로 완전 자동 transport failover는 아니다.
