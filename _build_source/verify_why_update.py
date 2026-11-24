from bs4 import BeautifulSoup

with open("index.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

why = soup.find('section', id='why')
print("=== UPDATED #why SECTION ===")
print("Cards count in why:", len(why.find_all(class_='why-card')))
print("Images count in why:", len(why.find_all('img')))
print("Figure:", why.find('figure').prettify() if why.find('figure') else "None")
for idx, c in enumerate(why.find_all(class_='why-card')):
    h3 = c.find('h3')
    print(f"  Card [{idx+1}]: {h3.get_text() if h3 else 'no h3'}")
