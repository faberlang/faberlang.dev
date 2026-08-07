+++
title = "Radix 0.40.0"
section = "releases"
order = 59
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.40.0 |
| **Tag** | `radix-v0.40.0` |
| **GitHub** | [radix-v0.40.0](https://github.com/faberlang/releases/releases/tag/radix-v0.40.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.40.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.40.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.40.0/radix-v0.40.0-aarch64-apple-darwin.tar.gz) | 1.3 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.40.0/radix-v0.40.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.40.0/radix-v0.40.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.40.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

A wide-ranging polish and closeout release across three themes: intrinsic
function promotion from stdlib into the compiler, a single-session 344-commit
polish campaign covering the entire `crates/radix` surface, and closure of the
intrinsics innatum residue plan with a new shared intrinsic registry and CISTA
package manager implementation.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 382 |
| Date span | 2026-06-04 → 2026-06-22 |
| Files changed | 324 |
| Insertions | 12,851 |
| Deletions | 3,793 |

### Theme 1: Intrinsics R&D — Naming Policy, HAL Polish, and Core Promotion

The first half of the range is an R&D and preparation phase that establishes a
consistent stdlib intrinsics architecture.

#### Stdlib API naming policy

A series of decision records codified the naming conventions for compiler-owned
intrinsic methods:

- `6236680e9` — intrinsics API curation policy (what qualifies as a compiler intrinsic)
- `12a87f660` — inventory of stdlib API naming cleanup candidates
- `a9255d489` — prefer `ne` predicates in stdlib naming
- `3dd579fa9` — replace `ut` conversions with glyph syntax
- `aa3bb0290` — clarify codec naming cleanup
- `428c5d815` — explore and reject codec conversion chains
- `a9084f1a2` — stdlib morphology consistency policy
- `5115e6ee6` — async morphology renames

#### HAL crate polish

Seven `crates/norma/hal` modules received targeted cleanup:

| Module | Commit | Focus |
| --- | --- | ---: |
| aleator | `68fff394c` | State locking hygiene |
| arca | `7fa7fe93a` | Encoding simplification (82→41 lines) |
| consolum | `de68fbda7` | Write path cleanup |
| http | `4d1414fe8` | Header snapshot stability |
| solum | `50972c1f3` | Metadata tidying |
| tempus | `3862c12d9` | Clock fallback polish |
| aleator tests | `0643bd5db` | Test stabilization |

#### Intrinsic promotion into the compiler

Five stdlib `innatum/` modules were promoted from runtime Faber source to
compiler-owned intrinsics with matching MIR nodes, typecheck rules, and
multi-target codegen. Each promotion deletes the stdlib definition and adds
a design doc, exempla fixtures, and cross-target test coverage.

| Intrinsic family | Commit | Files | Insertions | Deletions |
| --- | --- | ---: | ---: | ---: |
| **lista** (list methods) | `3166f4925` | 9 | 244 | 531 |
| **tabula** (map methods) | `881a91a90` | 12 | 318 | 214 |
| **copia** (copy/clone) | `dfe91e611` | 18 | 608 | 181 |
| **textus** (text methods) | `30b1d07f1` | 19 | 683 | 152 |
| **numerus + fractus** (numeric) | `f3e1756ec` | 23 | 664 | 146 |

A mixed-case tabula intrinsic was also demoted (`c656b1839`).

### Theme 2: Radix Polish Campaign (8 Stages)

A single 7-hour session (`83b1e42a1` → `22e67460f`, 344 commits) executed an
8-stage polish campaign across the entire `crates/radix` tree. Every stage
includes both implementation commits and companion docs commits recording
inspection findings.

| Stage | Scope | Key examples | Merge gate |
| ---: | --- | --- | ---: |
| **0** | Diagnostics, lexer, syntax | catalog, diagnostic render, token format, cursor, keywords, scan tests, span, visit | `a7e53c60d` |
| **1** | Parser, HIR nodes | parser/types, parser/pattern, parser/stmt, parser/expr, parser/decl, hir/nodes | `482b91df8` |
| **2** | HIR lowering, semantic, typecheck | hir/lower (types, pattern, expr, stmt, decl, mod), semantic (types, scope, error, resolve, borrow, exhaustive, lint, collect), typecheck (collect, infer, finalize, pattern, access, expr, item, aggregate, control, ops, call) | `89e449740` |
| **3** | MIR | mir/nodes, mir/dump, mir/visit, mir/validate, mir/lower (context, place, aggregate, control, collection_higher_order), mir/lower_test, mir/visit_test | `f9513f952` |
| **4** | Codegen base + Faber backend | codegen/writer, codegen/names, faber (types, literal, pattern, ops, expr, stmt, decl, mod) | `d9142fbdc` |
| **5** | TypeScript + Go backends | ts/types, ts/decl, ts/stmt, ts/expr, ts/mod, ts/tests; go/types, go/mod, go/decl, go/stmt, go/expr (mod, access, call, collection, control, convert, literal, ops, option, variants), go/tests | `1a4cb6dc3` |
| **6** | Rust codegen, tests, driver | rust/mod, rust/cli, rust/decl, rust/stmt, rust/prelude, rust/expr (mod, access, block, convert, format, literal, ops, option, pattern, collection, call, call_args, call_stdlib, control, branch, iteration, match), rust/tests (ad, call, collection, declaration, dynamic, failable, http, optional, type), driver (source, session, module, compile) | `64a55fe52` |
| **7** | Tooling CLI, exempla E2E, final lint | radix binary, tool commands (check, compile, emit, inspect, json, package, postprocess, source, targets), CLI tests, exempla e2e helpers, LLVM/Go/TS/Rust/wasm exempla harnesses, wasm behavior fixtures, final lint findings | `53254cb44` |

#### Campaign structure

Each stage follows the campaign protocol defined in `docs/campaigns/radix-polish-pass.md`:
per-file inventory, doc-recorded inspection, polish commit, test gate, and merge
documentation. Stage 7 alone covers every `radix` CLI subcommand and all four
codegen backends' exempla E2E harnesses.

Notable individual changes within the campaign:

- `8efb57cc9` — Split intrinsic exempla by method group for isolated testing
- `0ec6e9751` — Use debug formatting for Rust template composites
- `2996e698c` — Clean Faber exemplar language
- `4c8679a10` — Correct semantic types test ledger
- `f726c835f` — Resolve type names through type namespace
- `c80825445` — Plan intrinsics innatum residue cleanup (bridges to Theme 3)

### Theme 3: CISTA Package Manager + Intrinsics Residue Closure

The final 13 commits (`a73b37b92` → `99c922691`) close both the campaign and the
intrinsics residue plan.

#### CISTA package manager

- `a73b37b92` — Remove completed radix polish campaign artifacts and stale handoffs
- `bf2a09a42` — Trim intrinsics residue plan around CISTA split
- `e2bed1702` — Revise CISTA package architecture goal
- `46dc7e212` — Add CISTA package crate skeleton
- `2c2ce25bf` — Document CISTA package sysroot goal
- `ab3aa445c` — Add mathesis CISTA source package fixture
- `ed7608b4a` — Clean up CISTA package store goal docs (rewrite goal doc, 683 lines)
- `147714f6d` — Implement CISTA package check (manifest validation)
- `4677c5e26` — Implement local CISTA install (397 insertions, CLI + commands + manifest)

#### Intrinsics innatum residue cleanup

- `b761f91d9` — Remove retired `@ innatum` and `§ innatum` from EBNF, delete
  unreachable structured stdlib annotation AST variants, rename Rust codegen
  receiver-method lowering from `stdlib` to `intrinsics`, move
  `exempla/innatum/` → `exempla/intrinseca/` (19 files, net −69 lines)
- `740092c30` — Decide tabula lowers to native map idioms per target
- `3e4b3e11e` — Lower TypeScript tabula to native `Map<K,V>` idioms (171-line
  rewrite: type annotations, constructors, literals, method calls, index ops)
- `9a15c285c` — Implement Go tabula intrinsic lowering to native `map[K]V`
  idioms (196 insertions: index assign, comma-ok pointer lookups, presence
  checks, length queries)
- `949c71557` — **Shared compiler-owned intrinsic registry.** New
  `crates/radix/src/intrinsics/` module with a single `MethodIntrinsic` catalog
  covering all six promoted families (lista, tabula, copia, textus, numerus,
  fractus). Semantic method-call checking and MIR `collect_method_op` now
  resolve through registry lookup instead of parallel string-match tables
  (9 files, 530 insertions, net +131 lines)
- `99c922691` — Complete intrinsics residue phase 7 sweep: fix Faber package
  annotation handling after the structured Verte/Subsidia AST prune, retire
  `@ innatum` from active boundary exemplar fixtures in favor of CISTA notes,
  and mark the full delivery plan complete with a residual ledger. All gates
  pass (`./scripta/test`, `./scripta/lint`, `cargo test -p radix`).

#### Deleted artifacts

The campaign close removed 13 handoff/session infrastructure files (2,629 lines)
including the campaign pass docs, handoff shell, session notes, and stale
template. The `handoffs/` directory is retired with this release.

---

[All releases](/releases/) · [Install the current release](/start/install.html)
