import urllib.request
import os

headers = {'User-Agent': 'Mozilla/5.0'}
urls = [
    ("js/gsap.min.js", "https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"),
    ("js/ScrollTrigger.min.js", "https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js")
]

for out_path, url in urls:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as r:
            with open(out_path, "wb") as f:
                f.write(r.read())
        print(f"Downloaded {out_path} ({os.path.getsize(out_path)} bytes)")
    except Exception as e:
        print(f"Failed {url}: {e}")
