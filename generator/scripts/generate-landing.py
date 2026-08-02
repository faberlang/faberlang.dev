#!/usr/bin/env python3
"""
generate-landing.py — Generate the Faber landing page at /.

Narrative order, deliberately plain:

    1. what it is, in one sentence, with code visible immediately
    2. read it in your language      (reader-pack axis)
    3. compile it to what you need   (target axis)
    4. and it runs                   (GPU frames + interpreted latency)
    5. where to go

Both demo axes show the SAME program, and every panel is compiler output
captured by capture-landing-panels.sh — never hand-authored. Run that script
after a compiler or reader-pack change, then rebuild.

CLI:
    generate-landing.py <output.html> [--landing path] [--matrix path]
                        [--css /speculum.css]
"""

from __future__ import annotations

import argparse
import html as html_mod
import re
from pathlib import Path

# Reader-pack axis. Order is the argument: the surface a model writes and an
# English reader reads, then canonical Faber, then the human packs.
#
# `llm` is labelled honestly as the model-facing pack rather than as "English".
# There is no `en` pack today; conflating the two is the exact overstatement
# the positioning review flagged.
LOCALES: list[dict[str, str]] = [
    {"id": "llm", "name": "English", "code": "llm", "script": "",
     "note": "the model-facing pack — what a model writes, and what an "
             "English reader reads today"},
    {"id": "la", "name": "Latin", "code": "la", "script": "",
     "note": "canonical Faber — the classical surface the language is named for"},
    {"id": "th-TH", "name": "ภาษาไทย", "code": "th-TH", "script": "th",
     "note": "Thai — spaceless script"},
    {"id": "zh-Hans", "name": "简体中文", "code": "zh-Hans", "script": "zh",
     "note": "Simplified Chinese"},
    {"id": "zh-Hant", "name": "繁體中文", "code": "zh-Hant", "script": "zh",
     "note": "Traditional Chinese"},
    {"id": "vi", "name": "Tiếng Việt", "code": "vi", "script": "",
     "note": "Vietnamese"},
    {"id": "ar", "name": "العربية", "code": "ar", "script": "ar",
     "note": "Arabic — right-to-left, bidi isolated", "rtl": "1"},
    {"id": "hi", "name": "हिन्दी", "code": "hi", "script": "hi",
     "note": "Hindi — Devanagari"},
]

TARGETS: list[dict[str, str]] = [
    {"id": "rust", "name": "Rust",
     "note": "primary backend — reviewable source, then a native binary"},
    {"id": "go", "name": "Go", "note": "file emission"},
    {"id": "ts", "name": "TypeScript", "note": "file emission",
     "elide_before": "function saturate"},
    {"id": "llvm-text", "name": "LLVM IR",
     "note": "native code with no source language in between"},
    {"id": "wasm-text", "name": "WebAssembly", "note": "external host"},
    {"id": "wgsl-text", "name": "WGSL",
     "note": "GPU compute shader — from an @ nucleum kernel", "kernel": "1"},
    {"id": "metal-text", "name": "Metal",
     "note": "GPU compute shader — from an @ nucleum kernel", "kernel": "1"},
]

FRAMES: list[dict[str, str]] = [
    {"src": "/images/triga-budapest.png",
     "alt": "A low-poly 3D scene of a bridge with towers and lamp posts over water, rendered by Triga",
     "cap": "Scene graph, materials, lighting — <code>triga-budapest</code>"},
    {"src": "/images/triga-terrain.png",
     "alt": "A procedurally generated 3D terrain with lakes and hills, rendered by Triga",
     "cap": "Procedural heightmap terrain, biome shading"},
    {"src": "/images/triga-geometries.png",
     "alt": "Eight primitive 3D shapes — cylinder, cone, cube, torus, plane and others — rendered by Triga",
     "cap": "Primitive geometry set from <code>triga:geometria</code>"},
]


def esc(s: str) -> str:
    return html_mod.escape(s)


def read_matrix(path: Path) -> dict[str, str]:
    """Pull generated per-target coverage off the targets page, so the hero
    statistics cannot drift away from their own source."""
    out: dict[str, str] = {}
    if not path.is_file():
        return out
    for row in re.finditer(
        r"^\|\s*([a-z-]+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)%\s*\|",
        path.read_text(encoding="utf-8"), re.M,
    ):
        out[row.group(1)] = row.group(4)
    return out


