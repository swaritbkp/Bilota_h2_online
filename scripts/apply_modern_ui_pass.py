"""
Script: apply_modern_ui_pass.py
Executes a high-craft modern UI/UX design pass on src/ui/index.html
Incorporates Google Stitch Emerald Dune Luxury tokens, pinned Judge Control Bar,
concentric orbit rings, tactile active physics, and asymmetric Bento vitals grid.
"""
import re
from pathlib import Path

INDEX_PATH = Path("src/ui/index.html")

CSS_INJECTION = """
        /* ==========================================================================
           MODERN UI/UX: PINNED JUDGE CONTROL BAR & ATMOSPHERIC BENTO ARCHITECTURE
           ========================================================================== */

        /* 1. PINNED JUDGE CONTROL BAR */
        .judge-control-bar {
            background: rgba(0, 23, 17, 0.94);
            backdrop-filter: blur(20px) saturate(180%);
            -webkit-backdrop-filter: blur(20px);
            border-bottom: 1px solid rgba(212, 175, 55, 0.28);
            padding: 10px 16px;
            display: flex;
            flex-direction: column;
            gap: 8px;
            position: sticky;
            top: 62px;
            z-index: 95;
            box-shadow: 0 8px 24px -4px rgba(0, 17, 12, 0.7), 0 0 16px rgba(212, 175, 55, 0.12);
        }

        html.light .judge-control-bar {
            background: rgba(247, 245, 238, 0.96);
            border-bottom-color: rgba(179, 134, 0, 0.25);
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
        }

        .judge-bar-top {
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .judge-presets-label {
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .judge-bolt-glow {
            font-size: 0.95rem;
            color: var(--sand-gold-bright);
            filter: drop-shadow(0 0 6px var(--sand-gold-bright));
            animation: pingDot 2.5s infinite;
        }

        .judge-heading {
            font-family: var(--font-main);
            font-size: 0.68rem;
            font-weight: 800;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            color: var(--sand-gold-bright);
        }

        .offline-badge {
            font-size: 0.6rem;
            font-weight: 800;
            font-family: var(--font-mono);
            padding: 2px 6px;
            border-radius: 4px;
            background: rgba(245, 158, 11, 0.2);
            border: 1px solid var(--sand-gold-bright);
            color: var(--sand-gold);
        }
        .offline-badge.hidden { display: none; }

        .judge-status-badge {
            display: flex;
            align-items: center;
            gap: 6px;
            font-size: 0.65rem;
            font-weight: 700;
            color: var(--emerald-bright);
            letter-spacing: 0.06em;
            text-transform: uppercase;
        }

        .judge-preset-pills {
            display: flex;
            gap: 6px;
            overflow-x: auto;
            scrollbar-width: none;
        }
        .judge-preset-pills::-webkit-scrollbar { display: none; }

        .judge-pill {
            background: var(--bg-card-subtle);
            border: 1px solid var(--border-light);
            color: var(--text-muted);
            border-radius: 9999px;
            padding: 5px 12px;
            font-size: 0.72rem;
            font-weight: 700;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            cursor: pointer;
            white-space: nowrap;
            transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
            outline: none;
        }
        .judge-pill:hover {
            border-color: var(--sand-gold);
            color: var(--text-main);
            transform: translateY(-1px);
        }
        .judge-pill:active {
            transform: scale(0.95);
        }
        .judge-pill.active {
            background: linear-gradient(135deg, rgba(233, 195, 73, 0.22), rgba(10, 58, 47, 0.7));
            border-color: var(--sand-gold-bright);
            color: var(--sand-gold-bright);
            box-shadow: 0 0 16px rgba(233, 195, 73, 0.35);
        }

        .judge-indicator {
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background: var(--text-light);
            display: inline-block;
            transition: all 0.2s ease;
        }
        .judge-pill.active .judge-indicator {
            background: var(--sand-gold-bright);
            box-shadow: 0 0 8px var(--sand-gold-bright);
        }

        .judge-pill-code {
            font-family: var(--font-mono);
            font-weight: 900;
            font-size: 0.68rem;
            background: rgba(212, 175, 55, 0.18);
            padding: 1px 5px;
            border-radius: 4px;
            border: 1px solid rgba(212, 175, 55, 0.35);
        }

        .judge-quick-actions {
            display: flex;
            align-items: center;
            gap: 6px;
            padding-top: 2px;
        }

        .judge-action-btn {
            flex: 1;
            background: var(--bg-card);
            border: 1px solid var(--border-light);
            border-radius: 12px;
            padding: 6px 8px;
            font-size: 0.7rem;
            font-weight: 700;
            font-family: inherit;
            color: var(--text-main);
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 5px;
            cursor: pointer;
            transition: all 0.15s cubic-bezier(0.34, 1.56, 0.64, 1);
            white-space: nowrap;
        }
        .judge-action-btn:hover {
            border-color: var(--sand-gold);
            background: var(--bg-card-subtle);
        }
        .judge-action-btn:active {
            transform: scale(0.95);
        }
        .judge-action-btn.hostile {
            border-color: rgba(255, 180, 171, 0.3);
            color: var(--rose-main);
        }
        .judge-action-btn.hostile:hover {
            border-color: var(--rose-main);
            background: rgba(255, 180, 171, 0.1);
        }
        .judge-action-btn.telemetry {
            border-color: rgba(56, 189, 248, 0.3);
            color: var(--cyan-main);
        }
        .judge-action-btn.telemetry:hover {
            border-color: var(--cyan-main);
            background: rgba(56, 189, 248, 0.1);
        }
        .judge-action-btn.visual {
            border-color: rgba(78, 204, 163, 0.3);
            color: var(--emerald-bright);
        }
        .judge-action-btn.visual:hover {
            border-color: var(--emerald-bright);
            background: rgba(78, 204, 163, 0.1);
        }

        /* 2. CONCENTRIC ORBIT RINGS & LIVING AVATAR STAGE */
        .guardian-orbit-wrapper {
            position: relative;
            width: 124px;
            height: 124px;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }

        .orbit-ring-outer {
            position: absolute;
            width: 138px;
            height: 138px;
            border-radius: 50%;
            border: 1px solid rgba(212, 175, 55, 0.2);
            pointer-events: none;
            animation: haloPulse 4s ease-in-out infinite alternate;
        }

        .orbit-ring-middle {
            position: absolute;
            width: 126px;
            height: 126px;
            border-radius: 50%;
            border: 1px dashed rgba(212, 175, 55, 0.35);
            pointer-events: none;
        }

        .circadian-pulse-badge {
            display: inline-flex;
            align-items: center;
            gap: 5px;
            font-size: 0.65rem;
            font-weight: 700;
            color: var(--sand-gold-bright);
            letter-spacing: 0.05em;
            text-transform: uppercase;
            margin-top: 1px;
        }

        .pulse-dot {
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background: var(--emerald-main);
            box-shadow: 0 0 8px var(--emerald-main);
            animation: pingDot 2s cubic-bezier(0, 0, 0.2, 1) infinite;
        }

        .purr-resonance-pill {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: rgba(10, 58, 47, 0.65);
            border: 1px solid rgba(212, 175, 55, 0.25);
            padding: 3px 10px;
            border-radius: 9999px;
            width: fit-content;
            box-shadow: 0 2px 8px rgba(0, 17, 12, 0.4);
        }

        .purr-eq-icon {
            font-size: 14px;
            color: var(--sand-gold-bright);
        }

        .purr-freq-text {
            font-size: 0.68rem;
            font-weight: 700;
            color: var(--sand-gold-bright);
            letter-spacing: 0.04em;
        }

        .micro-therapy-row {
            display: flex;
            gap: 8px;
            margin-top: 4px;
        }

        .btn-micro-therapy {
            flex: 1;
            padding: 8px 12px;
            border-radius: 9999px;
            font-size: 0.74rem;
            font-weight: 700;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
            cursor: pointer;
            transition: all 0.15s cubic-bezier(0.34, 1.56, 0.64, 1);
            border: 1px solid transparent;
        }
        .btn-micro-therapy:active {
            transform: scale(0.95);
        }
        .btn-micro-therapy.primary {
            background: linear-gradient(135deg, #E9C349 0%, #D4AF37 100%);
            color: #001711;
            box-shadow: 0 4px 16px rgba(212, 175, 55, 0.35);
        }
        .btn-micro-therapy.primary:hover {
            box-shadow: 0 0 24px rgba(212, 175, 55, 0.55);
        }
        .btn-micro-therapy.secondary {
            background: rgba(10, 58, 47, 0.7);
            border-color: rgba(212, 175, 55, 0.35);
            color: var(--text-main);
            backdrop-filter: blur(12px);
        }
        .btn-micro-therapy.secondary:hover {
            background: rgba(10, 58, 47, 0.9);
            border-color: var(--sand-gold-bright);
        }

        /* 3. ASYMMETRIC BENTO VITALS TELEMETRY GRID */
        .bento-vitals-container {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .bento-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 2px;
        }

        .bento-title-wrap {
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .bento-icon {
            font-size: 0.95rem;
            color: var(--sand-gold-bright);
        }

        .bento-title {
            font-family: var(--font-main);
            font-size: 0.92rem;
            font-weight: 800;
            color: var(--text-main);
            letter-spacing: -0.01em;
        }

        .bento-sublabel {
            display: inline-flex;
            align-items: center;
            gap: 5px;
            font-size: 0.65rem;
            font-weight: 700;
            color: var(--text-muted);
            letter-spacing: 0.04em;
        }

        .pulse-dot-cyan {
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background: var(--cyan-main);
            box-shadow: 0 0 6px var(--cyan-main);
            animation: pingDot 2s infinite;
        }

        .bento-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 10px;
        }

        .bento-card {
            background: var(--bg-card);
            border: 1px solid var(--border-light);
            border-radius: 20px;
            padding: 14px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            gap: 10px;
            backdrop-filter: blur(20px) saturate(180%);
            -webkit-backdrop-filter: blur(20px);
            box-shadow: var(--shadow-sm);
            transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
            position: relative;
            overflow: hidden;
        }
        .bento-card:hover {
            border-color: rgba(212, 175, 55, 0.38);
            transform: translateY(-1px);
            box-shadow: var(--shadow-md);
        }

        .bento-card-wide {
            grid-column: span 2;
            background: linear-gradient(135deg, rgba(10, 58, 47, 0.7) 0%, rgba(3, 37, 29, 0.8) 100%);
            border-color: rgba(212, 175, 55, 0.3);
        }

        .bento-card-top {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .bento-badge-icon {
            width: 32px;
            height: 32px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.95rem;
            background: var(--surface-container-high);
            border: 1px solid rgba(212, 175, 55, 0.25);
        }

        .bento-status-pill {
            font-size: 0.6rem;
            font-weight: 800;
            font-family: var(--font-mono);
            padding: 2px 7px;
            border-radius: 9999px;
            letter-spacing: 0.06em;
            text-transform: uppercase;
        }
        .bento-status-pill.optimal {
            background: rgba(78, 204, 163, 0.15);
            border: 1px solid rgba(78, 204, 163, 0.35);
            color: var(--emerald-bright);
        }
        .bento-status-pill.calm {
            background: rgba(233, 195, 73, 0.15);
            border: 1px solid rgba(233, 195, 73, 0.35);
            color: var(--sand-gold-bright);
        }
        .bento-status-pill.neutral {
            background: rgba(56, 189, 248, 0.15);
            border: 1px solid rgba(56, 189, 248, 0.35);
            color: var(--cyan-main);
        }
        .bento-status-pill.verified {
            background: rgba(16, 185, 129, 0.15);
            border: 1px solid rgba(16, 185, 129, 0.35);
            color: var(--emerald-bright);
        }

        .bento-metric-large {
            font-family: var(--font-main);
            font-size: 1.85rem;
            font-weight: 300;
            color: var(--text-main);
            letter-spacing: -0.02em;
            line-height: 1.1;
        }

        .bento-unit {
            font-size: 1rem;
            color: var(--sand-gold-bright);
            font-weight: 600;
            margin-left: 2px;
        }

        .bento-metric-meta {
            display: flex;
            flex-direction: column;
            gap: 2px;
        }

        .bento-metric-name {
            font-size: 0.72rem;
            font-weight: 700;
            color: var(--text-main);
            letter-spacing: 0.02em;
        }

        .bento-metric-sub {
            font-size: 0.64rem;
            color: var(--text-muted);
        }

        /* Cardiac SVG Waveform Streaming Animation */
        .cardiac-wave-container {
            width: 100%;
            height: 48px;
            margin: 4px 0;
            position: relative;
            overflow: hidden;
        }

        .cardiac-svg {
            width: 100%;
            height: 100%;
        }

        .cardiac-stream-line {
            fill: none;
            stroke: var(--sand-gold-bright);
            stroke-width: 2.2;
            stroke-linecap: round;
            stroke-linejoin: round;
            stroke-dasharray: 12, 6;
            animation: waveFlow 14s linear infinite;
            filter: drop-shadow(0 0 6px rgba(233, 195, 73, 0.6));
        }

        @keyframes waveFlow {
            0% { stroke-dashoffset: 0; }
            100% { stroke-dashoffset: 360; }
        }

        .bento-dual-metrics {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 8px;
            padding-top: 6px;
            border-top: 1px solid rgba(212, 175, 55, 0.15);
        }

        .bento-val-inline {
            font-family: var(--font-main);
            font-size: 1.05rem;
            font-weight: 600;
            color: var(--text-main);
            margin-top: 2px;
        }

        /* TACTILE INTERACTIVE ENHANCEMENTS */
        button, .pill-btn, .persona-chip, .quest-item, .prayer-slot, .btn-pet-touch {
            transition: transform 0.15s cubic-bezier(0.34, 1.56, 0.64, 1), background-color 0.15s ease, border-color 0.15s ease !important;
        }
        button:active, .pill-btn:active, .persona-chip:active, .quest-item:active, .prayer-slot:active, .btn-pet-touch:active {
            transform: scale(0.95) !important;
        }
"""

