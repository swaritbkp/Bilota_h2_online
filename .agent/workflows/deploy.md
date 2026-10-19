---
description: Production build verification, public repo secret scan, comprehensive judge README, and demo-freeze git tag.
---

# Workflow: `/deploy`

When triggered:
1. Run `python eval/run_eval.py` and verify 100% `[MEASURED]` pass rate.
2. Run the secret scan: ensure `.env` is untracked and no `AIza...` or `AQ...` keys exist in working tree or git history.
3. Finalize the judge-facing `README.md` with:
   - Executive Summary & Problem Framing (Abu Dhabi behavioral retention gap).
   - 5-Domain Adaptive Architecture (Movement, Nutrition, Sleep, Smoking, Recovery).
   - How the Zero-Blame Lapse Recovery & Momentum Bank work.
   - Visible Evidence Table: BCT Codes, Support Modalities, Scientific Rationale, and Explicit Limits.
   - User Autonomy, Accessibility (Disability/Literacy/Shift-work), and Anti-Punitive Firewall.
   - Sustained Outcome & Equity Metrics (Persistence, Time-to-Recovery, Health Age delta).
   - **Gen AI Services Used** table (synced with `docs/GENAI-SERVICES.md`).
   - Quickstart & Live Deployed URL.
4. Commit, push, and tag `demo-freeze`. Print the Auto-Pilot Box for `/submit`.
