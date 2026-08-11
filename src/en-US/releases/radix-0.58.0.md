+++
title = "Radix 0.58.0"
section = "releases"
order = 42
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.58.0 |
| **Tag** | `radix-v0.58.0` |
| **GitHub** | [radix-v0.58.0](https://github.com/faberlang/releases/releases/tag/radix-v0.58.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.58.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.58.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.58.0/radix-v0.58.0-aarch64-apple-darwin.tar.gz) | 1.9 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.58.0/radix-v0.58.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.58.0/radix-v0.58.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.58.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

Minor release spanning **24 non-merge commits** (`v0.57.0..v0.58.0`).
Introduces the `intervallum<T>` range primitive through its full Commit A–C
sequence: construction, conversio clamp, materialization, algebra, instans
bounds, and cross-stack type-system integration. Alongside the range work,
exact-type equality reaches Commit C, scalar text ordering closes the
comparison-gaps factory track, and the AI/ML foundation docs are restructured
around `indexed-types`.

### Scale
| Signal | Count |
| --- | ---: |
| Commits (no merges) | 24 |
| Date span | 2026-06-28 (single day) |

### Major tracks

#### `intervallum<T>` range primitive (Commit A–C)

- **Commit A — type and construction:** HIR `Intervallum` type node, parser
  grammar for half-open (`‥`) and inclusive (`…` / `usque`) range expressions,
  typecheck pass (`intervallum.rs`), codegen stubs across Rust/Go/TS/Faber,
  codegen refactor of iteration control to consume the new range IR, and
  `faber::Intervallum<T>` runtime carrier with `longitudo` and iterator traits.
  (`b8bdb4f81`)

- **Commit B — conversio clamp, materialize, continet:** Parser expands to
  `↦` conversio targets: `intervallum` → `numerus` (clamp), `intervallum` →
  `lista<T>` (materialize), `intervallum` → `intervallum` (range-to-range
  clamp). Intrinsic `continet` (point containment → `bivalens`). HIR nodes for
  clamp/conversio/materia, MIR lowering, all four codegen backends. Exempla
  corpus `intervallum/conversio.fab`. (`67e159921`)

- **Materialize to 1-d tensor:** Extends the materialize path (`intervallum ↦
  tensor<T>`) producing a 1-dimensional tensor from range bounds. Rust codegen
  and typecheck conversions, exempla and test coverage. (`2f035d853`)

- **Commit C — range algebra, instans bounds:** Intersection (`inter`) and union
  (`union`) intrinsics with inclusivity-propagating semantics (half-open
  preserves half-open, inclusive union requires both operands inclusive).
  `instans` (datetime) bound support in addition to `numerus`. Infallible clamp
  adjacent to fallible `inter`/`union` (return `nihil` on disjoint/gap).
  `faber::Instans` carrier hooks. Full intrinsic registry entries and design doc
  `docs/design/intervallum-intrinsics.md`. (`243d8424a`)

- **Docs:** Proposed range type renamed from placeholder to `intervallum<T>`
  across factory goals, comparison-operators design, and corda/conversio
  docs. (`371230541`)

- **Stage 1 ledger and probes:** 10 probe files covering iteration, inclusivity
  variants, binding inference, type rejection, reverse iteration, and textus
  slice-index. Ledger tracks each probe against the stage gates.
  (`a5a2edea3`)

#### Exact-type equality (Commit B–C)

- **Commit B — exact-type equality:** `equality_exact_types_test.rs` matrix (133
  lines) exercising equality across exact numeric and text types, separate from
  the widened `convert` test surface. Typecheck ops extended with exact-type
  guards. (`37594e2ae`)

- **Commit C fallout closeout:** Driver `mod_test`, convert tests, comparison
  design, and `instans-intrinsics.md` updated for exact-type equality semantics.
  Ledger SHA anchors for Commit B/C. (`6ca197fbc`, `6360fef2a`)

- **Polish:** Extracted shared `infer.rs` equality helpers from `ops.rs`;
  factored `convert_test.rs` matrix into the dedicated test module.
  (`64d904bbd`, `b1afd9408`)

#### Scalar text ordering (comparison-gaps closeout)

- **Faber runtime:** `textus` scalar `cmp` helper and matching test coverage.
  (`66667fa22`)

- **Typecheck and codegen:** Scalar text ordering typecheck probes and inference
  rules; Rust codegen emits `Ord::cmp` / `PartialOrd::partial_cmp` for text
  types. (`13dad17e3`, `751b0533c`)

- **Chorda library:** Interval helpers refactored with a shared
  `_filtra_intervallo` walk across `chorda.fab`. (`6505f7541`)

- **Docs:** Comparison operators and chorda-methods design docs finalized;
  comparison-gaps factory ledger closed. (`4c6ce7e3a`, `57923d76e`,
  `5e4819384`)

#### AI/ML, AIR, and indexed-types foundation (design docs)

- **AI/ML lane scope:** Three factory goals drafted — `frame-valor-payload`
  (Valor tensor frame payloads), `cuda-kernel-emit` (GPU kernel emission), and
  `static-shape-foundation` (shape system). (`30b73108a`)

- **AIR charter narrowed:** `air-dialect.md` scoped under static-shape
  constraints; cross-linked with CUDA and AI/ML lane goals. (`ebafdd96c`)

- **AirProgram node model:** `air-representation/goal.md` defining the AIR node
  tree as an extension of the HIR under static-shape restrictions.
  (`3766c35e8`)

- **Static-shape → indexed-types generalization:** The static-shape foundation
  doc is subsumed by `indexed-types-foundation/goal.md`, expanding the model
  from shapes to a general indexed-container abstraction. (`944c91c24`)

- **Tensor as universal indexed container:** Indexed-types foundation reworked
  to treat tensor as the canonical indexed container with element-type
  relaxation. (`6b4f99069`)

- **Broadcasting stance:** AI/ML stack docs (aiml-foundation, air-dialect,
  tensor-intrinsics, CUDA, frame-valor-payload, indexed-types) aligned on a
  shared broadcasting model. (`b51b03a45`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
