#!/usr/bin/env python3
"""
inject-pass.py — place the agent pass on a docs page.

The Markdown pipeline cannot express the pass (a paper card with a link, three
fact rows and two copy buttons), so a page asks for it with one marker:

    ::agent-pass::

on a line of its own. The renderer wraps that in a paragraph, and this pass
swaps ``<p>::agent-pass::</p>`` for the pass markup from ``agent_pass.py`` — the
same component the landing page renders, with the visible strings read from the
page locale's ``chrome.toml`` ``[pass]`` table. The Start page carries the
marker in every locale.

Behaviour:
  - A page without the marker is not touched.
  - A page with the marker but no pass (missing locale strings, unreadable
    release facts) fails the run: a half-built Start page must not ship.
  - Idempotent: once swapped, the marker is gone and a second run finds nothing.

Run it after ``inject-toc.py``: the pass carries two ``h2`` elements that are
card labels, not sections of the page, and must not reach the contents rail.

Usage:
    inject-pass.py <dist_dir>

Requires Python 3.11+ (uses tomllib).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from agent_pass import load_pass_strings, read_release, render_pass  # noqa: E402
from locales_registry import load_registry, locale_dir_names  # noqa: E402

MARKER = "<p>::agent-pass::</p>"
RAW_MARKER = "::agent-pass::"


def main() -> int:
    dist = Path(sys.argv[1] if len(sys.argv) > 1 else "dist")
    if not dist.is_dir():
        print(f"ERROR: {dist} is not a directory", file=sys.stderr)
        return 2

    locales = sorted(locale_dir_names(load_registry()))
    release = None
    placed = 0
    failed: list[str] = []

    for locale in locales:
        root = dist / locale
        if not root.is_dir():
            continue
        strings = None
        for page in sorted(root.rglob("*.html")):
            html = page.read_text(encoding="utf-8")
            if RAW_MARKER not in html:
                continue
            if MARKER not in html:
                failed.append(f"{page}: marker is not a paragraph of its own")
                continue
            if strings is None:
                strings = load_pass_strings(locale)
            if release is None:
                release = read_release()
            page.write_text(html.replace(MARKER, render_pass(strings, release), 1),
                            encoding="utf-8")
            placed += 1

    for line in failed:
        print(f"ERROR: {line}", file=sys.stderr)
    print(f"Agent pass: placed on {placed} pages")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
