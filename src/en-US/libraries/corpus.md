+++
title = "The language corpus"
section = "libraries"
order = 3
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

Corpus content is divided by shape:

| Content | Lives in |
|---------|----------|
| Single-file language exempla (keywords, operators, types, concepts) | `radix/corpus/` |
| Package-shaped corpus fixtures | `radix/corpus-product/` |
| Complete simulation programs | `radix/corpus-simulations/` |
| Application demos | `examples/` (sibling dirs) |

The old `examples/corpus/` path is a redirect stub. The generated corpus
pages on this site are built from `radix/corpus/`.

## Simulations {#simulations}

Since 1.18 four complete programs sit beside the corpus, each with a README, a
small smoke and its provenance:

| Program | What it does |
|---|---|
| `fusion-containment` | Particle orbits from one Latin source, on the reference route, multicore CPU and Metal |
| `drone-mission` | Branchy aircraft mission evaluation, where each GPU lane flies a whole mission |
| `swarm-decimal` | A deterministic many-actor simulation in fixed-point decimals |
| `h264-encoder` | A constrained-baseline H.264 encoder on native multicore CPU workers; no GPU acceleration is claimed |

Device execution and the native Rust emitter are in the released `faber` binary,
not the open-source build. Each README gives its exact route requirements.

## Size {#stats}

The corpus holds several hundred `.fab` exemplar files, one directory per
keyword, operator group, or concept. Each term has one owning file, and the
`faber` build embeds the corpus, so there is no separate index to maintain.
`faber explain --list` prints the current term list.

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
```

## File format {#file-format}

Each `.fab` file begins with TOML frontmatter describing the term:

```toml
+++
term = "functio"
kind = "keyword"
category = "function"
canonical = false
summary = "Declares a named function or method."
syntax = "functio <name>(<params>) [modifiers] [→ <type>] [⇥ <error-type>] <block>"
related = ["→", "⇥", "redde", "sponte"]
locale = "en"
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

Terms are organised by category, for example `function`, `control-flow`,
`type`, `collection`, `conversion` and `testing`. List one category with
`faber explain --category <CATEGORY>`.
