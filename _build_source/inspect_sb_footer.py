from bs4 import BeautifulSoup

for filename in ["_build_source/sb_markets.html", "_build_source/sb_fall_protection.html"]:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")
        footer = soup.find('footer')
        if footer:
            print(f"\n=== FOOTER IN {filename} ===")
            print(footer.prettify()[:2500])
    except Exception as e:
        print(f"Error {filename}: {e}")
