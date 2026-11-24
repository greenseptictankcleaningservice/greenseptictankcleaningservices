from bs4 import BeautifulSoup
import re
import json

with open("sb_fall_protection.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

print("=== SB FALL PROTECTION INSPECTION ===")
# Meta tags
for meta in soup.find_all('meta'):
    if meta.get('name') or meta.get('property'):
        print("Meta:", meta.get('name') or meta.get('property'), "->", meta.get('content'))

# Fonts and stylesheets
print("\nFonts and Links:")
for link in soup.find_all('link'):
    print("Link:", link.get('rel'), link.get('href'))

# Navigation / Header
header = soup.find('header')
if header:
    print("\n--- Header / Nav HTML (first 1000 chars) ---")
    print(str(header)[:1000])

# Examine all sections
sections = soup.find_all('section')
for idx, sec in enumerate(sections):
    sec_id = sec.get('id', '')
    sec_cls = ' '.join(sec.get('class', []))
    h = sec.find(['h1', 'h2', 'h3'])
    h_text = h.get_text(separator=' ', strip=True) if h else ""
    p = sec.find('p')
    p_text = p.get_text(separator=' ', strip=True) if p else ""
    print(f"\n[Section {idx}] id='{sec_id}' class='{sec_cls}'")
    print(f"  Heading: {h_text}")
    print(f"  Snippet: {p_text[:120]}")

# Look at CSS variables or key styling
with open("sb_style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Find root variables
root_vars = re.findall(r'--[\w-]+:\s*[^;]+;', css)
print(f"\nCSS Root variables ({len(root_vars)} found):")
for v in root_vars[:30]:
    print(" ", v)
