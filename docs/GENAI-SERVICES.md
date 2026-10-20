# Gen AI Services Register

Updated whenever a Gen AI service is called. Aligned with Google ADK, Gemini 2.5, and Sovereign Behavioral Loop.

| Service / Model | Purpose | Where in code (`file:function`) | Where the user sees it | Live or fallback |
|---|---|---|---|---|
| Google ADK (`google-adk`) | Multi-tool behavioral orchestration & state routing | `src/agent/orchestrator.py:run_khatwa_agent` | Adaptive Plan Card & Telemetry Drawer | Live (deterministic BCT fallback on timeout) |
| Gemini 2.5 Flash (`gemini-2.5-flash`) | Low-latency barrier classification, L2 safety check, & BCT micro-action synthesis | `src/agent/tools.py:craft_graded_micro_action` | Instant Micro-Action Plan & L2 Shield | Live (`TOOL_TIMEOUT_MS=2500` with verified local fallback) |
| Gemini 2.5 Pro (`gemini-2.5-pro`) | Culturally nuanced bilingual (AR/EN) non-blaming lapse reframing & rationale explanation | `src/agent/tools.py:reframe_lapse_empathetically` | Bilingual Coach Message & BCT Rationale/Limits Card | Live (with verified local fallback) |
| Bilota Companion Engine (`gemini-2.5-flash` / Local BCT) | Interactive conversational micro-counseling with zero-shame reframing for Abu Dhabi dilemmas | `src/core/elite_features.py:chat_with_bilota` | Guardian Tab Chat Dialog & Audio Purr Cue | Live (with deterministic Khaleeji BCT mapping fallback) |
| Bio-Climatic Sensor Fusion | Micro-environment telemetry fusion with NCEMA heat directives & sanctuary routing | `src/core/elite_features.py:get_climate_intelligence` | Bio-Climatic Weather Radar & Indoor Sanctuary Modal | Deterministic live simulation |
| Sovereign ZKP Enclave | Hardware-isolated zk-SNARK proof verification under UAE Federal Law No. 2 of 2019 | `src/core/elite_features.py:generate_zkp_proof` | Zero-Knowledge Sovereign Enclave Dashboard | On-Device Cryptographic Enclave Simulation |
| Malaffi Biomarker Engine | Biological Health Age delta & 10-Yr ASCVD risk reduction calculation from IFHAS metrics | `src/core/elite_features.py:calculate_malaffi_age` | IFHAS Biomarker Health Age Clock | ADPHC / UKPDS validated risk equations |
