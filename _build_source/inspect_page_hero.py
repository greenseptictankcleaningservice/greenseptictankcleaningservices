from bs4 import BeautifulSoup

with open("sb_products.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

page_hero = soup.find(class_='page-hero')
if page_hero:
    print("Page hero HTML:")
    print(page_hero.prettify()[:1200])
