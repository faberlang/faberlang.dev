#!/usr/bin/env python3
"""
generate-portal.py — Generate the locale-less Faber language portal at /.

CLI:
    generate-portal.py <output.html> [--locales path] [--reader-root path] [--css /speculum.css]

Layout (Speculum porta):
    gate + glyph ring of locale nodes + question + honest status note
    + "same program" sample grid + full index by status + footer

Defaults:
    --locales       generator/locales.toml
    --reader-root   workspace/radix/stdlib/reader
    --css           /speculum.css
"""

from __future__ import annotations

import argparse
import html as html_mod
import math
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

# Short status line under each ring node (honest, not mockup "proposed")
STATUS_LINE: dict[str, str] = {
    "complete": "complete · full docs",
    "partial": "partial · English prose fallback",
}

# Pilot override: th-TH has authored Thai for index + start/*
PILOT_SITES: set[str] = {"th-TH"}
PILOT_STATUS_LINE = "pilot · index + start"

# One-line architectural stress for the index (design pack, updated for site)
STRESS: dict[str, str] = {
    "en-US": "full documentation; code via Latin pack (la)",
    "th-TH": "spaceless script; pilot translated slice",
    "zh-Hans": "paired keywords; NFKC width collapse",
    "zh-Hant": "sibling of zh-Hans; traditional forms",
    "vi": "Latin-but-not-English; NFKC diacritics",
    "ar": "right-to-left; bidi isolation",
    "hi": "Devanagari clusters; Indic numerals",
}


def infer_script_class(native_script: str) -> str:
    return SCRIPT_CLASSES.get(native_script, "")


def load_locales(path: Path) -> dict:
    with path.open("rb") as f:
        data = tomllib.load(f)
    return data.get("locales", {})


def load_sample(reader_root: Path, reader_locale: str) -> str:
    """Load exemplar sample: salve-munde first, else first .fab under exemplars/."""
    exemplars_dir = reader_root / reader_locale / "exemplars"
    if not exemplars_dir.is_dir():
        return ""

    salve = exemplars_dir / f"salve-munde.{reader_locale}.fab"
    if salve.is_file():
        return salve.read_text(encoding="utf-8").strip()

    for child in sorted(exemplars_dir.iterdir()):
        if child.suffix == ".fab":
            return child.read_text(encoding="utf-8").strip()

    return ""


def ring_position(index: int, count: int) -> tuple[float, float]:
    """Heptagon (or n-gon) positions for the Speculum ring, top-start, CSS px."""
    # Ring canvas: 560 × 520; center slightly above geometric midpoint for balance
    cx, cy, radius = 280.0, 250.0, 200.0
    angle = -math.pi / 2 + (2 * math.pi * index / count)
    return cx + radius * math.cos(angle), cy + radius * math.sin(angle)


def status_line_for(site: str, status: str) -> tuple[str, str]:
    """Return (css_modifier, human status line)."""
    if site in PILOT_SITES:
        return "pilot", PILOT_STATUS_LINE
    if status == "complete":
        return "complete", STATUS_LINE["complete"]
    return "partial", STATUS_LINE.get(status, status)


