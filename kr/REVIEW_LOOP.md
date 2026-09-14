# 하이브리드 자동 리뷰 루프

## 계약

코드를 변경하는 모든 작업의 루프는 primary orchestrator가 담당한다.

1. 직접 구현하거나 FE/BE에 위임한다.
2. QA에 원래 요구사항, 구현 요약, 이미 실행한 검사, 현재 diff 범위를 전달한다.
3. QA가 `FAIL`을 반환하면 담당 구현 agent 또는 orchestrator가 확인된 finding을 수정한다.
4. 갱신된 변경을 QA에 다시 보낸다.
5. `PASS` 또는 세 번째 QA 리뷰 뒤에 멈춘다. 상한에 도달하면 수정을 중단하고 미해결 finding을 보고한다.

QA는 항상 읽기 전용이다. QA 호출 한 번이 리뷰 한 round다. 명시적인 상한 도달 보고 외에는 `PASS` 전에 완료를 주장하지 않는다.

## QA 응답 계약

QA는 요구사항, diagnostics/test, regression 위험 순서로 리뷰한다. 확인된 각 finding에는 severity, confidence, 근거, 영향, 수정 방향을 포함한다. 모든 응답은 `PASS` 또는 `FAIL` 중 정확히 하나의 verdict로 끝난다.

## Runtime 자동화 경계

Runtime plugin은 설치하지 않았다. `@opencode-ai/plugin` 1.18.18은 `session.idle`을 포함하는 범용 `event` callback을 제공하고 SDK client는 `session.promptAsync`를 제공한다. 하지만 event는 “구현 완료” lifecycle 상태, 현재 workflow의 의미상 단계, QA verdict, 지속되는 review-round counter를 식별하지 않는다. idle event, message text, 비어 있지 않은 working-tree diff로 이를 추론하면 사용자 전용·QA·무관한 session을 다시 실행하거나 continuation loop를 만들 수 있다.

따라서 이 API에서 가능한 가장 강한 안전한 자동화는 in-turn orchestration이다. primary prompt와 feature/fix command가 추가 사용자 입력 없이 orchestrator의 루프 진행을 강제한다. `/review`는 읽기 전용 one-shot QA command로 유지한다. 신뢰할 수 있는 implementation-complete signal과 session 범위의 지속적 workflow state 또는 동등한 guarded metadata를 API가 제공할 때만 runtime plugin을 추가해야 한다.
