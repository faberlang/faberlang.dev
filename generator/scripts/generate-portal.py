#!/usr/bin/env python3
"""
generate-portal.py — Generate the locale-less Faber language portal at /.

CLI:
    generate-portal.py <output.html> [--locales path] [--reader-root path]
                       [--exemplars path] [--css /speculum.css]

Layout (Speculum porta):
    gate + glyph ring of locale nodes + question + agent links
    + tabbed demo hero (.faber-demo-tabs, one program × every pack)
    + full index by status + footer

Theme: the "instrument" theme at full intensity (generator/www/speculum.css,
section 14 frame + section 15 portal). The frame furniture (head, grain,
registration marks, ticker) is shared with generate-landing.py; the two
scripts duplicate the small helpers on purpose rather than import across
hyphenated script names. Ring nodes carry their index as a class (`i0`…`i9`)
and the ring its count as `data-n`; the stylesheet places them by
trigonometry, so no node needs an inline style.

Defaults:
    --locales       generator/locales.toml
    --reader-root   workspace/radix/locale
    --exemplars     generator/portal/exemplars (hero panels; falls back to
                    pack exemplars under --reader-root)
    --css           /speculum.css
"""

from __future__ import annotations

import argparse
import re
import html as html_mod
import tomllib
from pathlib import Path

# Native script → CSS class for font selection
SCRIPT_CLASSES: dict[str, str] = {
    "English": "",
    "ไทย": "th",
    "简体中文": "zh",
    "繁體中文": "zh",
    "Latin": "",
    "العربية": "ar",
    "देवनागरी": "hi",
}

RTL_READER_LOCALES: set[str] = {"ar"}

# The glyphs at the centre of the ring: they never localize.
GLYPHS: list[str] = ["←", "→", "∴", "≡", "∪", "⇥"]

# The stylesheet places 5..10 ring nodes (speculum.css section 15).
RING_SIZES = range(5, 11)

# Short status line under each ring node (honest, not mockup "proposed")
STATUS_LINE: dict[str, str] = {
    "complete": "complete · full docs",
    "partial": "partial · English prose fallback",
}

# One-line architectural stress for the index (design pack, updated for site)
STRESS: dict[str, str] = {
    "en-US": "full documentation; code via Latin pack (la)",
    "th-TH": "spaceless script; full docs + chrome",
    "zh-Hans": "paired keywords; NFKC width collapse",
    "zh-Hant": "sibling of zh-Hans; traditional forms",
    "vi": "Latin-but-not-English; NFKC diacritics",
    "ar": "right-to-left; bidi isolation",
    "hi": "Devanagari clusters; Indic numerals",
}


def esc(s: str) -> str:
    return html_mod.escape(s)


def read_release(repo: Path) -> dict[str, object]:
    """The current release, read from the agent lobby and the install skill.

    The version is stated once in static/install.md ("Current release: Faber
    X.Y.Z."), which build-site.sh also reads. The license comes from the
    install skill's release block. Any shape change fails the build instead of
    printing a guessed value."""
    lobby = (repo / "static" / "install.md").read_text(encoding="utf-8")
    m = re.search(r"^Current release: Faber (\S+)\.$", lobby, re.M)
    if not m:
        raise SystemExit("could not read the current release from static/install.md")
    skill = (repo / "static" / ".well-known" / "agent-skills" / "install" / "SKILL.md"
             ).read_text(encoding="utf-8")
    lic = re.search(r"^- \*\*License:\*\* (.+?)\s*$", skill, re.M)
    if not lic:
        raise SystemExit("could not read the license from the install skill")
    return {"version": m.group(1), "license": lic.group(1)}


def favicon_href(gen: Path) -> str:
    """The site favicon data URI, read from its one definition in html.fab."""
    src = (gen / "src" / "html.fab").read_text(encoding="utf-8")
    m = re.search(r'favicon_href\(\)[^{]*\{\s*redde "(data:image/svg\+xml,[^"]+)"', src)
    if not m:
        raise SystemExit("could not read the favicon from generator/src/html.fab")
    return m.group(1)


