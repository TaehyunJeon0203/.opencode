# Taehyun Harness — 전역 개발 규칙

에이전트 간, 그리고 orchestrator와 subagent 간의 모든 통신은 영어로 한다. 사용자와 직접 대화할 때만 한국어를 사용한다. 사용자에게서 받은 한국어 맥락은 내부에 전달할 수 있지만, 내부 요청·결과·계획·handoff는 영어로 작성한다.

내부 통신은 간결하게 작성한다. 불필요한 관사와 단어는 생략하되, 의미가 왜곡될 정도로 줄이지 않는다.

커밋 메시지는 `feat:`, `fix:`, `chore:`, `docs:` 같은 conventional prefix를 유지하고, prefix 뒤 설명은 한국어로 작성한다.

이 하네스는 PM, FE, BE, QA, Figma analyzer 역할 분리와 구독 사용량 관리, 검증을 포함한 개발 시스템이다. 수정 전에 이해하고 최소 변경을 우선하며 사실/가설을 구분한다. 반복적인 PM·QA·Figma 분석은 Go를 중심으로 하고 구현에는 Sol을 사용한다. `orchestrator-plus`는 자동 fallback이 아니라 수동으로 선택하는 대체 primary다. 요청 없이 commit/push나 파괴적 Git 작업을 하지 않는다.
