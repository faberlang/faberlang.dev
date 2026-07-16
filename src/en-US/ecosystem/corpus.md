+++
title = "Language corpus"
section = "ecosystem"
order = 6
sources = [
  "examples/corpus/ (292 .fab files, 174 registry terms, index.toml)",
  "examples/corpus/README.md",
]
+++

The Faber language corpus is the public language dictionary: one top-level
directory per keyword, operator group, or language type surface. It is the
development source for `faber explain` and the primary input for
multi-target compile matrices.

## Stats

- 292 `.fab` exemplar files
- 174 registry terms in `index.toml`
- ~135 keyword and concept directories

## Layout

```
corpus/
  functio/           # function keyword exemplars
  genus/             # record type exemplars
  si/                # conditional branch exemplars
  itera/             # iteration exemplars
  lista/ tabula/     # collection type exemplars
  tensor/ sparsa/    # tensor exemplars
  ad/                # capability call exemplars
  operatores/        # glyph / operator groups
  ...
  index.toml         # generated explain manifest
```

## File format

Each `.fab` file begins with TOML frontmatter describing the term:

```toml
+++
term = "functio"
kind = "keyword"
category = "function"
canonical = true
summary = "Declares a named function or method."
syntax = "functio <name>(<params>) [modifiers] [→ <type>] [⇥ <error-type>] <block>"
aliases = ["function"]
related = ["→", "⇥", "redde", "sponte"]
+++

functio saluta() {
    nota "Salve, Mundus!"
}
```

## Usage

```bash
faber explain functio       # show keyword reference
faber explain ≡             # show glyph reference
faber explain --search query # search across corpus
faber explain --list         # list all terms
```

## Categories

Terms are organised by category: `function`, `control-flow`, `type`,
`collection`, `transfer`, `annotation`, `iteration`, `destructuring`,
`testing`, `cli`, `concept`, `operator-group`, `existing-home`.
