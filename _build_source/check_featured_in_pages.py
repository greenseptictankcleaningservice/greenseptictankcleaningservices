import os
from bs4 import BeautifulSoup

for f in ["index.html", "services.html", "about.html", "areas.html", "contact.html"]:
    with open(f, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file.read(), "html.parser")
    featured = soup.find('section', id='featured')
    print(f"{f}: has #featured? {featured is not None}")
