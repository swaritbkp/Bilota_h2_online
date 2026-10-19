---
name: safety-and-guardrails
description: 3-Layer defense: L1 deterministic + privacy/clinical shield, L2 Gemini classifier, L3 schema/canary/citation check.
---

# Safety & Guardrail Rules (`src/core/guardrails.py`)

## Layer 1 - Deterministic Input & Policy Shield (instant, zero network)
1. Normalize Unicode NFKC, strip zero-width chars (`\u200b`), clamp to 5,000 chars, strip `<script>`/HTML tags.
2. **Prompt Injection Patterns**: Block `ignore previous|all instructions`, `disregard ... directions`, `system prompt`, `developer mode`, `DAN mode`, `reveal ... configuration`, `repeat everything above`.
3. **Employer / Insurer Punitive Firewall**: Deterministically block requests seeking individual employee lapse lists, HR disciplinary exports, salary/allowance deductions, or insurance premium risk surcharges (`status: GUARDRAIL_BLOCKED`, `category: PUNITIVE_SURVEILLANCE_BLOCKED`).
4. **Clinical Acute Triage Shield**: Intercept acute medical emergencies (chest pain, dyspnoea, suicidal ideation, unprescribed medication dosing) -> return `status: OUT_OF_SCOPE` with immediate Abu Dhabi emergency instructions (`998` Ambulance / `999` Police / Estijaba `8001717`).

## Layer 2 - Model-Based Safety & Manipulation Classifier
- Fast Gemini call returning strict JSON: `{"attack": bool, "manipulative_dark_pattern": bool, "category": string, "reason": string}`.
- If L2 times out, fall back cleanly to L1 and log `L2_SKIPPED` in telemetry.

## Layer 3 - Output Validation & Canary Protection
1. Validate strict Pydantic/JSON schema.
2. **Canary Check**: System prompt embeds `PW-CANARY-7f3a91`. If output contains it, block immediately and log `CANARY_LEAK`.
3. **Zero-Shame Lexical Filter**: Scrub blaming language ("you failed", "streak destroyed", "reset to 0", "non-compliant patient") and replace with neutral friction-diagnostic framing.
4. **PII Scrub**: Mask Emirates ID (`784-XXXX-XXXXXXX-X`), medical record numbers (MRN), and phone numbers in logs/exports.
