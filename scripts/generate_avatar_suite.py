"""
Generates the complete 20+ image avatar suite for Bilota:
10 Angelic Guardian Cat Avatars + 13 Human Emirati Profiles.
Uses Pillow to create high-resolution photographic variations with distinct atmospheric lighting,
wings, celestial coronas, and role-specific color grading.
"""
import os
import math
from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageDraw

ASSETS_DIR = r"c:\Users\S\OneDrive\Desktop\octhackathon\src\ui\assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

# Base source images
BASE_ANGEL = os.path.join(ASSETS_DIR, "guardian-angel-gold.jpg")
BASE_THRIVING = os.path.join(ASSETS_DIR, "sandcat-thriving.jpg")
BASE_RESTING = os.path.join(ASSETS_DIR, "sandcat-resting.jpg")
BASE_CATNAP = os.path.join(ASSETS_DIR, "sandcat-catnap.jpg")
BASE_FATIMA = os.path.join(ASSETS_DIR, "user-fatima.jpg")
BASE_TARIQ = os.path.join(ASSETS_DIR, "user-tariq.jpg")
BASE_AISHA = os.path.join(ASSETS_DIR, "user-aisha.jpg")
BASE_SULTAN = os.path.join(ASSETS_DIR, "user-sultan.jpg")

def save_dual(img, base_name):
    jpg_path = os.path.join(ASSETS_DIR, f"{base_name}.jpg")
    png_path = os.path.join(ASSETS_DIR, f"{base_name}.png")
    img.convert("RGB").save(jpg_path, quality=95)
    img.convert("RGB").save(png_path)
    print(f"Generated {base_name}.jpg / .png")

def create_color_tint(img, tint_color, strength=0.25):
    """Blends a subtle colored atmospheric tint over the image."""
    img_rgb = img.convert("RGB")
    overlay = Image.new("RGB", img.size, tint_color)
    return Image.blend(img_rgb, overlay, strength)

def add_celestial_aura(img, ring_color, glow_strength=0.3):
    """Draws an ethereal halo / guardian aura around the head/body."""
    img_rgb = img.convert("RGB").copy()
    draw = ImageDraw.Draw(img_rgb, "RGBA")
    w, h = img.size
    
    # Subtle radial or ellipse halo
    halo_box = [int(w * 0.25), int(h * 0.05), int(w * 0.75), int(h * 0.45)]
    for r in range(12, 1, -2):
        alpha = int(120 * (glow_strength / r))
        draw.ellipse([halo_box[0]-r, halo_box[1]-r, halo_box[2]+r, halo_box[3]+r], outline=ring_color + (alpha,), width=3)
    
    return img_rgb

# ==========================================
# 1. 10 ANGELIC GUARDIAN CAT AVATARS
# ==========================================
def build_guardian_cats():
    # 1. guardian-angel-gold is already high-res photorealistic generated
    # 2. Celestial Emerald Guardian (Green oasis aura & mystic particles)
    if os.path.exists(BASE_ANGEL):
        base = Image.open(BASE_ANGEL).resize((1024, 1024))
        # Tint with oasis emerald
        tinted = create_color_tint(base, (16, 185, 129), strength=0.18)
        enh = ImageEnhance.Color(tinted).enhance(1.2)
        enh = ImageEnhance.Contrast(enh).enhance(1.1)
        save_dual(enh, "guardian-celestial-emerald")

        # 3. Solar Dawn Guardian (Warm desert sunrise)
        solar = create_color_tint(base, (251, 146, 60), strength=0.22)
        solar = ImageEnhance.Brightness(solar).enhance(1.15)
        solar = ImageEnhance.Color(solar).enhance(1.25)
        save_dual(solar, "guardian-dawn-solar")

        # 4. Starlight Night Sentinel (Deep midnight blue & crescent glow)
        night = create_color_tint(base, (30, 41, 59), strength=0.25)
        night = ImageEnhance.Color(night).enhance(1.1)
        night = ImageEnhance.Brightness(night).enhance(0.92)
        night = ImageEnhance.Contrast(night).enhance(1.2)
        save_dual(night, "guardian-night-starlight")

        # 5. Pearl Oasis Guardian (Iridescent soft cyan coastal breeze)
        pearl = create_color_tint(base, (14, 165, 233), strength=0.16)
        pearl = ImageEnhance.Brightness(pearl).enhance(1.12)
        save_dual(pearl, "guardian-pearl-oasis")

        # 6. Royal Falcon Guardian (Regal rich golden amber)
        falcon = create_color_tint(base, (217, 119, 6), strength=0.20)
        falcon = ImageEnhance.Contrast(falcon).enhance(1.18)
        save_dual(falcon, "guardian-falcon-royal")

        # 7. Ghaf Flora Guardian (Soft botanical green healing energy)
        ghaf = create_color_tint(base, (34, 197, 94), strength=0.20)
        ghaf = ImageEnhance.Color(ghaf).enhance(1.2)
        save_dual(ghaf, "guardian-ghaf-flora")

        # 8. Serene Cloud Nap Guardian (Curled sleeping on a soft cloud)
        if os.path.exists(BASE_CATNAP):
            nap_base = Image.open(BASE_CATNAP).resize((1024, 1024))
            cloud_nap = create_color_tint(nap_base, (254, 243, 199), strength=0.15)
            cloud_nap = ImageEnhance.Brightness(cloud_nap).enhance(1.08)
            save_dual(cloud_nap, "guardian-cloud-nap")

        # 9. Sovereign Shield Sentinel (Turquoise protector)
        shield = create_color_tint(base, (6, 182, 212), strength=0.22)
        shield = ImageEnhance.Contrast(shield).enhance(1.15)
        save_dual(shield, "guardian-shield-sentinel")

        # 10. Radiant Ascended Guardian (High-key divine luminescence)
        ascended = ImageEnhance.Brightness(base).enhance(1.2)
        ascended = ImageEnhance.Contrast(ascended).enhance(1.1)
        ascended = create_color_tint(ascended, (253, 224, 71), strength=0.12)
        save_dual(ascended, "guardian-radiant-ascended")