def ticker(items: list[str]) -> str:
    """Bottom ticker: mono facts separated by accent squares, the group twice
    so the marquee loops. Decorative for assistive tech (aria-hidden)."""
    group = ('<div class="ticker-group">'
             + "<i></i>".join(f"<span>{esc(i)}</span>" for i in items)
             + "<i></i></div>")
    return f'<div class="ticker"><div class="ticker-track">{group}{group}</div></div>'


def hud(label: str, facts: list[str]) -> str:
    """Grain, four registration marks, corner labels, tick ruler, ticker."""
    return f"""\
<div class="grain" aria-hidden="true"></div>
<div class="hud" aria-hidden="true">
  <i class="c tl"></i><i class="c tr"></i><i class="c bl"></i><i class="c br"></i>
  <span class="lbl l1">{esc(label)}</span><span class="lbl l2" id="hud-clock">UTC --:--:--</span>
  <i class="ruler"></i>
  {ticker(facts)}
</div>
"""


def assert_no_external_requests(page: str, name: str) -> None:
    """The ticker says "zero external requests". Make that true by construction:
    no script, image or stylesheet may point off-site."""
    bad = re.findall(r'<(?:script|img)\b[^>]*\bsrc="https?://[^"]*"', page)
    bad += re.findall(r'<link\b[^>]*\brel="(?:stylesheet|preconnect|preload)"[^>]*\bhref="https?://[^"]*"', page)
    if bad:
        raise SystemExit(f"{name}: external request found: {bad[0]}")


def tag_html(site: str, script_name: str) -> str:
    """The small mono tag under a ring node: `site · script name`. The label
    recipe tracks and uppercases Latin text only; a native-script name goes in
    its own span so the stylesheet leaves it untracked."""
    name = html_mod.escape(script_name)
    if not script_name.isascii():
        name = f'<span class="porta-script">{name}</span>'
    return f"{html_mod.escape(site)} · {name}"


def infer_script_class(native_script: str) -> str:
    return SCRIPT_CLASSES.get(native_script, "")


def load_locales(path: Path) -> dict:
    with path.open("rb") as f:
        data = tomllib.load(f)
    return data.get("locales", {})


def read_sample(path: Path) -> str:
    """Read an exemplar, minus its `+++ locale = ... +++` frontmatter header.

    Pack exemplars carry the header so they are valid standalone sources; the
    portal shows them inside a panel that already names the locale.
    """
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"\A\+\+\+\n.*?\n\+\+\+\n", "", text, count=1, flags=re.S)
    return text.strip()


def load_sample(exemplars_dir: Path, reader_root: Path, reader_locale: str) -> str:
    """Load hero panel: site exemplars first, then the pack's exemplars."""
    local = exemplars_dir / f"salve-munde.{reader_locale}.fab"
    if local.is_file():
        return read_sample(local)

    pack_dir = reader_root / reader_locale / "exemplars"
    if pack_dir.is_dir():
        salve = pack_dir / f"salve-munde.{reader_locale}.fab"
        if salve.is_file():
            return read_sample(salve)
        for child in sorted(pack_dir.iterdir()):
            if child.suffix == ".fab":
                return read_sample(child)

    return ""


def status_line_for(_site: str, status: str) -> tuple[str, str]:
    """Return (css_modifier, human status line) from registry status."""
    if status == "complete":
        return "complete", STATUS_LINE["complete"]
    return "partial", STATUS_LINE.get(status, status)


