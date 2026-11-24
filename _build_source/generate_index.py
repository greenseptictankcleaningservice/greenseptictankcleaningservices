import html

index_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Green Septic Tank Cleaning Services | 24/7 Septic Tank Cleaning in Hyderabad | Call Now</title>
  <meta name="description" content="Green Septic Tank Cleaning Services provides professional 24/7 septic tank cleaning, sludge removal, STP plant cleaning, and emergency drainage unblocking in Hyderabad. 20+ years experience, heavy vacuum tankers. Call +91 94405 14057." />
  <meta property="og:type" content="website" />
  <meta property="og:title" content="Green Septic Tank Cleaning Services — Hyderabad" />
  <meta property="og:description" content="Professional septic tank cleaning, sewage pumping & sludge removal across Hyderabad. 24/7 emergency service. Call +91 94405 14057." />
  <meta property="og:image" content="images/resource/notch-septic-tank-cleaning-services.webp" />
  <link rel="icon" type="image/webp" href="images/logo.webp" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>

  <!-- ==================== NAVIGATION BAR ==================== -->
  <nav>
    <div class="wrap nav-in">
      <a class="brand" href="index.html" aria-label="Green Septic Tank Cleaning Services">
        <img src="images/logo.webp" alt="Green Septic Tank Cleaning Services Logo" class="brand-logo" height="46" width="160" />
      </a>
      <div class="nav-links">
        <a href="#services">Services</a>
        <a href="#why">Why Us</a>
        <a href="#works">Process</a>
        <a href="#areas">Service Areas</a>
        <a href="#testimonials">Reviews</a>
        <a href="#about">About</a>
        <a href="#faqs">FAQs</a>
        <a href="#contact">Contact</a>
      </div>
      <div class="nav-right">
        <a class="nav-phone" href="tel:+919440514057" aria-label="Call +91 94405 14057" style="display:flex; align-items:center; gap:8px; font-weight:700; font-size:0.95rem; text-decoration:none; color:var(--ink);">
          <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2Z"/></svg>
          <span>+91 94405 14057</span>
        </a>
        <a class="btn btn-orange nav-quote" href="#contact">Book Now</a>
        <button class="nav-burger" id="navBurger" type="button" aria-expanded="false" aria-controls="navPanel" aria-label="Toggle navigation menu">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
    <!-- Mobile Navigation Drawer -->
    <div class="nav-panel" id="navPanel" hidden>
      <a href="#services">Services</a>
      <a href="#why">Why Us</a>
      <a href="#works">How It Works</a>
      <a href="#areas">Service Areas in Hyderabad</a>
      <a href="#testimonials">Customer Reviews</a>
      <a href="#about">About Us</a>
      <a href="#faqs">FAQs</a>
      <a href="tel:+919440514057" style="color:var(--green); font-weight:700;">📞 Call: +91 94405 14057</a>
      <a class="btn btn-orange" href="#contact">Book Cleaning Service</a>
    </div>
  </nav>

  <!-- ==================== HERO SECTION ==================== -->
  <header class="hero" id="top">
    <picture>
      <source srcset="images/main-slider/fast-efficient-septic-services.webp" type="image/webp" />
      <img src="images/main-slider/fast-efficient-septic-services.webp" alt="Green Septic Tank Heavy Duty Vacuum Suction Truck Service in Hyderabad" class="hero-img" fetchpriority="high" decoding="async" width="1380" height="920" />
    </picture>
    <div class="hero-shade"></div>
    <div class="hero-glow"></div>
    <div class="hero-vig"></div>
    <div class="hero-grid"></div>
    <div class="hero-grain"></div>

    <div class="wrap hero-in">
      <div style="display:flex; align-items:center; gap:12px; flex-wrap:wrap; margin-bottom:16px;">
        <span class="hero-badge">🌿 20+ Years Field Experience in Hyderabad</span>
        <div class="live-pill" style="background:rgba(22,163,74,0.25); color:#86efac; border-color:rgba(34,197,94,0.4);">
          <span class="live-dot"></span>
          24/7 Emergency Dispatch Active
        </div>
      </div>
      <h1>Professional Septic Tank Cleaning & Sludge Removal You Can Trust</h1>
      <p class="hero-desc">
        Dealing with bad smell, toilet backflow, or tank overflow? With 20+ years of local experience across Balapur, LB Nagar, and Greater Hyderabad, we deliver heavy-duty vacuum suction pumping, thorough drainage blockage clearing, and 100% eco-friendly certified disposal.
      </p>
      <div class="hero-btns">
        <a class="btn btn-orange" href="#contact">Get Free Quote / Book Tanker</a>
        <a class="btn btn-white" href="tel:+919440514057">
          <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2Z"/></svg>
          Call +91 94405 14057
        </a>
        <a class="btn btn-whatsapp" href="https://wa.me/919440514057?text=Hello%20Green%20Septic%20Tank%20Cleaning%20Services,%20I%20need%20urgent%20septic%20tank%20cleaning%20support." target="_blank" rel="noopener">
          <svg width="18" height="18" fill="currentColor" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/></svg>
          WhatsApp Now
        </a>
      </div>
    </div>
  </header>

  <!-- ==================== FLOATING STATS STRIP ==================== -->
  <section class="stats">
    <div class="wrap">
      <div class="stats-card reveal">
        <div class="stats-g">
          <div class="stat">
            <div class="num">
              <span data-count="20">0</span><i>+</i>
            </div>
            <small>Years Local Experience</small>
          </div>
          <div class="stat">
            <div class="num">
              <span data-count="15000">0</span><i>+</i>
            </div>
            <small>Septic Tanks Cleaned</small>
          </div>
          <div class="stat">
            <div class="num">
              <span data-count="100">0</span><i>%</i>
            </div>
            <small>Eco-Friendly Disposal</small>
          </div>
          <div class="stat">
            <div class="num">
              <span data-count="24">0</span><i>/7</i>
            </div>
            <small>Emergency Night Support</small>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ==================== SERVICES SECTION ==================== -->
  <section class="sec services" id="services">
    <div class="wrap">
      <div class="sec-head left has-qlinks reveal">
        <span class="label">Comprehensive Services</span>
        <h2>Sanitation Solutions<br />Built <em>Around Your Property</em></h2>
        <p>From independent villas and housing colonies to 100+ flat gated apartments, commercial restaurants, and industrial plants — we deploy high-power vacuum tankers and trained technicians to solve sewage issues without odor or mess.</p>

        <!-- Service Category Filter Pills -->
        <div class="svc-tabs reveal">
          <button class="svc-tab-btn active" data-filter="all" type="button">All Services</button>
          <button class="svc-tab-btn" data-filter="residential" type="button">Residential</button>
          <button class="svc-tab-btn" data-filter="commercial" type="button">Commercial & Hotels</button>
          <button class="svc-tab-btn" data-filter="stp" type="button">STP Plant Cleaning</button>
          <button class="svc-tab-btn" data-filter="sludge" type="button">Sludge Suction</button>
          <button class="svc-tab-btn" data-filter="industrial" type="button">Industrial & Camps</button>
        </div>
      </div>

      <!-- Service Cards Grid -->
      <div class="cat-grid">
        <!-- 1. Residential -->
        <div class="cat-card reveal" data-category="residential">
          <div class="cat-media">
            <img src="images/resource/residential-septic-tank.webp" alt="Residential Septic Tank Cleaning Hyderabad" loading="lazy" />
            <span class="cat-badge">Residential</span>
          </div>
          <div class="cat-body">
            <h3>Residential Septic Tank Cleaning</h3>
            <p>Designed for independent houses, villas, and residential complexes. We quickly eliminate toilet bubbling, slow drainage, and bad smells with powerful suction hoses that keep your garden and compound spotless.</p>
            <ul style="margin:12px 0 16px 18px; color:var(--gray); font-size:0.88rem; line-height:1.6;">
              <li>High-vacuum suction pumping with long-reach pipes</li>
              <li>Chamber opening, thorough desludging, & resealing</li>
              <li>Complete odor neutralizing treatment</li>
            </ul>
            <div class="cat-foot">
              <span class="live-pill" style="padding:4px 10px; font-size:0.75rem;">Fast 30-Min Dispatch</span>
              <a href="#contact" class="btn btn-line btn-sm" style="padding:6px 16px; font-size:0.85rem;">Book Service</a>
            </div>
          </div>
        </div>

        <!-- 2. Commercial -->
        <div class="cat-card reveal" data-category="commercial">
          <div class="cat-media">
            <img src="images/resource/commercial-septic-tank-cleaning.webp" alt="Commercial Septic Tank Cleaning in Hyderabad" loading="lazy" />
            <span class="cat-badge">Commercial</span>
          </div>
          <div class="cat-body">
            <h3>Commercial Septic Tank Cleaning</h3>
            <p>Tailored for restaurants, malls, function halls, schools, and business offices. We clean high-capacity septic reservoirs and grease trap lines during off-peak hours so your commercial operations are never interrupted.</p>
            <ul style="margin:12px 0 16px 18px; color:var(--gray); font-size:0.88rem; line-height:1.6;">
              <li>Heavy grease trap and fat sludge extraction</li>
              <li>Flexible night and early morning scheduling</li>
              <li>Full compliance with municipal sanitation norms</li>
            </ul>
            <div class="cat-foot">
              <span class="live-pill" style="padding:4px 10px; font-size:0.75rem;">Night Shifts Available</span>
              <a href="#contact" class="btn btn-line btn-sm" style="padding:6px 16px; font-size:0.85rem;">Book Service</a>
            </div>
          </div>
        </div>

        <!-- 3. STP Plant -->
        <div class="cat-card reveal" data-category="stp commercial industrial">
          <div class="cat-media">
            <img src="images/resource/stp-plant-cleaning.webp" alt="STP Plant Cleaning Services Hyderabad" loading="lazy" />
            <span class="cat-badge">STP Plant</span>
          </div>
          <div class="cat-body">
            <h3>STP Plant Cleaning Services</h3>
            <p>Comprehensive Sewage Treatment Plant maintenance, overflow resolution, and deep biological sludge removal for large gated communities, corporate IT parks, and industrial complexes in Hyderabad.</p>
            <ul style="margin:12px 0 16px 18px; color:var(--gray); font-size:0.88rem; line-height:1.6;">
              <li>Aeration and settling tank deep cleaning</li>
              <li>Sludge dewatering, extraction, and eco-disposal</li>
              <li>Odor control & biological balance restoration</li>
            </ul>
            <div class="cat-foot">
              <span class="live-pill" style="padding:4px 10px; font-size:0.75rem;">Heavy Tanker Fleet</span>
              <a href="#contact" class="btn btn-line btn-sm" style="padding:6px 16px; font-size:0.85rem;">Book Service</a>
            </div>
          </div>
        </div>

        <!-- 4. Sludge Cleaning -->
        <div class="cat-card reveal" data-category="sludge residential commercial">
          <div class="cat-media">
            <img src="images/resource/septic-tank-sludge-cleaning.webp" alt="Septic Tank Sludge Cleaning Hyderabad" loading="lazy" />
            <span class="cat-badge">Sludge Removal</span>
          </div>
          <div class="cat-body">
            <h3>Septic Tank Sludge & Suction Work</h3>
            <p>Over years of usage, hardened sludge settles at the bottom of septic chambers, choking natural percolation. Our high-pressure jetting and vacuum liquefaction break down and extract all compacted waste.</p>
            <ul style="margin:12px 0 16px 18px; color:var(--gray); font-size:0.88rem; line-height:1.6;">
              <li>High-pressure water jetting for hardened sludge</li>
              <li>Thorough suction leaving zero residues</li>
              <li>Restores 100% tank storage and percolation capacity</li>
            </ul>
            <div class="cat-foot">
              <span class="live-pill" style="padding:4px 10px; font-size:0.75rem;">Deep Desludging</span>
              <a href="#contact" class="btn btn-line btn-sm" style="padding:6px 16px; font-size:0.85rem;">Book Service</a>
            </div>
          </div>
        </div>

        <!-- 5. Labour Camps -->
        <div class="cat-card reveal" data-category="industrial commercial">
          <div class="cat-media">
            <img src="images/resource/labour-camp-septic-tank.webp" alt="Construction Site Labour Camp Septic Tank Cleaning" loading="lazy" />
            <span class="cat-badge">Labour Camps</span>
          </div>
          <div class="cat-body">
            <h3>Labour Camp & Construction Sites</h3>
            <p>High-density labor camps and active construction sites generate continuous heavy sanitary loads. We provide routine scheduled pump-outs and emergency clearances to prevent health hazards and site shutdowns.</p>
            <ul style="margin:12px 0 16px 18px; color:var(--gray); font-size:0.88rem; line-height:1.6;">
              <li>Daily, weekly, or bi-weekly scheduled visits</li>
              <li>Multi-tanker simultaneous deployment for fast turnaround</li>
              <li>Strict health, safety, and pollution board compliance</li>
            </ul>
            <div class="cat-foot">
              <span class="live-pill" style="padding:4px 10px; font-size:0.75rem;">Bulk Contract Rates</span>
              <a href="#contact" class="btn btn-line btn-sm" style="padding:6px 16px; font-size:0.85rem;">Book Service</a>
            </div>
          </div>
        </div>

        <!-- 6. Industrial -->
        <div class="cat-card reveal" data-category="industrial">
          <div class="cat-media">
            <img src="images/resource/industrial-septic-tank-cleaning.webp" alt="Industrial Septic Tank Cleaning Hyderabad" loading="lazy" />
            <span class="cat-badge">Industrial</span>
          </div>
          <div class="cat-body">
            <h3>Industrial Septic Tank Cleaning</h3>
            <p>Specialized waste extraction for manufacturing plants, industrial estates, warehouses, and fabrication yards. Our heavy industrial suction trucks handle large-volume containment chambers safely and systematically.</p>
            <ul style="margin:12px 0 16px 18px; color:var(--gray); font-size:0.88rem; line-height:1.6;">
              <li>High-capacity 10,000+ liter vacuum tankers</li>
              <li>Safety harnesses, gas detectors & trained operatives</li>
              <li>Official disposal manifesting & environmental tracking</li>
            </ul>
            <div class="cat-foot">
              <span class="live-pill" style="padding:4px 10px; font-size:0.75rem;">Heavy Industrial Capacity</span>
              <a href="#contact" class="btn btn-line btn-sm" style="padding:6px 16px; font-size:0.85rem;">Book Service</a>
            </div>
          </div>
        </div>

        <!-- 7. Hospital -->
        <div class="cat-card reveal" data-category="commercial stp">
          <div class="cat-media">
            <img src="images/resource/hospital-septic-tank-cleaning.webp" alt="Hospital Septic Tank Cleaning Services Hyderabad" loading="lazy" />
            <span class="cat-badge">Healthcare</span>
          </div>
          <div class="cat-body">
            <h3>Hospital Septic Tank Cleaning</h3>
            <p>Medical and healthcare premises require non-negotiable hygiene, zero atmospheric contamination, and zero spills. Our sanitization specialists operate under strict biosafety protocols with closed-circuit suction pumps.</p>
            <ul style="margin:12px 0 16px 18px; color:var(--gray); font-size:0.88rem; line-height:1.6;">
              <li>Zero-emission closed-circuit vacuum pumping</li>
              <li>Hospital-grade surface disinfection around chambers</li>
              <li>24/7 priority emergency hotline for health facilities</li>
            </ul>
            <div class="cat-foot">
              <span class="live-pill" style="padding:4px 10px; font-size:0.75rem;">Priority Medical Dispatch</span>
              <a href="#contact" class="btn btn-line btn-sm" style="padding:6px 16px; font-size:0.85rem;">Book Service</a>
            </div>
          </div>
        </div>

        <!-- 8. Maintenance -->
        <div class="cat-card reveal" data-category="residential commercial">
          <div class="cat-media">
            <img src="images/resource/septic-tank-maintenance.webp" alt="Septic Tank Maintenance & Inspection Hyderabad" loading="lazy" />
            <span class="cat-badge">Preventative</span>
          </div>
          <div class="cat-body">
            <h3>Septic Tank Maintenance & Inspection</h3>
            <p>Routine inspection and chamber maintenance that catches blockages, pipe cracks, and sludge buildup before sewage overflows into your living spaces or foundation walls. Saves thousands in costly property repairs.</p>
            <ul style="margin:12px 0 16px 18px; color:var(--gray); font-size:0.88rem; line-height:1.6;">
              <li>Baffle wall, inlet & outlet inspection</li>
              <li>Percolation soak-pit check & root clearance</li>
              <li>Custom periodic maintenance plans for societies</li>
            </ul>
            <div class="cat-foot">
              <span class="live-pill" style="padding:4px 10px; font-size:0.75rem;">Annual Society Plans</span>
              <a href="#contact" class="btn btn-line btn-sm" style="padding:6px 16px; font-size:0.85rem;">Book Service</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ==================== WHY CHOOSE US ==================== -->
  <section class="sec" id="why">
    <div class="wrap">
      <div class="sec-head reveal">
        <span class="label">Why Choose Green Septic Tank</span>
        <h2>Why Hyderabad Property Owners<br /><em>Trust Our Fleet & Crew</em></h2>
        <p>People do not call a septic cleaning service for fancy talk. They call when there is foul smell, overflow, urgency, and stress. Here is why thousands of homeowners, RWAs, and businesses in Balapur and Greater Hyderabad rely on us:</p>
      </div>

      <div class="why-g">
        <div class="why-card reveal">
          <div class="scenario-icon">
            <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 8v4l3 3m6-3a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"/></svg>
          </div>
          <h3>20+ Years Field Experience</h3>
          <p>We know every soil type, drainage layout, and chamber structure in Hyderabad. Our seasoned technicians solve complex blockages quickly where newer operators struggle.</p>
        </div>

        <div class="why-card reveal">
          <div class="scenario-icon">
            <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M13 10V3L4 14h7v7l9-11h-7Z"/></svg>
          </div>
          <h3>High-Power Vacuum Tankers</h3>
          <p>Equipped with commercial-grade Italian and German vacuum pumps capable of lifting heavy, compacted sludge through long pipes from basement and narrow alleyway tanks.</p>
        </div>

        <div class="why-card reveal">
          <div class="scenario-icon">
            <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 6v6h4.5m4.5 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"/></svg>
          </div>
          <h3>24/7 Emergency Dispatch</h3>
          <p>Sewage disasters do not wait for business hours. Whether it is 2:00 AM on a Sunday or during torrential monsoon downpours, our emergency crews answer immediately.</p>
        </div>

        <div class="why-card reveal">
          <div class="scenario-icon">
            <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0 1 12 2.944a11.955 11.955 0 0 1-8.618 3.04A12.02 12.02 0 0 0 3 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016Z"/></svg>
          </div>
          <h3>Zero-Spill & Eco-Disposal</h3>
          <p>We strictly dispose of waste at authorized municipal treatment facilities in full compliance with environmental protection regulations. Zero illegal dumping, guaranteed.</p>
        </div>

        <div class="why-card reveal">
          <div class="scenario-icon">
            <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"/></svg>
          </div>
          <h3>Honest & Transparent Pricing</h3>
          <p>Clear, fixed pricing quoted upfront based on actual tank volume and site conditions. No surprise fees, no sudden extra charges after opening the chamber cover.</p>
        </div>

        <div class="why-card reveal">
          <div class="scenario-icon">
            <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M17 20h5v-2a3 3 0 0 0-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 0 1 5.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 0 1 9.288 0M15 7a3 3 0 1 1-6 0 3 3 0 0 1 6 0Zm6 3a2 2 0 1 1-4 0 2 2 0 0 1 4 0ZM7 10a2 2 0 1 1-4 0 2 2 0 0 1 4 0Z"/></svg>
          </div>
          <h3>Trained & Safety-Equipped Crew</h3>
          <p>Our personnel wear protective suits, respirators, rubber boots, and safety gloves. We prioritize health and safety for both our crew and your family.</p>
        </div>
      </div>

      <!-- Trust Checkmarks Strip -->
      <div class="cert-strip reveal" style="margin-top:40px; background:var(--green-tint); border:1px solid rgba(22,163,74,0.3); border-radius:16px; padding:20px 28px; display:flex; flex-wrap:wrap; justify-content:space-around; gap:16px;">
        <span style="display:flex; align-items:center; gap:8px; font-weight:600; color:#15803d; font-size:0.92rem;">
          <span style="color:#16a34a; font-weight:800;">✓</span> 20+ Years Continuous Service in Hyderabad
        </span>
        <span style="display:flex; align-items:center; gap:8px; font-weight:600; color:#15803d; font-size:0.92rem;">
          <span style="color:#16a34a; font-weight:800;">✓</span> Municipal Authorized Disposal Practice
        </span>
        <span style="display:flex; align-items:center; gap:8px; font-weight:600; color:#15803d; font-size:0.92rem;">
          <span style="color:#16a34a; font-weight:800;">✓</span> 100% Odor Neutralization Post-Clean
        </span>
        <span style="display:flex; align-items:center; gap:8px; font-weight:600; color:#15803d; font-size:0.92rem;">
          <span style="color:#16a34a; font-weight:800;">✓</span> 30 to 45 Minute Arrival Guarantee
        </span>
      </div>
    </div>
  </section>

  <!-- ==================== WORKING PROCESS ==================== -->
  <section class="sec" id="works" style="background:#f8fafc;">
    <div class="wrap">
      <div class="sec-head reveal">
        <span class="label">Our Working Process</span>
        <h2>From Your Call to a <em>Clean, Fresh Tank</em></h2>
        <p>We keep our service straightforward, fast, and completely hassle-free so you always know what to expect:</p>
      </div>

      <div class="works-g">
        <div class="work-step reveal">
          <div class="step-num">01</div>
          <h3>Quick Call or WhatsApp</h3>
          <p>You contact us and describe your issue (bad smell, overflow, bubbling toilet, or scheduled routine clean). We ask basic details about tank size, location, and accessibility, providing an immediate upfront estimate.</p>
        </div>

        <div class="work-step reveal">
          <div class="step-num">02</div>
          <h3>Prompt Arrival & Inspection</h3>
          <p>Our vacuum suction tanker arrives at your location in Hyderabad within 30–45 minutes. Our team inspects the chambers, drainage lines, and inlet/outlet connections with precision before starting.</p>
        </div>

        <div class="work-step reveal">
          <div class="step-num">03</div>
          <h3>High-Power Vacuum Pumping</h3>
          <p>We connect heavy-duty, leak-proof hoses and initiate high-pressure suction to extract wastewater, scum, and settled sludge right down to the tank floor without making any mess around your premises.</p>
        </div>

        <div class="work-step reveal">
          <div class="step-num">04</div>
          <h3>Odor Treatment & Eco-Disposal</h3>
          <p>We wash chamber walls, apply eco-friendly odor neutralizers, seal the lids tightly, and transport the waste directly to government-certified treatment facilities for safe biological processing.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ==================== MIDDLE EMERGENCY BANNER ==================== -->
  <section class="sec" style="padding:0;">
    <div class="wrap">
      <div class="cta-card reveal" style="background:linear-gradient(135deg, #0b130e 0%, #15803d 100%); color:#ffffff; border-radius:24px; padding:48px 40px; display:flex; flex-wrap:wrap; align-items:center; justify-content:space-between; gap:24px;">
        <div style="max-width:620px;">
          <div class="live-pill" style="background:rgba(255,255,255,0.15); color:#ffffff; border-color:rgba(255,255,255,0.3); margin-bottom:16px;">
            <span class="live-dot" style="background:#4ade80;"></span>
            Immediate Emergency Response Team on Duty
          </div>
          <h2 style="font-size:2.2rem; font-weight:800; line-height:1.2; margin-bottom:12px; color:#ffffff;">Dealing With Sewage Overflow Right Now?</h2>
          <p style="font-size:1.05rem; opacity:0.9; line-height:1.6; margin:0;">Don't let dirty backflow damage your flooring, spread germs, or create foul odors for your family or guests. Call our 24/7 emergency dispatch team right away.</p>
        </div>
        <div style="display:flex; flex-direction:column; gap:12px; min-width:260px;">
          <a href="tel:+919440514057" class="btn btn-white" style="font-size:1.05rem; padding:14px 24px; justify-content:center;">
            <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2Z"/></svg>
            Call: +91 94405 14057
          </a>
          <a href="https://wa.me/919440514057?text=EMERGENCY:%20I%20have%20septic%20tank%20overflow.%20Please%20dispatch%20tanker%20urgently." class="btn btn-whatsapp" target="_blank" rel="noopener" style="font-size:1.05rem; padding:14px 24px; justify-content:center;">
            <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/></svg>
            Emergency WhatsApp Dispatch
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- ==================== REAL PROBLEM SCENARIOS ==================== -->
  <section class="sec" id="scenarios">
    <div class="wrap">
      <div class="sec-head reveal">
        <span class="label">Real Case Scenarios</span>
        <h2>Real Customer Problems <em>We Solve Daily</em></h2>
        <p>Here are typical situations our teams resolve across Hyderabad residential and commercial premises:</p>
      </div>

      <div class="scenario-grid">
        <div class="scenario-card reveal">
          <div class="scenario-icon">
            <svg width="26" height="26" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364-.707-.707M6.343 6.343l-.707-.707m12.728 0-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 1 1-8 0 4 4 0 0 1 8 0Z"/></svg>
          </div>
          <h3 style="font-size:1.25rem; font-weight:700; margin-bottom:10px; color:var(--ink);">Overflow During Heavy Monsoon Rain</h3>
          <p style="color:var(--gray); font-size:0.92rem; line-height:1.6;">A villa in Balapur experienced severe wastewater bubbling near their side passage after heavy rain. The septic tank was already filled with sludge, and rain saturation caused immediate overflow. Our emergency tanker pumped out 5,000 liters within an hour, preventing interior damage.</p>
        </div>

        <div class="scenario-card reveal">
          <div class="scenario-icon">
            <svg width="26" height="26" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M19 21V5a2 2 0 0 0-2-2H7a2 2 0 0 0-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v5m-4 0h4"/></svg>
          </div>
          <h3 style="font-size:1.25rem; font-weight:700; margin-bottom:10px; color:var(--ink);">Apartment Multi-Flat Drainage Choke</h3>
          <p style="color:var(--gray); font-size:0.92rem; line-height:1.6;">In an LB Nagar housing complex, ground-floor bathrooms began backing up simultaneously. The main line connected to the community holding tank had clogged with solid grease. We combined water jetting with suction extraction, restoring smooth outflow for all 48 families.</p>
        </div>

        <div class="scenario-card reveal">
          <div class="scenario-icon">
            <svg width="26" height="26" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3Z"/></svg>
          </div>
          <h3 style="font-size:1.25rem; font-weight:700; margin-bottom:10px; color:var(--ink);">Toilet Backflow & Odor Near Living Areas</h3>
          <p style="color:var(--gray); font-size:0.92rem; line-height:1.6;">A family noticed recurring foul smells and slow flushing in their guest bathroom. When flushed, bubbles rose in the commode. We inspected the chamber, found a compacted sludge layer choking the inlet pipe, cleared the obstruction, and disinfected the chamber completely.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ==================== MODERN FLEET & CAPABILITIES ==================== -->
  <section class="sec" id="featured" style="background:#ffffff;">
    <div class="wrap">
      <div class="sec-head reveal">
        <span class="label">Our Modern Fleet</span>
        <h2>High-Power Vacuum Tech & <em>Sanitation Equipment</em></h2>
        <p>Equipped to handle any site condition: narrow residential lanes, deep underground STP basements, and massive industrial chambers:</p>
      </div>

      <div class="fac-strip" style="overflow-x:auto; display:flex; gap:20px; padding-bottom:16px;">
        <div class="fac-card reveal" style="min-width:320px; flex:1; background:#f8fafc; border:1px solid var(--line); border-radius:16px; overflow:hidden;">
          <img src="images/main-slider/eco-friendly-septic-services.webp" alt="High Capacity Eco-Friendly Vacuum Suction Tanker" style="width:100%; height:200px; object-fit:cover;" />
          <div style="padding:20px;">
            <h4 style="font-size:1.15rem; font-weight:700; margin-bottom:8px; color:var(--ink);">Heavy-Duty Vacuum Tankers</h4>
            <p style="color:var(--gray); font-size:0.88rem; line-height:1.5;">Capacities from 3,000 to 12,000 liters. Equipped with high-torque Italian vacuum pumps that lift heavy sludge without engine strain.</p>
          </div>
        </div>

        <div class="fac-card reveal" style="min-width:320px; flex:1; background:#f8fafc; border:1px solid var(--line); border-radius:16px; overflow:hidden;">
          <img src="images/resource/notch-septic-tank-cleaning-services.webp" alt="High Pressure Water Jetting and Desludging" style="width:100%; height:200px; object-fit:cover;" />
          <div style="padding:20px;">
            <h4 style="font-size:1.15rem; font-weight:700; margin-bottom:8px; color:var(--ink);">High-Pressure Jetting Systems</h4>
            <p style="color:var(--gray); font-size:0.88rem; line-height:1.5;">200+ bar pressurized water jets blast apart hardened grease, tree roots, scale, and stubborn debris inside underground pipes.</p>
          </div>
        </div>

        <div class="fac-card reveal" style="min-width:320px; flex:1; background:#f8fafc; border:1px solid var(--line); border-radius:16px; overflow:hidden;">
          <img src="images/resource/green-septic-solutions.webp" alt="Eco-Friendly Sanitation Chemical & Odor Control" style="width:100%; height:200px; object-fit:cover;" />
          <div style="padding:20px;">
            <h4 style="font-size:1.15rem; font-weight:700; margin-bottom:8px; color:var(--ink);">Eco Bio-Enzyme Treatments</h4>
            <p style="color:var(--gray); font-size:0.88rem; line-height:1.5;">Non-toxic, biological odor suppressants and microbial treatments that eliminate stench immediately and encourage natural digestion.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ==================== TESTIMONIALS SECTION ==================== -->
  <section class="sec testi" id="testimonials">
    <div class="wrap">
      <div class="sec-head reveal">
        <span class="label">Customer Reviews</span>
        <h2>Hear From Our <em>Happy Customers</em></h2>
        <p>Real feedback from homeowners, society secretaries, and facility managers across Hyderabad:</p>
      </div>

      <div class="t-wrap reveal">
        <div class="t-card">
          <div class="t-stars">
            <svg width="20" height="20" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
            <svg width="20" height="20" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
            <svg width="20" height="20" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
            <svg width="20" height="20" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
            <svg width="20" height="20" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
          </div>
          <p class="t-quote">
            "We faced severe sewage overflow during continuous rains in Balapur. The Green Septic team arrived within 40 minutes with a high-capacity vacuum tanker. They cleared the entire tank and cleaned the surrounding chamber spotless. Honest pricing and outstanding service!"
          </p>
          <div class="t-meta">
            <div>
              <b class="t-name">Narasimha Rao</b>
              <span class="t-role">Villa Owner, Balapur, Hyderabad</span>
            </div>
            <div class="t-nav">
              <button class="t-prev" aria-label="Previous testimonial" type="button">‹</button>
              <button class="t-next" aria-label="Next testimonial" type="button">›</button>
            </div>
          </div>
        </div>
        <div class="t-avs">
          <!-- Rendered via js/script.js -->
        </div>
      </div>
    </div>
  </section>

  <!-- ==================== SERVICE AREAS / HYDERABAD COVERAGE ==================== -->
  <section class="sec" id="areas" style="background:#f8fafc;">
    <div class="wrap">
      <div class="sec-head reveal">
        <span class="label">Local Service Areas</span>
        <h2>Fast Response Across <em>Greater Hyderabad & Secunderabad</em></h2>
        <p>With strategically deployed vacuum tankers stationed across Balapur, LB Nagar, and the IT corridor, we ensure rapid on-site arrival (30–45 mins):</p>
      </div>

      <div style="background:#ffffff; border:1px solid var(--line); border-radius:20px; padding:36px; box-shadow:0 8px 24px rgba(0,0,0,0.03);" class="reveal">
        <div style="display:flex; align-items:center; gap:12px; margin-bottom:20px;">
          <span style="font-size:1.4rem;">📍</span>
          <div>
            <h3 style="font-size:1.25rem; font-weight:700; color:var(--ink); margin:0;">Primary & Surrounding Coverage Zones</h3>
            <p style="color:var(--gray); font-size:0.88rem; margin:0;">Emergency service available across all the following localities:</p>
          </div>
        </div>

        <div class="area-tags">
          <span class="area-tag"><svg width="14" height="14" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd"/></svg> Balapur</span>
          <span class="area-tag"><svg width="14" height="14" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd"/></svg> LB Nagar</span>
          <span class="area-tag"><svg width="14" height="14" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd"/></svg> Dilsukhnagar</span>
          <span class="area-tag"><svg width="14" height="14" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd"/></svg> Champapet</span>
          <span class="area-tag"><svg width="14" height="14" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd"/></svg> Karmanghat</span>
          <span class="area-tag"><svg width="14" height="14" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd"/></svg> BN Reddy Nagar</span>
          <span class="area-tag"><svg width="14" height="14" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd"/></svg> Uppal</span>
          <span class="area-tag"><svg width="14" height="14" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd"/></svg> Nagole</span>
          <span class="area-tag"><svg width="14" height="14" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd"/></svg> Saroor Nagar</span>
          <span class="area-tag"><svg width="14" height="14" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd"/></svg> Gachibowli</span>
          <span class="area-tag"><svg width="14" height="14" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd"/></svg> Madhapur</span>
          <span class="area-tag"><svg width="14" height="14" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd"/></svg> Hitec City</span>
          <span class="area-tag"><svg width="14" height="14" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd"/></svg> Kondapur</span>
          <span class="area-tag"><svg width="14" height="14" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd"/></svg> Kukatpally</span>
          <span class="area-tag"><svg width="14" height="14" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd"/></svg> Miyapur</span>
          <span class="area-tag"><svg width="14" height="14" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd"/></svg> Banjara Hills</span>
          <span class="area-tag"><svg width="14" height="14" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd"/></svg> Jubilee Hills</span>
          <span class="area-tag"><svg width="14" height="14" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd"/></svg> Begumpet</span>
          <span class="area-tag"><svg width="14" height="14" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd"/></svg> Secunderabad</span>
          <span class="area-tag"><svg width="14" height="14" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd"/></svg> Shamshabad</span>
        </div>
      </div>
    </div>
  </section>

  <!-- ==================== ABOUT US SECTION ==================== -->
  <section class="sec" id="about">
    <div class="wrap about-g">
      <div class="reveal">
        <span class="label">About Our Company</span>
        <h2>Built on Trust. Driven by <em>20+ Years of Sanitation Excellence.</em></h2>
        <p class="ab-lead" style="font-size:1.1rem; line-height:1.7; color:var(--ink); margin-bottom:16px;">
          Established with the mission to bring scientific, modern, and hygienic sanitation solutions to Hyderabad, <b>Green Septic Tank Cleaning Services</b> has evolved into one of the region's most reputable sanitation and sludge management providers.
        </p>
        <p style="color:var(--gray); line-height:1.7; margin-bottom:20px;">
          Starting from Balapur, we grew our operations with state-of-the-art heavy vacuum tankers, professional drainage jetting tools, and rigorous environmental disposal standards. Today, we cater to independent home owners, multinational IT campuses, luxury hotels, private hospitals, and large industrial estates across Telangana.
        </p>
        <div style="display:flex; flex-wrap:wrap; gap:20px; margin-top:24px;">
          <div style="flex:1; min-width:200px; background:var(--green-tint); padding:18px; border-radius:12px; border:1px solid rgba(22,163,74,0.3);">
            <b style="color:#15803d; font-size:1.1rem; display:block; margin-bottom:4px;">100% Eco-Compliant</b>
            <span style="font-size:0.85rem; color:var(--gray);">Strict municipal disposal in designated biological facilities</span>
          </div>
          <div style="flex:1; min-width:200px; background:var(--green-tint); padding:18px; border-radius:12px; border:1px solid rgba(22,163,74,0.3);">
            <b style="color:#15803d; font-size:1.1rem; display:block; margin-bottom:4px;">Trained Personnel</b>
            <span style="font-size:0.85rem; color:var(--gray);">Full PPE gear, gas safety detectors, and certified protocols</span>
          </div>
        </div>
      </div>
      <div class="reveal">
        <div class="ab-figures" style="border-radius:20px; overflow:hidden; box-shadow:0 16px 36px rgba(0,0,0,0.08);">
          <img src="images/resource/reliable-septic-services.webp" alt="Green Septic Tank Cleaning Services Reliable Crew" style="width:100%; height:auto; display:block;" />
        </div>
      </div>
    </div>
  </section>

  <!-- ==================== CONTACT / BOOKING SECTION ==================== -->
  <section class="sec" id="contact" style="background:#f8fafc;">
    <div class="wrap">
      <div class="sec-head reveal">
        <span class="label">Book Tanker / Get Quote</span>
        <h2>Get in Touch <em>Today</em></h2>
        <p>Planning a routine cleaning or need an emergency suction tanker dispatched immediately? Send your details below or call our 24/7 hotline:</p>
      </div>

      <div class="contact-card reveal">
        <div class="cc-photo">
          <img src="images/background/clean-safe-septic-services.webp" alt="Green Septic Tank Cleaning Services Hyderabad Fleet" />
          <div class="cc-info">
            <h3 style="font-size:1.4rem; font-weight:800; margin-bottom:16px;">Contact Information</h3>
            <div class="cc-rows">
              <div class="cc-row">
                <span class="cc-ic">
                  <svg width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" viewBox="0 0 24 24"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2Z"/></svg>
                </span>
                <div>
                  <b>Phone / 24/7 Hotline</b>
                  <span>+91 94405 14057</span>
                </div>
              </div>

              <div class="cc-row">
                <span class="cc-ic">
                  <svg width="22" height="22" fill="currentColor" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/></svg>
                </span>
                <div>
                  <b>WhatsApp Direct</b>
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
                  <b>Main Office Address</b>
                  <span>45-591NP, Maruthi Nagar, Badangpet Village, Balapur Mandal, Ranga Reddy, Hyderabad - 500058, Telangana, India</span>
                </div>
              </div>

              <div class="cc-row">
                <span class="cc-ic">
                  <svg width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                </span>
                <div>
                  <b>Working Hours</b>
                  <span>Open 24 Hours / 7 Days a Week (Day & Night Emergency Dispatch)</span>
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
                  <option value="Drainage Blockage Unblocking">Drainage Blockage Unblocking</option>
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

  <!-- ==================== FAQS SECTION ==================== -->
  <section class="sec" id="faqs">
    <div class="wrap faq-g">
      <div class="faq-photos reveal">
        <img src="images/resource/notch-septic-tank-cleaning-services.webp" class="fp-1" alt="Green Septic Tank Inspection" />
        <img src="images/resource/safely-tank-cleaning-services.webp" class="fp-2" alt="Green Septic Tank Safety Protocols" />
      </div>

      <div>
        <div class="sec-head left reveal" style="margin-bottom:36px">
          <span class="label">Got Questions?</span>
          <h2>Frequently Asked <em>Questions</em></h2>
          <p>Common questions about septic tank cleaning, emergency response, costs, and maintenance in Hyderabad:</p>
        </div>

        <div class="faq-list">
          <details class="faq reveal" open>
            <summary>
              Do you provide 24/7 emergency septic tank cleaning?
              <span class="fx">−</span>
            </summary>
            <p class="a">
              Yes, absolutely! We handle urgent sewage overflow, toilet backflows, pipe bursts, and drainage choke-ups 24 hours a day, 7 days a week including Sundays and late-night emergencies. Our rapid tankers reach most Hyderabad locations within 30 to 45 minutes.
            </p>
          </details>

          <details class="faq reveal">
            <summary>
              How is the cost for septic tank cleaning determined?
              <span class="fx">+</span>
            </summary>
            <p class="a">
              Our pricing is completely honest and based on actual site conditions: tank capacity (e.g. 3,000L to 10,000L+), volume of solidified sludge, pipe reach distance from the tanker, and time of service. We quote a fixed, transparent price upfront before starting the work.
            </p>
          </details>

          <details class="faq reveal">
            <summary>
              How often should a residential septic tank be cleaned?
              <span class="fx">+</span>
            </summary>
            <p class="a">
              For an average family of 4 to 6 members, a residential septic tank should be inspected and pumped every 1 to 2 years. High-usage commercial premises, restaurants, and apartments require periodic desludging every 3 to 6 months to prevent sudden blockages.
            </p>
          </details>

          <details class="faq reveal">
            <summary>
              Will there be bad smell or mess around my house during cleaning?
              <span class="fx">+</span>
            </summary>
            <p class="a">
              No. We use heavy-duty sealed vacuum suction hoses that transfer waste directly from your underground chamber into our closed tanker truck without atmospheric exposure. Afterwards, we wash down the chamber opening and apply bio-neutralizers to eliminate residual odors completely.
            </p>
          </details>

          <details class="faq reveal">
            <summary>
              Do you clean Sewage Treatment Plants (STPs) and Grease Traps?
              <span class="fx">+</span>
            </summary>
            <p class="a">
              Yes, we specialize in complete STP plant desludging, settling chamber cleaning, aeration tank maintenance, and commercial grease trap pumping for apartments, hotels, and industrial sites across Hyderabad.
            </p>
          </details>

          <details class="faq reveal">
            <summary>
              Where do you dispose of the extracted septic waste?
              <span class="fx">+</span>
            </summary>
            <p class="a">
              We strictly adhere to Telangana State Pollution Control Board and municipal environmental regulations. All collected sewage is transported and safely discharged into authorized government sewage treatment facilities. We do not engage in illegal open dumping.
            </p>
          </details>
        </div>
      </div>
    </div>
  </section>

  <!-- ==================== BOTTOM HIGH-IMPACT CTA ==================== -->
  <section class="sec" style="background:#f8fafc; padding-bottom:70px;">
    <div class="wrap">
      <div class="cta-card reveal" style="text-align:center; padding:60px 24px; background:#ffffff; border:1px solid var(--line); border-radius:24px; box-shadow:0 12px 32px rgba(0,0,0,0.04);">
        <span class="label" style="display:inline-block; margin-bottom:12px;">Fast Local Support in Balapur & Greater Hyderabad</span>
        <h2 style="font-size:2.4rem; font-weight:800; color:var(--ink); margin-bottom:16px;">Ready to Restore Cleanliness & Eliminate Foul Odors?</h2>
        <p style="max-width:600px; margin:0 auto 28px; color:var(--gray); font-size:1.05rem; line-height:1.6;">
          Whether you need urgent sewage removal, drainage blockage clearing, or scheduled society maintenance, our fleet is ready to dispatch now. One call saves your property from severe sewage damage.
        </p>
        <div style="display:flex; justify-content:center; gap:16px; flex-wrap:wrap;">
          <a href="tel:+919440514057" class="btn btn-orange" style="padding:14px 28px; font-size:1.05rem;">
            <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2Z"/></svg>
            Call Now: +91 94405 14057
          </a>
          <a href="https://wa.me/919440514057?text=Hello%20Green%20Septic%20Tank%20Cleaning%20Services,%20I%20would%20like%20to%20book%20a%20tanker." class="btn btn-whatsapp" target="_blank" rel="noopener" style="padding:14px 28px; font-size:1.05rem;">
            <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/></svg>
            Book via WhatsApp
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- ==================== FOOTER ==================== -->
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
          <a href="#services">Our Services</a>
          <a href="#why">Why Choose Us</a>
          <a href="#works">How It Works</a>
          <a href="#areas">Service Areas</a>
          <a href="#testimonials">Client Reviews</a>
          <a href="#about">About Company</a>
          <a href="#faqs">FAQs</a>
          <a href="#contact">Contact Us</a>
        </div>

        <div class="f-col">
          <h4 style="color:#ffffff; font-size:1.05rem; font-weight:700; margin-bottom:16px;">Our Services</h4>
          <a href="#services">Residential Cleaning</a>
          <a href="#services">Commercial Septic</a>
          <a href="#services">STP Plant Cleaning</a>
          <a href="#services">Sludge Pumping</a>
          <a href="#services">Labour Camp Tanks</a>
          <a href="#services">Industrial Solutions</a>
          <a href="#services">Hospital Sanitation</a>
          <a href="#services">Drainage Jetting</a>
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

  <!-- ==================== FLOATING QUICK CONTACT DOCK ==================== -->
  <div class="floating-dock">
    <a href="https://wa.me/919440514057?text=Hello%20Green%20Septic%20Tank%20Cleaning%20Services,%20I%20need%20assistance." class="float-btn whatsapp" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">
      <svg viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/></svg>
    </a>
    <a href="tel:+919440514057" class="float-btn call" aria-label="Call +91 94405 14057">
      <svg viewBox="0 0 24 24"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2Z"/></svg>
    </a>
  </div>

  <!-- Scripts -->
  <script src="js/script.js"></script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_html)

print("Generated index.html successfully! Length:", len(index_html))
