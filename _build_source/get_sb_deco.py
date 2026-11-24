import urllib.request
import os

headers = {'User-Agent': 'Mozilla/5.0'}
sb_deco_urls = [
    "https://sbfallprotection-rust.vercel.app/assets/deco-lanyard-v.png",
    "https://sbfallprotection-rust.vercel.app/assets/deco-sling1-v.png",
    "https://sbfallprotection-rust.vercel.app/assets/deco-sling2-v.png",
    "https://sbfallprotection-rust.vercel.app/assets/deco-hook.png"
]

for url in sb_deco_urls:
    fname = os.path.basename(url)
    out = os.path.join("_build_source", fname)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as r:
            with open(out, "wb") as f:
                f.write(r.read())
        print(f"Downloaded {fname} ({os.path.getsize(out)} bytes)")
    except Exception as e:
        print(f"Failed {fname}: {e}")
