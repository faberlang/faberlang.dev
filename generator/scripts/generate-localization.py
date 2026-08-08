#!/usr/bin/env python3
"""
generate-localization.py — build the Localization overview page.

Reader locales are the language's most distinctive property, and they were
buried inside the cheat sheet. This is their own page, and it answers the
question the old page never did: *why these languages?*

The answer is not "the biggest ones." Each pack was chosen because it forces
the compiler to confront a Unicode or emission problem none of the others do —
a set picked for collective architectural coverage, which turns "pick
languages" into "derive architecture." That rationale lives in
`radix/docs/design/reader-locale.md`; the summaries below are carried here so
the site states its own reasoning instead of gesturing at a private tree.

Code panels are compiler output captured by capture-landing-panels.sh, the
same source the landing hero uses. Nobody hand-writes Thai or Arabic Faber.

Usage:
    generate-localization.py [--output src/en-US/localization.md]
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
PANELS = REPO / "generator" / "landing" / "locales"

# Order follows the landing hero: the English surface most readers arrive with,
# canonical Latin, then the human packs in the order they were built.
LOCALES: list[dict[str, str]] = [
    {
        "id": "en",
        "title": "English",
        "role": "Base surface",
        "why": "The spelling most people write day to day, and the one English-"
               "trained models emit most reliably. It is a reader pack like any "
               "other — not a privileged default — but it is where most source "
               "starts.",
        "stress": "None unique. It is the baseline the others are measured "
                  "against.",
    },
    {
        "id": "la",
        "title": "Latin",
        "role": "Canonical surface",
        "why": "Latin is the interchange dialect because it is **neutral "
               "relative to every modern national language**. No living "
               "population has a claim on it, so no reader pack has to be the "
               "one that everyone else is a translation of.",
        "stress": "None unique — by design. It is the complete template every "
                  "translated pack is built from.",
    },
    {
        "id": "th-TH",
        "title": "ภาษาไทย — Thai",
        "role": "The tokenizer stress test",
        "why": "The original access-wedge choice: a large developer population "
               "with low English proficiency and no existing "
               "native-programming-language tradition. It tests the access "
               "thesis directly rather than theoretically.",
        "stress": "**Spaceless script.** Thai has no inter-word boundaries, so "
                  "a tokenizer that quietly assumed whitespace separates words "
                  "breaks immediately. Combining vowel and tone marks stack on "
                  "base characters, so a keyword is not a run of independent "
                  "code points.",
    },
    {
        "id": "zh-Hans",
        "title": "简体中文 — Simplified Chinese",
        "role": "Width, pairing, and emission fidelity",
        "why": "Optimizes for reach while surfacing the deepest set of script "
               "problems beyond tokenization.",
        "stress": "**Full-width and half-width punctuation** collapse under "
                  "NFKC normalization, so the compiler cannot treat visually "
                  "distinct characters as distinct tokens. **Paired keywords** "
                  "(如果 / 否则) are single tokens rather than multi-token "
                  "phrases, which is what forced reader packs to support "
                  "keyword groups at all.",
    },
    {
        "id": "zh-Hant",
        "title": "繁體中文 — Traditional Chinese",
        "role": "Sibling-pack divergence",
        "why": "Not a variant spelling of Simplified — a separate pack with "
               "genuinely different vocabulary. `常量` against `定值` for the "
               "same concept.",
        "stress": "**Sibling packs.** Two packs for one language proved the "
                  "substrate could carry divergent vocabulary over identical "
                  "semantics, and forced the vocabulary-governance rules that "
                  "keep them from drifting apart.",
    },
    {
        "id": "vi",
        "title": "Tiếng Việt — Vietnamese",
        "role": "The Latin-script control",
        "why": "The control case. Without it the architecture could be "
               "\"works on exotic scripts, unproven on Latin\" — correct for "
               "the hard cases and quietly wrong for the familiar one.",
        "stress": "**Heavy diacritics on Latin script.** NFKC edge cases and "
                  "accent-sensitive suggestion matching, where two spellings "
                  "look nearly identical and must not be confused. Multi-word "
                  "keywords join with underscores: `bắt_đầu`.",
    },
    {
        "id": "ar",
        "title": "العربية — Arabic",
        "role": "The required RTL pack",
        "why": "The only right-to-left language in the set. Without it the "
               "architecture can ship code that is correct on paper and renders "
               "wrong on screen — and nobody would find out from a test suite.",
        "stress": "**Bidirectional text.** Contextual glyph shaping, ligatures, "
                  "and the split between logical and visual order. Diagnostics "
                  "have to bidi-isolate the source they quote, or an error "
                  "message points at the wrong character.",
    },
    {
        "id": "hi",
        "title": "हिन्दी — Hindi",
        "role": "The Indic-family representative",
        "why": "Stands in for the whole Indic family. A pack that handles "
               "Devanagari proves the path for Bengali, Tamil, Telugu, "
               "Gujarati, and the rest — they inherit the substrate this one "
               "established.",
        "stress": "**Matra and virama consonant clusters**, where a grapheme "
                  "spans several code points and NFKC equivalence has to hold. "
                  "It is also the pack that confirmed **Indic numerals** "
                  "(०-९) stay rejected inside numeric literals — a digit that "
                  "looks like a number but is not one.",
    },
]

HEAD = '''+++
title = "Localization"
section = "localization"
order = 2
sources = [
  "radix/docs/design/reader-locale.md",
]
+++

Faber source can be read in eight human languages. Not translated — *rendered*.
The compiler holds one analyzed program and prints it in whichever reader
locale you ask for, so keywords and type names change while identifiers, string
literals, and the glyphs carrying structure stay exactly where they were.

That is what makes cross-language review possible: two people can hold the same
package open in different languages and be editing one program.

## Why these languages {#why}

The set is not the eight largest languages, and it is not a wish list. Each
pack was selected against three axes:

| Axis | Question |
|---|---|
| **Access** | Does this population face a real English barrier when programming? |
| **Reach** | How many developers does it serve? |
| **Architectural stress** | Does it force the compiler to confront a Unicode or emission problem no other pack does? |

The third axis is the lever. A set chosen for population alone proves nothing
the substrate did not already handle; a set chosen for
**collective architectural coverage** turns "pick languages" into
"derive architecture."
Every major Unicode axis — spaceless tokenization, width normalization,
bidirectional rendering, consonant clusters, diacritic-heavy Latin — is
stressed by at least one language here, on purpose.

'''

TAIL = '''## Why not others {#why-not}

Reasonable languages that are deliberately absent, and what it would take to
add them:

| Language | Why not yet |
|---|---|
| **Japanese** | The natural next addition. Its concerns — Kanji/Kana mixing, paired constructs — overlap heavily with Chinese, so it adds reach more than new architecture. If the set grows, this is next. |
| **Korean** | Hangul handles cleanly under XID identifier rules, so it needs no new substrate work. |
| **Spanish · French · Russian · Portuguese** | Little unique architectural stress, and weaker access wedges — these populations broadly reach English already. Adding them is vocabulary work, not compiler work. |
| **Bengali · Tamil · Telugu · Gujarati** | Subsumed by Hindi as the Indic representative. Their packs inherit the substrate Hindi proved; they are additions, not new problems. |
| **Swahili · Hausa** | A genuine access wedge, but current LLM coverage is thin and developer populations small, so the authoring loop does not close yet. Worth revisiting as coverage improves. |

Absence is not judgement. A language missing from this list is missing because
it would not teach the compiler anything new — which means adding it later is
mostly translation, not architecture.

## What does not change {#invariant}

Across every pack above:

- **Glyphs** — `←` `→` `∴` `≡` `∪` `⇥` — never localize. Structure reads the
  same everywhere.
- **Identifiers and string literals** stay exactly as written.
- **The machine interior** — HIR, stable diagnostic codes, `norma:*` package
  ids — stays Latin behind the curtain, so tooling is not chasing a moving
  target.

Diagnostics render in your reader locale too. An error at the fault site is not
English prose sitting inside Thai source.

## Switching locale {#switching}

```bash
faber format --reader-locale th-TH <package>
```

A reader locale is a rendering choice, not a fork. There is one grammar; only
its surface spelling moves.

Related: [Reader locales](/language/reader-locales.html) for the full
mechanism · [Glyphs and Latin](/language/glyphs.html) for why the glyphs hold
still · [Cheat sheet](/cheatsheet/) where every example carries all eight
surfaces
'''


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", default="src/en-US/localization.md")
    args = ap.parse_args()

    parts = [HEAD]
    written = 0
    for loc in LOCALES:
        panel = PANELS / f"{loc['id']}.fab"
        if not panel.is_file():
            print(f"  warning: missing panel {panel}", file=sys.stderr)
            continue
        body = panel.read_text(encoding="utf-8").strip()
        parts.append(
            f"## {loc['title']} {{#{loc['id'].lower()}}}\n\n"
            f"**{loc['role']}.** {loc['why']}\n\n"
            f"*Architectural stress:* {loc['stress']}\n\n"
            f"```faber locale={loc['id']}\n{body}\n```\n\n"
        )
        written += 1

    if not written:
        print("ERROR: no locale panels found", file=sys.stderr)
        return 1

    parts.append(TAIL)
    out = REPO / args.output
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("".join(parts), encoding="utf-8")
    print(f"localization: {written} locales → {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
