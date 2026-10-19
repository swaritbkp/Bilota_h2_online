---
name: eval-lite
description: Runs eval/run_eval.py to produce measured pass rates, latency metrics, and markdown benchmark reports.
---
# Skill: Eval-Lite Runner
Execute `python eval/run_eval.py --mode cmd --target "python -m src.core.cli"` to validate schema, status codes, citations, grounding confidence, latency budgets, and forbidden canary/shame strings. Never hand-edit `eval/benchmark-report.md`.
