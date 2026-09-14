---
description: Diagnose and fix a bug with root-cause-first routing
agent: orchestrator
---

Diagnose and fix: $ARGUMENTS

Do not patch blindly. Use FE or BE for evidence-first diagnosis and implementation. For any code change, automatically continue through implementation -> read-only QA -> implementation fix -> QA, stopping only on PASS or after three QA rounds. Do not claim completion before PASS; at the cap, report unresolved findings.
