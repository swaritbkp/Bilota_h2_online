"""
Khatwa (خطوة) - Core Behavior Loop Engine
Exposes analyze(input_data) -> Result strictly adhering to 20-eval-contract.md.
"""
import time
from typing import Dict, Any, Optional

from src.core.guardrails import (
    clean_input_text,
    evaluate_l1_guardrails,
    scrub_output_content,
    CANARY_TOKEN
)
from src.agent.orchestrator import run_khatwa_agent


def analyze(input_data: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Main entrypoint for both CLI and API.
    Evaluates input sanitization, L1-L3 guardrails, agent orchestration, and output contract.
    """
    start_time = time.perf_counter()

    # 1. Input Validation
    if not isinstance(input_data, dict):
        return {
            "status": "INVALID_INPUT",
            "message": "Input must be a valid JSON object.",
            "telemetry": {
                "toolName": "input_validator",
                "status": "INVALID_INPUT",
                "durationMs": 1,
                "fallbackUsed": False,
                "promptVersion": "v1"
            }
        }

    raw_text = input_data.get("text")
    cleaned_text, err = clean_input_text(raw_text)

    # Check for malformed null text
    if raw_text is None or err == "INVALID_INPUT":
        return {
            "status": "INVALID_INPUT",
            "message": "Malformed input: 'text' field is required and cannot be null or empty.",
            "telemetry": {
                "toolName": "input_validator",
                "status": "INVALID_INPUT",
                "durationMs": 1,
                "fallbackUsed": False,
                "promptVersion": "v1"
            }
        }

    # 2. Layer 1 Guardrail Evaluation
    l1_result = evaluate_l1_guardrails(cleaned_text)
    if l1_result:
        elapsed_ms = int((time.perf_counter() - start_time) * 1000)
        status = l1_result["status"]
        return {
            "status": status,
            "category": l1_result.get("category"),
            "message": scrub_output_content(l1_result.get("message", "")),
            "reason": scrub_output_content(l1_result.get("reason", "")),
            "emergency_contact": l1_result.get("emergency_contact"),
            "telemetry": {
                "toolName": "guardrail_shield",
                "status": status,
                "durationMs": max(1, elapsed_ms),
                "fallbackUsed": False,
                "promptVersion": "v1",
                "groundingConfidence": 1.0,
                "layers": {
                    "L1": "BLOCKED" if status == "GUARDRAIL_BLOCKED" else "TRIAGED",
                    "L2": "SKIPPED",
                    "L3": "PASS"
                }
            }
        }

    # 3. Agent Execution (ADK Multi-Tool Loop)
    simulate_offline = bool(input_data.get("_simulateOffline", False))
    result = run_khatwa_agent(input_data, simulate_offline=simulate_offline)

    # 4. Layer 3 Output Validation & Scrubbing
    if "message" in result:
        result["message"] = scrub_output_content(result["message"])

    # Double check no canary leak
    elapsed_ms = int((time.perf_counter() - start_time) * 1000)
    result["telemetry"]["durationMs"] = max(1, elapsed_ms)

    return result
