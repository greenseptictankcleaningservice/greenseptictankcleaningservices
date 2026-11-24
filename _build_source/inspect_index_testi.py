from bs4 import BeautifulSoup

with open("index.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

testi = soup.find('section', id='testimonials')
if testi:
    print(testi.prettify()[:1500])
