from bs4 import BeautifulSoup

with open("index.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

featured = soup.find('section', id='featured')
print("=== UPDATED #featured SECTION ===")
print("Section tag:", featured.name, featured.get('id'), featured.get('class'))
print("Heading:", featured.find(['h2']).get_text())
print("Track:", featured.find(id='facTrack').name, featured.find(id='facTrack').get('class'))
cards = featured.find_all(class_='fac-card')
print(f"Cards count: {len(cards)}")
for idx, c in enumerate(cards):
    img = c.find('img')
    cap = c.find('figcaption')
    print(f"  [{idx+1}] {cap.get_text() if cap else 'no cap'} -> img: {img.get('src') if img else 'no img'}")
