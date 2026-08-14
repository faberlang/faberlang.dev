+++
title = "Compiling and targets"
section = "toolchain"
order = 2
sources = [
  "radix/docs/design/target-capability-matrix.md (40 KB)",
  "radix/README.md (Codegen Targets and HIR/MIR Split)",
  "faber targets CLI output",
  "radix/README.md (Compiler Performance section)",
]
+++

## Codegen targets

Faber has one language and many compilation contracts. Not every feature
must lower to every target. This page documents which features each target
supports, erases, warns on, or rejects.

### Policy verbs {#policy-verbs}

| Verb | Meaning |
|------|---------|
| **Support** | Lowers with intended semantics |
| **Erase** | Typechecks; codegen drops target-specific semantics |
| **Warn** | Legal Faber; no effect or degraded behaviour on target |
| **Reject** | Check or emit fails with explicit diagnostic |
| **Defer** | Parses/binds; lowering not implemented for any target |
| **Limited** | Stable contract with explicit subset gates |

### Target table {#target-table}

| Target | Lane | Build | Run | Package | Policy |
|--------|------|-------|-----|---------|--------|
| `rust` | HIR | yes | yes | yes | **Support** (widest package product surface today) |
| `fhir` | HIR | yes | yes | yes | **Support** |
| `fmir-text` | MIR | yes | yes | yes | **Support** |
| `fmir` | MIR | yes | yes | yes | **Support** |
| `fmir-bin` | MIR | yes | yes | yes | **Support** |
| `faber` | HIR | yes | no | no | **Support** |
| `ts` | HIR | yes | no* | no | **Probe** (measured e2e floors rising) |
| `go` | HIR | yes | no* | no | **Erase** (borrow modes; measured e2e floors rising) |
| `wasm` | MIR | yes | no | no | **Limited** |
| `wasm-text` | MIR | yes | no | no | **Limited** |
| `llvm-text` | MIR | yes | yes* | no | **Limited** |
| `metal-text` | MIR | yes | yes* | no | **Limited** |
| `wgsl-text` | MIR | yes | no | no | **Limited** |
| `sexp` | MIR | yes | no | no | **Limited** |

*`run` via device execution: `faber run --backend cuda` (llvm-text) /
`--backend metal` (metal-text) launches `@ nucleum` kernels on a real GPU;
`-t llvm-text` / `-t metal-text` themselves remain emit-only. TypeScript and
Go also have exempla e2e harnesses that execute emitted code under host
toolchains; that is a measurement surface, not a `faber package` product path.

### Pipeline routing {#pipeline-routing}

```
Source → Lex → Parse → Collect → Resolve → Lower → Typecheck → Analysis
                                                              ↓
                                    ┌─────────────────────────┴──────────┐
                                    │                                    │
                              HIR backends                        MIR backends
                                    │                                    │
            Rust · Faber · TS · Go            fmir · wasm · llvm · metal · wgsl · sexp
```

### Application lane (HIR) {#application-lane-hir}

| Target | Measured floor (exempla e2e floors, 2026-08-07 HEAD) |
|--------|---------------|
| Rust | Widest package product surface today. Borrow modes, CLI generation, failable Result lowering. |
| Faber | Canonical source view / round-trip. Not an execution backend. |
| TypeScript | Floors: 288 analysed · 289 emitted · 285 typecheck-valid · 283 runnable. Modular-width words, Valor JSON-root, identifier sanitation, and host-backend hardening in recent work. |
| Go | Floors: 251 pass · 304 accepted outcomes. Type carriers (vector/intervallum/tensor-bracket), valor/instans, reserved-word sanitation; borrow modes erased; `ad` rejected. |

### Systems lane (MIR) {#systems-lane-mir}

| Target | Role |
|--------|------|
| fmir* | Package MIR images; runner proves source independence. |
| wasm / wasm-text | Full-language MIR → Wasm surfaces (limited host imports). |
| llvm-text | Full-language MIR staging IR. **Also** the NVVM→PTX staging chain used by **CUDA device execution** (`faber run --backend cuda`). There is no separate `cuda` emit target. |
| metal-text | **Device-kernel subset** shader text (MSL). Real device runs use `faber run --backend metal`, not “% of whole-language corpus.” |
| wgsl-text | **Device-kernel subset** shader text (WGSL) for WebGPU hosts. |
| sexp | Validation / Racket-oriented dump. |

