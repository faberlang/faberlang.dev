#!/usr/bin/env python3
"""
generate-landing.py — Generate the Faber landing page at /.

Narrative order, deliberately plain:

    1. the user outcome: one semantic program, readable in your language
    2. the honest capability ladder: shipped, proven now, building next, frontier
    3. the product loop: application targets or real GPU work
    4. the supporting GPU and graphics proofs
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

# Reader-pack axis. Order is the argument: the English reader surface, then
# canonical Faber, then the human packs.
LOCALES: list[dict[str, str]] = [
    {"id": "en", "name": "English", "code": "en", "script": "",
     "note": "English reader surface — the base spelling for everyday source"},
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

# The target axis splits in two. Ordinary lowering comes from the demo program;
# the GPU shading languages need an `@ nucleum` kernel, which is a different
# source file. Mixing them in one tab strip made the kernel look like a variant
# of the same program when it is not.
TARGETS: list[dict[str, str]] = [
    {"id": "rust", "name": "Rust",
     "note": "primary backend — reviewable source, then a native binary"},
    {"id": "go", "name": "Go", "note": "file emission"},
    {"id": "ts", "name": "TypeScript", "note": "file emission",
     "elide_before": "        const flat_a"},
    {"id": "llvm-text", "name": "LLVM IR",
     "note": "native code with no source language in between"},
]

GPU_TARGETS: list[dict[str, str]] = [
    {"id": "wgsl-text", "name": "WGSL", "kernel": "1",
     "note": "WebGPU compute shader"},
    {"id": "metal-text", "name": "Metal", "kernel": "1",
     "note": "Apple GPU compute shader"},
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
            f'title="{p["hint"]}" '
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
            "tab": name, "hint": esc(loc["code"]),
            "label": f'<code>faber format --locale {esc(loc["code"])}</code> '
                     f'<span class="fdt-note">— {esc(loc["note"])}</span>',
            "code": esc(f.read_text(encoding="utf-8").strip()),
            "dir": (f' class="{loc["script"]}"' if loc["script"] else "")
                   + (' dir="rtl"' if loc.get("rtl") else ""),
        })
    return panels


def build_target_panels(d: Path, targets: list[dict[str, str]]) -> list[dict[str, str]]:
    panels = []
    for t in targets:
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
            "tab": esc(t["name"]), "hint": esc(t["id"]),
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
    target_panels = build_target_panels(args.landing, TARGETS)
    gpu_panels = build_target_panels(args.landing, GPU_TARGETS)

    kernel_fab = (args.landing / "targets" / "kernel.fab").read_text(encoding="utf-8").strip()

    read_tabs = demo_tabs(
        root_id="fl-loc", file_label="main.fab · reader locale",
        tablist_label="Reader locale", panels=locale_panels)
    target_tabs = demo_tabs(
        root_id="fl-tgt", file_label="main.fab → target",
        tablist_label="Compilation target", panels=target_panels)
    gpu_tabs = demo_tabs(
        root_id="fl-gpu", file_label="kernel.fab → GPU",
        tablist_label="GPU shading language", panels=gpu_panels)

    frames = "".join(
        f"""\
        <figure class="fl-frame">
          <img src="{f['src']}" alt="{esc(f['alt'])}" loading="lazy" width="1400" height="788">
          <figcaption>{f['cap']}</figcaption>
        </figure>
""" for f in FRAMES)

    desc = ("Faber is a multilingual developer tool for typed compute programs. "
            "One semantic program stays readable in your language and lowers "
            "toward application targets and a measured Metal/CUDA training path.")

    html = f"""\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Faber — multilingual compute programs for applications and GPUs</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="https://faberlang.dev/">
<link rel="alternate" hreflang="x-default" href="https://faberlang.dev/">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;600;700&amp;family=Noto+Serif:wght@400;600&amp;family=Noto+Sans+Mono:wght@400;600&amp;family=Noto+Sans+Arabic:wght@400;600;700&amp;family=Noto+Sans+Devanagari:wght@400;600&amp;family=Noto+Sans+SC:wght@400;600&amp;family=Noto+Sans+Thai:wght@400;600&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="{esc(args.css)}">
<meta property="og:title" content="Faber — multilingual compute programs for applications and GPUs">
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
    <a href="/en-US/language/">Language</a>
    <a href="https://github.com/faberlang">GitHub</a>
    <a class="fl-locale" href="/porta/">Language <span aria-hidden="true">▾</span></a>
  </nav>
</header>

