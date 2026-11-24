with open("css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

import re
f_tools_match = re.search(r'\.f-tools[^}]+\}', css)
if f_tools_match:
    print("f-tools CSS rule:")
    print(f_tools_match.group(0))

# Also search any related rules like .f-tools img
for m in re.finditer(r'\.f-tools[^{]*\{[^}]+\}', css):
    print(m.group(0))
