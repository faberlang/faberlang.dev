#!/usr/bin/env python3
"""
check-width-gate.py — fail the build when a layout child sets its own width.

The site decides width in exactly two places: the docs grid track, and the
landing page's `content`/`wide` column tracks (--measure). Any other element
that sets `max-width` re-introduces the ragged-column problem, where prose,
tables, and cards each stop at a different arbitrary point inside the same
container.

This gate exists because that happened five separate ways on the landing page
before 2026-08-02, and because it is the kind of thing that gets reintroduced
by every new page unless a machine objects.

Allowed:
  * containers that define a track  (.fl-wrap, .page, .porta-wrap …)
  * `max-width: 100%` / `none`     (media containment, never a cap)
  * `max-width: var(--…)`          (a shared token, not an ad-hoc number)
  * viewport units (vw/vh)         (a viewport constraint, not a container cap)
  * table cells (th/td)            (column sizing, not page layout)
  * @media query preludes

Anything else with a hard value on a block-level child is a finding.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

CSS = Path(__file__).resolve().parent.parent / "www" / "speculum.css"

# Selectors permitted to establish a width, because they *are* the container.
CONTAINERS = {
    ".fl-wrap", ".fl-top", ".fl-foot", ".page", "body.has-toc .page",
    ".porta-wrap", ".porta-note", ".porta-question", ".porta-node",
    ".renderbar-inner", ".search-panel", ".toc",
}

RULE = re.compile(r"([^{}]+)\{([^{}]*)\}", re.S)
MAXW = re.compile(r"max-width\s*:\s*([^;]+)", re.I)


def main() -> int:
    raw = CSS.read_text(encoding="utf-8")
    # Blank comments out rather than deleting them, so reported line numbers
    # still match the real file.
    css = re.sub(r"/\*.*?\*/", lambda m: re.sub(r"[^\n]", " ", m.group(0)), raw, flags=re.S)
    findings: list[str] = []

    for m in RULE.finditer(css):
        selector = " ".join(m.group(1).split())
        body = m.group(2)
        if selector.startswith("@"):
            continue
        for decl in MAXW.finditer(body):
            value = decl.group(1).strip()
            if value in ("100%", "none") or value.startswith("var("):
                continue
            if re.search(r"\d\s*(vw|vh|dvw|dvh)\b", value):
                continue
            sels = [s.strip() for s in selector.split(",")]
            if any(s in CONTAINERS for s in sels):
                continue
            # Table cells size columns; that is not page layout.
            if all(re.search(r"\b(th|td)\b[^ ]*$", s) for s in sels):
                continue
            line = css[: m.start(2) + decl.start()].count("\n") + 1
            findings.append(f"  speculum.css:{line}  {selector} → max-width: {value}")

    if findings:
        print("ERROR: layout children must not set their own max-width.", file=sys.stderr)
        print("Use the content/wide column tracks (see §15) or --measure.\n",
              file=sys.stderr)
        print("\n".join(findings), file=sys.stderr)
        return 1

    print("  [gate] width gate: no ad-hoc max-width on layout children")
    return 0


if __name__ == "__main__":
    sys.exit(main())
