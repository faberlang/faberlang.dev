/* faber-instrument — progressive enhancer for the landing page and the portal.
 *
 * Two jobs, both optional: a live UTC readout in the top-right corner label
 * (#hud-clock), and copy buttons ([data-copy]) that put the button's
 * data-copy text on the clipboard and show a green "done" state.
 *
 * Without JS the pages are fully readable: the clock reads "UTC --:--:--" and
 * the install link is plain, selectable text. No dependencies.
 */
(function () {
  'use strict';

  function pad(n) { return n < 10 ? '0' + n : String(n); }

  var clock = document.getElementById('hud-clock');
  if (clock) {
    var tick = function () {
      var d = new Date();
      clock.textContent = 'UTC ' + pad(d.getUTCHours()) + ':' + pad(d.getUTCMinutes()) + ':' + pad(d.getUTCSeconds());
    };
    tick();
    setInterval(tick, 1000);
  }

  function legacyCopy(text) {
    var ta = document.createElement('textarea');
    ta.value = text;
    ta.setAttribute('readonly', '');
    ta.setAttribute('aria-hidden', 'true');
    ta.className = 'sr-only';
    document.body.appendChild(ta);
    ta.select();
    var ok = false;
    try { ok = document.execCommand('copy'); } catch (e) { ok = false; }
    document.body.removeChild(ta);
    return ok;
  }

  function copyText(text) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      return navigator.clipboard.writeText(text).then(function () { return true; }, function () { return legacyCopy(text); });
    }
    return Promise.resolve(legacyCopy(text));
  }

  document.querySelectorAll('[data-copy]').forEach(function (btn) {
    var label = btn.textContent;
    var timer = null;
    btn.addEventListener('click', function () {
      copyText(btn.getAttribute('data-copy')).then(function (ok) {
        clearTimeout(timer);
        btn.classList.toggle('done', ok);
        btn.textContent = ok ? 'Copied ✓' : 'Select the text instead';
        timer = setTimeout(function () {
          btn.classList.remove('done');
          btn.textContent = label;
        }, 1600);
      });
    });
  });
})();
