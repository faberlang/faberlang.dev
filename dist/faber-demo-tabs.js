/* faber-demo-tabs — progressive enhancer for .faber-demo-tabs code cards.
 *
 * One component, two data axes (reader locales or examples). With JS: tabs
 * with roving tabindex, arrow/Home/End keys, copy button, one-shot typing on
 * scroll-into-view for [data-typing] heroes, and a "continue" link that
 * follows the active tab ([data-fdt-continue-link]).
 *
 * Without JS: the markup is a readable labeled stack of real <pre> text —
 * readable, copyable, agent-safe. No dependencies.
 */
(function () {
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function activate(root, id, focus) {
    root.querySelectorAll('.fdt-tab').forEach(function (t) {
      var on = t.dataset.panel === id;
      t.setAttribute('aria-selected', on ? 'true' : 'false');
      t.tabIndex = on ? 0 : -1;
      if (on && focus) t.focus();
    });
    root.querySelectorAll('.fdt-panel').forEach(function (p) {
      p.classList.toggle('active', p.id === id);
    });
    var link = root.querySelector('[data-fdt-continue-link]');
    if (link) {
      var tab = root.querySelector('.fdt-tab[data-panel="' + id + '"]');
      if (tab && tab.dataset.href) {
        link.href = tab.dataset.href;
        link.textContent = 'Continue to ' + (tab.dataset.name || tab.textContent.trim()) + ' \u2192';
      }
    }
  }

  function type(panel, done) {
    var pre = panel.querySelector('pre');
    var full = pre.textContent;
    pre.textContent = '';
    var caret = document.createElement('span');
    caret.className = 'fdt-caret';
    pre.appendChild(caret);
    var i = 0;
    (function step() {
      if (i >= full.length) { caret.remove(); if (done) done(); return; }
      var ch = full[i++];
      caret.insertAdjacentText('beforebegin', ch);
      /* vary the cadence a touch so it feels hand-typed */
      var d = ch === '\n' ? 90 : (Math.random() < 0.12 ? 55 : 18);
      setTimeout(step, d);
    })();
  }

  document.querySelectorAll('[data-fdt]').forEach(function (root) {
    root.classList.add('js');
    var tabs = Array.prototype.slice.call(root.querySelectorAll('.fdt-tab'));

    tabs.forEach(function (tab, idx) {
      tab.addEventListener('click', function () { activate(root, tab.dataset.panel); });
      tab.addEventListener('keydown', function (e) {
        var next = -1;
        if (e.key === 'ArrowRight') next = (idx + 1) % tabs.length;
        else if (e.key === 'ArrowLeft') next = (idx - 1 + tabs.length) % tabs.length;
        else if (e.key === 'Home') next = 0;
        else if (e.key === 'End') next = tabs.length - 1;
        if (next < 0) return;
        e.preventDefault();
        activate(root, tabs[next].dataset.panel, true);
      });
    });

    if (root.hasAttribute('data-typing') && !reduce) {
      var first = root.querySelector('.fdt-panel.active');
      var fired = false;
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting && !fired) { fired = true; io.disconnect(); type(first); }
        });
      }, { threshold: 0.5 });
      io.observe(root);
    }
  });

  document.querySelectorAll('.fdt-copy').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var root = btn.closest('[data-fdt]');
      var pre = root.querySelector('.fdt-panel.active pre') || root.querySelector('pre');
      navigator.clipboard && navigator.clipboard.writeText(pre.textContent);
      var old = btn.textContent;
      btn.textContent = 'Copied';
      setTimeout(function () { btn.textContent = old; }, 1200);
    });
  });
})();
