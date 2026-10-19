# Gen AI Services Register

Updated whenever a Gen AI service is called.

| Service / Model | Purpose | Where in code (`file:function`) | Where the user sees it | Live or fallback |
|---|---|---|---|---|
| Google ADK (`google-adk`) | Multi-tool behavioral orchestration & state routing | `src/agent/orchestrator.py:run_khatwa_agent` | Adaptive Plan Card & Telemetry Drawer | Live (deterministic BCT fallback on timeout) |
| Gemini 2.5 Flash (`gemini-2.5-flash`) | Low-latency barrier classification, L2 safety check, & BCT micro-action synthesis | `src/agent/tools.py:craft_graded_micro_action` | Instant Micro-Action Plan & L2 Shield | Live (`TOOL_TIMEOUT_MS=2500` with verified local fallback) |
| Gemini 2.5 Pro (`gemini-2.5-pro`) | Culturally nuanced bilingual (AR/EN) non-blaming lapse reframing & rationale explanation | `src/agent/tools.py:reframe_lapse_empathetically` | Bilingual Coach Message & BCT Rationale/Limits Card | Live (with verified local fallback) |
