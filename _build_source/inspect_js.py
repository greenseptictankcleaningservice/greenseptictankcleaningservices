with open("sb_script.js", "r", encoding="utf-8") as f:
    js = f.read()

# simple formatting
formatted = js.replace(';', ';\n').replace('{', '{\n').replace('}', '\n}\n')
with open("sb_script_formatted.js", "w", encoding="utf-8") as f_out:
    f_out.write(formatted)

print("Formatted JS preview (first 1200 chars):")
print(formatted[:1200])
