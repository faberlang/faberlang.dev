+++
title = "Radix 0.80.0"
section = "releases"
order = 20
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.80.0 |
| **Tag** | `radix-v0.80.0` |
| **GitHub** | [radix-v0.80.0](https://github.com/faberlang/releases/releases/tag/radix-v0.80.0) |
| **Published** | 2026-08-08 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.80.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.80.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.80.0/radix-v0.80.0-aarch64-apple-darwin.tar.gz) | 4.9 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.80.0/radix-v0.80.0-aarch64-apple-darwin.tar.gz.sha256) |
| **Linux x64** | [radix-v0.80.0-x86_64-unknown-linux-gnu.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.80.0/radix-v0.80.0-x86_64-unknown-linux-gnu.tar.gz) | 5.4 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.80.0/radix-v0.80.0-x86_64-unknown-linux-gnu.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.80.0/radix-v0.80.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.80.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

> **Status**: final

Minor release spanning **1074 commits** (`v0.79.0..v0.80.0`, 2026-07-31→2026-08-07).
Headline: **the carrier-typed Wasm package chain is complete** (cursor-stream
v1 row, package-aware emit, host run via cross-module `faber_external`
resolution), GPU inference
amendments (per-position RoPE + `F16Round` — Q2 prefill top-1 PASS on Metal
with an honest, non-claimed numeric parity record), Stage 7 Swift triage
(215/215 classification rows, corpus gate unblocked), device-lowering
structure, the tensor-family locale surface (shipped + archived), and the
component release-tooling spine.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 1074 |
| `feat(...)` commits | 178 |
| `fix(...)` commits | 138 |
| `docs(...)` commits | 431 |
| `test(...)` commits | 43 |

Reconstruct the full log:

```bash
git log v0.79.0..HEAD --oneline --no-merges
```

### Major tracks

#### Carrier-typed Wasm package chain complete (codex-gap Stage 6, U6)

The Stage 6 carrier-typed Wasm package proof is closed end to end.

- **Cursor-stream v1 row (U6-A).** Cursor streams materialize on the closed
  v1 row `__faber_rt_v1_cursor_stream` instead of failing closed — the
  long-standing `implementation-debt` cursor-stream entries in the Stage 0
  ledger are covered by emit (`bde336445`).
- **Package-aware emit (U6-C/U6-D).** Same-package cross-module imports emit
  package-aware (`fc25de6db`); `emit_wasm_text_probe_package_aware` is
  re-exported and forwarded through the `radix::mir` façade so product lanes
  can reach it (`2db533bb5`, `2d4a7c6a0`).
- **Product package path.** The faber package lane accepts, emits per-unit,
  links, and runs Wasm packages; the link manifests and
  `wasm_modules` carrier slots are populated per unit
  (faber-side `8a0403a`, `d9df04b`, `774436f`). `go_modules` remains owned by
  the separate Go path.
- **Host run (cross-module `faber_external` resolution).** The package-aware
  emitter's `faber_external` imports resolve against the canonical
  `__faber_external_product_…_module_…_func_…` exports the sibling modules
  define (radix `radix-mir-wasm` import surfaces + faber package-wasm lane).
- **Tier floors reconciled.** Wasm tier floors are re-anchored to the
  cursor-stream + package-lane proofs, ledger-driven (`774436f`).

Cross-module `textus` handles remain unsupported because separate Wasm modules
have separate linear memories. The completed proof is the carrier-typed
`importa-wasm` path, not general cross-module handle sharing.

#### GPU inference amendments (GI3-1)

The inference recipe surface amendments that unblocked the Q2 prefill top-1:

- **Per-position RoPE.** `RopePlan.per_row` / `rows` carry per-position
  rotation facts through plan construction, wire, and the Metal/LLVM
  emitters (periodic per-head cosine/sine tables).
- **`MirUnOp::F16Round`.** A new unary node for f32→f16 round-to-nearest,
  wired through validation, the stepper, and the Metal/LLVM/Wasm/Sexp
  emitters (sexp emission fallout fixed in `32f7b4b79`).
- **Per-head attention + K-major weight repack.** Attention weights split per
  head (q/o into the 15 query heads, k/v into the 5 KV heads) so per-head
  masked softmax is expressible; GGUF K-major weights are transposed to the
  device matmul row-major layout (faber prefill driver).
- **Q2 top-1 PASS on Metal.** The burgus Metal run executed the full
  5188-kernel prefill program (5188 launches, 2724 input-role slots, 6633
  buffer allocations) and matched the golden top-1 logit at position 0.
- **Honest scoping: numeric parity NOT claimed.** The per-element
  `atol 1e-5 / rtol 1e-5` band fails at a measured max delta 5.755e-3 (f32
  device arithmetic vs the oracle's f64 rms-norm accumulation, compounded
  over 32 layers). The comparison record stands with `ok: false` and
  `top1_matches: true` (`gi3-prefill-comparison.json`), thresholds unchanged
  (stop condition 3 honored — no weakening). The numeric inference parity
  claim is **deferred**; only the top-1 gate is claimed.

#### Stage 7 Swift triage (codex-gap)

- **Classification appendix.** The Stage 7 Swift classification appendix is
  reconciled with the Stage 0 ledger and the baseline evidence log — all
  215/215 rows classified (214 + 1, statically cross-checked; no duplicates,
  no gaps).
- **Corpus gate unblocked.** Swift row-level classification verified; the
  Stage 7 dependency on the classification slice is closed (`fcec6137d`,
  `efb0878c3`).

#### Device-lowering structure

Structural pass over the device-lowering surface — no behavior change, all
proof/code organization:

