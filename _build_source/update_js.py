with open("js/script.js", "r", encoding="utf-8") as f:
    js = f.read()

circle_js = """
  // ==========================================================================
  // MAGNETIC EXPANDING CIRCLE BUTTON EFFECT
  // ==========================================================================
  function initCircleButtons() {
    // Select all buttons with .btn (excludes navbar links, phone link, and burger)
    var buttons = document.querySelectorAll('.btn:not(.nav-burger)');

    buttons.forEach(function (btn) {
      // 1. Ensure circle element exists
      var circle = btn.querySelector('.circle');
      if (!circle) {
        circle = document.createElement('span');
        circle.className = 'circle';
        circle.setAttribute('aria-hidden', 'true');
        btn.prepend(circle);
      }

      // 2. Ensure text nodes are wrapped in span for proper z-index layering
      Array.from(btn.childNodes).forEach(function (node) {
        if (node.nodeType === Node.TEXT_NODE && node.textContent.trim().length > 0) {
          var wrapper = document.createElement('span');
          wrapper.textContent = node.textContent;
          node.parentNode.replaceChild(wrapper, node);
        }
      });

      // 3. Mouse-tracking coordinate calculations
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
"""

if "initCircleButtons" not in js:
    # Insert before the last closing })();
    last_idx = js.rfind("})();")
    if last_idx != -1:
        new_js = js[:last_idx] + circle_js + "\n" + js[last_idx:]
    else:
        new_js = js + "\n" + circle_js
    with open("js/script.js", "w", encoding="utf-8") as f:
        f.write(new_js)
    print("Added circle buttons JS to js/script.js!")
else:
    print("JS already contains initCircleButtons.")