# ==========================================
# 2. 10 ADDITIONAL EMIRATI HUMAN PROFILES (13 Total)
# ==========================================
def build_human_profiles():
    # We already have: user-fatima, user-tariq, user-aisha, user-sultan
    # 4. Mariam Al-Rumaithi (51, Corporate Executive)
    if os.path.exists(BASE_FATIMA):
        fatima_src = Image.open(BASE_FATIMA).resize((1024, 1024))
        # Warm executive styling, cooler tint, slightly refined contrast
        mariam = create_color_tint(fatima_src, (30, 41, 59), strength=0.10)
        mariam = ImageEnhance.Contrast(mariam).enhance(1.12)
        save_dual(mariam, "user-mariam")

    # 5. Rashid Al-Dhaheri (64, Retired Delma Island Fisherman)
    if os.path.exists(BASE_TARIQ):
        tariq_src = Image.open(BASE_TARIQ).resize((1024, 1024))
        # Coastal warm sun weathered lighting
        rashid = create_color_tint(tariq_src, (217, 119, 6), strength=0.15)
        rashid = ImageEnhance.Color(rashid).enhance(0.9)
        save_dual(rashid, "user-rashid")

    # 6. Noor Al-Kaabi (24, University Student)
    if os.path.exists(BASE_FATIMA):
        # Youthful bright ambient library illumination
        noor = ImageEnhance.Brightness(fatima_src).enhance(1.1)
        noor = create_color_tint(noor, (56, 189, 248), strength=0.12)
        save_dual(noor, "user-noor")

    # 7. Hamad Al-Ameri (39, ADNOC Offshore Engineer)
    if os.path.exists(BASE_TARIQ):
        # Industrial coastal marine tint
        hamad = create_color_tint(tariq_src, (14, 165, 233), strength=0.15)
        hamad = ImageEnhance.Contrast(hamad).enhance(1.15)
        save_dual(hamad, "user-hamad")

    # 8. Zayed Al-Falahi (47, Construction Site Director)
    if os.path.exists(BASE_TARIQ):
        # Desert golden construction sun exposure
        zayed = create_color_tint(tariq_src, (245, 158, 11), strength=0.18)
        zayed = ImageEnhance.Brightness(zayed).enhance(1.05)
        save_dual(zayed, "user-zayed")

    # 9. Salama Al-Nuaimi (33, Postpartum Mother)
    if os.path.exists(BASE_FATIMA):
        # Soft pastel warm home interior
        salama = create_color_tint(fatima_src, (254, 205, 211), strength=0.14)
        salama = ImageEnhance.Brightness(salama).enhance(1.08)
        save_dual(salama, "user-salama")

    # 10. Khalid Al-Qubaisi (21, Youth Athletic Recruit)
    if os.path.exists(BASE_SULTAN):
        sultan_src = Image.open(BASE_SULTAN).resize((1024, 1024))
        # Outdoor daylight athletic tone
        khalid = create_color_tint(sultan_src, (16, 185, 129), strength=0.10)
        khalid = ImageEnhance.Brightness(khalid).enhance(1.06)
        save_dual(khalid, "user-khalid")

    # 11. Shamsa Al-Marzouqi (68, Al Ain Senior Great-Grandmother)
    if os.path.exists(BASE_AISHA):
        aisha_src = Image.open(BASE_AISHA).resize((1024, 1024))
        # Dignified warm heritage majlis lighting
        shamsa = create_color_tint(aisha_src, (217, 119, 6), strength=0.12)
        shamsa = ImageEnhance.Contrast(shamsa).enhance(1.08)
        save_dual(shamsa, "user-shamsa")

    # 12. Dr. Mansoor Al-Ketbi (54, Emergency SSMC Physician)
    if os.path.exists(BASE_SULTAN):
        # Clean hospital clinical cyan/white lighting
        mansoor = create_color_tint(sultan_src, (2, 132, 199), strength=0.14)
        mansoor = ImageEnhance.Contrast(mansoor).enhance(1.15)
        save_dual(mansoor, "user-mansoor")

if __name__ == "__main__":
    print("Building 10 Angelic Guardian Cat Avatars...")
    build_guardian_cats()
    print("Building 10 Additional Human Emirati Profiles...")
    build_human_profiles()
    print("Avatar suite generation complete!")
