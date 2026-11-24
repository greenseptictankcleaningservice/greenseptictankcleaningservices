import os
import urllib.request
from bs4 import BeautifulSoup
import re
import json

base_url = "https://www.greenseptictankcleaningservices.com/"
headers = {'User-Agent': 'Mozilla/5.0'}

os.makedirs("public/images/resource", exist_ok=True)
os.makedirs("public/images", exist_ok=True)

# Find all images in gst_septic-tank-cleaning-services.html and gst_index.html
with open("gst_septic-tank-cleaning-services.html", "r", encoding="utf-8") as f:
    gst_service_html = f.read()

with open("gst_index.html", "r", encoding="utf-8") as f:
    gst_index_html = f.read()

soup_service = BeautifulSoup(gst_service_html, "html.parser")
soup_index = BeautifulSoup(gst_index_html, "html.parser")

all_img_srcs = set()
for s in [soup_service, soup_index]:
    for img in s.find_all('img'):
        src = img.get('src')
        if src and not src.startswith('data:'):
            all_img_srcs.add(src)

print(f"Found {len(all_img_srcs)} unique images in GST site:")
for src in sorted(all_img_srcs):
    print("  ", src)
    clean_src = src.lstrip('/')
    out_path = os.path.join("public", clean_src.replace('/', os.sep))
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    full_url = urllib.parse.urljoin(base_url, src)
    try:
        req = urllib.request.Request(full_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as r:
            with open(out_path, "wb") as f_out:
                f_out.write(r.read())
        print(f"    Downloaded -> {out_path}")
    except Exception as e:
        print(f"    Failed: {e}")

# Check any background images in CSS or inline styles in GST
bg_images = re.findall(r'url\([\'"]?([^\'")]+)[\'"]?\)', gst_service_html + gst_index_html)
print(f"Found {len(set(bg_images))} bg images:")
for bg in set(bg_images):
    if not bg.startswith('data:'):
        print("  bg:", bg)
        clean_bg = bg.lstrip('/')
        out_path = os.path.join("public", clean_bg.replace('/', os.sep))
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        full_url = urllib.parse.urljoin(base_url, bg)
        try:
            req = urllib.request.Request(full_url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as r:
                with open(out_path, "wb") as f_out:
                    f_out.write(r.read())
            print(f"    Downloaded bg -> {out_path}")
        except Exception as e:
            print(f"    Failed bg: {e}")

print("Image download complete.")
