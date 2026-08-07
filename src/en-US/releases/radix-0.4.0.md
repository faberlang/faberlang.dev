+++
title = "Radix 0.4.0"
section = "releases"
order = 95
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.4.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

Major feature release spanning **120 commits** (`v0.3.0..v0.4.0`). Introduces
multi-language codegen targets (TypeScript, Python, Zig, Rust, WASM, C++), a
beginnings of a type system with genus/pactum/ordo, Latin keyword syntax for
control flow and error handling, an error catalog system, comprehensive
documentation, and reorganized project structure.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 120 |
| Date span | 2025-12-22 → 2025-12-24 |
| Test growth | 210 → 402 (+91%) |
| Codegen targets | 6 (TS, Py, Zig, Rust, WASM, C++) |
| New exempla files | 33 focused examples |

### Major tracks

#### Codegen: multi-target architecture

**Target-first codegen restructure** (`7d73a5d9e`). Each target gets its own
directory under `fons/codegen/` with a `norma/` subdirectory for stdlib method
translations. The codegen router dispatches by target type.

**Skeleton targets scafolded** for Python, Ruby, C++, and WASM alongside the
existing TypeScript and Zig targets (`30c418784`). Ruby is replaced by Rust
shortly after (`3f9eacae0`).

**Codegen target checklist** (`14c4d7baf`) provides a comprehensive feature
matrix tracking implementation status across all targets.

**Target design documents** created in `consilia/codegen/`:
- TypeScript design doc (`4a59d8da6`)
- Zig design doc (`4a59d8da6`)
- Rust design doc (`4a59d8da6`)
- Python codegen doc (`0f5120fea`)
- C++23 design doc (`0f5120fea`)

#### Type system: genus, pactum, ordo

**Genus (struct) system:**
- Genus instantiation with `novum` and `cum` overrides (`e26b33ce7`)
- Auto-merge constructor with `creo()` no-args post-init hook (`f42f733b2`)
- Field defaults use colon syntax (`7e4a5d1e2`)
- Auto-merge constructor documented (`a393e6513`)

**Ordo (enum):**
- Full enum implementation for TypeScript with numeric/string values and
  auto-increment (`fb1dc43f3`)

**Pactum (interface):**
- Clarified that pactum enforcement happens in the semantic analyzer at compile
  time, similar to TypeScript→JavaScript type erasure (`1fdb46339`)

**Lowercase type convention:**
- All type names now lowercase (textus, numerus, etc.), matching classical Latin
  which had no case distinction (`3f62c4b9d`)
- Tree-sitter grammar regenerated for lowercase types (`1f3937fa2`)

**New types:**
- `objectum` type for object literals (`908a780b9`, `2990dca59`)
- Numeric types documented: numerus (i64), fractus (f64), decimus (arbitrary
  precision) (`73c0565d3`, `429297abf`)
- `octeti` (bytes) primitive type for raw binary data (`249a4f99f`)
- Array shorthand syntax `T[]` desugars to `Lista<T>` (`6658f3b2d`)

**Type system removals:**
- Latin type modifiers removed (naturalis, proprius, alienus, mutabilis) in
  favor of size-parametrized numerus (`44ef54804`)

**Fixes:**
- `bivalens` nominative for 3rd declension lookup (`f1f0b6caf`)
- User-defined types in function parameters now parse correctly
  (`3158d20d0`)

#### Core language keywords and syntax

**Equality and comparison operators:**
- `est` for strict equality (`4be072e74`)
- `non est` for strict inequality (`1305c4e98`)
- `negativum` / `positivum` unary checks (`4be072e74`)

**Conditionals:**
- Ternary expression with `sic`/`secus` Latin keywords (`8597060a8`)
- `sin` keyword as alias for `aliter si` (`09870dc14`)
- `secus` keyword as alias for `aliter` (`7df54d8d9`)
- `elige` now emits `if/else` chains instead of `switch` (`0b37f643e`)
- `quando` keyword removed as redundant with elige→if/else (`e4a01d2a9`)

**Lambda and block syntax:**
- `fac` keyword for block scoping with error handling (`8ededfc17`,
  `1b7b58564`)
- Lambda syntax evolves: `fac x fit expr` → `pro x redde expr` (`84e93c211`)
- Block body support for lambda expressions (`e852bfe4a`)
- `fit` as Latin alias for return type arrow (`2b6fbe18b`)

**Control flow:**
- `rumpe`/`perge` (break/continue) implemented for TypeScript (`8195980ef`)
- `mori` (fatal/panic) distinct from `iace` (recoverable) (`946b013c0`)
- `vide` and `mone` output keywords for debug/warn levels (`0cac3b51c`)
- Verb conjugation on loop syntax: `ex items fit item` / `ex items fiet item`
  (`4713b8001`)

**Async and iteration:**
- Unified `cede` replaces `exspecta` for both await and yield (`66c640268`,
  `b01f386f1`)
