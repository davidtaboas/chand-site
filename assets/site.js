// Chand — sin cookies, sin almacenamiento y sin peticiones a terceros.
(function () {
  var root = document.documentElement;
  root.classList.remove("no-js");

  // Idioma: quien llega desde fuera a una página en inglés con el navegador en español pasa a
  // la versión en español. Si el cambio de idioma se hace con el enlace del sitio, se respeta.
  try {
    var es = root.getAttribute("data-es");
    var internal = document.referrer && new URL(document.referrer).origin === location.origin;
    if (root.lang === "en" && es && !internal && /^es\b/i.test(navigator.language || "")) {
      location.replace(es + location.hash);
      return;
    }
  } catch (e) { /* sin redirección */ }

  // Fatiga: el control mueve el umbral y marca desde qué tirón toca parar.
  document.addEventListener("DOMContentLoaded", function () {
    var card = document.getElementById("fatigue-card");
    var range = document.getElementById("fatigue-range");
    if (!card || !range) return;
    var line = document.getElementById("fatigue-line");
    var label = document.getElementById("fatigue-label");
    var out = document.getElementById("fatigue-out");
    var verdict = document.getElementById("fatigue-verdict");
    var bars = card.querySelectorAll(".bar[data-loss]");
    var spanish = card.dataset.lang === "es";
    var base = 250, scale = 2.2;

    function update() {
      var threshold = Number(range.value);
      var percent = threshold + (spanish ? " %" : "%");
      var y = base - (100 - threshold) * scale;
      line.setAttribute("y1", y);
      line.setAttribute("y2", y);
      label.setAttribute("y", y + 16);
      label.textContent = card.dataset.threshold + " −" + percent;
      out.textContent = percent;
      var first = 0;
      bars.forEach(function (bar, i) {
        var over = Number(bar.dataset.loss) >= threshold;
        bar.classList.toggle("over", over);
        if (over && !first) first = i + 1;
      });
      verdict.textContent = card.dataset.stop.replace("{}", first);
    }
    range.addEventListener("input", update);
    update();
  });
})();
