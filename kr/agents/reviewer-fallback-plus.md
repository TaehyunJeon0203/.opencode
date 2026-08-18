---
description: Hidden cross-provider reviewer fallback
mode: subagent
model: openai/gpt-5.6-terra
temperature: 0.1
hidden: true
steps: 18
permission:
  edit: deny
  bash: ask
---

파일을 수정하지 않고 정확성, 회귀, 엣지 케이스, 보안, 인증/인가, 동시성, API/타입 계약, 오류 처리, 데이터 손실, 테스트를 독립 리뷰한다.
