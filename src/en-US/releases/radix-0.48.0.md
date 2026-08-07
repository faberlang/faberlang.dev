+++
title = "Radix 0.48.0"
section = "releases"
order = 51
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.48.0 |
| **Tag** | `radix-v0.48.0` |
| **GitHub** | [radix-v0.48.0](https://github.com/faberlang/releases/releases/tag/radix-v0.48.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.48.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.48.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.48.0/radix-v0.48.0-aarch64-apple-darwin.tar.gz) | 1.8 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.48.0/radix-v0.48.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.48.0/radix-v0.48.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.48.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

Tight compiler pipeline polish: MIR lower modules gain deduplicated call-lowering
helpers, semantic validators extract shared logic, and the e2e harness lands a
`rustc` smoke-typecheck gate for driver codegen emit tests. 25 non-merge commits,
all within a single ~15-minute window.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 25 |
| Date span | 2026-06-25 17:48 → 2026-06-25 18:03 EDT |

### Major tracks

#### MIR lowering modules

- `mir/lower.rs`: extract shared callable body lowering helper, reducing
  duplication across the main lower entry point (`4071866cc`)
- `mir/lower/callable.rs`: dedup `emit_call` for function and value callees —
  one path for both dispatch forms (`bb6e3af2e`)
- `mir/lower/runtime.rs`: share HIR call-arg lowering helper between runtime and
  non-runtime lower sites (`d9e15df0b`)
- `mir/lower/async_surface.rs`: document the `cede` lowering surface contract
  (`babe03931`)
- `mir/lower/provider.rs`: document the `ad` binding contract and its lowering
  invariants (`758111f6a`)
- `mir/lower/collection_higher_order.rs`: module-level docs and if-block hygiene
  for collection higher-order lowerings (`c24b45778`)
- `mir/validate.rs`: dedup duplicate local-id diagnostics, collapsing repeated
  error paths (`7a46b458f`)

#### Validators and semantic passes

- `semantic/passes/typecheck/convert.rs`: extract regex conversio validator into
  its own helper, isolating conversion validation from general type-checking
  (`f4355cc9f`)
- `semantic/passes/borrow.rs`: extract callee signature lookup into a shared
  helper used by both borrow-check branches (`47e1309b55`)
- `semantic/passes/definite_assignment.rs`: guard early-return paths to prevent
  spurious uninitialized-variable diagnostics (`09cd4319f`)
- `semantic/init_state.rs`: add `join_paths` lattice unit tests covering the
  definite-assignment dataflow join (`bee359bb8`)
- `semantic/types.rs`: guard nullable-union early exit to skip redundant checks
  (`dff77c98e`)
- `semantic/passes/typecheck/call.rs`: dedup argument visitation and method-name
  resolution in call type-checking (`4784a6c5b`)

#### e2e harness and smoke helpers

- `feat(radix)`: add `rustc` smoke typecheck step to the driver codegen emit
  test — every Rust codegen output is now vet-compiled by rustc to catch emit
  bugs early (`b54d196a0`)
- `exempla_e2e` harness: companion test wiring, shared `rustc` availability
  guard, and extracted MIR test module with dedicated test file
  (`c2f52e1cb`)
- `exempla_e2e/wasm_external.rs`: dedup the instantiation probe assembly
  (wasm-bindgen-style extern blocks) into a shared helper (`79fb81562`)
- `exempla_e2e/llvm`: module-level docs and run-probe constructor helpers for
  the LLVM e2e fixture layer (`911995179`)
- Close out the `rust-codegen-smoke-check` factory goal (`6734f213d`)

### Other changes

- `parser/stmt.rs`: dedup mutability parsing paths and align transfer-statement
  documentation (`12df6fa0d`)
- `hir/lower/stmt.rs`: dedup `elige` variant lowering across
  if-let / while-let / for patterns; add statement-lower module docs
  (`1d6bc72b4`)
- `hir/nodes.rs`: clarify HIR variant docs for dispatch and `ad` nodes
  (`150aedbf0`)
- `codegen/go/expr/convert.rs`: final pipeline-polish touch to close the loop
  (`52eac17dd`)
- `docs(scripta)`: track compiler-pipeline polish progress, record subagent
  containment rules, and update the polish-loop file list (`d85b87758`,
  `194827c94`, `bcfc5a529`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
