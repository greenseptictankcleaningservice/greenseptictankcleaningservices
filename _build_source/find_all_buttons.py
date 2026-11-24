from bs4 import BeautifulSoup

pages = ["index.html", "services.html", "about.html", "areas.html", "contact.html"]

for p in pages:
    with open(p, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    btns = soup.find_all(lambda tag: tag.name in ['a', 'button', 'input'] and ('btn' in tag.get('class', []) or any('btn' in c for c in tag.get('class', []))))
    print(f"\n{p}: {len(btns)} buttons found")
    for b in btns:
        classes = ' '.join(b.get('class', []))
        text = b.get_text(strip=True)[:40]
        print(f"  <{b.name} class='{classes}'>: {text}")
