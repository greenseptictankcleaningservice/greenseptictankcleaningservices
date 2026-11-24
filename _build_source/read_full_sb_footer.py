from bs4 import BeautifulSoup

with open("_build_source/sb_markets.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

footer = soup.find('footer')
print(footer.prettify())