<main class="fl-wrap" id="top">

  <section class="fl-hero">
    <p class="fl-kicker">Multilingual semantic programming for application code and GPU work · MIT</p>
    <h1>Write compute programs<br>in the language you think in.</h1>
    <p class="fl-lede">
      Faber keeps one semantic program readable across human-language surfaces,
      then lowers it toward application targets and a measured GPU path. Use
      the same typed source for package work, training proofs, and device
      kernels — with support stated target by target.
    </p>
    <p class="fl-thesis">
      Faber is mechanical, token-oriented, and <strong>LLM-first</strong> by
      design. <strong>Glyphs</strong> provide the stable structural frame;
      <strong>keywords</strong> provide the flexible, human-facing rendering.
      English keywords are selected for high-probability LLM generation,
      reducing transcription and coding errors when people and models write
      Faber together. <strong>HIR</strong> is the semantic core: every target
      language is a projection of the meaning held there. <strong>MIR</strong> is
      the systems lane, where that meaning takes execution-shaped form for
      low-level targets, validation surfaces, and package runtimes.
      <strong>GPU</strong> is the device lane, linking the compiler to real Metal
      and CUDA execution: bounded training is proven now, and inference is
      being built next.
    </p>

    <div class="fl-cta">
      <a class="fl-btn fl-btn-primary" href="/en-US/start/install.html">Install Faber</a>
      <a class="fl-btn" href="/en-US/start/examples.html#applications">Run the GPU proof</a>
    </div>
  </section>

  <section class="fl-lanes">
    <h2>Compiler lanes</h2>
    <table>
      <thead><tr><th>Lane</th><th>Targets / outputs</th></tr></thead>
      <tbody>
        <tr><td><strong>Locale</strong></td><td>en (default) · la · th-TH · zh-Hans · zh-Hant · ar · vi · hi</td></tr>
        <tr><td><strong>HIR</strong></td><td>Rust · TypeScript · Go</td></tr>
        <tr><td><strong>AIR (autograd)</strong></td><td>Typed HIR → reverse-mode AD / fusion → MIR</td></tr>
        <tr><td><strong>MIR</strong></td><td>LLVM · WASM · WGSL · S-expression</td></tr>
        <tr><td><strong>GPU</strong></td><td>Metal · CUDA</td></tr>
        <tr><td><strong>Packaging</strong></td><td>FLIB · FHIR · FMIR</td></tr>
      </tbody>
    </table>
  </section>

  <section class="fl-doors">
    <h2>One tool, four honest states</h2>
    <div class="fl-door-grid">
      <a class="fl-door" href="/en-US/language/reader-locales.html">
        <strong>Shipped · reader locales</strong>
        <span>Localized source, diagnostics, and formatting preserve one program’s meaning.</span>
      </a>
      <a class="fl-door" href="/en-US/toolchain/cli.html#device-execution">
        <strong>Proven now · Metal + CUDA training</strong>
        <span>A bounded device-program path runs an accepted training proof on both backends.</span>
      </a>
      <a class="fl-door" href="/en-US/toolchain/compiling.html#device-execution">
        <strong>Building next · GPU inference</strong>
        <span>Faber-owned inference is being built behind a pinned model contract and correctness oracle.</span>
      </a>
      <a class="fl-door" href="/en-US/toolchain/compiling.html#gpu">
        <strong>Frontier · multi-device execution</strong>
        <span>Virtual GPUs, sharding, and distributed execution are future direction, not current runtime claims.</span>
      </a>
    </div>
  </section>

  <section class="fl-proof">
    <div class="fl-proof-head">
      <h2>Readable in your language. Same meaning.</h2>
      <p>
        Faber’s reader locales change keywords, types, and diagnostics without
        changing program meaning. This example constructs two typed matrices,
        multiplies them, and reduces the product to a scalar. Pick a tab and
        that same compute program remains the same program. Identifiers and
        string literals stay intact, so teams can review durable code across
        language surfaces without a translation service in the middle.
      </p>
    </div>
{read_tabs}    <pre class="fl-run">$ faber run --interpret &lt;package&gt;
76.25</pre>
    <p class="fl-note">
      A reviewer sets their locale once. This is the compiler’s own rendering,
      so the program you approve is the program that ships.
    </p>
  </section>

  <section class="fl-proof">
    <div class="fl-proof-head">
      <h2>One semantic program for applications and GPU work</h2>
      <p>
        The same analyzed program can feed application targets or a device
        program. Rust is the primary executable path; TypeScript, Go, LLVM, and
        other targets have narrower, measured support. The target matrix is the
        source of truth, not a promise that every backend behaves the same way.
      </p>
      <p class="fl-note">
        Every panel below is literal <code>radix emit</code> output. The matrix
        records where a target emits, validates, runs, or remains limited. See
        <a href="/en-US/toolchain/target-matrix.html">target matrix</a>
        for the current boundary.
      </p>
    </div>
{target_tabs}  </section>

  <section class="fl-proof">
    <div class="fl-proof-head">
      <h2>Training through Metal or CUDA</h2>
      <p>
        The ordinary <code>faber run --backend metal|cuda</code> route executes
        a bounded device-program subset on accepted Metal and CUDA machines.
        The current accepted proof covers a dual-backend MLP training path with
        device-resident state, gradient mapping, and numeric comparison.
      </p>
      <pre class="fl-run">$ faber run --backend metal &lt;package&gt;
