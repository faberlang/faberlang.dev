+++
title = "Target compatibility"
section = "targets"
order = 2
sources = "radix/EBNF_MATRIX.md · target-capability-matrix.md · faber targets"
+++

Faber is one language with many compilation contracts. This page is the
**measured lowerability matrix**: for each corpus term, which targets can
lower it, and at what support level.

Policy verbs (support / erase / warn / reject / defer) and pipeline routing
live on [Compiling and targets](/toolchain/compiling.html). This page is the
large scannable row list — HIR application-lane targets and MIR systems-lane
targets side by side in the tables below.

Live CLI summary: `faber targets`.

**Generated**: unknown by `scripta/generate-ebnf-matrix.py` — **do not edit**.
**Measurement**: `emit_hir_target_matrix` + `emit_mir_target_matrix` (in-process, no external toolchains).
**Join**: `corpus/index.toml` terms → exempla.

This is the **official generated** grammar×target support matrix. It reports
**lowerability** — can target X lower grammar production Y — across every term in
the exempla corpus. Runtime semantics (erase/warn/defer policy verbs), per-target
contracts, and pipeline routing live in
[Compiling and targets](/toolchain/compiling.html), which links here for the rows.

## Legend

| Glyph | Meaning |
|---|---|
| ✓ | fully supported — all analyzable exempla for the term lower |
| ◐ | partial — some exempla lower, some have a measured gap |
| ○ | planned — not yet lowering; curated overlay (`scripta/ebnf-matrix-overrides.toml`) |
| ✕ | not supported — no exempla lower; default-truth, measured gap is real |
| — | not measured — no analyzable exempla for this term on this lane |

> A ✓ means the corpus exempla exercising this term lower to the target. It does
> **not** guarantee identical runtime semantics. Some targets *erase* or *warn* on
> certain constructs (e.g. Go erases borrow modes `de`/`in`/`ex`) — those still
> render ✓ here because they lower. See the policy doc for that nuance.

## Corpus-wide summary (all registered terms)

### How to read these percentages

This matrix answers one narrow question:

> For each **general-language corpus term**, does the named **emit target**
> lower the term's exempla?

It is **not** a product completion score for Metal, CUDA, or GPU training.

- **Application HIR** percentages (Rust / Go / TS / Faber) are fair "how much of
  the language emits" scores for host-language projections.
- **General MIR** percentages (llvm-text, wasm, sexp, …) score ordinary systems
  IR emission over the same full corpus.