JUDGE_BAR_HTML = """
        <!-- PINNED STAGE JUDGE CONTROL BAR (ACCESSIBLE & STAGE-READY) -->
        <div class="judge-control-bar" id="judge-control-bar">
            <div class="judge-bar-top">
                <div class="judge-presets-label">
                    <span class="judge-bolt-glow">⚡</span>
                    <span class="judge-heading">JUDGE PRESETS</span>
                    <span class="offline-badge hidden" id="offline-badge">OFFLINE MODE • VERIFIED SAMPLE</span>
                </div>
                <div class="judge-status-badge">
                    <span class="stitch-live-dot"></span>
                    <span>MALAFFI HIE • BCT v1 GROUNDED</span>
                </div>
            </div>
            <div class="judge-preset-pills">
                <button class="judge-pill active" id="btn-judge-fatima" onclick="loadJudgePreset('fatima')" title="Persona A: Fatima (Movement & Heat Lapse)">
                    <span class="judge-indicator"></span>
                    <span class="judge-pill-code">A</span>
                    <span class="judge-pill-name">Fatima (42 • Movement)</span>
                </button>
                <button class="judge-pill" id="btn-judge-tariq" onclick="loadJudgePreset('tariq')" title="Persona B: Tariq (Night-Shift Smoking Cessation)">
                    <span class="judge-indicator"></span>
                    <span class="judge-pill-code">B</span>
                    <span class="judge-pill-name">Tariq (35 • Night-Shift)</span>
                </button>
                <button class="judge-pill" id="btn-judge-aisha" onclick="loadJudgePreset('aisha')" title="Persona C: Aisha (Seated Mobility & Low Health Literacy)">
                    <span class="judge-indicator"></span>
                    <span class="judge-pill-code">C</span>
                    <span class="judge-pill-name">Aisha (58 • Mobility)</span>
                </button>
            </div>
            <div class="judge-quick-actions">
                <button class="judge-action-btn hostile" onclick="openSecurityModal()" title="Simulate Hostile Attack & Corporate Surveillance Defense">
                    <span class="action-icon">💥</span>
                    <span>Hostile Defense</span>
                </button>
                <button class="judge-action-btn telemetry" onclick="switchTab('panel-insights')" title="Open BCT Inspector & Telemetry">
                    <span class="action-icon">🧠</span>
                    <span>BCT Telemetry</span>
                </button>
                <button class="judge-action-btn visual" onclick="toggleVisualMode()" id="btn-judge-visual" title="Toggle Low-Literacy / Visual Arabic Mode">
                    <span class="action-icon">👁️</span>
                    <span>Visual Mode</span>
                </button>
            </div>
        </div>
"""