$ faber run --backend cuda  &lt;package&gt;</pre>
      <p>
        This is a bounded training proof, not a claim of a general training
        framework, broad hardware coverage, or a released package surface.
        Device execution is explicit and fail-closed: a requested backend does
        not silently fall back to CPU.
      </p>
      <p class="fl-note">
        <a href="/en-US/toolchain/cli.html#device-execution">Read the device
        execution contract</a> ·
        <a href="https://github.com/faberlang/examples/tree/main/training/device-summa">Open the training proof</a>
      </p>
    </div>
    <div class="fl-proof-head fl-proof-sub">
      <h3>One kernel, backend-specific output</h3>
      <p>
        A function marked <code>@ nucleum</code> is a compute kernel. The source
        stays small while Faber emits backend-specific shader code. These panels
        show the lowering surface; the real-device route above is the narrower
        product proof.
      </p>
      <pre class="fl-src">{esc(kernel_fab)}</pre>
    </div>
{gpu_tabs}  </section>

  <section class="fl-proof">
    <div class="fl-proof-head">
      <h2>Inference is being built next</h2>
      <p>
        Faber-owned GPU inference is in active development behind a pinned model
        contract and a correctness oracle. It is not a shipped inference server
        or a broad GGUF support claim yet. The homepage keeps this visible
        without turning an engineering track into a false availability promise.
      </p>
      <p class="fl-note">
        Follow the <a href="/en-US/start/examples.html#applications">AI and GPU examples</a>
        while the persistent inference path is built.
      </p>
    </div>
    <div class="fl-door-grid">
      <a class="fl-door" href="/en-US/toolchain/compiling.html#device-execution">
        <strong>Now · device substrate</strong>
        <span>Kernel lowering, explicit backend selection, and bounded training execution.</span>
      </a>
      <a class="fl-door" href="/en-US/toolchain/target-matrix.html">
        <strong>Next · persistent inference</strong>
        <span>One pinned model contract first; broader serving remains outside today’s claim.</span>
      </a>
      <a class="fl-door" href="/en-US/toolchain/compiling.html#gpu">
        <strong>Future · multi-device scale</strong>
        <span>Topology, placement, collectives, virtual GPUs, and sharding need their own accepted runtime path.</span>
      </a>
    </div>
  </section>

  <section class="fl-proof">
    <div class="fl-proof-head">
      <h2>Build the rest of the application around it</h2>
      <p>
        <a href="/en-US/libraries/triga.html">Triga</a> is a graphics and
        geometry engine written in Faber. These frames are supporting evidence
        that the same language can carry application and GPU-shaped work — not
        a replacement for the training and inference path above.
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
      <a class="fl-door" href="/en-US/language/">
        <strong>Language</strong>
        <span>Types, control flow, generics, glyphs, errors.</span>
      </a>
      <a class="fl-door" href="/en-US/language/reader-locales.html">
        <strong>Reader locales</strong>
        <span>How the rendering actually works.</span>
      </a>
      <a class="fl-door" href="/en-US/toolchain/target-matrix.html">
        <strong>Target matrix</strong>
        <span>Measured lowerability, every term × every backend.</span>
      </a>
      <a class="fl-door" href="/en-US/libraries/">
        <strong>Libraries</strong>
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
    compiler <a href="/en-US/toolchain/radix.html">Radix</a>
  </div>
  <div>
    <a href="/porta/">All languages</a> ·
    <a href="/en-US/reference/releases.html">Releases</a> ·
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
          f"({len(locale_panels)} reader panels, {len(target_panels)} target panels)")


if __name__ == "__main__":
    main()
