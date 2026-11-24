with open("css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

circle_css = """
/* ==========================================================================
   MAGNETIC CIRCLE BUTTON HOVER EFFECT
   ========================================================================== */

.btn {
  position: relative !important;
  overflow: hidden !important;
  cursor: pointer;
  z-index: 1;
}

/* Ensure all text, icons, and SVGs inside button stay above the circle */
.btn > *:not(.circle) {
  position: relative;
  z-index: 2;
  transition: color 0.25s ease, stroke 0.25s ease;
}

/* Circle element matching the specified effect */
.btn .circle {
  position: absolute;
  width: 220%;
  aspect-ratio: 1;
  border-radius: 50%;
  transform: translate(-50%, -50%);
  transform-origin: 0% 0%;
  scale: 0;
  transition: scale 0.25s ease-in-out, top 0.5s ease;
  pointer-events: none;
  z-index: 1;
}

/* On hover, circle expands smoothly from cursor location */
.btn:hover .circle {
  scale: 1;
  transition: scale 0.25s ease-in-out;
}

/* Button variants with matching color schemes */
/* 1. Green Primary Buttons (.btn-orange) */
.btn-orange .circle {
  background-color: var(--ink); /* #131312 */
}
.btn-orange:hover {
  color: #ffffff !important;
}

/* 2. White Buttons (.btn-white) */
.btn-white .circle {
  background-color: var(--orange); /* #16a34a */
}
.btn-white:hover {
  color: #ffffff !important;
}
.btn-white:hover svg {
  stroke: #ffffff !important;
  color: #ffffff !important;
}

/* 3. WhatsApp Buttons (.btn-whatsapp) */
.btn-whatsapp .circle {
  background-color: #0f5132; /* Deep WhatsApp Dark Green */
}
.btn-whatsapp:hover {
  color: #ffffff !important;
}

/* 4. Outlined Line Buttons (.btn-line) */
.btn-line .circle {
  background-color: var(--orange); /* #16a34a */
}
.btn-line:hover {
  color: #ffffff !important;
  border-color: var(--orange) !important;
}

/* 5. Dark Ink Buttons (.btn-ink) */
.btn-ink .circle {
  background-color: var(--orange);
}
.btn-ink:hover {
  color: #ffffff !important;
}
"""

if "MAGNETIC CIRCLE BUTTON HOVER EFFECT" not in css:
    new_css = css + "\n" + circle_css
    with open("css/style.css", "w", encoding="utf-8") as f:
        f.write(new_css)
    print("Added circle button CSS to css/style.css!")
else:
    print("CSS already contains circle button rules.")
