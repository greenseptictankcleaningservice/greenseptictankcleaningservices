from bs4 import BeautifulSoup

with open("index.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

btns = soup.find_all(lambda tag: tag.name in ['a', 'button'] and ('btn' in tag.get('class', [])))

print(f"Total .btn in index.html: {len(btns)}")
for idx, b in enumerate(btns):
    print(f"[{idx}] {b.name} class='{' '.join(b.get('class', []))}' -> {b.prettify()[:150]}")