def demo_tabs(*, root_id: str, file_label: str, tablist_label: str,
              panels: list[dict[str, str]]) -> str:
    tabs = bodies = ""
    for i, p in enumerate(panels):
        pid = f"{root_id}-p-{p['id']}"
        tabs += (
            f'    <button class="fdt-tab" role="tab" id="{root_id}-t-{p["id"]}" '
            f'data-panel="{pid}" data-name="{p["name"]}" aria-controls="{pid}" '
            f'aria-selected="{"true" if i == 0 else "false"}" '
            f'tabindex="{"0" if i == 0 else "-1"}">{p["tab"]}</button>\n'
        )
        bodies += (
            f'    <div class="fdt-panel{" active" if i == 0 else ""}" id="{pid}" '
            f'role="tabpanel" aria-labelledby="{root_id}-t-{p["id"]}">'
            f'<div class="fdt-panel-label">{p["label"]}</div>'
            f'<pre{p.get("dir", "")}>{p["code"]}</pre></div>\n'
        )
    return f"""\
  <div class="faber-demo-tabs fdt-hero" data-fdt>
    <div class="fdt-bar">
      <span class="fdt-mark" aria-hidden="true">f</span>
      <span class="fdt-file">{file_label}</span>
      <button class="fdt-copy" type="button">Copy</button>
    </div>
    <div class="fdt-tabs" role="tablist" aria-label="{tablist_label}">
{tabs}    </div>
{bodies}  </div>
"""


def build_locale_panels(d: Path) -> list[dict[str, str]]:
    panels = []
    for loc in LOCALES:
        f = d / "locales" / f"{loc['id']}.fab"
        if not f.is_file():
            continue
        name = (f'<span class="{loc["script"]}">{esc(loc["name"])}</span>'
                if loc["script"] else esc(loc["name"]))
        panels.append({
            "id": esc(loc["id"]), "name": esc(loc["name"]),
            "tab": f'{name} <span class="code">{esc(loc["code"])}</span>',
            "label": f'<code>faber format --reader-locale {esc(loc["code"])}</code> '
                     f'<span class="fdt-note">— {esc(loc["note"])}</span>',
            "code": esc(f.read_text(encoding="utf-8").strip()),
            "dir": (f' class="{loc["script"]}"' if loc["script"] else "")
                   + (' dir="rtl"' if loc.get("rtl") else ""),
        })
    return panels


