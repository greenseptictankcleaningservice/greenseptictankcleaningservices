from bs4 import BeautifulSoup
import re

new_footer_html = """  <footer>
    <div class="wrap">
      <div aria-hidden="true" class="f-tools">
        <img alt="Septic suction hose" src="images/deco-suction-hose.webp" />
        <img alt="High-pressure hydro-jetting nozzle" src="images/deco-jet-nozzle.webp" />
        <img alt="Sludge suction wand and valve" src="images/deco-sludge-pipe.webp" />
      </div>
      <div class="foot-grid">
        <div class="f-col">
          <h4>Quick Links</h4>
          <a href="about.html">About us</a>
          <a href="areas.html">Service Areas</a>
          <a href="index.html#works">How it Works</a>
          <a href="index.html#testimonials">Testimonials</a>
          <a href="services.html">All Services</a>
          <a href="contact.html">Contact Us</a>
          <a href="index.html#faqs">FAQs</a>
        </div>
        <div class="f-col">
          <h4>Services</h4>
          <a href="services.html">Residential Septic</a>
          <a href="services.html">Commercial Cleaning</a>
          <a href="services.html">STP Plant Cleaning</a>
          <a href="services.html">Sludge Suction</a>
          <a href="services.html">Labour Camp Tanks</a>
          <a href="services.html">Industrial Solutions</a>
          <a href="services.html">Hospital Sanitation</a>
          <a href="services.html">Drainage Unblocking</a>
        </div>
        <div class="f-col">
          <h4>Company</h4>
          <a href="about.html">About Green Septic</a>
          <a href="areas.html">Hyderabad Localities</a>
          <a href="contact.html">24/7 Emergency Dispatch</a>
          <a href="services.html">Eco Sanitation Norms</a>
          <a href="contact.html">Request Free Quote</a>
        </div>
        <div>
          <div class="fc-item">
            <span class="fc-ic">
              <svg fill="none" height="22" stroke="currentColor" stroke-linecap="round" stroke-width="1.8" viewBox="0 0 24 24" width="22">
                <path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2Z"></path>
              </svg>
            </span>
            <div>
              <b>Phone Number</b>
              <span>+91 94405 14057<br />+91 9440 514 057</span>
            </div>
          </div>
          <div class="fc-item">
            <span class="fc-ic">
              <svg fill="none" height="22" stroke="currentColor" stroke-linecap="round" stroke-width="1.8" viewBox="0 0 24 24" width="22">
                <rect height="14" rx="2" width="18" x="3" y="5"></rect>
                <path d="m3 7 9 6 9-6"></path>
              </svg>
            </span>
            <div>
              <b>Email Address</b>
              <span>greenseptictankcleaningservices@gmail.com</span>
            </div>
          </div>
        </div>
        <div>
          <div class="fc-item">
            <span class="fc-ic">
              <svg fill="none" height="22" stroke="currentColor" stroke-linecap="round" stroke-width="1.8" viewBox="0 0 24 24" width="22">
                <path d="M12 21s-7-5.6-7-11a7 7 0 0 1 14 0c0 5.4-7 11-7 11Z"></path>
                <circle cx="12" cy="10" r="2.5"></circle>
              </svg>
            </span>
            <div>
              <b>Physical Address</b>
              <span>45-591NP, Maruthi Nagar, Badangpet Village, Balapur Mandal, Ranga Reddy, Hyderabad — 500058, Telangana, India</span>
            </div>
          </div>
          <div class="f-socials">
            <a aria-label="WhatsApp" href="https://wa.me/919440514057?text=Hello%20Green%20Septic%20Tank%20Cleaning" rel="noopener" target="_blank">
              <svg fill="currentColor" height="18" viewBox="0 0 24 24" width="18"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"></path></svg>
            </a>
            <a aria-label="Phone" href="tel:+919440514057">
              <svg fill="none" height="18" stroke="currentColor" stroke-linecap="round" stroke-width="1.8" viewBox="0 0 24 24" width="18"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2Z"></path></svg>
            </a>
            <a aria-label="Location" href="https://maps.google.com/?q=Badangpet+Balapur+Hyderabad" rel="noopener" target="_blank">
              <svg fill="none" height="18" stroke="currentColor" stroke-linecap="round" stroke-width="1.8" viewBox="0 0 24 24" width="18"><path d="M12 21s-7-5.6-7-11a7 7 0 0 1 14 0c0 5.4-7 11-7 11Z"></path><circle cx="12" cy="10" r="2.5"></circle></svg>
            </a>
          </div>
        </div>
      </div>
      <div class="f-bar">
        <span>© 2026 Green Septic Tank Cleaning Services. All rights reserved.</span>
        <span>20+ Years Field Experience · Municipal Eco-Disposal · Hyderabad, Telangana</span>
      </div>
      <div class="f-mark-wrap">
        <svg aria-hidden="true" class="f-mark" focusable="false" role="img" viewBox="0 0 1000 124">
          <defs>
            <linearGradient id="fMarkFade" x1="0" x2="0" y1="0" y2="1">
              <stop offset="10%" stop-color="#ffffff" stop-opacity="0.95"></stop>
              <stop offset="72%" stop-color="#ffffff" stop-opacity="0.34"></stop>
              <stop offset="100%" stop-color="#ffffff" stop-opacity="0"></stop>
            </linearGradient>
          </defs>
          <text fill="url(#fMarkFade)" font-size="94" lengthAdjust="spacingAndGlyphs" letter-spacing="-2" text-anchor="middle" textLength="984" x="500" y="101">
            Green Septic Tank
          </text>
        </svg>
      </div>
    </div>
  </footer>"""

pages = ["index.html", "services.html", "about.html", "areas.html", "contact.html"]

for p in pages:
    with open(p, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace the existing <footer>...</footer> block
    updated = re.sub(r'<footer>[\s\S]*?</footer>', new_footer_html, content)
    
    with open(p, "w", encoding="utf-8") as f:
        f.write(updated)
    
    print(f"Updated footer in {p}")
