"use strict";

(function () {
  var root = document.documentElement;
  var toggle = document.querySelector("[data-theme-toggle]");
  var navToggle = document.querySelector("[data-nav-toggle]");
  var nav = document.querySelector("[data-nav]");
  var themeMeta = document.querySelector('meta[name="theme-color"]');

  function currentTheme() {
    return root.getAttribute("data-theme") === "dark" ? "dark" : "light";
  }

  function applyTheme(theme) {
    root.setAttribute("data-theme", theme);
    if (themeMeta) {
      themeMeta.setAttribute("content", theme === "dark" ? "#101614" : "#f3f0e8");
    }
    if (toggle) {
      var isDark = theme === "dark";
      toggle.setAttribute("aria-pressed", isDark ? "true" : "false");
      toggle.setAttribute("aria-label", isDark ? "Switch to light theme" : "Switch to dark theme");
    }
  }

  applyTheme(currentTheme());

  if (toggle) {
    toggle.addEventListener("click", function () {
      var next = currentTheme() === "dark" ? "light" : "dark";
      applyTheme(next);
      try {
        localStorage.setItem("theme", next);
      } catch (err) {
        /* Storage can be blocked. The in-memory theme still applies. */
      }
    });
  }

  var colorScheme = window.matchMedia("(prefers-color-scheme: dark)");
  if (typeof colorScheme.addEventListener === "function") {
    colorScheme.addEventListener("change", function (event) {
      var stored = null;
      try {
        stored = localStorage.getItem("theme");
      } catch (err) {
        stored = "set";
      }
      if (!stored) {
        applyTheme(event.matches ? "dark" : "light");
      }
    });
  }

  function closeNav() {
    if (!nav || !navToggle) return;
    nav.setAttribute("data-open", "false");
    navToggle.setAttribute("aria-expanded", "false");
  }

  if (navToggle && nav) {
    navToggle.addEventListener("click", function () {
      var open = nav.getAttribute("data-open") === "true";
      nav.setAttribute("data-open", open ? "false" : "true");
      navToggle.setAttribute("aria-expanded", open ? "false" : "true");
    });

    nav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", closeNav);
    });

    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape") closeNav();
    });

    document.addEventListener("click", function (event) {
      if (nav.getAttribute("data-open") !== "true") return;
      var target = event.target;
      if (!(target instanceof Node)) return;
      if (nav.contains(target) || navToggle.contains(target)) return;
      closeNav();
    });
  }

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (!reduceMotion && "IntersectionObserver" in window) {
    var nodes = document.querySelectorAll("[data-reveal]");
    nodes.forEach(function (node) {
      node.classList.add("reveal");
    });
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
    );
    nodes.forEach(function (node) {
      observer.observe(node);
    });
  }

  var copyButton = document.querySelector("[data-copy-email]");
  var copyStatus = document.querySelector("[data-copy-status]");
  if (copyButton) {
    copyButton.addEventListener("click", function () {
      var email = copyButton.getAttribute("data-copy-email") || "";
      if (!navigator.clipboard || !window.isSecureContext) {
        if (copyStatus) copyStatus.textContent = "Copy isn’t available here. Use the email link.";
        return;
      }
      navigator.clipboard.writeText(email).then(
        function () {
          if (copyStatus) copyStatus.textContent = "Email copied.";
          window.setTimeout(function () {
            if (copyStatus) copyStatus.textContent = "";
          }, 2000);
        },
        function () {
          if (copyStatus) copyStatus.textContent = "Copy didn’t work. Use the email link.";
        }
      );
    });
  }
})();
