with open("js/script.js", "r", encoding="utf-8") as f:
    js = f.read()

gsap_code = """
  // ==========================================================================
  // GSAP SCROLLTRIGGER STAGGER FOR WHY CHOOSE US (TEXT CARDS ONLY)
  // ==========================================================================
  function initWhyCardsStagger() {
    if (typeof gsap === 'undefined') return;

    if (typeof ScrollTrigger !== 'undefined') {
      gsap.registerPlugin(ScrollTrigger);
    }

    // Select ONLY text cards (.why-card), NOT the center photo card (.why-img)
    var textCards = document.querySelectorAll('#why .why-card');
    if (!textCards.length) return;

    if (!isReducedMotion) {
      gsap.fromTo(
        textCards,
        {
          opacity: 0,
          y: 45,
          scale: 0.95
        },
        {
          opacity: 1,
          y: 0,
          scale: 1,
          duration: 0.75,
          ease: 'power2.out',
          stagger: 0.12, // Stagger effect across the text cards only
          scrollTrigger: {
            trigger: '#why .why-g',
            start: 'top 80%',
            toggleActions: 'play none none none',
            once: true
          }
        }
      );
    } else {
      gsap.set(textCards, { opacity: 1, y: 0, scale: 1 });
    }
  }

  initWhyCardsStagger();
"""

if "initWhyCardsStagger" not in js:
    last_idx = js.rfind("})();")
    if last_idx != -1:
        new_js = js[:last_idx] + gsap_code + "\n" + js[last_idx:]
    else:
        new_js = js + "\n" + gsap_code
    with open("js/script.js", "w", encoding="utf-8") as f:
        f.write(new_js)
    print("Added initWhyCardsStagger to js/script.js!")
else:
    print("js/script.js already has initWhyCardsStagger")
