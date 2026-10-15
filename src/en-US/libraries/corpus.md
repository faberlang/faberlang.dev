+++
title = "The language corpus"
section = "libraries"
order = 3
sources = [
  "corpus/ (single-file exempla, one directory per term)",
  "corpus/README.md",
  "examples/corpus/README.md (relocation stub)",
]
+++

The Faber language corpus is the language dictionary: one top-level
directory per keyword, operator group, or language type surface. It is the
development source for `faber explain` and the primary input for
multi-target compile matrices.

## Location {#location}

Corpus content is divided by shape:

| Content | Lives in |
|---------|----------|
| Single-file language exempla (keywords, operators, types, concepts) | `corpus/` |
| Package-shaped corpus fixtures | `corpus-product/` |
| Application demos | `examples/` (sibling dirs) |

The old `examples/corpus/` path is a redirect stub. The generated corpus
pages on this site are built from `corpus/`.

## Size {#stats}

The corpus holds several hundred `.fab` exemplar files, one directory per
keyword, operator group, or concept. Each term has one owning file (the one whose
frontmatter lists it in `explains`), and a directory can hold further exempla
for the same term. There is no separate index file to maintain: the `faber`
build embeds every exemplum that declares `explains`, so `faber explain` always
matches the commit the binary was built from, and `faber explain --list`
prints the current term list. Directory names are the canonical term names,
spelled in Latin whichever reader locale you read the pages in.

## Layout {#layout}

```
corpus/functio/       function keyword exemplars
corpus/genus/         record type exemplars
corpus/si/            conditional branch exemplars
corpus/itera/         iteration exemplars
corpus/lista/         list type exemplars
corpus/tabula/        table (map) type exemplars
corpus/tensor/        tensor exemplars
corpus/sparsa/        sparse tensor exemplars
corpus/ad/            capability call exemplars
corpus/operatores/    glyph / operator groups
```

## File format {#file-format}

Each `.fab` file begins with TOML frontmatter describing the term:

```toml
+++
term = "functio"
explains = ["functio"]
kind = "keyword"
category = "function"
canonical = true
summary = "Declares a named function or method."
syntax = "functio <name>(<params>) [modifiers] [→ <type>] [⇥ <error-type>] <block>"
aliases = ["function"]
related = ["→", "⇥", "redde", "sponte"]
locale = "en"
+++

fn greet() → void {
    print "Hello, world!"
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

Terms are organised by category, for example `function`, `control-flow`,
`type`, `collection`, `conversion` and `testing`. List one category with
`faber explain --category <CATEGORY>`.
