+++
title = "Radix 0.65.0"
section = "releases"
order = 35
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.65.0 |
| **Tag** | `radix-v0.65.0` |
| **GitHub** | [radix-v0.65.0](https://github.com/faberlang/releases/releases/tag/radix-v0.65.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.65.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.65.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.65.0/radix-v0.65.0-aarch64-apple-darwin.tar.gz) | 2.1 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.65.0/radix-v0.65.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.65.0/radix-v0.65.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.65.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

Minor release spanning **30 non-merge commits** (v0.64.0..v0.65.0). Two
parallel campaign tracks landed in the same tag: **file namespace visibility and imports** (the `file-namespace-imports` factory goal, Milestones A–C)
and the **MIR LLVM campaign** (Stages 0–2 establishing the shared
pre-emission capability vocabulary and runtime-boundary classification
ledger).

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 30 |
| Date span | 2026-07-01 (single day) |

### Major tracks

#### File namespace visibility and imports

Ship the `file-namespace-imports` factory goal across three milestones,
closing the gap between kernel-glob re-export semantics and proper
package/library namespace routing.

- **Enforce file namespace export visibility.** `publica`/`protecta`
  annotations on declarations within imported file namespaces gate access;
  the visibility annotation pass resolves each scope decision against the
  import binding. (`176b9b99c`)
- **Wire public library namespace reexports.** Library packages now
  propagate re-exported items through `library_interface_items`, extending
  the existing kernel-glob precedent to the package boundary.
  (`c60fa4042`)
- **Preserve library import visibility.** The import graph tracks each
  binding's original visibility so downstream packages see the intended
  surface. (`b3f0d611e`)
- **Support type-only file namespace imports.** Syntax (`importa Type ex
  lib:mod`), parser, HIR lowering, and resolver accept qualified type-only
  imports alongside value imports. (`bc1fc658a`)
- **Lower local file namespace calls.** Rust codegen emits cross-namespace
  calls through the import-params seam, routing qualified function
  references through the correct module path. (`744ee8866`)
- **Reserve protecta visibility annotation.** EBNF, semantic pass, and
  exempla register `protecta` as the file-private visibility specifier.
  (`27e89d50d`)

Supporting fixes in the same area:

- Preserve local namespace import identity through codegen and semantic
  resolution. (`4c2c11f08`)
- Resolve local file namespace types with correct type-path construction.
  (`ad28ddab3`)
- Count qualified type namespace imports as used (fixes spurious
  unused-import warnings). (`33824bd58`)
- Stabilize namespace validation gates across parser, codegen, and
  driver test fixtures. (`d48ce3a6c`)
- Keep library item names under import aliases; do not replace the
  canonical name. (`97d16a1e3`)
- Stop synthesizing empty library namespaces in codegen output.
  (`db3bf86ca`)
- Keep `protecta.fab` reference parse canonical. (`85625f8b1`)

#### MIR LLVM campaign (Stages 0–2)

Establish the MIR LLVM campaign with a shared capability-validation
pattern, runtime-boundary taxonomy, and fresh baseline measurements.

- **Stage 0 — baseline refresh.** Measured MIR/LLVM floors against the
  pinned baseline; corpus grew 252→287. Every floor rose in absolute
  terms and meets its code-floor constant; verifier-invalid emitted IR
  stays at 0 (campaign hard invariant). (`5b4dea68f`, `f964bd127`)
- **Stage 1 — runtime boundary classification.** Inventory of all 19 LLVM
  runtime helper families sorted into a 4-category taxonomy
  (core-semantics, host-integration, probe-scaffolding,
  intentional-opaque-runtime) with per-family route-to-stage assignments.
  Guard test verifies every helper family is classified. (`d0419e46d`)
- **Stage 2 — target capability validation.** Add a target-neutral
  `mir::capability` vocabulary (`CapabilityGap` enum, `Lowerability`
  verdict) and an LLVM pre-emission classifier that rejects structurally
  known-unsupported programs with classified diagnostics before deep emit
  runs. Wasm is the reciprocal design client. (`8cb157283`)
- **Campaign routing refined.** Stage goals renumbered 00–10 and routing
  rationalized across the MIR LLVM campaign. (`e8c0cf32c`)
- **Debt ratchet.** Unsupported diagnostic ceiling raised 5→6
  (`conversio/fallibilis.fab` hits the existing `try_call` MIR-to-LLVM gap,
  tracked to Stage 8). (`098686c38`)
- **Staging gate refreshed.** `llvm-staging-gate.sh` pins stable
  floor/ceiling annotations instead of drifting exact ratios.
  (`a7f23b012`)
- **Delivery spec corrected.** Stage 2 delivery spec synced to as-built
  code (infallible visitor, no callee pre-classification, deviation log).
  (`8615b2e28`)

#### Canonical Faber emit in radix

- Move canonical Faber emit from `forma` into `radix::codegen::faber`,
  exposing `--emit faber` through the `radix` CLI's compile command. The
  `forma` crate retains its transform-only role. (`f0a1810ed`)

#### Morphologia cleanup

- Clean up `morphologia` intrinsic surfaces: `nihil`, `insum`,
  `exsero`/`exime`, JSON/YAML conversion methods, and the MIR dump/stepper
  representations. Deprecates the old `mixed-case-naming-debt.md` design
  doc. (`5676d700e`)

#### Stdlib directory module pattern

- Split `caelum.fab` into sub-modules (`terminus`, `connexus`,
  `auscultator`) establishing a directory-based stdlib module pattern.
  Each sub-module is independently importable via `norma:caelum/child`;
  the top-level `norma:caelum` import remains for convenience. Co-located
  `.proba` test files included. (`736442377`)

### Other changes

- Add MIR GPU campaign docs — 10-stage factory plan for GPU device
  subsets, kernel ABI metadata, layout facts, buffer tensor views, scalar/
  vector math, control flow, builtins, shader stage model, reflection
  sidecar, and Three.js/WebGPU proof. (`112cc7541`)
- Add WGSL-text spike goal doc — design factory for a WebGPU shader emit
  target as a sibling MIR probe to `metal-text`. (`5908c38d0`)
- Propose `file-namespace-imports` factory goal with three-milestone
  delivery spec; record aborted-run lessons (no forked `HirItemKind`,
  runnable-exemplar checkpoints, deliverable seam). (`1cb9bd621`,
  `7be5ecf88`)
- Document tensor and sparsa library design together in top-level
  README.md. (`fc3b2d856`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