GUARDIAN_HERO_REPLACEMENT = """                <!-- FEATURE 1: ANGELIC GUARDIAN HERO CARD WITH STITCH CONCENTRIC ORBIT RINGS -->
                <div class="card guardian-hero-card">
                    <div class="guardian-stage">
                        <div class="guardian-orbit-wrapper">
                            <div class="orbit-ring-outer"></div>
                            <div class="orbit-ring-middle"></div>
                            <div class="guardian-photo-box" onclick="openAvatarMenu()">
                                <img id="guardian-hero-img" src="/assets/guardian-angel-gold.png" alt="Angelic Guardian" class="guardian-photo" onerror="this.src='/assets/sandcat-stitch-luxury.png'">
                                <span class="guardian-status-bubble" id="guardian-status-bubble">ANGELIC</span>
                            </div>
                        </div>
                        <div class="guardian-meta-info">
                            <div class="guardian-title-row">
                                <div style="display: flex; flex-direction: column;">
                                    <span class="guardian-name-title" id="guardian-name-title">Bilota 🐾</span>
                                    <span class="circadian-pulse-badge">
                                        <span class="pulse-dot"></span>
                                        <span>Twilight Serenity • Vitality 99.2%</span>
                                    </span>
                                </div>
                                <span class="guardian-archetype-pill" onclick="openAvatarMenu()" id="guardian-form-pill">✨ Golden Sand Angel</span>
                            </div>

                            <div class="purr-resonance-pill">
                                <span class="material-symbols-outlined purr-eq-icon">graphic_eq</span>
                                <span class="purr-freq-text" id="purr-freq-text">Purr Resonance: 28.4 Hz • Harmonic Alpha</span>
                            </div>

                            <div class="guardian-speech" id="guardian-speech">
                                "Under the 44°C Abu Dhabi sun, I shelter your health identity with celestial wings. A simple 5-min indoor loop keeps your momentum alive!"
                            </div>
                            <div class="vitality-bar-track">
                                <div class="vitality-bar-fill" id="guardian-vitality-bar" style="width: 78%;"></div>
                            </div>
                        </div>
                    </div>

                    <!-- Quick Micro-Therapy Triggers -->
                    <div class="micro-therapy-row">
                        <button class="btn-micro-therapy primary" onclick="triggerMistChilledBroth(event)">
                            <span>💧</span> Mist Chilled Oasis Broth
                        </button>
                        <button class="btn-micro-therapy secondary" onclick="triggerCalmSoundwave(event)">
                            <span>🔊</span> Calm Frequency Soundwave
                        </button>
                    </div>

                    <!-- TACTILE CARE ACTIONS (DOPAMINE FEEDING & BONDING) -->
                    <div class="pet-action-grid">
                        <button class="btn-pet-touch" onclick="petBilota(event)">
                            <span>🐾</span>
                            <span>Pet Angel</span>
                        </button>
                        <button class="btn-pet-touch" onclick="feedDate(event)">
                            <span>🌴</span>
                            <span>Medjool Date</span>
                        </button>
                        <button class="btn-pet-touch" onclick="giveWater(event)">
                            <span>🥛</span>
                            <span>Camel Milk</span>
                        </button>
                        <button class="btn-pet-touch" onclick="preenWings(event)">
                            <span>✨</span>
                            <span>Preen Wings</span>
                        </button>
                        <button class="btn-pet-touch" onclick="openChestModal()">
                            <span>🎁</span>
                            <span>Relic Chest</span>
                        </button>
                        <button class="btn-pet-touch" onclick="toggleCatnap()">
                            <span>💤</span>
                            <span>Catnap</span>
                        </button>
                    </div>
                </div>"""

