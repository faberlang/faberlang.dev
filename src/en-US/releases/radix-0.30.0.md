+++
title = "Radix 0.30.0"
section = "releases"
order = 70
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.30.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

Dense 4-day release spanning **74 non-merge commits** that introduces the Rust-based recursive descent compiler skeleton (`radix-rs`), wires a full HIR lowering pipeline, adds bidirectional type inference and borrow analysis, migrates loop and import syntax across all backends, prunes legacy compilers, and adds faber/glyph serialization targets.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 74 |
| Date span | 2026-01-26 → 2026-01-29 |

### Major tracks

#### Rust compiler skeleton (`radix-rs`)

The initial **Rust-based recursive descent compiler** for Faber — 46 files, ~8800 lines — replacing the old TypeScript compiler as the primary implementation.

- Add Rust-based recursive descent compiler skeleton with lexer, parser (precedence climbing), full AST (1123 lines), HIR, 6-pass semantic architecture, codegen (Rust + Faber targets), ariadne-backed diagnostics, and CLI (`lex`/`parse`/`check`/`emit` commands) (`c8bc7f29`)
- Complete lexer with full token support using scanner/cursor pattern (`58adcb0c`)
- Implement 3-mode lexer with independent keyword namespaces (Normal, Annotation `@`, Section `§`) — mode resets on newline, enabling the same word to have different meanings per context (`9a789a00`)
- Add `\uNNNN` Unicode escape sequence handling in the lexer (`def0bd8a`)
- Wire diagnostics catalog with parsing fixes (`b32a3e50`)
- Add `Cargo.lock` (`327a253c`)

#### HIR lowering pipeline

A strict, explicit lowering phase from AST to HIR, with diagnostics and entry handling.

- Wire HIR lowering pipeline — explicit phase with lowering for decls, expressions, statements, patterns, and types (`6b4a4e63`)
- Lower locals and types — integrates lowering into the driver and semantic pipeline (`55a82f17`)
- Lower control structures — `si`/`dum`/`itera`/`elige`/`discerne` and basic pattern handling (`598d72b0`)
- Add destructuring bindings and extract (`a74226c0`)
- Attach annotations to statements (`a1ae0321`)

#### Semantic analysis passes

Six-pass semantic architecture with bidirectional type inference, borrow analysis, exhaustiveness checking, and linting.

- Add bidirectional type inference — 697-line typecheck pass with 555 insertions, enabling constraint-based inference (`992a1d35`)
- Implement collect and resolve — name collection and multi-stage name resolution (1101 lines of new code) (`a2aaef49`)
- Validate types and variants during resolution — 468 lines of enhanced checking in the resolve pass (`6a394a18`)
- Implement semantic exhaustiveness and lint — large commit adding exhaustive pattern checking (415 lines), lint warnings (359 lines), and deep typecheck integration (1279 lines) (`abe48807`)
- Add borrow analysis — 636-line borrow checker pass (`2fd8eb5f`)
- Make shadowing an error (`f7ce89a6`)
- Enhance lint warnings (`74234789`)
- Warn on unnecessary `qua` casts (`92793527`)
- Migrate `expressia()` to `synthesize()`/`check()` pattern (`94835d21`)

#### Parser: expressions, patterns, and keyword refinement

Extensive parser work for expression and pattern grammar, along with Latin keyword naming cleanup.

- Implement closure expression parsing (`6263616d`)
- Add builtin expression parsing — `scriptum`, `lege`, `praefixum` (comptime) (`46ffc3df`)
- Add `sic`/`secus` ternary expression parsing (`7089896c`)
- Add `ergo` keyword for inline statement blocks (`63d100c2`)
- Add path patterns in match arms (`3a4728ef`)
- Add `fixum`/`varia` pattern bindings (`2018b68c`)
- Allow template literal patterns (`85121dc9`)
- Use lookahead for variable declaration type detection (`543ff62d`)
- Use lookahead for `cura` resource binding type detection (`f8298541`)
- Clarify `praefixum` as comptime expression, add sed regex parsing (`4a7a1c67`)
- Latinize keyword-mapped nodes (`7dd38b37`)
- Rename parser methods to use Latin Faber keywords (`f0991f0d`)
- Support anonymous `cura` "arena" scope without binding (`18b65701`)
- Warn on `cura` "arena" for Rust codegen (`431c7885`)

