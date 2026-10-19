---
description: Produces Abu Dhabi production architecture (Sahatna, Malaffi FHIR, ADPHC), governance under UAE Federal Law No. 2 of 2019, and cost/latency optimisation.
---

# Workflow: `/scale`

When triggered:
1. Generate `docs/ARCHITECTURE.md` with:
   - Mermaid system architecture diagram showing integration with **Sahatna**, **Malaffi HIE (HL7 FHIR R4 Observation/CarePlan resources)**, **IFHAS Screening**, and **Wearable APIs (HealthKit/Health Connect)**.
   - **Scale**: Stateless Cloud Run containers in UAE region (me-central1/me-central2), deterministic caching for BCT lookups, async event queues for passive wearable drop-off detection.
   - **Govern**: Cryptographic separation between personal behavioral vaults and aggregate anonymized public-health analytics (UAE Federal Law No. 2 of 2019 compliance); append-only audit log (`logs/audit.jsonl`); human-in-the-loop escalation for clinical red flags.
   - **Optimise**: Gemini 2.5 Flash for real-time barrier sensing & micro-action sizing; Gemini 2.5 Pro reserved for complex multi-barrier empathetic reframing; measured latency and token cost table.
2. Add a 1-slide summary to `docs/SLIDES.md`.
3. Re-run `eval/run_eval.py` to confirm zero regressions. Commit and push `checkpoint: scale` and print the Auto-Pilot Box for `/deploy`.