**Do not read Metal/WGSL “2% capable” rows on the [target matrix](/toolchain/target-matrix.html) as product completeness.** Those
rows score *full-language corpus terms* against a *kernel-only* emitter. The
accepted dual-backend training path is proven on **Metal and CUDA** through
`faber run --backend metal|cuda` (see [device execution](#device-execution)).

For a **device-kernel product summary** (backends, workload families, expanding
CUDA hardware matrix) see
[Target matrix · Device kernel support](/toolchain/target-matrix.html#device-kernel-support).

For live capability flags, run `faber targets`.

### Full lowerability matrix {#full-matrix}

The large term × target tables (HIR application lane and MIR systems lane)
live on the [Target compatibility](/toolchain/target-matrix.html) page. That matrix
is generated from `faber/docs/EBNF_MATRIX.md` and reports **term lowerability only** —
not erase/warn policy, and not GPU product health. GPU backends and the “why
no CUDA column?” note are explained in that page’s summary.

## Compilation lanes

Faber has a single shared frontend — lex, parse, typecheck — and then forks into
multiple lowering routes depending on what the target needs. The intermediate
representations form a pipeline: source is analysed into HIR, optionally lowered
to MIR, and optionally detoured through AIR before final emission. Each IR serves
a distinct purpose, and each target consumes from whichever IR matches its needs.

### Pipeline overview {#overview}

```text
Source (.fab)  →  Lex  →  Parse  →  Collect  →  Resolve  →  Lower  →  Typecheck  →  Analysis
                                                              │
                                                    HIR (semantic core)
                                                    ┌─────┴─────┐
                                                    │           │
                                              Reader locale    MIR lowering
                                              (input/output)    │
                                                                │
                                                      ┌─────────┴─────────┐
                                                      │                   │
                                                CPU lanes           GPU lanes
                                                      │                   │
                                            ┌────┬────┼────┬────┐     ┌───┴───────┐
                                            │    │    │    │    │     │           │
                                          FMIR LLVM WASM  TS  Go   WGSL   Metal
```

The same frontend serves every target. After semantic analysis produces the HIR,
the compiler chooses a route based on the target:

- **HIR-direct** — emit directly from typed HIR for language-shaped backends (Rust, Faber, TypeScript, Go)
- **HIR → MIR** — lower to execution-shaped MIR, then emit for systems and low-level targets
- **HIR → MIR → AIR → MIR** — detour through pure-functional AIR for autodiff and fusion transforms, then rejoin MIR

### HIR — High-Level Intermediate Representation {#hir}

The HIR is the truth. It is a typed, language-shaped IR that preserves
declarations, type information, and structural relationships. Every Faber
program, regardless of its original locale or target destination, passes
through this representation.

#### Reader locale integration {#reader-locale-integration}

Reader locale operates through the HIR. A Faber source file written in Thai
keywords is parsed and lowered into the same HIR as the equivalent Latin
source. The locale is a surface rendering of the HIR, not a fork in the
semantic core.

- **Input:** localised source (Thai, Chinese, Arabic, etc.) → normalised HIR — **shipped**
- **Output:** HIR → localised source re-emission — **shipped** (`faber format --locale <locale>`)

`faber format --locale=th-TH` round-trips any Faber source through the HIR and
emits it with Thai keywords, completing the symmetry: the same HIR can produce
any locale surface, just as it can produce any target backend. `--locale la`
reproduces the former `--canonical` re-emit surface.

#### HIR-direct backends {#hir-direct-backends}

These targets emit directly from the typed HIR without lowering to MIR. They
preserve source-level structure longer and are suited for language-shaped output:

| Target | Status | Role |
|---|---|---|
| `Rust` | **Support** | Widest package product surface today (build/run/test via Cargo). One projection of HIR — not the semantic center. |
| `Faber` | **Support** | Canonical source view via `forma` formatter. Round-trip stability. |
| `TypeScript` | Probe | HIR-direct emission + rising exempla e2e floors. Not a `faber package` product path yet. |
| `Go` | Erase | HIR-direct emission + rising exempla e2e floors; borrow modes erased; `ad` rejected. |

### MIR — Mid-Level Intermediate Representation {#mir}

MIR is the execution-shaped IR. It represents control flow, locals, runtime
calls, places, branches, and error edges — the facts that low-level targets
need. Where HIR preserves source structure, MIR flattens it into a
control-flow graph.

HIR → MIR lowering translates language-shaped constructs into execution steps.
MIR is validated after lowering to catch structural issues before any backend
attempts emission.

> **Semantic ownership.** Faber maintains a clear boundary between rules
> enforced in the HIR/MIR (type checking, definite assignment, borrow mode
> lints) and rules left to target toolchains (Rust lifetime analysis, Go type
> safety). This prevents the compiler from duplicating work that target
> compilers already do correctly.

### AIR detour {#air}

AIR (Autograd / AI Representation) is a pure-functional transform detour off
the HIR → MIR path. It is entered by explicit annotation on individual
functions:

```faber locale=la
@ radix lane "air"
functio loss(numerus predicted, numerus expected) → numerus {
    fixum numerus delta ← predicted - expected
    redde delta * delta
}
```

AIR-lane functions must satisfy a purity policy — no mutation, no effects,
no loops. Functions that violate this are rejected with a diagnostic before
AIR lowering begins. The rest of the program continues to use ordinary Faber
with mutation, effects, and loops.

After the AIR transforms complete their work (autodiff and fusion — both
shipped), the result is re-lowered to MIR and rejoins the ordinary MIR
backend pipeline. AIR owns no backends and no independent typechecker — it
is a transform checkpoint, not a parallel IR.

```text
HIR  →  AIR purity check  →  HIR to AIR lowering  →  AIR validation  →  AIR to MIR re-lowering  →  MIR backend
```

This architecture mirrors JAX's approach: keep a pure-functional
representation for transforms, lower to imperative IR only at the end.
AIR exists because running autodiff over imperative MIR would require
reconstructing purity from code that was lowered into mutation.

### CPU target lanes {#cpu}

CPU targets consume MIR and produce either executable artifacts or text for
external toolchains. Faber emits text where possible and relies on lower-level
toolchains for the final compilation step — analogous to how a C compiler
emits assembly for the assembler and linker.

#### FMIR — Faber's own MIR runtime {#fmir}

FMIR is the MIR-native package executor. The compiler extracts MIR into a
binary payload and wraps it with a short Rust kernel loader. This produces
a self-contained executable that runs the MIR through Faber's in-process
stepper — no separate runtime installation required.

| Format | Description |
|---|---|
| `fmir-text` | Inspectable FMIR text image at `target/faber-mir/image.fmir.txt` |
| `fmir` | Compact binary FMIR image at `target/faber-mir/image.fmir` |
| `fmir-bin` | Self-contained runner at `target/faber-mir/exe/run` — embeds FMIR bytes |

#### LLVM text {#llvm}

Faber emits LLVM IR as text (`.ll`), not as integrated LLVM codegen.
The emitted IR is intended for external toolchain steps — verification,
optimisation, and native code generation are handled by downstream LLVM tools.
This is a staging and validation target, not a native codegen path embedded in
the compiler.

#### WASM {#wasm}

Faber emits WebAssembly text (`.wat`) and binary (`.wasm`)
formats. The emitted Wasm uses external host imports (`faber_*`
runtime symbols) and is validated through `wasm-tools validate`.
Wasm is a supported-with-limitations target — it proves the MIR lowering
pipeline for an open standard format, but is not a package delivery runtime.

| Format | CLI target | Output |
|---|---|---|
| `wasm-text` | `-t wasm-text` (alias `wat`) | WAT text format |
| `wasm` | `-t wasm` | Binary Wasm module |

#### TypeScript and Go (HIR-direct) {#typescript-go}

TypeScript and Go are HIR-direct proof targets: they validate that Faber's
semantics translate into widely used type systems. Measured exempla e2e floors
for both rose substantially in the 2026-08 HIR compatibility pass (Go pass
floor 251; TypeScript runnable floor 283). Full package build/run/test product
workflows still center on the Rust package path today — that is a packaging
convenience, not a claim that HIR meaning lives in Rust.

### GPU target lanes {#gpu}

#### WGSL (via WGPU) {#wgsl}

Faber emits WGSL compute shader source through the MIR pipeline. The emitted
WGSL is validated through `naga` (30.x) and includes a reflection
sidecar for bind-group metadata. This covers the device-safe kernel subset:
rank-1 `f32` device views are supported; rank-2 views reject. WGSL
is not a GPU launch runtime — Faber emits the shader source, but execution
requires an external WebGPU runtime. The [Triga](/libraries/triga.html)
library supplies the typed geometry, scene, and resource contracts consumed
by the sibling `hosts/webgpu-browser` host.

#### Metal {#metal}

Metal compute shader text emission follows the same pattern as WGSL: Faber
emits Metal Shading Language source for the device-safe kernel subset. The
Metal campaign was reopened on 2026-08-02 after the frozen probe regressed
undetected during its pause (see
`radix/docs/factory/phase-metal-campaign-pause-state.md`); the emitter now
covers a training surface (Transpose+, elementwise `train_step` / companion
VJP, Tanh, fused matmul+elementwise). Metal and CUDA are the product **device execution** paths for the accepted
bounded training proof (`faber run --backend metal|cuda`). Metal is the
Apple Silicon local-dev and API-parity host; CUDA is the NVIDIA deployment
host. WebGPU remains a browser graphics / headless proof lane (Triga +
`hosts/webgpu-browser`), not the product training or inference path.

#### Device execution (Metal / CUDA) {#device-execution}

A package carries a device program when its source declares an `@ nucleum`
compute kernel and its manifest declares a `[device]` section. The FMIR
image's `device` section embeds the canonical device program plus Metal MSL
and CUDA PTX artifacts, each with a provenance hash. `faber run --backend
metal|cuda|auto` runs it through a real device session (load → allocate →
copy-in → launch → sync → readback → release) and fails closed with stable
codes (`E_BACKEND_UNAVAILABLE`, `E_DEVICE_*`, `E_NO_DEVICE_PROGRAM`) instead
of silently falling back to CPU. The surface covers forward kernels and
training loops — a library-backed `train_step` / companion VJP with per-step
observation cadence, gradient-slot → buffer mapping, and end-of-run readback.
Proof fixture: `examples/training/device-summa`.

### Architecture note {#comparison}

Faber's compilation architecture is similar in spirit to how the Rust compiler
works. Rust lowers through HIR → MIR → LLVM IR, embedding the LLVM toolchain
directly for final native codegen. Faber takes a softer approach: it emits
text for external toolchains (LLVM text, WGSL, Metal, WAT) rather than embedding
them, while reserving direct code emission for its own runtime (FMIR) and its
widest package product surface today (Rust, where Cargo and rustc handle the downstream
pipeline).

The text-emission approach means Faber never needs to bundle LLVM, a Wasm
runtime, or a GPU driver — those remain external dependencies chosen by the
user. The tradeoff is that Faber cannot offer a single-command build for every
target; the user must install the appropriate toolchain for their chosen
backend.

### Target summary {#matrix}

| Target | IR | Family | Build | Run | Package |
|---|---|---|---|---|---|
| `Rust` | HIR | CPU | yes | yes | yes |
| `fhir` | HIR | — | yes | yes | yes |
| `fmir` / `fmir-bin` | MIR | CPU | yes | yes | yes |
| `Faber` (format) | HIR | — | no | no | no |
| `TypeScript` | HIR | CPU | no | no | no |
| `Go` | HIR | CPU | no | no | no |
| `LLVM text` | MIR | CPU | no | yes* | no |
| `WASM` / `WAT` | MIR | CPU | no | no | no |
| `WGSL` | MIR | GPU | no | no | no |
| `Metal` | MIR | GPU | no | yes* | no |

*`run` via device execution (`faber run --backend cuda` / `--backend metal`).

*`build`, `run`, and `package` describe Faber workflows. External toolchains (rustc, wasm-tools, naga) handle final compilation for text-emission targets.*

Full measured grammar × target lowerability (every corpus term, HIR and MIR
columns): [Target compatibility](/toolchain/target-matrix.html).

## Compiler performance

Radix's frontend scales roughly linearly with source size, in-process and
single-threaded.

### Frontend compile times {#frontend-compile-times}

| Program size | Source | Median compile |
|-------------|--------|---------------|
| 100 functions / ~650 lines | ~10 KB | ~0.6 ms |
| 500 functions / ~3.3K lines | ~52 KB | ~3 ms |
| 1,000 functions / ~6.5K lines | ~105 KB | ~6 ms |
| 5,000 functions / ~32K lines | ~530 KB | ~37 ms |

The largest real example today is ~140 lines, well below the noise floor.

### Backend costs (Rust target) {#backend-costs-rust-target}

For `faber build`, the user-perceived time is dominated by Cargo/rustc,
not by Faber's frontend:

| Phase | Cost |
|-------|------|
| Cold `faber` dep compile (once per target dir) | ~2.8 s |
| Cold `tokio` dep compile (only when needed) | ~2.3 s |
| Warm per-program build (cached deps) | ~30–110 ms |
| Per-program Cargo invocation overhead | ~400 ms |

### Incremental compilation {#incremental-compilation}

The `faber-runtime` crate compiles once per target directory and is cached
as `.rlib` artifacts:

| You change | faber-runtime crate | Your program |
|-----------|-------------------|-------------|
| Your program source | cached | recompiles |
| `norma/src/*.fab` (Faber source) | cached | recompiles |
| `faber/runtime/rust/src/*.rs` | recompiles once | recompiles |

The trap to avoid is building each program into a fresh `target/`.
Reuse a shared `--target-dir` to keep cached `.rlib`s warm.
