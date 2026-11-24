from bs4 import BeautifulSoup
import json

with open("sb_fall_protection.html", "r", encoding="utf-8") as f:
    sb_soup = BeautifulSoup(f.read(), "html.parser")

with open("gst_septic-tank-cleaning-services.html", "r", encoding="utf-8") as f:
    gst_service_soup = BeautifulSoup(f.read(), "html.parser")

with open("gst_index.html", "r", encoding="utf-8") as f:
    gst_index_soup = BeautifulSoup(f.read(), "html.parser")

print("=== 1. SB FALL PROTECTION NAV & TOPBAR ===")
nav = sb_soup.find('nav')
if nav:
    print("Nav outer HTML:")
    print(nav.prettify()[:1500])

print("\n=== 2. SB HERO SECTION ===")
hero = sb_soup.find('header', class_='hero')
if hero:
    print(hero.prettify()[:1500])

print("\n=== 3. SB STATS SECTION ===")
stats = sb_soup.find('section', class_='stats')
if stats:
    print(stats.prettify()[:1500])

print("\n=== 4. SB SERVICES / PRODUCTS ===")
products = sb_soup.find('section', id='products')
if products:
    print(products.prettify()[:1500])

print("\n=== 5. SB WHY CHOOSE US ===")
why = sb_soup.find('section', id='why')
if why:
    print(why.prettify()[:1500])

print("\n=== 6. SB WORKS / PROCESS ===")
works = sb_soup.find('section', id='works')
if works:
    print(works.prettify()[:1500])

print("\n=== 7. SB TESTIMONIALS ===")
testi = sb_soup.find('section', id='testimonials')
if testi:
    print(testi.prettify()[:1500])

print("\n=== 8. SB MARKETS / SERVICE AREAS ===")
markets = sb_soup.find('section', id='markets')
if markets:
    print(markets.prettify()[:1500])

print("\n=== 9. SB ABOUT ===")
about = sb_soup.find('section', id='about')
if about:
    print(about.prettify()[:1500])

print("\n=== 10. SB CONTACT ===")
contact = sb_soup.find('section', id='contact')
if contact:
    print(contact.prettify()[:1500])

print("\n=== 11. SB FAQS ===")
faqs = sb_soup.find('section', id='faqs')
if faqs:
    print(faqs.prettify()[:1500])

print("\n=== 12. SB FOOTER ===")
footer = sb_soup.find('footer')
if footer:
    print(footer.prettify()[:1500])
