from bs4 import BeautifulSoup

with open("_build_source/sb_fall_protection.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

featured = soup.find('section', id='featured')
if featured:
    print("=== SB FALL PROTECTION #featured (INSIDE THE FACTORY) SECTION ===")
    print(featured.prettify())
else:
    print("Could not find section with id='featured'")

# Also search for any section mentioning 'factory' or 'made'
for s in soup.find_all('section'):
    txt = s.get_text()
    if 'factory' in txt.lower() or 'inside' in txt.lower() or 'gear is made' in txt.lower():
        print(f"\nSection with match id='{s.get('id')}', class='{s.get('class')}':")
        print(s.prettify()[:1000])
