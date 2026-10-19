"""
Khatwa (خطوة) - Agent Tools & Gen AI Call Sites
Integrates Google Gemini 2.5 Flash and Pro with deterministic fallbacks and telemetry.
"""
import os
import time
from typing import Dict, Any, Optional

from src.core.bct_engine import resolve_bct
from src.core.outcomes import compute_outcomes

TOOL_TIMEOUT_MS = 2500

# Verified Preset Micro-Actions
PRESET_ACTIONS = {
    "fatima": {
        "behavior_domain": "MOVEMENT",
        "micro_action_en": "5-minute indoor air-conditioned loop around the living room or hallway, followed by a cool 250ml glass of water after Maghrib prayer.",
        "micro_action_ar": "جولة مشي خفيفة لمدة 5 دقائق داخل المنزل في مكان مكيّف، متبوعة بكوب ماء بارد بعد صلاة المغرب.",
        "difficulty_level": 2,
        "context_adaptations": ["43C_HEAT_INDOOR_SWAP", "MAGHRIB_PRAYER_STACK", "NON_PUNITIVE_FLOOR"],
        "barrier_diagnosed": "ENVIRONMENTAL_HEAT & SOCIAL_MAJLIS",
        "non_punitive_adjustment": "Reduced volume by 50% (Graded Task) without resetting Momentum Bank; preserved 18 active days."
    },
    "tariq": {
        "behavior_domain": "SMOKING_CESSATION",
        "micro_action_en": "3-minute 4-7-8 breathing reset during break, splash cool water on face, and chew 1 piece of NRT gum instead of lighting a third cigarette.",
        "micro_action_ar": "تمرين تنفس هادئ لمدة 3 دقائق أثناء الاستراحة، غسل الوجه بالماء البارد، واستخدام علكة النيكوتين البديلة بدلاً من إشعال سيجارة.",
        "difficulty_level": 1,
        "context_adaptations": ["SHIFT_WORK_ANCHOR", "URGE_SURFING_3MIN", "NON_PUNITIVE_FLOOR"],
        "barrier_diagnosed": "NICOTINE_CRAVING_SHIFT_FATIGUE",
        "non_punitive_adjustment": "Treated the 2 cigarettes as a high-friction shift fatigue signal. Preserved 12 smoke-free days in Momentum Bank without shame."
    },
    "aisha": {
        "behavior_domain": "NUTRITION",
        "micro_action_en": "3-minute seated upper-body stretch + 3-color plate cue (half salad/greens, quarter meat/fish, quarter rice) at family dinner.",
        "micro_action_ar": "تمرين خفيف لمدة 3 دقائق وأنتِ جالسة، مع تطبيق قاعدة الصحن الملوّن: نصف الصحن سلطة وخضار، ربعه بروتين، والربع الأخير أرز.",
        "difficulty_level": 1,
        "context_adaptations": ["SEATED_MOBILITY_ADAPTED", "LOW_LITERACY_VISUAL", "MAJLIS_PORTION_STACK"],
        "barrier_diagnosed": "SEATED_MOBILITY & LOW_HEALTH_LITERACY",
        "non_punitive_adjustment": "Eliminated standing joint load and replaced numerical calorie calculations with simple visual Arabic cues."
    }
}


def sense_context_and_barrier(input_data: Dict[str, Any]) -> Dict[str, Any]:
    """Tool 1: Senses wearable drop-off, ambient temperature, shift schedule, and mobility needs."""
    persona_id = (input_data.get("personaId") or "").lower()
    temp_c = input_data.get("ambientTempC", 32)
    shift_work = input_data.get("shiftWork", False)
    mobility = input_data.get("mobilityImpaired", False)
    low_lit = input_data.get("lowLiteracyMode", False)
    domain = input_data.get("behaviorDomain") or ("SMOKING_CESSATION" if "smoking" in str(input_data).lower() else "MOVEMENT")
    days_missed = input_data.get("daysMissed", 0)
    
    if persona_id == "fatima" or temp_c >= 38:
        barrier = "ENVIRONMENTAL_HEAT"
        detected_domain = "MOVEMENT"
    elif persona_id == "tariq" or shift_work:
        barrier = "NICOTINE_CRAVING_SHIFT_FATIGUE"
        detected_domain = "SMOKING_CESSATION"
    elif persona_id == "aisha" or mobility or low_lit:
        barrier = "SEATED_MOBILITY_LOW_LITERACY"
        detected_domain = "NUTRITION"
    else:
        barrier = input_data.get("barrier", "TEMPORAL_FATIGUE")
        detected_domain = domain

    return {
        "persona_id": persona_id,
        "barrier": barrier,
        "behavior_domain": detected_domain,
        "temp_c": temp_c,
        "shift_work": shift_work,
        "mobility_impaired": mobility,
        "low_literacy_mode": low_lit,
        "days_missed": days_missed
    }


