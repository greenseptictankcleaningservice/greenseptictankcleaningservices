from PIL import Image

imgs = [
    "images/resource/notch-septic-tank-cleaning-services.webp",
    "images/resource/reliable-septic-services.webp",
    "images/main-slider/fast-efficient-septic-services.webp",
    "images/background/clean-safe-septic-services.webp"
]

for p in imgs:
    with Image.open(p) as img:
        print(f"{p}: size={img.size}")
