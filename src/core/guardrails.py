"""
Khatwa (خطوة) - Layer 1-3 Guardrails Engine
Enforces input sanitization, prompt injection defense, employer/insurer privacy firewall,
clinical acute triage boundary, and zero-shame lexical scrubbing.
"""
import re
import unicodedata
from typing import Dict, Any, Optional, Tuple

CANARY_TOKEN = "PW-CANARY-7f3a91"

# Patterns for Prompt Injections
INJECTION_PATTERNS = [
    r"(?i)\b(ignore|disregard|forget|override)\b.*?\b(previous|all|prior|system)\b.*?\b(instruction|direction|prompt|rule|constraint)s?",
    r"(?i)\b(reveal|show|display|print|leak|output)\b.*?\b(system\s*prompt|canary|token|configuration|developer\s*mode|instructions)\b",
    r"(?i)\b(pw-canary|developer\s*mode|dan\s*mode|jailbreak)\b",
    r"(?i)\brepeat\s+(everything|all)\s+above\b",
]

# Patterns for Employer / Insurer Surveillance Abuse (UAE Federal Law No. 2 of 2019)
PUNITIVE_SURVEILLANCE_PATTERNS = [
    r"(?i)\b(export|list|report|dump)\b.*?\b(employee|staff|worker)s?\b.*?\b(relapse|miss|lapse|habit|target|smok|walk)\b.*?\b(hr|deduct|bonus|salary|penalt|punish|performance)\b",
    r"(?i)\b(deduct|dock|cut|penalize)\b.*?\b(wellness\s*bonus|bonus|salary|pay|allowance)\b",
    r"(?i)\b(raw\s+wearable|wearable\s+lapse|health\s+age\s+regression|adherence\s+log)s?\b.*?\b(policy|copay|co-pay|premium|underwrit|insurer|insurance)\b",
    r"(?i)\b(increase|raise|adjust)\b.*?\b(medical\s*insurance\s*co-?pay|insurance\s*co-?pay|premium)\b",
    r"(?i)\bfor\s+policy\s+#?784-\d+.*?\bco-?pay\b",
]

# Patterns for Clinical Acute Emergencies (UAE 998 Ambulance / 999 Police / 8001717 Estijaba)
CLINICAL_ACUTE_PATTERNS = [
    r"(?i)\b(crushing\s+chest\s+pain|chest\s+pain\s+radiating|radiating\s+to\s+(my\s+)?left\s+arm)\b",
    r"(?i)\b(chest\s+pain)\b.*?\b(shortness\s+of\s+breath|dyspnea|breathing)\b",
    r"(?i)\b(shortness\s+of\s+breath)\b.*?\b(chest\s+pain|left\s+arm)\b",
    r"(?i)\b(aspirin\s+dose|nitroglycerin\s+dose|medication\s+dose|how\s+many\s+mg\s+of\s+aspirin)\b",
    r"(?i)\b(suicid|kill\s+myself|end\s+my\s+life|self-harm)\b",
]

# Zero-Shame Scrubber Patterns
SHAME_PATTERNS = [
    (r"(?i)\bstreak\s+(lost|destroyed|broken|failed)\b", "momentum preserved in Momentum Bank"),
    (r"(?i)\breset\s+to\s+zero\b", "adjusted to a feasible micro-floor"),
    (r"(?i)\breset\s+to\s+0\b", "adjusted to a feasible micro-floor"),
    (r"(?i)\byou\s+failed\b", "temporary friction observed"),
    (r"(?i)\bnon-compliant\s+patient\b", "individual navigating environmental barriers"),
]


def clean_input_text(raw_text: Optional[str]) -> Tuple[Optional[str], Optional[str]]:
    """Layer 1: Normalizes text, strips zero-width chars and HTML, checks bounds."""
    if raw_text is None:
        return None, "INVALID_INPUT"
    
    # Strip zero-width chars & unicode normalization
    cleaned = re.sub(r"[\u200b\u200c\u200d\u200e\u200f\ufeff]", "", str(raw_text))
    cleaned = unicodedata.normalize("NFKC", cleaned)
    # Strip HTML tags
    cleaned = re.sub(r"<[^>]*>", "", cleaned).strip()
    
    if not cleaned:
        return None, "INVALID_INPUT"
    
    # Clamp to 5000 characters
    if len(cleaned) > 5000:
        cleaned = cleaned[:5000]
        
    return cleaned, None


def evaluate_l1_guardrails(text: str) -> Optional[Dict[str, Any]]:
    """
    Evaluates deterministic Layer 1 filters:
    1. Prompt Injections -> GUARDRAIL_BLOCKED
    2. Employer/Insurer Punitive Surveillance -> GUARDRAIL_BLOCKED
    3. Clinical Acute Triage -> OUT_OF_SCOPE (with 998 emergency redirect)
    """
    # 1. Prompt Injections
    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, text):
            return {
                "status": "GUARDRAIL_BLOCKED",
                "category": "PROMPT_INJECTION",
                "message": "Blocked: Prompt injection or instruction override attempt intercepted.",
                "reason": "Direct or obfuscated instruction override and canary probe blocked by Layer 1 Shield.",
            }

    # 2. Punitive Surveillance Firewall
    for pattern in PUNITIVE_SURVEILLANCE_PATTERNS:
        if re.search(pattern, text):
            return {
                "status": "GUARDRAIL_BLOCKED",
                "category": "PUNITIVE_SURVEILLANCE_BLOCKED",
                "message": "Request Blocked: Individual behavioral logs cannot be exported for HR disciplinary action or insurance underwriting under UAE Federal Law No. 2 of 2019.",
                "reason": "UAE Health Data Sovereignty Firewall: Zero-sharing policy protects individual adherence, lapse logs, and Health Age records from punitive use.",
            }

    # 3. Clinical Acute Triage
    for pattern in CLINICAL_ACUTE_PATTERNS:
        if re.search(pattern, text):
            return {
                "status": "OUT_OF_SCOPE",
                "category": "CLINICAL_ACUTE_EMERGENCY",
                "message": "EMERGENCY ALERT: Potential acute medical condition detected. Call 998 (Abu Dhabi Ambulance) or 999 (Police) immediately. If urgent support is needed, contact the DoH Estijaba Service at 8001717.",
                "emergency_contact": {"ambulance": "998", "police": "999", "estijaba": "8001717"},
                "reason": "Khatwa is an adaptive preventive lifestyle companion and is strictly prohibited from providing acute clinical triage, diagnostic advice, or emergency medication dosing.",
            }

    return None


def scrub_output_content(text: str) -> str:
    """Layer 3: Removes canary tokens, scrubs guilt/shame language, and masks PII."""
    if not text:
        return ""
    
    out = text
    # 1. Canary scrubbing
    if CANARY_TOKEN in out or "PW-CANARY" in out:
        out = out.replace(CANARY_TOKEN, "[PROTECTED_TOKEN]").replace("PW-CANARY", "[PROTECTED_TOKEN]")
    
    # 2. Zero-shame filter
    for pattern, replacement in SHAME_PATTERNS:
        out = re.sub(pattern, replacement, out)
        
    # 3. PII masking (Emirates ID)
    out = re.sub(r"\b784-\d{4}-\d{7}-\d\b", "784-XXXX-XXXXXXX-X", out)
    
    return out
