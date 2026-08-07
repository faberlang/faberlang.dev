#!/usr/bin/env python3
"""
generate-examples.py — build the Examples section from real package source.

Someone who clicks "Examples" wants to read code. The old page opened with
`git clone` and `faber check` — instructions useless to a visitor who has
installed nothing — and then described packages in prose while linking out to
GitHub, which asks a curious reader to go navigate an unfamiliar repository
tree before seeing a single line of Faber.

So: the index gives each project a name and one line about it, and every
project has a page carrying its actual source, highlighted, on this site. The
GitHub link stays as provenance, not as the delivery mechanism.

Source is read from the examples sibling checkout. A missing checkout skips
the section rather than failing the build.

Usage:
    generate-examples.py [--output-dir src/en-US/examples]
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
EXAMPLES = REPO.parent / "examples"
GITHUB = "https://github.com/faberlang/examples/tree/main"

# Ordered so the index reads from "smallest complete thing" to "largest real
# application". Each entry names the files worth reading, not every file in the
# package — a page that dumps a whole tree is the GitHub problem again.
PROJECTS: list[dict] = [
    {
        "slug": "device-summa",
        "title": "device-summa",
        "one_line": "A GPU device package: one compute kernel, run on real Metal or CUDA.",
        "about": "The smallest complete device package. A function marked "
                 "`@ nucleum` is a compute kernel; the manifest's `[device]` "
                 "section is what makes the packaged image carry Metal MSL and "
                 "CUDA PTX artifacts. This is the starter fixture behind the "
                 "`faber run --backend metal|cuda` path.",
        "path": "training/device-summa",
        "files": ["src/device_summa.fab"],
    },
    {
        "slug": "mlp-forward",
        "title": "gpu-workload — MLP forward",
        "one_line": "A neural-network forward pass as a device workload.",
        "about": "One rung of the GPU workload ladder. Tensor shapes are part "
                 "of the types, so the shape of every intermediate is checked "
                 "before anything reaches a device.",
        "path": "gpu-workload",
        "files": ["rung-2-mlp-forward.fab"],
    },
    {
        "slug": "cat",
        "title": "coreutils — cat",
        "one_line": "The Unix `cat` utility, reimplemented in Faber with parity tests.",
        "about": "Part of a campaign reimplementing common utilities with "
                 "parity harnesses. Worth reading for the ordinary shape of a "
                 "CLI package: argument annotations, file I/O through Norma, "
                 "and error handling on the `⇥` channel.",
        "path": "coreutils/packages/cat",
        "files": ["src/main.fab"],
        "package": True,
    },
    {
        "slug": "faber-ai",
        "title": "AI Workbench",
        "one_line": "A multi-command CLI for local model inventory, embeddings, and inference.",
        "about": "A real application with subcommands, JSON output, and a "
                 "Python harness validating its behaviour. The entry point "
                 "shows how a multi-command CLI is wired.",
        "path": "ai-workbench/packages/faber-ai",
        "files": ["src/main.fab"],
    },
    {
        "slug": "arena-handle",
        "title": "arena-handle",
        "one_line": "A generational arena with stable handles, done with pure value updates.",
        "about": "The densest single file here for language features: `genus` "
                 "records, a `discretio` sum type with variant payloads, "
                 "`discerne` matching over it, and a test suite in the same "
                 "file. Stale handles are rejected by a generation check "
                 "rather than by a runtime guard.",
        "path": "arena-handle",
        "files": ["src/main.fab"],
    },
    {
        "slug": "triga-budapest",
        "title": "triga-budapest",
        "one_line": "Geometry construction from the 3D scene rendered on the home page.",
        "about": "Graphics work in the same language, with the same types, as "
                 "everything else here. This is the box-geometry module of the "
                 "scene behind the rendered frames on the home page.",
        "path": "triga-budapest",
        "files": ["src/box_geom.fab"],
        "package": True,
    },
]

# Above this, the page says how long the file is before showing it, so nobody
# is surprised by a very long scroll.
LONG_FILE_LINES = 200


def frontmatter(title: str, order: int) -> list[str]:
    return [
        "+++",
        f'title = "{title}"',
        'section = "examples"',
        f"order = {order}",
        "sources = []",
        "+++",
        "",
    ]


def render_project(p: dict, order: int) -> str | None:
    base = EXAMPLES / p["path"]
    available = [(f, base / f) for f in p["files"] if (base / f).is_file()]
    if not available:
        return None

    lines = frontmatter(p["title"], order)
    lines += [p["about"], "", f"Source: [`examples/{p['path']}`]({GITHUB}/{p['path']})", ""]

    for rel, path in available:
        body = path.read_text(encoding="utf-8").rstrip()
        count = body.count("\n") + 1
        anchor = rel.replace("/", "-").replace(".", "-")
        lines += [f"## `{rel}` {{#{anchor}}}", ""]
        if count > LONG_FILE_LINES:
            lines += [f"{count} lines — the whole file, unabridged.", ""]
        if p.get("package"):
            lines += [
                "One file of a multi-file package: it refers to siblings that "
                "are not shown here.",
                "",
            ]
        # A file belonging to a multi-file package cannot resolve its sibling
        # imports when checked alone. Say so in the fence contract rather than
        # letting the gate fail on something that is correct in place.
        info = "faber mode=package" if p.get("package") else "faber"
        lines += [f"```{info}", body, "```", ""]

    lines += [
        "---",
        "",
        "[All examples](/examples/) · "
        "[Install](/start/install.html) · [Cheat sheet](/cheatsheet/)",
        "",
    ]
    return "\n".join(lines)


def render_index(built: list[dict]) -> str:
    lines = frontmatter("Examples", 5)
    lines += [
        "Real Faber packages, with their source on this site. Not snippets, and "
        "not a list of links asking you to go read someone else's repository.",
        "",
        "| Project | What it is |",
        "|---|---|",
    ]
    for p in built:
        lines.append(f"| [{p['title']}](/examples/{p['slug']}.html) | {p['one_line']} |")

    lines += [
        "",
        "Every package above lives in "
        f"[faberlang/examples]({GITHUB.rsplit('/tree/', 1)[0]}), which holds "
        "more than is shown here — coreutils in full, the whole GPU workload "
        "ladder, reader-locale demos, and the package-store lab.",
        "",
        "## Running them {#running}",
        "",
        "Once you have [installed Faber](/start/install.html):",
        "",
        "```bash",
        "git clone https://github.com/faberlang/examples.git",
        "faber check examples/coreutils/packages/cat",
        "faber run examples/coreutils/packages/cat",
        "```",
        "",
        "Entry commands vary by package; each has its own `README.md`. The "
        "daily command loop is on the [cheat sheet](/cheatsheet/commands.html).",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output-dir", default="src/en-US/examples")
    args = ap.parse_args()

    if not EXAMPLES.is_dir():
        print(f"  warning: no examples checkout at {EXAMPLES}; section skipped",
              file=sys.stderr)
        return 0

    out = REPO / args.output_dir
    out.mkdir(parents=True, exist_ok=True)
    for existing in out.glob("*.md"):
        existing.unlink()

    built: list[dict] = []
    order = 51
    for p in PROJECTS:
        page = render_project(p, order)
        if page is None:
            print(f"  warning: no readable source for {p['slug']}, skipped",
                  file=sys.stderr)
            continue
        (out / f"{p['slug']}.md").write_text(page, encoding="utf-8")
        built.append(p)
        order += 1

    if not built:
        print("ERROR: no example sources found", file=sys.stderr)
        return 1

    (out / "index.md").write_text(render_index(built), encoding="utf-8")
    print(f"examples: {len(built)} project pages → {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
