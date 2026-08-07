+++
title = "Radix 0.80.0"
section = "releases"
order = 19
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.80.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

> **Status**: draft — finalized at the v0.80.0 tag

Minor release spanning **1051 commits** (`v0.79.0..v0.80.0`, 2026-07-31→2026-08-07).
Headline: **the Wasm chain is complete** (cursor-stream v1 row, package-aware
emit, host run via cross-module `faber_external` resolution), GPU inference
amendments (per-position RoPE + `F16Round` — Q2 prefill top-1 PASS on Metal
with an honest, non-claimed numeric parity record), Stage 7 Swift triage
(215/215 classification rows, corpus gate unblocked), device-lowering
structure, the tensor-family locale surface (shipped + archived), and the
component release-tooling spine.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 1051 |
| `feat(...)` commits | 175 |
| `fix(...)` commits | 129 |
| `docs(...)` commits | 427 |
| `test(...)` commits | 42 |

Reconstruct the full log:

```bash
git log v0.79.0..HEAD --oneline --no-merges
```

### Major tracks

#### Wasm chain complete (codex-gap Stage 6, U6)

The Stage 6 Wasm gap chain is closed end to end.

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
  `wasm_modules` / `go_modules` carrier slots are populated per unit
  (faber-side `8a0403a`, `d9df04b`, `774436f`).
- **Host run (cross-module `faber_external` resolution).** The package-aware
  emitter's `faber_external` imports resolve against the canonical
  `__faber_external_product_…_module_…_func_…` exports the sibling modules
  define (radix `radix-mir-wasm` import surfaces + faber package-wasm lane).
- **Tier floors reconciled.** Wasm tier floors are re-anchored to the
  cursor-stream + package-lane proofs, ledger-driven (`774436f`).

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

- **Scripts + runbook.** `bump-version`, `regen-lock` (and release-context)
  scripts with tests, plus a thin radix-local component runbook
  (`docs/release/runbook.md`, `a098deec3`).
- **Cross-repo release-manifest support.** The coordinated release contract
  (authority, manifest schema, per-stage decision docs) lands on the faber
  side with `release-manifest.yaml` as the frozen payload record; radix is an
  independent component release unit that never advances the shared repo's
  global `Latest`.

#### Conditional — in flight at draft time

> The following was **in flight when this draft was written**. If it lands
> before the v0.80.0 tag, fold it into the wire-contract track below; if not,
> it ships in a later release.

- **FMIR serialized-contract ratchet.** A wire-version ratchet for the
  serialized device program contract (`WireRopePlan` / `MirProgram` wire
  shape) that admits the new plan facts fail-closed. Note: the versioned
  cadence/session wire section itself already landed (GI4-2,
  `9c3d41241` — session section + own version ratchet + admission, optional
  for single-device packages); the pending part is the nested
  device-program wire-version bump for the new rope shape.
- **Reduced-resource projection (council CB-2/CB-3).** Projection of the
  inference recipes under reduced resource budgets (smaller workspace /
  fewer kernels), pending council decisions CB-2/CB-3.

### Breaking / author-visible

| Change | Migration |
| --- | --- |
| `MirUnOp::F16Round` added (new unary node) | Additive; no existing surface changes. New device emitters must cover it (sexp/stepper already do). |
| `RopePlan.per_row` / `rows` added | Additive plan facts; new field must be carried through wire + Metal/LLVM emitters. |
| FMIR versioned session section (GI4-2) | Optional — absent for single-device packages; when present, admitted fail-closed on its own wire-version ratchet. No `WIRE_DEVICE_PROGRAM_VERSION` bump required for the session section. |
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
- The conditional wire-contract ratchet and CB-2/CB-3 projection are not
  counted as delivered unless they land before the tag.

### Version alignment

| Item | Value |
| --- | --- |
| Source tag | `v0.80.0` (planned) |
| `crates/radix` version | `0.80.0` (pending the release bump commit) |
| Public artifact tag | `radix-v0.80.0` on `faberlang/releases` (planned) |
| Workspace members bumped | all `0.79.0` → `0.80.0` (hygiene-ratchet stays `0.1.0`) |

### Verification (pre-release)

> Draft — verification is recorded on the release candidate tree at the tag,
> per the v0.79.0 precedent (`cargo build --locked --release -p radix --bin
> radix`, `radix --version`, `cargo nextest run`, then the `Publish` steps
> below). The draft intentionally does not block the tag on these notes.

### Publish

1. Bump all workspace crate versions `0.79.0` → `0.80.0` (not hygiene-ratchet);
   use `scripta/bump-version` + `scripta/regen-lock` per the thin runbook.
2. `cargo update` so `Cargo.lock` matches manifests.
3. Verify locked release build + nextest.
4. **Single commit** with version bump + lockfile (+ this notes file if still dirty):
   `release(radix): v0.80.0`
5. Annotated tag: `git tag -a v0.80.0 -m "Radix v0.80.0"`
6. Push: `git push origin main && git push origin v0.80.0`
7. Monitor: `gh run list -R faberlang/radix --limit 5`
8. Confirm `faberlang/releases` publishes `radix-v0.80.0` multi-arch archives.

**Never** tag a commit whose `Cargo.lock` is stale relative to the bumped
manifests — CI uses `cargo build --locked`.

---

[All releases](/releases/) · [Install the current release](/start/install.html)
