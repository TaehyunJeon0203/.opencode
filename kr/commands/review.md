---
description: Independently review current changes
agent: QA
subtask: true
---

다음을 독립 리뷰한다: $ARGUMENTS

범위가 없으면 working tree diff를 확인한다. 요구사항을 먼저 확인한 뒤 diagnostics/test와 regression 위험을 검토한다. 읽기 전용을 유지하고, 근거가 있는 수정 가능한 severity/confidence finding을 반환하며 명시적인 `PASS` 또는 `FAIL`로 끝낸다.
