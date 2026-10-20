---
name: modern-ui-ux
description: Complete blueprint, design systems, and execution procedures for generating modern, world-class UI/UX designs. Incorporates Google Stitch workflows, tactile feedback, ambient glassmorphism, responsive Bento grids, bilingual typography, and anti-AI-slop design heuristics.
---

# Skill: Modern UI/UX Designs

A production-grade design system and execution engine for creating ultra-modern, high-craft, accessible digital interfaces across mobile and web platforms.

## 1. Core Design Philosophy: Atmospheric Depth & Craft

Modern UI/UX has moved past flat rectangles and generic AI-generated template boxes ("AI Slop"). World-class modern design is characterized by:

1. **Atmospheric Layering & Ambient Lume**:
   - Depth is created by subtle tonal gradations and ambient lighting rather than heavy 1px black borders or harsh drop shadows.
   - Surface hierarchy moves progressively from canvas floor (`surface_dim` / `bg_canvas`) to sub-sections (`surface_container_low`), active interactive cards (`surface_container_high`), and elevated popovers (`surface_container_highest`).
   - Frosted glassmorphism (`backdrop-filter: blur(20px) saturate(180%)`) with semi-transparent surfaces (`rgba(255, 255, 255, 0.04)` to `0.10`).

2. **Bento Grid & Information Architecture**:
   - Content is modularized into high-contrast Bento cards with varied spans (1x1, 2x1, 2x2).
   - Each card has a distinct primary metric, micro-sparkline or visual indicator, and a single high-clarity contextual action.
   - Elimination of line dividers: borders are either completely absent or soft ghost outlines (`rgba(255, 255, 255, 0.08)` / `rgba(0, 0, 0, 0.06)`).

3. **Typography with Gravitas**:
   - Modern geometric sans-serif for Latin scripts: `Outfit`, `Inter`, `Plus Jakarta Sans`, `SF Pro`.
   - Native premium Arabic typography: `Cairo`, `IBM Plex Sans Arabic` with proper line-height balance (1.6+) and RTL optical centering.
   - Strict hierarchical sizing: `display-lg` (32-40px bold, tight tracking), `headline-md` (20-24px), `title-sm` (14-16px semi-bold), `label-xs` (10-12px uppercase, wide tracking +0.05em for metadata).

4. **Living Biometric & Avatar Visuals**:
   - Digital companions, progress visualizers, and state avatars that breathe and respond in real-time.
   - Tactile feedback loops: web-audio haptics, spring animations (`cubic-bezier(0.34, 1.56, 0.64, 1)`), and soft hover/press transforms.

5. **Human Dignity & Non-Punitive Feedback**:
   - Positive reinforcement and non-punitive momentum preservation.
   - Zero-shame lapses: difficulty auto-downshifts (BCT 8.7), streak protection shields, and warm micro-wins.

---

## 2. Google Stitch CLI Workflow

Use the official Google Stitch CLI (`@google/stitch`) to rapidly generate, iterate, and capture modern screens:

### Step 1: Authentication & Health Check
```bash
# Check current connection & canvas status
stitch status --json

# If not authenticated, login via OAuth PKCE or set API key:
stitch login
# or: stitch config set apiKey "<KEY>" --global
```

### Step 2: Canvas Project Linking
```bash
# List existing Stitch projects
stitch find projects --limit 10 --json

# Create or bind project
stitch create project --title "Project Name" --json
stitch config set project <PROJECT_ID>
```

### Step 3: Screen Generation with High-Craft Prompts
Enhance your generation prompts with Stitch-specific keywords:
```bash
stitch generate screen \
  --project <PROJECT_ID> \
  --device MOBILE \
  --title "Screen Title" \
  --prompt "Modern luxury mobile interface with ambient glassmorphism cards, living avatar hero, bento vitals grid, dark mode obsidian palette, emerald and warm sand gold accents, rounded-2xl pills, micro-sparklines." \
  --json
```

### Step 4: Reverse Snapshot (Code to Design)
Capture local frontend views into Stitch Canvas:
```bash
stitch capture http://localhost:8080/ -o .stitch/stage.html --json
stitch upload screen .stitch/stage.html --route / --title "Production Stage" --json
```

---

## 3. Design Token Architecture

```css
:root {
    /* Obsidian & Desert Gold Modern Palette */
    --surface-canvas: #090D16;
    --surface-card: #121826;
    --surface-card-hover: #182238;
    --surface-subtle: #1C263D;
    
    --border-ghost: rgba(255, 255, 255, 0.08);
    --border-accent: rgba(245, 158, 11, 0.35);

    --primary-accent: #F59E0B;
    --primary-glow: rgba(245, 158, 11, 0.25);
    --secondary-emerald: #10B981;
    --secondary-glow: rgba(16, 185, 129, 0.22);
    --tertiary-cyan: #06B6D4;

    --text-primary: #F8FAFC;
    --text-secondary: #94A3B8;
    --text-tertiary: #64748B;

    --radius-sm: 8px;
    --radius-md: 14px;
    --radius-lg: 20px;
    --radius-xl: 28px;
    --radius-full: 9999px;

    --shadow-ambient: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    --shadow-glow: 0 0 24px -4px var(--primary-glow);
}
```

---

## 4. Anti-AI-Slop Checklist

Before delivering or approving any UI design:
- [ ] No rainbow-gradient border loops around every single card.
- [ ] No text paragraphs explaining obvious UI controls.
- [ ] No placeholder icons without semantic meaning.
- [ ] Consistent 4px or 8px grid spacing throughout.
- [ ] Both Light and Dark modes have WCAG AA / AAA contrast ratios.
- [ ] RTL Arabic layout aligns typography and switches coordinate arrows naturally.
- [ ] Buttons have tangible active/press feedback states (`active:scale-95`).
- [ ] Top bar displays key status badges cleanly without crowding.
