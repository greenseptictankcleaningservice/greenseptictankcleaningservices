import re

with open("sb_style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Let's inspect the color replacements
# Replace #fe5922 with #16a34a (vibrant green)
# Replace #e8480f with #15803d (dark green)
# Replace #fef5ef with #f0fdf4 (soft green tint)
# Replace rgba(254,89,34,... with rgba(22,163,74,...

new_css = css

# Replace specific hex codes
new_css = re.sub(r'#fe5922\b', '#16a34a', new_css, flags=re.I)
new_css = re.sub(r'#e8480f\b', '#15803d', new_css, flags=re.I)
new_css = re.sub(r'#fef5ef\b', '#f0fdf4', new_css, flags=re.I)
new_css = re.sub(r'rgba\(254,\s*89,\s*34,', 'rgba(22, 163, 74,', new_css)
new_css = re.sub(r'rgba\(254,\s*89,\s*34\s*,', 'rgba(22, 163, 74,', new_css)

# Add custom Green Septic Tank CSS rules at the end
custom_addons = """
/* ==========================================================================
   GREEN SEPTIC TANK CLEANING SERVICES - CUSTOM EXTENSIONS & POLISH
   ========================================================================== */

:root {
  --green: #16a34a;
  --green-dark: #15803d;
  --green-light: #22c55e;
  --green-tint: #ecfdf5;
  --whatsapp: #25D366;
}

/* Enhanced logo & brand */
.brand {
  display: flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
}
.brand img.brand-logo {
  height: 48px;
  width: auto;
  object-fit: contain;
  filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));
}
.brand .brand-text {
  display: flex;
  flex-direction: column;
}
.brand .brand-text b {
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--ink);
  line-height: 1.1;
  letter-spacing: -0.02em;
}
.brand .brand-text span {
  font-size: 0.72rem;
  font-weight: 600;
  text-transform: uppercase;
  color: var(--green);
  letter-spacing: 0.05em;
}
nav.scrolled .brand .brand-text b {
  color: var(--ink);
}
nav:not(.scrolled) .brand .brand-text b {
  color: #ffffff;
}
nav:not(.scrolled) .brand .brand-text span {
  color: #4ade80;
}

/* Emergency indicator pulse */
.live-pill {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(22, 163, 74, 0.12);
  border: 1px solid rgba(22, 163, 74, 0.3);
  padding: 6px 14px;
  border-radius: 9999px;
  font-size: 0.82rem;
  font-weight: 600;
  color: #15803d;
}
.live-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background-color: #22c55e;
  box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.7);
  animation: pulse-green 2s infinite;
}
@keyframes pulse-green {
  0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.7); }
  70% { transform: scale(1); box-shadow: 0 0 0 8px rgba(34, 197, 94, 0); }
  100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(34, 197, 94, 0); }
}

/* Button variants */
.btn-whatsapp {
  background: #25D366;
  color: #ffffff !important;
  border: 1px solid #20ba59;
  display: inline-flex;
  align-items: center;
  gap: 8px;
}
.btn-whatsapp:hover {
  background: #1eb857;
  color: #ffffff !important;
  transform: translateY(-1px);
}

/* Floating Contact Dock */
.floating-dock {
  position: fixed;
  bottom: 24px;
  right: 24px;
  z-index: 999;
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.float-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 54px;
  height: 54px;
  border-radius: 50%;
  box-shadow: 0 8px 24px rgba(0,0,0,0.22);
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  text-decoration: none;
}
.float-btn:hover {
  transform: translateY(-3px) scale(1.05);
}
.float-btn.whatsapp {
  background: #25D366;
  color: #fff;
}
.float-btn.call {
  background: #16a34a;
  color: #fff;
}
.float-btn svg {
  width: 26px;
  height: 26px;
  fill: currentColor;
}

/* Service filter tabs */
.svc-tabs {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin: 28px 0 36px;
}
.svc-tab-btn {
  background: var(--light);
  border: 1px solid var(--line);
  color: var(--ink);
  padding: 8px 18px;
  border-radius: 9999px;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}
.svc-tab-btn:hover, .svc-tab-btn.active {
  background: var(--green);
  border-color: var(--green);
  color: #ffffff;
}

/* Service Card Image styling */
.cat-media {
  position: relative;
  width: 100%;
  height: 220px;
  overflow: hidden;
  border-radius: 12px;
  background: #e2e8f0;
}
.cat-media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.4s ease;
}
.cat-card:hover .cat-media img {
  transform: scale(1.05);
}
.cat-badge {
  position: absolute;
  top: 12px;
  left: 12px;
  background: rgba(15, 23, 42, 0.85);
  backdrop-filter: blur(8px);
  color: #ffffff;
  padding: 4px 10px;
  border-radius: 6px;
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.03em;
}

/* Problem Scenarios Cards */
.scenario-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 24px;
  margin-top: 36px;
}
.scenario-card {
  background: #ffffff;
  border: 1px solid var(--line);
  border-radius: 16px;
  padding: 28px;
  transition: transform 0.25s ease, box-shadow 0.25s ease;
  position: relative;
}
.scenario-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 16px 32px rgba(0,0,0,0.06);
  border-color: rgba(22, 163, 74, 0.4);
}
.scenario-icon {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  background: var(--green-tint);
  color: var(--green);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 18px;
}

/* Hyderabad Location Tags */
.area-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 16px;
}
.area-tag {
  background: #ffffff;
  border: 1px solid var(--line);
  color: var(--ink);
  padding: 6px 14px;
  border-radius: 8px;
  font-size: 0.85rem;
  font-weight: 500;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: all 0.2s ease;
}
.area-tag:hover {
  border-color: var(--green);
  color: var(--green);
  background: var(--green-tint);
}
.area-tag svg {
  color: var(--green);
}

/* Testimonial Stars */
.t-stars {
  display: flex;
  gap: 3px;
  color: #f59e0b;
  margin-bottom: 12px;
}
"""

new_css += custom_addons

import os
os.makedirs("css", exist_ok=True)
with open("css/style.css", "w", encoding="utf-8") as f:
    f.write(new_css)

print("Generated css/style.css:", len(new_css), "bytes")