- `cede ex` for yield delegation (`8f98ecf92`)
- Generator syntax: `cursor functio` / `fluxus functio` (`bc8b1c514`)
- Pipeline syntax: `ex...per...pro` for inline transformation chains
  (`1fc30d9e5`)
- Range expressions now inclusive on both ends (`395d9d4b4`)

**Events:**
- `emitte` keyword for event emission (`6f53f2ba1`)
- `ausculta` keyword for event stream subscription (`d2ad18de0`)

**Destructuring and ownership:**
- `ex...fixum/varia` destructuring syntax (`e9aedde8e`)
- `de`/`in` ownership prepositions for systems targets (`6405c2a80`)
- Scope-based arena syntax: `fac arena` replaces `cum arena` (`667e31617`)

**Verb conjugation system:**
- `cum` prefix pattern replaced with Latin verb conjugation that encodes
  mutability and async in verb forms (`71452a5de`)
- Verb conjugation documented for async/iterator semantics (`6eecf9aac`)

#### Error handling model

**Two-tier error model:** `iace` for recoverable errors, `mori` for fatal/panic
(`946b013c0`). `fac/cape` for block-level error handling with `demum` only
available on TS/Python targets (`1b7b58564`).

**Error catalog system** (`b7506fdf7`): Phase-prefixed error codes (P/S/L for
parser/semantic/lexer), structured error interfaces with code/text/help fields,
and comprehensive compiler-rules.md coding guidelines.

**Obsoleta:** Remove `fors<T>` result type — superseded by iace/mori/cape model
(`26ea529ac`).

#### Codegen target implementations

**TypeScript:**
- Collection method registries for lista (50+), tabula (17), copia (14)
  (`a9b723630`)
- Collection method dispatch using semantic type info (`3c6b46471`)
- Preamble infrastructure with feature tracking (`564ca4543`, `586787af7`)
- `nexum` (reactive binding) implementation (`0338fc490`)
- `figendum`/`variandum` async bindings and tempus stdlib (`d2744537f`)
- `ordo` (enum) implementation (`fb1dc43f3`)
- `privatus` keyword for private fields (`5d13cf9a9`)
- Preamble system design doc (`586787af7`)

**Python 3.10+:** Full codegen implementation including type mappings, all
statement/expression generators, 30 lista method translations, and 72 passing
tests (`c8085bb5e`).

**Zig:**
- OOP support: genus→struct, pactum→duck-typed doc, ego→self (`8a5885224`)
- Non-applicable features marked: generators, tempta/demum (`582e94b94`)
- Zig-specific target notes documented (`63b48ed24`)

**Rust:** Ruby target renamed to Rust with ownership/lifetime-aware generator
skeleton (`3f9eacae0`).

#### Ownership and memory design (Rust/Zig)

**Latin preposition-based ownership** (`40a61b1f6`): No preposition = owned,
`de` = borrowed (`&T`), `in` = mutable borrow (`&mut T`). Maps Rust ownership to
Latin grammatical cases.

**Lifetime design** (`c41390721`): `de` on return type ties to input lifetimes,
mirroring Rust's elision rules — no explicit lifetime names needed.

**Async/generator restriction** (`c4178ae3b`): Borrowed returns (`de`) only
allowed with `fit` (sync), not `fiet` (async), matching Rust's fundamental
constraint.

**Unified memory management:** Arena allocation as default strategy across both
Rust (bumpalo) and Zig (ArenaAllocator) (`5e44621a6`).

#### Collection DSL and stdlib

**Collection DSL:**
- Unary predicates documented (`ebab36bc6` — hash `ebabi36bc6`)
- Collection DSL and loops unified under `ex` syntax (`849311284`)
- Prefix operations with comma chaining (`1dcb05300`)
- Closure syntax design: three levels of expressiveness (`fdf81ab78`)
- Lodash-inspired methods: ordina, congrega, unica, plana, and many more
  (`570d7b6b7`)

**Stdlib skeleton types:** lista, tabula, copia, promissum (`d074c70f2`).

**Name collision resolution** across stdlib docs (`5298d0afe`): copia→duplica,
iunge→ws.aperi, ausculta→servi, intervallum→series, dele→erade.

#### Documentation

**Thesis:**
- Project purpose and lowercase convention rationale (`093819811`)
- "Code for a New Reader" section articulating word-over-symbol approach
  (`033034077`)

**Design docs created:**
- Types design: genus, pactum, syntax (`b222c856d`)
- Collections, async, and iteration (`ccddcaa6e`, `570d7b6b7`)
- Stdlib and binding design: caelum, tempus, solum, vincula (`7e7dd8938`)
- Event system: eventus.md (`6f53f2ba1`, `d2ad18de0`)
- File I/O: fasciculus.md (`dec77a89d`)
- Network, crypto, compression, encoding: caelum, crypto, comprimo, codex
  (`249a4f99f`)
