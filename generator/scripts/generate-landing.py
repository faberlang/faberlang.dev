#!/usr/bin/env python3
"""
generate-landing.py — Generate the Faber landing page at /.

The landing page states one claim and then proves it three times:

    claim   meaning lives in the semantic core, not in any surface
    proof 1 one program, seven human renderings   (reader-locale packs)
    proof 2 one program, seven machine renderings (codegen targets)
    proof 3 it runs — GPU frames from Triga, and interpreted-run latency

Both proof panels reuse the existing `.faber-demo-tabs` component, so the
no-JS fallback stays a readable stack of real <pre> text.

CLI:
    generate-landing.py <output.html> [--locales path] [--exemplars path]
                        [--targets path] [--matrix path] [--css /speculum.css]

Defaults:
    --locales     generator/locales.toml
    --exemplars   generator/portal/exemplars   (proof 1 panels)
    --targets     generator/landing/targets    (proof 2 panels, real emissions)
    --matrix      src/en-US/tooling/targets.md (generated coverage numbers)
    --css         /speculum.css
"""

from __future__ import annotations

import argparse
import html as html_mod
import re
import tomllib
from pathlib import Path

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

# Proof 2 axis. Order is the argument: source languages you already read,
# then the IRs, then the two GPU shading languages.
TARGETS: list[dict[str, str]] = [
    {"id": "rust", "file": "out.rust.txt", "name": "Rust",
     "note": "primary backend — reviewable source, then a native binary"},
    {"id": "go", "file": "out.go.txt", "name": "Go",
     "note": "file emission"},
    {"id": "ts", "file": "out.ts.txt", "name": "TypeScript",
     "note": "file emission", "elide_before": "function saturate"},
    {"id": "llvm-text", "file": "out.llvm-text.txt", "name": "LLVM IR",
     "note": "MIR-backed — native code with no source language in between"},
    {"id": "wasm-text", "file": "out.wasm-text.txt", "name": "WebAssembly",
     "note": "MIR-backed WAT, external host"},
    {"id": "wgsl-text", "file": "out.wgsl-text.txt", "name": "WGSL",
     "note": "GPU compute shader — from an @ nucleum kernel", "kernel": "1"},
    {"id": "metal-text", "file": "out.metal-text.txt", "name": "Metal",
     "note": "GPU compute shader — from an @ nucleum kernel", "kernel": "1"},
]

# Proof 3 frames. Rendered by Triga, written in Faber, run on the GPU.
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


def load_locales(path: Path) -> dict:
    with path.open("rb") as f:
        return tomllib.load(f).get("locales", {})


def sort_locale_keys(keys: list[str]) -> list[str]:
    rest = sorted(k for k in keys if k not in ("en-US", "th-TH"))
    ordered = [k for k in ("en-US", "th-TH") if k in keys]
    ordered.extend(rest)
    return ordered


def read_matrix(path: Path) -> dict[str, str]:
    """Pull the generated per-target coverage percentages off the targets page.

    The numbers are measured by `generate-target-matrix.py`; reading them here
    keeps the landing page from drifting away from its own evidence.
    """
    out: dict[str, str] = {}
    if not path.is_file():
        return out
    for row in re.finditer(
        r"^\|\s*([a-z-]+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)%\s*\|",
        path.read_text(encoding="utf-8"),
        re.M,
    ):
        out[row.group(1)] = row.group(4)
    return out


def demo_tabs(
    *,
    root_id: str,
    file_label: str,
    tablist_label: str,
    panels: list[dict[str, str]],
    hero: bool = False,
) -> str:
    """Render a .faber-demo-tabs card. Panels: id, tab, label, code, dir."""
    tabs = ""
    bodies = ""
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
    cls = "faber-demo-tabs fdt-hero" if hero else "faber-demo-tabs"
    return f"""\
  <div class="{cls}" data-fdt>
    <div class="fdt-bar">
      <span class="fdt-mark" aria-hidden="true">f</span>
      <span class="fdt-file">{file_label}</span>
      <button class="fdt-copy" type="button">Copy</button>
    </div>
    <div class="fdt-tabs" role="tablist" aria-label="{tablist_label}">
{tabs}    </div>
{bodies}  </div>
"""


