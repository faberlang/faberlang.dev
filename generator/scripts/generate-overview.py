#!/usr/bin/env python3
"""
generate-overview.py — assemble src/en-US/language/overview.md.

The Overview page is the landing claim plus the shape of everything: one real
program, what the language gives you, where it compiles, and where to go next.
Its code panels are the captured compiler output under `generator/landing/`
(the same cache the landing page reads), inlined here so the two pages cannot
drift.

Only the committed cache is read; a checkout without sibling repositories
still builds. The page is rendered by the site generator, so its Faber panel is
authored in canonical Latin and transcoded to the page's reader locale
(English) by the normal Markdown pipeline — the same convention every other
source page follows.

CLI:
    generate-overview.py [--landing generator/landing]
                         [--output src/en-US/language/overview.md]
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent

# Reader-locale program panel. `locales/la.fab` is the canonical Latin surface
# captured by capture-landing-panels.sh; the en-US build transcodes it to the
# English reader surface at render time. The page never hand-writes code.
PROGRAM_PANEL = "locales/la.fab"
PROGRAM_OUTPUT = "program.out.txt"
TARGET_PANEL = "targets/out.rust.txt"
TARGETS_ROWS = "targets/faber-targets.txt"

# Escapes for the target table's yes/— cells; `faber targets` spells the rest.
def yn(value: str | None) -> str:
    return "yes" if value == "yes" else "—"


def read_targets(path: Path) -> list[dict[str, str]]:
    """Parse `faber targets` rows: `key available=yes check=yes build=yes ...`."""
    rows: list[dict[str, str]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        key, _, rest = line.partition(" ")
        cells = {m.group(1): m.group(2) for m in re.finditer(r"(\w+)=(\S+)", rest.split(" note=")[0])}
        if key and cells:
            cells["key"] = key
            rows.append(cells)
    return rows


def target_table(rows: list[dict[str, str]]) -> str:
    body = ""
    for row in rows:
        if row.get("available") != "yes":
            continue
        body += (
            f"| `{row['key']}` | {yn(row.get('build'))} | {yn(row.get('package'))} "
            f"| {yn(row.get('run'))} |\n"
        )
    return (
        "| Target | Emits | Package | Runs |\n"
        "|--------|-------|---------|------|\n"
        f"{body}"
    )


def build(landing: Path) -> str:
    program = (landing / PROGRAM_PANEL).read_text(encoding="utf-8").strip()
    output = (landing / PROGRAM_OUTPUT).read_text(encoding="utf-8").strip()
    rust = (landing / TARGET_PANEL).read_text(encoding="utf-8").strip()
    targets = target_table(read_targets(landing / TARGETS_ROWS))

    return f"""\
+++
title = "Overview"
section = "language"
order = 1
sources = []
+++

Faber is a statically typed language for coding agents and human authors. It
has a small mechanical grammar, explicit static and generic types, and
math-oriented operators — and the same program can be written and read in
eight language surfaces. This page is the claim plus the shape of everything;
the pages below it go one level deeper.

## One program {{#program}}

This is the whole program the landing page opens with: a small type, a generic
helper, and an entry point. Every panel on this page is compiler output, so the
page cannot claim something the toolchain does not produce.

```faber
{program}
```

Its real output:

```text
$ faber run
{output}
```

Reading it left to right, the shape repeats everywhere in the language:
the type comes before the name (`f64 low`), generics are written out
(`fn choose<T>`), `←` binds a value at run time while `=` fixes a field's
shape at compile time, `÷` is true division and `/` floors (`-7 / 2` is
`-4`), and `main` is the entry point. None of that changes when the keywords
are rendered in another language — the glyphs and the order stay put.

## What the language gives you {{#capabilities}}

- **A mechanical grammar.** One construct has one spelling. Arrows mean
  runtime effects (`←` assign, `→` return, `⇥` error channel); `=` and `:`
  only state compile-time facts. [Why the glyphs work this way](/language/behavior/glyph-law.html).
- **Type-first declarations.** A declaration is a type followed by a name —
  `f64 low`, never `low: f64` — for parameters, locals and fields alike.
  Nullability is `T ∪ none`, and crossing between integer and float is an
  explicit `↦`. [Types and values](/language/types.html).
- **Math-oriented operators.** Integer `/` floors; true division is `÷`;
  comparisons read as math (`≤`, `≥`, `≠`, `≈`). When math and hardware
  convention disagree, Faber follows the math.
- **Widths apply at the store.** Arithmetic runs unbounded; a width limit is
  applied once, where a value is stored into or converted to a bounded cell.
  [Math in the ether](/language/behavior/numeric-widths.html).
- **Reader locales, sealed.** One reader locale per file, never mixed. The
  same program renders in eight surfaces and converts losslessly back to
  canonical Latin. [Reader locales](/language/reader-locales.html).
- **Errors as values, tests as declarations.** A fallible function declares
  its error channel with `⇥`; callers recover with `fac`/`cape`. Test suites
  live beside the code with `probandum`, `proba` and `adfirma`.
  [Errors and testing](/language/behavior/errors-and-tests.html).

## Where it compiles {{#targets}}

Faber compiles through one analyzed program to many targets. Write a library,
emit it in the language your project already uses, and add it alongside your
existing code. This small class, with no generics and no `main`, is emitted
below exactly as `radix emit --target rust` produces it:

```rust
{rust}
```

The table is read from `faber targets`, so it cannot drift from the toolchain.
`Emits` is source emission, `Package` is package assembly, `Runs` is running
through faber.

{targets}
Rust builds as a Cargo package today. Other targets give you source files to
add to your existing project; assembling them into installable packages is
not built yet. Support is stated target by target — generics and some
operators do not lower to every target, and the matrix records where.
[Read the target matrix](/toolchain/target-matrix.html).

## Where to go next {{#next}}

| If you want to | Read |
|---|---|
| See the reasoning behind the language | [Behavior](/language/behavior/glyph-law.html) |
| Start writing code | [Start](/start/) |
| Look up a construct | [Cheat sheet](/cheatsheet/) and [Examples](/examples/) |
| Read the formal grammar | [Grammar](/reference/grammar.html) |
| Use the compiler | [Faber command line](/toolchain/cli.html) |
| Pick another reader language | [Reader locales](/language/reader-locales.html) |
"""


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    gen = Path(__file__).resolve().parent.parent
    ap.add_argument("--landing", type=Path, default=gen / "landing")
    ap.add_argument("--output", type=Path,
                    default=REPO / "src" / "en-US" / "language" / "overview.md")
    args = ap.parse_args()

    for rel in (PROGRAM_PANEL, PROGRAM_OUTPUT, TARGET_PANEL, TARGETS_ROWS):
        if not (args.landing / rel).is_file():
            raise SystemExit(f"missing landing panel {args.landing / rel}; "
                             "run capture-landing-panels.sh")

    text = build(args.landing)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(text, encoding="utf-8")
    print(f"wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