- Resource management: cura.md (`249a4f99f`)
- Iteration implementation status (`7b31a17a9`, `6ec83af25`)
- Gap analysis: checklist vs consilia across ~190 features (`0f7036953`)
- Preamble system design (`586787af7`)
- Clausura design document (`84e93c211`)
- Codegen principles (`0b37f643e`)
- Project thesis rendering (`3c9179d4e`)

**Design consistency audit** (`615c7e277`): Range syntax, lambda syntax, `de`/`in`
ownership annotations, async gerundives, promise combinator naming.

**Vincula.md updated** to be sync/async agnostic (`35449828a`).

#### Project structure

- Stdlib moved from `fons/stdlib/` to `arca/` at project root (`9371c1010`)
- `consilia/` directory created for planning documents (`093819811`)
- Exempla reorganized into logical subdirectories with 33 focused files
  (`8a38e97f6`)
- `arca/` removed — outdated and superseded by codegen intrinsics
  (`99669c6d4`)
- Preamble checklist relocated to `consilia/codegen/` (`586787af7`)

#### Grammar and editor tooling

- Tree-sitter grammar synced with AST: ordo, genus, pactum, rumpe/perge, fac,
  emitte, ausculta, lambda, ternary (`623784a85`)
- Prettier printer synced with all AST node types (`623784a85`)
- `check:ast` script detects out-of-sync grammars (`e03fe65d4`)
- Prettier and tree-sitter test coverage (`005b89bfe`)

#### Compiler infrastructure

- Error catalog system with phase-prefixed codes (`b7506fdf7`)
- Semantic type checking for nulla/nonnulla, comparisons, and arrays
  (`b6b96cd12`)
- Type safety fixes: MemberExpression property type, lexicon data deduplication
  (`419e05fea`, `a29447e5b`)
- Formatting passes: codebase format, prettier, lint (`78d20e406`,
  `5d8dbb2ed`, `2ade016d9`)
- ESLint rules relaxed for generated exempla code (`4fc11685b`)
- Build script: always rebuild faber to avoid stale executable (`e852bfe4a`)

#### Test coverage

- 192 new tests across all compiler phases (210→402, +91%) (`d005dd80b`)
- Focus on edge cases, error recovery (28 malformed syntax tests), boundary
  values, and unicode
- 96.5% pass rate (388/402), 14 `.todo()` tests documenting known gaps
- All 42 exempla `.fab` files fixed to compile successfully (`f4ca48736`)

### Other changes

- Lambda syntax exempla updated for `pro` and inclusive ranges (`3e4948d19`)
- Errores.fab created, fac/cape content moved from clausura.fab (`57fb59514`)
- `format` script simplified to `.ts` only (`78d20e406`)
- Automatic formatter run on exempla and compiler source (`aa99b2c07`)
- Codegen style improvements: constructor braces, public-by-default fields
  (`5d13cf9a9`)

### Breaking / author-visible

| Change | Migration |
| --- | --- |
| `esto` replaced with `varia` for mutable bindings (`d60cebde9`) | Use `varia x = 5` instead of `esto x = 5` |
| `exspecta` replaced with `cede` for async await (`66c640268`) | Use `cede` instead of `exspecta` |
| Range expressions now inclusive on both ends (`395d9d4b4`) | `0..5` includes 5; update off-by-one assumptions |
| Lambda syntax changed: `pro x fit expr` → `pro x redde expr` (`84e93c211`) | Use `redde` instead of `fit` in lambda bodies |
| `elige` emits `if/else` chains, not `switch` (`0b37f643e`) | Output changes but semantics are equivalent |
| `quando` keyword removed (`e4a01d2a9`) | Use `si`/`elige` instead |
| Latin type modifiers removed (naturalis, proprius, alienus, mutabilis) (`44ef54804`) | Use `numerus<u32>` or `numerus<u64>` syntax |
| Lowercase type convention (`3f62c4b9d`) | All type names must be lowercase (textus, numerus, not Textus, Numerus) |
| `fac arena` syntax replaces `cum arena` for scope-based arenas (`667e31617`) | Use `fac arena { }` instead of `cum arena { }` |
| `de`/`in` ownership prepositions added (`6405c2a80`) | Parameter syntax may be affected on systems targets |
| `fors<T>` result type obsolete (`26ea529ac`) | Use iace/mori/cape error model instead |
| Stdlib moved from `fons/stdlib/` to `arca/` (`9371c1010`) | Import paths changed |
| Codegen restructured to target-first organization (`7d73a5d9e`) | Import paths for codegen changed |
| `cum` prefix replaced with verb conjugation (`71452a5de`) | Collection methods use conjugated verb forms |
| Field defaults use `:` not `=` (`7e4a5d1e2`) | Use `textus nomen: "Incognitus"` instead of `textus nomen = "Incognitus"` |
| Ruby target renamed to Rust (`3f9eacae0`) | Use `--target rs` instead of `--target rb` |

---

[All releases](/releases/) · [Install the current release](/start/install.html)
