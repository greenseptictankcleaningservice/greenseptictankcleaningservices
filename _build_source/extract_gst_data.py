from bs4 import BeautifulSoup
import json
import re

with open("gst_septic-tank-cleaning-services.html", "r", encoding="utf-8") as f:
    soup_s = BeautifulSoup(f.read(), "html.parser")

with open("gst_index.html", "r", encoding="utf-8") as f:
    soup_i = BeautifulSoup(f.read(), "html.parser")

data = {}

# Services list from sidebar / menu
services = []
for a in soup_s.find_all('a'):
    href = a.get('href', '')
    text = a.get_text(strip=True)
    if 'cleaning' in href or 'service' in href or 'septic' in href or 'stp' in href:
        if text and len(text) > 3 and text not in services:
            services.append(text)
data['services_nav'] = services

# All paragraphs and sections in service page
sections = []
for sec in soup_s.find_all(['section', 'div'], class_=re.compile(r'service|about|process|faq|content|detail', re.I)):
    h = sec.find(['h1', 'h2', 'h3', 'h4', 'h5'])
    if h:
        title = h.get_text(strip=True)
        ps = [p.get_text(strip=True) for p in sec.find_all('p') if p.get_text(strip=True)]
        lis = [li.get_text(strip=True) for li in sec.find_all('li') if li.get_text(strip=True)]
        sections.append({
            'title': title,
            'paragraphs': ps[:4],
            'bullets': lis[:8]
        })
data['service_page_sections'] = sections

# FAQs
faqs = []
faq_blocks = soup_s.find_all(class_=re.compile(r'accordion|faq', re.I))
for b in faq_blocks:
    for btn in b.find_all(['button', 'h5', 'h4', 'div'], class_=re.compile(r'acc-btn|question|title', re.I)):
        q = btn.get_text(strip=True)
        # find sibling or next content
        nxt = btn.find_next(class_=re.compile(r'acc-content|answer|content', re.I))
        a = nxt.get_text(strip=True) if nxt else ""
        if q and a:
            faqs.append({'q': q, 'a': a})
data['faqs'] = faqs

# Extract from Index page
index_sections = []
for sec in soup_i.find_all('section'):
    h = sec.find(['h1', 'h2', 'h3', 'h4'])
    if h:
        title = h.get_text(strip=True)
        ps = [p.get_text(strip=True) for p in sec.find_all('p') if p.get_text(strip=True)]
        lis = [li.get_text(strip=True) for li in sec.find_all('li') if li.get_text(strip=True)]
        index_sections.append({
            'title': title,
            'paragraphs': ps[:4],
            'bullets': lis[:8]
        })
data['index_sections'] = index_sections

with open("gst_extracted_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Extracted data saved to gst_extracted_data.json")
print("Services:", services)
print(f"Service sections count: {len(sections)}")
print(f"Index sections count: {len(index_sections)}")
print(f"FAQs count: {len(faqs)}")
