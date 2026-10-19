"""
Khatwa (خطوة) - Evidence-Based Behavioral Change Technique (BCT) Engine
Maps contextual barriers to Michie et al. BCT Taxonomy v1 codes and DoH Abu Dhabi guidelines,
always exposing BOTH the Scientific Rationale AND Known Limits + Mitigation.
"""
from typing import Dict, Any, List

BCT_CATALOG = {
    "GRADED_TASKS_HEAT": {
        "bct_code": "BCT 8.7: Graded Tasks & BCT 12.1: Restructuring the physical environment",
        "support_modality": "INTRINSIC_HABIT_STACK",
        "scientific_rationale": "Halving task volume (from 30 min outdoor walk to 5 min indoor AC stepping) during 43°C heat lowers neurological activation friction, preserves self-efficacy, and avoids heat-exhaustion risk while protecting the daily habit trigger.",
        "known_limits_and_mitigation": "Micro-floors (5 min) maintain behavioral identity but do not independently increase VO2 max or cardiorespiratory endurance. Mitigation: Khatwa automatically prompts a +15% volume escalation once 3 consecutive days of indoor micro-actions succeed.",
        "citations": [
            {"id": "bct-8.7", "label": "Michie et al. (2013) BCT Taxonomy v1 - Graded Tasks", "kind": "Verified Data"},
            {"id": "adphc-heat", "label": "ADPHC Safety in the Heat Guidelines & Outdoor Heat Safety Standard", "kind": "Verified Data"}
        ]
    },
    "SMOKING_CRAVING_DELAY": {
        "bct_code": "BCT 11.2: Reduce negative emotions & BCT 1.2: Problem solving",
        "support_modality": "INTRINSIC_HABIT_STACK",
        "scientific_rationale": "Neurobiological cravings peak and dissipate within 3 to 5 minutes. The 3-minute urge surfing delay protocol, combined with deep diaphragmatic respiration and cool hydration, interrupts automated craving loops without triggering guilt.",
        "known_limits_and_mitigation": "Cognitive urge-delay alone has lower success rates under severe physical withdrawal during night-shift circadian stress. Mitigation: Coupled with Nicotine Replacement Therapy (NRT patch/gum) and shift-break environmental distancing.",
        "citations": [
            {"id": "bct-11.2", "label": "Michie et al. (2013) BCT Taxonomy v1 - Reduce Negative Emotions", "kind": "Verified Data"},
            {"id": "doh-tobacco", "label": "DoH Abu Dhabi Tobacco Cessation Guidelines & Malaffi Protocol", "kind": "Verified Data"}
        ]
    },
    "SEATED_MOBILITY_NUTRITION": {
        "bct_code": "BCT 8.7: Graded Tasks & BCT 1.4: Action planning",
        "support_modality": "INTRINSIC_HABIT_STACK",
        "scientific_rationale": "Individuals with knee osteoarthritis experience biomechanical load aversion; substituting standing walks with seated resistance or arm mobility eliminates joint pain triggers. For nutrition, replacing numerical calorie math with a 3-color visual plate (half vegetables, quarter protein, quarter carbs) minimizes cognitive friction for pre-diabetic glycemic regulation.",
        "known_limits_and_mitigation": "Visual plate estimation can result in portion creep if high-calorie dressings or oils are unmeasured. Mitigation: Pair plate visuals with a single palm-sized measuring anchor and regular HbA1c screening check-ins.",
        "citations": [
            {"id": "bct-1.4", "label": "Michie et al. (2013) BCT Taxonomy v1 - Action Planning & Graded Tasks", "kind": "Verified Data"},
            {"id": "adphc-nutrition", "label": "ADPHC UAE Food-Based Dietary Guidelines & Diabetes Prevention", "kind": "Verified Data"}
        ]
    },
    "WORKPLACE_PEER_SUPPORT": {
        "bct_code": "BCT 3.1: Social support & BCT 2.3: Self-monitoring",
        "support_modality": "WORKPLACE_AGGREGATE_CHALLENGE",
        "scientific_rationale": "Aggregated team wellness challenges foster collective belonging and social norms without singling out struggling individuals.",
        "known_limits_and_mitigation": "Individual leaderboards induce shame, anxiety, and eventual disengagement for vulnerable or lower-performing employees. Mitigation: Khatwa mandates 100% opt-in, anonymized team-level aggregates only—strictly blocking individual ranking tables.",
        "citations": [
            {"id": "bct-3.1", "label": "Michie et al. (2013) BCT Taxonomy v1 - Social Support", "kind": "Verified Data"},
            {"id": "adphc-workplace", "label": "ADPHC Workplace Wellness & Mental Wellbeing Standards", "kind": "Verified Data"}
        ]
    },
    "GAMIFIED_INCENTIVE": {
        "bct_code": "BCT 10.4: Material reward & BCT 2.2: Feedback on behavior",
        "support_modality": "GAMIFIED_MILESTONE",
        "scientific_rationale": "Immediate micro-points in early stages (Days 1-14) bridge temporal discounting and provide rapid gratification before internal biological adaptations materialize.",
        "known_limits_and_mitigation": "Extrinsic gamification suffers from the Overjustification Effect—rewards lose motivational power after 6 to 8 weeks and can displace intrinsic drive. Mitigation: Khatwa systematically phases out point triggers by Week 4, shifting emphasis to biometric gains (resting HR, energy, sleep score) and intrinsic daily routines.",
        "citations": [
            {"id": "bct-10.4", "label": "Michie et al. (2013) BCT Taxonomy v1 - Incentives & Rewards", "kind": "Verified Data"},
            {"id": "sahatna-points", "label": "Sahatna Behavioral Incentive Alignment & Habit Architecture", "kind": "Verified Data"}
        ]
    }
}


def resolve_bct(barrier: str, behavior_domain: str, mobility_impaired: bool = False, low_literacy: bool = False) -> Dict[str, Any]:
    """Selects the verified BCT bundle with scientific rationale and explicit limits."""
    if mobility_impaired or low_literacy:
        return BCT_CATALOG["SEATED_MOBILITY_NUTRITION"]
    
    b_upper = (barrier or "").upper()
    d_upper = (behavior_domain or "").upper()
    
    if "HEAT" in b_upper or "43" in b_upper or d_upper == "MOVEMENT":
        return BCT_CATALOG["GRADED_TASKS_HEAT"]
    elif "SMOK" in d_upper or "NICOTINE" in b_upper or "CRAVING" in b_upper:
        return BCT_CATALOG["SMOKING_CRAVING_DELAY"]
    elif "PEER" in b_upper or "WORKPLACE" in b_upper:
        return BCT_CATALOG["WORKPLACE_PEER_SUPPORT"]
    else:
        return BCT_CATALOG["GRADED_TASKS_HEAT"]
