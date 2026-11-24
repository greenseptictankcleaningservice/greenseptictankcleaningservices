from bs4 import BeautifulSoup

with open("_build_source/sb_fall_protection.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

testi = soup.find('section', id='testimonials')
if testi:
    print("=== SB FALL PROTECTION #testimonials SECTION ===")
    print(testi.prettify())
else:
    print("Could not find section with id='testimonials'")

# Also inspect any other element mentioning 'testimonial'
for s in soup.find_all(class_=lambda c: c and 'testi' in c):
    print(f"\nElement with class 'testi': <{s.name} id='{s.get('id')}' class='{s.get('class')}'>")