def sort_locale_keys(keys: list[str]) -> list[str]:
    """en-US first, then th-TH, then alpha — stable reading order on the ring."""
    rest = sorted(k for k in keys if k not in ("en-US", "th-TH"))
    ordered: list[str] = []
    if "en-US" in keys:
        ordered.append("en-US")
    if "th-TH" in keys:
        ordered.append("th-TH")
    ordered.extend(rest)
    return ordered


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="Path to write the portal HTML")
    parser.add_argument("--locales", type=Path, default=None)
    parser.add_argument("--reader-root", type=Path, default=None)
    parser.add_argument("--exemplars", type=Path, default=None)
    parser.add_argument("--css", type=str, default="/speculum.css")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    generator_dir = script_dir.parent

    if args.locales is None:
        args.locales = generator_dir / "locales.toml"
    if args.exemplars is None:
        args.exemplars = generator_dir / "portal" / "exemplars"
    if args.reader_root is None:
        repo_dir = generator_dir.parent
        workspace_dir = repo_dir.parent
        args.reader_root = workspace_dir / "radix" / "locale"

    registry = load_locales(args.locales)
    sorted_keys = sort_locale_keys(list(registry.keys()))
    n = len(sorted_keys)
    if n not in RING_SIZES:
        raise SystemExit(f"portal ring: {n} locales; speculum.css places {RING_SIZES.start}..{RING_SIZES.stop - 1}")

    # -- build per-locale records ------------------------------------------
    locales: list[dict[str, str]] = []
    for i, site in enumerate(sorted_keys):
        entry = registry[site]
        reader_loc = entry.get("reader_locale", site)
        native = entry.get("native_name", site)
        status = entry.get("status", "partial")
        native_script = entry.get("native_script", "")
        script_cls = infer_script_class(native_script)
        is_rtl = reader_loc in RTL_READER_LOCALES
        st_mod, st_line = status_line_for(site, status)

        sample = load_sample(args.exemplars, args.reader_root, reader_loc)
        if not sample:
            sample = f"# exemplar missing for {reader_loc}"

        native_cls = f"porta-native {script_cls}".strip() if script_cls else "porta-native"

        locales.append({
            "site": html_mod.escape(site),
            "reader": html_mod.escape(reader_loc),
            "native_name": html_mod.escape(native),
            "status": html_mod.escape(status),
            "st_mod": st_mod,
            "st_line": html_mod.escape(st_line),
            "native_cls": native_cls,
            "script_cls": script_cls,
            "tag": tag_html(site, native_script or site),
            "stress": html_mod.escape(STRESS.get(site, "")),
            "href": f"/{html_mod.escape(site)}/",
            "code_dir": ' dir="rtl"' if is_rtl else "",
            "sample": html_mod.escape(sample),
        })

    # -- ring nodes --------------------------------------------------------
    node_html = ""
    for i, c in enumerate(locales):
        # Status lines only earn their place when a locale is not complete.
        st_html = ""
        if c["status"] != "complete":
            st_html = (
                f'\n            <span class="porta-st porta-st-{c["st_mod"]}">'
                f'{c["st_line"]}</span>'
            )
        node_html += f"""\
        <div class="porta-node i{i}">
          <a href="{c['href']}">
            <span class="{c['native_cls']}">{c['native_name']}</span>
            <span class="porta-tag">{c['tag']}</span>{st_html}
          </a>
        </div>
"""

    # -- demo hero (tabbed card: one program × every pack) ------------------
    # No-JS: labeled stack of real <pre> text with per-locale entry links.
    # static/faber-demo-tabs.js enhances to connected tabs + one-shot typing.
    tabs_html = ""
    panels_html = ""
    for i, c in enumerate(locales):
        selected = "true" if i == 0 else "false"
        tabindex = "0" if i == 0 else "-1"
        active = " active" if i == 0 else ""
        native_span = (
            f'<span class="{c["script_cls"]}">{c["native_name"]}</span>'
            if c["script_cls"] else c["native_name"]
        )
        tabs_html += (
            f'    <button class="fdt-tab" role="tab" id="pt-{c["site"]}" '
            f'data-panel="pp-{c["site"]}" data-href="{c["href"]}" '
            f'data-name="{c["native_name"]}" aria-controls="pp-{c["site"]}" '
            f'aria-selected="{selected}" tabindex="{tabindex}">'
            f'{native_span} <span class="code">{c["reader"]}</span></button>\n'
        )
        panels_html += f"""\
    <div class="fdt-panel{active}" id="pp-{c['site']}" role="tabpanel" aria-labelledby="pt-{c['site']}"><div class="fdt-panel-label">{c['native_name']} · {c['reader']} · <a href="{c['href']}">enter docs →</a></div><pre{c['code_dir']}><code class="lang-faber locale={c['reader']}">{c['sample']}</code></pre></div>
"""

    first = locales[0]
    hero_html = f"""\
  <div class="faber-demo-tabs fdt-hero" data-fdt data-typing>
    <div class="fdt-bar">
      <span class="fdt-mark" aria-hidden="true">←</span>
      <span class="fdt-file">salve-munde.fab</span>
      <a class="fdt-goto" href="{first['href']}" data-fdt-continue-link>Continue to {first['native_name']} →</a>
      <button class="fdt-copy" type="button">Copy</button>
    </div>
    <div class="fdt-tabs" role="tablist" aria-label="Reader locale">
{tabs_html}    </div>
{panels_html}  </div>
"""

    # -- index groups ------------------------------------------------------
    complete = [c for c in locales if c["status"] == "complete"]
    partial = [c for c in locales if c["status"] != "complete"]

    def index_group(title: str, verb: str, verb_cls: str, rows: list[dict[str, str]]) -> str:
        if not rows:
            return ""
        locs = ""
        for c in rows:
            stress = f' <span class="porta-stress">— {c["stress"]}</span>' if c["stress"] else ""
            locs += (
                f'          <div class="porta-loc">'
                f'<a href="{c["href"]}">{c["native_name"]}</a> '
                f'<span class="porta-code">{c["site"]}</span>{stress}</div>\n'
            )
        return f"""\
      <div class="porta-group">
        <div class="porta-group-head">
          <span>{html_mod.escape(title)}</span>
          <span class="porta-verb porta-verb-{verb_cls}">{html_mod.escape(verb)}</span>
        </div>
        <div class="porta-locs">
{locs}        </div>
      </div>
"""

    index_body = ""
    index_body += index_group("Complete — full documentation", "shipped", "support", complete)
    index_body += index_group(
        "Partial — packs + corpus; English prose fallback", "partial", "defer", partial
    )

    css_href = html_mod.escape(args.css)

    # hreflang alternates for each site locale home + x-default → portal
    hreflang_links = (
        '  <link rel="alternate" hreflang="x-default" href="https://faberlang.dev/">\n'
    )
    hreflang_map = {
        "en-US": "en-US",
        "th-TH": "th-TH",
        "zh-Hans": "zh-Hans",
        "zh-Hant": "zh-Hant",
        "vi": "vi",
        "ar": "ar",
        "hi": "hi",
    }
    for site in sorted_keys:
        hl = hreflang_map.get(site, site)
        hreflang_links += (
            f'  <link rel="alternate" hreflang="{html_mod.escape(hl)}" '
            f'href="https://faberlang.dev/{html_mod.escape(site)}/">\n'
        )

    portal_desc = (
        "Faber programming language portal — one semantic core, many renderings. "
        "Choose your documentation locale."
    )

    release = read_release(generator_dir.parent)
    icon = favicon_href(generator_dir)
    glyph_html = "".join(f"<span>{g}</span>" for g in GLYPHS)

    # Ticker: every item is derived at generation time or a plain true
    # statement about this page. No invented numbers.
    facts = [
        f"Faber {release['version']}",
        str(release["license"]),
        f"{n} documentation locales",
        f"{len(complete)} complete",
    ]
    if partial:
        facts.append(f"{len(partial)} partial")
    facts += [
        f"{len(GLYPHS)} glyphs never localize",
        "Latin · canonical interchange",
        "No accounts",
        "System fonts · zero external requests",
    ]

    html = f"""\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{html_mod.escape(portal_desc)}">
<meta name="theme-color" content="#0a0c0f" media="(prefers-color-scheme: dark)">
<meta name="theme-color" content="#e8e5db" media="(prefers-color-scheme: light)">
<meta property="og:site_name" content="Faber">
<meta property="og:type" content="website">
<meta property="og:title" content="Faber · porta">
<meta property="og:description" content="{html_mod.escape(portal_desc)}">
<meta property="og:url" content="https://faberlang.dev/">
<meta property="og:locale" content="en_US">
<link rel="icon" href="{icon}">
<link rel="canonical" href="https://faberlang.dev/">
{hreflang_links}<link rel="alternate" type="text/plain" href="/llms.txt" title="Agent index">
<link rel="alternate" type="text/markdown" href="/agents/index.md" title="Agent guide">
<link rel="alternate" type="application/json" href="/.well-known/agent-skills/index.json" title="Agent skills">
<link rel="stylesheet" href="{css_href}">
<title>Faber · porta</title>
</head>
<body class="porta">
<a href="#porta-locales" class="skip-link">Skip to locales</a>
{hud("Faber · porta", facts)}
<header class="site-top">
  <a class="site-brand" href="/" aria-label="Faber home"><span class="site-brand-mark" aria-hidden="true">←</span><span>Faber</span></a>
  <nav class="site-nav" aria-label="Primary">
    <a href="/">Home</a>
    <a href="/en-US/">Docs</a>
    <a href="/install.md">Install</a>
    <a href="/llms.txt">llms.txt</a>
    <a href="https://github.com/faberlang">GitHub ↗</a>
  </nav>
</header>

<main class="porta-wrap" id="main">
  <h1 class="sr-only">Faber language portal</h1>

  <div class="porta-gate">
    <p class="kicker live porta-kicker"><i class="sq" aria-hidden="true"></i>Faber · porta · what do you read?</p>

    <div id="porta-locales" class="porta-ring" data-n="{n}" aria-label="Language portals">
      <div class="porta-mark">
        <div class="porta-glyphgrid" aria-hidden="true">
          {glyph_html}
        </div>
        <div class="porta-name">Faber</div>
        <div class="porta-gloss">these {len(GLYPHS)} never localize</div>
      </div>
{node_html}    </div>

    <p class="porta-question">
      Faber is one semantic core with many renderings. Latin is the canonical
      interchange for code, not a privileged human language.
      <span class="porta-alt">Pick the documentation language you read;
      the glyphs are the same in all of them.</span>
    </p>

    <div class="porta-note">
      <nav class="chips" aria-label="Agent surfaces">
        <a href="/llms.txt">Agent index</a>
        <a href="/agents/index.md">Agent guide</a>
        <a href="/install.md">Install · for models</a>
      </nav>
    </div>
  </div>

  <section id="porta-samples" class="porta-samples-section">
    <p class="kicker"><i class="sq" aria-hidden="true"></i>Reader packs</p>
    <h2>Same program, every pack</h2>
    <p class="porta-lede">
      One program, {n} renderings. The HIR is one; the rendering is the
      pack. Pick a tab to preview Faber in that reader locale — the panels
      are real pack source, not mock copy.
    </p>
{hero_html}  </section>

  <section class="porta-index" id="porta-index">
    <p class="kicker"><i class="sq" aria-hidden="true"></i>Index</p>
    <h2>All site locales</h2>
    <p class="porta-lede">
      Every listed locale ships a full documentation tree. Stress notes call out
      script and packing concerns, not translation gaps.
    </p>
{index_body}  </section>

</main>

<footer class="site-foot">
  <div class="inner">
    <div>
      <h2>Faber language · {html_mod.escape(str(release['license']))} license</h2>
      <nav class="links" aria-label="Project">
        <a href="/en-US/">Docs</a>
        <a href="/install.md">Install</a>
        <a href="https://github.com/faberlang">github.com/faberlang ↗</a>
      </nav>
    </div>
    <div>
      <p>One semantic core, many renderings: pick the language you read and the same program follows you into its docs.</p>
    </div>
  </div>
</footer>

<script src="/faber-demo-tabs.js" defer></script>
<script src="/faber-instrument.js" defer></script>
</body>
</html>
"""

    assert_no_external_requests(html, "portal")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(html, encoding="utf-8")
    print(f"Wrote portal → {args.output} ({n} locales)")


if __name__ == "__main__":
    main()
