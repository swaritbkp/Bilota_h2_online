"""
Applies Google Stitch 'Emerald Dune Luxury' design system to src/ui/index.html
"""
import re

def update_ui():
    with open('src/ui/index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update html tag to dark default
    content = content.replace('<html lang="en" dir="ltr" class="light">', '<html lang="en" dir="ltr" class="dark">')

    # 2. Add Plus Jakarta Sans & Material Symbols to fonts
    old_fonts = '<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=Outfit:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">'
    new_fonts = '<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=Outfit:wght@300;400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">\n    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet">'
    content = content.replace(old_fonts, new_fonts)

    # 3. Stitch Design System Styles
    stitch_css = """
        :root {
            /* STITCH GOOGLE DESIGN SYSTEM: EMERALD DUNE LUXURY */
            --bg-app: #001711;
            --surface-container-lowest: #00110c;
            --surface-container-low: #002019;
            --surface-container: #03251d;
            --surface-container-high: #0f2f27;
            --surface-container-highest: #1b3a32;

            --bg-card: rgba(10, 58, 47, 0.55);
            --bg-card-subtle: rgba(15, 47, 39, 0.65);
            --border-light: rgba(212, 175, 55, 0.22);
            --border-focus: #E9C349;

            --text-main: #F4EBD9;
            --text-muted: #C0C8C4;
            --text-light: #8A938E;

            --sand-gold: #D4AF37;
            --sand-gold-light: rgba(233, 195, 73, 0.16);
            --sand-gold-bright: #E9C349;

            --emerald-main: #4ECCA3;
            --emerald-light: rgba(78, 204, 163, 0.18);
            --emerald-bright: #A2D0C0;

            --cyan-main: #38BDF8;
            --cyan-light: rgba(56, 189, 248, 0.15);

            --rose-main: #FFB4AB;
            --rose-light: rgba(255, 180, 171, 0.15);

            --indigo-main: #818CF8;
            --indigo-light: rgba(129, 140, 248, 0.15);

            --font-main: 'Outfit', 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
            --font-body: 'Plus Jakarta Sans', sans-serif;
            --font-ar: 'Cairo', 'Outfit', sans-serif;
            --font-mono: 'JetBrains Mono', monospace;

            --shadow-sm: 0 2px 6px rgba(0, 17, 12, 0.4);
            --shadow-md: 0 8px 24px -4px rgba(0, 17, 12, 0.6), 0 0 16px rgba(212, 175, 55, 0.08);
            --shadow-lg: 0 16px 40px -6px rgba(0, 17, 12, 0.7), 0 0 28px rgba(162, 208, 192, 0.12);

            --bottom-nav-height: 68px;
            --safe-bottom: env(safe-area-inset-bottom, 12px);
        }

        /* REFINED LIGHT OASIS PALETTE */
        html.light {
            --bg-app: #F7F5EE;
            --bg-card: #FFFFFF;
            --bg-card-subtle: #F0EDE4;
            --border-light: #E2DBD0;
            --border-focus: #CBD5E1;

            --text-main: #0E2922;
            --text-muted: #4B635C;
            --text-light: #7E968F;

            --sand-gold: #B38600;
            --sand-gold-light: #FFF8E1;
            --sand-gold-bright: #D4AF37;

            --emerald-main: #0B6B53;
            --emerald-light: #E0F2ED;
            --emerald-bright: #108A6B;

            --cyan-main: #0284C7;
            --cyan-light: #E0F2FE;

            --rose-main: #E11D48;
            --rose-light: #FFE4E6;

            --indigo-main: #6366F1;
            --indigo-light: #EEF2FF;

            --shadow-sm: 0 1px 3px rgba(0,0,0,0.05);
            --shadow-md: 0 4px 14px -2px rgba(0,0,0,0.06);
            --shadow-lg: 0 12px 30px -4px rgba(0,0,0,0.08);
        }

        /* DARK MODE LUXURY PALETTE (STITCH CANONICAL) */
        html.dark {
            --bg-app: #001711;
            --bg-card: rgba(10, 58, 47, 0.6);
            --bg-card-subtle: rgba(15, 47, 39, 0.7);
            --border-light: rgba(212, 175, 55, 0.22);
            --border-focus: #E9C349;

            --text-main: #F4EBD9;
            --text-muted: #C0C8C4;
            --text-light: #8A938E;

            --sand-gold-light: rgba(233, 195, 73, 0.16);
            --emerald-light: rgba(78, 204, 163, 0.18);
            --cyan-light: rgba(56, 189, 248, 0.15);
            --rose-light: rgba(255, 180, 171, 0.15);
            --indigo-light: rgba(129, 140, 248, 0.15);

            --shadow-sm: 0 2px 6px rgba(0, 17, 12, 0.4);
            --shadow-md: 0 8px 24px -4px rgba(0, 17, 12, 0.6);
            --shadow-lg: 0 16px 40px -6px rgba(0, 17, 12, 0.7);
        }

        /* STITCH DESIGN SYSTEM COMPONENTS */
        .stitch-petsync-strip {
            background: rgba(0, 32, 25, 0.85);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-bottom: 1px solid rgba(212, 175, 55, 0.2);
            padding: 7px 18px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .stitch-live-dot {
            width: 7px;
            height: 7px;
            border-radius: 50%;
            background: #4ECCA3;
            box-shadow: 0 0 8px #4ECCA3;
            display: inline-block;
            animation: pingDot 2s cubic-bezier(0, 0, 0.2, 1) infinite;
        }
        @keyframes pingDot {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.5; transform: scale(1.2); }
        }
        .halo-pulse {
            animation: haloPulse 4s ease-in-out infinite alternate;
        }
        @keyframes haloPulse {
            0% {
                box-shadow: 0 0 20px rgba(233, 195, 73, 0.25), 0 0 45px rgba(10, 58, 47, 0.5);
            }
            100% {
                box-shadow: 0 0 35px rgba(233, 195, 73, 0.45), 0 0 60px rgba(162, 208, 192, 0.35);
            }
        }
    """

    # Replace root block
    pattern_root = r":root\s*\{[^}]*\}\s*/\*\s*DARK MODE LUXURY PALETTE\s*\*/\s*html\.dark\s*\{[^}]*\}"
    content = re.sub(pattern_root, stitch_css.strip(), content, flags=re.DOTALL)

    # 4. Enhance body background with ambient gradients
    old_body = """        body {
            background-color: var(--bg-app);
            color: var(--text-main);
            font-family: var(--font-main);
            font-size: 14px;
            line-height: 1.5;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            overflow-x: hidden;
            -webkit-font-smoothing: antialiased;
        }"""
    
    new_body = """        body {
            background-color: var(--bg-app);
            color: var(--text-main);
            font-family: var(--font-body);
            font-size: 14px;
            line-height: 1.5;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            overflow-x: hidden;
            -webkit-font-smoothing: antialiased;
            background: radial-gradient(ellipse at top right, rgba(233, 195, 73, 0.12) 0%, transparent 60%), radial-gradient(ellipse at bottom left, rgba(78, 204, 163, 0.1) 0%, transparent 60%), #001711;
        }

        html.light body {
            background: linear-gradient(135deg, #F5F1E8 0%, #EAE4D5 100%);
        }"""
    content = content.replace(old_body.replace('\r\n', '\n'), new_body)

    # 5. Insert Malaffi PetSync strip right after top-judge-bar
    petsync_markup = """
        <!-- STITCH DESIGN: MALAFFI PETSYNC REALTIME STATUS STRIP -->
        <div class="stitch-petsync-strip">
            <div style="display: flex; align-items: center; gap: 8px;">
                <span class="stitch-live-dot"></span>
                <span style="font-size: 0.72rem; font-weight: 700; color: var(--emerald-bright); letter-spacing: 0.05em; text-transform: uppercase;">Malaffi PetSync: Active</span>
            </div>
            <div style="display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 0.65rem; color: var(--sand-gold); background: var(--sand-gold-light); padding: 2px 8px; border-radius: 9999px; border: 1px solid rgba(212, 175, 55, 0.3); font-weight: 700;">UAE-09418</span>
                <span style="font-size: 0.68rem; color: var(--text-muted); font-weight: 600;">Abu Dhabi 38°C Safe Oasis</span>
            </div>
        </div>
    """

    if '<header class="top-judge-bar">' in content and 'stitch-petsync-strip' not in content:
        content = content.replace('</header>', '</header>\n' + petsync_markup, 1)

    with open('src/ui/index.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("Successfully updated src/ui/index.html with Stitch Emerald Dune Luxury design system!")

if __name__ == '__main__':
    update_ui()
