from bs4 import BeautifulSoup

with open("index.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

featured = soup.find('section', id='featured')
if featured:
    print(featured.prettify()[:1500])
