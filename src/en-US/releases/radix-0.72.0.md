+++
title = "Radix 0.72.0"
section = "releases"
order = 25
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.72.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

HIR provider emit and matrix work: CPU matrix register/applica subset, vector/matrix parity, WGSL stage-1 subset.

### Scale
| Signal | Count |
| --- | ---: |
| Commits (no merges) | 82 |
| `feat(...)` commits | 41 |
| `fix(...)` commits | 7 |
| `docs(...)` commits | 31 |
| Date span | 2026-07-10 → 2026-07-10 (single day) |

### Major tracks

#### HIR-v1 provider emit (G1–G5 measurement matrix)

Land the **analyzed application contract** (`e7a1a9851`): a coherent snapshot
(HIR, types, resolver, annotation contracts, function facts, resolved uses,
qualified identity) built only through analysis. Add `AnalyzedUnit` with
`annotation_contracts` and fact tables; HIR backends install shared function
facts; production emission routes through `generate_from_analyzed`.

Target-neutral **G2 mode and access traps** (`36ec2a6ea`): split de/in/ex mode
analysis from Rust lifetime qualification. Plain lista/textus/tabula access
traps on absence for Rust/TS/Go; optional paths stay accipe/tensor bracket.

**G3 structured emission needs** (`33c2a9a5f`): introduce `RustNeeds`/`TsNeeds`/
`GoNeeds` collectors driven by HIR and type tables. Rust prelude no longer scans
body text for runtime types. Wire `resolved_uses` on analyzed emit.

**G4 package spine and P2 artifact plan** (`9f8289c11`): add target-neutral
`PackageId`/`ModuleId`/`ExportId`/`BindingId` identities and `AnalyzedPackage`
composition with distinct package-dependency vs source-import edges. Expose an
inspectable deterministic artifact plan for Rust/Go/TS with fail-closed
rejection.

**G5 target qualification measurement matrix** (`f8f1dd389`): bridge
`qualify_for_target` to `classify_hir_coverage` gap slugs, add stable slug
fixtures, and ship a fast exempla HIR matrix (rust/go/ts/faber) with pinned
floors and `scripta/hir-target-coverage` for `--full`.

Provider import plumbing:
- Unblock `triga` provider imports with two-phase file-interface install; emit
  `de`/`in` parameters as `&T`/`&mut T` with matching call sites; nullable
  `est nihil` uses `Option::is_none` so payload `PartialEq` is not required
  (`93e1c682e`)
- Resolve provider imports and `de` field loads: wire radix check/emit contracts
  to `FABER_LIBRARY_HOME` provider modules, skip partial export failures
  instead of dropping the whole interface, clone non-Copy fields through de/in
  (`93ecd2ba0`)
- Emit provider imports as Rust modules with typed paths: single-file emit
  materializes file-namespace providers as `pub mod` blocks, wires
  `ImportedNamespaceInfo` for `crate::ns::name` paths (`d5b5c17af`)
- Fix auto-deref de/in borrow ABI in path emission: provider-import emit uses
  `&T`/`&mut T`; path loads/stores must deref the payload (`33502365b`)

#### MIR: CPU matrix register matmul and applica subset

Admit nested-lista matrix materialize (≤4×4), expand matmul and `matrix.applica`
into cell/lane mul-add MIR, and execute construct/cell/lane paths in the
stepper. GPU/device parity remains out of scope (`582701f5d`).

Add `MirUnOp::Sqrt` and expand register-vector length/normalize (Triga near-zero
→ zero policy). Admit square 2×2 inverse and affine 4×4 inverse with
singular→nihil `Option`. GPU matrix targets stay fail-closed (`a02a00fd8`).

Add CPU stepper evidence for the shared register-vector subset and for the T*S
point product matching `triga-transforms.fab` numbers (7,4,-1). Row-major
language matrix with column-vector applica (`436ff0bff`).

#### LLVM host Stage 4 lowerings (4AA–4AF)

Lower valor map-literal via `map_new` (Stage 4AA) (`cd18070e2`), array-literal
via `array_new` (Stage 4AB) (`cfda0ef8c`), intervallum via versioned ABI
(Stage 4AC) (`ab57113a9`), and collection convert bridges — lista↔copia,
tabula↦lista keys/values, lista↔cursor (Stage 4AD) (`77d6f5b10`).

Close isolable aggregate residuals: empty valor maps and tabula index, plus
tensor→valor boxing (Stage 4AE) (`4e4643c21`). Unique sparse construct status
latch ids to fix `llvm-as` collisions (Stage 4AF) (`441a2f795`).

