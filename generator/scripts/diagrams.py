#!/usr/bin/env python3
"""
diagrams.py — ```mermaid fences → committed, theme-aware inline SVG

Two subcommands, one hash function, so the render side and the inject side
can never disagree about what a diagram is called.

    diagrams.py render [src_dir ...]   # fill the SVG cache from Markdown
    diagrams.py inject <dist_dir>      # swap cached SVG into rendered HTML

Why a cache instead of rendering during the build: the SVGs are committed
alongside dist/, so a machine without Node (or without a browser for Mermaid
to draw in) can still produce a complete site. `render` is a source-side
authoring step, run when a diagram is added or changed; `inject` is a
build-side step that only ever reads the cache.

Cache entries live in generator/diagrams/<hash>.svg. The hash covers the
normalized diagram source plus THEME_VERSION, so re-theming invalidates
every entry at once.

Theme independence: Mermaid writes literal hex colours into its SVG. The
renderer feeds it sentinel colours (see render-mermaid.mjs) which are
rewritten here to the site's CSS custom properties. The result follows
light/dark with the rest of the page.

Exit codes
    0  success (inject always; render unless --strict and something failed)
    1  render failure under --strict, or a missing/unusable renderer
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
GENERATOR_DIR = SCRIPT_DIR.parent
REPO_DIR = GENERATOR_DIR.parent
CACHE_DIR = GENERATOR_DIR / "diagrams"
TOOLS_DIR = GENERATOR_DIR / "target" / "diagram-tools"
RENDERER = SCRIPT_DIR / "render-mermaid.mjs"

# Bump to re-render every diagram (palette or renderer option changes).
THEME_VERSION = "1"

# Sentinel hex → site token. Must match the S map in render-mermaid.mjs.
SENTINELS = {
    "#fe0001": "var(--paper)",
    "#fe0002": "var(--paper-alt)",
    "#fe0003": "var(--paper-deep)",
    "#fe0004": "var(--ink)",
    "#fe0005": "var(--ink-dim)",
    "#fe0006": "var(--rule-strong)",
    "#fe0007": "var(--glyph)",
    "#fe0008": "var(--glyph-soft)",
    # Mermaid derives a couple of colours by inverting the background.
    "#01fffe": "var(--ink)",
}

# Mermaid's sequence renderer writes a few colours straight onto the elements
# as presentation attributes; they come from neither the theme nor the sequence
# config, so no themeVariables override can reach them. They are stable
# literals in the Mermaid source, mapped here by the role they play.
MERMAID_DEFAULTS = {
    "#eaeaea": "var(--paper-alt)",   # .actor box fill
    "#666": "var(--rule-strong)",    # .actor / .note stroke
    "#999": "var(--rule)",           # .actor-line lifeline
    "#edf2ae": "var(--glyph-soft)",  # .note fill
}

NPM_DEPS = ["mermaid@11", "playwright@1.61.1"]

MERMAID_FENCE_RE = re.compile(r"^```mermaid[^\n]*\n(.*?)^```", re.S | re.M)
MERMAID_BLOCK_RE = re.compile(
    r'<pre class="faber-code"><code class="lang-mermaid">(.*?)</code></pre>', re.S
)
# An already-injected figure, so `inject` can run twice without doubling up.
FIGURE_RE = re.compile(
    r'<figure class="diagram" data-diagram="([0-9a-f]+)">.*?</figure>', re.S
)


# ── hashing ──────────────────────────────────────────────────────────────────


def normalize(source: str) -> str:
    """Whitespace-insensitive form of a diagram, for stable hashing."""
    lines = [line.rstrip() for line in source.replace("\r\n", "\n").split("\n")]
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines)


def digest(source: str) -> str:
    payload = f"{THEME_VERSION}\n{normalize(source)}".encode("utf-8")
    return hashlib.sha256(payload).hexdigest()[:16]


def cache_path(key: str) -> Path:
    return CACHE_DIR / f"{key}.svg"


# ── SVG rewriting ────────────────────────────────────────────────────────────


def tokenize_svg(svg: str) -> str:
    """Rewrite sentinel and hardcoded colours to CSS custom properties."""
    for literal, token in {**SENTINELS, **MERMAID_DEFAULTS}.items():
        # \b keeps #666 from eating the first half of a six-digit colour.
        svg = re.sub(re.escape(literal) + r"\b", token, svg, flags=re.I)
    return svg


def leftover_colors(svg: str) -> list[str]:
    """Literal colours that survived tokenization (diagnostic only)."""
    found = set()
    for match in re.findall(r"#[0-9a-fA-F]{3,8}\b", svg):
        found.add(match.lower())
    # Pure black shows up only in unused katex/state rules.
    return sorted(c for c in found if c not in ("#000", "#000000"))


VIEWBOX_RE = re.compile(r'viewBox="\s*[-\d.]+\s+[-\d.]+\s+([\d.]+)\s+([\d.]+)\s*"')
SVG_MAXWIDTH_RE = re.compile(r'(<svg\b[^>]*?)\s*style="max-width:[^"]*"')


def strip_inline_sizing(svg: str) -> str:
    """Drop Mermaid's inline max-width so the stylesheet governs display size."""
    return SVG_MAXWIDTH_RE.sub(r"\1", svg, count=1)