def sort_locale_keys(keys: list[str]) -> list[str]:
    """en-US first, then th-TH pilot, then alpha — stable reading order on the ring."""
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
    parser.add_argument("--css", type=str, default="/speculum.css")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    generator_dir = script_dir.parent

    if args.locales is None:
        args.locales = generator_dir / "locales.toml"
    if args.reader_root is None:
        repo_dir = generator_dir.parent
        workspace_dir = repo_dir.parent
        args.reader_root = workspace_dir / "radix" / "stdlib" / "reader"

    registry = load_locales(args.locales)
    sorted_keys = sort_locale_keys(list(registry.keys()))
    n = len(sorted_keys)

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

        sample = load_sample(args.reader_root, reader_loc)
        if not sample:
            sample = f"# exemplar missing for {reader_loc}"

        left, top = ring_position(i, n)
        native_cls = f"porta-native {script_cls}".strip() if script_cls else "porta-native"

        locales.append({
            "site": html_mod.escape(site),
            "native_name": html_mod.escape(native),
            "status": html_mod.escape(status),
            "st_mod": st_mod,
            "st_line": html_mod.escape(st_line),
            "native_cls": native_cls,
            "tag": html_mod.escape(f"{site} · {native_script or site}"),
            "stress": html_mod.escape(STRESS.get(site, "")),
            "href": f"/{html_mod.escape(site)}/",
            "left": f"{left:.1f}",
            "top": f"{top:.1f}",
            "code_dir": ' dir="rtl"' if is_rtl else "",
            "sample": html_mod.escape(sample),
            "card_rtl": " porta-sample-rtl" if is_rtl else "",
        })

    # -- ring nodes --------------------------------------------------------
    node_html = ""
    for c in locales:
        node_html += f"""\
        <div class="porta-node" style="left:{c['left']}px;top:{c['top']}px">
          <a href="{c['href']}">
            <span class="{c['native_cls']}">{c['native_name']}</span>
            <span class="porta-tag">{c['tag']}</span>
            <span class="porta-st porta-st-{c['st_mod']}">{c['st_line']}</span>
          </a>
        </div>
"""

    # -- sample cards (PHASE-2: code samples required) ---------------------
    sample_html = ""
    for c in locales:
        sample_html += f"""\
        <article class="porta-sample{c['card_rtl']}">
          <header>
            <span class="{c['native_cls']}">{c['native_name']}</span>
            <span class="porta-id">{c['site']}</span>
            <span class="porta-badge porta-badge-{c['status']}">{c['status']}</span>
          </header>
          <pre class="faber-code"><code{c['code_dir']}>{c['sample']}</code></pre>
          <a class="porta-link" href="{c['href']}">{c['native_name']} →</a>
        </article>
"""

    # -- index groups ------------------------------------------------------
    complete = [c for c in locales if c["status"] == "complete"]
    pilot = [c for c in locales if c["st_mod"] == "pilot"]
    partial = [c for c in locales if c["status"] == "partial" and c["st_mod"] != "pilot"]

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
        "Pilot — translated prose slice", "pilot · partial", "limited", pilot
    )
    index_body += index_group(
        "Partial — packs + corpus; English prose fallback", "partial", "defer", partial
    )

    css_href = html_mod.escape(args.css)

    html = f"""\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Faber programming language portal — one semantic core, many renderings. Enter your locale.">
<meta name="theme-color" content="#faf9f6" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#1c1b19" media="(prefers-color-scheme: dark)">
<meta property="og:site_name" content="Faber">
<meta property="og:type" content="website">
<meta property="og:title" content="Faber · porta">
<meta property="og:description" content="Faber programming language portal — one semantic core, many renderings.">
<link rel="icon" href="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2064%2064'%3E%3Crect%20width='64'%20height='64'%20rx='12'%20fill='%232a4a9e'/%3E%3Ctext%20x='32'%20y='47'%20font-family='Georgia,serif'%20font-size='44'%20font-style='italic'%20text-anchor='middle'%20fill='%23faf9f6'%3Ef%3C/text%3E%3C/svg%3E">
<link rel="canonical" href="https://faberlang.dev/">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;600;700&amp;family=Noto+Serif:wght@400;600&amp;family=Noto+Sans+Mono:wght@400;600&amp;family=Noto+Sans+Arabic:wght@400;600;700&amp;family=Noto+Sans+Devanagari:wght@400;600&amp;family=Noto+Sans+SC:wght@400;600&amp;family=Noto+Sans+Thai:wght@400;600&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="{css_href}">
<title>Faber · porta</title>
</head>
<body class="porta">
<a href="#porta-locales" class="skip-link">Skip to locales</a>

<main class="porta-wrap">

  <div class="porta-gate">
    <div class="porta-kicker">Faber · porta · what do you read?</div>

    <div id="porta-locales" class="porta-ring" aria-label="Language portals">
      <div class="porta-mark">
        <div class="porta-glyphgrid" aria-hidden="true">
          <span>←</span><span>→</span><span>∴</span>
          <span>≡</span><span>∪</span><span>⇥</span>
        </div>
        <div class="porta-name">FABER</div>
        <div class="porta-gloss">these six never localize</div>
      </div>
{node_html}    </div>

    <p class="porta-question">
      Faber is one semantic core with many renderings. Latin is the canonical
      interchange for code, not a privileged human language.
      <span class="porta-alt">Pick the documentation language you read;
      the glyphs are the same in all of them.</span>
    </p>

    <div class="porta-note">
      <p>
        <b>Status.</b> <b>English</b> (<code>en-US</code>) is complete — docs, corpus,
        and tooling. <b>Thai</b> (<code>th-TH</code>) is the pilot locale: <code>index</code>
        and <code>start/*</code> have authored Thai prose; remaining sections still fall
        back to English. Every other locale ships reader packs and corpus pages with
        English prose fallback. Code samples below are the same <code>salve-munde</code>
        program from each pack — not proposed mock copy.
      </p>
      <p class="porta-agent-links">
        <a href="/llms.txt">Agent index</a>
        ·
        <a href="/agents/index.md">Agent guide</a>
        ·
        <a href="/en-US/start/install.html">Install</a>
      </p>
    </div>
  </div>

  <section id="porta-samples" class="porta-samples-section">
    <h2>Same program, every pack</h2>
    <p class="porta-lede">
      Each card shows the pack's <code>salve-munde</code> exemplar. The HIR is one;
      the rendering is the pack.
    </p>
    <div class="porta-samples">
{sample_html}    </div>
  </section>

  <section class="porta-index" id="porta-index">
    <h2>All site locales</h2>
    <p class="porta-lede">
      Grouped by what is true of the documentation tree today — not by population,
      and not by a future keyword-pack roadmap.
    </p>
{index_body}  </section>

  <footer class="porta-footer">
    <span>Faber language · MIT license</span>
    <span>
      <a href="/en-US/">docs</a>
      ·
      <a href="/en-US/start/install.html">install</a>
      ·
      <a href="https://github.com/faberlang">github.com/faberlang</a>
    </span>
  </footer>

</main>

</body>
</html>
"""

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(html, encoding="utf-8")
    print(f"Wrote portal → {args.output} ({n} locales)")


if __name__ == "__main__":
    main()
