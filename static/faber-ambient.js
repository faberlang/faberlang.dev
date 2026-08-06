/* faber-ambient — programmatic ambient background for faberlang.dev.
 *
 * Draws a slow "compute field" on one fixed full-viewport <canvas> behind
 * all content: a faint workgroup dot lattice, drifting Faber glyphs
 * (← → ∴ ≡ ∪ ⇥), and one wandering soft glow. Everything is computed live;
 * there is no pre-generated art.
 *
 * Progressive enhancement, same contract as faber-demo-tabs.js:
 *  - no JS            → no canvas; the CSS gradient layer carries the texture
 *  - reduced motion   → one static frame, no animation loop
 *  - hidden tab       → loop paused (visibilitychange)
 * Colors are read from the page's own CSS custom properties, so the field
 * follows the light/dark scheme with the rest of the site. No dependencies.
 */
(function () {
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var scheme = window.matchMedia ? window.matchMedia('(prefers-color-scheme: dark)') : null;

  /* Intensity tiers — every visibility knob lives here. Landing + portal
     carry the full field; docs pages get a quieter pass behind the prose. */
  var full = document.body.classList.contains('landing') ||
             document.body.classList.contains('porta');
  var TIER = full ? {
    density: 26000,        /* px² of viewport per glyph particle */
    latticeStep: 88,
    latticeAlpha: 0.8,
    glyphAlpha: [0.10, 0.18],
    heroEvery: 6,          /* every Nth particle is a bright "hero" glyph */
    heroAlpha: [0.26, 0.34],
    glowAlpha: 0.10,
    speed: 12,
    heroSpeed: 18
  } : {
    density: 42000,
    latticeStep: 112,
    latticeAlpha: 0.7,
    glyphAlpha: [0.07, 0.12],
    heroEvery: 0,          /* no hero glyphs behind docs prose */
    heroAlpha: [0, 0],
    glowAlpha: 0.07,
    speed: 8,
    heroSpeed: 0
  };

  var GLYPHS = ['\u2190', '\u2192', '\u2234', '\u2261', '\u222A', '\u21E5'];
  var MONO = "'Noto Sans Mono', ui-monospace, 'SF Mono', Menlo, Consolas, monospace";

  var canvas = document.createElement('canvas');
  canvas.className = 'ambient-canvas';
  canvas.setAttribute('aria-hidden', 'true');
  document.body.insertBefore(canvas, document.body.firstChild);
  document.body.classList.add('has-ambient');
  var ctx = canvas.getContext('2d');
  if (!ctx) { canvas.remove(); return; }

  var W = 0, H = 0, DPR = 1;
  var colGlyph = { r: 42, g: 74, b: 158 };
  var colRule = { r: 216, g: 213, b: 203 };
  var particles = [];
  var running = false;
  var rafId = 0;
  var t0 = 0;

  function hexToRgb(hex) {
    var m = /^\s*#([0-9a-f]{6})\s*$/i.exec(hex || '');
    if (!m) return null;
    var n = parseInt(m[1], 16);
    return { r: (n >> 16) & 255, g: (n >> 8) & 255, b: n & 255 };
  }

  function rgba(c, a) { return 'rgba(' + c.r + ',' + c.g + ',' + c.b + ',' + a + ')'; }

  function readColors() {
    var cs = getComputedStyle(document.body);
    var g = hexToRgb(cs.getPropertyValue('--glyph'));
    var r = hexToRgb(cs.getPropertyValue('--rule-strong')) ||
            hexToRgb(cs.getPropertyValue('--rule'));
    if (g) colGlyph = g;
    if (r) colRule = r;
  }

  function seed() {
    particles = [];
    var area = W * H;
    var n = Math.round(area / TIER.density);
    for (var i = 0; i < n; i++) {
      var hero = TIER.heroEvery > 0 && i % TIER.heroEvery === 0;
      var a = hero ? TIER.heroAlpha : TIER.glyphAlpha;
      var v = hero ? TIER.heroSpeed : TIER.speed;
      particles.push({
        ch: GLYPHS[i % GLYPHS.length],
        x: Math.random() * W,
        y: Math.random() * H,
        vx: (Math.random() - 0.5) * 2 * v,
        vy: (Math.random() - 0.5) * 1.5 * v,
        size: hero ? 22 + Math.random() * 8 : 13 + Math.random() * 8,
        alpha: a[0] + Math.random() * (a[1] - a[0])
      });
    }
  }

  function resize() {
    DPR = Math.min(window.devicePixelRatio || 1, 2);
    W = window.innerWidth;
    H = window.innerHeight;
    canvas.width = Math.round(W * DPR);
    canvas.height = Math.round(H * DPR);
    canvas.style.width = W + 'px';
    canvas.style.height = H + 'px';
    ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
    seed();
  }

  function lattice() {
    var step = TIER.latticeStep;
    ctx.fillStyle = rgba(colRule, TIER.latticeAlpha);
    for (var x = step / 2; x < W; x += step) {
      for (var y = step / 2; y < H; y += step) {
        ctx.fillRect(x - 0.75, y - 0.75, 1.5, 1.5);
      }
    }
  }

  function glow(t) {
    var R = Math.max(W, H) * 0.55;
    var cx = W * (0.5 + 0.28 * Math.sin(t * 0.00007));
    var cy = H * (0.42 + 0.22 * Math.cos(t * 0.00009));
    var grad = ctx.createRadialGradient(cx, cy, 0, cx, cy, R);
    grad.addColorStop(0, rgba(colGlyph, TIER.glowAlpha));
    grad.addColorStop(1, rgba(colGlyph, 0));
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, W, H);
  }

  function draw(t, dt) {
    ctx.clearRect(0, 0, W, H);
    lattice();
    glow(t);
    var margin = 30;
    for (var i = 0; i < particles.length; i++) {
      var p = particles[i];
      p.x += p.vx * dt;
      p.y += p.vy * dt;
      if (p.x < -margin) p.x = W + margin; else if (p.x > W + margin) p.x = -margin;
      if (p.y < -margin) p.y = H + margin; else if (p.y > H + margin) p.y = -margin;
      ctx.font = p.size + 'px ' + MONO;
      ctx.fillStyle = rgba(colGlyph, p.alpha);
      ctx.fillText(p.ch, p.x, p.y);
    }
  }

  var last = 0;
  function frame(now) {
    if (!running) return;
    if (!t0) t0 = now;
    var dt = Math.min((now - last) / 1000, 0.1);
    last = now;
    draw(now - t0, dt);
    rafId = requestAnimationFrame(frame);
  }

  function start() {
    if (running || reduce) return;
    running = true;
    last = performance.now();
    rafId = requestAnimationFrame(frame);
  }

  function stop() {
    running = false;
    if (rafId) cancelAnimationFrame(rafId);
    rafId = 0;
  }

  readColors();
  resize();

  if (reduce) {
    draw(0, 0);
  } else {
    start();
    document.addEventListener('visibilitychange', function () {
      if (document.hidden) stop(); else start();
    });
  }

  var resizeTimer = 0;
  window.addEventListener('resize', function () {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function () {
      resize();
      if (reduce) draw(0, 0);
    }, 150);
  });

  if (scheme && scheme.addEventListener) {
    scheme.addEventListener('change', function () {
      readColors();
      if (reduce) draw(0, 0);
    });
  }
})();
