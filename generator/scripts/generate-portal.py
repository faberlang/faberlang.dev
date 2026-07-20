#!/usr/bin/env python3
"""
generate-portal.py — Generate the locale-less Faber language portal at /.

CLI:
    generate-portal.py <output.html> [--locales path] [--reader-root path] [--css /speculum.css]

Defaults:
    --locales       generator/locales.toml (relative to script parent)
    --reader-root   workspace/radix/stdlib/reader (workspace = parent of repo dir)
    --css           /speculum.css

Loads every locale from the registry, reads its exemplar code sample,
and produces a full Speculum-styled portal HTML page with card grid.
"""

from __future__ import annotations

import argparse
import html as html_mod
import tomllib
from pathlib import Path

# ---------------------------------------------------------------------------
# Native script → CSS class mapping for locale name display
# ---------------------------------------------------------------------------
SCRIPT_CLASSES: dict[str, str] = {
    "English": "",
    "ไทย": "th",
    "简体中文": "zh",
    "繁體中文": "zh",
    "Latin": "",
    "العربية": "ar",
    "देवनागरी": "hi",
}

# ---------------------------------------------------------------------------
# Reader-locale values known to be RTL
# ---------------------------------------------------------------------------
RTL_READER_LOCALES: set[str] = {"ar"}


def infer_script_class(native_script: str) -> str:
    """Return the CSS font class for a locale's native_script value."""
    return SCRIPT_CLASSES.get(native_script, "")


def load_locales(path: Path) -> dict:
    """Load the [locales.*] section from a TOML file."""
    with path.open("rb") as f:
        data = tomllib.load(f)
    return data.get("locales", {})


def load_sample(reader_root: Path, reader_locale: str) -> str:
    """Load the exemplar code sample for a reader locale.

    Tries ``salve-munde.{reader_locale}.fab`` first, then any ``.fab`` file
    under the exemplars directory.
    """
    exemplars_dir = reader_root / reader_locale / "exemplars"
    if not exemplars_dir.is_dir():
        return ""

    # Prefer the canonical salve-munde file
    salve = exemplars_dir / f"salve-munde.{reader_locale}.fab"
    if salve.is_file():
        return salve.read_text(encoding="utf-8").strip()

    # Fallback: first .fab file
    for child in sorted(exemplars_dir.iterdir()):
        if child.suffix == ".fab":
            return child.read_text(encoding="utf-8").strip()

    return ""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="Path to write the portal HTML")
    loci_help = "Path to locales.toml (default: generator/locales.toml)"
    parser.add_argument("--locales", type=Path, default=None, help=loci_help)
    rr_help = "Path to radix/stdlib/reader (default: workspace/radix/stdlib/reader)"
    parser.add_argument("--reader-root", type=Path, default=None, help=rr_help)
    parser.add_argument("--css", type=str, default="/speculum.css",
                        help="Stylesheet path (default: /speculum.css)")
    args = parser.parse_args()

    # -- resolve defaults --------------------------------------------------
    script_dir = Path(__file__).resolve().parent
    generator_dir = script_dir.parent

    if args.locales is None:
        args.locales = generator_dir / "locales.toml"

    if args.reader_root is None:
        # Workspace = parent of repo dir; repo dir = parent of generator dir
        repo_dir = generator_dir.parent
        workspace_dir = repo_dir.parent
        args.reader_root = workspace_dir / "radix" / "stdlib" / "reader"

    # -- load locales ------------------------------------------------------
    registry = load_locales(args.locales)
    # Sort: en-US first, then alphabetically by key
    sorted_keys = sorted(registry.keys())
    sorted_keys = [k for k in sorted_keys if k == "en-US"] + \
                  [k for k in sorted_keys if k != "en-US"]

    # -- build card data ---------------------------------------------------
    cards: list[dict[str, str]] = []
    for site in sorted_keys:
        entry = registry[site]
        reader_loc = entry.get("reader_locale", site)
        native = entry.get("native_name", site)
        status = entry.get("status", "partial")
        native_script = entry.get("native_script", "")
        script_cls = infer_script_class(native_script)
        is_rtl = reader_loc in RTL_READER_LOCALES

        sample = load_sample(args.reader_root, reader_loc)
        if not sample:
            sample = f"# exemplar missing for {reader_loc}"
        sample_escaped = html_mod.escape(sample)

        lang_classes = "porta-lang"
        if script_cls:
            lang_classes = f"porta-lang {script_cls}"
        card_classes = "porta-card"
        if is_rtl:
            card_classes = "porta-card porta-card-rtl"

        cards.append({
            "site": html_mod.escape(site),
            "native_name": html_mod.escape(native),
            "status": html_mod.escape(status),
            "lang_classes": lang_classes,
            "card_classes": card_classes,
            "code_dir": ' dir="rtl"' if is_rtl else "",
            "sample": sample_escaped,
        })

    # -- build HTML --------------------------------------------------------
    card_rows = ""
    for c in cards:
        card_rows += f"""\
          <article class="{c['card_classes']}">
            <header>
              <span class="{c['lang_classes']}">{c['native_name']}</span>
              <span class="porta-id">{c['site']}</span>
              <span class="porta-badge porta-badge-{c['status']}">{c['status']}</span>
            </header>
            <pre class="faber-code"><code{c['code_dir']}>{c['sample']}</code></pre>
            <a class="porta-link" href="/{c['site']}/">{c['native_name']} →</a>
          </article>
"""

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
<link rel="stylesheet" href="{html_mod.escape(args.css)}">
<title>Faber · porta</title>
</head>
<body class="porta">
<a href="#porta-locales" class="skip-link">Skip to locales</a>

<div class="porta-bar">
  <span class="porta-brand">Faber</span>
  <span class="porta-sep">·</span>
  <span class="porta-sub">porta</span>
  <span class="porta-sep">·</span>
  <span class="porta-question">what do you read?</span>
</div>

<div class="porta-gate">
  <p class="porta-intro">
    Faber lives in a semantic core — the HIR — not in any single rendering.
    Every locale below reads the same language in its own script and vocabulary.
    Choose your portal to enter the documentation, corpus, and tooling.
  </p>
</div>

<div id="porta-locales" class="porta-locales">
{card_rows}</div>

<div class="porta-note">
  <p>
    <strong>Status:</strong> English is complete — all docs, corpus, and tooling pages
    are authored and rendered. The remaining locales are <strong>partial</strong>:
    packs and corpus pages are shipped for every locale shown here, but authored
    prose sections fall back to English. Full translation is an open community goal.
  </p>
  <p class="porta-agent-links">
    <a href="/llms.txt">Agent index</a>
    ·
    <a href="/agents/index.md">Agent guide</a>
    ·
    <a href="/en-US/start/install.html">Install</a>
  </p>
</div>

<footer class="porta-footer">
  <span>Faber language · MIT license</span>
  <a href="https://github.com/faberlang">GitHub org</a>
</footer>
</body>
</html>
"""

    # -- write -------------------------------------------------------------
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(html, encoding="utf-8")
    print(f"Wrote portal → {args.output}")


if __name__ == "__main__":
    main()
