/* DGS session pager — one section.page visible at a time, left agenda, prev/next, arrow keys.
   Local file, no dependencies. Without JS every page is shown in order (graceful fallback). */
(function () {
  "use strict";
  var pages = Array.prototype.slice.call(document.querySelectorAll("section.page"));
  if (!pages.length) return;
  document.documentElement.classList.add("js");

  var links = Array.prototype.slice.call(document.querySelectorAll(".agenda a[data-page]"));
  var prevBtn = document.querySelector(".pager .prev");
  var nextBtn = document.querySelector(".pager .next");
  var counter = document.querySelector(".pager .count");
  var bar = document.querySelector(".progress > span");
  var cur = 0;

  function idx() {
    var m = /^#p(\d+)$/.exec(location.hash);
    var n = m ? parseInt(m[1], 10) - 1 : 0;
    return Math.min(Math.max(n, 0), pages.length - 1);
  }
  function show(n, push) {
    cur = n;
    pages.forEach(function (p, i) { p.classList.toggle("active", i === n); });
    links.forEach(function (a, i) {
      a.classList.toggle("active", i === n);
      if (i === n) a.setAttribute("aria-current", "page"); else a.removeAttribute("aria-current");
    });
    if (counter) counter.textContent = (n + 1) + " / " + pages.length;
    if (bar) bar.style.width = ((n + 1) / pages.length * 100) + "%";
    if (prevBtn) prevBtn.disabled = n === 0;
    if (nextBtn) nextBtn.disabled = n === pages.length - 1;
    var t = pages[n].getAttribute("data-title");
    if (t) document.title = t + " — " + document.title.replace(/^.*?— /, "");
    if (push !== false) {
      var h = "#p" + (n + 1);
      if (location.hash !== h) history.replaceState(null, "", h);
    }
    window.scrollTo({ top: 0, behavior: "instant" in window ? "instant" : "auto" });
    var active = links[n]; if (active && active.scrollIntoView) active.scrollIntoView({ block: "nearest" });
  }
  function go(d) { var n = cur + d; if (n >= 0 && n < pages.length) show(n); }

  if (prevBtn) prevBtn.addEventListener("click", function () { go(-1); });
  if (nextBtn) nextBtn.addEventListener("click", function () { go(1); });
  links.forEach(function (a, i) {
    a.addEventListener("click", function (e) { e.preventDefault(); show(i); });
  });
  window.addEventListener("hashchange", function () { show(idx(), false); });
  document.addEventListener("keydown", function (e) {
    if (e.target && /^(INPUT|TEXTAREA|SELECT)$/.test(e.target.tagName)) return;
    if (e.key === "ArrowRight" || e.key === "PageDown") { go(1); e.preventDefault(); }
    if (e.key === "ArrowLeft" || e.key === "PageUp") { go(-1); e.preventDefault(); }
  });
  Array.prototype.forEach.call(document.querySelectorAll("[data-print]"), function (b) {
    b.addEventListener("click", function () { window.print(); });
  });
  // agenda toggle on small screens
  var tg = document.querySelector(".agenda-toggle");
  if (tg) tg.addEventListener("click", function () { document.body.classList.toggle("agenda-open"); });


  // break timer: <section class="page" data-timer="15"> gets a mm:ss countdown with Start / Pause / Reset
  Array.prototype.forEach.call(document.querySelectorAll("section.page[data-timer]"), function (sec) {
    var mins = parseInt(sec.getAttribute("data-timer"), 10) || 15;
    var box = sec.querySelector(".timer"); if (!box) return;
    var disp = box.querySelector(".t-display"), st = box.querySelector(".t-start"), rs = box.querySelector(".t-reset");
    var left = mins * 60, id = null;
    function paint() {
      var m = Math.floor(left / 60), s = left % 60;
      disp.textContent = (m < 10 ? "0" : "") + m + ":" + (s < 10 ? "0" : "") + s;
      box.classList.toggle("done", left === 0);
    }
    function stop() { if (id) { clearInterval(id); id = null; } st.textContent = "Start"; }
    st.addEventListener("click", function () {
      if (id) { stop(); return; }
      if (left === 0) left = mins * 60;
      st.textContent = "Pause";
      id = setInterval(function () { if (left > 0) { left--; paint(); } if (left === 0) stop(); }, 1000);
    });
    rs.addEventListener("click", function () { stop(); left = mins * 60; paint(); });
    paint();
  });

  // ---- interactive diagrams: click any [data-explain] node -> explanation panel inside the same figure
  function closeExplain(fig) {
    var p = fig.querySelector(".explain-panel"); if (p) { p.hidden = true; p.innerHTML = ""; }
    Array.prototype.forEach.call(fig.querySelectorAll("[data-explain].sel"), function (n) { n.classList.remove("sel"); });
  }
  function openExplain(node) {
    var fig = node.closest("figure"); if (!fig) return;
    var key = node.getAttribute("data-explain");
    var src = fig.querySelector('.explain-data [data-key="' + key + '"]');
    var panel = fig.querySelector(".explain-panel");
    if (!src || !panel) return;
    if (node.classList.contains("sel")) { closeExplain(fig); return; }
    closeExplain(fig);
    node.classList.add("sel");
    panel.innerHTML = '<button class="x" type="button" aria-label="Close">&times;</button>' + src.innerHTML;
    panel.hidden = false;
    panel.querySelector(".x").addEventListener("click", function () { closeExplain(fig); });
  }
  document.addEventListener("click", function (e) {
    var n = e.target.closest && e.target.closest("[data-explain]"); if (n) { openExplain(n); }
  });
  document.addEventListener("keydown", function (e) {
    if ((e.key === "Enter" || e.key === " ") && e.target.hasAttribute && e.target.hasAttribute("data-explain")) { e.preventDefault(); openExplain(e.target); }
  });

  // ---- MCQ engine: .mcq[data-answer] > .opts > button[data-opt]; .fb feedback; .mcq-score inside the same .quiz
  Array.prototype.forEach.call(document.querySelectorAll(".quiz"), function (quiz) {
    var items = Array.prototype.slice.call(quiz.querySelectorAll(".mcq"));
    var score = quiz.querySelector(".mcq-score"), reset = quiz.querySelector(".mcq-reset");
    var done = 0, right = 0;
    function paint() { if (score) score.textContent = right + " / " + items.length + " correct" + (done < items.length ? "  ·  " + (items.length - done) + " left" : "  ·  done"); }
    items.forEach(function (m) {
      var ans = m.getAttribute("data-answer");
      Array.prototype.forEach.call(m.querySelectorAll("button[data-opt]"), function (btn) {
        btn.addEventListener("click", function () {
          if (m.classList.contains("answered")) return;
          m.classList.add("answered"); done++;
          var ok = btn.getAttribute("data-opt") === ans; if (ok) right++;
          btn.classList.add(ok ? "right" : "wrong");
          var c = m.querySelector('button[data-opt="' + ans + '"]'); if (c) c.classList.add("right");
          var fb = m.querySelector(".fb"); if (fb) { fb.hidden = false; fb.classList.add(ok ? "ok" : "no"); }
          paint();
        });
      });
    });
    if (reset) reset.addEventListener("click", function () {
      done = 0; right = 0;
      items.forEach(function (m) {
        m.classList.remove("answered");
        Array.prototype.forEach.call(m.querySelectorAll("button[data-opt]"), function (b) { b.classList.remove("right", "wrong"); });
        var fb = m.querySelector(".fb"); if (fb) { fb.hidden = true; fb.classList.remove("ok", "no"); }
      });
      paint();
    });
    paint();
  });

  show(idx(), false);
})();
