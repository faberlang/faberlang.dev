/* faber-instrument — progressive enhancer for every page.
 *
 * Three jobs, all optional: a live UTC readout in the top-right corner label
 * (#hud-clock); copy buttons ([data-copy]) that put the button's data-copy
 * text on the clipboard and show a green "done" state; and a COPY button added
 * to the title bar of every fenced code block on the docs pages.
 *
 * Without JS the pages are fully readable: the clock reads "UTC --:--:--", the
 * install link is plain, selectable text, and code blocks carry no button and
 * stay selectable. No dependencies.
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

  /* Button labels follow the page's own language. Each [data-copy] button can
     carry its own data-copied / data-failed text (the pass does, from the
     locale chrome); the generated block buttons use this small table. */
  var LABELS = {
    en: ['Copy', 'Copied \u2713', 'Select the text instead'],
    ar: ['\u0646\u0633\u062e', '\u062a\u0645 \u0627\u0644\u0646\u0633\u062e \u2713', '\u062d\u062f\u0651\u062f \u0627\u0644\u0646\u0635 \u0628\u062f\u0644\u064b\u0627 \u0645\u0646 \u0630\u0644\u0643'],
    hi: ['\u0915\u0949\u092a\u0940 \u0915\u0930\u0947\u0902', '\u0915\u0949\u092a\u0940 \u0939\u094b \u0917\u092f\u093e \u2713', '\u0907\u0938\u0915\u0947 \u092c\u091c\u093e\u092f \u091f\u0947\u0915\u094d\u0938\u094d\u091f \u091a\u0941\u0928\u0947\u0902'],
    th: ['\u0e04\u0e31\u0e14\u0e25\u0e2d\u0e01', '\u0e04\u0e31\u0e14\u0e25\u0e2d\u0e01\u0e41\u0e25\u0e49\u0e27 \u2713', '\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e02\u0e49\u0e2d\u0e04\u0e27\u0e32\u0e21\u0e41\u0e17\u0e19'],
    vi: ['Sao ch\u00e9p', '\u0110\u00e3 sao ch\u00e9p \u2713', 'H\u00e3y ch\u1ecdn v\u0103n b\u1ea3n'],
    'zh-hans': ['\u590d\u5236', '\u5df2\u590d\u5236 \u2713', '\u8bf7\u6539\u4e3a\u9009\u4e2d\u6587\u672c'],
    'zh-hant': ['\u8907\u88fd', '\u5df2\u8907\u88fd \u2713', '\u8acb\u6539\u70ba\u9078\u53d6\u6587\u5b57']
  };

  function labelsFor(lang) {
    lang = (lang || 'en').toLowerCase();
    if (LABELS[lang]) return LABELS[lang];
    if (lang.indexOf('zh') === 0) return LABELS[lang.indexOf('hant') > -1 || lang === 'zh-tw' || lang === 'zh-hk' ? 'zh-hant' : 'zh-hans'];
    return LABELS[lang.split('-')[0]] || LABELS.en;
  }

  /* One click handler for both kinds of button: put the text on the clipboard,
     show the green done state for a moment, then restore the label. */
  function wireCopy(btn, getText, copied, failed) {
    var label = btn.textContent;
    var timer = null;
    btn.addEventListener('click', function () {
      copyText(getText()).then(function (ok) {
        clearTimeout(timer);
        btn.classList.toggle('done', ok);
        btn.textContent = ok ? copied : failed;
        timer = setTimeout(function () {
          btn.classList.remove('done');
          btn.textContent = label;
        }, 1600);
      });
    });
  }

  var labels = labelsFor(document.documentElement.lang);

  document.querySelectorAll('[data-copy]').forEach(function (btn) {
    wireCopy(btn, function () { return btn.getAttribute('data-copy'); },
      btn.getAttribute('data-copied') || labels[1],
      btn.getAttribute('data-failed') || labels[2]);
  });

  /* Fenced blocks. The reader-locale tab cards bring their own Copy button, so
     they are skipped. The block is wrapped (not the button placed inside the
     <pre>) because the <pre> scrolls sideways and the button must stay put.
     A block with a title bar keeps the button inside the bar; a bar-less one
     (plain text output) gets a corner button and room to the right of its
     first line. */
  document.querySelectorAll('pre.faber-code').forEach(function (pre) {
    if (pre.closest('.faber-demo-tabs, .fdt-panel') || pre.parentNode.classList.contains('code-block')) return;
    var wrap = document.createElement('div');
    var bar = getComputedStyle(pre, '::before').content;
    wrap.className = 'code-block' + (bar && bar !== 'none' && bar !== 'normal' ? '' : ' no-bar');
    pre.parentNode.insertBefore(wrap, pre);
    wrap.appendChild(pre);
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'code-copy';
    btn.textContent = labels[0];
    wrap.appendChild(btn);
    wireCopy(btn, function () { return pre.textContent.replace(/\n$/, ''); }, labels[1], labels[2]);
  });
})();
