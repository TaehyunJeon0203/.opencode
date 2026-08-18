# Taehyun Harness — 전역 개발 규칙

이 하네스는 역할 분리와 구독 사용량 관리, 검증, fallback을 포함한 개발 시스템이다. 수정 전에 이해하고 최소 변경을 우선하며 사실/가설을 구분한다. 반복 작업은 Go를 중심으로, Sol/Terra는 고가치 구현·디버깅·설계에 집중한다. OpenCode는 agent별 단일 모델을 문서화하므로 fallback은 별도 subagent로 구현한다. quota/rate-limit/provider/model/auth/연결 실행 실패에만 fallback하고 기존 문맥을 전달한다. 요청 없이 commit/push나 파괴적 Git 작업을 하지 않는다.
