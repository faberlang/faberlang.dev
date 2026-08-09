+++
title = "Radix 0.53.0"
section = "releases"
order = 44
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.53.0 |
| **Tag** | `radix-v0.53.0` |
| **GitHub** | [radix-v0.53.0](https://github.com/faberlang/releases/releases/tag/radix-v0.53.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.53.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.53.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.53.0/radix-v0.53.0-aarch64-apple-darwin.tar.gz) | 1.9 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.53.0/radix-v0.53.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.53.0/radix-v0.53.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.53.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

Minor release spanning **26 non-merge commits** (`v0.52.0..v0.53.0`). This
release moves the exempla corpus and e2e harness into their own crate; retools
the Rust, TypeScript, and Go e2e runners for shared target dirs, batch builds,
and parallel subprocess tiers (cutting full-corpus time from ~10 min to ~30 s);
and introduces the `modulus` namespace construct as Stage 2 of the native stdlib
campaign.

### Scale
| Signal | Count |
| --- | ---: |
| Commits (no merges) | 26 |
| Date span | 2026-06-27 → 2026-06-27 |

### Major tracks

#### Exempla crate migration

The exempla corpus (220+ `.fab` files, expectations, support files) and the
entire `exempla_e2e` harness (Rust, TS, Go, MIR, LLVM, WASM, script, smoke,
roundtrip tiers) move from `crates/radix/src/` into a dedicated
`crates/exempla/` crate (`1c1c767e4`). This decouples the exempla dependency
tree from the compiler crate — corpus additions no longer trigger a radix
recompile, and the harness gets its own `Cargo.toml` for targeted dependency
management.

Post-move visibility normalization collapses 28 now-orphaned `pub(super)` items
to `pub(crate)` (`0252cecdb`). The migration is documented through goal/plan/
ledger phases (`60e4ca0db`, `ec8f8c492`) and closed out in the ledger
(`3cd5f05ce`).

#### E2E speed work

A coordinated campaign to pull the full 220-exemplum e2e suite from ~10 min
down to a responsive developer cycle. Three structural improvements compound:

**Shared `CARGO_TARGET_DIR`** (`b1984809d`): Every Rust exemplum previously
wrote its own fresh `target/` directory, causing the full `faber` + `norma` +
`tokio` dependency tree to recompile ~220 times. A single shared target dir
reuses the compiled tree across all exempla. Clippy `--fix` (a duplicate-dep
compile) is dropped from the per-exemplum loop — it belongs to the
rust-canonical RC-003 tier. Result: **~10 min → 137 s** with streaming
per-exemplum progress.

**Batch workspace build** (`ad71894b9`): The remaining 137 s was dominated by
Cargo's per-invocation spawn + fingerprint overhead (~400 ms × 220 = ~95 s).
Restructured into three phases: (1) Faber-compile + write each exemplum as a
workspace member, (2) a single `cargo build --keep-going` at the workspace
root, (3) run + verify each binary. Status: **220/220 in 45.8 s** (was 137 s).

**Parallel binary runner** (`99708fbde`): The run phase still launched 218
binaries serially (~175 ms spawn tax each). A new `scripta/run-exempla-parallel`
script runs the built binaries concurrently via `xargs -P`, collapsing spawn
tax across cores. Status: **~0.7 s run phase** on an 18-core host (was 38 s).

**Tier-level parallelization for TS and Go**:

- **TypeScript** (`e31a3c79b`): Restructured into serial frontend + parallel
  typecheck/runtime tiers via `std::thread::scope`. **48–63 s (was 163 s)**
  — ~2.6–3.4× speedup. Identical pass/fail: 147/220 runnable, 20/220
  behavior-checked.
- **Go** (`c4c786754`): Same two-phase model; `go vet` dropped from the loop
  (pure cost, never affected pass/fail). Unique `.go` files per exemplum for
  parallel safety. **27.97 s (was 64.45 s)** — ~2.3× speedup.

**Compiler performance docs** (`0bf23ed5a`): A new `examples/bench_compile.rs`
benchmarks the full pipeline (frontend ~16 MB/s linear, Rust codegen, scena
scripting path). Documented in README.md with backend/linking scaling analysis
(`c580cadc8`): dep model, per-package target-dir reuse, the what-recompiles
matrix, and cold-vs-warm costs.

#### Modulus namespace (Stage 2)

The `modulus` keyword introduces a body-bearing namespace/module construct,
separating the overloaded `pactum` role into two distinct constructs
(`b77f20186`):

- **modulus** (new): namespace/module façade with body-bearing methods by
  default. First customer: `norma:chorda`.
- **pactum** (unchanged): interface contract, signature-only, `implet` target.
- **genus** (unchanged): instantiable object with `ego` and instance state.

Prerequisite: the untyped frontmatter metadata key `modulus` is renamed to
`group` to free the keyword for permanent language surface (`84cac383d`).

The full parse/lower/codegen path lands in `9892f3722`: lexer token, parser
decl, AST node, HIR lower (`LoweredProgram.modules`, `AnalyzedUnit.modules`),
Rust codegen dispatch, and five targeted tests. Chorda surface docs
(`2b0b11111`) lock the stdlib API surface. Stage 2 is frozen at `9892f372`
(`d9d9c58f8`).

### Other changes

- **Factory docs — tensor ledger closeout:** Tensor-types ledger is closed with
  per-stage SHAs and verification evidence (`f522dbe26`, `a9775fa03`,
  `68d4ee289`). Native-stdlib delivery spec, plan, and ledger added
  (`eec5d31bc`).
- **Factory docs — e2e speed documentation:** Goal, phased plan, measured
  results, and cross-harness comparison recorded in the factory ledger
  (`86e9f05ce`, `f9e36d8c2`, `0688a48ed`, `888ddbe74`).
- **Stage 2 pause:** Native-stdlib delivery is paused at Stage 2 closeout
  (`706ec8b6c`).

---

[All releases](/releases/) · [Install the current release](/start/install.html)
