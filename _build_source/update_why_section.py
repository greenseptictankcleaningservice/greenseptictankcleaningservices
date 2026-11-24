with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

import re

new_why_section = """  <!-- ==================== WHY CHOOSE US ==================== -->
  <section class="sec" id="why">
    <div class="wrap">
      <div class="sec-head reveal">
        <span class="label">Why Choose Us</span>
        <h2>Why Hyderabad Property Owners<br /><em>Trust Our Service</em></h2>
        <p>We combine 20+ years of local field experience, modern high-power vacuum suction tankers, and certified eco-friendly disposal to solve critical sewage issues with zero mess and zero odor.</p>
      </div>

      <div class="why-g">
        <div class="why-col">
          <div class="why-card reveal">
            <div class="why-ic">
              <svg fill="none" height="22" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" viewBox="0 0 24 24" width="22">
                <path d="M12 3 4.5 6v5c0 4.8 3.2 8.5 7.5 10 4.3-1.5 7.5-5.2 7.5-10V6L12 3Z"></path>
                <path d="m9 12 2 2 4-4.5"></path>
              </svg>
            </div>
            <h3>20+ Years Field Experience</h3>
            <p>Seasoned local sanitation experts with two decades of service across Balapur, LB Nagar, and Hyderabad. We diagnose and resolve deep septic and drainage blockages quickly.</p>
          </div>

          <div class="why-card reveal">
            <div class="why-ic">
              <svg fill="none" height="22" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" viewBox="0 0 24 24" width="22">
                <circle cx="12" cy="8" r="5"></circle>
                <path d="m8.5 12.6-1.4 8.4 4.9-2.9 4.9 2.9-1.4-8.4"></path>
              </svg>
            </div>
            <h3>Heavy Vacuum Tanker Fleet</h3>
            <p>Equipped with commercial-grade vacuum pumps from 3,000L to 12,000L capacity, capable of lifting dense, compacted sludge from basement tanks and narrow residential alleys.</p>
          </div>

          <div class="why-card reveal">
            <div class="why-ic">
              <svg fill="none" height="22" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" viewBox="0 0 24 24" width="22">
                <path d="M12 3v3M12 18v3M3 12h3M18 12h3M5.6 5.6l2.1 2.1M16.3 16.3l2.1 2.1M5.6 18.4l2.1-2.1M16.3 7.7l2.1-2.1"></path>
                <circle cx="12" cy="12" r="3.2"></circle>
              </svg>
            </div>
            <h3>High-Pressure Jetting Systems</h3>
            <p>200+ bar hydro-jetters break down hardened grease, tree roots, scale, and stubborn debris inside underground lines, restoring 100% full flow capacity.</p>
          </div>
        </div>

        <figure class="why-img reveal" style="margin:0">
          <img alt="Green Septic Tank vacuum suction service truck in Hyderabad" src="images/why-service.webp" />
          <figcaption>Trusted by 15,000+ homes, societies &amp; businesses across Hyderabad</figcaption>
        </figure>

        <div class="why-col">
          <div class="why-card reveal">
            <div class="why-ic">
              <svg fill="none" height="22" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" viewBox="0 0 24 24" width="22">
                <circle cx="12" cy="12" r="9"></circle>
                <path d="M12 6v6l4 2"></path>
              </svg>
            </div>
            <h3>24/7 Rapid Emergency Response</h3>
            <p>Sewage overflow cannot wait. Our emergency teams operate 24 hours a day, 7 days a week, reaching your premises within 30 to 45 minutes anywhere in Hyderabad.</p>
          </div>

          <div class="why-card reveal">
            <div class="why-ic">
              <svg fill="none" height="22" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" viewBox="0 0 24 24" width="22">
                <path d="M10 3h4M10 3v6l-5 9.2A2 2 0 0 0 6.8 21h10.4a2 2 0 0 0 1.8-2.8L14 9V3"></path>
                <path d="M7.6 15h8.8"></path>
              </svg>
            </div>
            <h3>100% Authorized Eco-Disposal</h3>
            <p>We strictly discharge all collected waste at government-authorized municipal treatment plants in compliance with environmental standards. Zero illegal dumping.</p>
          </div>

          <div class="why-card reveal">
            <div class="why-ic">
              <svg fill="none" height="22" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" viewBox="0 0 24 24" width="22">
                <path d="M4 21h16M6 21V9l6-5 6 5v12M10 21v-6h4v6"></path>
              </svg>
            </div>
            <h3>Honest &amp; Transparent Rates</h3>
            <p>Transparent pricing quoted upfront based on tank size and site conditions. No hidden fees, no sudden extra costs after opening chamber covers.</p>
          </div>
        </div>
      </div>
    </div>
  </section>"""

# Replace the why section in index.html
updated_html = re.sub(r'<!-- ==================== WHY CHOOSE US ==================== -->[\s\S]*?</section>', new_why_section, html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(updated_html)

print("Updated why section in index.html successfully!")
