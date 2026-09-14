---
description: Diagnose and fix a bug with root-cause-first routing
agent: orchestrator
---

다음 문제를 진단하고 수정한다: $ARGUMENTS

맹목적으로 patch하지 않는다. FE 또는 BE가 증거 중심으로 진단하고 구현한다. 코드 변경이 있으면 `구현 -> 읽기 전용 QA -> 구현 agent의 수정 -> QA`를 자동으로 이어가며 `PASS` 또는 QA 3회 뒤에만 멈춘다. `PASS` 전에는 완료를 주장하지 않고, 상한에 도달하면 미해결 finding을 보고한다.
