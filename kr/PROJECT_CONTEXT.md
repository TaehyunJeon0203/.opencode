# 프로젝트 컨텍스트 — Taehyun OpenCode Harness

## 먼저 읽기
이 프로젝트는 앱이 아니라 `~/.config/opencode/`에 설치하는 개인 OpenCode 개발 하네스다. 목표는 역할 분리, 구독 효율화, fallback, 문서화, `kr/` 미러 유지다.

## 작업 이력
v1에서 전역 규칙, permission, architect/coder/debugger/reviewer, feature/fix/review command, React/Django/Docker/Git skill을 만들었고 모델은 지정하지 않았다. v2에서는 사용자가 제공한 실제 모델 목록을 바탕으로 모델 배정과 fallback을 추가했다.

## 공식 OpenCode 확인 결과
2026-08-19 기준 agent는 단일 `model` override, primary/subagent, Task, `permission.task`, hidden subagent, `default_agent`, `subagent_depth`를 지원한다. 공식 Agents/Config/Models 문서에는 순서형 model fallback 배열이 문서화되어 있지 않았다. 따라서 fallback 모델마다 별도 hidden subagent를 만든다.

## 구조
사용자 -> `orchestrator`(Go Luna) -> explorer/architect/coder/debugger/tester/reviewer/docs. specialist Task가 quota/rate-limit/provider/model/auth/연결 오류로 실패하면 해당 fallback agent를 호출한다. Go primary 자체가 실행 불가하면 `orchestrator-plus`로 수동 전환한다.

## 수정 규칙
다음 에이전트는 이 파일, `MODEL_ROUTING.md`, `README.md`를 먼저 읽고 새 config key는 최신 공식 문서를 확인한다. 사용자가 새 모델 목록을 주지 않으면 확인된 모델 ID만 쓴다. Go 사용량 정책 변경 시 최신 공식 한도를 다시 확인한다. 활성 파일을 바꾸면 대응 `kr/` 파일도 갱신한다. 수동 provider 전환을 자동 fallback이라 부르지 않는다.

## 미완료
실제 잔여 구독량 기반 동적 라우팅, 검증된 transport-level plugin fallback, telemetry, security/performance specialist, 개인 repo 벤치마크는 아직 하지 않았다.
