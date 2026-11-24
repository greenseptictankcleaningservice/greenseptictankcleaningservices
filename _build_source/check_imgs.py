import os
from PIL import Image

for root, dirs, files in os.walk("public/images"):
    for f in files:
        path = os.path.join(root, f)
        try:
            with Image.open(path) as img:
                print(f"{path}: {img.size}, format={img.format}")
        except Exception as e:
            print(f"{path}: error {e}")
