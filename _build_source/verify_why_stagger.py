from bs4 import BeautifulSoup

with open("index.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

why = soup.find('section', id='why')
text_cards = why.find_all(class_='why-card')
img_card = why.find(class_='why-img')

print(f"Text cards in #why: {len(text_cards)}")
for idx, c in enumerate(text_cards):
    print(f"  [{idx+1}] class='{' '.join(c.get('class', []))}', h3='{c.find('h3').get_text()}'")

print(f"\nPhoto card in #why: class='{' '.join(img_card.get('class', [])) if img_card else 'None'}'")

print("\nScripts at bottom:")
for s in soup.find_all('script'):
    print(" ", s.get('src'))