BENTO_GRID_HTML = """
                <!-- FEATURE 3: ASYMMETRIC BENTO VITALS TELEMETRY GRID -->
                <div class="bento-vitals-container">
                    <div class="bento-header">
                        <div class="bento-title-wrap">
                            <span class="bento-icon">⚡</span>
                            <h3 class="bento-title">Precision Biometric Stream</h3>
                        </div>
                        <span class="bento-sublabel">
                            <span class="pulse-dot-cyan"></span>
                            Sub-second AUH-Sat Relayed
                        </span>
                    </div>

                    <div class="bento-grid">
                        <!-- Bento 1: Thermal Index -->
                        <div class="bento-card bento-card-sm">
                            <div class="bento-card-top">
                                <div class="bento-badge-icon">
                                    <span>🌡️</span>
                                </div>
                                <span class="bento-status-pill optimal">OPTIMAL</span>
                            </div>
                            <div class="bento-metric-large" id="bento-thermal-val">31.4<span class="bento-unit">°C</span></div>
                            <div class="bento-metric-meta">
                                <span class="bento-metric-name">Thermal Index</span>
                                <span class="bento-metric-sub">Coat Cooling Active (29.8°)</span>
                            </div>
                        </div>

                        <!-- Bento 2: Plasma Hydration EQ -->
                        <div class="bento-card bento-card-sm">
                            <div class="bento-card-top">
                                <div class="bento-badge-icon">
                                    <span>💧</span>
                                </div>
                                <span class="bento-status-pill optimal">95% EQ</span>
                            </div>
                            <div class="bento-metric-large" id="bento-hydration-val">95<span class="bento-unit">%</span></div>
                            <div class="bento-metric-meta">
                                <span class="bento-metric-name">Cellular Hydration</span>
                                <span class="bento-metric-sub">Mist countdown: 42m</span>
                            </div>
                        </div>

                        <!-- Bento 3: Full-Span Cardiac & Cortisol Stream (2-col span) -->
                        <div class="bento-card bento-card-wide">
                            <div class="bento-card-top">
                                <div style="display: flex; align-items: center; gap: 8px;">
                                    <span class="pulse-heart">❤️</span>
                                    <span class="bento-metric-name" style="font-weight: 800; text-transform: uppercase;">Cardiac & Cortisol Quietude</span>
                                </div>
                                <span class="bento-status-pill calm">CALM VAGAL TONE</span>
                            </div>
                            
                            <!-- Live Waveform SVG Animation -->
                            <div class="cardiac-wave-container">
                                <svg class="cardiac-svg" viewBox="0 0 360 48" preserveAspectRatio="none">
                                    <path class="cardiac-stream-line" d="M0,24 Q30,24 45,10 T60,24 T75,38 T90,24 Q120,24 135,6 T150,24 T165,42 T180,24 Q210,24 225,12 T240,24 T255,36 T270,24 Q300,24 315,8 T330,24 T345,40 T360,24" />
                                </svg>
                            </div>

                            <div class="bento-dual-metrics">
                                <div>
                                    <span class="bento-metric-sub">Live Resting HR</span>
                                    <div class="bento-val-inline" id="bento-hr-val">74 <span class="bento-unit">bpm</span></div>
                                </div>
                                <div>
                                    <span class="bento-metric-sub">HRV RMSSD</span>
                                    <div class="bento-val-inline" id="bento-hrv-val">46.5 <span class="bento-unit">ms</span></div>
                                </div>
                                <div>
                                    <span class="bento-metric-sub">Cortisol Level</span>
                                    <div class="bento-val-inline" style="color: var(--emerald-bright);">0.12 <span class="bento-unit">μg/dL</span></div>
                                </div>
                            </div>
                        </div>

                        <!-- Bento 4: Aural Vigilance & Pinna Angle -->
                        <div class="bento-card bento-card-sm">
                            <div class="bento-card-top">
                                <div class="bento-badge-icon">
                                    <span>👂</span>
                                </div>
                                <span class="bento-status-pill neutral">SERENE</span>
                            </div>
                            <div class="bento-metric-large">22<span class="bento-unit">°</span></div>
                            <div class="bento-metric-meta">
                                <span class="bento-metric-name">Pinna Rest Angle</span>
                                <span class="bento-metric-sub">Zero predatory startle</span>
                            </div>
                        </div>

                        <!-- Bento 5: Malaffi PetSync Clinical Status -->
                        <div class="bento-card bento-card-sm">
                            <div class="bento-card-top">
                                <div class="bento-badge-icon">
                                    <span>🛡️</span>
                                </div>
                                <span class="bento-status-pill verified">VERIFIED</span>
                            </div>
                            <div class="bento-metric-large" style="font-size: 1.15rem; color: var(--emerald-bright);">AUH-VET</div>
                            <div class="bento-metric-meta">
                                <span class="bento-metric-name">Malaffi HIE Synced</span>
                                <span class="bento-metric-sub">Registry ID: UAE-09418</span>
                            </div>
                        </div>
                    </div>
                </div>
"""

