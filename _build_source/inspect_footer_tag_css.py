with open("css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

import re
footer_matches = re.findall(r'footer[^{]*\{[^}]+\}', css)
for m in footer_matches:
    print(m)
