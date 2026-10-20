# Submission Pack (Official 6 Requirements)
**Abu Dhabi Adaptive Health Behavior Challenge | Production Package**

---

### 1. GitHub Repository Link
* **URL**: `https://github.com/swaritbkp/Bilota_h2_online`
* **Status**: Configured with remote tracking and `demo-freeze` git tag.

---

### 2. Repository Visibility & Public Access
* **Access Level**: **PUBLIC**
* **Verification**: Verified clean clone in incognito environment; secret scan verified zero API keys or credentials committed.

---

### 3. Deployed Project Link
* **Production Dashboard URL**: `http://127.0.0.1:8080`
* **Health Endpoint**: `http://127.0.0.1:8080/api/health`
* **Inference Endpoint**: `http://127.0.0.1:8080/api/analyze`
* **Features**: Pinned Judge Control Bar, 13 Real Emirati Personas, 20 Feline Companions, Multi-Generational Family Oasis, Sovereign Family QR Tagging & Care Circles, Bedouin Relic Chest, Arabic RTL mode, Low-Literacy Visual Mode, and BCT Inspector Drawer.

---

### 4. Brief Project Description (135 Words)
**Bilota (بيلوتا / قطوة)** is a feline-guided Adaptive Health Behavior Loop Engine designed for Abu Dhabi to bridge screenings (IFHAS), Sahatna journeys, Health Age scores, and wearable biometrics into sustained daily habits across movement, nutrition, sleep, smoking cessation, and recovery. Traditional wellness apps fail when life intervenes—punishing lapses with "streak resets" that trigger drop-out. Bilota replaces streaks with a feline **Momentum Bank** and **Graded Task Downshifting (Michie BCT 8.7)**. When wearable drop-off or environmental barriers arise (44°C summer heat, rotating shifts, or osteoarthritic joint pain), Bilota diagnoses the friction and scales habits down to 2-minute achievable micro-actions in Arabic or English. Every intervention displays its clinical BCT rationale and explicit limits, enforces a cryptographic Anti-Punitive Firewall (UAE Federal Law No. 2 of 2019), and measures 90-day persistence, recovery speed, and Health Age rejuvenation.

---

### 5. Gen AI Services Used & Where

| Service / Model | Primary Purpose | Exact Call Site (`file:function`) | UI Visibility |
|---|---|---|---|
| **Google ADK (`google-adk`)** | Multi-tool behavioral loop orchestration & state routing | `src/agent/orchestrator.py:run_khatwa_agent` | Adaptive Plan Card & Telemetry Drawer |
| **Gemini 2.5 Flash (`gemini-2.5-flash`)** | Low-latency barrier classification & BCT micro-action synthesis | `src/agent/tools.py:craft_graded_micro_action` | Instant Micro-Action Plan & L2 Shield |
| **Gemini 2.5 Pro (`gemini-2.5-pro`)** | Culturally nuanced bilingual (AR/EN) non-blaming lapse reframing | `src/agent/tools.py:reframe_lapse_empathetically` | Bilingual Coach Message & Rationale Card |

*Full register maintained in [`docs/GENAI-SERVICES.md`](file:///c:/Users/S/OneDrive/Desktop/octhackathon/docs/GENAI-SERVICES.md).*

---

### 6. Project Demo Video Link & Timed Script
* **Video Script Specification**: [`docs/DEMO-VIDEO.md`](file:///c:/Users/S/OneDrive/Desktop/octhackathon/docs/DEMO-VIDEO.md)
* **Timed Duration**: Exactly 120 Seconds (2:00) covering hook, Fatima 44°C heat lapse, Tariq night-shift slip, Aisha seated low-literacy mode, sovereign HR attack block, Family Majlis Oasis, and 100% measured benchmark telemetry.
