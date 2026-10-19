---
name: feline-health-ui
description: Design principles, tactile aesthetics, and interaction patterns for Bilota's living feline health companion UI/UX. Eliminates AI slop, establishes human-pet role clarity, and creates living biometric avatars.
---

# Skill: Feline Health Companion UI/UX (Living Biometric Pet)

## 1. Foundational Architecture: The Mirror Principle
- **The User is Human**: Users (e.g., Fatima, Tariq, Aisha) are Emirati citizens with distinct human clinical baselines, wearable biometric streams (IFHAS, Sahatna, Malaffi), and cultural/environmental constraints. They are NEVER depicted as cats.
- **The Cat is the Living Companion (Bilota)**: The Arabian Sand Cat (*Felis margarita harrisoni*) is the user's virtual health pet. The cat's visual state, posture, coat sheen, and energy level directly mirror the user's autonomic recovery and habit persistence.
- **Symbiotic Care Loop**: The user does not track habits for an abstract streak number; they care for Bilota. When the user logs an indoor 5-min walk, Bilota perks up, drinks fresh water, and purrs. When the user experiences heat fatigue, Bilota seeks shade and rests without blame.

## 2. Strict Anti-AI-Slop Design Heuristics
- **No Neon Border Spaghetti**: Eliminate arbitrary glowing gradients (no random pink/cyan/lime boxes). Use restrained, physical borders (`rgba(255, 255, 255, 0.08)`) and purposeful illumination (single light source, subtle ambient occlusion).
- **No Text Wall Disguised as UI**: Replace paragraphs of explanatory text with structured micro-data, tactile controls, and visual states.
- **No Childish Emoji Overload**: Restrict icons to meaningful SVG primitives or high-craft indicators.
- **Typography with Gravitas**:
  - Latin: Inter / Outfit / SF Pro Display with clean letter spacing and distinct weights.
  - Arabic: Cairo / IBM Plex Sans Arabic with authentic Modern Standard Arabic typography and proper RTL line-height (1.6+).
- **Tactile Depth & Material Authenticity**: Use matte dark slate (`#0B0E14`), deep midnight navy (`#111624`), subtle frosted glass (`backdrop-filter: blur(24px)`), and authentic physical press states (`transform: translateY(1px)`).

## 3. Living Companion Visual States (Arabian Sand Cat)
Bilota transitions dynamically across 4 biometric states:
1. **Thriving (State: ENERGIZED)**:
   - *Biometrics*: Active habits completed, resting HR optimal, 90-day momentum strong.
   - *Visual*: Alert golden eyes, sleek sand-colored coat sheen, upright alert posture, playful ear tufts.
2. **Resting & Cooling (State: HYDRATING_SHADE)**:
   - *Biometrics*: 43°C summer heat detected, volume halved via BCT 8.7.
   - *Visual*: Relaxed indoor posture, grooming paws near a cool water bowl, peaceful expression.
3. **Fatigued / Lapsed (State: LOW_ENERGY_NO_SHAME)**:
   - *Biometrics*: 4-day missed activity, zero streak punishment, awaiting micro-win.
   - *Visual*: Drowsy, curled softly on a cushion, low energy bar (never dead or injured!), gently purring when petted.
4. **48h Catnap (State: RECOVERY_PAUSE)**:
   - *Biometrics*: Guilt-free pause activated.
   - *Visual*: Deep curled sleep with slow breathing animation, gentle Zzz floating effect.

## 4. Sensory & Tactile Feedback Loops
- **Web Audio Haptics**: Synthesized subtle harmonic chords on habit completion (pentatonic C-E-G-C) and gentle cat purr oscillations (60-120 Hz modulation) when interacted with.
- **Direct Physical Cause-and-Effect**:
  - `[Drink Water]` -> Water level in bowl drops, Bilota laps water, User hydration +250ml logged.
  - `[Log 5-Min Step]` -> Bilota stretches front paws, coat glows with a golden sheen, +1 Day added to Momentum Bank.
  - `[Pet Bilota]` -> Subtle vibration/purr audio, heart bubble rises.
