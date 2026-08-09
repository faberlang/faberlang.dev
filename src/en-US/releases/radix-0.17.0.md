+++
title = "Radix 0.17.0"
section = "releases"
order = 80
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.17.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

Norma registry unification, function type syntax, shift operator keywords, and
conversio operators in Rivus — 25 commits across codegen, parser, semantics,
documentation, and the compiler backend.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 25 |
| Date span | 2026-01-06 → 2026-01-06 |

### Major tracks

- **Unified codegen registry.** Removes per-target norme (aleator, mathesis,
  tempus) from C++, Python, Rust, TS, and Zig codegen backends. Replaced by a
  single declarative norma registry (`norma-registry.gen.ts` /
  `norma-registry.gen.fab`) with `.fab` module definitions for tabula, copia,
  aleator, tempus, mathesis, and solum. Includes cross-module type resolution,
  template escaping fixes, and removal of fallback-guessing paths.
  (`8cda3c48c`, `d953b53c7`, `638836ecc`, `c6b5cb4a4`, `56b19b2c9`,
  `3a980f84a`, `f884009bd`)

- **Function type syntax.** Adds function type annotations across all codegen
  targets (TS, Rust, Zig, C++, Python, Fab), parser AST and grammar support,
  return types in `lista.fab`, and corresponding documentation.
  (`4f060c75b`, `fc5e0a5ca`, `2612f6749`, `21467aa72`)

- **Shift operator keyword migration.** Replaces `<<` / `>>` tokens with
  `dextratum` / `sinistratum` keywords across all six codegen backends, the
  tokenizer, parser AST, and lexicon. (`735abe21f`, `21467aa72`)

- **Conversio operators in Rivus compiler.** Implements type-conversion
  operators in the Rivus backend: AST, lexer tokens, parser (unary expression),
  semantic analysis, and TypeScript codegen. Includes examples and checklist
  entries. (`f3012901e`, `467208e8e`, `bd6a64b36`)

- **Verum/falsum unary operators.** Adds `verum` / `falsum` unary operators to
  the parser, with fix for consumption across newlines and correction to
  `si…cape…secus` codegen. (`5bea87fa9`, `a2662ea8a`)

- **Documentation audit and reorganization.** Moves `consilia/futura/` entries
  to `completa/` or `archived/`; adds new design notes (de, ex, in, pro, qua,
  ut); adds exempla files for conversio, innatum, optional-chaining, praefixum,
  ternary, vel, externa, incipiet, and mori. Deletes `phd-thesis.md`.
  (`233d4c252`, `954e1091f`)

- **Async-generator-first design principle.** Adds detailed design note
  (`consilia/futura/async-generator.md`, 342 lines) and morphology integration
  notes for `@` ad-annotation design. (`7d711890d`, `89a896045`)

- **solum.fab stdlib skeleton.** Adds a 254-line local I/O stdlib module
  (`fons/norma/solum.fab`) and `curata` allocator binding with Zig 0.15
  compatibility fixes across exempla and Zig codegen.
  (`7163b6278`, `4383a69fc`)

### Other changes

- Remove `lege` example and tests (`21ae0eea5`)
- Remove nested generic spacing workaround in `nucleus.fab` (`1ed13cefb`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
