+++
title = "Radix 0.38.0"
section = "releases"
order = 62
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.38.0 |
| **Tag** | `radix-v0.38.0` |
| **GitHub** | [radix-v0.38.0](https://github.com/faberlang/releases/releases/tag/radix-v0.38.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.38.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.38.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.38.0/radix-v0.38.0-aarch64-apple-darwin.tar.gz) | 1.2 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.38.0/radix-v0.38.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.38.0/radix-v0.38.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.38.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

Minor release spanning **59 commits** (`v0.37.0..v0.38.0`), touching **168 files**
(+16,168 / −331 lines). This release introduces MIR-backed Wasm, Go, and TypeScript
codegen targets (WasmText/LlvmText), builds out the wasm host syscall bridge across
Epics 4–6, and hardens closure and effect-return semantics.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 59 |
| Date span | 2026-05-24 → 2026-06-02 |
| Wasm text backend commits | ~20 |
| MIR lowering (shared) commits | ~9 |

Reconstruct the full log:

```bash
git log v0.37.0..v0.38.0 --oneline --no-merges
```

### Major tracks

#### MIR codegen targets: Wasm text backend

New **WasmText** probe target backed by MIR. This is the first functional
MIR-based backend for wasm, emitting validated WAT (WebAssembly Text Format)
primitives.

- Add experimental MIR-backed WasmText and LlvmText probe targets (`c098db68a`)
- Rename `WASM` probe target to `WasmText` (`b568253db`)
- Rename `LLVM` probe target to `LlvmText` (`d33edf2fd`)
- Wasm: emit primitive validated WAT subset (`99943cdb2`)
- Wasm: emit primitive branch dispatch (`aa8d3e0a7`)
- Wasm: emit primitive unary values (`ea01727e9`)
- Wasm: emit fractus scalars (`0015500e4`)
- Wasm: emit text handle subset (`6f5f82bd0`)
- Wasm: emit opaque aggregate handles (`bcb1c558b`)
- Wasm: emit aggregate projection reads (`7de24f0fa`)
- Wasm: emit runtime import calls (`6492261ec`)
- Wasm: emit option coalesce and bitwise ops (`41a1f38d1`)
- Wasm: lower assert intrinsics (`283610530`)
- Test: add wasm exemplar baseline harness (`8260fcd2c`)
- Test: gate wasm exemplar tier baseline (`bfae3558a`)

#### MIR lowering (shared infrastructure)

Shared MIR lowering passes that serve all codegen targets.

- Lower non-empty entry blocks (`2b1b98571`)
- Lower compound assignment (`546bae1de`)
- Lower array iteration (`652fced28`)
- Lower numeric range iteration (`6932e3b17`)
- Lower predicate operators (`5e277b032`)
- Lower literal switches (`2b3fd9d24`)
- Lower diagnostic arguments individually (`82efd22b7`)
- Lower typed vacua aggregates (`d11742fb9`)
- Lower genus methods for wasm (`c6404c6eb`)

#### Go and TypeScript codegen foundations

First Go and TypeScript codegen baseline, including exemplar harnesses and
target-specific fixes.

- Codegen: promote Go fractus assignment operands (`7b2ec7091`)
- Codegen: advance Go optional nullable e2e (`3261fdcad`)
- Test: gate Go exempla expected failures (`da69ae35a`)
- Test: add TypeScript exempla baseline harness (`c9292d67d`)
- Fix: emit TypeScript genus instance methods (`457ac3046`)
- Docs: add TypeScript codegen factory goal (`a31eba06a`)

#### Host syscall bridge (Epics 4–6)

Wasm host syscall infrastructure, macOS host route proof, and consolum HAL
work spanning execution roadmap Epics 4–6.

- Tighten Epic 4 host topology plan (`86389e17c`)
- Implement macOS host route proof with kernel frame/router/syscall modules (`46f7a2819`)
- Attach macOS host component import proof (`762e87fab`)
- Revise Epic 5 around Rust-to-Wasm syscall bridge (`3b7d1765f`)
- Bridge ad helper to wasm host syscall import (`0e16d9548`)
- Add core wasm host syscall runner (`25469b30c`)
- Prove generated wasm ad host syscalls (`ae59d2b0a`)
- Refine Epic 6 norma migration scope (`4cf31f903`)
- Define Epic 6 first slice conditions (`d89c47d38`)
- Classify norma Epic 6 baseline (`94707d049`)
- Feat(host): expose consolum syscalls (`23721860c`)
- Close Epic 6 ledger (`8d8d49504`)

#### Language semantics: closure and return hardening

- Require closure error channel for `iace` (`e9dd79329`)
- Require explicit closure return for `redde` (`c10bfceb6`)
- Harden effect-only function returns (`0f14e070f`)

#### Consolum and ad protocol

- Require consolum read size payload (`fda60f095`)
- Document sigcall boundary and move consolum HAL (`82f6cb59f`)
- Refactor consolum around typed calls (`073159215`)
- Draft frame-stream ad rewrite goal (`2d9d17feb`)
- Clarify ad frame protocol goal (`c6af7f6ed`)
- Document future host dependency manifests (`9cdd0de39`)

### Other changes

- Add target support matrix factory goal (`75a0eb1de`)
- Add Go and Wasm codegen factory goals (`5b544fda4`)
- Clarify codegen factory worktree assignments (`32bc78199`)
- Record Go codegen baseline (`798af8c7e`)
- Clarify TypeScript factory base commit (`e55dff758`)
- Refresh exempla corpus (`50e39a3ee`)
- Chore: align hygiene budgets with current production code counts (`d6018ed1c`)
- Chore: lint fixes (`8782355fc`)

### Notes

- The WasmText and LlvmText probe targets are experimental — declared by name
  in the tool surface, not yet wired as default build targets.
- Target support matrix factory goal (`docs/factory/target-support-matrix/goal.md`)
  formalises the multi-architecture build plan.
- Host syscall bridge commits span the `hosts/macos-arm64/` kernel and HAL
  modules; wasm guest code is in `crates/radix/src/codegen/`.
- Tag range: `v0.37.0..v0.38.0`.

---

[All releases](/releases/) · [Install the current release](/start/install.html)
