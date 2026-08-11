+++
title = "Radix 0.64.0"
section = "releases"
order = 36
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.64.0 |
| **Tag** | `radix-v0.64.0` |
| **GitHub** | [radix-v0.64.0](https://github.com/faberlang/releases/releases/tag/radix-v0.64.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.64.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.64.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.64.0/radix-v0.64.0-aarch64-apple-darwin.tar.gz) | 2.0 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.64.0/radix-v0.64.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.64.0/radix-v0.64.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.64.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

A dense single-day release shipping **live sermo directional views**
(`meus<T>`/`tuus<T>`), the **tuus cursor Phase 2 escape analysis**, **radix type parameter domains**, the full **`sparsa` sparse tensor type** through
Phase G (docs/exempla), and the **legacy ad syntax removal** clean break.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 51 |
| `feat(...)` commits | 2 |
| `fix(...)` commits | 10 |
| Date span | 2026-07-01 |

### Major tracks

#### Live sermo directional views (`meus<T>` / `tuus<T>`)

- Ship `meus<T>` and `tuus<T>` as shared-conversation runtime views with
  `da`/`accipe`/`cursor`/`exhauri`/`fini`. Demote `meus`/`tuus` from lexer
  keywords to type names. Wire compiler typecheck and Rust lowering to
  `faber::frame` carriers. Add canonical exempla and updated frame-stream
  design docs. (`93dc76fe0`)
- Retain tuus terminal status on accipe/cursor drain; make `tuus_cursor` a
  lazy iterator with per-frame for-loop codegen. (`202a977f0`)
- Borrow directional view receivers and fix accipe scrinium data emit so
  chained calls compile. (`3fda96adc`)
- Resolve frame builtins by `DefId` not `NameCatalog` for reliable type
  rendering and view dispatch. (`ec7a52fd8`)

#### Tuus cursor values (Phase 2 escape diagnostics)

- Ship Phase 1 local bind and lazy bound iteration via `TuusCursor` metadata
  and `generate_local` hook. Reject unsupported cursor escapes (params,
  returns, copy, reassignment, conversio) in semantic analysis before codegen
  can eager-drain. (`0e509487d`, `64c7d6eca`)
- Rewrite the escape pass on `HirVisitor` with parent-context stack, fixing
  traversal holes in Array/Tuple/Binary operands, `nota`/`lista` entries,
  and array literals. Allow `tuus.cursor()` in `IteraSource` for direct
  `itera ex` loops. (`99b58429f`, `4cd3c61c0`)
- Close the live cursor factory goal with ledger and delivery spec
  bookkeeping. (`399667483`, `fcf58a19b`, `337a8a2a8`)

#### Type parameter domains

- Implement the `radix` type parameter domains system: parser syntax for
  domain annotations on generic parameters, HIR lowering, typecheck
  unification, and Rust codegen support. Add `solum-lege-generic` exemplar.
  Lock architecture decisions and refine annotation syntax in design docs.
  (`18064f65d`, `cda2e0ade`, `67aa915b8`)

#### `sparsa` — sparse tensor type (Phases A–G)

- **Phase A:** Design docs and EBNF grammar surface for `sparsa<T, Figura>`
  as a sibling sparse tensor type with omitted-coordinates-equal-zero
  semantics. (`8b20b902d`)
- **Phase B:** Parser recognition (`TypeExprKind::Sparsa`), semantic
  `Type::Sparsa` variant, exhaustiveness across all IR/codegen/MIR/forma
  arms, and numeric-only v1 enforcement. (`df581ffc3`)
- **Phase C:** Runtime core — `faber::Sparsa<T>` with `vacua`, `accipe`,
  `ponde`, `nonnihil`, `densata` and 17 unit tests. (`d37b1d2f0`)
- **Phase D:** Intrinsic registration (`IntrinsicReceiver::Sparsa` with 6
  methods), Rust codegen (real `faber::Sparsa<T>` emit), typecheck routing,
  and vacua literal resolution. (`878ec7ab4`, `1f98eb0ae`)
- Fix 4 bugs: sparsa equality arm, vacua typecheck acceptance, densata
  zero-dim coordinate generation, and Go/TS fail-closed rejection.
  (`77adc5128`)
- Tighten shape plumbing: extract standalone `codegen/rust/expr/call/sparsa.rs`
  module. (`bb9b214fb`); polish runtime lowering. (`31a32bc3d`)
- **Phase E:** Numeric type sugar (`sf32`, `si64[N]`) for sparsa shorthand.
  (`a12b1b73c`)
- **Phase F:** Conversio coverage — typecheck conversion rules and Rust
  codegen for sparsa->tensor and tensor->sparsar conversions.
  (`8ba98158b`, `73539bbaa`)
- **Phase G:** Exempla docs — full corpus fixtures (decl, access, conversio,
  sugar, rejection cases) wired into the e2e test matrix for Rust, Go, TS,
  Sexp, and Wasm. (`9e50d4d14`)
- Sparse tensor follow-up plan refined. (`33051ffd1`)

#### Legacy ad syntax removal

- Hard-error statement-level ad, block `meus`/`tuus` arms, and `emitte` at
  parse time. Delete legacy HIR/MIR/codegen paths (provider stmt lowering,
  `__faber_ad` shim) and block-only frame runtime helpers. Retire five legacy
  exempla fixtures; add `scripta/check-exempla-ad-canonical` guardrail.
  (`97380f7b1`, `a09a426a5`)

### Other changes

- Document `morphologia` verb tense families in design docs and open cleanup
  goal. (`f80f265af`, `f5e226581`)
- Add core stdlib campaign document (300-line CAMPAIGN.md). (`6abc5e10f`)
- Document return and error channels in README. (`0c5962822`)
- Refresh README against current Faber surface; label unsupported snippets
  and pair them with canonical form references. (`27fd3a39f`, `8ba8ce3f4`,
  `e0c800486`)
- Reset stale legacy-from-faber-www website contents (18,894 lines removed).
  (`e9a7321e1`)
- Raise expect budget in faber hygiene ratchet to 10. (`9fea98da9`)
- Lint fixes from clippy and formatting fixes from foreign session.
  (`98fc7bcf0`, `4e14db5c5`, `3f4b371f2`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
