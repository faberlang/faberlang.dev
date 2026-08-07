+++
title = "Radix 0.11.0"
section = "releases"
order = 88
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.11.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

Major bootstrap compiler push: the semantic analyzer and TypeScript codegen are
now written in Faber and compile through the bootstrap toolchain. The language
gains optional parameters (`si`/`vel` syntax) and alias bindings in pattern
matching (`ut`). The `lege` I/O form drops parens to match standard read/readline
convention. Parser internals are cleaned up with extracted keyword predicates,
fixed idiom bugs, and simplified casts.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 32 |
| Date span | 2025-12-31 → 2026-01-01 |

### Major tracks

#### Bootstrap compiler (self-hosting)

- Adds the Phase 2 semantic analyzer for the bootstrap compiler (`fons-fab/semantic/`):
  18 files, ~2,900 lines covering type resolution, scope chains, error reporting,
  and the `Resolvitor` pattern for mutual recursion (`25a26fe81`)
- Adds the TypeScript code generator written in Faber (`fons-fab/codegen/ts/`):
  5 files, ~1,480 lines covering 24 expression types and 31 statement types
  (`9474df2b1`)
- Adds the codegen entry point and a minimal `stdin→stdout` CLI bootstrap
  compiler (`8adfe3c61`)
- Fixes 52 files across the bootstrap compiler: adds `@ publicum` exports,
  corrects `SymbolumGenus` enum member names (`Semicolon→PunctumColon` etc.),
  and fixes stdlib method names to match the `lista` registry, reducing
  TypeScript errors from 358 to 299 (`9b090eaf5`)
- Refactors TS codegen from string concatenation to `scriptum()` builder
  (`4a97381d3`)
- Refactors codegen to use `ut` alias binding in `discerne` blocks
  (`df76c1982`)
- Fixes `scriptum()` brace escaping in TS codegen (`88632adcc`)
- Removes unnecessary `qua Expressia` casts now that type inference handles
  `discerne` bindings (`dea753769`)
- Applies `si` optional parameter syntax in bootstrap compiler source
  (`34c988410`)
- Extracts statement-starting and genus-member keyword predicates from
  `nucleus.fab` into `lexicon/verba.fab` as a single source of truth,
  eliminating the maintenance hotspot identified by LLM reviewers
  (`b042924df`)
- Fixes `specta`/`praevius` parser idiom bugs in `declara.fab`, `fluxus.fab`,
  and `imperium.fab`; adds LLM Readability Goal to design philosophy
  (`926c74e83`)
- Adds `lineam` keyword to the `fons-fab` lexicon (`9a923fed3`)

#### Optional parameters (`si`/`vel` syntax)

- Implements optional function parameters using `si` (if) to mark optional and
  `vel` (or) to provide defaults — syntax `de si numerus depth vel 3` — with
  codegen for all 6 targets (TS, Py, Rust, C++, Zig, Fab) and semantic rules
  enforcing required-before-optional ordering (`672e957d1`)
- Documents the `si`/`vel` parameter modifier syntax in `CLAUDE.md`
  (`5862d23f2`)

#### Alias bindings in `discerne` pattern matching (`ut`)

- Adds the `ut` keyword to bind a whole variant to a name instead of
  destructuring fields positionally with `pro` — codegen updated for all 6
  targets (`9031e9f56`)
- Recommends `ut` over `pro` for readability in `CLAUDE.md` (`be26dc785`)

#### `lege` stdin syntax change

- Changes stdin reading from `lege()` to `lege` (read all) and adds
  `lege lineam` (read one line), following standard I/O convention of read vs
  readline; updates parser, AST, all codegen targets, and tests
  (`2df48ca57`)
- Regenerates grammar documentation for the new `lege lineam` syntax
  (`fd88f7956`)

#### Semantic analysis fixes

- Fixes `discerne` pattern binding type inference: adds `DiscretioType` with
  variant field tracking so bindings like `si Click pro x, y` correctly infer
  field types instead of defaulting to `unknown` (`475b8e9ce`)
- Fixes `discretio` return type mismatch for `finge...qua` expressions: the
  `resolveFingeExpression` now looks up the actual `discretio` type from the
  symbol table instead of creating a mismatched `userType()` (`98529af43`)

#### Documentation and process

- Updates `AGENTS.md` with workspace layout and process documentation
  (`9488acba5`)
- Merges `CLAUDE.md` into `AGENTS.md` (`3219f9fd9`), then adds grammar
  verification guidelines to `AGENTS.md` (`2f4c49f35`)
- Adds LLM cross-model validation finding to README (`31cdedc89`)
- Creates `consilia/futura/si-intra.md` — a planning document for an
  if-within-if guard clause pattern (`20f75f287`)
- Updates `bootstrap-ts.md` for parser completion (27 files, 6,259 lines)
  and progress tracking (`6a5a6ec9e`, `80756ce17`, `ac9d033ae`)
- Adds test documentation files (`5eeb8923d`)

#### Other changes

- Disables the `format` CLI command; the archived prettier plugin is removed
  (`5574cb06e`)
- Moves prettier source from `fons/` to `archivum/` (`8e86d046f`)
- Renames disabled prettier test (`a35876011`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
