import os
from bs4 import BeautifulSoup

for f in ["index.html", "services.html", "about.html", "areas.html", "contact.html"]:
    with open(f, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file.read(), "html.parser")
    why = soup.find('section', id='why')
    print(f"{f}: has #why? {why is not None}")
