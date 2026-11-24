import os

# Common header navigation template
def get_nav(active_page=""):
    return f"""
  <nav class="scrolled">
    <div class="wrap nav-in">
      <a class="brand" href="index.html" aria-label="Green Septic Tank Cleaning Services">
        <img src="images/logo.webp" alt="Green Septic Tank Cleaning Services Logo" class="brand-logo" height="46" width="160" />
      </a>
      <div class="nav-links">
        <a href="services.html" class="{'active' if active_page == 'services' else ''}">Services</a>
        <a href="index.html#why">Why Us</a>
        <a href="index.html#works">Process</a>
        <a href="areas.html" class="{'active' if active_page == 'areas' else ''}">Service Areas</a>
        <a href="about.html" class="{'active' if active_page == 'about' else ''}">About</a>
        <a href="index.html#faqs">FAQs</a>
        <a href="contact.html" class="{'active' if active_page == 'contact' else ''}">Contact</a>
      </div>
      <div class="nav-right">
        <a class="nav-phone" href="tel:+919440514057" aria-label="Call +91 94405 14057" style="display:flex; align-items:center; gap:8px; font-weight:700; font-size:0.95rem; text-decoration:none; color:var(--ink);">
          <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2Z"/></svg>
          <span>+91 94405 14057</span>
        </a>
        <a class="btn btn-orange nav-quote" href="contact.html">Book Now</a>
        <button class="nav-burger" id="navBurger" type="button" aria-expanded="false" aria-controls="navPanel" aria-label="Toggle navigation menu">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
    <div class="nav-panel" id="navPanel" hidden>
      <a href="services.html">Services</a>
      <a href="index.html#why">Why Us</a>
      <a href="index.html#works">How It Works</a>
      <a href="areas.html">Service Areas in Hyderabad</a>
      <a href="about.html">About Us</a>
      <a href="index.html#faqs">FAQs</a>
      <a href="contact.html">Contact Us</a>
      <a href="tel:+919440514057" style="color:var(--green); font-weight:700;">📞 Call: +91 94405 14057</a>
      <a class="btn btn-orange" href="contact.html">Book Cleaning Service</a>
    </div>
  </nav>
"""

