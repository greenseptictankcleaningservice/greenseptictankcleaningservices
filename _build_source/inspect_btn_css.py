with open("css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Let's inspect the existing .btn rule
import re
btn_rule = re.search(r'\.btn\{[^}]+\}', css)
if btn_rule:
    print("Existing .btn rule:")
    print(btn_rule.group(0))

orange_rule = re.search(r'\.btn-orange\{[^}]+\}', css)
if orange_rule:
    print("\nExisting .btn-orange rule:")
    print(orange_rule.group(0))
