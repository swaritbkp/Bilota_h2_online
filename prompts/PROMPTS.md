# Master Copy-Paste Execution Commands (Khatwa v4.0)

## Step 1: `/kickoff`
```text
/kickoff
Problem Statement: Help people in Abu Dhabi start, maintain, and recover healthier behaviors (movement, nutrition, sleep, smoking cessation, recovery) through support that adapts to their goals, circumstances, motivation, and setbacks over time. Bridge existing building blocks (IFHAS screening, Sahatna app journeys, Health Age scoring, wearable data, workplace/community campaigns) into an adaptive behavior-change loop that translates goals into small feasible actions, detects declining engagement or lapses without blame, uses evidence-based behavior-change techniques (with rationale and limits visible), protects user autonomy/inclusion/accessibility against employer or insurer punishment, and measures sustained longitudinal outcomes and equitable benefit.
Total build time: 36 hours
Pitch length: 3 minutes
Team size: 1
Public GitHub repo URL: https://github.com/swaritbkp/h2s_bilota
Mandated tech / judging criteria: Google ADK + Gemini (Flash/Pro) | Adaptive personal plans, continuous learning & zero-blame re-engagement, BCT evidence + visible limits, autonomy/accessibility/anti-punitive privacy, sustained longitudinal outcomes.
Depth: FULL
```

## Step 2: `/optimize`
```text
/optimize
Mode: High Thinking Enabled
Build the full Khatwa application from docs/KICKOFF.md and domain-packs/uae_health.md:
1. src/core/: guardrails.py (L1-L3 + HR/Insurer punitive block + 998 clinical triage + zero-shame scrubber), bct_engine.py (BCT Taxonomy v1 + visible rationale & limits), outcomes.py (Momentum Bank, Time-to-Recovery, 90d persistence, Health Age delta, Equitable Benefit Index), engine.py & cli.py (Result contract).
2. src/agent/: Google ADK + Gemini 2.5 Flash/Pro with 4 connected tools, tagging every Gen AI call in docs/GENAI-SERVICES.md.
3. src/ui/ & src/app.py: FastAPI + interactive bilingual (AR/EN RTL) & accessible (Low-Literacy / Seated Mobility) dashboard with pinned Judge Control Bar (3 Personas: Fatima, Tariq, Aisha; Lapse Simulator; Hostile HR/Injection Attack tester; BCT & Limits Telemetry Drawer).
4. Verify 100% pass rate on eval/run_eval.py.
```

## Step 3: `/guardrails`
```text
/guardrails
Run eval/run_eval.py across all 10 vectors (Fatima heat lapse, Tariq night-shift smoking slip, Aisha seated low-literacy mode, offline fallback, direct/paraphrased/obfuscated injections, corporate HR punitive surveillance block, acute clinical chest-pain block, oversized input). Record [MEASURED] results in eval/benchmark-report.md and docs/GUARDRAIL-NOTES.md.
```

## Step 4: `/scale`
```text
/scale
Generate docs/ARCHITECTURE.md covering Sahatna & Malaffi HL7 FHIR R4 integration, UAE Federal Law No. 2 of 2019 privacy vault isolation, and Gemini Flash/Pro tiering.
```

## Step 5: `/deploy`
```text
/deploy
Run production check, scan for leaked keys, finalize judge README.md with Gen AI Services table and BCT Rationale/Limits summary, commit, push, and tag demo-freeze.
```

## Step 6: `/submit`
```text
/submit
Audit all 6 official submission requirements in docs/SUBMISSION.md, reconcile docs/GENAI-SERVICES.md, and generate the 2-minute demo video script in docs/DEMO-VIDEO.md.
```

## Step 7: `/pitch`
```text
/pitch
Generate PITCH_SCRIPT.md, docs/SLIDES.md, and docs/JUDGE-QA.md with [MEASURED] and [SOURCED] tags.
```
