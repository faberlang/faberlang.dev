+++
title = "Radix 0.57.0"
section = "releases"
order = 40
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.57.0 |
| **Tag** | `radix-v0.57.0` |
| **GitHub** | [radix-v0.57.0](https://github.com/faberlang/releases/releases/tag/radix-v0.57.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.57.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.57.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.57.0/radix-v0.57.0-aarch64-apple-darwin.tar.gz) | 1.9 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.57.0/radix-v0.57.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.57.0/radix-v0.57.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.57.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

Comparison gaps: scalar `textus`/`ascii` ordering through typecheck and Rust codegen,
chorda native interval filters that walk Unicode scalar bounds, and a dedicated
exact-type equality workstream split from the ordering matrix.

### Scale
| Signal | Count |
| --- | ---: |
| Commits (no merges) | 13 |
| Date span | 2026-06-28 → 2026-06-28 |

### Major tracks

- **Scalar text ordering** — typecheck single-scalar `textus`/`ascii` `<` `≤` `>` `≥` via literal, unit `sectio`, and unary-textus predicate parameters. Lower to `faber::unicode_scalar_value` in Rust codegen. Completes equality-exact-types Stage 1 ledger. (`77d679863`)
- **Chorda native interval filters** — replace `@ externa retine_intervallo`/`expurga_intervallo` with native Faber bodies that walk `sectio` scalars and compare inclusive Unicode scalar bounds. Retire Rust interval helpers from `crates/norma/chorda.rs`. Typechecker rejects multi-scalar bounds at call sites. (`186b17fef`)
- **Chorda cord-filter closeout** — land `scala`/`retine`/`expurga`/`residuum` native bodies plus externa-backed interval filters, `comprime`, `angustat`, `temptat`, and `discidit` in `stdlib/norma/chorda.fab`. Add exempla, norma unit tests, design-doc filter table, and factory closeout ledger. (`952b3bad8`)
- **Equality exact-types split** — new dedicated factory goal for exact-type equality (flow permissive, compare exact) with probe fixtures and ledger. Narrow `comparison-gaps` to ordering only; cross-link both workstreams in comparison-operators.md. (`4d62f3bed`)
- **Comparison-gaps goal and Stage 1 probes** — inventory equality vs ordering vs intra/inter contracts, chorda externa blockers, and candidate seams for scalar text order. Run 17 probe rows across `numerus`, `fractus`, `instans`, `textus`, `bivalens`, `octeti`, `lista` — including fractus NaN policy, chained comparisons, and `est`/`non est` semantics. (`95d80dccc`, `ba2a9140f`, `bcc488f7d`, `58d3b1c3b`)

### Other changes

- Add `go-failable-alternate-exit` factory goal for Go ⇥ parity (membership, `(T,error)` signatures, `iace`, `fac`/`cape`, `conversio`) superseding standalone `go-conversio-loud-failure`. (`47abc7156`)
- Tighten AIR routing constraints in `docs/design/air-dialect.md`. (`e67e0e74a`)
- Polish `conversio_outcome` shared failure helpers: centralize `Option`/`Result` outcome emission and document v1 propagation invariants. (`b353a10b5`)
- Route `try_from`, `instans`, and regex arms through `conversio_outcome` helpers; deduplicate regex propagation finishing. (`e283a3923`)
- Share `parseInstans` fixture, tighten closure-boundary assertions, and group failable test coverage for conversio propagation. (`05f30a1ee`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
