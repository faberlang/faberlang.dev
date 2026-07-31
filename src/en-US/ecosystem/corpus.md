+++
title = "Language corpus"
section = "ecosystem"
order = 6
sources = [
  "radix/corpus/ (304 .fab files, 185 registry terms, index.toml)",
  "radix/corpus/README.md",
  "examples/corpus/README.md (relocation stub)",
]
+++

The Faber language corpus is the language dictionary: one top-level
directory per keyword, operator group, or language type surface. It is the
development source for `faber explain` and the primary input for
multi-target compile matrices.

## Location {#location}

The corpus was split in Radix v0.79.0:

| Content | Lives in |
|---------|----------|
| Single-file language exempla (keywords, operators, types, concepts) | `radix/corpus/` |
| Package-shaped corpus fixtures | `faber/corpus/` |
| Application demos | `examples/` (sibling dirs) |

The old `examples/corpus/` path is a redirect stub. The generated corpus
pages on this site are built from `radix/corpus/`.

## Stats {#stats}

- 304 `.fab` exemplar files
- 185 registry terms in `index.toml`
- ~135 keyword and concept directories

## Layout {#layout}

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

## File format {#file-format}

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

## Usage {#usage}

```bash
faber explain functio       # show keyword reference
faber explain ≡             # show glyph reference
faber explain --search query # search across corpus
faber explain --list         # list all terms
```

## Categories {#categories}

Terms are organised by category: `function`, `control-flow`, `type`,
`collection`, `transfer`, `annotation`, `iteration`, `destructuring`,
`testing`, `cli`, `concept`, `operator-group`, `existing-home`.
