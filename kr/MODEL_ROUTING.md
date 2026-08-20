# 모델 라우팅

2026-08-19 사용자의 `opencode models` 출력 기준.

| Agent | Mode | Model | 책임 |
|---|---|---|---|
| `orchestrator` | primary (기본) | `opencode-go/gpt-5.6-luna` | 라우팅과 작은 작업 직접 처리 |
| `orchestrator-plus` | primary (수동 전환) | `openai/gpt-5.6-luna` | Plus 기반 대체 오케스트레이션 |
| `PM` | subagent | `opencode-go/glm-5.2` | 요구사항, 범위, 인수 조건 |
| `FE` | subagent | `openai/gpt-5.6-sol` | frontend 구현과 코드 변경 |
| `BE` | subagent | `opencode-go/deepseek-v4-pro` | backend, API, data-layer 구현 |
| `QA` | subagent | `opencode-go/kimi-k2.7-code` | 검증, 회귀 테스트, 리뷰 |
| `figma-analyzer` | subagent | `opencode-go/gpt-5.6-luna` | 읽기 전용 Figma 및 디자인 시스템 분석 |

Go 공식 한도는 5시간 $12, 주 $30, 월 $60 가치 기준이다. 반복적인 PM, QA, Figma 분석에는 Go 모델을 사용하고 구현에는 OpenAI Sol을 사용한다. `orchestrator-plus`는 자동 fallback이 아니라 사용자가 선택하는 수동 primary 전환이다.
