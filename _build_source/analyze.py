from bs4 import BeautifulSoup
import re
import json

print("=== PARSING SB FALL PROTECTION ===")
with open("sb_fall_protection.html", "r", encoding="utf-8") as f:
    sb_html = f.read()

soup_sb = BeautifulSoup(sb_html, "html.parser")
print("SB Title:", soup_sb.title.string if soup_sb.title else "No title")

# Check navigation links
nav_links = [(a.get_text(strip=True), a.get('href')) for a in soup_sb.find_all('a') if a.get('href')]
print("\nSB Nav/Links count:", len(nav_links))
unique_links = []
for text, href in nav_links:
    if href.startswith('/') or 'sbfallprotection' in href:
        if (text, href) not in unique_links:
            unique_links.append((text, href))
print("SB Internal Links:")
for text, href in unique_links[:25]:
    print(f"  '{text}' -> {href}")

# Check sections in SB
sections = soup_sb.find_all(['section', 'header', 'footer', 'main'])
print(f"\nSB Major tags count: {len(sections)}")
for i, s in enumerate(sections):
    classes = s.get('class', [])
    s_id = s.get('id', '')
    h = s.find(['h1', 'h2', 'h3'])
    h_text = h.get_text(strip=True) if h else "(no heading)"
    print(f"  [{i}] <{s.name} id='{s_id}' class='{' '.join(classes[:3])}'> Heading: {h_text[:60]}")

print("\n=== PARSING GREEN SEPTIC TANK ===")
with open("gst_septic-tank-cleaning-services.html", "r", encoding="utf-8") as f:
    gst_html = f.read()

soup_gst = BeautifulSoup(gst_html, "html.parser")
print("GST Title:", soup_gst.title.string if soup_gst.title else "No title")

# Look for images and logo
imgs = soup_gst.find_all('img')
print(f"\nGST Images count: {len(imgs)}")
for img in imgs:
    src = img.get('src')
    alt = img.get('alt', '')
    if src:
        print(f"  img: src='{src}' alt='{alt}'")

# Look for phone numbers, email, addresses
text_all = soup_gst.get_text(separator="\n")
phones = set(re.findall(r'(\+?91[\s-]?[6-9]\d{9}|\b[6-9]\d{9}\b|\b0?[48]\d{7,8}\b)', text_all))
emails = set(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text_all))
print("\nGST Phones:", phones)
print("GST Emails:", emails)

# Headings in GST
headings = soup_gst.find_all(['h1', 'h2', 'h3', 'h4'])
print("\nGST Headings:")
for h in headings:
    print(f"  <{h.name}>: {h.get_text(strip=True)}")

# Also check gst_index.html
with open("gst_index.html", "r", encoding="utf-8") as f:
    gst_idx_html = f.read()
soup_gst_idx = BeautifulSoup(gst_idx_html, "html.parser")
idx_headings = soup_gst_idx.find_all(['h1', 'h2', 'h3', 'h4'])
print("\nGST Index Headings:")
for h in idx_headings:
    print(f"  <{h.name}>: {h.get_text(strip=True)}")