# Common footer template
def get_footer():
    return """
  <footer>
    <div class="wrap">
      <div class="foot-grid" style="display:grid; grid-template-columns:2fr 1fr 1fr 1.5fr; gap:36px; padding:60px 0 40px; border-bottom:1px solid rgba(255,255,255,0.1);">
        <div>
          <a class="brand" href="index.html" style="margin-bottom:16px;">
            <img src="images/logo.webp" alt="Green Septic Tank Cleaning Services" height="42" width="150" />
          </a>
          <p style="color:var(--gray); font-size:0.9rem; line-height:1.6; margin-bottom:20px; max-width:320px;">
            Green Septic Tank Cleaning Services is Hyderabad's trusted, professional sanitation partner with 20+ years of dedicated service in Balapur, Ranga Reddy, and Greater Hyderabad. 24/7 heavy vacuum tanker support.
          </p>
          <div style="display:flex; gap:12px;">
            <a href="tel:+919440514057" style="color:#ffffff; background:rgba(255,255,255,0.1); padding:8px 14px; border-radius:8px; font-size:0.85rem; text-decoration:none; display:inline-flex; align-items:center; gap:6px;">
              📞 Call +91 94405 14057
            </a>
            <a href="https://wa.me/919440514057" target="_blank" rel="noopener" style="color:#ffffff; background:#25D366; padding:8px 14px; border-radius:8px; font-size:0.85rem; text-decoration:none; display:inline-flex; align-items:center; gap:6px;">
              💬 WhatsApp
            </a>
          </div>
        </div>

        <div class="f-col">
          <h4 style="color:#ffffff; font-size:1.05rem; font-weight:700; margin-bottom:16px;">Quick Links</h4>
          <a href="services.html">Our Services</a>
          <a href="index.html#why">Why Choose Us</a>
          <a href="index.html#works">How It Works</a>
          <a href="areas.html">Service Areas</a>
          <a href="about.html">About Company</a>
          <a href="index.html#faqs">FAQs</a>
          <a href="contact.html">Contact Us</a>
        </div>

        <div class="f-col">
          <h4 style="color:#ffffff; font-size:1.05rem; font-weight:700; margin-bottom:16px;">Our Services</h4>
          <a href="services.html">Residential Cleaning</a>
          <a href="services.html">Commercial Septic</a>
          <a href="services.html">STP Plant Cleaning</a>
          <a href="services.html">Sludge Pumping</a>
          <a href="services.html">Labour Camp Tanks</a>
          <a href="services.html">Industrial Solutions</a>
          <a href="services.html">Hospital Sanitation</a>
          <a href="services.html">Drainage Jetting</a>
        </div>

        <div class="f-col">
          <h4 style="color:#ffffff; font-size:1.05rem; font-weight:700; margin-bottom:16px;">Get In Touch</h4>
          <p style="color:var(--gray); font-size:0.88rem; line-height:1.6; margin-bottom:12px;">
            <b>Address:</b> 45-591NP, Maruthi Nagar, Badangpet Village, Balapur Mandal, Ranga Reddy, Hyderabad - 500058, Telangana, India
          </p>
          <p style="color:var(--gray); font-size:0.88rem; line-height:1.6; margin-bottom:12px;">
            <b>Phone:</b> <a href="tel:+919440514057" style="color:#86efac; text-decoration:none;">+91 94405 14057</a>
          </p>
          <p style="color:var(--gray); font-size:0.88rem; line-height:1.6; margin-bottom:12px;">
            <b>Email:</b> <a href="mailto:greenseptictankcleaningservices@gmail.com" style="color:#86efac; text-decoration:none;">greenseptictankcleaningservices@gmail.com</a>
          </p>
          <p style="color:var(--gray); font-size:0.88rem; line-height:1.6;">
            <b>Availability:</b> 24 Hours / 7 Days a Week
          </p>
        </div>
      </div>

      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:16px; padding:24px 0; color:var(--gray); font-size:0.85rem;">
        <div>
          © 2026 Green Septic Tank Cleaning Services. All rights reserved.
        </div>
        <div>
          Sanitation & Waste Management Services in Hyderabad, Telangana
        </div>
      </div>
    </div>
  </footer>

  <div class="floating-dock">
    <a href="https://wa.me/919440514057?text=Hello%20Green%20Septic%20Tank%20Cleaning%20Services,%20I%20need%20assistance." class="float-btn whatsapp" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">
      <svg viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/></svg>
    </a>
    <a href="tel:+919440514057" class="float-btn call" aria-label="Call +91 94405 14057">
      <svg viewBox="0 0 24 24"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2Z"/></svg>
    </a>
  </div>

  <script src="js/script.js"></script>
</body>
</html>
"""

