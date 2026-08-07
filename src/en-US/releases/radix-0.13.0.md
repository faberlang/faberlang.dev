+++
title = "Radix 0.13.0"
section = "releases"
order = 86
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.13.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

Consolidates the workspace directory structure under a unified `fons/` tree,
introduces the **Rivus** bootstrap compiler (Faber compiler written in Faber
itself), adds the `reddit` keyword for concise early returns, and applies
readability refactorings across the bootstrap compiler source.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 31 |
| Date span | 2026-01-02 → 2026-01-02 |

### Major tracks

#### Directory restructuring: `fons/` consolidation

Collapses top-level directories into a unified `fons/` tree with clear naming:

- Moves `proba/` → `fons/proba/` (`88dc15158`)
- Moves `subsidia/` → `fons/subsidia/` (`168ab8ffd`)
- Moves `exempla/` → `fons/exempla/` (`ac6043b56`)
- Moves the bootstrap compiler source into `fons/proprius/` (`0754ca1dc`)
- Moves the original TypeScript compiler source into `fons/primus/` (`ac8b180d9`)
- Updates all script paths, import paths, and docs references for the new layout (`0e6851e3d`)
- Renames `fons/primus` → `fons/faber/` and `fons/proprius` → `fons/rivus/` with matching `package.json`, `AGENTS.md`, and `GRAMMAR.md` updates (`6e39b3b5f`)
- Clarifies Faber CLI vs Rivus CLI usage guidelines in `AGENTS.md` (`521165243`)

#### Rivus bootstrap compiler

Adds and stabilizes the bootstrap compiler — a Faber-to-TypeScript compiler
written in Faber itself:

- Adds the `rivus` CLI wrapper and `build-rivus` compilation script in `scripta/` (`666b9ffab`)
- Adds a dedicated test runner `proba/rivus.test.ts` that runs all tests through the bootstrap compiler (`2852ffaaf`)
- Fixes build and test paths: enables `globstar` to recurse subdirectories (was building 21/51 files), updates import paths and script references (`f95cdde6e`)
- Documents test commands and known parser infinite-loop issue (`42c797c6b`)
- Hardens Rivus tests and prevents parser hangs (`632586cc1`)

#### `reddit` keyword and parser/language evolution

Introduces concise early-return syntax across the language and builds out
operator capabilities:

- Adds the `reddit` keyword (Latin "it returns") as syntactic sugar for `ergo redde` — supports `si`/`sin`/`secus` conditionals, `dum`/`ex`/`de` loops, `elige`/`casu`/`ceterum` switches, `discerne` pattern matching, `custodi` guards, and `incipit`/`incipiet` entry points (`ae3f6b7d6`)
- Applies `reddit` syntax and cleans up resolved TODOs in `parser/nucleus.fab` (`8f98df27d`)
- Supports character range containment with the `intra` operator: `c intra "a".."z"` now works alongside the existing numeric operand support (`d3a236697`)
- Refactors lexor character checks to use the `intra` operator (`d76e65545`)
- Adds `Parser.locusActualis()` helper, replacing 60 occurrences of `p.specta(0).locus` (`32926020c`)

#### fons-fab code quality (inter operator, compound assignment, primus/ultimus)

Applies readability refactorings driven by operator capability research:

- Documents 24 valid `inter` operator candidates and 0 valid `intra` candidates across the bootstrap source (`ff3c51f65`)
- Applies the `inter` operator (set membership) at 24 sites in lexor, semantic, codegen, and parser modules — replaces `aut` chains with `x inter [a, b, c]` for a ~28% average code reduction (`3a2719ed3`)
- Replaces 25 instances of `x = x + 1` with compound assignments `x += 1`, `x -= 1` — syntax already supported but previously unused (`2bf347979`)
- Uses `primus()`/`ultimus()` for first/last element access (`fc2e2ea35`)

#### Codegen and semantic fixes

Aligns the bootstrap compiler's codegen and semantics with the current AST:

- Fixes genus instantiation: emits `new Genus({…})` instead of `({…} as Genus)` for object literal casts, preserving prototype methods (`8ccdf79fb`)
- Adds comment preservation scaffolding stubs (`formataNotaePrae`/`formataNotaePost`) for TS codegen (`a572154d2`)
- Lowers tabula bracket access to `Map.get`/`Map.set` in TypeScript output (`b92ef64b6`)
- Adds missing `@ publicum` annotations across Lexor, Parser, and Resolvitor — reduces TypeScript errors from 310 to 254 (`190c06d8e`)
- Aligns fons-fab field names (e.g. `AngulusSin/Dex` → `QuadratusSin/Dex`), replaces `tabula.habet()` with `nonnihil tabula[key]`, adds missing scope enter/exit, and fixes AST field name alignment (`ef1d25918`)
- Removes tabula method workarounds and updates discriminant names in bootstrap TS output (`061272089`)

#### Bootstrap compiler tracking

Marks progress toward full bootstrap self-compilation:

- Updates bootstrap tracking doc: Phase 0 complete, Phase 1 ready (`4d3a67898`)
- Marks import hoisting complete (`20b19ed21`)
- Declares Phase 1 complete with zero TypeScript errors (`04374f8ab`)

### Other changes

- Note coverage: Phase 0/1 tracking, known parser-infinite-loop issue, compound assignment adoption.

---

[All releases](/releases/) · [Install the current release](/start/install.html)
