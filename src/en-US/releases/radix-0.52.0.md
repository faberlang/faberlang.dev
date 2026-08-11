+++
title = "Radix 0.52.0"
section = "releases"
order = 48
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.52.0 |
| **Tag** | `radix-v0.52.0` |
| **GitHub** | [radix-v0.52.0](https://github.com/faberlang/releases/releases/tag/radix-v0.52.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.52.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.52.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.52.0/radix-v0.52.0-aarch64-apple-darwin.tar.gz) | 1.8 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.52.0/radix-v0.52.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.52.0/radix-v0.52.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.52.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

Tensor types, sized numeric primitives, and a v1 runtime shell land as the
centerpiece, alongside a compiler-wide production function naming policy and
several refactors that tighten the stepper containment boundary.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 15 |
| Date span | 2026-06-27 (single day) |

### Major tracks

#### Tensor and sized numeric types (factory stages 1–6)

Six-stage factory campaign adding tensor types and width-parameterised numeric
primitives to the compiler, runtime, and exempla suite.

- **Stage 1 — Spec merge** (EBNF for tensor declarations, target-capability
  matrix, factory ledger/plan docs) (`4935b29a7`)
- **Stage 2 — Sized numerus/fractus primitives**: new `NumericWidth` type
  hierarchy, `sized-numerus` and `sized-family-error` exempla, codegen types
  across Rust/TS/Go/Faber emit surfaces (`4f948074f`)
- **Stage 3 — Conversio width unify**: HIR lowering and Rust codegen for
  conversions between sized numeric widths, plus typecheck conversion rules
  (`dc6c2a778`)
- **Stage 4 — Tensor type shell and target reject**: HIR/MIR lowering for the
  tensor type, MIR validate/reject for unsupported targets, exemplum
  `tensor/decl.fab` (`38c519ff7`)
- **Stage 5 — Tensor runtime and v1 intrinsics**: `faber::tensor` runtime
  module in `crates/faber`, intrinsics registry entries (`tensor`,
  `tensor_shape`, `tensor_rank`), parser and typecheck support for tensor
  intrinsic calls, exemplum `tensor/shape.fab` (`deb165d19`)
- **Stage 6 — Closeout tests, exempla, and gate verification**: tensor goal
  gate in semantic pass, Rust codegen tensor tests, convert/types integration
  tests, tensor exempla registered in `index.toml` (`3d39a4526`)

#### Radix function naming policy (RFN-000–RFN-008)

Mechanical renames across the entire compiler codebase — codegen for
Rust/TS/Go/Faber, HIR/MIR lowering, semantic passes — to enforce a consistent
production function naming convention. Includes a Python audit script
(`scripta/audit-radix-fn-naming.py`) and documented policy in
`docs/compiler-engineering-rules.md` (`879058689`).

### Other changes

- **Host trait containment**: route `processus.{lege,scribe,sedes,muta}` and
  `identitas.pid` through the `Host` trait. `StdioHost` wraps real process
  env/cwd; `BufferHost` uses an in-memory sandbox so test and exempla runs
  never touch the real process environment. Drops five `std::env/std::process`
  call sites from the stepper (`fb7407c69`)
- **Stepper visibility tightening**: Frame struct field visibility reduced from
  `pub` to private; dead `_trap_preserves_span` function removed from scena
  (`91fa9d56a`)
- **Hoist duplicate pattern helpers**: three pattern-matching helpers
  (`pattern_variant_id`, `is_catchall_pattern`, `is_null_literal_pattern`)
  lifted from nested local copies to module-level free functions in the
  exhaustive pass (`3c41f7611`)
- **FRN naming completion**: rename six remaining `*_faber_value*` codegen
  helpers to `*_dynamic_valor*` to match the runtime type they describe.
  The case-sensitive FRN grep gate missed the snake_case residue
  (`10ab08dec`)
- **Naming ledger tidying**: drop stale `#[allow(dead_code)]` on
  `MirNames::value`; clarify `NameCatalog::iter` doc comment (`068fdc754`)
- **Fix omnia mixed-arm catchall evasion (DEFER-028)**: the omnia catchall
  detection used `all()` instead of `any()`, letting a mixed arm like
  `casu A, _` slip through unflagged. Fix the quantifier and add a regression
  test (`1faba7e75`)
- **`.gitignore` guardrail**: add `/*.rs` to block accidental root-level
  Rust emit artifacts from `faber emit` (`24fc5e1a1`)
- **Doc corrections**: add missing `ex.series` method to census-types plan;
  fix banned colon-type syntax and missing `ignotum` assignability in clavis
  goal docs (`b03d644a5`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
