+++
title = "Faber"
section = ""
order = 0
sources = []
+++

**Faber** is a package-oriented programming language with a Latin
behavioural vocabulary, a small regular grammar, and a type-first static
type system. Source is compiled through the Radix compiler to reviewable
Rust and native binaries. Its defining architectural property is that
meaning lives in a semantic core — the HIR (high-level intermediate
representation) — rather than in any particular rendering.

The name derives from the Latin word for *maker* or *craftsman*. The
compiler is named Radix, from the Latin *root*. The language is
developed by Ian Zepp and released under the MIT license.

| | |
|---|---|
| **Paradigm** | Package-oriented; semantic staging |
| **Typing** | Static, type-first; nullable via `T ∪ nihil` |
| **Glyphs** | `← → ∴ ≡ ∪ ⇥` |
| **Designed by** | Ian Zepp |
| **First appeared** | 2024 |
| **Compiler** | Radix (Rust) |
| **Lanes** | Application (HIR) · Systems (MIR) |
| **Primary target** | Rust → native binary |
| **Reader locales** | 7 shipped (la, ar, hi, vi, th-TH, zh-Hans, zh-Hant) |
| **Standard library** | Norma (`norma:*`) |
| **License** | MIT |

## Overview {#overview}

Faber is designed around a core insight: the intermediate representation
is the truth, and no target or human-language surface is privileged. A
Faber program written in Latin keywords can be rendered into Thai,
Arabic, or Chinese keywords through the same mechanism that renders it
into Rust, Go, or WebAssembly — because the HIR is the authority and
every output is a *rendering* of it.

The language makes three deliberate signal choices that work together:

- **Type-first declarations** — shape reads toward binding: `textus nomen`,
  not `nomen: textus`.
- **Latin behavioural words** — declarations, statements, and lifecycle:
  `functio`, `genus`, `fixum`, `redde`, `si`.
- **Structural glyphs** — value flow and type joints: `←` (bind), `→`
  (return type), `∴` (compact branch), `≡` (equality), `∪` (union).

The result is source with stable grammatical shape that can be reviewed,
transformed, and lowered without losing the reader's sense of intent.

## Documentation {#documentation}

| Section | Description |
|---|---|
| [History](/history/index.html) | Development timeline, influences, and release history |
| [Features](/features/index.html) | Reader locale, compilation lanes, Latin vocabulary, glyph system, design principles |
| [Syntax](/syntax/index.html) | Complete reference: types, functions, control flow, errors, generics, collections |
| [Tooling](/tooling/index.html) | Radix compiler pipeline, Faber CLI, codegen targets, scripting |
| [Ecosystem](/ecosystem/index.html) | Norma, Cista, Triga, coreutils, AI Workbench, corpus |
| [References](/references/index.html) | EBNF grammar, design documents, repositories |

## Quick example {#quick-example}

A simple function demonstrating key Faber patterns — type-first
parameters, glyph return type, nullable union, Latin control words:

```text
functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ∴ redde nihil
    redde a / b
}
```

## Live rendering {#live-rendering}

The divide function above is rendered in the Latin pack by default. The
compiler can render the same program in seven reader locales — Thai,
Chinese, Arabic, Hindi, Vietnamese — each remapping keywords and types
to that language while glyphs and identifiers remain unchanged. This is
not a translation layer applied to the page; it is the same mechanism
the compiler uses to produce localized source.

See the [reader locale](/features/reader-locale.html) documentation for
the full discussion.
