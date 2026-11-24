with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

import re

# 1. Update script tags at the bottom
if "gsap.min.js" not in html:
    html = html.replace(
        '<script src="js/script.js"></script>',
        '<script src="js/gsap.min.js"></script>\n  <script src="js/ScrollTrigger.min.js"></script>\n  <script src="js/script.js"></script>'
    )
    print("Updated script tags in index.html")

# 2. In #why, remove 'reveal' only from .why-card, leaving why-img reveal intact
# Find the why section
why_match = re.search(r'(<section class="sec" id="why">[\s\S]*?</section>)', html)
if why_match:
    why_block = why_match.group(1)
    # Replace class="why-card reveal" with class="why-card" inside why_block
    new_why_block = why_block.replace('class="why-card reveal"', 'class="why-card"')
    html = html.replace(why_block, new_why_block)
    print("Removed 'reveal' from text cards in #why, kept on why-img!")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html successfully!")
