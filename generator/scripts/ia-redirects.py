#!/usr/bin/env python3
"""
ia-redirects.py — the old→new URL map for the 2026-08 IA restructure.

Two jobs, selected by subcommand:

    rewrite   rewrite internal links across src/<locale>/**/*.md
    stubs     write meta-refresh stubs at the retired paths in dist/

The map is ordered longest-prefix-first so that a retired leaf is never
swallowed by its retired section.
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent

# Ordered: specific pages before their section prefixes.
MAP: list[tuple[str, str]] = [
    # reference/repositories → open-source (the readable front door; the
    # repository tables, host platform list, and issue routing all folded in)
    ("/reference/repositories.html", "/open-source.html"),
    # reference/releases → its own section: an index of every Faber and Radix
    # version, each with pinned install instructions and full release notes
    ("/reference/releases.html", "/releases/"),
    # start/commands → the cheat sheet's Commands page (it was always a cheat
    # sheet, sitting in the middle of a sequenced tutorial track)
    ("/start/commands.html", "/cheatsheet/commands.html"),
    # start/examples → the Examples section, which carries real package
    # source on the site instead of describing it and linking to GitHub
    ("/start/examples.html", "/examples/"),
    # syntax/* → language/*
    ("/syntax/types.html", "/language/types.html"),
    ("/syntax/variables.html", "/language/types.html"),
    ("/syntax/collections.html", "/language/types.html"),
    ("/syntax/strings.html", "/language/types.html"),
    ("/syntax/nullability.html", "/language/types.html"),
    ("/syntax/conversion.html", "/language/types.html"),
    ("/syntax/functions.html", "/language/functions.html"),
    ("/syntax/control-flow.html", "/language/functions.html"),
    ("/syntax/generics.html", "/language/functions.html"),
    ("/syntax/errors.html", "/language/errors.html"),
    ("/syntax/glyphs.html", "/language/glyphs.html"),
    ("/syntax/", "/language/"),
    # features/* → language/*, toolchain/*, reference/*
    ("/features/testing.html", "/language/errors.html"),
    ("/features/latin-and-glyphs.html", "/language/glyphs.html"),
    ("/features/canonical-vs-sugar.html", "/language/glyphs.html"),
    ("/features/reader-locale.html", "/language/reader-locales.html"),
    ("/features/frames.html", "/language/capabilities.html"),
    ("/features/compilation-lanes.html", "/toolchain/compiling.html"),
    ("/features/commandments.html", "/reference/design.html"),
    ("/features/", "/language/"),
    # tooling/* → toolchain/*
    ("/tooling/faber-build-tool.html", "/toolchain/cli.html"),
    ("/tooling/scripting.html", "/toolchain/cli.html"),
    ("/tooling/codegen-targets.html", "/toolchain/compiling.html"),
    ("/tooling/performance.html", "/toolchain/compiling.html"),
    ("/tooling/targets.html", "/toolchain/target-matrix.html"),
    ("/tooling/cista-package-manager.html", "/toolchain/packages.html"),
    ("/tooling/radix-compiler.html", "/toolchain/radix.html"),
    ("/tooling/radix-architecture.html", "/toolchain/radix.html"),
    ("/tooling/", "/toolchain/"),
    # ecosystem/* → libraries/*, start/*, language/*
    ("/ecosystem/norma.html", "/libraries/norma.html"),
    ("/ecosystem/triga.html", "/libraries/triga.html"),
    ("/ecosystem/corpus.html", "/libraries/corpus.html"),
    ("/ecosystem/reader-locale-packages.html", "/language/reader-locales.html"),
    ("/ecosystem/ai-workbench.html", "/examples/"),
    ("/ecosystem/coreutils.html", "/examples/"),
    ("/ecosystem/", "/libraries/"),
    # references/* → reference/*
    ("/references/ebnf.html", "/reference/grammar.html"),
    ("/references/design-docs.html", "/reference/design.html"),
    ("/references/repositories.html", "/open-source.html"),
    ("/references/", "/reference/"),
    # history/* → reference/*
    ("/history/releases.html", "/releases/"),
    ("/history/", "/reference/design.html"),
]

STUB = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="refresh" content="0; url={target}">
<link rel="canonical" href="https://faberlang.dev{target}">
<meta name="robots" content="noindex">
<title>Moved</title>
</head>
<body><p>This page moved to <a href="{target}">{target}</a>.</p></body>
</html>
"""


def rewrite() -> None:
    src = REPO / "src"
    changed = 0
    for md in src.rglob("*.md"):
        text = original = md.read_text(encoding="utf-8")
        for old, new in MAP:
            text = text.replace(f"]({old}", f"]({new}")
            text = text.replace(f'href="{old}', f'href="{new}')
        if text != original:
            md.write_text(text, encoding="utf-8")
            changed += 1
    print(f"rewrite: {changed} markdown files updated")


def stubs() -> None:
    dist = REPO / "dist"
    locales = [d.name for d in (REPO / "src").iterdir() if d.is_dir()]
    written = 0
    fellback = 0
    for old, new in MAP:
        for loc in locales:
            target = f"/{loc}{new}"
            # A locale that has not translated the destination yet would get a
            # stub pointing into a 404. The link gate cannot see this — it does
            # not follow meta-refresh targets — so check here and fall back to
            # the English page, which always exists.
            dest = dist / loc / new.lstrip("/")
            if new.endswith("/"):
                dest = dest / "index.html"
            if not dest.exists():
                target = f"/en-US{new}"
                fellback += 1
            path = (dist / loc / old.lstrip("/") /
                    "index.html") if old.endswith("/") else (
                    dist / loc / old.lstrip("/"))
            if path.exists():
                continue  # a live page already occupies this URL
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(STUB.format(target=target), encoding="utf-8")
            written += 1
    print(f"stubs: {written} redirect pages written "
          f"({fellback} fell back to en-US for an untranslated target)")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "rewrite":
        rewrite()
    elif cmd == "stubs":
        stubs()
    else:
        print(__doc__)
        sys.exit(1)
