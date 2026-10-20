---
description: Generates, audits, and upgrades application UI/UX using modern design systems, Bento layouts, ambient glassmorphism, and Google Stitch CLI integration.
---

# Workflow: `/modern-ui`

Execute a modern UI/UX design pass or design evolution for the application.

## 1. Context & Design Heuristics Audit
1. Evaluate current UI against modern design tokens:
   - **Atmospheric Layering**: Remove harsh borders; replace with tonal depth (`surface_dim` -> `surface_container_high`).
   - **Bento Grid Architecture**: Ensure 2-column and full-span asymmetric cards with clean hierarchy.
   - **Typography**: Check Latin font pairing (`Outfit`/`Inter`) and Arabic typography (`Cairo`/`IBM Plex Sans Arabic`) for proper RTL alignment.
   - **Tactile Feel**: Verify micro-interactions, press feedback (`active:scale-95`), and haptic audio cues.
   - **Anti-AI-Slop**: Remove generic rainbow gradients, walls of text, and meaningless placeholders.

## 2. Google Stitch CLI Design Loop
1. Verify Stitch authentication status:
   ```bash
   stitch status --json
   ```
2. Generate screen concepts or variants using Stitch:
   ```bash
   stitch generate screen -p <PROJECT_ID> --device MOBILE --prompt "<Art direction prompt>" --json
   ```
3. Extract design tokens and inspect generated layout/assets.
4. Capture local preview to Stitch Canvas:
   ```bash
   stitch capture http://localhost:8080/ -o .stitch/stage.html --json
   ```

## 3. Implementation & Visual Polish
1. Apply design changes to `src/ui/index.html` or frontend templates.
2. Verify Judge Control Bar visibility, accessibility, and bilingual toggle.
3. Validate responsive mobile container (max 480px) and dark/light luxury modes.
4. Provide summary of changes and preview links.
