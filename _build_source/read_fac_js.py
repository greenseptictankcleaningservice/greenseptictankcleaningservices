with open("_build_source/sb_script_formatted.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if "facTrack" in line:
        start = max(0, idx - 5)
        end = min(len(lines), idx + 60)
        print("".join(lines[start:end]))
        break
