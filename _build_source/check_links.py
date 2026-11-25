import os
from bs4 import BeautifulSoup

files = [
    "index.html", "services.html", "about.html", "areas.html", "contact.html", "blog.html",
    "privacy-policy.html", "terms-and-conditions.html", "cookies-policy.html", "disclaimer.html"
]

broken = 0
for f in files:
    with open(f, "r", encoding="utf-8") as fp:
        soup = BeautifulSoup(fp.read(), "html.parser")
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        if href.startswith(("http://", "https://", "tel:", "mailto:", "#", "javascript:")):
            continue
        target_file = href.split("#")[0]
        if target_file and not os.path.exists(target_file):
            print(f"BROKEN LINK in {f}: {href}")
            broken += 1

if broken == 0:
    print("ALL INTERNAL LINKS ARE 100% VALID ACROSS ALL 10 PAGES!")
else:
    print(f"Found {broken} broken links!")
