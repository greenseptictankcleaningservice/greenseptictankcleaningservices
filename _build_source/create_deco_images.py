from PIL import Image, ImageDraw, ImageFilter
import math
import os

os.makedirs("images", exist_ok=True)

# 1. DECO SUCTION HOSE (deco-suction-hose.webp) - 220 x 850 px
# Heavy duty flexible corrugated suction hose with brass/aluminum camlock coupler at the bottom
w, h = 240, 850
img1 = Image.new("RGBA", (w, h), (0, 0, 0, 0))
draw1 = ImageDraw.Draw(img1)

# Hose runs from top (y=0) down to y=680, then metallic coupling at 680-840
hose_w = 64
cx = w // 2

# Draw the corrugated heavy-duty green & black septic suction hose
for y in range(0, 680):
    # Sinusoidal ribbing effect
    phase = math.sin(y * 0.25)
    r_offset = int(phase * 4)
    hw = (hose_w // 2) + r_offset
    
    # Lighting gradient across horizontal slice
    for x_offset in range(-hw, hw + 1):
        x = cx + x_offset
        norm_x = (x_offset + hw) / (2 * hw) # 0 to 1
        
        # Color gradient: dark emerald green with glossy highlight
        # Rib ring lighting
        is_ridge = phase > 0.3
        if is_ridge:
            base_r, base_g, base_b = 28, 140, 65
        else:
            base_r, base_g, base_b = 15, 60, 30
            
        # Cylindrical highlight (specular reflection at ~30% from left)
        highlight = math.exp(-((norm_x - 0.32) ** 2) / 0.05)
        shadow = math.sin(norm_x * math.pi)
        
        r = int(min(255, base_r * shadow + highlight * 180))
        g = int(min(255, base_g * shadow + highlight * 220))
        b = int(min(255, base_b * shadow + highlight * 160))
        img1.putpixel((x, y), (r, g, b, 255))

# Heavy Brass / Aluminum Camlock Coupler at the bottom (y=680 to 820)
# Collar ring
for y in range(675, 710):
    cw = hose_w // 2 + 8
    for x in range(cx - cw, cx + cw + 1):
        norm = (x - (cx - cw)) / (2 * cw)
        hl = math.exp(-((norm - 0.35) ** 2) / 0.04)
        c = int(140 * math.sin(norm * math.pi) + hl * 115)
        # Silver-aluminum metallic with slight golden-brass accent
        img1.putpixel((x, y), (c, int(c * 0.95), int(c * 0.85), 255))

# Camlock body with lever arms
for y in range(710, 790):
    cw = hose_w // 2 + 12
    for x in range(cx - cw, cx + cw + 1):
        norm = (x - (cx - cw)) / (2 * cw)
        hl = math.exp(-((norm - 0.35) ** 2) / 0.04)
        sh = math.sin(norm * math.pi)
        # Gold/brass camlock body
        r = int(min(255, 180 * sh + hl * 75))
        g = int(min(255, 145 * sh + hl * 70))
        b = int(min(255, 60 * sh + hl * 40))
        img1.putpixel((x, y), (r, g, b, 255))

# Camlock ear levers (left & right)
draw1.rectangle([cx - cw - 8, 725, cx - cw + 2, 765], fill=(160, 130, 50, 255), outline=(90, 70, 20, 255))
draw1.rectangle([cx + cw - 2, 725, cx + cw + 8, 765], fill=(160, 130, 50, 255), outline=(90, 70, 20, 255))

# Nozzle tip / opening
for y in range(790, 835):
    cw = hose_w // 2 + 4
    for x in range(cx - cw, cx + cw + 1):
        norm = (x - (cx - cw)) / (2 * cw)
        sh = math.sin(norm * math.pi)
        hl = math.exp(-((norm - 0.35) ** 2) / 0.04)
        c = int(130 * sh + hl * 125)
        img1.putpixel((x, y), (c, c, int(c * 1.05), 255))

# End hole
draw1.ellipse([cx - 24, 825, cx + 24, 842], fill=(20, 25, 20, 255), outline=(100, 100, 100, 255), width=3)

img1.save("images/deco-suction-hose.webp", "WEBP", quality=95)
print("Created images/deco-suction-hose.webp")


# 2. DECO HYDRO-JETTING HOSE & NOZZLE (deco-jet-nozzle.webp) - 220 x 950 px
# High pressure slim black/steel reinforced flexible hose with bullet rotary jetter nozzle
w2, h2 = 240, 950
img2 = Image.new("RGBA", (w2, h2), (0, 0, 0, 0))
draw2 = ImageDraw.Draw(img2)
cx2 = w2 // 2
hose_w2 = 36

# Jetting hose runs y=0 to 760
for y in range(0, 760):
    hw = hose_w2 // 2
    for x_offset in range(-hw, hw + 1):
        x = cx2 + x_offset
        norm_x = (x_offset + hw) / (2 * hw)
        # Tough matte black/charcoal high-pressure rubber hose with fine braiding texture
        braid = (x + y) % 6 < 3
        sh = math.sin(norm_x * math.pi)
        hl = math.exp(-((norm_x - 0.3) ** 2) / 0.04)
        base = 28 if braid else 38
        r = int(base * sh + hl * 90)
        g = int(base * sh + hl * 90)
        b = int((base + 6) * sh + hl * 100)
        img2.putpixel((x, y), (r, g, b, 255))

# Stainless steel hose crimp collar (y=760 to 810)
for y in range(760, 810):
    cw = hose_w2 // 2 + 6
    for x in range(cx2 - cw, cx2 + cw + 1):
        norm = (x - (cx2 - cw)) / (2 * cw)
        hl = math.exp(-((norm - 0.35) ** 2) / 0.03)
        sh = math.sin(norm * math.pi)
        c = int(min(255, 170 * sh + hl * 160))
        img2.putpixel((x, y), (c, c, int(c * 1.05), 255))

# Hex nut coupling (y=810 to 845)
for y in range(810, 845):
    cw = hose_w2 // 2 + 10
    for x in range(cx2 - cw, cx2 + cw + 1):
        norm = (x - (cx2 - cw)) / (2 * cw)
        hl = math.exp(-((norm - 0.4) ** 2) / 0.03)
        sh = math.sin(norm * math.pi)
        c = int(min(255, 180 * sh + hl * 150))
        img2.putpixel((x, y), (c, c, c, 255))

# Bullet rotary stainless steel jetting head (y=845 to 935)
for y in range(845, 935):
    progress = (y - 845) / 90 # 0 to 1
    # Tapers slightly to bullet point at bottom
    cw = int((hose_w2 // 2 + 8) * (1 - progress * 0.55))
    for x in range(cx2 - cw, cx2 + cw + 1):
        norm = (x - (cx2 - cw)) / (2 * cw if cw > 0 else 1)
        hl = math.exp(-((norm - 0.32) ** 2) / 0.03)
        sh = math.sin(norm * math.pi)
        c = int(min(255, 190 * sh + hl * 170))
        img2.putpixel((x, y), (c, c, int(c * 1.05), 255))

# Front jet orifice & backward thrust orifices
draw2.ellipse([cx2 - 4, 930, cx2 + 4, 938], fill=(15, 15, 15, 255))
draw2.ellipse([cx2 - 12, 880, cx2 - 6, 888], fill=(30, 30, 30, 255))
draw2.ellipse([cx2 + 6, 880, cx2 + 12, 888], fill=(30, 30, 30, 255))

img2.save("images/deco-jet-nozzle.webp", "WEBP", quality=95)
print("Created images/deco-jet-nozzle.webp")


# 3. DECO SLUDGE SUCTION WAND & VALVE (deco-sludge-pipe.webp) - 220 x 880 px
# Stainless / Heavy PVC suction lance with brass ball valve and inlet strainer
w3, h3 = 240, 880
img3 = Image.new("RGBA", (w3, h3), (0, 0, 0, 0))
draw3 = ImageDraw.Draw(img3)
cx3 = w3 // 2
pipe_w = 46

# Pipe shaft y=0 to 650
for y in range(0, 650):
    pw = pipe_w // 2
    for x_offset in range(-pw, pw + 1):
        x = cx3 + x_offset
        norm = (x_offset + pw) / (2 * pw)
        hl = math.exp(-((norm - 0.3) ** 2) / 0.04)
        sh = math.sin(norm * math.pi)
        # Anodized aluminum / high-grade stainless suction wand
        c = int(min(255, 175 * sh + hl * 155))
        img3.putpixel((x, y), (int(c * 0.95), c, int(c * 1.05), 255))

# Brass ball-valve assembly (y=650 to 740)
for y in range(650, 740):
    vw = pipe_w // 2 + 14
    for x in range(cx3 - vw, cx3 + vw + 1):
        norm = (x - (cx3 - vw)) / (2 * vw)
        hl = math.exp(-((norm - 0.35) ** 2) / 0.04)
        sh = math.sin(norm * math.pi)
        r = int(min(255, 195 * sh + hl * 60))
        g = int(min(255, 155 * sh + hl * 55))
        b = int(min(255, 55 * sh + hl * 30))
        img3.putpixel((x, y), (r, g, b, 255))

# Red valve handle protruding to the left
draw3.rectangle([cx3 - vw - 24, 675, cx3 - vw + 4, 695], fill=(215, 35, 30, 255), outline=(130, 15, 10, 255), width=2)
draw3.ellipse([cx3 - vw - 30, 673, cx3 - vw - 18, 697], fill=(225, 40, 35, 255))

# Lower suction pipe extension (y=740 to 800)
for y in range(740, 800):
    pw = pipe_w // 2
    for x in range(cx3 - pw, cx3 + pw + 1):
        norm = (x - (cx3 - pw)) / (2 * pw)
        hl = math.exp(-((norm - 0.3) ** 2) / 0.04)
        sh = math.sin(norm * math.pi)
        c = int(min(255, 175 * sh + hl * 155))
        img3.putpixel((x, y), (int(c * 0.95), c, int(c * 1.05), 255))

# Sludge strainer basket / perforated cage (y=800 to 865)
for y in range(800, 865):
    sw = pipe_w // 2 + 8
    for x in range(cx3 - sw, cx3 + sw + 1):
        norm = (x - (cx3 - sw)) / (2 * sw)
        hl = math.exp(-((norm - 0.35) ** 2) / 0.04)
        sh = math.sin(norm * math.pi)
        # Perforation holes
        is_hole = ((x + y * 2) % 10 < 4) and ((y % 8) < 4)
        if is_hole:
            img3.putpixel((x, y), (20, 25, 20, 255))
        else:
            c = int(min(255, 160 * sh + hl * 140))
            img3.putpixel((x, y), (c, c, int(c * 1.05), 255))

img3.save("images/deco-sludge-pipe.webp", "WEBP", quality=95)
print("Created images/deco-sludge-pipe.webp")
