/* faber-search — renderbar keyword jump box.
 *
 * Progressive enhancement: the markup carries a hidden [data-search] span;
 * this script reveals it and wires a typeahead over /search-index.json
 * (generated at build time from corpus frontmatter). Without JS the box
 * simply never appears — the renderbar is unchanged.
 *
 * Index entry: {t: term, k: kind, c: category, s: summary, a: [aliases]}.
 * Hrefs are built per current page locale as
 *   /{site_locale}/corpus/{encodeURIComponent(term)}.html
 * matching the corpus renderer's literal-term filenames.
 */
(function () {
  var box = document.querySelector('[data-search]');
  if (!box) return;

  var locale = document.documentElement.lang || 'en-US';
  var input = box.querySelector('input');
  if (!input) return;

  var index = null;   /* lazily fetched on first focus */
  var open = false;
  var active = -1;
  var matches = [];

  var list = document.createElement('ul');
  list.className = 'searchdrop';
  list.setAttribute('role', 'listbox');
  list.hidden = true;
  box.appendChild(list);
  box.hidden = false;

  function fetchIndex() {
    if (index) return;
    index = [];
    fetch('/search-index.' + locale + '.json')
      .then(function (r) { return r.ok ? r.json() : fetch('/search-index.json').then(function (r2) { return r2.ok ? r2.json() : []; }); })
      .then(function (data) { index = data; })
      .catch(function () { index = []; });
  }

  function hrefFor(term) {
    return '/' + locale + '/corpus/' + encodeURIComponent(term) + '.html';
  }

  /* Rank: term prefix > display/alias prefix > term substring > display/alias substring. */
  function find(query) {
    var q = query.trim().toLowerCase();
    if (!q || !index) return [];
    var buckets = [[], [], [], []];
    index.forEach(function (e) {
      var t = e.t.toLowerCase();
      var alts = (e.a || []).concat(e.d ? [e.d] : []);
      if (t.indexOf(q) === 0) { buckets[0].push({ e: e, via: null }); return; }
      var viaPrefix = null;
      var viaSub = null;
      alts.forEach(function (al) {
        var a = al.toLowerCase();
        if (a.indexOf(q) === 0 && !viaPrefix) viaPrefix = al;
        else if (a.indexOf(q) >= 0 && !viaSub) viaSub = al;
      });
      if (viaPrefix) { buckets[1].push({ e: e, via: viaPrefix }); return; }
      if (t.indexOf(q) >= 0) { buckets[2].push({ e: e, via: null }); return; }
      if (viaSub) buckets[3].push({ e: e, via: viaSub });
    });
    return buckets[0].concat(buckets[1], buckets[2], buckets[3]).slice(0, 8);
  }

  function close() {
    open = false;
    active = -1;
    list.hidden = true;
    list.innerHTML = '';
  }

  function render() {
    list.innerHTML = '';
    matches.forEach(function (m, i) {
      var li = document.createElement('li');
      li.setAttribute('role', 'option');
      li.className = i === active ? 'active' : '';
      var a = document.createElement('a');
      a.href = hrefFor(m.e.t);
      var term = document.createElement('code');
      term.textContent = m.e.d || m.e.t;
      a.appendChild(term);
      if (m.e.d && m.e.d !== m.e.t) {
        var lat = document.createElement('span');
        lat.className = 'lat';
        lat.textContent = m.e.t;
        a.appendChild(lat);
      }
      if (m.via) {
        var via = document.createElement('span');
        via.className = 'via';
        via.textContent = m.via + ' →';
        a.appendChild(via);
      }
      var kind = document.createElement('span');
      kind.className = 'kind';
      kind.textContent = m.e.k;
      a.appendChild(kind);
      if (m.e.s) {
        var sum = document.createElement('span');
        sum.className = 'sum';
        sum.textContent = m.e.s;
        a.appendChild(sum);
      }
      li.appendChild(a);
      list.appendChild(li);
    });
    list.hidden = !open || matches.length === 0;
  }

  function refresh() {
    matches = find(input.value);
    open = true;
    active = matches.length ? 0 : -1;
    render();
  }

  input.addEventListener('focus', fetchIndex);
  input.addEventListener('input', refresh);
  input.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
      if (!open) refresh();
      else if (matches.length) {
        var d = e.key === 'ArrowDown' ? 1 : -1;
        active = (active + d + matches.length) % matches.length;
        render();
      }
      e.preventDefault();
    } else if (e.key === 'Enter') {
      if (open && active >= 0 && matches[active]) {
        window.location.href = hrefFor(matches[active].e.t);
        e.preventDefault();
      }
    } else if (e.key === 'Escape') {
      close();
      input.blur();
    }
  });
  document.addEventListener('click', function (e) {
    if (!box.contains(e.target)) close();
  });
})();
