from bs4 import BeautifulSoup

with open("_build_source/sb_fall_protection.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

why = soup.find('section', id='why')
if why:
    print("=== SB FALL PROTECTION #why SECTION ===")
    print(why.prettify())
else:
    print("Could not find section with id='why'")

# Also check next sibling section
if why:
    nxt = why.find_next_sibling('section')
    if nxt:
        print("\n=== NEXT SIBLING SECTION ===")
        print(nxt.prettify()[:1000])