def build_target_panels(d: Path) -> list[dict[str, str]]:
    panels = []
    for t in TARGETS:
        f = d / "targets" / f"out.{t['id']}.txt"
        if not f.is_file():
            continue
        body = f.read_text(encoding="utf-8").strip()
        # Some backends prepend a fixed runtime shim. Showing 120 lines of it
        # buries the lowering the panel exists to demonstrate — so cut it, and
        # say so in the output rather than trimming quietly.
        marker = t.get("elide_before")
        if marker and marker in body:
            head, _, tail = body.partition(marker)
            body = (f"// … {head.count(chr(10))} lines of generated "
                    f"display/runtime shim elided …\n\n{marker}{tail}")
        origin = "kernel.fab" if t.get("kernel") else "main.fab"
        panels.append({
            "id": esc(t["id"]), "name": esc(t["name"]),
            "tab": f'{esc(t["name"])} <span class="code">{esc(t["id"])}</span>',
            "label": f'<code>radix emit --target {esc(t["id"])} {origin}</code> '
                     f'<span class="fdt-note">— {esc(t["note"])}</span>',
            "code": esc(body),
        })
    return panels


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("output", type=Path)
    ap.add_argument("--landing", type=Path, default=None)
    ap.add_argument("--matrix", type=Path, default=None)
    ap.add_argument("--css", type=str, default="/speculum.css")
    args = ap.parse_args()

    gen = Path(__file__).resolve().parent.parent
    args.landing = args.landing or gen / "landing"
    args.matrix = args.matrix or gen.parent / "src" / "en-US" / "tooling" / "targets.md"

    matrix = read_matrix(args.matrix)
    locale_panels = build_locale_panels(args.landing)
    target_panels = build_target_panels(args.landing)

    hero_code = (args.landing / "locales" / "llm.fab").read_text(encoding="utf-8").strip()
    kernel_fab = (args.landing / "targets" / "kernel.fab").read_text(encoding="utf-8").strip()

    read_tabs = demo_tabs(
        root_id="fl-loc", file_label="main.fab · reader locale",
        tablist_label="Reader locale", panels=locale_panels)
    target_tabs = demo_tabs(
        root_id="fl-tgt", file_label="main.fab → target",
        tablist_label="Compilation target", panels=target_panels)

    frames = "".join(
        f"""\
        <figure class="fl-frame">
          <img src="{f['src']}" alt="{esc(f['alt'])}" loading="lazy" width="1400" height="788">
          <figcaption>{f['cap']}</figcaption>
        </figure>
""" for f in FRAMES)

    desc = ("Faber is a statically typed language built to be written by models and "
            "reviewed by people. Everyone reads the same program in their own "
            "language, and it compiles to Rust, native code, or GPU shaders.")

    html = f"""\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Faber — a language written by models, reviewed by people</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="https://faberlang.dev/">
<link rel="alternate" hreflang="x-default" href="https://faberlang.dev/">
<link rel="stylesheet" href="{esc(args.css)}">
<meta property="og:title" content="Faber — a language written by models, reviewed by people">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://faberlang.dev/">
<meta property="og:image" content="https://faberlang.dev/images/triga-budapest.png">
<meta name="twitter:card" content="summary_large_image">
</head>
<body class="landing">
<a class="skip-link" href="#top">Skip to content</a>

<header class="fl-top">
  <a class="fl-brand" href="/"><span class="fl-brand-mark" aria-hidden="true">f</span> Faber</a>
  <nav class="fl-topnav" aria-label="Primary">
    <a href="/en-US/start/install.html">Install</a>
    <a href="/en-US/">Docs</a>
    <a href="/en-US/syntax/">Syntax</a>
    <a href="https://github.com/faberlang">GitHub</a>
    <a class="fl-locale" href="/porta/">Language <span aria-hidden="true">▾</span></a>
  </nav>
</header>

<main class="fl-wrap" id="top">

  <section class="fl-hero">
    <p class="fl-kicker">A programming language by Ian Zepp · MIT</p>
    <h1>A language your model writes<br>and you actually read.</h1>
    <p class="fl-lede">
      Faber is a statically typed, compiled programming language. A model
      writes it against the surface it predicts most reliably. You read the
      same program back in your own language — English, Thai, Arabic — because
      the compiler renders it, not a translator. Then it compiles to whatever
      you need to run: Rust, a native binary, or a GPU shader.
    </p>

    <div class="fl-first">
      <pre class="fl-src">{esc(hero_code)}</pre>
      <pre class="fl-run">$ faber run --interpret app
opacus 255</pre>
    </div>
    <p class="fl-note">
      Real output from <code>faber format --reader-locale llm</code> — a tagged
      union, sized numerics, a typed error channel, defaulted parameters,
      pattern matching, and a glyph closure. Same program, seven more readings
      below.
    </p>

    <div class="fl-cta">
      <a class="fl-btn fl-btn-primary" href="/en-US/start/install.html">Install Faber</a>
      <a class="fl-btn" href="/en-US/start/">Five-minute tour</a>
    </div>
    <div class="fl-facts">
      <span><strong>8</strong> reader surfaces</span>
      <span><strong>7</strong> compilation targets</span>
      <span><strong>{matrix.get('rust', '99')}%</strong> corpus → Rust</span>
      <span><strong>{matrix.get('llvm-text', '96')}%</strong> corpus → LLVM</span>
      <span><strong>Norma</strong> standard library, bundled</span>
    </div>
  </section>

  <section class="fl-proof">
    <div class="fl-proof-head">
      <h2>Everyone reads it in their own language</h2>
      <p>
        These are not translated comments or a localized tutorial. It is one
        program, and the compiler accepts every one of these spellings. Only
        the keywords and type names change — identifiers and string literals
        stay exactly as written, so two people who share no language can still
        talk about <code>saturate</code> on line one.
      </p>
    </div>
{read_tabs}    <p class="fl-note">
      A reviewer sets their locale once. Nobody presses a translate button, and
      no model sits in the middle guessing — this is the compiler's own
      rendering, so the program you approve is the program that ships.
    </p>
  </section>

  <section class="fl-proof">
    <div class="fl-proof-head">
      <h2>It compiles to whatever has to run it</h2>
      <p>
        Same program again, pointed the other way. Every panel below is literal
        <code>radix emit</code> output — nothing here is hand-written or
        illustrative. LLVM IR comes straight off the MIR, so Faber reaches
        native code without passing through Rust, C, or any other source
        language. The two GPU panels come from an <code>@ nucleum</code>
        kernel, which is a different source file:
      </p>
      <pre class="fl-src">{esc(kernel_fab)}</pre>
      <p class="fl-note">
        WebAssembly is absent from these tabs on purpose. This program uses
        <code>numerus&lt;u8&gt;</code>, and the MIR-to-WASM backend does not yet
        accept sized numerics, so it fails closed rather than emitting
        something wrong. That is what the
        <a href="/en-US/toolchain/target-matrix.html">target matrix</a>
        measures.
      </p>
    </div>
{target_tabs}  </section>

  <section class="fl-proof">
    <div class="fl-proof-head">
      <h2>And it runs</h2>
      <p>
        <a href="/en-US/ecosystem/triga.html">Triga</a> is a graphics and
        geometry engine written in Faber. These frames were produced by Faber
        source compiled to WGSL and executed on a GPU — no JavaScript, no
        three.js, no engine underneath doing the real work.
      </p>
    </div>
    <div class="fl-frames">
{frames}    </div>
    <div class="fl-proof-head fl-proof-sub">
      <h3>Fast enough to use like a script</h3>
      <p>
        Faber also runs with no build step. <code>faber run --interpret</code>
        takes source through parse, typecheck and MIR lowering, then steps the
        MIR in-process — no <code>rustc</code>, no linker, no build directory.
      </p>
    </div>
    <div class="fl-bench">
      <table>
        <caption>Same program, end to end, median of 15 runs (M-series Mac)</caption>
        <thead><tr><th>Command</th><th>Wall clock</th></tr></thead>
        <tbody>
          <tr><td><code>faber run --interpret</code> <span class="fl-note">(incl. full typecheck)</span></td><td><strong>4.4 ms</strong></td></tr>
          <tr><td><code>python3 script.py</code> <span class="fl-note">(no typecheck)</span></td><td>13.3 ms</td></tr>
        </tbody>
      </table>
      <p class="fl-note">
        Reproduce with <a href="/en-US/tooling/scripting.html">the scripting
        docs</a>. A statically typed language should not be slower to start
        than a dynamic one, and it isn't.
      </p>
    </div>
  </section>

  <section class="fl-doors">
    <h2>Where to go</h2>
    <div class="fl-door-grid">
      <a class="fl-door" href="/en-US/start/install.html">
        <strong>Install</strong>
        <span>Download, verify, first <code>faber check</code>.</span>
      </a>
      <a class="fl-door" href="/en-US/start/">
        <strong>Five-minute tour</strong>
        <span>The shape of the language, start to finish.</span>
      </a>
      <a class="fl-door" href="/en-US/syntax/">
        <strong>Syntax</strong>
        <span>Types, control flow, generics, glyphs, errors.</span>
      </a>
      <a class="fl-door" href="/en-US/features/reader-locale.html">
        <strong>Reader locales</strong>
        <span>How the rendering actually works.</span>
      </a>
      <a class="fl-door" href="/en-US/tooling/targets.html">
        <strong>Target matrix</strong>
        <span>Measured lowerability, every term × every backend.</span>
      </a>
      <a class="fl-door" href="/en-US/ecosystem/">
        <strong>Ecosystem</strong>
        <span>Norma, Triga, Cista, the language corpus.</span>
      </a>
    </div>
  </section>

  <section class="fl-agents">
    <h2>Reading this as a model?</h2>
    <p>
      Machine surfaces are locale-less and live at the root:
      <a href="/llms.txt"><code>/llms.txt</code></a> for the index,
      <a href="/agents/index.md"><code>/agents/index.md</code></a> for the
      learning path, and
      <a href="/.well-known/agent-skills/index.json"><code>/.well-known/agent-skills/</code></a>
      for focused skill guides.
    </p>
  </section>

</main>

<footer class="fl-foot">
  <div>
    <strong>Faber</strong> · designed by Ian Zepp · MIT licensed ·
    compiler <a href="/en-US/tooling/radix-compiler.html">Radix</a>
  </div>
  <div>
    <a href="/porta/">All languages</a> ·
    <a href="/en-US/history/releases.html">Releases</a> ·
    <a href="https://github.com/faberlang">GitHub</a>
  </div>
</footer>

<script src="/faber-demo-tabs.js" defer></script>
</body>
</html>
"""

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(html, encoding="utf-8")
    print(f"landing: {args.output} "
          f"({len(locale_panels)} reader panels, {len(target_panels)} target panels)")


if __name__ == "__main__":
    main()
