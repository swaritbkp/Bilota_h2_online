# Khatwa (خطوة) — Abu Dhabi Adaptive Behavior Pack v4.0

Challenge: Help people in Abu Dhabi start, maintain, and recover healthier behaviors (movement, nutrition, sleep, smoking cessation, recovery) through support that adapts to their goals, circumstances, motivation, and setbacks over time.

## The 6 Official Submission Requirements
1. GitHub repository link submitted on the platform.
2. The repository is published and set to PUBLIC access.
3. "Deployed Project" link submitted on the platform.
4. Brief description of the project built (~120-150 words).
5. Clearly mention which Gen AI services were used AND where in the submission.
6. Project demo video link for evaluators to review.

## Pipeline
| # | Command | What it does | Output |
|---|---------|--------------|--------|
| 1 | `/kickoff` | Locks 6 requirements, binds `uae_health.md`, sets longitudinal contract | `docs/KICKOFF.md` |
| 2 | `/optimize` | Builds 5-module app, Judge Bar, 4 ADK tools, bilingual/accessible UI, public deploy | working app + live URL |
| 3 | `/guardrails` | L1/L2/L3 defense + Employer/Insurer privacy firewall + measured `run_eval.py` | `eval/benchmark-report.md` |
| 4 | `/scale` | Malaffi/Sahatna HL7 FHIR integration, UAE data residency, cost/latency tiering | `docs/ARCHITECTURE.md` |
| 5 | `/deploy` | Redeploy, secret scan, judge README with Gen AI table, `demo-freeze` tag | `demo-freeze` tag |
| 6 | `/submit` | Audits all 6 requirements, reconciles Gen AI register, writes video script | `docs/SUBMISSION.md` |
| 7 | `/pitch` | Timed script, slide deck, and 7-question Judge Defense Matrix | `PITCH_SCRIPT.md` |
| - | `/rescue` | Anytime emergency triage: revert to last green checkpoint, protect submission floor | rescue plan |
