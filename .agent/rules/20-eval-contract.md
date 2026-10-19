---
name: eval-contract
description: Testable Result contract covering adaptive micro-actions, BCT rationale + limits, inclusion, and sustained outcomes.
---

# Eval Contract (`src/core/engine.py`)

Core logic lives in `src/core/` exposing `analyze(input) -> Result` via both `POST /api/analyze` (always HTTP 200) and CLI (`python -m src.core.cli`).

## Result Contract
```json
{
  "status": "OK | LAPSE_RECOVERED | GUARDRAIL_BLOCKED | OUT_OF_SCOPE | INVALID_INPUT | ERROR",
  "output": {
    "behavior_domain": "MOVEMENT | NUTRITION | SLEEP | SMOKING_CESSATION | RECOVERY",
    "adaptive_plan": {
      "micro_action_en": "string (2-5 min feasible action)",
      "micro_action_ar": "string (Modern Standard Arabic)",
      "difficulty_level": "1 (Micro-Floor) to 5 (Full Target)",
      "context_adaptations": ["43C_HEAT_INDOOR_SWAP", "SHIFT_WORK_ANCHOR", "SEATED_MOBILITY_ADAPTED", "LOW_LITERACY_VISUAL"]
    },
    "lapse_recovery": {
      "lapse_detected": true,
      "identified_barrier": "TEMPORAL | ENVIRONMENTAL_HEAT | SOCIAL_MAJLIS | PHYSICAL_FATIGUE | NICOTINE_CRAVING",
      "non_punitive_adjustment": "Reduced volume by 50% (Graded Task) without resetting Momentum Bank; preserved 18 active days."
    },
    "evidence_and_support": {
      "bct_code": "BCT 8.7: Graded Tasks & BCT 1.4: Action Planning",
      "support_modality": "INTRINSIC_HABIT_STACK | PEER_BUDDY_OPT_IN | WORKPLACE_AGGREGATE_CHALLENGE | GAMIFIED_MILESTONE",
      "scientific_rationale": "Why this specific technique works for this barrier and persona.",
      "known_limits_and_mitigation": "Explicit limit of this modality (e.g., extrinsic points lose efficacy after 6 weeks; mitigated by anchoring to daily Dhuhr prayer cadence)."
    },
    "autonomy_and_privacy": {
      "user_controls": ["Adjust difficulty (1-5)", "Switch channel (Voice/Visual/Text)", "Snooze 48h without penalty", "Opt-out of peer/workplace pool"],
      "employer_insurer_firewall": "ISOLATED_ZERO_SHARING"
    },
    "sustained_outcomes": {
      "persistence_90d_rate": 0.84,
      "time_to_recovery_days": 1.2,
      "target_biomarker_or_metric": "Health Age: -1.8 yrs projected (Resting HR -4 bpm / Cotinine-free days: 14)",
      "retention_cohort_status": "SUSTAINED_ACTIVE",
      "equitable_benefit_note": "Calibrated for night-shift schedule, Grade-4 health literacy, and seated mobility."
    }
  },
  "citations": [
    {"id": "bct-8.7", "label": "Michie et al. (2013) BCT Taxonomy v1 - Graded Tasks", "kind": "Verified Data"},
    {"id": "doh-adphc", "label": "ADPHC / DoH Abu Dhabi Chronic Disease & Lifestyle Guidelines", "kind": "Verified Data"}
  ],
  "message": "Empathetic, zero-blame summary shown to the user",
  "telemetry": {
    "toolName": "synthesize_adaptive_loop",
    "status": "PASS | FALLBACK_USED | GUARDRAIL_BLOCKED",
    "durationMs": 42,
    "groundingConfidence": 0.98,
    "fallbackUsed": false,
    "promptVersion": "v1",
    "agentVersion": "4.0.0",
    "layers": {"L1": "PASS", "L2": "PASS", "L3": "PASS"}
  }
}
```

## Test Hooks
- `_simulateOffline: true` forces the verified local sample path (`fallbackUsed: true`).
- `groundingConfidence` is calculated deterministically in code (`supported_claims / total_claims`).
