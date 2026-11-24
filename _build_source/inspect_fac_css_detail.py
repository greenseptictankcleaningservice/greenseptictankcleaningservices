with open("css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

import re
matches = re.findall(r'([^{}]*fac-(?:track|strip|set|card)[^{}]*\{[^}]+\})', css)
print(f"Found {len(matches)} rules:")
for m in matches:
    print(" ", m)
