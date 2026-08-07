+++
title = "Radix 0.27.0"
section = "releases"
order = 72
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.27.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

Short release spanning four days with significant ecosystem expansion: three new
microcompiler implementations (Rust, Go, Python), Go language support throughout the
pipeline, a new postfix construction syntax, and a unified stdin/stdout build model.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 79 |
| Date span | 2026-01-18 → 2026-01-21 |

### Major tracks

#### Nanus microcompiler ecosystem (Rust, Go, Python)

Three new implementations of the Faber microcompiler, all sharing a common
`subsidia` core library pattern:

- **nanus-rs:** Rust implementation with lexer, parser, semantic analysis,
  Faber emitter, and TypeScript emitter. Uses a shared `subsidia-rs` library
  crate (`812d1ef35`, `18c6f7bfc`, `ee0b5dd3b`)
  - Ownership annotations (`ex`/`de`/`in`) preserved on parameters
    (`43a982d78`)
  - Semantic lookup for match pattern enum names (`68c7e0400`)
  - 4-space indentation, `in` keyword for mutable borrow preposition
    (`2bcb409b3`, `4b6447563`)
  - Round-trip Faber emit fidelity fixes (`fbd93e22d`)

- **nanus-go:** Go implementation with TypeScript, Faber, and Faber Glyph (FG)
  emitters. Imports `subsidia/go` for shared AST and parser (`667905f23`,
  `01ecb23be`)
  - Struct/operator code generation, generic constructors, `const iota` enums
    (`7b958e3af`)
  - Go keyword sanitization for package names (`ddc2bdaaa`)
  - `-f` flag for output format selection (`c5675890f`)

- **nanus-py:** Self-contained Python implementation with lexer, Pratt parser,
  two-pass semantic analysis, and Faber/Python emitters (`9524fca19`,
  `47c119c6a`)

- **nanus-ts:** Low-effort parser improvements, renamed from `nanus` to
  `nanus-ts` (`9bab3e259`, `5f52cb5ce`)

- `verify-nanus` gains summary mode, directory/glob support (`4c5f26bb8`)

- All nanus compilers unified to stdin/stdout I/O (`c67da5e22`, `06f270038`)
  with unified error handling (`20891caa0`)

#### Go language support ecosystem

- **Go workspace:** `go.work` for monorepo module resolution, replaces fragile
  `replace` directives (`d6040d4f5`)
- **`subsidia/go` shared library:** extracted AST, parser, and error handling
  shared between nanus-go and glyph-go (`01ecb23be`)
- **`glyph-go` tool:** bidirectional Faber ↔ Faber Glyph conversion CLI
  (`01ecb23be`, `349cd92c3`)
- **Go HAL implementations:** `consolum` (stdin/stdout/stderr I/O) and `solum`
  (filesystem operations) at `subsidia/go/norma/hal/` (`1ccaa5eae`)
- **Semantic analysis pass** for Go code generation (`5622b2d10`)
- **Go build scripts** added for rivus and glyph-go (`f263a88de`, `65f9dff15`)
- **Organize and simplify** project structure for glyph-go, nanus-go
  (`349cd92c3`)

#### Postfix `novum` construction syntax

- `{...} novum Type` emits `new Type({...})` across all compilers (faber, rivus,
  nanus-ts, nanus-go, nanus-rs) (`f621246f4`)
- `{...} qua Type` is now exclusively a type assertion (`{...} as Type`)
- ~228 `} qua GenusName` usages in rivus source migrated to `} novum GenusName`
- Issue documentation added (`018ad2a8b`)

#### Rivus refactoring for Go compatibility

- Removed `tempta`/`cape` (try/catch) blocks — parser collects errors instead
  of throwing (`81cb1c7e3`)
- Disabled multi-file module resolution — rivus is now stdin-only
  (`81cb1c7e3`)
- Eliminated async entry point (`incipiet` → `incipit`), standardized on `mori`
  (panic) for error handling (`2c79eda26`)
- Ownership prepositions (`de`/`in`/`ex`) added to all ~437 function parameters
  across 102 files (`fc8e5a36a`)

#### Golden test corpus

- `corpus/` directory renamed to `golden/` (`003ab6222`)
- Golden corpus relocated to `fons/corpus/` as canonical location
  (`a54c818a1`)
- Golden test scripts added to main build pipeline (`620a372af`)
- TypeScript golden corpus files (`cc8791be3`, `2cacce809`)
- Complete nanus compilation support verified against rivus (`cdcbddc67`)

#### Faber Glyph format

- **Faber Glyph specification** added: Unicode-based alternative representation
  using Braille, Block Elements, and Math Operator ranges (`9d3f6d454`)
- README replaces GLYPH.md (`e743ff1e2`, `cc6e8059f`)
- TBDs resolved, glyph mappings reorganized (`be441d70f`)
- Round-trip encoding/decoding fixes (`9b9ac7194`)
- Mappings synced with updated README spec (`ca9f83bf6`)

### Other changes

- `--stdin-filename` flag added to all compilers (`f6772dbed`)
- CLI entry points renamed to match module names (`fons/faber/cli.ts` →
  `faber.ts`, `nanus-ts/cli.ts` → `nanus.ts`) (`fa9f42710`)
- Parser enforces `si` before `de`/`in`/`ex` parameter ordering across faber,
  rivus, nanus-ts, and subsidia-go (`9400ed465`)
- `subsidia-rs` gains low-effort parser improvements (`c765b7ba2`)
- `subsidia/go` parser improvements (`dd58181bc`)
- `fix(subsidia)`: reject invalid TypeScript-style type syntax (`8da7e78a3`)
- `fix(nanus)`: correct field visibility and add `===` operator
  (`231711225`)
- `fix(nanus)`: emit naked body for sync incipit, async IIFE for incipiet
  (`2c73bcffa`)
- `fix(faber)`: disable comment emission, fix golden import path
  (`ee64d391d`)
- `fix(build-norma)`: preserve `de` modifiers in generated function params
  (`3fcbaf2e9`)
- `feat(rivus)`: display auxilium help text in error messages (`bb2400466`)
- Docs: EBNF.md synced with current implementation (`9e1a0be76`,
  `d33898e0d`)
- Docs: shell script documentation and error handling improved (`2e88492dd`)
- Scripts organized with better comments and CI workflow documentation
  (`3a5617ff0`, `f3f528517`)
- Build pipeline restructured into 3 stages: nanus → norma+faber → rivus
  (`20a3b7c0e`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
