# 프로젝트 컨텍스트 — Taehyun OpenCode Harness

## 먼저 읽기
이 프로젝트는 앱이 아니라 `~/.config/opencode/`에 설치하는 개인 OpenCode 개발 하네스다. 목표는 PM, FE, BE, QA, Figma 분석 역할 분리, 구독 효율화, 문서화, `kr/` 미러 유지다.

## 현재 운영 결정
- 활성 프로젝트 경로: `/Users/taehyunjeon/taehyun/dev/project/taehyun-opencode-harness-v2`.
- 이 프로젝트에서 발생한 요청은 먼저 프로젝트 로컬 변경으로 처리한다.
- 프로젝트 설정을 변경한 뒤 동일한 전역 변경을 적용할지 사용자에게 묻고, 자동으로 전역 설정을 변경하지 않는다.
- 활성 텍스트나 설정이 바뀌면 한국어 참조 미러인 `kr/`도 동기화한다.
- 프로젝트와 전역 설정 모두 `question: allow`를 사용하며, `deep-interview`는 방향키·Enter 질문 UI를 우선 사용한다.
- 이름이 비슷한 `/Users/taehyunjeon/taehyun/dev/project/opencode` 디렉터리는 이 하네스가 아니므로 대상으로 사용하지 않는다.

## 작업 이력
v1에서 전역 규칙, permission, 여러 build specialist, feature/fix/review command, React/Django/Docker/Git skill을 만들었고 모델은 지정하지 않았다. v2에서는 사용자가 제공한 실제 모델 목록을 바탕으로 모델을 배정했다.

## 공식 OpenCode 확인 결과
2026-08-19 기준 agent는 단일 `model` override, primary/subagent, Task, `permission.task`, `default_agent`, `subagent_depth`를 지원한다. 공식 Agents/Config/Models 문서에는 순서형 model fallback 배열이 문서화되어 있지 않았다.

## 구조
사용자 -> `orchestrator`(Go Luna) -> PM/FE/BE/QA/figma-analyzer. Go primary 자체가 실행 불가하면 사용자가 `orchestrator-plus`로 수동 전환한다.

## 수정 규칙
다음 에이전트는 이 파일, `MODEL_ROUTING.md`, `README.md`를 먼저 읽고 새 config key는 최신 공식 문서를 확인한다. 사용자가 새 모델 목록을 주지 않으면 확인된 모델 ID만 쓴다. Go 사용량 정책 변경 시 최신 공식 한도를 다시 확인한다. 활성 파일을 바꾸면 대응 `kr/` 파일도 갱신한다. 수동 provider 전환을 자동 fallback이라 부르지 않는다.

## 다음 작업 큐
새 세션을 시작할 때 다음 순서로 진행한다.
1. `/report`로 실제 사용량 telemetry baseline을 만들고, 프롬프트나 세션 본문을 저장하지 않은 집계 결과를 최소 1주일 기록한다.
2. findings, decisions, changed files, risks, verification, next action을 포함하는 간결한 에이전트 handoff 형식을 표준화한다. (완료: `/handoff`에 필수 형식을 정의했다.)
3. 작업 복잡도(`tiny`, `standard`, `complex`)에 따른 라우팅을 추가해 작은 작업은 primary가 처리하고 전문화 효과가 있는 작업만 위임한다.
4. baseline 데이터로 모델 라우팅을 조정하고 비용, 소요 시간, QA 재작업의 전후 결과를 문서화한다.
5. 현재 plugin API를 확인한 뒤에만 로컬 telemetry 자동 수집과 루프 감지용 OpenCode plugin을 검토한다.
6. 아키텍처 다이어그램, 설치 방법, 측정 사례, 데모, 개인정보·안전성 한계를 포함해 포트폴리오 형태로 패키징한다.

첫 구현 단계는 완료했다. `scripts/opencode-report.py`와 `/report`가 로컬 OpenCode SQLite 데이터베이스를 읽기 전용으로 열어 세션, 비용, 토큰, 시간, 에이전트, 모델을 집계하며 프롬프트나 세션 본문은 출력하지 않는다. 전역 복사본은 `~/.config/opencode/` 아래에 있다.

## 미완료
실제 잔여 구독량 기반 동적 라우팅, 검증된 transport-level plugin fallback, 자동화된 telemetry baseline, 추가 specialist, 개인 repo 벤치마크는 아직 하지 않았다.
