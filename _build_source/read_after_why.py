with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

why_sec = soup.find('section', id='why')
if why_sec:
    nxt = why_sec.find_next_sibling('section')
    if nxt:
        print("Next section tag and id:", nxt.name, nxt.get('id'), nxt.get('class'))
        print(nxt.prettify()[:500])