# ==================== 1. SERVICES.HTML ====================
services_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Our Services — Septic Tank Cleaning & Waste Management Catalogue | Green Septic Tank</title>
  <meta name="description" content="Explore Green Septic Tank Cleaning Services range: residential, commercial, industrial septic tank cleaning, STP plant maintenance, sludge suction in Hyderabad." />
  <link rel="icon" type="image/webp" href="images/logo.webp" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>
{get_nav(active_page='services')}

  <header class="page-hero">
    <div class="page-hero-media">
      <img src="images/main-slider/eco-friendly-septic-services.webp" alt="Sanitation Services Catalogue" width="1800" height="720" />
    </div>
    <div class="page-hero-shade"></div>
    <div class="page-hero-glow"></div>
    <div class="page-hero-grid"></div>
    <div class="page-hero-grain"></div>
    <div class="wrap page-hero-in">
      <div aria-label="Breadcrumb" class="crumb">
        <a href="index.html">Home</a>
        <i>/</i>
        <span>Services</span>
      </div>
      <span class="label page-hero-eyebrow">Service Catalogue</span>
      <h1>Comprehensive Sanitation Solutions <em>For Every Property</em></h1>
      <p>From private villas to large commercial complexes and industrial STPs, our 20+ years of field experience, modern vacuum suction fleet, and certified disposal deliver guaranteed satisfaction.</p>
    </div>
  </header>

  <section class="sec">
    <div class="wrap">
      <div class="sec-head reveal">
        <span class="label">Full Range Overview</span>
        <h2>Professional Sanitation Services in Hyderabad</h2>
        <p>Explore our specialized service capabilities below. Each service includes high-power vacuum suction, odor control, and eco-friendly municipal disposal.</p>
      </div>

      <div class="cat-grid">
        <div class="cat-card reveal">
          <div class="cat-media">
            <img src="images/resource/residential-septic-tank.webp" alt="Residential Septic Tank Cleaning" />
            <span class="cat-badge">Residential</span>
          </div>
          <div class="cat-body">
            <h3>Residential Septic Tank Cleaning</h3>
            <p>Designed for independent houses, villas, and small housing colonies. Eliminates bad smells, toilet bubbling, and slow drainage with powerful suction that leaves zero mess.</p>
            <div class="cat-foot">
              <span class="live-pill" style="padding:4px 10px; font-size:0.75rem;">Capacity: Up to 6,000L</span>
              <a href="contact.html" class="btn btn-line btn-sm">Book Tanker</a>
            </div>
          </div>
        </div>

        <div class="cat-card reveal">
          <div class="cat-media">
            <img src="images/resource/commercial-septic-tank-cleaning.webp" alt="Commercial Septic Tank Cleaning" />
            <span class="cat-badge">Commercial</span>
          </div>
          <div class="cat-body">
            <h3>Commercial Septic Tank Cleaning</h3>
            <p>For restaurants, commercial complexes, banquet halls, and offices. Heavy grease and fat extraction with flexible night scheduling so your business is never disrupted.</p>
            <div class="cat-foot">
              <span class="live-pill" style="padding:4px 10px; font-size:0.75rem;">Off-Peak & Night Hours</span>
              <a href="contact.html" class="btn btn-line btn-sm">Book Tanker</a>
            </div>
          </div>
        </div>

        <div class="cat-card reveal">
          <div class="cat-media">
            <img src="images/resource/stp-plant-cleaning.webp" alt="STP Plant Cleaning Services" />
            <span class="cat-badge">STP Plant</span>
          </div>
          <div class="cat-body">
            <h3>STP Plant Cleaning & Maintenance</h3>
            <p>Sewage Treatment Plant deep cleaning, settling chamber sludge removal, and biological balance restoration for gated communities, IT parks, and factories.</p>
            <div class="cat-foot">
              <span class="live-pill" style="padding:4px 10px; font-size:0.75rem;">Capacity: 50KLD - 500KLD</span>
              <a href="contact.html" class="btn btn-line btn-sm">Book Tanker</a>
            </div>
          </div>
        </div>

        <div class="cat-card reveal">
          <div class="cat-media">
            <img src="images/resource/septic-tank-sludge-cleaning.webp" alt="Septic Tank Sludge Cleaning" />
            <span class="cat-badge">Sludge Removal</span>
          </div>
          <div class="cat-body">
            <h3>Septic Tank Sludge & Desludging</h3>
            <p>Deep extraction of hardened bottom sediment using high-pressure water jetting and high-vacuum pumps. Restores 100% soak-pit percolation capacity.</p>
            <div class="cat-foot">
              <span class="live-pill" style="padding:4px 10px; font-size:0.75rem;">Hard Sludge Removal</span>
              <a href="contact.html" class="btn btn-line btn-sm">Book Tanker</a>
            </div>
          </div>
        </div>

        <div class="cat-card reveal">
          <div class="cat-media">
            <img src="images/resource/labour-camp-septic-tank.webp" alt="Labour Camp Septic Tank Cleaning" />
            <span class="cat-badge">Labour Camps</span>
          </div>
          <div class="cat-body">
            <h3>Construction Camp Septic Tank Services</h3>
            <p>Scheduled daily or weekly pump-outs for high-density construction worker camps and temporary sanitation facilities with rapid multi-truck dispatch.</p>
            <div class="cat-foot">
              <span class="live-pill" style="padding:4px 10px; font-size:0.75rem;">Scheduled Contracts</span>
              <a href="contact.html" class="btn btn-line btn-sm">Book Tanker</a>
            </div>
          </div>
        </div>

        <div class="cat-card reveal">
          <div class="cat-media">
            <img src="images/resource/industrial-septic-tank-cleaning.webp" alt="Industrial Septic Tank Cleaning" />
            <span class="cat-badge">Industrial</span>
          </div>
          <div class="cat-body">
            <h3>Industrial Septic & Waste Cleaning</h3>
            <p>Heavy containment cleaning for industrial estates, factories, and fabrication facilities. Compliant with pollution control board manifesting requirements.</p>
            <div class="cat-foot">
              <span class="live-pill" style="padding:4px 10px; font-size:0.75rem;">Industrial Vacuum Pumps</span>
              <a href="contact.html" class="btn btn-line btn-sm">Book Tanker</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

