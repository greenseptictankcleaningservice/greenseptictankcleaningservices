with open("css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

import re
selectors = ['.fc-item', '.f-socials', '.f-bar', '.f-mark-wrap', '.foot-grid', '.f-tools']
for s in selectors:
    matches = re.findall(rf'{re.escape(s)}[^{{]*\{{[^}}]+\}}', css)
    print(f"\nSelector {s} ({len(matches)} matches):")
    for m in matches[:2]:
        print(" ", m[:150])
