+++
title = "Radix 0.77.0"
section = "releases"
order = 22
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.77.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

Minor release spanning **145 commits** (`v0.76.0..v0.77.0`, 2026-07-20→2026-07-22).
Driven by the MIR Swarm campaign: graphics pipeline reflection goes end-to-end,
the AIR backward proof chain wires through the driver, WGSL workgroup reductions
ship, and the workspace drops host/exempla siblings.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 145 |
| `feat(...)` commits | 13 |
| `fix(...)` commits | 28 |
| `docs(...)` commits | 47 |
| `delivery(...)` commits | 16 |

### Major tracks

#### Graphics pipeline reflection

End-to-end pipeline reflection from HIR shader-stage annotations through WGSL
emission to JSON. The initial seam (`MirGraphicsPipelineReflection` +
`MirKernelShaderStage`) was laid down, then extended from stub counts to full
resource descriptors, multi-target color attachments, depth/stencil, stencil
read/write masks, host-configurable primitive topology, fragment source
extraction with combined vertex+fragment WGSL emission, and conflicting-stage
diagnostics. Goal 01 completion (`50d300b98`) wires `MirTrigaPipelineFact` into
the `--reflection` tool output.

- `feat(mir): graphics pipeline reflection + draw prerequisites seam` (`140ec8707`)
- `feat(mir): assign MirKernelShaderStage during HIR→MIR lowering` (`961725982`)
- `feat(mir): surface resource counts in graphics pipeline reflection` (`d04c4bf81`)
- `feat(mir): add per-stage resource descriptors to graphics pipeline reflection` (`58662d138`)
- `feat(mir): multi-target color attachments in pipeline reflection` (`dbd6afbe2`)
- `feat(mir): depth/stencil state for graphics pipeline reflection` (`78c8c117c`)
- `feat(mir): stencil read/write masks and per-face stencil state` (`bd27ab6cf`)
- `feat(mir): host-configurable primitive topology builder` (`f792908d2`)
- `feat(mir): add emit_wgsl_fragment_entry_contract_with_targets to radix-mir-wgsl` (`6d8463878`)
- `feat(mir): implement fragment source extraction and combined vertex+ fragment WGSL emission` (`cc75ccc4a`)
- `feat(mir): emit diagnostic for conflicting shader-stage annotations` (`a159f5a10`)
- `feat(hir+mir): is_vertex/is_fragment HIR flags + Stage 4 lowering inventory` (`c6bc07db5`)
- `Goal 01 completion: pipeline-level reflection extraction from source` (`50d300b98`)

#### AIR backward proof chain & autograd pipeline

The generated-gradient pipeline wires through the driver for backward-annotated
tensor units: `generate_air_lane_backward` runs the full proof chain (companion
→ AIR-to-MIR → result contract → eligibility → admission). Op-family dispatch
routes elementwise, reduction, and matmul to the correct `prove_*` function.
Fill/Vacuum type mismatches on the reduction path were repaired, and the
`MirBackwardResultContract` now supports variable field counts.

- `D-A-02 S1: wire AIR proof chain into driver for backward-annotated units` (`cada5a953`)
- `d-a-02 S2: source-level entry point + end-to-end exemplum` (`5f124b126`)
- `D-A-02 S3: elementwise op expansion — Div and Neg` (`66935a25f`)
- `D-A-02 S4: reduction op expansion — Sum + Mean` (`48b3e4502`)
- `D-A-02 S5: rank-2 matmul expansion (FINAL stage)` (`81568e64d`)
- `d-a-02 S4+S5 repair: wire dispatcher, fix Fill/Vacuum, add tests` (`e44733bc3`)
- `fix(radix): driver backward-skip repairs — Box::leak, scalar skip, detect_backward_op` (`c7479e1c2`)
- `fix(delivery): correct transpose oracle layout convention in D-A-08` (`80e17f05b`)
- `delivery: D-A-07 domain unary backward (Exp + Log) — 4-unit serial graph` (`bb0580ecb`)

#### Gradient ABI & LLVM backend

ABI gradient handles hit both the surface (host-abi symbols + payload) and the
LLVM backend emit for gradient calls. The `GRADIENT_HANDLE_TYPE` reserved
constant was documented.

- `D-A-03 U1: gradient ABI surface (host-abi symbols + ABI payload)` (`aef79e4d7`)
- `D-A-03 U2: LLVM backend emit for gradient calls` (`7175b728f`)
- `docs: document GRADIENT_HANDLE_TYPE as reserved constant` (`2494caa03`)

#### WGSL workgroup reductions