#### Codegen: faber and glyph serialization targets

Two new rivus codegen targets for pure AST-to-text serialization (~4700 lines total):

- **Faber target**: pretty-printer emitting canonical Faber source with indentation tracking — handles all 30 expression types and 35 statement types (`a49882bc`)
- **Glyph target**: Unicode glyph representation per the glyph specification — complete mapping tables for keywords, operators, delimiters, and braille (`a49882bc`)
- Fix build errors in faber and glyph targets (`48a1dd98`)
- Add glyph build script (`0fc878aa`)

#### Rivus (TypeScript codegen) fixes

- Fix type system and codegen from epic #291 (`b9d53f52`)
- Correct TS codegen for norma imports and `tabula` type (`4644d3a7`)
- Rename fields to avoid Python reserved words (`a559fe33`)
- Escape backticks and dollar signs in `scriptum` output (`e5b50431`)
- Update all loops to `itera` syntax per issue #305 (`b5c8f161`)
- Convert import syntax to verb-first format (`fa80e8de`)

#### Nanus (Python/Go/Rust/TS codegen) fixes

- Multiple Python codegen fixes (`85cc75e5`)
- Implement `itera` keyword for loops across all four nanus backends (`993dca8a`, `bb461283`, `4c66b365`, `55a3f25e`)
- Implement new import syntax across all four nanus backends (`0d6e74a2`, `0c9fde19`, `be48092e`, `462cbc35`)
- Accept `itera pro` with unsupported error in nanus (`7dba36b4`)

#### Iterator range syntax: `itera pro`

- Add EBNF grammar for `itera pro` range iteration (`02f62724`)
- Add `itera pro` range mode and fix `sin` else-if parsing (`fb222c9f`)
- Rivus: add `itera pro` for range iteration per issue #307 (`a30a1cd5`)

#### Loop syntax migration (issue #305)

Standardized loop syntax from bare `ex`/`de` to the `itera ex`/`itera de` keyword-prefixed form across all backends.

- Rivus: add `itera` keyword to parser (`9a0826b2`)
- Rivus: update all loops to `itera` syntax (`b5c8f161`)
- Docs: update loop syntax to `itera ex/de` per issue #305 (`c04e7310`)
- All four nanus backends: implement `itera` keyword for loops (`993dca8a`–`55a3f25e`)

#### Import syntax migration (issue #304)

Converted import syntax to verb-first format across all compilers.

- Docs: update import syntax examples to new format (`9cbe5e20`)
- Rivus: implement new import syntax per issue #304 (`f83520ac`)
- Rivus: convert import syntax to verb-first format (`fa80e8de`)
- All four nanus backends: implement new import syntax (`0d6e74a2`–`462cbc35`)

#### Compiler pruning and cleanup

- Remove `glyph-go` standalone compiler (`3919877d`)
- Remove `faber-ts` compiler and all references (`8055e015`)
- Remove `figendum`/`variandum` async binding sugar (`77be8010`)
- Remove `&&`/`||` support from nanus-go/py lexers and core per issue #308 (`64eb6db6`, `262cb24f`)

#### Build and CI

- Add `-t`/`--target` flag to filter compilers in rivus build (`04999859`)
- Add Python syntax check to `build-rivus` (`5eb431aa`)
- Simplify CI to single `bun run build` command (`8f5a32a1`)
- Simplify compiler output naming (`f3e65e9c`)
- Simplify `nonnihil` + `longitudo()` checks to `nonnulla` (`76c6620e`)

#### AST and core refactors

- Replace nullable lists with empty lists per issue #310 (`37be5f6e`)

#### Standard library

- Add Python implementation of the standard library (`norma-py`) (`31bfc80d`)

#### Documentation

- Add `omnia` modifier to `discerneStmt` for exhaustiveness in EBNF (`bc8cb334`)
- Update loop syntax docs per issue #305 (`c04e7310`)
- Update import syntax examples (`9cbe5e20`)
- Move `demos/` to `docs/` (`0a74622e`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
