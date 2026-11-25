import os
from bs4 import BeautifulSoup
import re

html_files = [
    "index.html",
    "services.html",
    "about.html",
    "areas.html",
    "contact.html",
    "blog.html",
    "privacy-policy.html",
    "terms-and-conditions.html",
    "cookies-policy.html",
    "disclaimer.html"
]

all_valid = True

for hf in html_files:
    if not os.path.exists(hf):
        print(f"ERROR: {hf} does not exist!")
        all_valid = False
        continue
    
    with open(hf, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    
    print(f"\n--- Checking {hf} ---")
    
    # Check CSS
    for link in soup.find_all('link', rel='stylesheet'):
        href = link.get('href')
        if not href.startswith('http') and not href.startswith('//'):
            clean_href = href.split('?')[0].split('#')[0]
            if os.path.exists(clean_href):
                print(f"  [OK] CSS: {clean_href} ({os.path.getsize(clean_href)} bytes)")
            else:
                print(f"  [MISSING] CSS: {clean_href}")
                all_valid = False

    # Check JS
    for script in soup.find_all('script'):
        src = script.get('src')
        if src and not src.startswith('http') and not src.startswith('//'):
            clean_src = src.split('?')[0].split('#')[0]
            if os.path.exists(clean_src):
                print(f"  [OK] JS: {clean_src} ({os.path.getsize(clean_src)} bytes)")
            else:
                print(f"  [MISSING] JS: {clean_src}")
                all_valid = False

    # Check IMGs
    missing_imgs = 0
    checked_imgs = 0
    for img in soup.find_all('img'):
        src = img.get('src')
        if src and not src.startswith('http') and not src.startswith('//') and not src.startswith('data:'):
            checked_imgs += 1
            clean_src = src.split('?')[0].split('#')[0]
            if not os.path.exists(clean_src):
                print(f"  [MISSING] IMG: {clean_src}")
                missing_imgs += 1
                all_valid = False

    print(f"  Images verified: {checked_imgs} total, {missing_imgs} missing.")

if all_valid:
    print("\n>>> ALL LOCAL ASSETS & LINKS ARE 100% VALIDATED AND IN PLACE! <<<")
else:
    print("\n>>> SOME LOCAL ASSETS ARE MISSING! <<<")
