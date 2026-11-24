with open("sb_style.css", "r", encoding="utf-8") as f:
    css = f.read()

print("CSS length:", len(css))
# Check key selectors
import re
selectors = re.findall(r'([.#][\w-]+)\s*\{', css)
print("Unique selectors sample:", sorted(list(set(selectors)))[:50])

with open("sb_script.js", "r", encoding="utf-8") as f:
    js = f.read()

print("\nJS length:", len(js))
print("JS preview:")
print(js[:500])