- **Device-kernel emitters are not scored here.** `metal-text` and `wgsl-text`
  lower a device-safe kernel surface — `@ nucleum` compute kernels and related
  GPU views — and deliberately nothing else: no packages, async, CLI, full
  control flow, or host libraries. Measuring them against all ~280
  general-language terms answers a question that does not apply to them, so
  this matrix does not ask it. Their real support is the
  [device kernel support](#device-kernel-support) summary below, and real
  device execution runs through `faber run --backend metal`.
- **There is no `cuda` column.** CUDA is not a text emit target. CUDA device
  programs are produced on the **NVVM → PTX** path (staged with **llvm-text** /
  MIR device emission) and run with `faber run --backend cuda`. Product GPU
  backends are **Metal** and **CUDA**; matrix columns track **emit surfaces**,
  not every host session.

For product policy (build/run/package, erase/reject, device backends), use
[Compiling and targets](/toolchain/compiling.html) and `faber targets` — not
these corpus rows as a quality score.

**Application lane (HIR → emitted source languages)**

| target | capable | analyzable | % |
|---|---|---|---|
| rust | 278 | 280 | 99% |
| go | 262 | 280 | 94% |
| ts | 274 | 280 | 98% |
| faber | 280 | 280 | 100% |

**Systems lane (MIR → device/IR artifacts)**

| target | capable | analyzable | % |
|---|---|---|---|
| llvm-text | 277 | 280 | 99% |
| wasm-text | 257 | 280 | 92% |
| wasm | 257 | 280 | 92% |
| sexp-struct | 222 | 280 | 79% |
| sexp | 222 | 280 | 79% |
| scena | 238 | 280 | 85% |

## Device kernel support (product summary) {#device-kernel-support}

This section is the **GPU product view**. It is intentionally separate from the
corpus % tables below.

**Status of measurement (2026-08-07):** dual-backend training proofs and local
device fixtures are accepted on named machines. A multi-card CUDA verification
matrix (ephemeral cloud pods) is **active and expanding** — more rows land as
RunPod lanes and Faber package fixtures close. Numbers here are **evidence snapshots**, not a permanent completion score.

### Product backends

| Backend | How you run it | Emit / artifact chain | Accepted product proof (current) | Not claimed |
|---|---|---|---|---|
| **Metal** | `faber run --backend metal` | MIR → Metal MSL in the package device image | Dual-backend **MLP training** (100 deterministic steps, gradient mapping, numeric oracle) on Apple Silicon (burgus M-class). Starter fixtures under [`examples/training/`](https://github.com/faberlang/examples/tree/main/training). | General training framework; all SM/GPU models; multi-device |
| **CUDA** | `faber run --backend cuda` | MIR → NVVM → PTX in the package device image (llvm device chain) | Same dual-backend **MLP training** proof on NVIDIA (pharos RTX 5070 class). Same fixture family. | General GGUF inference product; multi-GPU product |
| **WebGPU** | browser / headless host path | MIR → WGSL text | Workload-shaped chain proofs on the WebGPU route (e.g. tiny linear + ReLU device fragments) | Dual-backend training product claim; Metal/CUDA parity |

### Workload / kernel families (measured so far)

Statuses use three labels only:

| Label | Meaning |
|---|---|
| **Proven** | Real-device evidence packet / oracle PASS on a named backend |
| **Emit / staging** | Compiler or host can produce artifacts; full numeric device gate not claimed here |
| **Building** | In active development; do not treat as shipped |

| Family / fixture | Metal | CUDA | WebGPU | Notes |
|---|---|---|---|---|
| Forward kernels + `device-summa` class | **Proven** (local) | **Proven** (local pharos; cloud matrix expanding) | — | Ordinary `faber run --backend …` package path |
| Dual-backend MLP train (Gradus surface, 100 steps) | **Proven** | **Proven** | — | Oracle authority: `examples/training/mlp` (`device_image.metal` / `.cuda` PASS) |
| Elementwise / fused matmul+elementwise / train_step · VJP surface | **Proven** (training path) | **Proven** (training path; residual Stage-6 rows may still be in repair) | Emit / staging | Product claim is the **accepted training path**, not every Stage-6 capstone |
| GPU workload rungs 0–4 (`examples/gpu-workload`) | Emit / staging | Emit / staging | Partial **Proven** chain (rungs 1–2 style device fragments) | Systems-track oracles; CUDA-route output-checked floors still low — see package README honesty |
| Transformer / BERT-tiny training capstone | Building | Building | — | Metal has stronger local evidence than CUDA on some Stage-6 rows; CUDA numeric repair in flight — **not** a public PASS claim |
| GPU inference (GGUF recipes, device prefill) | Building | Building | — | CPU oracle track real; end-to-end **device** inference not shipped |

### CUDA hardware verification matrix (cloud, expanding)

Opt-in **RunPod** lanes exercise short CUDA proofs on cards the operator does
not own. This is **verification infrastructure**, not a new product backend.

| Card / class | Role | Latest public snapshot (2026-08-06 first matrix) | Notes |
|---|---|---|---|
| RTX 4090 (consumer Ada) | Bootstrap / harness | **PASS** (toolchain probe) | Optional consumer lane |
| RTX 5090 (consumer Blackwell) | SM coverage | **PASS** (toolchain probe) | Driver/CC diversity |
| RTX 3090 (consumer Ampere) | Older consumer | **PASS** (toolchain probe) | |
| L40S (datacenter Ada) | Middle datacenter | **PASS** (toolchain probe) | Named lane `dc-l40s` |
| H100 80GB (datacenter Hopper) | Newer datacenter | **PASS** (toolchain probe) | Named lane `dc-h100` |
| A100 80GB (datacenter Ampere, **sm_80 PTX baseline**) | Baseline lane `dc-a100` | First-hour **AVAILABILITY** (out of stock); **rung-0 matmul closure later reported PASS** on `dc-a100` | Baseline PTX policy A; same-artifact Faber package matrix still expanding |

**Honesty bounds on the cloud matrix:**

1. The **first** multi-card receipt was largely a **per-pod compile+run viability** probe (same small CUDA program, pod-local toolchain), not a claim
   that every card already ran the full dual-backend MLP oracle.
2. **Same-artifact** Faber package portability (`device-summa` / training
   fixtures on one PTX blob across cards) is the follow-on track — active now.
3. Metal stays on **local** Apple Silicon acceptance hosts; RunPod lanes are
   **CUDA only**.
4. Expect this table to **grow** as more lanes, fixtures, and receipts land.
   Prefer linking factory receipts over inventing percentages.

### Where to look for live evidence

| Artifact | What it proves |
|---|---|
| [`examples/training/mlp`](https://github.com/faberlang/examples/tree/main/training/mlp) | Dual-backend training oracle + `device_image` Metal/CUDA PASS notes |
| [`examples/training/device-summa`](https://github.com/faberlang/examples/tree/main/training/device-summa) | Starter device package for ordinary `faber run --backend` |
| [`examples/gpu-workload`](https://github.com/faberlang/examples/tree/main/gpu-workload) | Workload rung oracles (matmul, softmax, MLP forward, …) |
| [Device execution CLI](/toolchain/cli.html#device-execution) | Product command contract |
| [Compiling · device execution](/toolchain/compiling.html#device-execution) | Emit vs run boundary |

Internal factory control plane (not a public product surface): RunPod lane
registry and matrix receipts under the radix factory tree
(`docs/factory/runpod-gpu-verification/`).

## Keywords — application lane

### keyword

| term | rust | go | ts | faber |
|---|---|---|---|---|
| `abstractus` | ✓ | ✓ | ✓ | ✓ |
| `ab` | ✓ | ✓ | ✓ | ✓ |
| `ad` | ✓ | ✕ | ✓ | ✓ |
| `adfirma` | ✓ | ✓ | ✓ | ✓ |
| `ante` | ✓ | ✓ | ✓ | ✓ |
| `atomic` | ✕ | ✓ | ✓ | ✓ |
| `argumenta` | ✓ | ✓ | ✓ | ✓ |
| `bivalens` | ✓ | ✓ | ✓ | ✓ |
| `cape` | ✓ | ✓ | ✓ | ✓ |
| `casu` | ✓ | ✓ | ✓ | ✓ |
| `cede` | ✓ | ✓ | ✓ | ✓ |
| `ceteri` | ✓ | ✓ | ✓ | ✓ |
| `ceterum` | ✓ | ✓ | ✓ | ✓ |
| `clausura` | ✓ | ✓ | ✓ | ✓ |
| `cli` | ✓ | ✓ | ✓ | ✓ |
| `copia` | ✓ | ✓ | ✓ | ✓ |
| `cura` | ✓ | ✓ | ✓ | ✓ |
| `curata` | ✓ | ✓ | ✓ | ✓ |
| `cursor` | ✓ | ✓ | ✓ | ✓ |
| `custodi` | ✓ | ✓ | ✓ | ✓ |
| `de` | ✓ | ✓ | ✓ | ✓ |
| `descriptio` | ✓ | ✓ | ✓ | ✓ |
| `discerne` | ✓ | ✓ | ✓ | ✓ |
| `discretio` | ✓ | ✓ | ✓ | ✓ |
| `dum` | ✓ | ✓ | ✓ | ✓ |
| `ego` | ✓ | ✓ | ✓ | ✓ |
| `elige` | ✓ | ✓ | ✓ | ✓ |
| `errata` | ✓ | ✓ | ✓ | ✓ |
| `est` | ✓ | ✓ | ✓ | ✓ |
| `ex` | ✓ | ✓ | ✓ | ✓ |
| `exitus` | ✓ | ✓ | ✓ | ✓ |
| `fac` | ✓ | ✓ | ✓ | ✓ |
| `falsum` | ✓ | ✓ | ✓ | ✓ |
| `fient` | ✓ | ✓ | ✓ | ✓ |
| `fiet` | ✓ | ✓ | ✓ | ✓ |
| `figendum` | ✓ | ✓ | ✓ | ✓ |
| `finge` | ✓ | ✓ | ✓ | ✓ |
| `fiunt` | ✓ | ✓ | ✓ | ✓ |
| `fixum` | ✓ | ✓ | ✓ | ✓ |
| `fragilis` | ✓ | ✓ | ✓ | ✓ |
| `fractus` | ✓ | ✓ | ✓ | ✓ |
| `functio` | ✓ | ✓ | ✓ | ✓ |
| `futura` | ✓ | ✓ | ✓ | ✓ |
| `futurum` | ✓ | ✓ | ✓ | ✓ |
| `generis` | ✓ | ✓ | ✓ | ✓ |
| `genus` | ✓ | ✓ | ✓ | ✓ |
| `iace` | ✓ | ✓ | ✓ | ✓ |
| `iacit` | ✓ | ✓ | ✓ | ✓ |
| `ignotum` | ✓ | ✓ | ✓ | ✓ |
| `immutata` | ✓ | ✓ | ✓ | ✓ |
| `implet` | ✓ | ✓ | ✓ | ✓ |
| `importa` | ✓ | ✓ | ✓ | ✓ |
| `in` | ✓ | ✓ | ✓ | ✓ |
| `incipiet` | ✓ | ✓ | ✓ | ✓ |
| `incipit` | ✓ | ✓ | ✓ | ✓ |
| `inter` | ✓ | ✓ | ✓ | ✓ |
| `intra` | ✓ | ✓ | ✓ | ✓ |
| `instans` | ✓ | ✓ | ✓ | ✓ |
| `itera` | ✓ | ✓ | ✓ | ✓ |
| `lege` | ✓ | ✓ | ✓ | ✓ |
| `lineam` | ✓ | ✓ | ✓ | ✓ |
| `lista` | ✓ | ✓ | ✓ | ✓ |
| `matrix` | ✓ | ✕ | ✓ | ✓ |
| `mone` | ✓ | ✓ | ✓ | ✓ |
| `mori` | ✓ | ✓ | ✓ | ✓ |
| `nexum` | ✓ | ✓ | ✓ | ✓ |
| `nihil` | ✓ | ✓ | ✓ | ✓ |
| `numquam` | ✓ | ✓ | ✓ | ✓ |
| `numerus` | ✓ | ✓ | ✓ | ✓ |
| `non` | ✓ | ✓ | ✓ | ✓ |
| `omitte` | ✓ | ✓ | ✓ | ✓ |
| `omnia` | ✓ | ✓ | ✓ | ✓ |
| `operandus` | ✓ | ✓ | ✓ | ✓ |
| `optio` | ✓ | ✓ | ✓ | ✓ |
| `optiones` | ✓ | ✓ | ✓ | ✓ |
| `ordo` | ✓ | ✓ | ✓ | ✓ |
| `octeti` | ✓ | ✓ | ✓ | ✓ |
| `implendum` | ✓ | ✓ | ✓ | ✓ |
| `per` | ✓ | ✓ | ✓ | ✓ |
| `perge` | ✓ | ✓ | ✓ | ✓ |
| `postpara` | ✓ | ✓ | ✓ | ✓ |
| `postparabit` | ✓ | ✓ | ✓ | ✓ |
| `prae` | ✓ | ✓ | ✓ | ✓ |
| `praefixum` | — | — | — | — |
| `praepara` | ✓ | ✓ | ✓ | ✓ |
| `praeparabit` | ✓ | ✓ | ✓ | ✓ |
| `promissum` | ✓ | ✓ | ✓ | ✓ |
| `privata` | ✓ | ✓ | ✓ | ✓ |
| `proba` | ✓ | ✓ | ✓ | ✓ |
| `probandum` | ✓ | ✓ | ✓ | ✓ |
| `protecta` | — | — | — | — |
| `publica` | ✓ | ✓ | ✓ | ✓ |
| `redde` | ✓ | ✓ | ✓ | ✓ |
| `reddet` | ✓ | ✓ | ✓ | ✓ |
| `repete` | ✓ | ✓ | ✓ | ✓ |
| `rumpe` | ✓ | ✓ | ✓ | ✓ |
| `scribe` | ✓ | ✓ | ✓ | ✓ |
| `scriptum` | ✓ | ✓ | ✓ | ✓ |
| `secus` | ✓ | ✓ | ✓ | ✓ |
| `si` | ✓ | ✓ | ✓ | ✓ |
| `sic` | ✓ | ✓ | ✓ | ✓ |
| `sin` | ✓ | ✓ | ✓ | ✓ |
| `sit` | ✓ | ✓ | ✓ | ✓ |
| `solum_in` | ✓ | ✓ | ✓ | ✓ |
| `solum` | ✓ | ✓ | ✓ | ✓ |
| `sparge` | ✓ | ✓ | ✓ | ✓ |
| `sponte` | ✓ | ✓ | ✓ | ✓ |
| `sub` | ✓ | ✓ | ✓ | ✓ |
| `tacet` | ✓ | ✓ | ✓ | ✓ |
| `tacebit` | ✓ | ✓ | ✓ | ✓ |
| `tabula` | ✓ | ✓ | ✓ | ✓ |
| `tag` | ✓ | ✓ | ✓ | ✓ |
| `temporis` | ✓ | ✓ | ✓ | ✓ |
| `tensor` | ✓ | ✓ | ✓ | ✓ |
| `textus` | ✓ | ✓ | ✓ | ✓ |
| `typus` | ✓ | ✓ | ✓ | ✓ |
| `ubique` | ✓ | ✓ | ✓ | ✓ |
| `usque` | ✓ | ✓ | ✓ | ✓ |
| `ut` | ✓ | ✓ | ✓ | ✓ |
| `varia` | ✓ | ✓ | ✓ | ✓ |
| `variandum` | ✓ | ✓ | ✓ | ✓ |
| `vector` | ✓ | ◐ | ✓ | ✓ |
| `vacuum` | ✓ | ✓ | ✓ | ✓ |
| `verum` | ✓ | ✓ | ✓ | ✓ |
| `vide` | ✓ | ✓ | ✓ | ✓ |

## Operators — application lane

### operator-group

| term | rust | go | ts | faber |
|---|---|---|---|---|
| `⊜` | ✓ | ✓ | ✓ | ✓ |
| `∧` | ✓ | ✓ | ✓ | ✓ |
| `→` | ✓ | ✓ | ✓ | ✓ |
| `⇥` | ✓ | ✓ | ✓ | ✓ |
| `←` | ✓ | ✓ | ✓ | ✓ |
| `aut` | ✓ | ✓ | ✓ | ✓ |
| `![` | ✓ | ✓ | ✓ | ✓ |
| `!.` | ✓ | ✓ | ✓ | ✓ |
| `≠` | ✓ | ✓ | ✓ | ✓ |
| `!(` | ✓ | ✓ | ✓ | ✓ |
| `⊻` | ✓ | ✓ | ✓ | ✓ |
| `↦` | ✓ | ✓ | ✓ | ✓ |
| `⇒` | ✓ | ✓ | ✓ | ✓ |
| `‥` | ✓ | ✓ | ✓ | ✓ |
| `…` | ✓ | ✓ | ✓ | ✓ |
| `≡` | ✓ | ✓ | ✓ | ✓ |
| `=` | ✓ | ✓ | ✓ | ✓ |
| `et` | ✓ | ✓ | ✓ | ✓ |
| `≥` | ✓ | ✓ | ✓ | ✓ |
| `≤` | ✓ | ✓ | ✓ | ✓ |
| `⊖` | ✓ | ✓ | ✓ | ✓ |
| `modulus<u16>` | ✓ | ✕ | ✕ | ✓ |
| `modulus<u32>` | ✓ | ✕ | ✕ | ✓ |
| `modulus<u64>` | ✓ | ✕ | ✕ | ✓ |
| `modulus<u8>` | ✓ | ✕ | ✕ | ✓ |
| `non est` | ✓ | ✓ | ✓ | ✓ |
| `⊚` | ✓ | ✓ | ✓ | ✓ |
| `∨` | ✓ | ✓ | ✓ | ✓ |
| `∪` | ✓ | ✓ | ✓ | ✓ |
| `⊕` | ✓ | ✓ | ✓ | ✓ |
| `?[` | ✓ | ✓ | ✓ | ✓ |
| `?.` | ✓ | ✓ | ✓ | ✓ |
| `?(` | ✓ | ✓ | ✓ | ✓ |
| `§` | ✓ | ✓ | ✓ | ✓ |
| `⇐` | ✓ | ✓ | ✓ | ✓ |
| `⊘` | ✓ | ✓ | ✓ | ✓ |
| `⊛` | ✓ | ✓ | ✓ | ✓ |
| `¬` | ✓ | ✓ | ✓ | ✓ |
| `vel` | ✓ | ✓ | ✓ | ✓ |
| `∷` | ✓ | ✓ | ✓ | ✓ |
| `∴` | ✓ | ✓ | ✓ | ✓ |
| `ergo` | ✓ | ✓ | ✓ | ✓ |

## Keywords — systems lane

### keyword

| term | llvm-text | wasm-text | wasm | sexp-struct | sexp | scena |
| --- | --- | --- | --- | --- | --- | --- |
| `abstractus` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `ab` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `ad` | ✓ | ✕ | ✕ | ✕ | ✕ | ✓ |
| `adfirma` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `ante` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `atomic` | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ |
| `argumenta` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `bivalens` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `cape` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `casu` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `cede` | ✓ | ✕ | ✕ | ✕ | ✕ | ✓ |
| `ceteri` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `ceterum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `clausura` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `cli` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `copia` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| `cura` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `curata` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| `cursor` | ✓ | ✕ | ✕ | ✕ | ✕ | ✓ |
| `custodi` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `de` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `descriptio` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `discerne` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `discretio` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `dum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `ego` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `elige` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `errata` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| `est` | ✓ | ✓ | ✓ | ✕ | ✕ | ✕ |
| `ex` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `exitus` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `fac` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `falsum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `fient` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `fiet` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `figendum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `finge` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `fiunt` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `fixum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `fragilis` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| `fractus` | ✓ | ✓ | ✓ | ◐ | ◐ | ✓ |
| `functio` | ✓ | ◐ | ◐ | ✓ | ✓ | ✓ |
| `futura` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `futurum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| `generis` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `genus` | ✓ | ✓ | ✓ | ◐ | ◐ | ✓ |
| `iace` | ✓ | ◐ | ◐ | ✓ | ✓ | ✓ |
| `iacit` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `ignotum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `immutata` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| `implet` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `importa` | ✓ | ◐ | ◐ | ◐ | ◐ | ◐ |
| `in` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| `incipiet` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `incipit` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `inter` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `intra` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `instans` | ✓ | ✕ | ✕ | ✕ | ✕ | ◐ |
| `itera` | ✓ | ◐ | ◐ | ◐ | ◐ | ✓ |
| `lege` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| `lineam` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `lista` | ✓ | ✓ | ✓ | ◐ | ◐ | ✓ |
| `matrix` | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ |
| `mone` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `mori` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| `nexum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `nihil` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `numquam` | ✓ | ✓ | ✓ | ✕ | ✕ | ✕ |
| `numerus` | ✓ | ✓ | ✓ | ◐ | ◐ | ◐ |
| `non` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `omitte` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| `omnia` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `operandus` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `optio` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `optiones` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| `ordo` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `octeti` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `implendum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `per` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `perge` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `postpara` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| `postparabit` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| `prae` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| `praefixum` | — | — | — | — | — | — |
| `praepara` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| `praeparabit` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| `promissum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `privata` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `proba` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| `probandum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| `protecta` | — | — | — | — | — | — |
| `publica` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `redde` | ✓ | ✓ | ✓ | ✓ | ✓ | ◐ |
| `reddet` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `repete` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| `rumpe` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `scribe` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `scriptum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `secus` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `si` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `sic` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `sin` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `sit` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `solum_in` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| `solum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| `sparge` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `sponte` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| `sub` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `tacet` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `tacebit` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `tabula` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| `tag` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| `temporis` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| `tensor` | ✓ | ✓ | ✓ | ◐ | ◐ | ◐ |
| `textus` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| `typus` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `ubique` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `usque` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `ut` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `varia` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `variandum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `vector` | ✓ | ◐ | ◐ | ◐ | ◐ | ✕ |
| `vacuum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `verum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `vide` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

## Operators — systems lane

### operator-group

| term | llvm-text | wasm-text | wasm | sexp-struct | sexp | scena |
| --- | --- | --- | --- | --- | --- | --- |
| `⊜` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `∧` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `→` | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `⇥` | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `←` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `aut` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `![` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `!.` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `≠` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `!(` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `⊻` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `↦` | ✓ | ◐ | ◐ | ✕ | ✕ | ✓ |
| `⇒` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `‥` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `…` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `≡` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `=` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `et` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `≥` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `≤` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `⊖` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `modulus<u16>` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| `modulus<u32>` | ✓ | ✓ | ✓ | ◐ | ◐ | ✓ |
| `modulus<u64>` | ✓ | ✓ | ✓ | ◐ | ◐ | ✓ |
| `modulus<u8>` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| `non est` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `⊚` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `∨` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `∪` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `⊕` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `?[` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `?.` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `?(` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `§` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `⇐` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `⊘` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `⊛` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `¬` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `vel` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `∷` | ✓ | ✓ | ✓ | ◐ | ◐ | ✓ |
| `∴` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `ergo` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

## Other terms (`existing-home` / unspecified)

### existing-home

| term | rust | go | ts | faber |
|---|---|---|---|---|
| `alias` | ✓ | ✓ | ✓ | ✓ |
| `arena` | ✓ | ✓ | ✓ | ✓ |
| `@` | ✓ | ✓ | ✓ | ✓ |
| `f16` | ✕ | ✓ | ✓ | ✓ |
| `imperia` | ✓ | ✓ | ✓ | ✓ |
| `imperium` | ✓ | ✓ | ✓ | ✓ |
| `manifest` | ✓ | ✓ | ✓ | ✓ |
| `metior` | ✓ | ✓ | ✓ | ✓ |
| `nondum` | ✓ | ✓ | ✓ | ✓ |
| `objectum` | ✓ | ✓ | ✓ | ✓ |
| `prima` | ✓ | ✓ | ✓ | ✓ |
| `requirit` | ✓ | ✓ | ✓ | ✓ |
| `string` | ✓ | ✓ | ✓ | ✓ |
| `block-string` | ✓ | ✓ | ✓ | ✓ |
| `summa` | ✓ | ✓ | ✓ | ✓ |
| `targets` | ✓ | ✓ | ✓ | ✓ |
| `ultima` | ✓ | ✓ | ✓ | ✓ |
| `versio` | ✓ | ✓ | ✓ | ✓ |
