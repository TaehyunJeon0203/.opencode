---
description: Route a feature through the subscription-aware engineering workflow
agent: orchestrator
---

다음 기능을 구현한다: $ARGUMENTS

작업에 따라 PM, Figma analyzer, FE, BE, QA에 비례해 위임한다. 코드 변경이 있으면 `구현 -> 읽기 전용 QA -> 구현 agent의 수정 -> QA`를 자동으로 이어가며 `PASS` 또는 QA 3회 뒤에만 멈춘다. `PASS` 전에는 완료를 주장하지 않고, 상한에 도달하면 미해결 finding을 보고한다.
