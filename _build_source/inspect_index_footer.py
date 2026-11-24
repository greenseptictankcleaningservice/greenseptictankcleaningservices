with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if "<footer" in line or "foot-grid" in line or "fc-item" in line or "f-tools" in line:
        print(f"Line {idx+1}: {line.strip()[:100]}")
