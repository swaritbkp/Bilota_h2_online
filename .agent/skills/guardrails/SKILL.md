---
name: guardrails
description: Implements L1-L3 guardrails including injection defense, corporate/insurer surveillance blocks, clinical acute triage, and zero-shame scrubbing.
---
# Skill: Guardrails Shield
Implement `src/core/guardrails.py` covering Unicode normalization, injection regexes, employer/insurer punitive export blocking, acute symptom redirection (998/999), canary leak checks (`PW-CANARY-7f3a91`), and blaming-language removal.
