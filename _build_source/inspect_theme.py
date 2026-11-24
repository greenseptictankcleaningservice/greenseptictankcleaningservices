with open("sb_style.css", "r", encoding="utf-8") as f:
    css = f.read()

import re
# Find all occurrences of #fe5922 or #e8480f or orange
oranges = set(re.findall(r'#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3}|rgb\([^)]+\)|rgba\([^)]+\)', css))
color_vars = re.findall(r'(--[\w-]+:\s*[^;]+;)', css)
print("Color vars in CSS:")
for cv in color_vars:
    print(" ", cv)

# Check button classes
btns = re.findall(r'(\.btn[a-zA-Z0-9-_]*)\s*\{', css)
print("Button classes:", set(btns))

# Check badges, cards, layout
cards = re.findall(r'(\.[a-zA-Z0-9-_]*card[a-zA-Z0-9-_]*)\s*\{', css)
print("Card classes:", set(cards))
