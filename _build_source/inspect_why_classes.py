from bs4 import BeautifulSoup

with open("index.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

why_sec = soup.find('section', id='why')
cards = why_sec.find_all(class_='why-card')
print(f"Found {len(cards)} cards in #why:")
for idx, c in enumerate(cards):
    print(f"[{idx+1}] class='{' '.join(c.get('class', []))}'")

img_card = why_sec.find(class_='why-img')
print(f"why-img class: {' '.join(img_card.get('class', [])) if img_card else 'not found'}")
