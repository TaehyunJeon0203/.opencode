---
description: 개인정보를 보호하는 로컬 OpenCode 사용량 리포트 생성
agent: orchestrator
subtask: false
---

`python3 scripts/opencode-report.py $ARGUMENTS`를 실행해 로컬 세션 수, 기록된 비용, 토큰 사용량, 세션 시간, 에이전트별 사용량, 모델별 사용량을 확인한다. OpenCode 데이터베이스를 읽기 전용으로 열며 프롬프트나 세션 본문은 출력하지 않는다.

선택 필터: `--since YYYY-MM-DD`, `--directory /path/to/project`, `--db /path/to/opencode.db`.
