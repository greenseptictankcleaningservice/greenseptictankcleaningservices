with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

why_sec = soup.find('section', id='why')
if why_sec:
    print(why_sec.prettify()[:1500])
