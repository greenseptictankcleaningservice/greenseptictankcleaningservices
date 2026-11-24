from bs4 import BeautifulSoup

with open("gst_septic-tank-cleaning-services.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

# Get main content
content_div = soup.find('div', class_='service-detail') or soup.find('div', class_='content-side') or soup.find('main') or soup.body

# Let's print all h2, h3, h4, h5 and their following text
for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5']):
    text = tag.get_text(strip=True)
    if not text:
        continue
    print(f"\n[{tag.name.upper()}] {text}")
    # find next sibling paragraphs or lists
    curr = tag.next_sibling
    count = 0
    while curr and count < 5:
        if hasattr(curr, 'name'):
            if curr.name in ['h1', 'h2', 'h3', 'h4', 'h5']:
                break
            if curr.name in ['p', 'ul', 'div']:
                val = curr.get_text(separator=' ', strip=True)
                if val:
                    print(f"  -> {val[:200]}...")
                    count += 1
        curr = curr.next_sibling