The MIR WGSL emitter now lowers `Sum` and `Mean` collection intrinsics to a
workgroup reduction pattern: shared memory load, workgroup barrier, sequential
tree reduce, and guarded output write (`TensorMean` divides by workgroup size).
This promotion moves WGSL reductions from `CheckedDebt` to `NativeSupport`.

- `feat(mir-wgsl): emit workgroup reduction for Sum/Mean Collection intrinsic` (`f4917c740`)
- `test: fix stage5 native blocker assertion after WGSL reduction promotion` (`51e6707d9`)

#### MIR operations & infrastructure

`MirUnOp::Relu` added with stepper dispatch (`max(0, x)` for Float/Int), dump
label, validation, and exhaustiveness fixes. WASM backend gets a dedicated Relu
type arm emitting `f64.max`. `MirInputStepMode` and `Bgra8Unorm` added to the
radix-mir ABI types. MIR name analysis gains `is_collection_op` and
`is_collection_type` helpers. The LM studio annotation exclusivity check was
narrowed per CTO.

- `radix: add MirUnOp::Relu with stepper dispatch, dump label, validation, and exhaustiveness fixes` (`961e04beb`)
- `fix(radix-mir-wasm): dedicated Relu type arm + negative tests` (`82c13ce93`)
- `mir: add MirInputStepMode + Bgra8Unorm to radix-mir ABI types` (`ea95b924d`)
- `fix(mir): annotation exclusivity + narrowed Stage 4 inventory per CTO` (`c6e49fd14`)
- `fix(mir): with_stencil fails closed when depth_stencil is None` (`a9e049429`)

#### Spine design docs: device execution, reflection reciprocity, placement

Three major design documents codify spine law for the GPU/host execution model:

- **Placement execution contract** (`3fc85670b`): 14-section spine law defining
  executable placement semantics — copy-in, readback, sync through
  `__faber_gpu_v1_*` ABI symbols, WebGPU first with LLVM parity follow-on.
- **Reflection reciprocity** (`9a35b18b2`): the compute↔graphics reflection
  schema contract — reciprocity matrix, shared root inventory, divergence rules,
  versioning policy, freeze process.
- **Unified WebGPU host resource model** (`aead2be51`): buffer identity via
  `logicalId + generation`, create-before-retire, queue-completion-gated
  destruction, compute-vs-render-pass ownership.

Delivery specs for each spine stage were also filed:

- `delivery: D-SPINE-02 placement execution — 5-stage serial` (`8c011182b`)
- `delivery: D-SPINE-03 reflection reciprocity — 2-stage` (`00bb749bf`)
- `d-spine-01 S1: unified WebGPU host resource model design doc` (`aead2be51`)
- `spine: G-SPINE-03 S1 reflection reciprocity design doc` (`9a35b18b2`)
- `spine: placement execution contract design doc (G-SPINE-02 S1)` (`3fc85670b`)
- `fix(d-spine-02): correct abi_test.rs evidence path` (`f1ce397cf`)

#### Workspace restructuring

The `crates/exempla` e2e harness and the `hosts/` directory (macos-arm64,
webgpu-browser) were removed from the radix workspace. Platform hosts moved to
the sibling `faberlang/hosts` repo; exempla moved to the sibling
`faber/crates/exempla`. This unblocks standalone radix release builds that do
not depend on the faber CLI sibling.

- `refactor: move exempla e2e harness out of radix workspace` (`ef93b3e12`)
- `refactor: drop host products from radix workspace` (`59df81088`)

#### Clippy pedantic deny (crates/radix)

The main `crates/radix` package now denies pedantic clippy, matching the posture
of the leaf crates. A multi-wave cleanup fixed ~hundreds of warnings across docs,
`must_use`, `map_or`, imports, borrows, path borrows, and restore of
rustdoc backtick code-links after a bad rewrite.

- `chore(clippy): enable pedantic deny on crates/radix with structural allows` (`41fdff0bf`)
- `style(clippy): auto-fix mechanical pedantic on crates/radix` (`d6d5a67c6`)
- `style(clippy): must_use and remaining auto-fixable pedantic on radix` (`72e15b7fb`)
- `fix(clippy): parallel pedantic cleanup wave on crates/radix` (`734beec00`)
- `fix(clippy): second pedantic wave — docs, map_or, imports, borrows` (`af0575b91`)
- `fix(clippy): residual pedantic docs, allows, and path borrows` (`c3ae2faf3`)
- `fix(clippy): finish pedantic deny for crates/radix package` (`bb3954ecc`)
- `fix(clippy): clear residual non-pedantic warnings on crates/radix` (`dfa423465`)