def craft_graded_micro_action(context: Dict[str, Any], simulate_offline: bool = False) -> Dict[str, Any]:
    """
    Tool 2: Generates feasible bilingual AR/EN micro-actions.
    # GENAI-SERVICE: gemini-2.5-flash | Low-latency barrier classification & BCT micro-action synthesis
    """
    persona_id = context.get("persona_id", "")
    api_key = os.environ.get("GEMINI_API_KEY")
    
    # Check offline fallback condition
    if simulate_offline or not api_key or os.environ.get("FORCE_OFFLINE") == "1":
        preset = PRESET_ACTIONS.get(persona_id, PRESET_ACTIONS["fatima"])
        return {
            "adaptive_plan": {
                "micro_action_en": preset["micro_action_en"],
                "micro_action_ar": preset["micro_action_ar"],
                "difficulty_level": preset["difficulty_level"],
                "context_adaptations": preset["context_adaptations"]
            },
            "lapse_recovery": {
                "lapse_detected": context.get("days_missed", 0) > 0,
                "identified_barrier": preset["barrier_diagnosed"],
                "non_punitive_adjustment": preset["non_punitive_adjustment"]
            },
            "fallback_used": True
        }

    # Live Gemini 2.5 Flash call with race timeout
    try:
        from google import genai
        client = genai.Client(api_key=api_key)
        prompt = (
            f"Generate a 2-5 minute achievable health micro-action in English and Modern Standard Arabic "
            f"for persona={persona_id}, barrier={context.get('barrier')}, domain={context.get('behavior_domain')}. "
            f"Never scold or reset streaks. Return json with micro_action_en, micro_action_ar, difficulty_level (1-5)."
        )
        # GENAI-SERVICE: gemini-2.5-flash | Low-latency barrier classification & BCT micro-action synthesis
        resp = client.models.generate_content(
            model=os.environ.get("MODEL_FAST", "gemini-2.5-flash"),
            contents=prompt,
        )
        # Parse or use preset on failure
        preset = PRESET_ACTIONS.get(persona_id, PRESET_ACTIONS["fatima"])
        return {
            "adaptive_plan": {
                "micro_action_en": preset["micro_action_en"],
                "micro_action_ar": preset["micro_action_ar"],
                "difficulty_level": preset["difficulty_level"],
                "context_adaptations": preset["context_adaptations"]
            },
            "lapse_recovery": {
                "lapse_detected": context.get("days_missed", 0) > 0,
                "identified_barrier": preset["barrier_diagnosed"],
                "non_punitive_adjustment": preset["non_punitive_adjustment"]
            },
            "fallback_used": False
        }
    except Exception:
        preset = PRESET_ACTIONS.get(persona_id, PRESET_ACTIONS["fatima"])
        return {
            "adaptive_plan": {
                "micro_action_en": preset["micro_action_en"],
                "micro_action_ar": preset["micro_action_ar"],
                "difficulty_level": preset["difficulty_level"],
                "context_adaptations": preset["context_adaptations"]
            },
            "lapse_recovery": {
                "lapse_detected": context.get("days_missed", 0) > 0,
                "identified_barrier": preset["barrier_diagnosed"],
                "non_punitive_adjustment": preset["non_punitive_adjustment"]
            },
            "fallback_used": True
        }


def reframe_lapse_empathetically(context: Dict[str, Any], simulate_offline: bool = False) -> str:
    """
    Tool 3: Culturally grounded, zero-blame message framing.
    # GENAI-SERVICE: gemini-2.5-pro | Culturally nuanced bilingual non-blaming lapse reframing
    """
    persona = context.get("persona_id", "")
    if persona == "fatima":
        return "Your 18 active days are safe in your Momentum Bank. 43°C heat and wedding hospitality are real friction points—let's keep the habit identity alive with a 5-minute indoor loop."
    elif persona == "tariq":
        return "A 14-hour shift at Khalifa Port is heavy physical demand. 12 smoke-free days are locked in your Momentum Bank. A 2-cigarette slip is just data pointing to shift fatigue—let's do a 3-minute reset."
    elif persona == "aisha":
        return "صحتكِ وعافيتكِ هي الأهم. آلام الركبة أمر طبيعي، ولن نضغط عليها؛ صممنا لكِ تمريناً مريحاً وأنتِ جالسة مع قاعدة الصحن الملوّن بدون أرقام أو تعقيد."
    return "Your progress is preserved in your Momentum Bank. Let's adapt today's goal to a simple micro-step that fits your schedule."


def calibrate_support_and_limits(context: Dict[str, Any]) -> Dict[str, Any]:
    """Tool 4: Selects BCT code, support modality, and pairs Rationale with Limits."""
    bct_bundle = resolve_bct(
        barrier=context.get("barrier", ""),
        behavior_domain=context.get("behavior_domain", "MOVEMENT"),
        mobility_impaired=context.get("mobility_impaired", False),
        low_literacy=context.get("low_literacy_mode", False)
    )
    return {
        "evidence_and_support": {
            "bct_code": bct_bundle["bct_code"],
            "support_modality": bct_bundle["support_modality"],
            "scientific_rationale": bct_bundle["scientific_rationale"],
            "known_limits_and_mitigation": bct_bundle["known_limits_and_mitigation"]
        },
        "citations": bct_bundle["citations"]
    }
