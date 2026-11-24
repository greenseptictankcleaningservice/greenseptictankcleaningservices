with open("css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

import re
marquee_matches = re.findall(r'@keyframes fac-marquee[^}]+\}[^}]*\}', css)
print("fac-marquee matches:", len(marquee_matches))
for m in marquee_matches:
    print(m)
