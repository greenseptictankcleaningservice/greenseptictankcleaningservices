with open("js/script.js", "r", encoding="utf-8") as f:
    js = f.read()

print("Length of js/script.js:", len(js))
print("End of js/script.js:")
print(js[-600:])
