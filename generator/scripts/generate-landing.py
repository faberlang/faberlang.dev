#!/usr/bin/env python3
"""
generate-landing.py — Generate the Faber landing page at /.

The page answers "what is this?" before anything else, in this order:

    1. claim + the one program, in every reader locale, with its real output
    2. locale strip: a door into each language's own docs home
    3. why it suits models: mechanical grammar, explicit types, math operators
    4. cross-compilation: one library emitted for each target, plus a
       capability table parsed from `faber targets`
    5. libraries (Norma, Gradus, Triga, Tela, Inferentia, Cista)
    6. the grammar, sized from the generated EBNF
    7. compute as one capability among them, with its honesty bounds
    8. where to go; machine surfaces

Compute and GPU work used to be the headline (commit e8d3dde91). They are now
one section among several: the language is the subject, not one workload.

Every code panel is compiler output captured by capture-landing-panels.sh —
never hand-authored. Run that script after a compiler or reader-pack change,
then rebuild. Counts (grammar productions) and the target capability table are
read from their sources at generation time so they cannot drift.

CLI:
    generate-landing.py <output.html> [--landing path] [--ebnf path]
                        [--css /speculum.css]
"""

from __future__ import annotations

import argparse
import html as html_mod
import re
from pathlib import Path

# Reader-pack axis. Order is the argument: English reader surface, canonical
# Latin, then the human packs. `site` is the docs home the locale strip links
# to; Latin is canonical Faber and has no docs site of its own.
LOCALES: list[dict[str, str]] = [
    {"id": "en", "name": "English", "code": "en", "script": "", "site": "en-US",
     "note": "English reader surface — the base spelling for everyday source"},
    {"id": "la", "name": "Latin", "code": "la", "script": "", "site": "",
     "note": "canonical Faber — the classical surface the language is named for"},
    {"id": "th-TH", "name": "ภาษาไทย", "code": "th-TH", "script": "th", "site": "th-TH",
     "note": "Thai — spaceless script"},
    {"id": "zh-Hans", "name": "简体中文", "code": "zh-Hans", "script": "zh", "site": "zh-Hans",
     "note": "Simplified Chinese"},
    {"id": "zh-Hant", "name": "繁體中文", "code": "zh-Hant", "script": "zh", "site": "zh-Hant",
     "note": "Traditional Chinese"},
    {"id": "vi", "name": "Tiếng Việt", "code": "vi", "script": "", "site": "vi",
     "note": "Vietnamese"},
    {"id": "ar", "name": "العربية", "code": "ar", "script": "ar", "site": "ar",
     "note": "Arabic — right-to-left, bidi isolated", "rtl": "1"},
    {"id": "hi", "name": "हिन्दी", "code": "hi", "script": "hi", "site": "hi",
     "note": "Hindi — Devanagari"},
]

# Library targets shown as emitted source. Only targets whose emitted library
# was compile-checked in its own toolchain are listed (see the capture script).
TARGETS: list[dict[str, str]] = [
    {"id": "rust", "name": "Rust",
     "note": "builds as a Cargo package with `faber build`; uses the small faber runtime crate",
     "elide_before": "#[derive(Clone, PartialEq)]"},
    {"id": "ts", "name": "TypeScript",
     "note": "a source file you add to your project; imports `@faber/runtime`",
     "elide_before": "class Span {"},
    {"id": "go", "name": "Go", "note": "a source file in `package main`"},
    {"id": "swift", "name": "Swift", "note": "a source file; no runtime dependency"},
]

