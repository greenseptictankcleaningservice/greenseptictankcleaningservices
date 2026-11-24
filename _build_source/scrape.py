import urllib.request
import urllib.parse
import re
import json
import os

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

def fetch(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.read().decode('utf-8', errors='ignore')
    except Exception as e:
        return f"ERROR: {e}"

# 1. Fetch SB Fall Protection
print("Fetching SB Fall Protection...")
sb_html = fetch("https://sbfallprotection-rust.vercel.app/")
with open("sb_fall_protection.html", "w", encoding="utf-8") as f:
    f.write(sb_html)
print(f"SB Fall Protection HTML length: {len(sb_html)}")

# Find any js/css bundles or other links in SB
css_files = re.findall(r'href="([^"]+\.css[^"]*)"', sb_html)
js_files = re.findall(r'src="([^"]+\.js[^"]*)"', sb_html)
print("SB CSS files:", css_files)
print("SB JS files:", js_files[:5])

# 2. Fetch Green Septic Tank
print("\nFetching Green Septic Tank Cleaning Services...")
gst_urls = [
    "https://www.greenseptictankcleaningservices.com/",
    "https://www.greenseptictankcleaningservices.com/septic-tank-cleaning-services.html",
    "https://www.greenseptictankcleaningservices.com/about-us.html",
    "https://www.greenseptictankcleaningservices.com/contact-us.html",
    "https://www.greenseptictankcleaningservices.com/services.html",
    "https://www.greenseptictankcleaningservices.com/stp-plant-cleaning-services.html"
]

for url in gst_urls:
    name = url.split('/')[-1] or "index.html"
    print(f"Fetching {url} -> gst_{name}...")
    content = fetch(url)
    with open(f"gst_{name}", "w", encoding="utf-8") as f:
        f.write(content)
    print(f"gst_{name} length: {len(content)}")

print("Done scraping!")
