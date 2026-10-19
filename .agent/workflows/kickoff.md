---
description: Locks the 6 official submission requirements, binds domain-packs/uae_health.md, defines the longitudinal Result contract, and sets the build plan.
---

# Workflow: `/kickoff`

When triggered, create `docs/KICKOFF.md` with these exact sections:
1. **Constraints & Submission Checklist** - the 6 official requirements from `40-submission-requirements.md`.
2. **Abu Dhabi Ecosystem Context** - bridging IFHAS screenings, Sahatna app journeys, Health Age scoring, Malaffi HIE, and wearable feeds into an adaptive behavior-change loop.
3. **Judging Rubric Alignment** - Adaptive personal plans (20%), Continuous learning & non-punitive re-engagement (20%), Evidence-based BCTs with visible rationale & limits (20%), User autonomy, accessibility & anti-punitive privacy (20%), Sustained longitudinal outcome measurement & equity (20%).
4. **Core System Friction** - Quantified gap between short-term campaign awareness and 90-day behavioral retention (`[SOURCED]` / `[ESTIMATE]`).
5. **Connected 4-Stage Loop** - (1) Contextual Intake & Barrier Sensing -> (2) Adaptive Micro-Action & BCT Selection -> (3) Non-Punitive Lapse Recovery & Support Calibration -> (4) Longitudinal Outcome & Equity Telemetry.
6. **Domain Binding** - Bind `domain-packs/uae_health.md` covering Movement, Nutrition, Sleep, Smoking Cessation, and Recovery.
7. **Contract Lock** - Confirm the JSON schema from `20-eval-contract.md`.
8. **Clock-Time Plan & The One Wow** - Live side-by-side comparison showing how a traditional wellness app punishes a 4-day lapse ("Streak Reset to 0!") versus how **Khatwa** diagnoses the barrier (43°C heat / shift fatigue), downshifts task difficulty by 50% (`BCT 8.7`), displays the scientific rationale and limits of the intervention, and preserves the user's Momentum Bank.

Then commit and push `checkpoint: kickoff` and output the Auto-Pilot Box for `/optimize`.