# Capability table rows: (target id in `faber targets`, display name, what it is).
# The yes/no cells come from the toolchain; the sentence is editorial and kept
# within what the cells and `radix/docs/design/target-capability-matrix.md`
# actually say.
CAPABILITY_GROUPS: list[tuple[str, list[tuple[str, str, str]]]] = [
    ("Source for your existing project", [
        ("rust", "Rust", "The primary target: a full Cargo package, and runnable through faber."),
        ("ts", "TypeScript", "Source emission; package assembly is not built yet."),
        ("go", "Go", "Source emission; package assembly is not built yet."),
        ("swift", "Swift", "Source emission; a subset."),
        ("python", "Python", "Source emission; a limited subset."),
        ("haskell", "Haskell", "Source emission; a limited subset."),
    ]),
    ("Systems, native and device", [
        ("llvm-host", "Native executable", "MIR lowered to LLVM, linked for the local host."),
        ("wasm-text", "WebAssembly", "WAT text; binary conversion uses external tools."),
        ("llvm-text", "LLVM IR", "Text for LLVM tooling; also the CUDA device route."),
        ("metal-text", "Metal", "Shader source; device execution through the Metal route."),
        ("wgsl-text", "WGSL", "WebGPU compute shader source."),
    ]),
    ("Portable package images", [
        ("fhir", "FHIR", "A portable analyzed-program package envelope."),
        ("fmir", "FMIR", "A source-independent package image that faber can run."),
    ]),
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

# Libraries: honest one-line status, verified against each repo's own README /
# AGENTS.md / source on 2026-09-30. Status wording is deliberately plain.
LIBRARIES: list[dict[str, str]] = [
    {"name": "Norma", "href": "/en-US/libraries/norma.html", "status": "the standard library",
     "desc": "The default public library: text, JSON, TOML and YAML, files, HTTP, time, "
             "crypto, collections and math, imported as <code>norma:*</code>."},
    {"name": "Gradus", "href": "/en-US/libraries/gradus.html", "status": "autograd and ML",
     "desc": "Automatic differentiation, losses, optimizers and neural-network primitives. "
             "Models are pure functions; the backward pass is compiler-generated code."},
    {"name": "Triga", "href": "/en-US/libraries/triga.html", "status": "graphics and geometry",
     "desc": "Scene graph, materials and geometry modeled on three.js shapes, written as a "
             "small, readable Faber library."},
    {"name": "Tela", "href": "/en-US/libraries/tela.html", "status": "early; UI and view protocol",
     "desc": "Typed HTML and SVG view values with fail-closed validation and deterministic "
             "HTML and CSS output. The static renderer comes first."},
    {"name": "Inferentia", "href": "/en-US/libraries/inferentia.html", "status": "in development",
     "desc": "A local-first GGUF inference server written in Faber. Today it is a command-line "
             "shell; model loading and HTTP serving are the next stages."},
    {"name": "Cista", "href": "/en-US/toolchain/packages.html", "status": "package store",
     "desc": "The package manager: install, resolve, inspect and cache Faber packages, "
             "independent of the compiler."},
]


def esc(s: str) -> str:
    return html_mod.escape(s)


def ebnf_productions(path: Path) -> int:
    """Count grammar productions in the generated EBNF so the page's size claim
    is read from the grammar, not typed in."""
    text = path.read_text(encoding="utf-8")
    return len(re.findall(r"^# \[\d+\] ", text, re.M))


def read_targets(path: Path) -> dict[str, dict[str, str]]:
    """Parse `faber targets` rows: `key available=yes check=yes build=yes ...`."""
    out: dict[str, dict[str, str]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        key, _, rest = line.partition(" ")
        row = {m.group(1): m.group(2) for m in re.finditer(r"(\w+)=(\S+)", rest.split(" note=")[0])}
        if key and row:
            out[key] = row
    return out


def yn(v: str | None) -> str:
    return "yes" if v == "yes" else "—"


def capability_table(targets: dict[str, dict[str, str]]) -> str:
    rows = ""
    for group, items in CAPABILITY_GROUPS:
        rows += f'        <tr class="fl-cap-group"><th colspan="5" scope="colgroup">{esc(group)}</th></tr>\n'
        for tid, name, sentence in items:
            t = targets.get(tid)
            if t is None or t.get("available") != "yes":
                raise SystemExit(f"capability table: `{tid}` is not an available target in `faber targets`")
            rows += (
                f'        <tr><td><strong>{esc(name)}</strong></td>'
                f'<td>{yn(t.get("build"))}</td><td>{yn(t.get("package"))}</td>'
                f'<td>{yn(t.get("run"))}</td><td>{esc(sentence)}</td></tr>\n'
            )
    return f"""\
    <table class="fl-cap">
      <caption>What each target does today. The first three columns are read from <code>faber targets</code>.</caption>
      <thead><tr><th>Target</th><th>Emits</th><th>Package</th><th>Runs</th><th>In practice</th></tr></thead>
      <tbody>
{rows}      </tbody>
    </table>
"""


def demo_tabs(*, root_id: str, file_label: str, tablist_label: str,
              panels: list[dict[str, str]]) -> str:
    tabs = bodies = ""
    for i, p in enumerate(panels):
        pid = f"{root_id}-p-{p['id']}"
        tabs += (
            f'    <button class="fdt-tab" role="tab" id="{root_id}-t-{p["id"]}" '
            f'data-panel="{pid}" data-name="{p["name"]}" aria-controls="{pid}" '
            f'title="{p["hint"]}" '
            f'aria-selected="{"true" if i == 0 else "false"}" '
            f'tabindex="{"0" if i == 0 else "-1"}">{p["tab"]}</button>\n'
        )
        bodies += (
            f'    <div class="fdt-panel{" active" if i == 0 else ""}" id="{pid}" '
            f'role="tabpanel" aria-labelledby="{root_id}-t-{p["id"]}">'
            f'<div class="fdt-panel-label">{p["label"]}</div>'
            f'<pre{p.get("script_class", "")}{p.get("dir", "")}>'
            f'<code class="lang-{p["lang"]}">{p["code"]}</code></pre></div>\n'
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
            raise SystemExit(f"missing locale panel {f}; run capture-landing-panels.sh")
        name = (f'<span class="{loc["script"]}">{esc(loc["name"])}</span>'
                if loc["script"] else esc(loc["name"]))
        panels.append({
            "id": esc(loc["id"]), "name": esc(loc["name"]),
            "tab": name, "hint": esc(loc["code"]),
            "label": f'<code>faber convert --to {esc(loc["code"])}</code> '
                     f'<span class="fdt-note">— {esc(loc["note"])}</span>',
            "code": esc(f.read_text(encoding="utf-8").strip()),
            # The panel names its own reader locale so highlight-code.py paints
            # each pack in its own spellings; the landing page is locale-less at
            # the site root and has no page locale to inherit.
            "lang": f'faber locale={esc(loc["code"])}',
            "script_class": f' class="{loc["script"]}"' if loc["script"] else "",
            "dir": ' dir="rtl"' if loc.get("rtl") else "",
        })
    return panels


def build_target_panels(d: Path) -> list[dict[str, str]]:
    panels = []
    for t in TARGETS:
        f = d / "targets" / f"out.{t['id']}.txt"
        if not f.is_file():
            raise SystemExit(f"missing target panel {f}; run capture-landing-panels.sh")
        body = f.read_text(encoding="utf-8").strip()
        # Some backends prepend a fixed header or runtime shim. Showing it buries
        # the lowering the panel exists to demonstrate — so cut it, and say so in
        # the output rather than trimming quietly.
        marker = t.get("elide_before")
        if marker and marker in body:
            head, _, tail = body.partition(marker)
            body = (f"// … {head.count(chr(10)) + 1} lines of generated header and "
                    f"runtime shim elided …\n\n{marker}{tail}")
        panels.append({
            "id": esc(t["id"]), "name": esc(t["name"]),
            "tab": esc(t["name"]), "hint": esc(t["id"]),
            "label": f'<code>radix emit --target {esc(t["id"])} span.fab</code> '
                     f'<span class="fdt-note">— {t["note"].replace("`", "")}</span>',
            "code": esc(body),
            "lang": esc(t["id"]),
        })
    return panels


def locale_strip() -> str:
    tiles = ""
    for loc in LOCALES:
        if not loc["site"]:
            continue
        script = f' class="{loc["script"]}"' if loc["script"] else ""
        rtl = ' dir="rtl"' if loc.get("rtl") else ""
        tiles += (
            f'      <a class="fl-loc" href="/{loc["site"]}/" hreflang="{esc(loc["code"])}" '
            f'lang="{esc(loc["code"])}">'
            f'<span class="fl-loc-name"><span{script}{rtl}>{esc(loc["name"])}</span></span>'
            f'<span class="fl-loc-code">{esc(loc["code"])}</span></a>\n'
        )
    return f'    <div class="fl-locs" role="list" aria-label="Documentation by language">\n{tiles}    </div>\n'


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("output", type=Path)
    ap.add_argument("--landing", type=Path, default=None)
    ap.add_argument("--ebnf", type=Path, default=None)
    ap.add_argument("--css", type=str, default="/speculum.css")
    args = ap.parse_args()

    gen = Path(__file__).resolve().parent.parent
    args.landing = args.landing or gen / "landing"
    args.ebnf = args.ebnf or gen.parent.parent / "faber" / "docs" / "EBNF.md"

    productions = ebnf_productions(args.ebnf)
    targets = read_targets(args.landing / "targets" / "faber-targets.txt")
    locale_panels = build_locale_panels(args.landing)
    target_panels = build_target_panels(args.landing)
    program_out = (args.landing / "program.out.txt").read_text(encoding="utf-8").strip()
    span_fab = (args.landing / "targets" / "span.fab").read_text(encoding="utf-8").strip()

    read_tabs = demo_tabs(
        root_id="fl-loc", file_label="main.fab · reader locale",
        tablist_label="Reader locale", panels=locale_panels)
    target_tabs = demo_tabs(
        root_id="fl-tgt", file_label="span.fab → target",
        tablist_label="Compilation target", panels=target_panels)

    libs = "".join(
        f"""\
      <a class="fl-lib" href="{l['href']}">
        <strong>{esc(l['name'])}</strong>
        <em>{esc(l['status'])}</em>
        <span>{l['desc']}</span>
      </a>
""" for l in LIBRARIES)

    frames = "".join(
        f"""\
        <figure class="fl-frame">
          <img src="{f['src']}" alt="{esc(f['alt'])}" loading="lazy" width="1400" height="788">
          <figcaption>{f['cap']}</figcaption>
        </figure>
""" for f in FRAMES)

    title = "Faber — a programming language models write well, in the language you read"
    desc = ("Faber is a statically typed programming language for coding agents and human "
            "authors: a mechanical grammar, explicit generic types and math-oriented "
            "operators, written in eight language surfaces and compiled to Rust, "
            "TypeScript, Go, Swift and more.")

    html = f"""\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="https://faberlang.dev/">
<link rel="alternate" hreflang="x-default" href="https://faberlang.dev/">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;600;700&amp;family=Noto+Serif:wght@400;600&amp;family=Noto+Sans+Mono:wght@400;600&amp;family=Noto+Sans+Arabic:wght@400;600;700&amp;family=Noto+Sans+Devanagari:wght@400;600&amp;family=Noto+Sans+SC:wght@400;600&amp;family=Noto+Sans+Thai:wght@400;600&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="{esc(args.css)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://faberlang.dev/">
<meta property="og:image" content="https://faberlang.dev/images/triga-budapest.png">
<meta name="twitter:card" content="summary_large_image">
</head>
<body class="landing">
<a class="skip-link" href="#top">Skip to content</a>

<aside class="fl-banner" role="status">
  <strong>Experimental through version 1.</strong>
  Version 0 was alpha. This is the first language release: the interface is
  relatively stable, not frozen. Nothing is promised stable until version 2.
</aside>

<header class="fl-top">
  <a class="fl-brand" href="/"><span class="fl-brand-mark" aria-hidden="true">f</span> Faber</a>
  <nav class="fl-topnav" aria-label="Primary">
    <a href="/en-US/start/install.html">Install</a>
    <a href="/en-US/">Docs</a>
    <a href="/en-US/language/">Language</a>
    <a href="/en-US/libraries/">Libraries</a>
    <a href="https://github.com/faberlang">GitHub</a>
    <a class="fl-locale" href="/porta/">All languages <span aria-hidden="true">▾</span></a>
  </nav>
</header>

<main class="fl-wrap" id="top">

  <section class="fl-hero">
    <p class="fl-kicker">A statically typed language for coding agents and human authors · MIT</p>
    <h1>Written by models,<br>read in your language.</h1>
    <p class="fl-lede">
      Faber has a clear mechanical grammar, explicit static and generic types,
      and math-oriented operators. The same program is written and read in
      eight language surfaces, and compiles to Rust, TypeScript, Go, Swift and
      more — so a library you write once can go into the project you already
      have.
    </p>
    <p class="fl-open-source">
      The language, public libraries, examples, and tooling ship under the
      <strong>MIT</strong> license. <strong>Radix</strong>, the compiler, is
      closed only while it is under active development. That is temporary,
      not a permanent fence.
    </p>
    <div class="fl-cta">
      <a class="fl-btn fl-btn-primary" href="/en-US/start/install.html">Install</a>
      <a class="fl-btn" href="/en-US/start/">Five-minute tour</a>
      <a class="fl-btn" href="/en-US/reference/grammar.html">Read the grammar</a>
    </div>
{read_tabs}    <pre class="fl-run">$ faber run
{esc(program_out)}</pre>
    <p class="fl-note">
      One program, eight readings. Every tab is the compiler’s own rendering
      (<code>faber convert</code>), and each one runs. Keywords, types and
      diagnostics change; identifiers and string literals do not.
    </p>
  </section>

  <section class="fl-proof" id="languages">
    <div class="fl-proof-head">
      <h2>Start in your own language</h2>
      <p>
        People should not need English to use a model for code, or to read what
        the model wrote. Each language has its own documentation home, written
        in that language. Source is written the same way: one reader locale per
        file, sealed against the others, so a Thai file contains Thai keywords
        and nothing else.
      </p>
    </div>
{locale_strip()}    <p class="fl-note">
      Latin is the canonical interchange form the language is named for. Reader
      locales also localize compiler diagnostics. <a href="/porta/">See all languages</a> ·
      <a href="/en-US/language/reader-locales.html">How reader locales work</a>
    </p>
  </section>

  <section class="fl-proof" id="models">
    <div class="fl-proof-head">
      <h2>Built for models to write</h2>
      <p>
        A model writes best against a surface with few surprises. Faber keeps
        the rules small, regular and explicit, then shows the result in the
        reader’s language.
      </p>
    </div>
    <div class="fl-points">
      <div class="fl-point">
        <strong>A mechanical grammar</strong>
        <span>
          {productions} grammar productions, generated and checked as the parser’s
          authority. One construct has one spelling. Arrows mean runtime effects
          (<code>←</code> assign, <code>→</code> return, <code>⇥</code> error channel);
          <code>=</code> and <code>:</code> only state compile-time facts.
          <a href="/en-US/reference/grammar.html">Read the grammar</a>
        </span>
      </div>
      <div class="fl-point">
        <strong>Explicit static and generic types</strong>
        <span>
          Declarations are type-first: <code>f64 low</code>, never <code>low: f64</code>.
          Nullability is written <code>T ∪ none</code>. Generics are written out
          (<code>fn choose&lt;T&gt;</code>), and crossing between integer and float is
          an explicit <code>↦</code>, not an accident.
          <a href="/en-US/language/types.html">Types and values</a>
        </span>
      </div>
      <div class="fl-point">
        <strong>Math-oriented operators</strong>
        <span>
          Integer <code>/</code> floors, so <code>-7 / 2</code> is <code>-4</code>; true
          division is <code>÷</code>. Comparisons read as math (<code>≤ ≥ ≠ ≈</code>),
          and tensor work has its own operators (<code>·</code> matmul,
          <code>⊙</code> elementwise). When math and hardware convention disagree,
          Faber follows the math.
          <a href="/en-US/language/glyphs.html">Glyphs and Latin</a>
        </span>
      </div>
      <div class="fl-point">
        <strong>Machine-readable by design</strong>
        <span>
          Diagnostics are coded and explainable. The documentation ships an agent
          index and focused skill guides at fixed paths, so a model can learn the
          language from the site itself.
          <a href="/llms.txt">/llms.txt</a>
        </span>
      </div>
    </div>
  </section>

  <section class="fl-proof" id="targets">
    <div class="fl-proof-head">
      <h2>Write it once. Put it in the project you already have.</h2>
      <p>
        Faber compiles through one analyzed program to many targets. Write a
        library in Faber, emit it in the language your project already uses, and
        add it alongside your existing code. This small library, with no
        generics and no <code>main</code>, is emitted below exactly as
        <code>radix emit</code> produces it, and each panel was checked in its
        own toolchain.
      </p>
      <pre class="fl-src"><code class="lang-faber locale=en">{esc(span_fab)}</code></pre>
    </div>
{target_tabs}    <p class="fl-note">
      Rust builds as a Cargo package today. TypeScript, Go and Swift give you
      source files to add to your project; assembling them into installable
      packages is not built yet. Support is stated target by target: generics and
      some operators do not lower to every target, and the target matrix records
      where. <a href="/en-US/toolchain/target-matrix.html">Read the target matrix</a>
    </p>
{capability_table(targets)}  </section>

  <section class="fl-proof" id="libraries">
    <div class="fl-proof-head">
      <h2>Libraries written in Faber</h2>
      <p>
        The libraries are ordinary Faber source. They show what the language is
        for, and each one can be read, changed and emitted like your own code.
        Status is stated plainly.
      </p>
    </div>
    <div class="fl-libs">
{libs}    </div>
    <div class="fl-frames">
{frames}    </div>
    <p class="fl-note">
      Example scenes built with <a href="/en-US/libraries/triga.html">Triga</a>.
    </p>
  </section>

  <section class="fl-proof" id="grammar">
    <div class="fl-proof-head">
      <h2>A grammar you can read in one sitting</h2>
      <p>
        The language is specified as {productions} productions in a single
        EBNF, generated from one source and published in full. It is large
        enough to be expressive and regular enough to hold in your head or a
        model’s context. The reference pages are generated from the same source,
        so they cannot disagree with the parser.
      </p>
      <p class="fl-note">
        <a href="/en-US/reference/grammar.html">EBNF grammar</a> ·
        <a href="/en-US/syntax/">Syntax guide</a> ·
        <a href="/en-US/corpus/">Corpus of keyword examples</a> ·
        <a href="/en-US/cheatsheet/">Cheat sheet</a>
      </p>
    </div>
  </section>

  <section class="fl-proof" id="compute">
    <div class="fl-proof-head">
      <h2>Compute is one thing you can build</h2>
      <p>
        The same language carries numeric and device work. Tensor operators and
        <code>@ nucleum</code> kernels lower to WGSL, Metal and CUDA routes, and
        <a href="/en-US/libraries/gradus.html">Gradus</a> uses them for
        autograd. Device execution is explicit and fail-closed: a requested
        backend never silently falls back to CPU. Bounded training runs on
        accepted Metal and CUDA machines; device inference is not shipped.
      </p>
      <p class="fl-note">
        <a href="/en-US/toolchain/compiling.html#device-execution">Device execution contract</a> ·
        <a href="https://github.com/faberlang/examples/tree/main/training/device-summa">Training proof</a>
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
      <a class="fl-door" href="/en-US/language/">
        <strong>Language</strong>
        <span>Types, control flow, generics, glyphs, errors.</span>
      </a>
      <a class="fl-door" href="/en-US/language/reader-locales.html">
        <strong>Reader locales</strong>
        <span>How the same program reads in every language.</span>
      </a>
      <a class="fl-door" href="/en-US/toolchain/target-matrix.html">
        <strong>Target matrix</strong>
        <span>Measured lowerability, every term × every backend.</span>
      </a>
      <a class="fl-door" href="/en-US/libraries/">
        <strong>Libraries</strong>
        <span>Norma, Gradus, Triga, Tela, Inferentia, Cista.</span>
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
    <strong>Faber</strong> · designed by Ian Zepp · language &amp; libraries MIT ·
    <a href="/en-US/toolchain/radix.html">Radix</a> closed while under active development
  </div>
  <div>
    <a href="/porta/">All languages</a> ·
    <a href="/en-US/releases/">Releases</a> ·
    <a href="https://github.com/faberlang">GitHub</a>
  </div>
</footer>

<script src="/faber-demo-tabs.js" defer></script>
<script src="/faber-ambient.js" defer></script>
</body>
</html>
"""

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(html, encoding="utf-8")
    print(f"landing: {args.output} "
          f"({len(locale_panels)} reader panels, {len(target_panels)} target panels, "
          f"{productions} grammar productions)")


if __name__ == "__main__":
    main()
