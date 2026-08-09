+++
title = "Radix 0.7.0"
section = "releases"
order = 90
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.7.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

Focused release adding `lege()` stdin I/O across the compiler, removing JS-style
arrow syntax in favor of the colon-lambda form, deepening Zig codegen coverage,
and trimming stale `rivus/` lexicon files.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 10 |
| Date span | 2025-12-30 (single day) |

### Major tracks

#### Language: arrow syntax removal, lambda simplification

- Removes `=>` arrow-function syntax (token, parser, AST node, codegen for all
  6 targets, tests) in favor of the consistent Latin-colon form **`pro x: expr`**.
  Block-form `pro x { body }` is unchanged. (`e7f1fdd24`)

#### I/O: `lege()` stdin expression

- Adds `lege()` keyword, parser rule, AST node, and semantic analysis for
  reading stdin as a string. (`9b559ac50`)
- TypeScript codegen emits `await Bun.stdin.text()`. (`2ec0cd82a`)
- Zig codegen for `lege()` wired through the preamble. (`9b559ac50`)
- Renames the `pactum` method `lege` → `accipe` to free the reserved word. (`9b559ac50`)

#### Zig codegen expansion

- **Lambda type inference and Lista construction** — lambda/arrow expressions
  now infer return types from semantic analysis (generating proper Zig structs
  instead of `@compileError`). Array literals assigned to `lista<T>` variables
  emit `Lista(T).fromItems()` / `Lista(T).init()`. `qua` casts to `lista<T>`
  also emit Lista construction. (`09ddc6cf9`)
- **Output stream fix** — `scribe` → stdout, `mone` → stderr, `vide` → debug,
  correcting the Zig preamble stream mapping. (`3277e031a`)
- **Tabula** — adds `confla` and `inLista` to the Zig tabula runtime, alongside
  updated probes. (`3ed8c59c6`)

#### Test runner: allocator context (`wrap`)

- Adds a general-purpose `wrap` property to test cases that wraps input with a
  template (`$` = placeholder), used to provide allocator context for Zig tests
  requiring `cura` blocks. Applied to 15 tests across scriptum, lista, copia,
  and tabula. (`c7fd80ea7`)

#### Cleanup

- Removes the old `rivus/lexicon/` files (nomina, typi, typi_constructi, verba,
  verba_clavium — 1181 lines). (`41d274a87`)

#### Bootstrap documentation

- Marks **Phase 3 I/O complete** (stdin/stdout). Documents minimum Zig
  requirements for self-hosting the Faber compiler. (`fa8d326b4`, `3ed8c59c6`)

### Other changes

- Disables parser tests for unimplemented `cura` curator kinds (`liber`,
  `conexio`, `mutex`) and skips corresponding codegen tests. (`9b559ac50`)
- Release commit: package.json version bump to 0.7.0. (`1b22da336`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