{get_footer()}
"""

with open("services.html", "w", encoding="utf-8") as f:
    f.write(services_html)
print("Generated services.html")

# ==================== 2. ABOUT.HTML ====================
about_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>About Us — Green Septic Tank Cleaning Services Hyderabad</title>
  <meta name="description" content="Learn about Green Septic Tank Cleaning Services: 20+ years of sanitation experience, modern vacuum suction fleet, safety protocols, and eco-friendly disposal in Hyderabad." />
  <link rel="icon" type="image/webp" href="images/logo.webp" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>
{get_nav(active_page='about')}

  <header class="page-hero">
    <div class="page-hero-media">
      <img src="images/background/clean-safe-septic-services.webp" alt="About Green Septic Tank Cleaning Services" width="1800" height="720" />
    </div>
    <div class="page-hero-shade"></div>
    <div class="page-hero-glow"></div>
    <div class="page-hero-grid"></div>
    <div class="page-hero-grain"></div>
    <div class="wrap page-hero-in">
      <div aria-label="Breadcrumb" class="crumb">
        <a href="index.html">Home</a>
        <i>/</i>
        <span>About Us</span>
      </div>
      <span class="label page-hero-eyebrow">Our Legacy & Mission</span>
      <h1>Built on Trust. Driven by <em>20+ Years of Sanitation Excellence.</em></h1>
      <p>Providing hygienic, scientific, and eco-friendly septic tank and drainage solutions across Greater Hyderabad and Secunderabad since inception.</p>
    </div>
  </header>

  <section class="sec">
    <div class="wrap about-g">
      <div class="reveal">
        <span class="label">Our Story</span>
        <h2>20+ Years Serving Greater Hyderabad</h2>
        <p class="ab-lead" style="font-size:1.1rem; line-height:1.7; color:var(--ink); margin-bottom:16px;">
          Starting from Balapur, <b>Green Septic Tank Cleaning Services</b> was founded to replace unhygienic, hazardous manual cleaning methods with modern, powerful vacuum suction technology.
        </p>
        <p style="color:var(--gray); line-height:1.7; margin-bottom:20px;">
          Over the past two decades, we have handled over 15,000 septic tanks across Hyderabad, Secunderabad, and Ranga Reddy district. We have continually upgraded our fleet with high-vacuum tankers, pressurized hydro-jetters, and trained personnel equipped with full biosafety gear.
        </p>
        <p style="color:var(--gray); line-height:1.7;">
          Today, we are the go-to emergency partner for thousands of villa owners, housing associations, hospitals, schools, and commercial establishments who know that when drainage emergencies happen, our trucks arrive on time and complete the job cleanly.
        </p>
      </div>
      <div class="reveal">
        <img src="images/resource/reliable-septic-services.webp" alt="Reliable Septic Tank Team" style="width:100%; border-radius:20px; box-shadow:0 12px 30px rgba(0,0,0,0.08);" />
      </div>
    </div>
  </section>

  <section class="sec" style="background:#f8fafc;">
    <div class="wrap">
      <div class="sec-head reveal">
        <span class="label">Our Core Values</span>
        <h2>Why We Do Things Differently</h2>
        <p>We believe sanitation should be safe, transparent, and environmentally responsible:</p>
      </div>

      <div class="why-g">
        <div class="why-card reveal">
          <div class="scenario-icon">
            <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0 1 12 2.944a11.955 11.955 0 0 1-8.618 3.04A12.02 12.02 0 0 0 3 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016Z"/></svg>
          </div>
          <h3>100% Authorized Eco Disposal</h3>
          <p>Every liter of collected waste is unloaded strictly at designated municipal sewage treatment plants. We protect Hyderabad's groundwater and environment.</p>
        </div>

        <div class="why-card reveal">
          <div class="scenario-icon">
            <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"/></svg>
          </div>
          <h3>Transparent Upfront Rates</h3>
          <p>No sudden price increases, no exploitation during emergencies. We provide straightforward estimates based on tank volume and distance.</p>
        </div>

        <div class="why-card reveal">
          <div class="scenario-icon">
            <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M13 10V3L4 14h7v7l9-11h-7Z"/></svg>
          </div>
          <h3>Speed & Reliability</h3>
          <p>With multiple trucks distributed across Hyderabad, we average a 30 to 45 minute arrival time for critical overflow emergencies.</p>
        </div>
      </div>
    </div>
  </section>

{get_footer()}
"""

