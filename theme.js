// Theme switch. Follows the OS preference until the visitor picks one; the choice is kept in localStorage.
(function () {
  var key = "busnes-theme";
  var root = document.documentElement;
  var media = window.matchMedia("(prefers-color-scheme: dark)");

  function stored() {
    try { var v = localStorage.getItem(key); return v === "light" || v === "dark" ? v : null; } catch (e) { return null; }
  }

  function apply(theme) {
    root.setAttribute("data-theme", theme);
    var meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.setAttribute("content", theme === "dark" ? "#182326" : "#f8f6f0");
    var btn = document.querySelector(".theme-toggle");
    if (btn) {
      btn.setAttribute("aria-pressed", theme === "dark" ? "true" : "false");
      btn.setAttribute("aria-label", theme === "dark" ? "Switch to light mode" : "Switch to dark mode");
    }
  }

  function current() { return stored() || (media.matches ? "dark" : "light"); }

  apply(current());

  media.addEventListener("change", function () { if (!stored()) apply(current()); });

  document.addEventListener("DOMContentLoaded", function () {
    var btn = document.querySelector(".theme-toggle");
    if (!btn) return;
    apply(current());
    btn.addEventListener("click", function () {
      var next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
      try { localStorage.setItem(key, next); } catch (e) {}
      apply(next);
    });
  });
})();
