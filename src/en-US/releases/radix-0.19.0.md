+++
title = "Radix 0.19.0"
section = "releases"
order = 78
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.19.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

Release spanning **50 non-merge commits** (`v0.18.0..v0.19.0`). This cycle adds
three new codegen backends (Rust, C++, Zig) with norma-registry stdlib method
translation, overhauls the discerne pattern-matching system (ceterum default
cases, wildcards, exhaustiveness), fixes numerous parser and semantic bugs in
the rivus bootstrap compiler, and ships **Probationes v2.0** — a major expansion
of the LLM learnability trial framework with 34 new grammar tests, a SQLite
results database, token tracking, and ~17k trial runs across 30+ models.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 50 |
| Date span | 2026-01-07 → 2026-01-08 |

### Major tracks

#### New codegen backends (Rust, C++, Zig) with norma-registry integration

- **Rust codegen** (`fons/rivus/codegen/rs/`, 20 files, ~1434 lines): full
  statement/expression coverage with type mappings (numerus→i64, textus→String,
  lista→Vec, tabula→HashMap, copia→HashSet), async support, Result-based error
  handling, and norma-registry method translation (`b8d09d322`)
- **C++ codegen** (`fons/rivus/codegen/cpp/`, 18 files, ~1674 lines): C++23
  features (std::format, ranges), collectiones.hpp helper library, include
  tracking, and norma integration (`53b59a726`)
- **Zig codegen** norma-registry wiring: stdlib method translation via
  `getNormaTranslation`/`VerteTranslation` with §-placeholder template
  substitution and allocator threading (`8d766e239`)
- Bootstrap self-compile test that compiles rivus sources through the rivus
  executable, exposing gaps needed for full self-hosting (`b110a15fc`)

#### discerne pattern matching overhaul

- **ceterum default case**: catch-all default in discerne statements matching
  Zig's `else {}` approach — AST, parser, semantic, and all-backend codegen
  (`5f742ad3b`)
- **Wildcard handling**: `casu _` generates `else` instead of `if (x.tag === '_')`,
  fixing 29 files with non-exhaustive discerne statements (build: 78→106 of 107
  files) (`6cb15f305`, `a11910684`)
- **Exhaustiveness checking restored**: variant tracking and S017 error reporting
  that was accidentally removed in an earlier commit (`e55face0f`)

#### rivus lexer and parser fixes

- **Shift operators removed from lexer**: `>>` and `>>>` no longer tokenized as
  right-shift — fixes nested generic parsing (`tabula<textus, lista<textus>>`)
  (`d813ff22d`)
- **Bit-shift keywords**: `sinistratum`/`dextratum` keyword support (`161d7e60b`)
- **innatum keyword** for native type construction (`{} innatum tabula<…>`)
  (`12d776a02`)
- **verum/falsum/nihil prefix operators** respect line boundaries (fixes compound
  assignment after truth-check) (`ad2b158ed`)
- **Body-less @ externa** function declarations allowed at parser level
  (`d38fccc96`)
- **Keywords-as-identifiers** where appropriate (`4a4700d91`)

#### rivus semantic analysis fixes

- **Block scope creation** for si, dum, elige, custodi control flow — fixes 65
  false-positive "already defined" errors (`bf99d4833`)
- **Member property resolution** guarded with computatum check — prevents
  spurious "Undefined variable" for `obj.field` dot access (`107f36ce5`)
- **Primitivum type** handling in nomenReceptor for norma translation
  (`096bb5167`)
- **Cross-module type resolution**: three-pass export extraction for tabula
  chained property access across module boundaries (`26c478fcb`)
- **Pactum method type resolution** for cross-module imports (`c6d63b24e`)
- **User-defined genus** methods skip stdlib validation in all backends
  (`cc71fa5b9`)
- **Morphology parser** misclassifying single-vowel suffixes (stem-guided vs
  greedy disambiguation) (`a004e4747`)

#### Codegen fixes (all backends)

- **Bare string literals** in Rust/C++ codegen — emit `&str`/`const char*`
  instead of `String::from()`/`std::string()` (`d7da3b7ee`)
- **C++ string concatenation**: wrap left operand in `std::string()` for const
  char* compatibility (`46ffe92fc`, `7f8cc426c`)
- **TypeScript tabula (Map) iteration** fix (`6b0a9aee8`)
- **lista.filtra** / **lista.sectio** template placeholder fixes for C++ and
  Zig (`80f205baf`, `ac7db3120`)
- **Tabula.mappaValores/mappaClaves** C++ test expectation fixes (`5ab715978`)
- **{} qua copia\<T\>** generates `new Set<T>()` instead of type assertion
  (`6deac763f`)
- Norma-registry method translations applied in TS codegen (`243c8131f`)
- Binary test updates for new keywords (`15f9fa462`)
- Auto-generated `norma-registry.gen` files ignored (`8d907d542`)

#### Probationes v2.0 (LLM learnability trials)

- **34 new grammar tasks** covering error handling, switch statements, object
  literals, destructuring, for-in loops, ternary, type casts, nullish
  coalescing, string interpolation, imports, and more — task count: 61→95
  (`ca76b7304`)
- **trials-researcher agent** for experiment design and analysis (approval-gated)
  (`8b4e4e8a9`)
- **SQLite database** (`probationes/results/trials.db`) with import, query, and
  summary commands (`cf8c27d79`)
- **Token tracking** for drafter/verifier pipeline stages (`2ae52aee4`)
- **Framework 2.1**: 347 OpenRouter models, 30 models in config, 17k trials,
  control tasks for Faber vs TypeScript baseline — findings show minimal context
  outperforms complete context, and verbosity harms results (`7b5e944d8`)
- `--help` flag and explicit-args guard to prevent accidental expensive runs
  (`ba38b1035`)

#### Workspace and agent infrastructure

- **Agent renaming**: faber-lang-designer→cicero, trials-researcher→curie,
  test-fixer→galen, typescript-fixer→titus; new columbo agent; AGENTS.md
  consolidated (`269c35132`)
- **Harden agent instructions**: all agents must read AGENTS.md first; test-fixer
  gets allow/forbid lists and no-exploration principle (`9ea61401c`)
- Stdlib method tables centralized to `fons/norma/README.md` (`461ced099`)
- Stdlib (norma) section added to AGENTS.md (`fbdb90638`)
- `salve-munde.fab` example program (`e482faf0c`)
- Compilation error fixes for first successful full build (`818670f29`)

### Other changes

- Normalize table formatting in rivus CHECKLIST (`ead65f3d2`)
- Update AGENTS.md (`dc0e10b02`)
- Update rivus CHECKLIST to reflect actual implementation status
  (`3992135b0`, `f1b11e3d5`)
- Trials results data commits (`b21e3c769`, `a2c0cf514`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
