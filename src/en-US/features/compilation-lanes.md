+++
title = "Compilation lanes"
section = "features"
order = 2
sources = []
+++

Faber has a single shared frontend — lex, parse, typecheck — and then forks into
multiple lowering routes depending on what the target needs. The intermediate
representations form a pipeline: source is analysed into HIR, optionally lowered
to MIR, and optionally detoured through AIR before final emission. Each IR serves
a distinct purpose, and each target consumes from whichever IR matches its needs.

## Pipeline overview {#overview}

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
                                            ┌────┬────┼────┬────┐     ┌───┴───┐
                                            │    │    │    │    │     │       │
                                          FMIR LLVM WASM  TS  Go   WGSL   Metal
                                                                          (hold)
```

The same frontend serves every target. After semantic analysis produces the HIR,
the compiler chooses a route based on the target:

- **HIR-direct** — emit directly from typed HIR for language-shaped backends (Rust, Faber, TypeScript, Go)
- **HIR → MIR** — lower to execution-shaped MIR, then emit for systems and low-level targets
- **HIR → MIR → AIR → MIR** — detour through pure-functional AIR for autodiff and fusion transforms, then rejoin MIR

## HIR — High-Level Intermediate Representation {#hir}

The HIR is the truth. It is a typed, language-shaped IR that preserves
declarations, type information, and structural relationships. Every Faber
program, regardless of its original locale or target destination, passes
through this representation.

### Reader locale integration {#reader-locale-integration}

Reader locale operates through the HIR. A Faber source file written in Thai
keywords is parsed and lowered into the same HIR as the equivalent Latin
source. The locale is a surface rendering of the HIR, not a fork in the
semantic core.

- **Input:** localised source (Thai, Chinese, Arabic, etc.) → normalised HIR — **shipped**
- **Output:** HIR → localised source re-emission — **in progress** (being implemented)

When the output direction ships, `faber format --reader-locale=th-TH`
will round-trip any Faber source through the HIR and emit it with Thai keywords,
completing the symmetry: the same HIR can produce any locale surface, just as it
can produce any target backend.

### HIR-direct backends {#hir-direct-backends}

These targets emit directly from the typed HIR without lowering to MIR. They
preserve source-level structure longer and are suited for language-shaped output:

| Target | Status | Role |
|---|---|---|
| `Rust` | **Primary** | Production path. Packages, build, run, test. Cargo + rustc for native binaries. |
| `Faber` | **Support** | Canonical source view via `forma` formatter. Round-trip stability. |
| `TypeScript` | Probe | File emission only. Proves semantics across target shapes. |
| `Go` | Erase | File emission only. Borrow modes erased; `ad` rejected. |

## MIR — Mid-Level Intermediate Representation {#mir}

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

## AIR detour {#air}

AIR (Autograd / AI Representation) is a pure-functional transform detour off
the HIR → MIR path. It is entered by explicit annotation on individual
functions:

```faber
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

After the AIR transform completes its work (future: autodiff, fusion), the
result is re-lowered to MIR and rejoins the ordinary MIR backend pipeline.
AIR owns no backends and no independent typechecker — it is a transform
checkpoint, not a parallel IR.

```text
HIR  →  AIR purity check  →  HIR to AIR lowering  →  AIR validation  →  AIR to MIR re-lowering  →  MIR backend
```

This architecture mirrors JAX's approach: keep a pure-functional
representation for transforms, lower to imperative IR only at the end.
AIR exists because running autodiff over imperative MIR would require
reconstructing purity from code that was lowered into mutation.

## CPU target lanes {#cpu}

CPU targets consume MIR and produce either executable artifacts or text for
external toolchains. Faber emits text where possible and relies on lower-level
toolchains for the final compilation step — analogous to how a C compiler
emits assembly for the assembler and linker.

### FMIR — Faber's own MIR runtime {#fmir}

