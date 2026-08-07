+++
title = "Radix 0.54.0"
section = "releases"
order = 45
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.54.0 |
| **Tag** | `radix-v0.54.0` |
| **GitHub** | [radix-v0.54.0](https://github.com/faberlang/releases/releases/tag/radix-v0.54.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.54.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.54.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.54.0/radix-v0.54.0-aarch64-apple-darwin.tar.gz) | 1.9 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.54.0/radix-v0.54.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.54.0/radix-v0.54.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.54.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

Native-stdlib campaign reaches its first compiler-integrated milestone: a
`chorda` v1 subset compiled through the full toolchain. Two MIR cross-backend
refactoring strata eliminate duplicated shape-query and type-resolution code
between the LLVM and Wasm text probes.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 15 |
| Date span | 2026-06-27 → 2026-06-27 |

### Major tracks

#### Native stdlib: `chorda` v1 subset

- **Stage 3** delivers `chorda.retorque` compiled through the `faber build`
  pipeline — the first native-stdlib function to survive the full compiler
  toolchain, with semantic typecheck support for builtin calls and the
  codegen rust emit surface (`68a6cf3cc`).
- **Stage 4** closes with a broader `chorda` v1 subset: the `chorda.fab`
  exemplar corpus, compiler-side parser/decl and codegen wiring for method
  dispatch, and supporting runtime glue in `norma/chorda.rs` and
  `faber-cli/src/package.rs` (`57a5df61e`).
- **Stage 5** delivers the final chorda-native-body surface plus EBNF grammar
  updates: parser/decl stripping of the placeholder `segmentum` rules, and
  removal of the legacy codegen rust `const_tabula` path (`b3bfbc9b3`).
- Mechanical design locked to a UTF-8 `textus` ↔ `octeti` trio: design docs
  for `chorda-methods.md` and `stdlib-mechanical-verbs.md` updated to the v1
  subset (`5cc78773b`).
- **DEFER-029** tracks the remaining `octeti` UTF-8 native-body gap — tagged
  as deferred rather than blocking the milestone (`0bf8371e2`).

#### MIR shape-query refactors (Strata 1 & 2)

- **Stratum 1** moves four pure MIR shape functions (`kind_name`,
  `definition_id`, `operands`, `has_spread`) from byte-for-byte duplicated
  free functions in `llvm_text.rs` / `wasm_text.rs` into inherent methods on
  the MIR node types in `mir/nodes.rs` (`fa960dbed`).
- **Stratum 2** lifts shared MIR type-resolution (`option_payload_ty`,
  `option_chain_base_ty`, `constant_ty`, `place_base_ty`) into a new
  `mir::ty` module with a `MirTypeLookup` trait, `MirTypeError`, and 9
  dedicated unit tests. Both probes now apply the same nullable-type policy
  (`11597e553`).
- Unused `mir::rust_probe` backend (~1400 lines including tests) removed; its
  probe-slot replaced by the sexp probe (`569362d0e`).
- Sexp probe signature aligned with the LLVM/Wasm probes for uniform dispatch
  (`e827a8a96`).

#### Validation infrastructure & factory closure

- `scripta/verify-native-stdlib` stage-gate script added, scoped to per-stage
  unit tests (avoids `--workspace --all` overhead) (`f3a0e4e6e`).
- Native-stdlib validation tiered to per-stage unit tests in the factory
  plan/ledger (`db05cd988`).
- Exempla-crate and faber-runtime-namespace factory campaigns closed —
  ledger/goal/plan marked done (`a5459823b`).

### Other changes

- Anchor commits recorded for Stages 3, 4, and 5 in the native-stdlib factory
  ledger (`0be1db396`, `cc81010a5`, `8d2657f4d`).

---

[All releases](/releases/) · [Install the current release](/start/install.html)