Lower scalar numeric intrinsics (`0aed139b0`), lista value methods
(`89bb0e567`), lista option results (`314c19163`), unified option lowering ABI
(`7cd5529a3`), lista order and sum (`bae31b737`), text handles and formatting
(`c00af6cb6`), text query transformations (`6bc3620a0`), and text scalar
conversions (`1ab433936`).

Lower map and set runtime (`38f86e14b`). Valor scalar conversions
(`1ab433936`), opaque Valor aggregates (`e958ef48c`), atomic Valor genus
conversions (`1da7c84c7`), typed octeti operations (`cb6c30d7b`), and typed
instans conversions (`9b15d1ddd`).

Lower typed tensor core carrier (Stage 4V) (`1a22f7b1e`), tensor arithmetic
family (Stage 4W) (`ad03cd06d`), tensor conversion bridges (Stage 4X)
(`4e534c8d6`), sparse tensor carrier (Stage 4Y) (`b3d3f6b62`), and regex
conversion (Stage 4Z) (`02830b4e5`).

Gap ledger documentation across the range: residual census (`327a860f4`),
regeneration (`f70af7ffb`), pairwise floor note (`93d04c3ef`), stage ownership
rebaseline (`7e8815670`), and volatile campaign totals removal (`ebac8696b`).

#### Host parity: WASM, CUDA, macOS/ARM

WASM host:
- Prove B2 second wasm-host fixture via `functio.fab` through `WasmRtV1Host`:
  pure `faber_rt_v1` with `nota_ptr` plus `nota_i64`, multi-function exports,
  stdout matches corpus expected (`b410ab70c`)
- First `faber_rt_v1` product run on wasm-host-parity (`4d6ab8847`)
- Align closed-set host imports to CPU ABI v1: map overlapping wasm-text ops
  onto `__faber_rt_v1_*` symbols and retire dual dialect (`c9fa87848`)
- Drop unused host ABI symbol imports (`ca82ce206`)

CUDA host:
- Admit CUDA host path A with fail-closed discovery (`ac2b9d9ac`)
- Emit NVVM kernel metadata for CUDA leaf (`6b37bb751`)

macOS/ARM:
- Adapt `macos-arm64` to public provider crates: register host-kernel plus five
  core public providers, delete duplicated private `norma` family handlers
  (`0049f439c`)

#### WGSL / WebGPU stage-1 subset

Define browser product boundary with structured failure kinds (artifact-fetch,
reflection, webgpu, product), Node product-boundary checks, explicit
product/serve/inspection contract, and honest delivery closeout: static+boundary
non-GPU evidence (`5b7260be1`, `2c6217251`).

Plan and close wgpu phase documentation: product boundary admission,
phase status correction, and host parity goal definition (`03081b5b0`,
`389f27e50`, `e4866047f`, `ecfaac463`).

#### Native host bootstrap and codegen

Emit structured native host bootstrap: add package-only `native_host_bootstrap`
so generated entrypoints call `host_register::install_or_exit` without rewriting
source text (`91ef4302b`). Close solum live route residuals (`4ce91cd7d`) and
Platform P6 authority (`05d87fc15`).

### Other changes

- Style: cargo fmt for matrix/normalize and de/in paths (`cc3919c77`)
- Fix(llvm-host): unique sparse construct status latch ids to fix `llvm-as`
  SSA collision (Stage 4AF) (`441a2f795`)
- Fix(mir): validate sparse shape queries (`dc3fa705c`)
- Fix(rust): auto-deref de/in borrow ABI in path emission (`33502365b`)
- Fix(hir): unblock triga provider imports and Rust de/nil ABI (`93e1c682e`)
- Fix(hir): resolve provider imports and de field loads for Triga (`93ecd2ba0`)
- Fix(hir): emit provider imports as Rust modules with typed paths (`d5b5c17af`)
- Factory docs: draft faber-mir-v1 release roadmap campaign (`38f86e14b`),
  CPU host ABI v1 unify sidecar goal (`2a05ba028`), operator-managed worktree
  packets (`9bdcde389`), HIR-v1 delivery queue (`1f339134a`), HIR-v1 release
  roadmap (`b77025b83`)
- MIR-v1 documentation: block routing (`26ef8c99c`), host north-star gates
  (`b82c559c9`), FMIR reference executor assessment (`1cb1cba11`), ledger
  contract freeze (`c405c29e5`), packet coordination handoff (`6a4e9fdaa`),
  multiple host parity goal definitions and phase status updates

---

[All releases](/releases/) · [Install the current release](/start/install.html)
