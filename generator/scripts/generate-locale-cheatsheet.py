#!/usr/bin/env python3
"""
generate-locale-cheatsheet.py — build the reader-locale cheat sheet page.

The page shows one program rendered in every reader locale. Those renderings
are compiler output, captured by capture-landing-panels.sh into
generator/landing/locales/*.fab — the same panels the landing page uses. This
script assembles them into a Markdown page rather than anyone retyping Thai or
Arabic source by hand, which would drift from the compiler the moment a reader
pack changed.

Usage:
    generate-locale-cheatsheet.py [--output src/en-US/cheatsheet/locales.md]
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
PANELS = REPO / "generator" / "landing" / "locales"

# Order: the English surface first because it is the base spelling most readers
# arrive with, then canonical Latin, then the human packs.
LOCALES = [
    ("en", "English", "The English reader surface — the base spelling for everyday source."),
    ("la", "Latin", "Canonical Faber, the classical surface the language is named for."),
    ("th-TH", "ภาษาไทย — Thai", "A spaceless script; the compiler tokenizes it the same way."),
    ("zh-Hans", "简体中文 — Simplified Chinese", "Keywords and type names remap; identifiers do not."),
    ("zh-Hant", "繁體中文 — Traditional Chinese", "A separate pack from Simplified — `常量` against `定值`."),
    ("vi", "Tiếng Việt — Vietnamese", "Multi-word keywords join with underscores: `bắt_đầu`."),
    ("ar", "العربية — Arabic", "Right-to-left, bidi isolated. Identifiers stay left-to-right."),
    ("hi", "हिन्दी — Hindi", "Devanagari keywords over unchanged identifiers and literals."),
]

HEAD = '''+++
title = "Reader locales"
section = "cheatsheet"
order = 41
sources = []
+++

The same program, rendered in eight human languages. Not a translation of a
document — the compiler renders source into a reader locale, so what you see
below is the same analyzed program every time.

Keywords and primitive type names remap. **Identifiers and string literals do
not.** `flat_a` stays `flat_a` in Arabic; `media()` stays `media()` in Thai.
That is what makes a review across locales possible: the nouns of your program
are stable, only the grammar words move.

Every panel on this page is compiler output, captured from the toolchain rather
than written by hand.

## The program {#program}

It builds two typed matrices, multiplies them, and reduces the product to a
scalar mean.

'''

TAIL = '''## Switching locale {#switching}

Render existing source into another locale with `faber format`:

```bash
faber format --reader-locale th-TH <package>
```

The reader locale is a rendering choice, not a fork. Two people can hold the
same package open in different locales and be editing one program.

## What this is not {#not}

- Not a translation layer over the page. The compiler produces these.
- Not string localization. Your `"messages"` are untouched.
- Not a dialect. There is one grammar; only its surface spelling changes.

Related: [Reader locales](/language/reader-locales.html) for the full
mechanism · [Glyphs and Latin](/language/glyphs.html) for why the glyphs stay
constant across every pack
'''


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", default="src/en-US/cheatsheet/locales.md")
    args = ap.parse_args()

    parts = [HEAD]
    written = 0
    for code, label, note in LOCALES:
        panel = PANELS / f"{code}.fab"
        if not panel.is_file():
            print(f"  warning: missing panel {panel}", file=sys.stderr)
            continue
        body = panel.read_text(encoding="utf-8").strip()
        anchor = code.lower()
        parts.append(f"### {label} {{#{anchor}}}\n\n{note}\n\n")
        # The fence names its own locale so the highlighter paints each pack in
        # its own spellings; the page itself is English.
        parts.append(f"```faber locale={code}\n{body}\n```\n\n")
        written += 1

    if not written:
        print("ERROR: no locale panels found", file=sys.stderr)
        return 1

    parts.append(TAIL)
    out = REPO / args.output
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("".join(parts), encoding="utf-8")
    print(f"locale cheat sheet: {written} panels → {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
