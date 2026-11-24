with open("sb_script_formatted.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
# Search for functions or listeners
for idx, line in enumerate(lines):
    if any(k in line for k in ['addEventListener', 'IntersectionObserver', 'querySelector', 'querySelectorAll', 'setInterval', 'function', 'class']):
        print(f"[{idx}] {line.strip()[:100]}")
