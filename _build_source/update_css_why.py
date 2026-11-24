with open("css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

rule = """
/* GSAP Stagger optimization for #why .why-card */
#why .why-card {
  will-change: transform, opacity;
}
"""

if "GSAP Stagger optimization for #why .why-card" not in css:
    css += "\n" + rule
    with open("css/style.css", "w", encoding="utf-8") as f:
        f.write(css)
    print("Added will-change optimization to css/style.css")
else:
    print("Already in css/style.css")