def wrap_figure(key: str, svg: str) -> str:
    """Wrap a cached SVG in the figure the stylesheet expects.

    --dw carries the diagram's natural width. The stylesheet uses it to scale
    a diagram down to the column only as far as it stays readable, and to
    scroll rather than shrink past that point: these are 2000px-wide compiler
    pipelines, and fitting one into a 760px column makes 16px labels 5px.
    """
    match = VIEWBOX_RE.search(svg)
    width = f"{float(match.group(1)):.0f}" if match else "0"
    style = f' style="--dw:{width}px"' if match else ""
    return f'<figure class="diagram" data-diagram="{key}"{style}>{svg}</figure>'


# ── render ───────────────────────────────────────────────────────────────────


def collect_sources(src_dirs: list[Path]) -> dict[str, str]:
    """Map hash → diagram source for every ```mermaid fence found."""
    found: dict[str, str] = {}
    for src_dir in src_dirs:
        if not src_dir.is_dir():
            continue
        for md in sorted(src_dir.rglob("*.md")):
            text = md.read_text(encoding="utf-8")
            for match in MERMAID_FENCE_RE.finditer(text):
                source = normalize(match.group(1))
                if source:
                    found[digest(source)] = source
    return found


def ensure_tools() -> str | None:
    """Install the Node renderer's dependencies on demand.

    Returns None when ready, or a human-readable reason it is not.
    """
    if shutil.which("npm") is None or shutil.which("node") is None:
        return "node and npm are required to render diagrams"

    marker = TOOLS_DIR / "node_modules" / "mermaid" / "package.json"
    if not marker.exists():
        TOOLS_DIR.mkdir(parents=True, exist_ok=True)
        if not (TOOLS_DIR / "package.json").exists():
            (TOOLS_DIR / "package.json").write_text(
                json.dumps({"name": "speculum-diagram-tools", "private": True}) + "\n",
                encoding="utf-8",
            )
        print(f"  installing diagram renderer into {TOOLS_DIR}...")
        result = subprocess.run(
            ["npm", "install", "--no-audit", "--no-fund", "--silent", *NPM_DEPS],
            cwd=TOOLS_DIR,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            return f"npm install failed: {result.stderr.strip()[:400]}"

    # Mermaid needs a browser to measure and lay out text. Launching is the
    # only honest probe: executablePath() names the full Chromium build even
    # when only the headless shell is installed.
    probe = subprocess.run(
        [
            "node",
            "-e",
            "require('playwright').chromium.launch()"
            ".then(b=>b.close()).then(()=>process.exit(0),()=>process.exit(1))",
        ],
        cwd=TOOLS_DIR,
        capture_output=True,
        text=True,
    )
    if probe.returncode != 0:
        print("  installing headless browser for Mermaid layout...")
        install = subprocess.run(
            ["npx", "--yes", "playwright", "install", "chromium", "--only-shell"],
            cwd=TOOLS_DIR,
            capture_output=True,
            text=True,
        )
        if install.returncode != 0:
            return f"playwright browser install failed: {install.stderr.strip()[:400]}"
    return None


def run_renderer(jobs: list[dict]) -> list[dict]:
    env = dict(os.environ, SPECULUM_DIAGRAM_TOOLS=str(TOOLS_DIR))
    result = subprocess.run(
        ["node", str(RENDERER)],
        cwd=TOOLS_DIR,
        env=env,
        input=json.dumps(jobs),
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip()[:800] or "renderer exited non-zero")
    return json.loads(result.stdout)


def cmd_render(args) -> int:
    src_dirs = [Path(d) for d in args.src] if args.src else [REPO_DIR / "src"]
    sources = collect_sources(src_dirs)
    if not sources:
        print("  no mermaid fences found")
        return 0

    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    missing = {k: v for k, v in sources.items() if not cache_path(k).exists()}
    if args.force:
        missing = sources

    print(f"  {len(sources)} diagram(s), {len(missing)} to render")
    if not missing:
        return 0

    reason = ensure_tools()
    if reason:
        print(f"  WARNING: {reason}", file=sys.stderr)
        print("  WARNING: diagrams stay as code blocks until this is fixed", file=sys.stderr)
        return 1 if args.strict else 0

    jobs = [{"id": f"d-{key}", "source": source} for key, source in sorted(missing.items())]
    try:
        results = run_renderer(jobs)
    except (RuntimeError, json.JSONDecodeError) as exc:
        print(f"  ERROR: renderer failed: {exc}", file=sys.stderr)
        return 1 if args.strict else 0

    failures = 0
    for item in results:
        key = item["id"].removeprefix("d-")
        if "error" in item:
            failures += 1
            print(f"  ✗ {key}: {item['error']}", file=sys.stderr)
            continue
        svg = strip_inline_sizing(tokenize_svg(item["svg"]))
        stray = leftover_colors(svg)
        if stray:
            print(f"  ! {key}: literal colours survived: {' '.join(stray)}", file=sys.stderr)
        cache_path(key).write_text(svg + "\n", encoding="utf-8")
        print(f"  ✓ {key}.svg")

    if failures and args.strict:
        return 1
    return 0


# ── inject ───────────────────────────────────────────────────────────────────


def cmd_inject(args) -> int:
    dist = Path(args.dist)
    if not dist.is_dir():
        print(f"ERROR: not a directory: {dist}", file=sys.stderr)
        return 1

    cache: dict[str, str] = {}
    for svg_file in CACHE_DIR.glob("*.svg") if CACHE_DIR.is_dir() else []:
        cache[svg_file.stem] = svg_file.read_text(encoding="utf-8").strip()

    injected = 0
    skipped = 0
    touched = 0

    for page in sorted(dist.rglob("*.html")):
        text = page.read_text(encoding="utf-8")
        if "lang-mermaid" not in text and 'class="diagram"' not in text:
            continue

        stats = {"injected": 0, "skipped": 0}

        def replace(match: re.Match) -> str:
            source = normalize(html.unescape(match.group(1)))
            key = digest(source)
            svg = cache.get(key)
            if svg is None:
                stats["skipped"] += 1
                return match.group(0)
            stats["injected"] += 1
            return wrap_figure(key, svg)

        def refresh(match: re.Match) -> str:
            """Re-inline an already-injected figure from the current cache."""
            key = match.group(1)
            svg = cache.get(key)
            return wrap_figure(key, svg) if svg else match.group(0)

        # Refresh first so a re-run picks up re-rendered SVGs, then convert
        # any code blocks that have not been converted yet.
        updated = FIGURE_RE.sub(refresh, text)
        updated = MERMAID_BLOCK_RE.sub(replace, updated)
        if updated != text:
            page.write_text(updated, encoding="utf-8")
            touched += 1
        injected += stats["injected"]
        skipped += stats["skipped"]

    print(f"  diagrams: {injected} inlined across {touched} page(s)")
    if skipped:
        print(
            f"  WARNING: {skipped} diagram(s) have no cached SVG — "
            f"run diagrams.py render",
            file=sys.stderr,
        )
        if args.strict:
            return 1
    return 0


# ── entry ────────────────────────────────────────────────────────────────────


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    render = sub.add_parser("render", help="render missing diagrams into the cache")
    render.add_argument("src", nargs="*", help="source dirs to scan (default: src/)")
    render.add_argument("--force", action="store_true", help="re-render everything")
    render.add_argument("--strict", action="store_true", help="fail on render errors")
    render.set_defaults(func=cmd_render)

    inject = sub.add_parser("inject", help="inline cached diagrams into built HTML")
    inject.add_argument("dist", help="dist directory")
    inject.add_argument("--strict", action="store_true", help="fail on cache misses")
    inject.set_defaults(func=cmd_inject)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
