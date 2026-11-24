from PIL import Image

src_path = "images/background/clean-safe-septic-services.webp"
with Image.open(src_path) as img:
    # 2000 x 1331 -> crop center to 800 x 1100 ratio
    # target aspect: 800/1100 = 0.727
    w, h = img.size
    target_ratio = 800 / 1100
    new_w = int(h * target_ratio)
    left = (w - new_w) // 2
    cropped = img.crop((left, 0, left + new_w, h))
    resized = cropped.resize((800, 1100), Image.Resampling.LANCZOS)
    resized.save("images/why-service.webp", "WEBP", quality=92)
    print("Created images/why-service.webp (800x1100)")
