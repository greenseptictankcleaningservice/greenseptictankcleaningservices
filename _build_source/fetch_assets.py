import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0'}

def fetch(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.read()
    except Exception as e:
        print(f"Error {url}: {e}")
        return None

# Fetch CSS
css_data = fetch("https://sbfallprotection-rust.vercel.app/_astro/about.Rlf23sT7.css")
if css_data:
    with open("sb_style.css", "wb") as f:
        f.write(css_data)
    print(f"Downloaded sb_style.css: {len(css_data)} bytes")

# Also fetch JS if available
js_data = fetch("https://sbfallprotection-rust.vercel.app/_astro/Base.astro_astro_type_script_index_0_lang.edDZzk6g.js")
if js_data:
    with open("sb_script.js", "wb") as f:
        f.write(js_data)
    print(f"Downloaded sb_script.js: {len(js_data)} bytes")

print("Assets fetched.")
