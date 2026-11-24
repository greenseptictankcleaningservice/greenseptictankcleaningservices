from bs4 import BeautifulSoup
import re

pages = ["index.html", "services.html", "about.html", "areas.html", "contact.html"]

for p in pages:
    with open(p, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")
    btns = soup.find_all(lambda tag: tag.name in ['a', 'button'] and ('btn' in tag.get('class', [])))

    count = 0
    for btn in btns:
        # Check if already has .circle
        if not btn.find(class_='circle'):
            # Create circle element
            circle = soup.new_tag("span", **{"class": "circle"})
            # Check existing children
            # If button contains text directly without span, wrap text in span
            new_contents = [circle]
            for child in list(btn.contents):
                if isinstance(child, str):
                    t = child.strip()
                    if t:
                        sp = soup.new_tag("span")
                        sp.string = t
                        new_contents.append(sp)
                else:
                    new_contents.append(child)
            btn.clear()
            for c in new_contents:
                btn.append(c)
            count += 1

    with open(p, "w", encoding="utf-8") as f:
        f.write(str(soup))

    print(f"Updated {p}: {count} buttons updated with .circle")