FMIR is the MIR-native package executor. The compiler extracts MIR into a
binary payload and wraps it with a short Rust kernel loader. This produces
a self-contained executable that runs the MIR through Faber's in-process
stepper — no separate runtime installation required.

| Format | Description |
|---|---|
| `fmir-text` | Inspectable FMIR text image at `target/faber-mir/image.fmir.txt` |
| `fmir` | Compact binary FMIR image at `target/faber-mir/image.fmir` |
| `fmir-bin` | Self-contained runner at `target/faber-mir/exe/run` — embeds FMIR bytes |

### LLVM text {#llvm}

Faber emits LLVM IR as text (`.ll`), not as integrated LLVM codegen.
The emitted IR is intended for external toolchain steps — verification,
optimisation, and native code generation are handled by downstream LLVM tools.
This is a staging and validation target, not a native codegen path embedded in
the compiler.

### WASM {#wasm}

Faber emits WebAssembly text (`.wat`) and binary (`.wasm`)
formats. The emitted Wasm uses external host imports (`faber_*`
runtime symbols) and is validated through `wasm-tools validate`.
Wasm is a supported-with-limitations target — it proves the MIR lowering
pipeline for an open standard format, but is not a package delivery runtime.

| Format | CLI target | Output |
|---|---|---|
| `wasm-text` | `-t wasm-text` (alias `wat`) | WAT text format |
| `wasm` | `-t wasm` | Binary Wasm module |

### TypeScript and Go (HIR-direct) {#typescript-go}

Though typically used for application-level file emission, TypeScript and Go
also serve as proof targets: they validate that Faber's semantics translate
to widely-used type systems, even if package compilation and runtime execution
remain Rust-only today.

## GPU target lanes {#gpu}

### WGSL (via WGPU) {#wgsl}

Faber emits WGSL compute shader source through the MIR pipeline. The emitted
WGSL is validated through `naga` (30.x) and includes a reflection
sidecar for bind-group metadata. This covers the device-safe kernel subset:
rank-1 `f32` device views are supported; rank-2 views reject. WGSL
is not a GPU launch runtime — Faber emits the shader source, but execution
requires an external WebGPU runtime.

### Metal (on hold) {#metal}

Metal compute shader text emission is designed and partially implemented but
is currently on hold. The architecture follows the same pattern as WGSL:
Faber emits Metal Shading Language source for the device-safe kernel subset,
with external toolchain handling compilation and execution. Work is planned
to resume.

## Architecture note {#comparison}

Faber's compilation architecture is similar in spirit to how the Rust compiler
works. Rust lowers through HIR → MIR → LLVM IR, embedding the LLVM toolchain
directly for final native codegen. Faber takes a softer approach: it emits
text for external toolchains (LLVM text, WGSL, Metal, WAT) rather than embedding
them, while reserving direct code emission for its own runtime (FMIR) and its
primary package target (Rust, where Cargo and rustc handle the downstream
pipeline).

The text-emission approach means Faber never needs to bundle LLVM, a Wasm
runtime, or a GPU driver — those remain external dependencies chosen by the
user. The tradeoff is that Faber cannot offer a single-command build for every
target; the user must install the appropriate toolchain for their chosen
backend.

## Target summary {#matrix}

| Target | IR | Family | Build | Run | Package |
|---|---|---|---|---|---|
| `Rust` | HIR | CPU | yes | yes | yes |
| `fmir` / `fmir-bin` | MIR | CPU | yes | yes | yes |
| `Faber` (format) | HIR | — | no | no | no |
| `TypeScript` | HIR | CPU | no | no | no |
| `Go` | HIR | CPU | no | no | no |
| `LLVM text` | MIR | CPU | no | no | no |
| `WASM` / `WAT` | MIR | CPU | no | no | no |
| `WGSL` | MIR | GPU | no | no | no |
| `Metal` (hold) | MIR | GPU | no | no | no |

*`build`, `run`, and `package` describe Faber workflows. External toolchains (rustc, wasm-tools, naga) handle final compilation for text-emission targets.*
