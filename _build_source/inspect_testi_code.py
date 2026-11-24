import re

with open("css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

print("=== CSS FOR TESTIMONIALS ===")
for m in re.finditer(r'([^{}]*(?:testi|t-card|t-photo|t-content|t-rating|t-quote|t-who|t-avatars|t-nav|t-arrow|t-av|deco-l|deco-r)[^{}]*\{[^}]+\})', css):
    print(m.group(0))

with open("_build_source/sb_script_formatted.js", "r", encoding="utf-8") as f:
    js = f.read()

print("\n=== JS FOR TESTIMONIALS ===")
for idx, line in enumerate(js.splitlines()):
    if any(k in line for k in ['tCard', 'tPhoto', 'tQuote', 'tName', 'tRole', 'tAvatars', 'tPrev', 'tNext']):
        print(f"[{idx}] {line.strip()[:140]}")
