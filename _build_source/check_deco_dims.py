from PIL import Image
import os

for f in ["deco-lanyard-v.png", "deco-sling1-v.png", "deco-sling2-v.png", "deco-hook.png"]:
    p = os.path.join("_build_source", f)
    if os.path.exists(p):
        with Image.open(p) as img:
            print(f"{f}: size={img.size}, mode={img.mode}")
