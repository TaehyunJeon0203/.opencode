# Taehyun OpenCode Harness v2

역할별 모델, ChatGPT Plus/OpenCode Go 사용량 분리, hidden fallback subagent를 포함하는 개인 OpenCode 하네스다. 기본 primary는 `orchestrator`(Go Luna), Go 전체 장애/소진 시 수동 전환할 primary는 `orchestrator-plus`(OpenAI Luna)다. OpenCode 공식 문서는 순서형 model fallback 배열을 문서화하지 않으므로 Task와 별도 subagent로 구성했다. 상세는 `MODEL_ROUTING.md`, 이어서 개발할 에이전트는 `PROJECT_CONTEXT.md`를 먼저 읽는다.
