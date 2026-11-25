
(function () {
  'use strict';

  var isReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  var nav = document.querySelector('nav');
  function handleScroll() {
    if (nav) {
      nav.classList.toggle('scrolled', window.scrollY > 40);
    }
  }
  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();

  var burger = document.getElementById('navBurger');
  var panel = document.getElementById('navPanel');
  if (burger && panel) {
    function toggleMenu(open) {
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
      if (open) {
        panel.hidden = false;
        panel.setAttribute('data-open', '1');
        if (nav) nav.classList.add('scrolled');
      } else {
        panel.removeAttribute('data-open');
        panel.hidden = true;
        handleScroll();
      }
    }
    burger.addEventListener('click', function () {
      var isOpen = burger.getAttribute('aria-expanded') === 'true';
      toggleMenu(!isOpen);
    });
    panel.addEventListener('click', function (e) {
      if (e.target.closest('a')) {
        toggleMenu(false);
      }
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') toggleMenu(false);
    });
    window.addEventListener('resize', function () {
      if (window.innerWidth > 920) toggleMenu(false);
    });
  }

  function initHeroMotion() {
    var hero = document.querySelector('.hero');
    var heroImg = document.querySelector('.hero-img');
    if (!hero || !heroImg) return;

    if (typeof gsap === 'undefined') return;

    var hasHover = window.matchMedia('(hover: hover) and (pointer: fine)').matches;

    if (isReducedMotion) {
      gsap.set(['.hero-img', '.hero-badge', '.hero h1', '.hero-desc', '.hero-btns .btn', '.hero-rev', '.avs img'], {
        opacity: 1,
        y: 0,
        x: 0,
        scale: 1
      });
      return;
    }

    var heroTl = gsap.timeline({ defaults: { ease: 'power3.out' } });

    heroTl.fromTo(heroImg,
      { scale: 1.18 },
      { scale: 1.06, duration: 2.2, ease: 'power2.out' },
      0
    );

    var heroBadge = hero.querySelector('.hero-badge');
    if (heroBadge) {
      heroTl.fromTo(heroBadge,
        { y: -22, opacity: 0 },
        { y: 0, opacity: 1, duration: 0.8 },
        0.15
      );
    }

    var heroTitle = hero.querySelector('h1');
    if (heroTitle) {
      heroTl.fromTo(heroTitle,
        { y: 32, opacity: 0 },
        { y: 0, opacity: 1, duration: 1.0 },
        0.3
      );
    }

    var heroDesc = hero.querySelector('.hero-desc');
    if (heroDesc) {
      heroTl.fromTo(heroDesc,
        { y: 22, opacity: 0 },
        { y: 0, opacity: 1, duration: 0.9 },
        0.45
      );
    }

    var heroBtns = hero.querySelectorAll('.hero-btns .btn');
    if (heroBtns.length) {
      heroTl.fromTo(heroBtns,
        { y: 20, opacity: 0, scale: 0.96 },
        { y: 0, opacity: 1, scale: 1, duration: 0.7, stagger: 0.12, ease: 'back.out(1.5)' },
        0.6
      );
    }

    var heroRev = hero.querySelector('.hero-rev');
    var heroAvatars = hero.querySelectorAll('.avs img');
    var heroRevMeta = hero.querySelector('.rev-meta');
    if (heroRev) {
      heroTl.fromTo(heroRev,
        { opacity: 0, y: 18 },
        { opacity: 1, y: 0, duration: 0.8 },
        0.75
      );
      if (heroAvatars.length) {
        heroTl.fromTo(heroAvatars,
          { scale: 0, opacity: 0 },
          { scale: 1, opacity: 1, duration: 0.5, stagger: 0.08, ease: 'back.out(2)' },
          0.85
        );
      }
      if (heroRevMeta) {
        heroTl.fromTo(heroRevMeta,
          { opacity: 0, x: -10 },
          { opacity: 1, x: 0, duration: 0.6 },
          1.0
        );
      }
    }

    if (typeof ScrollTrigger !== 'undefined') {
      gsap.to(heroImg, {
        yPercent: 18,
        ease: 'none',
        scrollTrigger: {
          trigger: hero,
          start: 'top top',
          end: 'bottom top',
          scrub: true
        }
      });

      var heroIn = hero.querySelector('.hero-in');
      if (heroIn) {
        gsap.to(heroIn, {
          yPercent: -12,
          opacity: 0.25,
          ease: 'none',
          scrollTrigger: {
            trigger: hero,
            start: 'top top',
            end: 'bottom 40%',
            scrub: true
          }
        });
      }
    }

    if (hasHover) {
      hero.addEventListener('mousemove', function (e) {
        var rect = hero.getBoundingClientRect();
        var xRel = (e.clientX - rect.left) / rect.width - 0.5;
        var yRel = (e.clientY - rect.top) / rect.height - 0.5;

        gsap.to(heroImg, {
          x: xRel * -22,
          y: yRel * -16,
          duration: 0.7,
          ease: 'power1.out',
          overwrite: 'auto'
        });

        var heroIn = hero.querySelector('.hero-in');
        if (heroIn) {
          gsap.to(heroIn, {
            x: xRel * 10,
            y: yRel * 8,
            duration: 0.7,
            ease: 'power1.out',
            overwrite: 'auto'
          });
        }
      });

      hero.addEventListener('mouseleave', function () {
        gsap.to(heroImg, {
          x: 0,
          y: 0,
          duration: 0.9,
          ease: 'power2.out'
        });
        var heroIn = hero.querySelector('.hero-in');
        if (heroIn) {
          gsap.to(heroIn, {
            x: 0,
            y: 0,
            duration: 0.9,
            ease: 'power2.out'
          });
        }
      });
    }
  }

  initHeroMotion();

  var reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && !isReducedMotion) {
    var revealObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('in');
          revealObserver.unobserve(entry.target);
        }
      });
    }, { rootMargin: '0px 0px -40px 0px', threshold: 0.1 });
    reveals.forEach(function (el) {
      revealObserver.observe(el);
    });
  } else {
    reveals.forEach(function (el) {
      el.classList.add('in');
    });
  }

  var countElements = document.querySelectorAll('[data-count]');
  if ('IntersectionObserver' in window) {
    var countObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          var el = entry.target;
          var targetVal = parseInt(el.getAttribute('data-count'), 10);
          if (!isNaN(targetVal)) {
            var startTime = null;
            var duration = 1800;
            function step(timestamp) {
              if (!startTime) startTime = timestamp;
              var progress = Math.min((timestamp - startTime) / duration, 1);
              var easeProgress = 1 - Math.pow(1 - progress, 3);
              el.textContent = Math.floor(easeProgress * targetVal);
              if (progress < 1) {
                requestAnimationFrame(step);
              } else {
                el.textContent = targetVal;
              }
            }
            requestAnimationFrame(step);
          }
          countObserver.unobserve(el);
        }
      });
    }, { threshold: 0.2 });
    countElements.forEach(function (el) {
      countObserver.observe(el);
    });
  } else {
    countElements.forEach(function (el) {
      el.textContent = el.getAttribute('data-count');
    });
  }

  var testData = [
    {
      q: "“We live in the Dilsukhnagar area, and last night heavy rainfall flooded our property due to a blocked manhole. Found Green Septic Tank Cleaning Services on Google Maps and called them immediately. They answered within seconds, arrived on time with required equipment, and cleared all accumulated water by removing the manhole blockage. Highly experienced, worked professionally, and very affordable pricing. Highly recommend them across Hyderabad!”",
      n: "Shanthan",
      r: "Verified Google Review · Dilsukhnagar, Hyderabad",
      av: "images/resource/avatar-1.webp",
      ph: "images/resource/residential-septic-tank.webp"
    },
    {
      q: "“Mr. Das and his co-worker cleaned the septic tank and all manholes inside the house very nicely. They have done an extremely good job with their modern vacuum tanker. Honest, reasonable price and prompt arrival. I highly recommend Mr. Das and Green Septic Tank Cleaning Services to everyone in Hyderabad.”",
      n: "Venkatraman Athreya",
      r: "Verified Google Review · Hyderabad",
      av: "images/resource/avatar-2.webp",
      ph: "images/resource/commercial-septic-tank-cleaning.webp"
    },
    {
      q: "“Fast and reliable service! Their team arrived right on schedule with a heavy vacuum suction truck. Thoroughly pumped out the septic tank and cleared the drain line without any mess or lingering odor. Very reasonable rates and professional behavior. Truly 5-star septic service in Hyderabad.”",
      n: "Raja Simha Reddy Police",
      r: "Verified Google Review · Hyderabad",
      av: "images/resource/avatar-3.webp",
      ph: "images/resource/notch-septic-tank-cleaning-services.webp"
    },
    {
      q: "“Good service, work neat ga chesaru 👍. They brought long suction hoses that reached our interior backyard easily. Cleaned the septic tank completely and left the premises spotless. Very polite workers and punctual dispatch.”",
      n: "Kethavath Sharath",
      r: "Verified Google Review · Hyderabad",
      av: "images/resource/avatar-4.webp",
      ph: "images/resource/labour-camp-septic-tank.webp"
    },
    {
      q: "“Excellent services and timely work. Their commercial-grade vacuum suction tanker reached within 35 minutes of calling. Handled the sludge extraction safely and transported it directly to authorized STPs. Best septic tank cleaner in Greater Hyderabad.”",
      n: "Photo Teaser",
      r: "Verified Google Review · Hyderabad",
      av: "images/resource/avatar-1.webp",
      ph: "images/resource/residential-septic-tank.webp"
    },
    {
      q: "“Excellent worker, time to time working! Punctual arrival, heavy-duty suction machinery, and transparent upfront charges. Very polite crew and clean execution. Highly recommended for all residential and commercial septic cleaning.”",
      n: "Jarupla Thirupathi",
      r: "Verified Google Review · Hyderabad",
      av: "images/resource/avatar-2.webp",
      ph: "images/resource/commercial-septic-tank-cleaning.webp"
    }
  ];

  var tQuote = document.getElementById("tQuote");
  var tName = document.getElementById("tName");
  var tRole = document.getElementById("tRole");
  var tPhoto = document.getElementById("tPhoto");
  var tAvatars = document.getElementById("tAvatars");
  var tCard = document.getElementById("tCard");
  var tPrev = document.getElementById("tPrev");
  var tNext = document.getElementById("tNext");

  if (tQuote && tAvatars && tCard) {
    var p = 0;
    var tTimer = null;
    var isReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    function updateTestimonialSlide() {
      var item = testData[p];
      if (tQuote) tQuote.textContent = item.q;
      if (tName) tName.textContent = item.n;
      if (tRole) {
        tRole.innerHTML = '<span class="t-google-tag"><svg width="13" height="13" viewBox="0 0 24 24" style="vertical-align:-1px; margin-right:4px;" aria-hidden="true"><path fill="#4285F4" d="M23.745 12.27c0-.7-.06-1.4-.19-2.07H12v4.51h6.6c-.29 1.52-1.14 2.82-2.4 3.68v3.05h3.88c2.27-2.09 3.66-5.17 3.66-9.17z"/><path fill="#34A853" d="M12 24c3.24 0 5.95-1.08 7.93-2.91l-3.88-3.05c-1.08.72-2.45 1.16-4.05 1.16-3.12 0-5.77-2.1-6.72-4.93H1.25v3.15C3.27 21.4 7.35 24 12 24z"/><path fill="#FBBC05" d="M5.28 14.27c-.25-.72-.38-1.49-.38-2.27s.13-1.55.38-2.27V6.58H1.25C.45 8.18 0 9.99 0 12s.45 3.82 1.25 5.42l4.03-3.15z"/><path fill="#EA4335" d="M12 4.75c1.77 0 3.35.61 4.6 1.8l3.42-3.42C17.95 1.19 15.24 0 12 0 7.35 0 3.27 2.6 1.25 6.58l4.03 3.15c.95-2.83 3.6-4.98 6.72-4.98z"/></svg>' + item.r + '</span>';
      }
      if (tPhoto) {
        tPhoto.src = item.ph;
        tPhoto.alt = item.n + " - " + item.r;
      }
      Array.prototype.forEach.call(tAvatars.children, function (el, idx) {
        el.classList.remove("on");
        if (idx === p) {
          void el.offsetWidth;
          el.classList.add("on");
        }
      });
    }

    function goToTestimonial(idx) {
      p = (idx + testData.length) % testData.length;
      if (isReducedMotion) {
        updateTestimonialSlide();
        resetTestimonialTimer();
        return;
      }
      tCard.style.transition = "opacity .25s ease";
      tCard.style.opacity = "0";
      setTimeout(function () {
        updateTestimonialSlide();
        tCard.style.opacity = "1";
      }, 250);
      resetTestimonialTimer();
    }

    function resetTestimonialTimer() {
      if (tTimer) clearInterval(tTimer);
      tTimer = setInterval(function () {
        goToTestimonial(p + 1);
      }, 7000);
    }

    tAvatars.innerHTML = "";
    testData.forEach(function (item, idx) {
      var span = document.createElement("span");
      span.className = "t-av" + (idx === 0 ? " on" : "");
      span.setAttribute("role", "button");
      span.setAttribute("tabindex", "0");
      span.setAttribute("aria-label", "Show testimonial " + (idx + 1) + ": " + item.n);
      var img = document.createElement("img");
      img.src = item.av;
      img.alt = item.n;
      span.addEventListener("click", function () {
        goToTestimonial(idx);
      });
      span.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          goToTestimonial(idx);
        }
      });
      span.appendChild(img);
      tAvatars.appendChild(span);
    });

    updateTestimonialSlide();
    resetTestimonialTimer();

    if (tPrev) {
      tPrev.addEventListener("click", function () {
        goToTestimonial(p - 1);
      });
    }
    if (tNext) {
      tNext.addEventListener("click", function () {
        goToTestimonial(p + 1);
      });
    }
  }

  var filterButtons = document.querySelectorAll('.svc-tab-btn');
  var serviceCards = document.querySelectorAll('.cat-card[data-category]');
  if (filterButtons.length && serviceCards.length) {
    filterButtons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        filterButtons.forEach(function (b) { b.classList.remove('active'); });
        btn.classList.add('active');
        var cat = btn.getAttribute('data-filter');
        serviceCards.forEach(function (card) {
          var cardCats = card.getAttribute('data-category') || '';
          if (cat === 'all' || cardCats.includes(cat)) {
            card.style.display = '';
            card.style.opacity = '0';
            setTimeout(function () {
              card.style.transition = 'opacity 0.3s ease';
              card.style.opacity = '1';
            }, 50);
          } else {
            card.style.display = 'none';
          }
        });
      });
    });
  }

  var faqItems = document.querySelectorAll('.faq details, details.faq');
  faqItems.forEach(function (detail) {
    detail.addEventListener('toggle', function () {
      var span = detail.querySelector('.fx');
      if (span) {
        span.textContent = detail.open ? '−' : '+';
      }
    });
  });

  var quoteForm = document.getElementById('quoteForm');
  if (quoteForm) {
    quoteForm.addEventListener('submit', function (e) {
      e.preventDefault();
      var t = e.target;
      var getVal = function (name) {
        return t.elements[name] && t.elements[name].value ? t.elements[name].value.trim() : '';
      };

      var fname = getVal('fname');
      var lname = getVal('lname');
      var fullName = (fname + ' ' + lname).trim() || getVal('name') || 'Customer';
      var phone = getVal('phone') || '';
      var email = getVal('email') || '';
      var service = getVal('type') || getVal('service') || 'Septic Tank Cleaning';
      var area = getVal('area') || '';
      var urgency = getVal('urgency') || '';
      var message = getVal('msg') || getVal('message') || '';

      var lines = [
        "Hello Green Septic Tank Cleaning Services,",
        "I would like to request a quote / book a service:",
        "• Name: " + fullName,
        "• Phone: " + phone
      ];
      if (email) {
        lines.push("• Email: " + email);
      }
      if (service) {
        lines.push("• Service: " + service);
      }
      if (area) {
        lines.push("• Locality / Area: " + area);
      }
      if (urgency) {
        lines.push("• Urgency: " + urgency);
      }
      if (message) {
        lines.push("• Details: " + message);
      }
      lines.push("Please confirm vehicle availability and cost estimate.");

      var waText = lines.join("\n");
      var waUrl = "https://wa.me/919440514057?text=" + encodeURIComponent(waText);

      var submitBtn = t.querySelector('button[type="submit"]');
      if (submitBtn) {
        submitBtn.disabled = true;
        var btnSpan = submitBtn.querySelector('span:not(.circle)');
        if (btnSpan) {
          btnSpan.textContent = 'Redirecting to WhatsApp...';
        } else {
          submitBtn.textContent = 'Redirecting to WhatsApp...';
        }
      }

      window.location.href = waUrl;
    });
  }

  var facTrack = document.getElementById("facTrack");
  if (facTrack) {
    var rawCards = Array.prototype.slice.call(facTrack.children);
    var strip = document.createElement("div");
    strip.className = "fac-strip";

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

    facTrack.addEventListener("mouseenter", pauseMarquee);
    facTrack.addEventListener("mouseleave", function () { resumeMarquee(300); });

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

  var topBtn = document.getElementById('topBtn');
  if (topBtn) {
    window.addEventListener('scroll', function () {
      topBtn.classList.toggle('show', window.scrollY > 400);
    }, { passive: true });
    topBtn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  function initCircleButtons() {

    var buttons = document.querySelectorAll('.btn:not(.nav-burger), .t-arrow');

    buttons.forEach(function (btn) {

      var circle = btn.querySelector('.circle');
      if (!circle) {
        circle = document.createElement('span');
        circle.className = 'circle';
        circle.setAttribute('aria-hidden', 'true');
        btn.prepend(circle);
      }

      Array.from(btn.childNodes).forEach(function (node) {
        if (node.nodeType === Node.TEXT_NODE && node.textContent.trim().length > 0) {
          var wrapper = document.createElement('span');
          wrapper.textContent = node.textContent;
          node.parentNode.replaceChild(wrapper, node);
        }
      });

      function updatePos(e) {
        var rect = btn.getBoundingClientRect();
        circle.style.top = (e.clientY - rect.top) + 'px';
        circle.style.left = (e.clientX - rect.left) + 'px';
      }

      btn.addEventListener('mouseenter', updatePos);
      btn.addEventListener('mousemove', updatePos);
      btn.addEventListener('mouseleave', updatePos);
    });
  }

  initCircleButtons();

  function initWhyCardsStagger() {
    if (typeof gsap === 'undefined') return;

    if (typeof ScrollTrigger !== 'undefined') {
      gsap.registerPlugin(ScrollTrigger);
    }

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
          stagger: 0.12,
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

  function initWorksMotion() {
    var worksSec = document.getElementById('works');
    if (!worksSec) return;

    var n1 = document.getElementById('fNode1');
    var n2 = document.getElementById('fNode2');
    var n3 = document.getElementById('fNode3');
    var n4 = document.getElementById('fNode4');
    if (!n1 || !n2 || !n3 || !n4) return;

    var c1 = n1.querySelector('.node-circle');
    var c2 = n2.querySelector('.node-circle');
    var c3 = n3.querySelector('.node-circle');
    var c4 = n4.querySelector('.node-circle');

    var svg = document.getElementById('flowSvg');
    var path12 = document.getElementById('activePath12');
    var path23 = document.getElementById('activePath23');
    var path34 = document.getElementById('activePath34');
    var guide12 = document.getElementById('guidePath12');
    var guide23 = document.getElementById('guidePath23');
    var guide34 = document.getElementById('guidePath34');

    var travelCall = document.getElementById('travelCall');
    var travelTo3 = document.getElementById('travelTo3');
    var travelTo4 = document.getElementById('travelTo4');
    var allNodes = [n1, n2, n3, n4];

    if (typeof gsap === 'undefined') return;
    if (typeof MotionPathPlugin !== 'undefined') {
      gsap.registerPlugin(MotionPathPlugin);
    }
    if (typeof ScrollTrigger !== 'undefined') {
      gsap.registerPlugin(ScrollTrigger);
    }

    var masterTl = null;

    function calculateAndBuildMotion() {
      if (masterTl) {
        masterTl.kill();
      }

      var container = document.getElementById('worksFlow');
      if (!container) return;
      var cRect = container.getBoundingClientRect();

      function getCenter(el) {
        var r = el.getBoundingClientRect();
        return {
          x: r.left + r.width / 2 - cRect.left,
          y: r.top + r.height / 2 - cRect.top
        };
      }

      var p1 = getCenter(c1);
      var p2 = getCenter(c2);
      var p3 = getCenter(c3);
      var p4 = getCenter(c4);

      svg.setAttribute('viewBox', '0 0 ' + cRect.width + ' ' + cRect.height);

      var midY12 = Math.min(p1.y, p2.y) - 35;
      var d12 = 'M ' + p1.x + ' ' + p1.y + ' C ' + (p1.x + (p2.x - p1.x) * 0.45) + ' ' + midY12 + ', ' + (p1.x + (p2.x - p1.x) * 0.55) + ' ' + midY12 + ', ' + p2.x + ' ' + p2.y;
      path12.setAttribute('d', d12);
      if (guide12) guide12.setAttribute('d', d12);

      var midY23 = Math.min(p2.y, p3.y) - 35;
      var d23 = 'M ' + p2.x + ' ' + p2.y + ' C ' + (p2.x + (p3.x - p2.x) * 0.45) + ' ' + midY23 + ', ' + (p2.x + (p3.x - p2.x) * 0.55) + ' ' + midY23 + ', ' + p3.x + ' ' + p3.y;
      path23.setAttribute('d', d23);
      if (guide23) guide23.setAttribute('d', d23);

      var midY34 = Math.min(p3.y, p4.y) - 35;
      var d34 = 'M ' + p3.x + ' ' + p3.y + ' C ' + (p3.x + (p4.x - p3.x) * 0.45) + ' ' + midY34 + ', ' + (p3.x + (p4.x - p3.x) * 0.55) + ' ' + midY34 + ', ' + p4.x + ' ' + p4.y;
      path34.setAttribute('d', d34);
      if (guide34) guide34.setAttribute('d', d34);

      var len12 = path12.getTotalLength() || 350;
      var len23 = path23.getTotalLength() || 350;
      var len34 = path34.getTotalLength() || 350;

      gsap.set(travelCall, { x: p1.x, y: p1.y, xPercent: -50, yPercent: -50, autoAlpha: 0, scale: 0.6 });
      gsap.set(travelTo3, { x: p2.x, y: p2.y, xPercent: -50, yPercent: -50, autoAlpha: 0, scale: 0.6 });
      gsap.set(travelTo4, { x: p3.x, y: p3.y, xPercent: -50, yPercent: -50, autoAlpha: 0, scale: 0.6 });

      gsap.set(path12, { strokeDasharray: len12, strokeDashoffset: len12 });
      gsap.set(path23, { strokeDasharray: len23, strokeDashoffset: len23 });
      gsap.set(path34, { strokeDasharray: len34, strokeDashoffset: len34 });

      if (isReducedMotion) {
        allNodes.forEach(function (n) { n.classList.add('active'); });
        gsap.set([path12, path23, path34], { strokeDashoffset: 0 });
        return;
      }

      masterTl = gsap.timeline({
        repeat: -1,
        repeatDelay: 2.2,
        scrollTrigger: {
          trigger: '#works',
          start: 'top 75%',
          toggleActions: 'play pause resume pause'
        }
      });

      masterTl
        .call(function () {
          allNodes.forEach(function (n, idx) {
            n.classList.toggle('active', idx === 0);
          });
        })
        .set([path12, path23, path34], { strokeDashoffset: function (i) { return [len12, len23, len34][i]; } })
        .set([travelCall, travelTo3, travelTo4], { autoAlpha: 0, scale: 0.6 })
        .set(travelCall, { x: p1.x, y: p1.y, xPercent: -50, yPercent: -50 })
        .set(travelTo3, { x: p2.x, y: p2.y, xPercent: -50, yPercent: -50 })
        .set(travelTo4, { x: p3.x, y: p3.y, xPercent: -50, yPercent: -50 })
        .fromTo(c1, { scale: 0.95 }, { scale: 1.12, duration: 0.45, yoyo: true, repeat: 1, ease: 'power2.out' })

        .to(travelCall, { autoAlpha: 1, scale: 1, duration: 0.35, ease: 'back.out(1.7)' })
        .to(path12, { strokeDashoffset: 0, duration: 1.4, ease: 'power2.inOut' }, '-=0.15')
        .to(travelCall, {
          motionPath: {
            path: '#activePath12',
            align: '#activePath12',
            alignOrigin: [0.5, 0.5],
            autoRotate: false
          },
          duration: 1.4,
          ease: 'power2.inOut'
        }, '<')

        .to(travelCall, { scale: 1.3, autoAlpha: 0, duration: 0.28, ease: 'power1.in' })
        .call(function () {
          n2.classList.add('active');
        })
        .fromTo(c2, { scale: 0.9 }, { scale: 1.2, duration: 0.45, yoyo: true, repeat: 1, ease: 'back.out(2)' }, '<')

        .to({}, { duration: 0.35 })

        .set(travelTo3, { x: p2.x, y: p2.y, xPercent: -50, yPercent: -50 })
        .to(travelTo3, { autoAlpha: 1, scale: 1, duration: 0.35, ease: 'back.out(1.7)' })
        .to(path23, { strokeDashoffset: 0, duration: 1.4, ease: 'power2.inOut' }, '-=0.15')
        .to(travelTo3, {
          motionPath: {
            path: '#activePath23',
            align: '#activePath23',
            alignOrigin: [0.5, 0.5],
            autoRotate: false
          },
          duration: 1.4,
          ease: 'power2.inOut'
        }, '<')

        .to(travelTo3, { scale: 1.3, autoAlpha: 0, duration: 0.28, ease: 'power1.in' })
        .call(function () {
          n3.classList.add('active');
        })
        .fromTo(c3, { scale: 0.9 }, { scale: 1.2, duration: 0.45, yoyo: true, repeat: 1, ease: 'back.out(2)' }, '<')

        .to({}, { duration: 0.35 })

        .set(travelTo4, { x: p3.x, y: p3.y, xPercent: -50, yPercent: -50 })
        .to(travelTo4, { autoAlpha: 1, scale: 1, duration: 0.35, ease: 'back.out(1.7)' })
        .to(path34, { strokeDashoffset: 0, duration: 1.4, ease: 'power2.inOut' }, '-=0.15')
        .to(travelTo4, {
          motionPath: {
            path: '#activePath34',
            align: '#activePath34',
            alignOrigin: [0.5, 0.5],
            autoRotate: false
          },
          duration: 1.4,
          ease: 'power2.inOut'
        }, '<')

        .to(travelTo4, { scale: 1.3, autoAlpha: 0, duration: 0.28, ease: 'power1.in' })
        .call(function () {
          n4.classList.add('active');
        })
        .fromTo(c4, { scale: 0.9 }, { scale: 1.2, duration: 0.45, yoyo: true, repeat: 1, ease: 'back.out(2)' }, '<')

        .to({}, { duration: 2.2 });
    }

    calculateAndBuildMotion();

    var resizeTimer = null;
    window.addEventListener('resize', function () {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(calculateAndBuildMotion, 250);
    }, { passive: true });
  }

  initWorksMotion();

  function initCtaMotion() {
    var ctaCard = document.getElementById('ctaCard');
    if (!ctaCard) return;

    var ctaBg = ctaCard.querySelector('.cta-bg');
    var decoL = ctaCard.querySelector('.cd-l');
    var decoR = ctaCard.querySelector('.cd-r');
    var badge = ctaCard.querySelector('.cta-badge');
    var title = ctaCard.querySelector('.cta-inner h2');
    var text = ctaCard.querySelector('.cta-inner p');
    var btns = ctaCard.querySelector('.cta-inner .btns');

    if (typeof gsap === 'undefined') return;

    if (typeof ScrollTrigger !== 'undefined' && !isReducedMotion) {
      var ctaTl = gsap.timeline({
        scrollTrigger: {
          trigger: '#bottomCta',
          start: 'top 85%',
          toggleActions: 'play none none none',
          once: true
        }
      });

      ctaTl
        .fromTo(ctaCard,
          { opacity: 0, y: 45, scale: 0.95 },
          { opacity: 1, y: 0, scale: 1, duration: 0.85, ease: 'power2.out' }
        )
        .fromTo([badge, title, text, btns],
          { opacity: 0, y: 22 },
          { opacity: 1, y: 0, duration: 0.55, stagger: 0.1, ease: 'power2.out' },
          '-=0.45'
        )
        .fromTo([decoL, decoR],
          { opacity: 0, scale: 0.7 },
          { opacity: 0.9, scale: 1, duration: 0.7, stagger: 0.12, ease: 'back.out(1.7)' },
          '-=0.4'
        );

      if (ctaBg) {
        gsap.fromTo(ctaBg,
          { yPercent: -6 },
          {
            yPercent: 6,
            ease: 'none',
            scrollTrigger: {
              trigger: '#bottomCta',
              start: 'top bottom',
              end: 'bottom top',
              scrub: 1.2
            }
          }
        );
      }
    }

    if (!isReducedMotion) {
      if (decoL) {
        gsap.to(decoL, {
          y: -14,
          rotation: -4,
          duration: 3.4,
          yoyo: true,
          repeat: -1,
          ease: 'sine.inOut'
        });
      }
      if (decoR) {
        gsap.to(decoR, {
          y: 16,
          rotation: 5,
          duration: 4.0,
          yoyo: true,
          repeat: -1,
          ease: 'sine.inOut',
          delay: 0.4
        });
      }

      ctaCard.addEventListener('mousemove', function (e) {
        var rect = ctaCard.getBoundingClientRect();
        var xRel = (e.clientX - rect.left) / rect.width - 0.5;
        var yRel = (e.clientY - rect.top) / rect.height - 0.5;

        gsap.to(ctaCard, {
          rotationY: xRel * 8,
          rotationX: -yRel * 8,
          transformPerspective: 900,
          duration: 0.5,
          ease: 'power1.out'
        });

        if (decoL) {
          gsap.to(decoL, {
            x: xRel * 26,
            y: yRel * 26,
            duration: 0.5,
            ease: 'power1.out'
          });
        }
        if (decoR) {
          gsap.to(decoR, {
            x: -xRel * 26,
            y: -yRel * 26,
            duration: 0.5,
            ease: 'power1.out'
          });
        }
      });

      ctaCard.addEventListener('mouseleave', function () {
        gsap.to(ctaCard, {
          rotationY: 0,
          rotationX: 0,
          duration: 0.8,
          ease: 'power2.out'
        });
        if (decoL) {
          gsap.to(decoL, { x: 0, y: 0, duration: 0.8, ease: 'power2.out' });
        }
        if (decoR) {
          gsap.to(decoR, { x: 0, y: 0, duration: 0.8, ease: 'power2.out' });
        }
      });
    }
  }

  initCtaMotion();

})();
