---
description: Produce a concise continuation handoff for another agent
agent: orchestrator
---

다음 형식으로 간결한 연속 작업용 인수인계를 영어로 작성한다.

## Handoff: <한 줄 목표>

- **Goal**: 현재 세션 또는 작업의 목적을 한 문장으로 작성한다.
- **Findings**: 확인된 사실을 기록하고 필요한 경우 `file:line`을 덧붙인다. 가설이나 가정은 명시한다. 기존 프로젝트 컨텍스트와 다른 구조·맥락만 포함한다.
- **Completed work**: 실제 수행한 작업을 요약한다.
- **Decisions**: 이후 작업에 영향을 주는 결정과 간단한 근거를 기록한다.
- **Changed files**: `git status`/`git diff`를 기준으로 변경된 경로와 용도를 나열한다. 기존의 무관한 작업 트리 변경은 별도로 표시한다.
- **Risks & open issues**: 알려진 위험, 미해결 결함, 확인이 필요한 가정을 나열한다.
- **Verification**: 실제 실행한 명령과 결과를 나열한다. 실행하지 않은 검사는 `not run`으로 표시하며, 실행하지 않은 검사를 통과했다고 쓰지 않는다.
- **Next action**: 구체적인 다음 단계 하나와 담당 역할(`PM`, `FE`, `BE`, `QA`, `figma-analyzer`)을 제안한다.

**Goal**, **Verification**, **Next action**은 항상 포함한다. 보고할 내용이 없는 다른 섹션은 생략할 수 있다. 사실과 가정을 구분하고 정보를 지어내지 않는다. 인수인계는 채팅으로 출력하며, 프로젝트 수준 결정이 변경된 경우에만 `PROJECT_CONTEXT.md`를 수정한다.