#### Codegen fixes (failable functions)

Two related fixes ensure library-imported and locally-defined failable functions
(`⇥` / `∅`) are correctly registered during Rust codegen. The `extend_library_failable`
call was missing when a type table was present, and the HIR-level `collect_failable_functions`
scan was gated behind a legacy branch. Both paths now run unconditionally,
fixing roundtrip failures for `norma::json`, `http_provider`, and `sqlite`
packages.

- `fix(codegen): call extend_library_failable when type table is present` (`793908373`)
- `fix(codegen): always collect failable functions from HIR alongside library failable` (`58e83dc40`)

#### MIR Swarm campaign planning

47 `docs(mir-swarm)` commits cover Wave 0 retrospective, Wave 1 lock ledger
rescore, P2 goal-check audits, P3 delivery audits, P1 supplementary goal forge,
gap-forge queue management, and Wave 2 goal admission. Process docs codify the
three-pass goal lowering pipeline, Vivi planning lessons, and fleet authority
deferral. All 12 Wave 2 goals reached READY status.

Representative:

- `docs(mir-swarm): add three-pass goal lowering pipeline` (`efbb3ae74`)
- `docs(mir-swarm): Wave 1 lock ledger rescore — 15 rows updated` (`2e0e27dd0`)
- `docs(mir-swarm): gap-forge-queue — 12 Wave 2 goals at READY` (`4a414189c`)

#### Inference & fragment architecture

The inference blocker matrix was updated to distinguish safetensors F32
(product-ready) from parked items (GGUF, tokenizer, quantization). A fragment
architecture design doc (`fragment-architecture.md`) defines the fragment
concept, rung ladder, tier model, and dtype policy (f32-only). Activations
target rows were added to the tensor systems matrix.

- `delivery: D-P-04 safetensors ingest — 4-stage serial unit graph` (`3ef24aa15`)
- `d-p-03 S1: fragment architecture design note` (`aef79e4d7`)
- `d-p-04 S4: update inference blocker matrix for safetensors availability` (`7175b728f`)
- `U4: Activations target rows + TensorOps blocker update` (`17473f18a`)

### Other changes

- Fix backward parser: `unknown_annotation_family` now treated as skip, fixing
  231+ test failures (`2b8cb69a1`)
- Ratchet hygiene budgets to match current source state (`848564f00`)
- Eliminate parallel cross-module `FABER_LIBRARY_HOME` env var race in tests
  (`492add128`)
- Fix `str::replace` patterns for 8-arg `layout_matches` (`00909fda2`)
- Restore varying validation + graphics pipeline reflection tests
  (`fee457fc3`)
- Add verifier-valid LLVM integration tests, remove dead code
  (`fee457fc3`)
- Fix WASM `value_expr` to return actual Wasm instruction type instead of MIR
  semantic type (`834213a16`)
- WGSL test: reject duplicate source vertex locations (`d04c4bf81`)
- Fix LLVM `llvm.sqrt.f32/f64` intrinsic declaration before use
  (`8e36c429f`)
- Suppress false positive in diagnostic text ratchet for `radix_lane_test`
  (`396497cb5`)
- Fix `doc_markdown` backticks in `tensor_operation_floor` (`6b526e62d`)
- `cargo fmt` import reordering (`4c0c8fc3b`)
- Fix reflection-reciprocity doc accuracy + stale citations
  (`707699089`)
- Fix false counter invariant in design doc — destroyed is subset of retired
  (`1a395bc24`)
- `release(radix): v0.77.0` — bump all 22 workspace crates to `0.77.0`
  (`10e555055`)

### Verification

Recorded on the release commit (`bcdfd06fa`):

| Gate | Result |
| --- | --- |
| `cargo build --locked --release -p radix --bin radix` | pass |
| `./target/release/radix --version` | `radix 0.77.0` |
| `cargo clippy -p radix -- -D warnings` | pass |
| `RUST_TEST_THREADS=1 cargo test --all` | pass |

### Publish

1. Push `main` (includes this notes file and version bump).
2. Annotated tag: `git tag -a v0.77.0 -m "Radix v0.77.0"`
3. Push tag: `git push origin v0.77.0` (triggers `.github/workflows/release.yml`)
   or `workflow_dispatch` with tag `v0.77.0`.
4. Confirm `faberlang/releases` publishes `radix-v0.77.0` multi-arch archives.

---

[All releases](/releases/) · [Install the current release](/start/install.html)
