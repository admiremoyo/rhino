/* RhinoFence — tiny, dependency-free interactions */
(function () {
  "use strict";

  // Mobile nav toggle
  var toggle = document.querySelector(".nav-toggle");
  var links = document.querySelector(".nav-links");
  if (toggle && links) {
    toggle.addEventListener("click", function () {
      links.classList.toggle("open");
      var expanded = links.classList.contains("open");
      toggle.setAttribute("aria-expanded", expanded ? "true" : "false");
    });
    links.addEventListener("click", function (e) {
      if (e.target.tagName === "A") links.classList.remove("open");
    });
  }

  // Quote form -> WhatsApp (works even without a backend)
  var form = document.querySelector("#quote-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var name = (form.name && form.name.value || "").trim();
      var phone = (form.phone && form.phone.value || "").trim();
      var service = (form.service && form.service.value || "").trim();
      var detail = (form.detail && form.detail.value || "").trim();
      var msg =
        "Hello RhinoFence, I'd like a free fencing quote.%0A%0A" +
        "Name: " + encodeURIComponent(name) + "%0A" +
        "Phone: " + encodeURIComponent(phone) + "%0A" +
        "Service: " + encodeURIComponent(service) + "%0A" +
        "Details: " + encodeURIComponent(detail);
      // Primary WhatsApp number (263 country code, drop leading 0)
      window.open("https://wa.me/263714194324?text=" + msg, "_blank", "noopener");
    });
  }

  // Current year in footer
  var y = document.querySelector("[data-year]");
  if (y) y.textContent = new Date().getFullYear();

  // Animated stat counters (run once when scrolled into view)
  var counters = document.querySelectorAll("[data-count]");
  if (counters.length && "IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        io.unobserve(el);
        var target = parseInt(el.getAttribute("data-count"), 10);
        var suffix = el.getAttribute("data-suffix") || "";
        var start = null, dur = 1200;
        function tick(ts) {
          if (!start) start = ts;
          var p = Math.min((ts - start) / dur, 1);
          // ease-out
          var val = Math.round(target * (1 - Math.pow(1 - p, 3)));
          el.textContent = val + suffix;
          if (p < 1) requestAnimationFrame(tick);
        }
        requestAnimationFrame(tick);
      });
    }, { threshold: 0.5 });
    counters.forEach(function (el) { io.observe(el); });
  }

  // Hero carousel: bright, un-dimmed photos of real installations,
  // crossfading with a label naming each fence type. Dots allow manual
  // selection; auto-advance pauses in hidden tabs and respects
  // reduced-motion preferences.
  var car = document.querySelector(".carousel");
  if (car) {
    var slides = Array.prototype.slice.call(car.querySelectorAll(".c-slide"));
    var label = car.querySelector("[data-c-label]");
    var dotsHost = car.querySelector(".c-dots");
    var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var idx = 0, dots = [];
    var goTo = function (i) {
      slides[idx].classList.remove("active");
      if (dots[idx]) dots[idx].classList.remove("active");
      idx = (i + slides.length) % slides.length;
      slides[idx].classList.add("active");
      if (dots[idx]) dots[idx].classList.add("active");
      if (label) label.textContent = slides[idx].getAttribute("data-label") || "";
    };
    if (dotsHost && slides.length > 1) {
      slides.forEach(function (_, i) {
        var b = document.createElement("button");
        b.className = "c-dot" + (i === 0 ? " active" : "");
        b.setAttribute("aria-label", "Show slide " + (i + 1));
        b.addEventListener("click", function () { goTo(i); });
        dotsHost.appendChild(b);
        dots.push(b);
      });
    }
    if (slides.length > 1 && !reduceMotion) {
      setInterval(function () {
        if (!document.hidden) goTo(idx + 1);
      }, 5000);
    }
  }

  // Scroll-to-top button
  var toTop = document.querySelector(".to-top");
  if (toTop) {
    var onScroll = function () {
      toTop.classList.toggle("show", window.scrollY > 600);
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
    toTop.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }
})();
