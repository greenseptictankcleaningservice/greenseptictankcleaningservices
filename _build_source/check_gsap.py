import os

for f in ["index.html", "js/script.js", "css/style.css"]:
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
    print(f"{f}: has gsap? {'gsap' in content.lower()}")
