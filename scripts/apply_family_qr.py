import sys
from pathlib import Path

INDEX_PATH = Path("src/ui/index.html")

def apply_updates():
    content = INDEX_PATH.read_text(encoding="utf-8")

    # 1. CSS UPDATES
    css_anchor = ".avatar-grid {"
    css_addition = """        /* FAMILY MAJLIS OASIS & QR INTERACTION STYLES */
        .family-card {
            background: var(--bg-card);
            border: 1px solid var(--border-light);
            border-radius: 14px;
            padding: 10px;
            display: flex;
            align-items: center;
            gap: 8px;
            cursor: pointer;
            transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
            position: relative;
        }
        .family-card:hover {
            transform: translateY(-2px);
            border-color: var(--emerald-main);
            box-shadow: 0 6px 16px rgba(16, 185, 129, 0.15);
        }
        .family-card:active {
            transform: scale(0.98);
        }
        .qr-scanner-box {
            position: relative;
            width: 100%;
            height: 200px;
            border-radius: 18px;
            background: #090D16;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            border: 2px dashed #0D9488;
        }
        .qr-laser-line {
            position: absolute;
            left: 5%;
            width: 90%;
            height: 3px;
            background: linear-gradient(90deg, transparent, #10B981, #06B6D4, transparent);
            box-shadow: 0 0 14px #10B981, 0 0 24px #06B6D4;
            animation: qrLaserScan 2s infinite ease-in-out;
        }
        @keyframes qrLaserScan {
            0% { top: 10%; opacity: 0.3; }
            50% { top: 85%; opacity: 1; }
            100% { top: 10%; opacity: 0.3; }
        }
        .qr-svg-wrap {
            width: 220px;
            height: 220px;
            margin: 0 auto;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 20px;
            box-shadow: 0 10px 25px rgba(16, 185, 129, 0.15);
            background: #FFFFFF;
            padding: 6px;
        }

        .avatar-grid {"""
    if ".family-card {" not in content:
        assert css_anchor in content, "css_anchor not found"
        content = content.replace(css_anchor, css_addition, 1)
        print("CSS styles added.")

    # 2. FAMILY OASIS SECTION IN PANEL-SANCTUARY
    old_oasis_start = "<!-- FEATURE: MULTI-GENERATIONAL EMIRATI FAMILY MAJLIS OASIS -->"
    old_oasis_end = "<!-- ONE-TAP FAMILY BLESSING ACTIONS -->"
    assert old_oasis_start in content and old_oasis_end in content, "Oasis section anchors not found"

    new_oasis_section = """<!-- FEATURE: MULTI-GENERATIONAL EMIRATI FAMILY MAJLIS OASIS -->
                <div class="card" style="border: 2px solid #A7F3D0; background: linear-gradient(180deg, #F0FDF4 0%, var(--bg-card) 100%);">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div>
                            <span style="font-size: 1rem; font-weight: 800; color: var(--emerald-main);">🌳 Family Majlis Oasis</span>
                            <span style="font-size: 0.68rem; font-family: var(--font-ar); color: var(--emerald-main); margin-left: 4px;">(الواحة العائلية)</span>
                        </div>
                        <span style="font-size: 0.68rem; font-family: var(--font-mono); font-weight: 800; background: #D1FAE5; color: var(--emerald-main); padding: 2px 8px; border-radius: 6px;">COOPERATIVE CO-PLAY</span>
                    </div>
                    <p style="font-size: 0.76rem; color: var(--text-muted); margin-top: 2px;">
                        Zero toxic leaderboards. 4 generations of the Al-Mansouri family nurturing our shared <strong>Sacred Ghaf Tree</strong>.
                    </p>

                    <!-- DUAL ACTION BUTTONS: SHARE QR & SCAN/TAG -->
                    <div style="display: flex; gap: 8px; margin: 4px 0 6px 0;">
                        <button class="pill-btn active" onclick="openFamilyQrModal('share')" style="flex: 1; justify-content: center; padding: 8px 12px; font-weight: 800; font-size: 0.76rem; background: linear-gradient(135deg, #059669, #0D9488); border: none; color: #FFF; box-shadow: 0 4px 12px rgba(13, 148, 136, 0.25);">
                            📲 Share Oasis QR
                        </button>
                        <button class="pill-btn" onclick="openFamilyQrModal('scan')" style="flex: 1; justify-content: center; padding: 8px 12px; font-weight: 800; font-size: 0.76rem; border-color: var(--sand-gold); color: var(--sand-gold); background: var(--bg-card);">
                            📷 Scan &amp; Tag Member
                        </button>
                    </div>

                    <!-- SACRED GHAF TREE PROGRESS -->
                    <div style="background: var(--bg-card); border: 1px solid var(--border-light); border-radius: 14px; padding: 12px; display: flex; flex-direction: column; gap: 8px;">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <div style="display: flex; align-items: center; gap: 6px;">
                                <span style="font-size: 1.2rem;">🌸</span>
                                <div>
                                    <div style="font-size: 0.84rem; font-weight: 800;">Sacred Ghaf Tree: Level 4 (Flowering Canopy)</div>
                                    <div style="font-size: 0.68rem; color: var(--text-muted);">Next Bloom: Festive Oasis Illumination at 2,000 drops</div>
                                </div>
                            </div>
                            <span style="font-size: 0.8rem; font-weight: 800; font-family: var(--font-mono); color: var(--emerald-main);" id="ghaf-drops-pct">92%</span>
                        </div>
                        <div class="vitality-bar-track">
                            <div class="vitality-bar-fill" id="ghaf-tree-bar" style="width: 92%; background: linear-gradient(90deg, #10B981, #F59E0B);"></div>
                        </div>
                        <div style="display: flex; justify-content: space-between; font-size: 0.68rem; color: var(--text-muted); font-family: var(--font-mono);">
                            <span id="ghaf-drops-count">1,840 / 2,000 Hydration Drops</span>
                            <span style="color: var(--sand-gold);">✨ Radiant Oasis Bloom</span>
                        </div>
                    </div>

                    <!-- 4 FAMILY GENERATION CARDS WITH TACTILE STACK INSPECTION -->
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 4px;">
                        <span style="font-size: 0.74rem; font-weight: 800; color: var(--text-muted);">Family Care Circle (Tap to View Stack):</span>
                        <span style="font-size: 0.66rem; color: var(--emerald-main); font-weight: 700;">UAE Law 2/2019 Sovereign</span>
                    </div>

                    <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 8px;" id="family-member-grid">
                        <!-- AISHA (GRANDMOTHER) -->
                        <div class="family-card" onclick="openFamilyMemberStack('aisha')">
                            <div style="position: relative;">
                                <img src="/assets/user-aisha.png" alt="Grandmother Aisha" style="width: 44px; height: 44px; border-radius: 10px; object-fit: cover;" onerror="this.src='/assets/user-aisha.jpg'">
                                <img src="/assets/cat-fluffy-white.png" alt="Cat" style="position: absolute; bottom: -4px; right: -4px; width: 20px; height: 20px; border-radius: 6px; border: 1px solid #FFF; object-fit: cover;">
                            </div>
                            <div style="overflow: hidden; flex: 1;">
                                <div style="display: flex; justify-content: space-between; align-items: center;">
                                    <div style="font-size: 0.78rem; font-weight: 800;">Aisha (الجدة)</div>
                                    <span style="font-size: 0.58rem; background: #D1FAE5; color: var(--emerald-main); padding: 1px 4px; border-radius: 4px; font-weight: 800;">21d Grace</span>
                                </div>
                                <div style="font-size: 0.65rem; color: var(--emerald-main); font-weight: 600;">☁️ Fluffy White Angora</div>
                                <div style="font-size: 0.62rem; color: var(--text-muted);">+460 drops • Seated Stretch</div>
                                <div style="font-size: 0.60rem; color: var(--emerald-main); font-weight: 700; margin-top: 2px;">🔍 Tap to View Stack</div>
                            </div>
                        </div>

                        <!-- FATIMA (MOTHER) -->
                        <div class="family-card" onclick="openFamilyMemberStack('fatima')">
                            <div style="position: relative;">
                                <img src="/assets/user-fatima.png" alt="Mother Fatima" style="width: 44px; height: 44px; border-radius: 10px; object-fit: cover;" onerror="this.src='/assets/user-fatima.jpg'">
                                <img src="/assets/cat-fluffy-ginger.png" alt="Cat" style="position: absolute; bottom: -4px; right: -4px; width: 20px; height: 20px; border-radius: 6px; border: 1px solid #FFF; object-fit: cover;">
                            </div>
                            <div style="overflow: hidden; flex: 1;">
                                <div style="display: flex; justify-content: space-between; align-items: center;">
                                    <div style="font-size: 0.78rem; font-weight: 800;">Fatima (الأم)</div>
                                    <span style="font-size: 0.58rem; background: #D1FAE5; color: var(--emerald-main); padding: 1px 4px; border-radius: 4px; font-weight: 800;">18d Loops</span>
                                </div>
                                <div style="font-size: 0.65rem; color: var(--emerald-main); font-weight: 600;">🦁 Marmalade Tabby</div>
                                <div style="font-size: 0.62rem; color: var(--text-muted);">+540 drops • 5-min Indoor Walk</div>
                                <div style="font-size: 0.60rem; color: var(--emerald-main); font-weight: 700; margin-top: 2px;">🔍 Tap to View Stack</div>
                            </div>
                        </div>

                        <!-- TARIQ (FATHER) -->
                        <div class="family-card" onclick="openFamilyMemberStack('tariq')">
                            <div style="position: relative;">
                                <img src="/assets/user-tariq.png" alt="Father Tariq" style="width: 44px; height: 44px; border-radius: 10px; object-fit: cover;" onerror="this.src='/assets/user-tariq.jpg'">
                                <img src="/assets/cat-fluffy-midnight.png" alt="Cat" style="position: absolute; bottom: -4px; right: -4px; width: 20px; height: 20px; border-radius: 6px; border: 1px solid #FFF; object-fit: cover;">
                            </div>
                            <div style="overflow: hidden; flex: 1;">
                                <div style="display: flex; justify-content: space-between; align-items: center;">
                                    <div style="font-size: 0.78rem; font-weight: 800;">Tariq (الوالد)</div>
                                    <span style="font-size: 0.58rem; background: #E0E7FF; color: var(--indigo-main); padding: 1px 4px; border-radius: 4px; font-weight: 800;">12d Shift</span>
                                </div>
                                <div style="font-size: 0.65rem; color: var(--cyan-main); font-weight: 600;">🐾 Midnight Velvet</div>
                                <div style="font-size: 0.62rem; color: var(--text-muted);">+420 drops • 4-7-8 Urge Reset</div>
                                <div style="font-size: 0.60rem; color: var(--emerald-main); font-weight: 700; margin-top: 2px;">🔍 Tap to View Stack</div>
                            </div>
                        </div>

                        <!-- KHALID (SON) -->
                        <div class="family-card" onclick="openFamilyMemberStack('khalid')">
                            <div style="position: relative;">
                                <img src="/assets/user-khalid.png" alt="Son Khalid" style="width: 44px; height: 44px; border-radius: 10px; object-fit: cover;" onerror="this.src='/assets/user-khalid.jpg'">
                                <img src="/assets/cat-fluffy-siamese.png" alt="Cat" style="position: absolute; bottom: -4px; right: -4px; width: 20px; height: 20px; border-radius: 6px; border: 1px solid #FFF; object-fit: cover;">
                            </div>
                            <div style="overflow: hidden; flex: 1;">
                                <div style="display: flex; justify-content: space-between; align-items: center;">
                                    <div style="font-size: 0.78rem; font-weight: 800;">Khalid (الابن)</div>
                                    <span style="font-size: 0.58rem; background: #FEF3C7; color: var(--sand-gold); padding: 1px 4px; border-radius: 4px; font-weight: 800;">26d Vape Reset</span>
                                </div>
                                <div style="font-size: 0.65rem; color: var(--indigo-main); font-weight: 600;">👑 Silky Balinese</div>
                                <div style="font-size: 0.62rem; color: var(--text-muted);">+420 drops • Pushup Craving Delay</div>
                                <div style="font-size: 0.60rem; color: var(--emerald-main); font-weight: 700; margin-top: 2px;">🔍 Tap to View Stack</div>
                            </div>
                        </div>
                    </div>
                    """

    start_idx = content.find(old_oasis_start)
    end_idx = content.find(old_oasis_end)
    content = content[:start_idx] + new_oasis_section + content[end_idx:]
    print("Oasis section updated with QR buttons and interactive cards.")

    # 3. MODALS (family-stack-modal and family-qr-modal)
    modal_anchor = "<!-- MODAL 7: BEDOUIN MYSTERY GHAF RELIC CHEST -->"
    assert modal_anchor in content, "modal_anchor not found"

    new_modals = """    <!-- MODAL 8: FAMILY MEMBER HABIT STACK & HEALTH VITALITY MATRIX -->
    <div class="modal-overlay" id="family-stack-modal">
        <div class="modal-card" style="border-color: #A7F3D0; max-height: 88vh;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span style="font-size: 1.2rem;">🌳</span>
                    <div>
                        <div style="font-weight: 800; font-size: 0.98rem; color: var(--emerald-main);" id="fsm-name">Aisha Al-Mansouri (الجدة عائشة)</div>
                        <div style="font-size: 0.7rem; color: var(--text-muted);" id="fsm-role">Grandmother • Root Nourisher</div>
                    </div>
                </div>
                <button class="pill-btn" onclick="closeFamilyStackModal()">✕</button>
            </div>

            <!-- COMPANION HERO BANNER -->
            <div style="background: var(--bg-card-subtle); border-radius: 16px; padding: 10px 14px; display: flex; align-items: center; gap: 12px; border: 1px solid var(--border-light);">
                <img id="fsm-companion-img" src="/assets/cat-fluffy-white.png" alt="Cat" style="width: 52px; height: 52px; border-radius: 14px; object-fit: cover; border: 2px solid var(--sand-gold);">
                <div>
                    <div style="display: flex; align-items: center; gap: 6px;">
                        <span id="fsm-companion-name" style="font-size: 0.86rem; font-weight: 800;">Fluffy White Angora</span>
                        <span id="fsm-companion-icon">☁️</span>
                    </div>
                    <div id="fsm-companion-aura" style="font-size: 0.7rem; color: var(--emerald-main); font-weight: 600;">Pure Cloud Serenity (سكينة السحاب)</div>
                    <div style="font-size: 0.65rem; color: var(--text-muted); margin-top: 2px;" id="fsm-last-active">Active 12m ago post-Dhuhr</div>
                </div>
            </div>

            <!-- BCT 1.4 HABIT STACK BLOCK -->
            <div style="background: #F0FDF4; border: 1px solid #A7F3D0; border-radius: 16px; padding: 12px; display: flex; flex-direction: column; gap: 6px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-size: 0.72rem; font-weight: 800; color: var(--emerald-main); letter-spacing: 0.5px;">BCT 1.4 DAILY HABIT STACK</span>
                    <span style="font-size: 0.64rem; font-family: var(--font-mono); background: #D1FAE5; color: var(--emerald-main); padding: 2px 6px; border-radius: 4px; font-weight: 800;" id="fsm-bct-code">BCT 8.7 + BCT 1.4</span>
                </div>
                <div style="font-size: 0.82rem; font-weight: 800; color: var(--text-main);" id="fsm-anchor-title">⚓ Post-Dhuhr Prayer (بعد صلاة الظهر)</div>
                <div style="font-size: 0.76rem; color: var(--text-muted); line-height: 1.4;" id="fsm-micro-habit">
                    Seated Knee Mobility & 3-Color Plate Cue
                </div>
                <div style="font-size: 0.68rem; color: var(--emerald-main); font-weight: 600; background: rgba(16, 185, 129, 0.1); padding: 6px 8px; border-radius: 8px;" id="fsm-rationale">
                    🔬 Rationale: Seated mobility eliminates joint pain while daily prayer provides 5 natural anchors.
                </div>
            </div>

            <!-- VITALITY TELEMETRY MATRIX -->
            <div>
                <div style="font-size: 0.74rem; font-weight: 800; margin-bottom: 6px; color: var(--text-muted);">LIVE VITALITY &amp; BIOMETRIC FLOOR:</div>
                <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 8px;">
                    <!-- STEPS FLOOR -->
                    <div style="background: var(--bg-card-subtle); border-radius: 12px; padding: 8px 10px; border: 1px solid var(--border-light);">
                        <div style="font-size: 0.68rem; color: var(--text-muted);">Step Floor (BCT 8.7)</div>
                        <div style="font-size: 0.95rem; font-weight: 900; font-family: var(--font-mono); color: var(--emerald-main);" id="fsm-steps-val">1,820 / 2,000</div>
                        <div style="font-size: 0.62rem; color: var(--emerald-main); font-weight: 700;" id="fsm-steps-badge">Floor Secured 🌿</div>
                    </div>
                    <!-- HYDRATION DROPS -->
                    <div style="background: var(--bg-card-subtle); border-radius: 12px; padding: 8px 10px; border: 1px solid var(--border-light);">
                        <div style="font-size: 0.68rem; color: var(--text-muted);">Hydration Drops</div>
                        <div style="font-size: 0.95rem; font-weight: 900; font-family: var(--font-mono); color: var(--cyan-main);" id="fsm-hydra-val">6 / 8 Cups</div>
                        <div style="font-size: 0.62rem; color: var(--text-muted);">1.5L / 2.0L Target</div>
                    </div>
                    <!-- RHR / HRV -->
                    <div style="background: var(--bg-card-subtle); border-radius: 12px; padding: 8px 10px; border: 1px solid var(--border-light);">
                        <div style="font-size: 0.68rem; color: var(--text-muted);">Cardio Tone (RHR/HRV)</div>
                        <div style="font-size: 0.95rem; font-weight: 900; font-family: var(--font-mono); color: var(--rose-main);" id="fsm-cardio-val">65 bpm • 62ms</div>
                        <div style="font-size: 0.62rem; color: var(--emerald-main); font-weight: 700;">Autonomic Tone Restored</div>
                    </div>
                    <!-- BIOLOGICAL AGE DELTA -->
                    <div style="background: var(--bg-card-subtle); border-radius: 12px; padding: 8px 10px; border: 1px solid var(--border-light);">
                        <div style="font-size: 0.68rem; color: var(--text-muted);">ADPHC Health Age</div>
                        <div style="font-size: 0.95rem; font-weight: 900; font-family: var(--font-mono); color: var(--sand-gold);" id="fsm-age-val">-1.5 Yrs</div>
                        <div style="font-size: 0.62rem; color: var(--text-muted);">IFHAS Biomarker Clock</div>
                    </div>
                </div>
            </div>

            <!-- MOMENTUM BANK & SOVEREIGN ENCLAVE SEAL -->
            <div style="background: var(--bg-card-subtle); border-radius: 12px; padding: 10px; border: 1px solid var(--border-light); display: flex; flex-direction: column; gap: 6px;">
                <div style="display: flex; justify-content: space-between; font-size: 0.72rem; font-weight: 700;">
                    <span>🛡️ 9-Lives Momentum Bank:</span>
                    <span style="color: var(--emerald-main);" id="fsm-momentum-status">21 Days of Grace Preserved</span>
                </div>
                <div style="font-size: 0.66rem; color: var(--emerald-main); display: flex; align-items: center; gap: 4px; font-weight: 600;">
                    <span>🔒</span>
                    <span>UAE Law No. 2/2019 Sovereign Enclave: Zero surveillance data leaked.</span>
                </div>
            </div>

            <!-- ONE-TAP BLESSING TO THIS MEMBER -->
            <div style="display: flex; gap: 8px; margin-top: 4px;">
                <button class="pill-btn active" onclick="sendDirectFamilyBlessing('dua')" style="flex: 1; justify-content: center; padding: 10px; font-weight: 800;">
                    🤲 Send Du'a (+40 ✨)
                </button>
                <button class="pill-btn" onclick="sendDirectFamilyBlessing('gahwa')" style="flex: 1; justify-content: center; padding: 10px; font-weight: 800; border-color: var(--sand-gold); color: var(--sand-gold);">
                    ☕ Send Gahwa (+35 ✨)
                </button>
            </div>
        </div>
    </div>

    <!-- MODAL 9: SOVEREIGN FAMILY QR PAIRING & SCANNER MODAL -->
    <div class="modal-overlay" id="family-qr-modal">
        <div class="modal-card" style="border-color: var(--emerald-main); max-height: 88vh; text-align: center;">
            <div style="display: flex; justify-content: space-between; align-items: center; width: 100%;">
                <div style="display: flex; align-items: center; gap: 6px;">
                    <span style="font-size: 1.2rem;">📲</span>
                    <span style="font-weight: 800; font-size: 1rem; color: var(--emerald-main);">Family Care Circle QR</span>
                </div>
                <button class="pill-btn" onclick="closeFamilyQrModal()">✕</button>
            </div>
            <p style="font-size: 0.76rem; color: var(--text-muted); margin-top: -6px;">
                UAE Federal Law No. 2 of 2019 Cryptographic Handshake. Instant multi-generational pairing with zero login friction.
            </p>

            <!-- TAB SWITCHER: SHARE QR vs SCAN & TAG -->
            <div style="display: flex; gap: 6px; width: 100%; margin-top: 4px;">
                <button class="pill-btn active" id="fqr-tab-share" onclick="switchQrTab('share')" style="flex: 1; justify-content: center; font-size: 0.74rem;">
                    📲 My Sovereign QR
                </button>
                <button class="pill-btn" id="fqr-tab-scan" onclick="switchQrTab('scan')" style="flex: 1; justify-content: center; font-size: 0.74rem;">
                    📷 Scan &amp; Tag Member
                </button>
            </div>

            <!-- TAB VIEW 1: MY SOVEREIGN QR CODE -->
            <div id="fqr-view-share" style="display: flex; flex-direction: column; gap: 10px; width: 100%; align-items: center;">
                <div style="font-size: 0.8rem; font-weight: 800; color: var(--sand-gold);" id="fqr-inviter-label">
                    Fatima Al-Mansouri (عائلة المنصوري)
                </div>

                <div class="qr-svg-wrap" id="fqr-svg-container">
                    <div style="font-size: 0.8rem; color: var(--text-muted);">Generating Sovereign QR...</div>
                </div>

                <!-- SCOPED CONSENT TOGGLES -->
                <div style="background: var(--bg-card-subtle); border-radius: 12px; padding: 10px 12px; width: 100%; text-align: left; font-size: 0.68rem; display: flex; flex-direction: column; gap: 5px; border: 1px solid var(--border-light);">
                    <div style="font-weight: 800; color: var(--emerald-main); font-size: 0.72rem;">Sovereign Consent Scopes (UAE Law 2/2019):</div>
                    <div style="display: flex; justify-content: space-between;">
                        <span>✅ Share Habit Stacks &amp; Ghaf Tree Drops</span>
                        <span style="color: var(--emerald-main); font-weight: 700;">ACTIVE</span>
                    </div>
                    <div style="display: flex; justify-content: space-between;">
                        <span>✅ Emergency Fall &amp; Cardiac 998 Alerts</span>
                        <span style="color: var(--emerald-main); font-weight: 700;">ACTIVE</span>
                    </div>
                    <div style="display: flex; justify-content: space-between; color: var(--text-muted);">
                        <span>🔒 Raw Medical Records &amp; Lapse Logs</span>
                        <span style="color: var(--sand-gold); font-weight: 700;">LOCKED IN ENCLAVE</span>
                    </div>
                </div>

                <div style="display: flex; gap: 8px; width: 100%;">
                    <button class="pill-btn" onclick="copyCareCircleLink()" style="flex: 1; justify-content: center; padding: 10px; font-size: 0.74rem;">
                        📋 Copy Invite Link
                    </button>
                    <button class="pill-btn active" onclick="simulateFamilyScan()" style="flex: 1.2; justify-content: center; padding: 10px; font-size: 0.74rem; background: linear-gradient(135deg, #F59E0B, #D97706); border: none; color: #FFF; box-shadow: 0 4px 12px rgba(245, 158, 11, 0.3);">
                        ⚡ Simulate Khalid's Scan
                    </button>
                </div>
            </div>

            <!-- TAB VIEW 2: SCAN & TAG MEMBER -->
            <div id="fqr-view-scan" style="display: none; flex-direction: column; gap: 10px; width: 100%; align-items: center;">
                <div class="qr-scanner-box">
                    <div class="qr-laser-line"></div>
                    <div style="position: relative; z-index: 2; text-align: center; color: #E2E8F0;">
                        <span style="font-size: 2.5rem; display: block; margin-bottom: 4px;">📷</span>
                        <span style="font-size: 0.78rem; font-weight: 700;">Align Family Member QR in Frame</span>
                        <span style="display: block; font-size: 0.65rem; color: #94A3B8; font-family: var(--font-mono); margin-top: 2px;">CAMERA HUD: READY</span>
                    </div>
                </div>

                <!-- PRESET QUICK TAG BUTTONS FOR HACKATHON DEMO -->
                <div style="width: 100%; text-align: left;">
                    <div style="font-size: 0.72rem; font-weight: 800; margin-bottom: 6px; color: var(--text-muted);">Select Family Member to Tag:</div>
                    <div style="display: flex; flex-direction: column; gap: 6px;">
                        <button class="pill-btn" onclick="tagFamilyMember('hamad')" style="justify-content: space-between; padding: 10px 12px; width: 100%;">
                            <div style="display: flex; align-items: center; gap: 8px;">
                                <img src="/assets/user-hamad.png" style="width: 28px; height: 28px; border-radius: 8px; object-fit: cover;">
                                <div style="text-align: left;">
                                    <div style="font-size: 0.78rem; font-weight: 800;">Uncle Hamad (العم حمد)</div>
                                    <div style="font-size: 0.65rem; color: var(--text-muted);">Offshore Navigator • Zirku Island</div>
                                </div>
                            </div>
                            <span style="font-size: 0.68rem; color: var(--emerald-main); font-weight: 700;">+50 Drops 🌿</span>
                        </button>

                        <button class="pill-btn" onclick="tagFamilyMember('shamsa')" style="justify-content: space-between; padding: 10px 12px; width: 100%;">
                            <div style="display: flex; align-items: center; gap: 8px;">
                                <img src="/assets/user-shamsa.png" style="width: 28px; height: 28px; border-radius: 8px; object-fit: cover;">
                                <div style="text-align: left;">
                                    <div style="font-size: 0.78rem; font-weight: 800;">Great-Grandmother Shamsa (شمسة)</div>
                                    <div style="font-size: 0.65rem; color: var(--text-muted);">Oasis Root • Al Ain Elder</div>
                                </div>
                            </div>
                            <span style="font-size: 0.68rem; color: var(--emerald-main); font-weight: 700;">+50 Drops 🌿</span>
                        </button>
                    </div>
                </div>

                <button class="pill-btn active" onclick="tagFamilyMember('hamad')" style="width: 100%; justify-content: center; padding: 12px; font-weight: 800; background: linear-gradient(135deg, #059669, #0D9488); border: none; color: #FFF; box-shadow: 0 4px 15px rgba(13, 148, 136, 0.35);">
                    📸 Scan &amp; Pair into Majlis Oasis
                </button>
            </div>
        </div>
    </div>

"""
    if "id=\"family-stack-modal\"" not in content:
        content = content.replace(modal_anchor, new_modals + modal_anchor, 1)
        print("Modals added for Family Stack and Family QR.")

    # 4. JAVASCRIPT FUNCTIONS
    js_anchor = "// MULTI-GENERATIONAL FAMILY MAJLIS BLESSINGS"
    assert js_anchor in content, "js_anchor not found"

    new_js = """        // ==========================================
        // SOVEREIGN FAMILY QR & HABIT STACK SUITE
        // ==========================================
        let activeFsmMemberId = "aisha";
        let cachedQrDeepLink = "";

        async function openFamilyMemberStack(memberId) {
            activeFsmMemberId = memberId;
            playSound('tap');
            try {
                const res = await fetch(`/api/family-member-stack?member_id=${memberId}`);
                const data = await res.json();

                document.getElementById('fsm-name').innerText = data.name;
                document.getElementById('fsm-role').innerText = data.role;
                document.getElementById('fsm-companion-img').src = data.companion.image;
                document.getElementById('fsm-companion-name').innerText = data.companion.name;
                document.getElementById('fsm-companion-icon').innerText = data.companion.icon;
                document.getElementById('fsm-companion-aura').innerText = data.companion.aura;

                // Habit Stack
                document.getElementById('fsm-anchor-title').innerText = `⚓ ${data.habit_stack.anchor_name}`;
                document.getElementById('fsm-micro-habit').innerText = data.habit_stack.micro_habit;
                document.getElementById('fsm-bct-code').innerText = data.habit_stack.bct_mapping;
                document.getElementById('fsm-rationale').innerText = `🔬 Rationale: ${data.habit_stack.rationale}`;

                // Vitality
                document.getElementById('fsm-steps-val').innerText = `${data.vitality.steps.current.toLocaleString()} / ${data.vitality.steps.target.toLocaleString()}`;
                document.getElementById('fsm-steps-badge').innerText = data.vitality.steps.badge;
                document.getElementById('fsm-hydra-val').innerText = `${data.vitality.hydration.current_cups} / ${data.vitality.hydration.target_cups} Cups`;
                document.getElementById('fsm-cardio-val').innerText = `${data.vitality.rhr.bpm} bpm • ${data.vitality.hrv.rmssd_ms}ms`;
                document.getElementById('fsm-age-val').innerText = data.vitality.health_age_delta;
                document.getElementById('fsm-momentum-status').innerText = data.vitality.momentum_bank.status;

                document.getElementById('family-stack-modal').classList.add('open');
            } catch (err) {
                console.error("Failed to load stack", err);
                document.getElementById('family-stack-modal').classList.add('open');
            }
        }

        function closeFamilyStackModal() {
            document.getElementById('family-stack-modal').classList.remove('open');
        }

        async function sendDirectFamilyBlessing(type) {
            playSound('blessing');
            try {
                const p = PERSONAS[activePersonaIdx];
                const res = await fetch('/api/family-blessing', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({ sender_id: p.id, recipient_id: activeFsmMemberId, blessing_type: type })
                });
                const d = await res.json();
                addPearls(d.pearls_awarded_both);
                familyGhafDrops += d.ghaf_tree_drops_added;
                const pct = Math.min(100, (familyGhafDrops / 2000 * 100)).toFixed(0);
                document.getElementById('ghaf-drops-pct').innerText = `${pct}%`;
                document.getElementById('ghaf-tree-bar').style.width = `${pct}%`;
                document.getElementById('ghaf-drops-count').innerText = `${familyGhafDrops.toLocaleString()} / 2,000 Hydration Drops`;

                showToast(`🤲 ${d.blessing} delivered to ${activeFsmMemberId}! +${d.pearls_awarded_both} Pearls.`);
                fireConfetti();
                closeFamilyStackModal();
            } catch (err) {
                showToast("☕ Family Blessing sent! Sacred Ghaf Tree nourished.");
                closeFamilyStackModal();
            }
        }

        async function openFamilyQrModal(initialTab = 'share') {
            switchQrTab(initialTab);
            document.getElementById('family-qr-modal').classList.add('open');
            playSound('tap');

            try {
                const p = PERSONAS[activePersonaIdx];
                const res = await fetch('/api/family-qr-generate', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({ user_id: p.id, family_id: "al-mansouri" })
                });
                const d = await res.json();
                document.getElementById('fqr-inviter-label').innerText = `${d.inviter_name} • Sacred Oasis Care Circle`;
                document.getElementById('fqr-svg-container').innerHTML = d.qr_svg;
                cachedQrDeepLink = d.deep_link;
            } catch (err) {
                console.error("QR gen error", err);
            }
        }

        function closeFamilyQrModal() {
            document.getElementById('family-qr-modal').classList.remove('open');
        }

        function switchQrTab(tab) {
            if (tab === 'share') {
                document.getElementById('fqr-view-share').style.display = 'flex';
                document.getElementById('fqr-view-scan').style.display = 'none';
                document.getElementById('fqr-tab-share').classList.add('active');
                document.getElementById('fqr-tab-scan').classList.remove('active');
            } else {
                document.getElementById('fqr-view-share').style.display = 'none';
                document.getElementById('fqr-view-scan').style.display = 'flex';
                document.getElementById('fqr-tab-share').classList.remove('active');
                document.getElementById('fqr-tab-scan').classList.add('active');
            }
        }

        function copyCareCircleLink() {
            const link = cachedQrDeepLink || "bilota://majlis/pair?family=al-mansouri&token=sovereign-oasis-v4";
            navigator.clipboard.writeText(link).then(() => {
                showToast("📋 Sovereign Care Circle deep link copied to clipboard!");
            }).catch(() => {
                showToast("📋 Care Circle token: bilota://majlis/pair?family=al-mansouri");
            });
        }

        function simulateFamilyScan() {
            playSound('win');
            fireConfetti();
            addPearls(50);
            familyGhafDrops += 50;
            const pct = Math.min(100, (familyGhafDrops / 2000 * 100)).toFixed(0);
            document.getElementById('ghaf-drops-pct').innerText = `${pct}%`;
            document.getElementById('ghaf-tree-bar').style.width = `${pct}%`;
            document.getElementById('ghaf-drops-count').innerText = `${familyGhafDrops.toLocaleString()} / 2,000 Hydration Drops`;

            showToast("🎉 Khalid's phone scanned your Sovereign QR! Al-Mansouri Care Circle linked (+50 Drops).");
            setTimeout(closeFamilyQrModal, 1200);
        }

        async function tagFamilyMember(memberId) {
            playSound('win');
            fireConfetti();
            try {
                const res = await fetch('/api/family-qr-pair', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({ qr_token: "MEMBER-TAG", new_member_id: memberId })
                });
                const d = await res.json();
                const m = d.tagged_member;

                // Dynamically add to family grid if not present
                const grid = document.getElementById('family-member-grid');
                if (!document.getElementById(`fcard-${m.id}`)) {
                    const card = document.createElement('div');
                    card.id = `fcard-${m.id}`;
                    card.className = "family-card";
                    card.onclick = () => openFamilyMemberStack(m.id);
                    card.innerHTML = `
                        <div style="position: relative;">
                            <img src="${m.avatar}" alt="${m.name}" style="width: 44px; height: 44px; border-radius: 10px; object-fit: cover;" onerror="this.src='/assets/user-fatima.png'">
                            <span style="position: absolute; bottom: -4px; right: -4px; font-size: 1rem;">✨</span>
                        </div>
                        <div style="overflow: hidden; flex: 1;">
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <div style="font-size: 0.78rem; font-weight: 800;">${m.name}</div>
                                <span style="font-size: 0.58rem; background: #D1FAE5; color: var(--emerald-main); padding: 1px 4px; border-radius: 4px; font-weight: 800;">NEW PAIR</span>
                            </div>
                            <div style="font-size: 0.65rem; color: var(--sand-gold); font-weight: 600;">${m.cat_badge}</div>
                            <div style="font-size: 0.62rem; color: var(--text-muted);">+${m.drops_contributed} drops • ${m.active_habit}</div>
                            <div style="font-size: 0.60rem; color: var(--emerald-main); font-weight: 700; margin-top: 2px;">🔍 Tap to View Stack</div>
                        </div>
                    `;
                    grid.appendChild(card);
                }

                addPearls(d.pearls_awarded_both);
                familyGhafDrops += d.ghaf_tree_drops_added;
                const pct = Math.min(100, (familyGhafDrops / 2000 * 100)).toFixed(0);
                document.getElementById('ghaf-drops-pct').innerText = `${pct}%`;
                document.getElementById('ghaf-tree-bar').style.width = `${pct}%`;
                document.getElementById('ghaf-drops-count').innerText = `${familyGhafDrops.toLocaleString()} / 2,000 Hydration Drops`;

                showToast(d.affirmation_en);
                setTimeout(closeFamilyQrModal, 1200);
            } catch (err) {
                showToast("✨ Mabrook! Family member connected to Oasis!");
                closeFamilyQrModal();
            }
        }

"""
    if "openFamilyMemberStack" not in content:
        content = content.replace(js_anchor, new_js + js_anchor, 1)
        print("JavaScript functions added for Family QR and Habit Stacks.")

    INDEX_PATH.write_text(content, encoding="utf-8")
    print("SUCCESS: index.html updated successfully!")

if __name__ == "__main__":
    apply_updates()