with open("about.html", "w", encoding="utf-8") as f:
    f.write(about_html)
print("Generated about.html")

# ==================== 3. AREAS.HTML ====================
areas_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Service Areas — Septic Tank Cleaning Hyderabad & Secunderabad | Green Septic Tank</title>
  <meta name="description" content="Green Septic Tank Cleaning coverage across Hyderabad: Balapur, LB Nagar, Dilsukhnagar, Uppal, Gachibowli, Madhapur, Kukatpally, Secunderabad. 30-min response." />
  <link rel="icon" type="image/webp" href="images/logo.webp" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>
{get_nav(active_page='areas')}

  <header class="page-hero">
    <div class="page-hero-media">
      <img src="images/main-slider/fast-efficient-septic-services.webp" alt="Hyderabad Service Areas" width="1800" height="720" />
    </div>
    <div class="page-hero-shade"></div>
    <div class="page-hero-glow"></div>
    <div class="page-hero-grid"></div>
    <div class="page-hero-grain"></div>
    <div class="wrap page-hero-in">
      <div aria-label="Breadcrumb" class="crumb">
        <a href="index.html">Home</a>
        <i>/</i>
        <span>Service Areas</span>
      </div>
      <span class="label page-hero-eyebrow">Local Coverage</span>
      <h1>Rapid Tanker Dispatch <em>Across Greater Hyderabad</em></h1>
      <p>Strategically positioned suction tankers across South Hyderabad, East Hyderabad, and the Cyberabad IT Corridor guarantee swift arrival when you need us most.</p>
    </div>
  </header>

  <section class="sec">
    <div class="wrap">
      <div class="sec-head reveal">
        <span class="label">Coverage Zones</span>
        <h2>Neighborhoods & Key Localities We Serve</h2>
        <p>Our fleet operates across all major zones in Hyderabad, Ranga Reddy, and Secunderabad 24 hours a day:</p>
      </div>

      <div class="why-g">
        <div class="why-card reveal">
          <div class="scenario-icon">📍</div>
          <h3>South Hyderabad (Headquarters)</h3>
          <p><b>Balapur (HQ), Badangpet, Meerpet, Chandrayangutta, Falaknuma, Shamshabad, Kothapet, Saroor Nagar.</b></p>
          <span class="live-pill" style="margin-top:12px; font-size:0.75rem;">Fastest Response: 20-30 Mins</span>
        </div>

        <div class="why-card reveal">
          <div class="scenario-icon">📍</div>
          <h3>East Hyderabad</h3>
          <p><b>LB Nagar, Dilsukhnagar, Champapet, Karmanghat, BN Reddy Nagar, Vanasthalipuram, Hayathnagar, Uppal, Nagole.</b></p>
          <span class="live-pill" style="margin-top:12px; font-size:0.75rem;">Response: 30-40 Mins</span>
        </div>

        <div class="why-card reveal">
          <div class="scenario-icon">📍</div>
          <h3>West & IT Corridor</h3>
          <p><b>Gachibowli, Madhapur, Hitec City, Kondapur, Jubilee Hills, Banjara Hills, Manikonda, Financial District.</b></p>
          <span class="live-pill" style="margin-top:12px; font-size:0.75rem;">Response: 35-45 Mins</span>
        </div>

        <div class="why-card reveal">
          <div class="scenario-icon">📍</div>
          <h3>North & Secunderabad</h3>
          <p><b>Kukatpally, Miyapur, Nizampet, Begumpet, Secunderabad, Bowenpally, Alwal, Malkajgiri, ECIL.</b></p>
          <span class="live-pill" style="margin-top:12px; font-size:0.75rem;">Response: 40-50 Mins</span>
        </div>
      </div>

      <div style="margin-top:48px; text-align:center;" class="reveal">
        <h3 style="font-size:1.4rem; font-weight:700; margin-bottom:12px; color:var(--ink);">Is your location outside these zones?</h3>
        <p style="color:var(--gray); margin-bottom:24px;">We also serve farmhouse clusters, industrial belts, and peripheral zones along the Outer Ring Road (ORR).</p>
        <a href="tel:+919440514057" class="btn btn-orange">Call Dispatch Desk: +91 94405 14057</a>
      </div>
    </div>
  </section>

