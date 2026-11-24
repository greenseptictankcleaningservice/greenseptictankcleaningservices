with open("js/script.js", "r", encoding="utf-8") as f:
    js = f.read()

import re
print("facTrack in js/script.js:", "facTrack" in js)
print("fac-track in js/script.js:", "fac-track" in js)
print("fac-strip in js/script.js:", "fac-strip" in js)

# Print lines with fac
for line in js.splitlines():
    if "fac" in line.lower():
        print(" ", line.strip()[:100])