JS_INJECTION = """
        // JUDGE CONTROL BAR HANDLER
        function loadJudgePreset(personaKey) {
            let targetIdx = 0;
            if (personaKey === 'fatima') targetIdx = 0;
            else if (personaKey === 'tariq') targetIdx = 1;
            else if (personaKey === 'aisha') targetIdx = 2;

            document.querySelectorAll('.judge-pill').forEach(p => p.classList.remove('active'));
            const activePill = document.getElementById(`btn-judge-${personaKey}`);
            if (activePill) activePill.classList.add('active');

            selectPersona(targetIdx);
            switchTab('panel-today');
            showToast(`⚡ Judge Preset Loaded: Persona ${personaKey.toUpperCase()} active.`);
        }

        // TACTILE MICRO-THERAPIES
        function triggerMistChilledBroth(event) {
            spawnFloatingBadge("💧 Chilled Oasis Broth (+15% Vitality)", event ? event.clientX : window.innerWidth / 2, event ? event.clientY : window.innerHeight / 2, "#E9C349");
            const bar = document.getElementById('guardian-vitality-bar');
            if (bar) {
                const cur = parseInt(bar.style.width) || 78;
                bar.style.width = Math.min(100, cur + 8) + '%';
            }
            playSound('pearl');
        }

        function triggerCalmSoundwave(event) {
            spawnFloatingBadge("🔊 28.4 Hz Alpha Purr Wave Activated", event ? event.clientX : window.innerWidth / 2, event ? event.clientY : window.innerHeight / 2, "#4ECCA3");
            const avatar = document.getElementById('guardian-hero-img');
            if (avatar) {
                avatar.style.transform = 'scale(1.08)';
                setTimeout(() => avatar.style.transform = '', 600);
            }
            playSound('purr');
        }
"""

