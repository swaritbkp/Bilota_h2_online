---
description: Builds the working Khatwa app, 4 ADK tools, 3-persona Judge Control Bar, bilingual/accessible UI, and deploys the public skeleton.
---

# Workflow: `/optimize`

When triggered:
1. Read `docs/KICKOFF.md` and `domain-packs/uae_health.md`.
2. Build `src/core/`:
   - `src/core/guardrails.py`: L1 deterministic shield (injection regex, Employer/Insurer punitive block, acute clinical emergency redirect to 998/999), L2 classifier hook, L3 schema/canary (`PW-CANARY-7f3a91`) and zero-shame lexical scrubber.
   - `src/core/bct_engine.py`: Deterministic mapping of barriers (heat, time, shift fatigue, cravings, mobility, social dining) to Michie's BCT Taxonomy v1 codes, pairing each with its **Scientific Rationale** AND **Known Limits + Mitigation**.
   - `src/core/outcomes.py`: Deterministic calculation of Momentum Bank (anti-streak), Time-to-Recovery (TTR), 90-day persistence score, Health Age / biomarker trajectory, and Equitable Benefit Index.
   - `src/core/engine.py` & `src/core/cli.py`: Exposes `analyze(input) -> Result` adhering strictly to `20-eval-contract.md`.
3. Build `src/agent/` using Google ADK + Gemini:
   - Tool 1: `sense_context_and_barrier` (evaluates wearable drop-off, ambient temp, shift schedule, accessibility needs).
   - Tool 2: `craft_graded_micro_action` (generates bilingual AR/EN feasible actions across movement, nutrition, sleep, or smoking cessation).
   - Tool 3: `calibrate_support_and_limits` (selects intrinsic habit stack, peer buddy, or workplace aggregate challenge and outputs visible rationale + limits).
   - Tool 4: `compute_sustained_outcomes` (updates longitudinal persistence, recovery speed, and biomarker delta).
   - Tag every Gen AI call site with `# GENAI-SERVICE: <model> | <purpose>` and update `docs/GENAI-SERVICES.md`.
4. Build `src/ui/` (FastAPI `src/app.py` + rich interactive single-page dashboard):
   - Pinned Judge Control Bar: 3 Personas (Fatima, Tariq, Aisha), Simulate Lapse button, Hostile/Punitive HR Attack button, BCT & Telemetry Inspector drawer, AR/EN RTL toggle, and Low-Literacy / Accessibility mode toggle.
   - Visible `OFFLINE MODE - verified sample data` badge when `FORCE_OFFLINE=1` or API times out (`TOOL_TIMEOUT_MS=2500`).
5. Create judge-facing `README.md` stub and verify `python eval/run_eval.py` passes 100% locally.
6. Commit and push `checkpoint: optimize` and print the Auto-Pilot Box for `/guardrails`.
