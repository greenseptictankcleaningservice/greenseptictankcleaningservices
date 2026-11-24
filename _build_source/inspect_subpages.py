from bs4 import BeautifulSoup

for page in ["sb_products.html", "sb_about.html", "sb_contact.html", "sb_markets.html"]:
    with open(page, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    print(f"\n=== {page} ===")
    print("Title:", soup.title.string if soup.title else "")
    h1 = soup.find('h1')
    print("H1:", h1.get_text(strip=True) if h1 else "")
    page_hero = soup.find(class_=lambda c: c and 'page-hero' in c)
    if page_hero:
        print("Page Hero classes:", page_hero.get('class'))
    sections = soup.find_all('section')
    print(f"Sections count: {len(sections)}")
    for s in sections[:4]:
        sh = s.find(['h2', 'h3'])
        print(f"  section id='{s.get('id')}' class='{' '.join(s.get('class', []))}': {sh.get_text(strip=True) if sh else ''}")
