from bs4 import BeautifulSoup

with open("_build_source/sb_fall_protection.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

cert_strip = soup.find(class_='cert-strip')
if cert_strip:
    parent_sec = cert_strip.find_parent('section')
    print("cert-strip parent section id/class:", parent_sec.get('id') if parent_sec else None, parent_sec.get('class') if parent_sec else None)
    print("cert-strip HTML:")
    print(cert_strip.prettify()[:600])
else:
    print("cert-strip not found in SB")