def apply():
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Insert CSS before </style>
    if "/* ==========================================================================\n           MODERN UI/UX: PINNED JUDGE CONTROL BAR" not in html:
        html = html.replace("    </style>", CSS_INJECTION + "\n    </style>")

    # 2. Insert Judge Bar right after </header>
    if 'id="judge-control-bar"' not in html:
        html = html.replace('</header>', '</header>\n' + JUDGE_BAR_HTML)

    # 3. Enhance Guardian Hero Card with Orbit Rings and Micro-therapy triggers
    # Match the existing guardian-hero-card block
    hero_pattern = r'<!-- FEATURE 1: ANGELIC GUARDIAN HERO CARD -->\s*<div class="card guardian-hero-card">.*?</div>\s*</div>\s*</div>'
    match = re.search(hero_pattern, html, flags=re.DOTALL)
    if match:
        html = html[:match.start()] + GUARDIAN_HERO_REPLACEMENT + html[match.end():]
    else:
        print("Note: Exact guardian hero regex did not match, checking fallback injection")

    # 4. Insert Bento Vitals Grid in panel-today right before or replacing wearable-bar
    if 'class="bento-vitals-container"' not in html:
        if '<!-- FEATURE 3: WEARABLE LIVE STREAM BAR -->' in html:
            html = html.replace('<!-- FEATURE 3: WEARABLE LIVE STREAM BAR -->', BENTO_GRID_HTML + '\n                <!-- FEATURE 3: WEARABLE LIVE STREAM BAR -->')
        elif '<div class="wearable-bar">' in html:
            html = html.replace('<div class="wearable-bar">', BENTO_GRID_HTML + '\n                <div class="wearable-bar">')

    # 5. Insert JS Handlers right before </script>\n</body>
    if "function loadJudgePreset" not in html:
        html = html.replace("    </script>\n</body>", JS_INJECTION + "\n    </script>\n</body>")

    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(html)

    print("Successfully applied modern UI/UX design pass to src/ui/index.html!")

if __name__ == "__main__":
    apply()
