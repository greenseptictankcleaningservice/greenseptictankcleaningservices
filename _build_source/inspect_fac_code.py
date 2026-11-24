import re

with open("css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

print("=== CSS FOR fac-track / fac-card ===")
for m in re.finditer(r'([^{}]*(?:fac-track|fac-card|fac-strip|fac-set)[^{}]*\{[^}]+\})', css):
    print(m.group(0))

with open("_build_source/sb_script_formatted.js", "r", encoding="utf-8") as f:
    js = f.read()

print("\n=== JS FOR facTrack / fac-track ===")
for line in js.splitlines():
    if any(k in line for k in ['facTrack', 'fac-track', 'fac-card', 'fac-strip', 'fac-set', 'fac_track']):
        print(" ", line.strip()[:140])
