+++
title = "Radix 0.24.0"
section = "releases"
order = 73
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.24.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

This release overhauls the CLI annotation system from single-command to
multi-option support, adds typed lambda parameters and array destructuring,
improves semantic error diagnostics, and refactors the Rivus compiler AST into
a modular structure.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 36 |
| Date span | 2026-01-15 → 2026-01-16 |

### Major tracks

#### CLI system redesign (`@optio` → `@argumenta`, multi-option, `--help`)

The CLI annotation grammar was redesigned and expanded. `@optio` annotations
now accept structured options with named arguments, `--help` generation, and
support for both `@imperium` functions and `incipiet` (async) entry points.
The binding was later renamed from `@optio` to `@argumenta` for clarity.

- Implement single-command CLI mode with `@optio` and `@operandus` (`82385f8e`)
- Redesign `@optio` annotation grammar (`ad921cc6`)
- Support CLI annotations on `incipiet` (async entry point) (`607546d8f`)
- Support `@optio` and `@descriptio` on `@imperium` functions (`4f51a7432`)
- Add comprehensive CLI options to all commands (`685cd6025`)
- Rename CLI binding from `@optio` to `@argumenta` (`6feeb139f`)
- Extract shared CLI utilities and standardize idioms (`1887811b0`)
- Add `--help` support for leaf commands with options (`b54a1d404`)
- Require string literals for `@optio` and `@operandus` names (`3998b94f0`)
- Implement basic directory listing (`ls`) with options (`372e01d41`)
- Fix: use project root for build output paths (`33bd01fc9`)
- Fix: run semantic analysis on dependencies before codegen (`65164bb55`)
- Add `wc.fab` example demonstrating multi-option CLI (`1308f484a`)
- Document single-command CLI mode (`b6ed05f6e`)

#### Parser and semantic diagnostics

- Support array destructuring in for-of loops (`4831e1ed5`)
- Show file:line for parse errors in imported modules (`103dba8d1`)
- Include file path in semantic errors (`3de4842a7`)
- Add `iacit`/`moritor` support to `custodi` clauses (`3dd477b0a`)
- Add `§` (section) annotations for build configuration (`e3da279a7`)
- Make `futura` a contextual keyword (`0da4d514a`)

#### Rivus compiler (TypeScript) refactoring

- Split `parser/ast.ts` into a modular file structure (`ecd15ad68`)
- Stabilize `discretio` and method tagging (`25ec2be77`)
- Emit `discretio` variants as standalone TS types (`9a0c532ed`)
- Rename `LambdaCorpus.Expressia` variant to `Expr` to avoid collision (`5bf60dfbe`)
- Tighten rivus AST unions (`ca7d270f7`)

#### HAL (Hardware Abstraction Layer)

- Redesign `processus` API for portable subprocess spawning (`6588dc2ef`)
- Add `Status` genus and `status()`/`legeVinculum()` to `solum` HAL (`3e99c61e1`)
- Update test expectations for HAL module syntax (`3333ca3f1`)

#### Language features

- Support typed parameters in lambda expressions (`b15c8f835`)

### Other changes

- Add comprehensive design critique (`consilia/you-suck.md`) and response
  (`consilia/you-suck-feedback.md`) documenting known compiler issues
  (`a78776fe4`, `8bfddae0e`)
- Create then remove obsolete `fabh-headers.md` proposal (`07aacdad9`,
  `33ac0f079`)
- Update `.gitignore` for build artifacts (`fed07ec53`, `a8237f6f4`)
- Fix function declaration parser in `declara.fab` (`3c06e70cd`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
