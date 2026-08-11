+++
title = "Radix 0.74.0"
section = "releases"
order = 26
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.74.0 |
| **Tag** | `radix-v0.74.0` |
| **GitHub** | [radix-v0.74.0](https://github.com/faberlang/releases/releases/tag/radix-v0.74.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.74.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.74.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.74.0/radix-v0.74.0-aarch64-apple-darwin.tar.gz) | 3.1 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.74.0/radix-v0.74.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.74.0/radix-v0.74.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.74.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

RR4 coverage closure: Go floor lifted to 249/292, missing intrinsics registered,
structural sexp matrix support wired, Stage5 LLVM host parity batch closed,
and a neutral host ABI seam deployed across backends.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 73 |
| `feat` commits | 16 |
| `fix` commits | 17 |
| `test` commits | 9 |
| `docs` commits | 9 |
| `refactor` commits | 4 |
| Date span | 2026-07-11 → 2026-07-13 |

### Major tracks

#### Go coverage floor (249/292)

- Raise the Go public-corpus pass floor from 226 to **249 accepted/pass**, preserving the 292 denominator and failure ceiling (`b3f4ef00`)
- Go ad route dispatch: non-genus route dispatch for host ABI calls (`43146843`, `2731a068`)
- Go ad frame views: directional frame views for tensor arithmetic reduction (`26c46b34`, `c43a9a1`)
- Go ad numeric recovery with vacuum drain (`c4d29dc9`, `8cc77962`)
- Go ad numeric recovery (duplicate entry for separate route path) (`5b7f971c`)
- Go tensor arithmetic reduction carrier for generated helpers (`8ba2ac49`)
- Go import encapsulation via resolved HIR carriers (`2fde74ad`)
- Go bare numerus overflow trap (`cd2f6f60`)
- Go hardened generated tensor helpers (`c37f83e3`)
- Go grouped method call lowering context (`b3b7b827`)
- Go structured import rendering test coverage (`7c675155`)

#### Intrinsics registry fixes

- Register missing `intervallum coercere` intrinsic (`0107d5f8`)
- Register missing `tabula valores` (map values) intrinsic (`9a15e004`)
- Register missing `tabula claves` (map keys) intrinsic (`15f7c1ea`)
- Register missing `textus vacua` (text empty) intrinsic (`d02c90d0`)

#### Structural sexp matrix support

- **Sexp function values in matrix**: emit sexp capability for function-valued matrix cells — covers emit, capability detection, and exempla coverage (`743ffb2d`)
- **Post-lowering interner retention**: retain the sexp interner snapshot after MIR lowering so matrix comparison can decode indexed values (`769fc336`)
- **Scena structural tier alignment**: align Scena structural and run tiers in the stepper, covering conversio and scalar paths (`0d5c5476`)
- **Proven via coverage test**: structural sexp matrix support confirmed in `mir_target_matrix` exempla (`2f417412`)

#### Stage5 LLVM host parity closure

- Close scalar valor parity row (runtime scalar values) (`a399376d`)
- Close regex conversion parity batch (`8e406956`)
- Close non-genus instans parity batch (`2ff647a2`)
- Close instans failable parity residual (`1f5e7bd8`)
- Close scalar conversion and failable gaps (`bdb975a5`)
- Close format text and grouped diagnostics (`7c1229b0`)
- Close text diagnostic display slice (`36cd19f3`)
- Close bivalens display parity slice (`66657402`)

#### Host ABI refactor

- Replace per-backend ABI imports with a **neutral host ABI seam** across 38 files in LLVM and Wasm text backends, aligning on a single `radix_host` contract (`468eea65`)

#### Wasm diagnostic import disambiguation

- Disambiguate diagnostic import locals in Wasm binary and text backends to avoid name collisions (`1c025c2a`)
- Disambiguate collection import locals in Wasm import names and program emission (`e80698bb`)

#### Backend emission needs module split

- Split monolithic `codegen/needs.rs` into per-backend modules (`go`, `rust`, `ts`) under `codegen/needs/`, reducing module coupling ahead of further backend work (`cea9d229`)

#### LLVM backend fixes

- Lower async solum poll boundary across declaration, emit, and host ABI context (`68e45218`)
- Retain lowered interner snapshot in LLVM text emission (`b3b3d09e`)
- Prove and close async tempus host link (`218042d8`, `fef375b5`)

#### TS backend fixes

- Emit cursor iteration generators (`e280150d`, `e1a5d7fc`)
- Preserve spread call arguments (`b9c0ccb7`)
- Cover tensor materialize behavior (`73b725cf`, `b85e0aa7`)
- Record tensor error behavior (`9457c374`)
- Emit est variant checks (`c649e801`)
- Narrow untagged tabula checks (`a175c023`)
- Derive helper needs from HIR carriers (`b1b641f7`)
- Migrate to shared output fixtures, removing inline snapshots (`e08c69ee`)

#### Coherence drift guards

- Report complete intrinsic drift in coherence test (`ee381f59`)
- Guard host ABI and frame protocol drift (`612d0f8f`)
- LLVM host smoke fixture contracts (`eadb06cb`)

#### Rust backend fix

- Use resolved identities for imports, replacing ad-hoc identity propagation with fully resolved `ResolvedUse` entries across codegen needs and semantic analysis (`6708098b`)

#### File interface diagnostics

- Reject ambiguous nominal imports where a name resolves to multiple candidates (`4bc4fba7`)
- Centralize reader catalog inventories into diagnostic catalogs with reduced duplication (`b1a2316f`)
- Retain public imports in path normalization test case (`ef6e03ba`)
- Satisfy diagnostic hygiene ratchet (`0ea63c5c`)

#### Stepper/frame polish

- Honor frame terminal states in TS frames (`be69e092`)
- Consume generated frame queues in Go frames (`b9ef1e4a`)
- Reserve SSA IDs for diagnostics in LLVM host (`25ad8634`)

### Documentation and planning

- HIR release readiness evidence refresh (`7f4dcaa0`)
- Radix recurring audit charter (D1–D9) by head-cso: trust boundaries, codegen/unsafe/FS/network/supply-chain domains (`1b325a4c`)
- Refresh ecosystem and design guidance (`5ffbd3f7`)
- Reconcile factory goal and campaign status (`1f31e6ae`, `357fd37f`)
- Define Wasm host parity campaign with delivery materials (`619ec222`, `631836c6`)
- Preplan WGPU host parity campaign (`1437e8b8`)
- Draft nucleum CPU emulator goal (`e7daa3a4`)
- macOS temporal route carrier assertion (`55861f7a`)

### Refactors and hygiene

- **Typed CLI entry**: carry typed CLI entry, reducing `unwrap`/expect churn in `cli.rs` (`6e31d58`)
- **MIR diagnostic symbols**: group diagnostic lowering symbols under `mir/lower.rs` (`0cb52374`)

### Other changes

- **Secondary feat(stage5) parity closings**: bivalens display, text diagnostic display, format text diagnostics, grouped diagnostics — all listed under Stage5 above

---

[All releases](/releases/) · [Install the current release](/start/install.html)
