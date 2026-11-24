import re

# 1. Update index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

new_featured_html = """  <!-- ==================== MODERN FLEET & CAPABILITIES ==================== -->
  <section class="sec" id="featured" style="padding-top:12px">
    <div class="wrap">
      <div class="sec-head left reveal">
        <span class="label">Inside Our Operations</span>
        <h2>See How We Clean: <em>Heavy-Duty Fleet &amp; Tech</em></h2>
        <p>A look at our specialized high-capacity vacuum suction tankers, high-pressure hydro-jetters, and deep sludge extraction machinery operating across Greater Hyderabad.</p>
      </div>
    </div>
    <div class="reveal">
      <div class="fac-track" id="facTrack">
        <figure class="fac-card">
          <img alt="High Capacity Heavy Duty Vacuum Suction Tanker" src="images/main-slider/fast-efficient-septic-services.webp" />
          <figcaption>12,000L Heavy Vacuum Suction Tanker</figcaption>
        </figure>

        <figure class="fac-card">
          <img alt="Deep Septic Tank Sludge Vacuum Extraction" src="images/resource/notch-septic-tank-cleaning-services.webp" />
          <figcaption>Deep Sludge Vacuum Extraction</figcaption>
        </figure>

        <figure class="fac-card">
          <img alt="High Pressure Sewer Hydro-Jetting Machine" src="images/resource/green-septic-solutions.webp" />
          <figcaption>200+ Bar Sewer Hydro-Jetting</figcaption>
        </figure>

        <figure class="fac-card">
          <img alt="Commercial &amp; Gated Community Sanitation Tanker" src="images/background/clean-safe-septic-services.webp" />
          <figcaption>Rapid Dispatch Across Greater Hyderabad</figcaption>
        </figure>

        <figure class="fac-card">
          <img alt="Sewage Treatment Plant Maintenance &amp; Cleaning" src="images/resource/stp-plant-cleaning.webp" />
          <figcaption>STP Plant Desludging &amp; Maintenance</figcaption>
        </figure>

        <figure class="fac-card">
          <img alt="Eco-Friendly Municipal Sludge Transport &amp; Disposal" src="images/main-slider/eco-friendly-septic-services.webp" />
          <figcaption>100% Authorized Municipal Eco-Disposal</figcaption>
        </figure>
      </div>
    </div>
  </section>"""

# Replace existing #featured section in index.html
updated_html = re.sub(r'<!-- ==================== MODERN FLEET & CAPABILITIES ==================== -->[\s\S]*?</section>', new_featured_html, html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(updated_html)

print("Updated #featured section in index.html!")

# 2. Update js/script.js Section 10
with open("js/script.js", "r", encoding="utf-8") as f:
    js = f.read()

# Replace the existing section 10 block with the authentic facTrack engine
old_sec_10_pattern = r'// 10\.\s*Fleet & Facility Auto-scroll and Drag[\s\S]*?(?=// 11\.)'

new_sec_10 = """// 10. Modern Fleet & Equipment Infinite Marquee Track (#facTrack)
  var facTrack = document.getElementById("facTrack");
  if (facTrack) {
    var rawCards = Array.prototype.slice.call(facTrack.children);
    var strip = document.createElement("div");
    strip.className = "fac-strip";

    // Create 2 identical sets for seamless continuous marquee loop
    for (var setIdx = 0; setIdx < 2; setIdx++) {
      var set = document.createElement("div");
      set.className = "fac-set";
      rawCards.forEach(function (card) {
        set.appendChild(setIdx ? card.cloneNode(true) : card);
      });
      strip.appendChild(set);
    }
    facTrack.appendChild(strip);

    var speed = isReducedMotion ? 15 : 75;
    function updateDur() {
      var halfWidth = strip.scrollWidth / 2;
      if (halfWidth > 0) {
        strip.style.setProperty("--fac-dur", (halfWidth / speed) + "s");
      }
    }
    updateDur();
    window.addEventListener("resize", updateDur);
    if (window.ResizeObserver) {
      new ResizeObserver(updateDur).observe(strip);
    }

    var isPausedTimer;
    function pauseMarquee() {
      facTrack.classList.add("is-paused");
      clearTimeout(isPausedTimer);
    }
    function resumeMarquee(delay) {
      clearTimeout(isPausedTimer);
      isPausedTimer = setTimeout(function () {
        facTrack.classList.remove("is-paused");
      }, delay || 600);
    }

    // Hover pause
    facTrack.addEventListener("mouseenter", pauseMarquee);
    facTrack.addEventListener("mouseleave", function () { resumeMarquee(300); });

    // Drag / Touch interaction
    var isDragging = false, startX = 0, scrollStart = 0;
    facTrack.addEventListener("mousedown", function (e) {
      isDragging = true;
      startX = e.pageX;
      scrollStart = facTrack.scrollLeft;
      facTrack.classList.add("dragging");
      pauseMarquee();
      e.preventDefault();
    });
    window.addEventListener("mousemove", function (e) {
      if (!isDragging) return;
      facTrack.scrollLeft = scrollStart - (e.pageX - startX);
    });
    window.addEventListener("mouseup", function () {
      if (isDragging) {
        isDragging = false;
        facTrack.classList.remove("dragging");
        resumeMarquee(800);
      }
    });

    facTrack.addEventListener("touchstart", pauseMarquee, { passive: true });
    facTrack.addEventListener("touchend", function () { resumeMarquee(2000); }, { passive: true });
    facTrack.addEventListener("touchcancel", function () { resumeMarquee(400); }, { passive: true });
  }

  """

updated_js = re.sub(old_sec_10_pattern, new_sec_10, js)

with open("js/script.js", "w", encoding="utf-8") as f:
    f.write(updated_js)

print("Updated Section 10 in js/script.js!")