def build_locale_panels(registry: dict, exemplars: Path) -> list[dict[str, str]]:
    panels = []
    for site in sort_locale_keys(list(registry.keys())):
        entry = registry[site]
        reader = entry.get("reader_locale", site)
        native = entry.get("native_name", site)
        script_cls = SCRIPT_CLASSES.get(entry.get("native_script", ""), "")
        sample_path = exemplars / f"salve-munde.{reader}.fab"
        if not sample_path.is_file():
            continue
        native_span = (
            f'<span class="{script_cls}">{esc(native)}</span>' if script_cls else esc(native)
        )
        panels.append({
            "id": esc(site),
            "name": esc(native),
            "tab": f'{native_span} <span class="code">{esc(reader)}</span>',
            "label": f'{esc(native)} · {esc(reader)} · '
                     f'<a href="/{esc(site)}/">read the docs in {esc(native)} →</a>',
            "code": esc(sample_path.read_text(encoding="utf-8").strip()),
            "dir": ' dir="rtl"' if reader in RTL_READER_LOCALES else "",
        })
    return panels


def build_target_panels(targets_dir: Path) -> list[dict[str, str]]:
    panels = []
    for t in TARGETS:
        out = targets_dir / t["file"]
        if not out.is_file():
            continue
        body = out.read_text(encoding="utf-8").strip()
        # Some backends prepend a fixed runtime shim. Showing 120 lines of it
        # buries the lowering the panel exists to demonstrate, so cut it — but
        # say so in the output rather than quietly trimming.
        marker = t.get("elide_before")
        if marker and marker in body:
            head, _, tail = body.partition(marker)
            skipped = head.count("\n")
            body = (
                f"// … {skipped} lines of generated display/runtime shim elided …\n\n"
                f"{marker}{tail}"
            )
        origin = "kernel.fab" if t.get("kernel") else "main.fab"
        panels.append({
            "id": esc(t["id"]),
            "name": esc(t["name"]),
            "tab": f'{esc(t["name"])} <span class="code">{esc(t["id"])}</span>',
            "label": f'<code>radix emit --target {esc(t["id"])} {origin}</code> '
                     f'<span class="fdt-note">— {esc(t["note"])}</span>',
            "code": esc(body),
        })
    return panels


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("output", type=Path)
    ap.add_argument("--locales", type=Path, default=None)
    ap.add_argument("--exemplars", type=Path, default=None)
    ap.add_argument("--targets", type=Path, default=None)
    ap.add_argument("--matrix", type=Path, default=None)
    ap.add_argument("--css", type=str, default="/speculum.css")
    args = ap.parse_args()

    generator_dir = Path(__file__).resolve().parent.parent
    repo_dir = generator_dir.parent
    args.locales = args.locales or generator_dir / "locales.toml"
    args.exemplars = args.exemplars or generator_dir / "portal" / "exemplars"
    args.targets = args.targets or generator_dir / "landing" / "targets"
    args.matrix = args.matrix or repo_dir / "src" / "en-US" / "tooling" / "targets.md"

    registry = load_locales(args.locales)
    matrix = read_matrix(args.matrix)

    locale_panels = build_locale_panels(registry, args.exemplars)
    target_panels = build_target_panels(args.targets)

    source_fab = (args.targets / "source.fab").read_text(encoding="utf-8").strip()
    kernel_fab = (args.targets / "kernel.fab").read_text(encoding="utf-8").strip()

    proof1 = demo_tabs(
        root_id="fl-loc",
        file_label="salve-munde.fab",
        tablist_label="Reader locale",
        panels=locale_panels,
        hero=True,
    )
    proof2 = demo_tabs(
        root_id="fl-tgt",
        file_label="main.fab → target",
        tablist_label="Compilation target",
        panels=target_panels,
        hero=True,
    )

    frames = ""
    for f in FRAMES:
        frames += f"""\
        <figure class="fl-frame">
          <img src="{f['src']}" alt="{esc(f['alt'])}" loading="lazy" width="1400" height="788">
          <figcaption>{f['cap']}</figcaption>
        </figure>
"""

    def pct(key: str, fallback: str) -> str:
        return matrix.get(key, fallback)

    css_href = esc(args.css)
    desc = (
        "Faber is a programming language whose meaning lives in a semantic core, "
        "not in its syntax. One program compiles to Rust, Go, LLVM IR, WebAssembly "
        "and GPU compute shaders — and renders in seven human languages."
    )

    html = f"""\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Faber — one semantic core, many renderings</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="https://faberlang.dev/">
<link rel="alternate" hreflang="x-default" href="https://faberlang.dev/">
<link rel="stylesheet" href="{css_href}">
<meta property="og:title" content="Faber — one semantic core, many renderings">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://faberlang.dev/">
<meta property="og:image" content="https://faberlang.dev/images/triga-budapest.png">
<meta name="twitter:card" content="summary_large_image">
</head>
<body class="landing">
<a class="skip-link" href="#claim">Skip to content</a>

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

<main class="fl-wrap">

  <section class="fl-hero" id="claim">
    <p class="fl-kicker">A programming language by Ian Zepp · MIT</p>
    <h1>Meaning lives in the core,<br>not in the syntax.</h1>
    <p class="fl-lede">
      Faber programs are stored as a semantic core, not as text in one
      particular language. Everything else — the words a human reads, the
      machine code that finally runs — is a <em>rendering</em> of that core.
      Change the rendering and the program does not change.
    </p>
    <p class="fl-lede">
      That single property is why Faber can print itself in Thai, and why the
      same function can come out as Rust, as LLVM IR, or as a GPU compute
      shader. It is one architectural bet, pointed in two directions.
    </p>
    <div class="fl-cta">
      <a class="fl-btn fl-btn-primary" href="/en-US/start/install.html">Install Faber 1.3.0</a>
      <a class="fl-btn" href="/en-US/start/">Five-minute tour</a>
    </div>
    <div class="fl-facts">
      <span><strong>7</strong> compilation targets</span>
      <span><strong>7</strong> reader locales</span>
      <span><strong>{pct('rust', '99')}%</strong> corpus → Rust</span>
      <span><strong>{pct('llvm-text', '96')}%</strong> corpus → LLVM</span>
      <span><strong>Norma</strong> standard library, bundled</span>
    </div>
  </section>

  <section class="fl-proof">
    <div class="fl-proof-head">
      <span class="fl-proof-n">Proof 1</span>
      <h2>One program, seven human renderings</h2>
      <p>
        These are not translations of a comment or a tutorial. They are the
        same program, and the compiler accepts every one of them. The keywords
        are supplied by a <a href="/en-US/features/reader-locale.html">reader-locale
        pack</a>; identifiers stay in canonical Latin so code stays portable
        between people who do not share a language.
      </p>
    </div>
{proof1}  </section>

  <section class="fl-proof">
    <div class="fl-proof-head">
      <span class="fl-proof-n">Proof 2</span>
      <h2>One program, seven machine renderings</h2>
      <p>
        Same idea, other direction. This function —
      </p>
      <pre class="fl-src">{esc(source_fab)}</pre>
      <p>
        — lowers to each of the following. Nothing here is hand-written or
        illustrative; every panel is literal <code>radix emit</code> output.
        The GPU panels come from an <code>@ nucleum</code> kernel:
      </p>
      <pre class="fl-src">{esc(kernel_fab)}</pre>
      <p class="fl-note">
        LLVM IR is emitted from MIR directly — Faber reaches native code
        without passing through Rust, C, or any other source language.
      </p>
    </div>
{proof2}  </section>

  <section class="fl-proof">
    <div class="fl-proof-head">
      <span class="fl-proof-n">Proof 3</span>
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
        Faber also runs without a build step. <code>faber run --interpret</code>
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
      <a class="fl-door" href="/en-US/tooling/targets.html">
        <strong>Target matrix</strong>
        <span>Measured lowerability, every term × every backend.</span>
      </a>
      <a class="fl-door" href="/en-US/ecosystem/">
        <strong>Ecosystem</strong>
        <span>Norma, Triga, Cista, the language corpus.</span>
      </a>
      <a class="fl-door" href="/en-US/features/">
        <strong>Design</strong>
        <span>Why the language is shaped the way it is.</span>
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
    print(
        f"landing: {args.output} "
        f"({len(locale_panels)} locale panels, {len(target_panels)} target panels)"
    )


if __name__ == "__main__":
    main()
