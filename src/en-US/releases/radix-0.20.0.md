+++
title = "Radix 0.20.0"
section = "releases"
order = 79
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.20.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

Minor release spanning 31 non-merge commits across the compiler pipeline, semantic
analyzer, runtime design, and CI infrastructure. This release establishes a working
GitHub Actions CI pipeline, migrates the norma registry to a flat JSON format,
fixes multiple type inference gaps in the rivus bootstrap compiler, and completes
a major design review of the Nucleus async runtime.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 31 |
| Date span | 2026-01-08 → 2026-01-09 |

### Major tracks

#### CI pipeline and build order

- Add GitHub Actions CI workflow with sequential build stages and artifact passing
  between jobs (`acd723b6d`)
- Fix CI job order so `build:norma` runs first — its generated registry files are
  gitignored so they must be produced before `build:faber` (`efbd5077e`)
- Fix build order: norma must also run before faber in the local build script
  (`585fd2943`)
- Fix artifact path: `upload-artifact` strips the common `fons/` prefix — copy
  files to correct location after download (`0058953ea`, `1f9de65cf`)
- Update CI paths for the flat JSON norma registry (`30557e8b8`)

#### Build pipeline (artifex and build-exempla)

- Rename the self-hosting compilation target from `bootstrap` to `artifex`,
  aligning with Faber's Latin naming convention: faber (craftsman) → rivus (stream)
  → artifex (master craftsman) (`78e72bf26`, closes #73)
- Restructure the build pipeline to produce an `opus/bin/artifex` executable and
  add `--verify-diff` support for comparing against faber output (`f3e0b52bb`)
- Fix `build-exempla` to use stdin for all compilers — rivus/artifex read from
  stdin differently than faber's CLI interface (`34144198e`)
- Add norma-generated artifact to `build-artifex` — rivus source imports
  `norma-registry.gen.fab` at compile time (`4d9985daf`)

#### Norma registry: flat JSON format

- Add a flat JSON format for the norma registry with `collection:method:target`
  keys — O(1) hash lookup vs O(n) control flow, 72 KB vs 122 KB for the FAB elige
  equivalent (`e02724744`)
- Populate the registry with innatum (collection metadata) and radixForms (method
  metadata) data — 878 entries: 11 collections, 48 methods, 819 translations
  (`65bcd3dd1`)
- Migrate faber codegen to consume `fons/norma/index.json` directly instead of
  the generated `norma-registry.gen.ts` (`edf07dcfe`)

#### Rivus semantic analyzer fixes (type inference)

- Fix pattern binding type inference in `discerne` statements — alias bindings
  (`ut g`) now resolve to variant types instead of IGNOTUM; partial field binding
  support (`30a8bf6a3`, fixes #78)
- Add `InnatumExpressia` type resolution — variables declared with `[] innatum`
  expressions now resolve to their target type, reducing artifex build errors from
  1198 to 39 (`b8a37110f`, fixes #74)
- Resolve `Usitatum` field types via symbol table lookup — field access on
  user-defined types (`lexResult.errores`) now resolves the actual Genus
  definition to enable norma translation (`9235f4e64`, fixes #68/#69)
- Fix `ignotum` type annotation to produce the proper `Ignotum{}` variant instead
  of `Usitatum{nomen: "ignotum"}` (`fdb86c2dc`, fixes #62/#64)
- Fix predeclaration: use IGNOTUM instead of VACUUM for declared return types,
  matching faber's behavior (`51c27a069`, fixes #51/#58)

#### Rivus codegen improvements

- Emit `export` keyword for public declarations — add visibility tracking to AST
  types and all codegen generators so module-level symbols are properly exported
  (`a570115a6`, fixes #67/#70)
- Fix class field visibility inheritance — fields in public classes now inherit
  parent visibility instead of defaulting to private, matching TypeScript implicit
  public semantics (`030620876`, fixes #75)
- Fix double braces in rivus TypeScript codegen `scriptum()` templates — `{{`/`}}`
  passed through literally in 11 template files, causing malformed output for
  for-loops, async IIFEs, classes, and other block constructs (`5c2968c4c`,
  fixes #66/#71)

#### Rivus parser: multi-discriminant discerne

- Implement multi-discriminant pattern matching in the rivus parser — enables
  `discerne left, right { casu A ut l, B ut r { … } }` syntax across AST,
  parser, codegen, and semantic analysis (`637769d0b`, fixes #48/#63)
- Fix pactum methods map type in module export extraction — `Map<string, SemanticType>`
  vs `Map<string, FunctionType>` mismatch (`96ff0077f`, fixes #65)

#### Nucleus runtime design

- Consolidate Nucleus runtime design around async generators as the fundamental
  primitive — first revision adds Latin conjugation mapping, stdlib examples, and
  target-specific design sections (`347a11c9d`)
- Merge `async-generator.md` into `nucleus.md` — add The Inversion comparison,
  scope boundaries, Zig 0.15 alignment, ChunkIterator impl, LegetFuture state
  machine, and trade-offs analysis (`fe55fd016`)
- Split the 1800-line Nucleus design monolith into focused documents: README,
  responsum, streaming, executor, dispatch, targets, and implementation (`a79f9b3a0`)
- Add augur review concerns and edge cases — streaming-first edge cases, Latin
  conjugation ambiguity, database streaming, architecture boundaries, executor
  concerns, backpressure, and phase-specific issues (`27c9acdb8`)
- Resolve design review findings and add `probationes.md` — protocol naming
  (Latin canonical), target-varying protocol shapes, allocator threading, verb
  syntax codegen, and execution test framework using Faber's proba syntax
  (`678e7dbca`)

#### Development tooling

- Add **augur** agent — a forward-looking consequence analyst with feedback,
  revision, and issues modes for design document review (`b86aeb89d`)
- Update `columbo.md` with additional investigation procedures (`8c571d54f`)
- Update `augur.md` (`d63ebc5ca`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