{get_footer()}
"""

with open("areas.html", "w", encoding="utf-8") as f:
    f.write(areas_html)
print("Generated areas.html")

# ==================== 4. CONTACT.HTML ====================
contact_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Contact Us — 24/7 Septic Tank Cleaning Booking | Green Septic Tank</title>
  <meta name="description" content="Contact Green Septic Tank Cleaning Services Hyderabad. Call +91 94405 14057 for 24/7 emergency dispatch, free quote, or WhatsApp booking." />
  <link rel="icon" type="image/webp" href="images/logo.webp" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>
{get_nav(active_page='contact')}

  <header class="page-hero">
    <div class="page-hero-media">
      <img src="images/background/clean-safe-septic-services.webp" alt="Contact Green Septic Tank Cleaning Services" width="1800" height="720" />
    </div>
    <div class="page-hero-shade"></div>
    <div class="page-hero-glow"></div>
    <div class="page-hero-grid"></div>
    <div class="page-hero-grain"></div>
    <div class="wrap page-hero-in">
      <div aria-label="Breadcrumb" class="crumb">
        <a href="index.html">Home</a>
        <i>/</i>
        <span>Contact</span>
      </div>
      <span class="label page-hero-eyebrow">24/7 Dispatch Desk</span>
      <h1>Get in Touch <em>Today</em></h1>
      <p>Have an urgent septic overflow or planning routine maintenance? Contact our Balapur dispatch desk for instant quotes and prompt tanker deployment.</p>
    </div>
  </header>

  <section class="sec">
    <div class="wrap">
      <div class="contact-card reveal">
        <div class="cc-photo">
          <img src="images/background/clean-safe-septic-services.webp" alt="Contact Info Green Septic Tank" />
          <div class="cc-info">
            <h3 style="font-size:1.4rem; font-weight:800; margin-bottom:16px;">Direct Contact Info</h3>
            <div class="cc-rows">
              <div class="cc-row">
                <span class="cc-ic">
                  <svg width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" viewBox="0 0 24 24"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2Z"/></svg>
                </span>
                <div>
                  <b>Phone / Helpline</b>
                  <span>+91 94405 14057</span>
                </div>
              </div>

              <div class="cc-row">
                <span class="cc-ic">
                  <svg width="22" height="22" fill="currentColor" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/></svg>
                </span>
                <div>
                  <b>WhatsApp Quick Chat</b>
                  <span>+91 94405 14057</span>
                </div>
              </div>

              <div class="cc-row">
                <span class="cc-ic">
                  <svg width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" viewBox="0 0 24 24"><rect width="18" height="14" x="3" y="5" rx="2"/><path d="m3 7 9 6 9-6"/></svg>
                </span>
                <div>
                  <b>Email Address</b>
                  <span>greenseptictankcleaningservices@gmail.com</span>
                </div>
              </div>

              <div class="cc-row">
                <span class="cc-ic">
                  <svg width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" viewBox="0 0 24 24"><path d="M12 21s-8-6.5-8-12a8 8 0 1 1 16 0c0 5.5-8 12-8 12Z"/><circle cx="12" cy="9" r="3"/></svg>
                </span>
                <div>
                  <b>Main Office</b>
                  <span>45-591NP, Maruthi Nagar, Badangpet Village, Balapur Mandal, Ranga Reddy, Hyderabad - 500058, Telangana, India</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="cc-form">
          <h3 style="font-size:1.35rem; font-weight:700; margin-bottom:8px; color:var(--ink);">Book a Tanker / Request Free Estimate</h3>
          <p style="color:var(--gray); font-size:0.9rem; margin-bottom:20px;">Fill in your details below for instant dispatch coordination:</p>
          
          <form id="quoteForm" class="contact-form">
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px;">
              <div>
                <label style="display:block; font-size:0.85rem; font-weight:600; color:var(--ink); margin-bottom:6px;">Your Name *</label>
                <input type="text" name="name" required placeholder="e.g. Ramesh Reddy" style="width:100%; padding:10px 14px; border:1px solid var(--line); border-radius:8px; font-size:0.95rem;" />
              </div>
              <div>
                <label style="display:block; font-size:0.85rem; font-weight:600; color:var(--ink); margin-bottom:6px;">Phone Number *</label>
                <input type="tel" name="phone" required placeholder="e.g. 9876543210" style="width:100%; padding:10px 14px; border:1px solid var(--line); border-radius:8px; font-size:0.95rem;" />
              </div>
            </div>

            <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:16px;">
              <div>
                <label style="display:block; font-size:0.85rem; font-weight:600; color:var(--ink); margin-bottom:6px;">Service Type *</label>
                <select name="service" style="width:100%; padding:10px 14px; border:1px solid var(--line); border-radius:8px; font-size:0.95rem;">
                  <option value="Residential Septic Tank Cleaning">Residential Septic Tank Cleaning</option>
                  <option value="Commercial Septic Tank Cleaning">Commercial Septic Tank Cleaning</option>
                  <option value="STP Plant Cleaning">STP Plant Cleaning Services</option>
                  <option value="Septic Tank Sludge Cleaning">Septic Tank Sludge Cleaning</option>
                  <option value="Labour Camp Septic Cleaning">Labour Camp Septic Cleaning</option>
                  <option value="Industrial Septic Cleaning">Industrial Septic Cleaning</option>
                </select>
              </div>
              <div>
                <label style="display:block; font-size:0.85rem; font-weight:600; color:var(--ink); margin-bottom:6px;">Locality / Area *</label>
                <input type="text" name="area" required placeholder="e.g. Balapur, LB Nagar, Gachibowli" style="width:100%; padding:10px 14px; border:1px solid var(--line); border-radius:8px; font-size:0.95rem;" />
              </div>
            </div>

            <div style="margin-top:16px;">
              <label style="display:block; font-size:0.85rem; font-weight:600; color:var(--ink); margin-bottom:6px;">Urgency Level</label>
              <select name="urgency" style="width:100%; padding:10px 14px; border:1px solid var(--line); border-radius:8px; font-size:0.95rem;">
                <option value="Emergency (Dispatch Today / ASAP)">🚨 Emergency (Dispatch Today / ASAP)</option>
                <option value="Within 24 Hours">Within 24 Hours</option>
                <option value="Schedule for Weekend">Schedule for Weekend</option>
                <option value="Routine General Enquiry">Routine General Enquiry</option>
              </select>
            </div>

            <div style="margin-top:16px;">
              <label style="display:block; font-size:0.85rem; font-weight:600; color:var(--ink); margin-bottom:6px;">Additional Details (Optional)</label>
              <textarea name="message" rows="3" placeholder="Approx tank size, number of floors/flats, or problem description..." style="width:100%; padding:10px 14px; border:1px solid var(--line); border-radius:8px; font-size:0.95rem; resize:vertical;"></textarea>
            </div>

            <button type="submit" class="btn btn-orange" style="width:100%; margin-top:20px; padding:14px; font-size:1rem; justify-content:center;">
              Submit Request & Coordinate Dispatch
            </button>
          </form>
        </div>
      </div>
    </div>
  </section>

{get_footer()}
"""

with open("contact.html", "w", encoding="utf-8") as f:
    f.write(contact_html)
print("Generated contact.html")

print("All subpages generated successfully!")
