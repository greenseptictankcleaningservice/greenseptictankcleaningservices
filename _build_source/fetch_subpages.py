import urllib.request

headers = {'User-Agent': 'Mozilla/5.0'}
urls = [
    ("sb_products.html", "https://sbfallprotection-rust.vercel.app/products"),
    ("sb_about.html", "https://sbfallprotection-rust.vercel.app/about"),
    ("sb_contact.html", "https://sbfallprotection-rust.vercel.app/contact"),
    ("sb_markets.html", "https://sbfallprotection-rust.vercel.app/export-markets")
]

for filename, url in urls:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as r:
            content = r.read().decode('utf-8', errors='ignore')
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Fetched {url} -> {filename} ({len(content)} bytes)")
    except Exception as e:
        print(f"Failed {url}: {e}")
