with open("css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

import re
selectors = ['.why-g', '.why-col', '.why-card', '.why-ic', '.why-img']
for s in selectors:
    matches = re.findall(rf'{re.escape(s)}[^{{]*\{{[^}}]+\}}', css)
    print(f"\n{s}:")
    for m in matches:
        print(" ", m)