- **Device-safe gate admission pre-passes** (dead-fold-artifact and
  dead-const-copy slot scans) split into proof categories in dedicated
  submodules (`d6bd07df4`).
- **Metal recipe tests split per-recipe** (`radix-mir-metal` emit tests →
  per-recipe modules, `31411a504`).
- **LLVM declarations dispatch to named helpers** (`bc8c9b0b3`).
- **NVVM dead-path retirement.** The dead same-kernel reduced-buffer
  read-back is retired (`28a54117b`).
- **`imports_scan` extraction.** Repeated import-collection scans are
  extracted into shared helpers (`834de0b02`).

#### Locale — tensor-family surface

- **Shipped.** Tensor-family + vacua locale surface lands: registry, emitter,
  and la/en packs (unit 1, `b80153537`), plus non-Latin tensor-family
  glosses and a th-TH round-trip golden (unit 2, `829a34ce6`).
- **Archived.** The `tensor-family-locale-surface` goal is closed and
  archived (`3fa9969b2`).

#### Release tooling spine (component side)

- **Scripts + runbook.** `bump-version`, `regen-lock`, and
  `release-linux-context` scripts with tests, plus a thin radix-local component runbook
  (`docs/release/runbook.md`, `a098deec3`).
- **Cross-repo release-manifest support.** The coordinated release contract
  (authority, manifest schema, per-stage decision docs) lands on the faber
  side with `release-manifest.yaml` as the frozen payload record; radix is an
  independent component release unit that never advances the shared repo's
  global `Latest`.

#### Wire-8 device contract and reduced-resource projection

- **Clean wire break.** The serialized device-program contract advances to
  wire version 8 and carries reduced-resource projections explicitly.
- **Fail-closed admission.** FMIR rejects unsupported axis-reduction operators,
  degenerate projections, mismatched carried-resource facts, and malformed
  reduced-resource projections (`faf688032`, `8e3887d4a`, `a554c8b42`,
  `dff1d95cf`).
- **Measured parity baseline.** The Wasm baseline-gap ledger is regenerated
  from the live wire-8 measurement (`5614335ae`).

#### Canonical imported nominal identity

Imported nominal types now retain canonical identity across analysis snapshots,
including enum variant snapshots. Identity-bearing resolution fails closed when
the canonical definition is missing (`8bf58961c`, `8d1b3ea1d`).

#### Tool and parser polish

- `radix check` and `radix emit` expose separate `--locale` and
  `--diagnostics-locale` controls (`7506d7f41`).
- Comments between `si`-chain branch links retain their structural trivia
  (`decfa3d99`).

### Breaking / author-visible

| Change | Migration |
| --- | --- |
| `MirUnOp::F16Round` added (new unary node) | Additive; no existing surface changes. New device emitters must cover it (sexp/stepper already do). |
| `RopePlan.per_row` / `rows` added | Additive plan facts; new field must be carried through wire + Metal/LLVM emitters. |
| FMIR versioned session section (GI4-2) | Optional — absent for single-device packages; when present, admitted fail-closed on its own wire-version ratchet. No `WIRE_DEVICE_PROGRAM_VERSION` bump required for the session section. |
| FMIR device-program wire version 8 | Clean serialized-contract break; producers and consumers must use the wire-8 reduced-resource projection shape. |
| Imported nominal identity snapshots | Additive compiler artifact facts; malformed or unresolved identity-bearing imports now fail closed. |
| Wasm package path (faber-side) | Wasm emit is package-aware; `faber_external` cross-module imports resolve against canonical product exports. |

No author-visible breaking removals in this range: the retired NVVM read-back
and the stale `WARN006`/`DeprecatedFeature` residue were internal-only.

### What is NOT included

- **No numeric GPU inference parity claim.** The per-element parity band is
  explicitly not claimed (`ok: false` record); the top-1 gate is the only
  claimed inference result.
- No new language surface beyond the locale and codegen additions above.
- No changes to the `faber` product CLI surface beyond the Wasm package path
  noted above (sibling repo release — this notes file covers radix only).
- No claim that reduced-resource projection makes every inference recipe fit a
  given device budget; wire-8 carries and validates the projection facts.

### Version alignment

| Item | Value |
| --- | --- |
| Source tag | `v0.80.0` |
| `crates/radix` version | `0.80.0` |
| Public artifact tag | `radix-v0.80.0` on `faberlang/releases` |
| Workspace members bumped | all `0.79.0` → `0.80.0` (hygiene-ratchet stays `0.1.0`) |

### Verification contract

The release commit is gated by `cargo build --locked --release -p radix --bin
radix` and `cargo nextest run`. The tag workflow runs the full Radix ladder
before publishing component artifacts.

### Publish

1. Bump all workspace crate versions `0.79.0` → `0.80.0` (not hygiene-ratchet);
   use `scripta/bump-version` + `scripta/regen-lock` per the thin runbook.
2. `cargo update` so `Cargo.lock` matches manifests.
3. Verify locked release build + nextest.
4. **Single commit** with version bump + lockfile:
   `release(radix): v0.80.0`
5. Annotated tag: `git tag -a v0.80.0 -m "Radix v0.80.0"`
6. Push: `git push origin main && git push origin v0.80.0`
7. Monitor: `gh run list -R faberlang/radix --limit 5`
8. Confirm `faberlang/releases` publishes `radix-v0.80.0` multi-arch archives.

**Never** tag a commit whose `Cargo.lock` is stale relative to the bumped
manifests — CI uses `cargo build --locked`.

---

[All releases](/releases/) · [Install the current release](/start/install.html)
