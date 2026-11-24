from bs4 import BeautifulSoup

with open("index.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

nav = soup.find('nav')
print("=== NAV BUTTONS ===")
for b in nav.find_all(class_='btn'):
    print(b.prettify())

hero = soup.find('header', class_='hero')
print("\n=== HERO BUTTONS ===")
for b in hero.find_all(class_='btn'):
    print(b.prettify())
