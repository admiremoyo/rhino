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
})();
