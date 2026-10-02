+++
title = "Target lanes"
section = "targets"
order = 60
sources = []
+++

Faber compiles through lanes, and every target is a **projection** of the meaning the compiler holds — not a separate implementation. These pages put the source beside what it becomes.

Every generated panel is captured compiler output. If a page shows Rust, that is the Rust the compiler emits for the program above it.

## HIR — the application lane {#hir}

HIR is the semantic core. Every target in this lane is a projection of the meaning held there, emitted as source you can read.

[HIR lane overview](/targets/hir.html)

| Target | Emits | Scenarios shown |
|---|---|---|
| [Rust](/targets/rust.html) | Rust source | 3 of 3 |
| [TypeScript](/targets/ts.html) | TypeScript source | 3 of 3 |
| [Go](/targets/go.html) | Go source | 3 of 3 |
| [Faber](/targets/faber.html) | Canonical Faber | 3 of 3 |

## MIR — the systems lane {#mir}

MIR is where meaning takes execution-shaped form: lower-level targets, validation surfaces, and package runtimes.

[MIR lane overview](/targets/mir.html)

| Target | Emits | Scenarios shown |
|---|---|---|
| [LLVM IR](/targets/llvm-text.html) | LLVM IR text | 3 of 3 |
| [WebAssembly text](/targets/wasm-text.html) | WebAssembly text | 2 of 3 |

## GPU — the device lane {#gpu}

A function marked `@ nucleum` is a compute kernel. The device lane links the compiler to real Metal and CUDA execution.

[GPU lane overview](/targets/gpu.html)

| Target | Emits | Scenarios shown |
|---|---|---|
| [WGSL](/targets/wgsl-text.html) | WGSL compute shader | 1 of 1 |
| [Metal](/targets/metal-text.html) | Metal MSL | 1 of 1 |

## Other lanes {#other-lanes}

Three more compiler lanes carry no source-text target of their own and so have no page here: **Locale** renders reader spellings (see [reader locales](/cheatsheet/locales.html)), **AIR** is the autograd surface between typed HIR and MIR, and **Packaging** produces the FHIR and FMIR artifacts a package ships.

This is the honest target list: a page exists only for a lane the compiler exposes as a text target. There is no CUDA page — CUDA device programs are produced on the NVVM → PTX path and run with `faber run --backend cuda`, not emitted as source text. The [target matrix](/toolchain/target-matrix.html) measures a few more emit surfaces than the site gives pages to.

## The scenarios {#scenarios}

The same small programs run through every lane, so the pages compare like with like.

| Scenario | What it exercises |
|---|---|
| **Typed tensors** | Builds two shaped matrices, multiplies them, and reduces the product to a scalar. Exercises shape-bearing types and a reduction. |
| **The error channel** | A function that may fail, and a caller that catches. Shows how the `⇥` channel becomes each target's own error idiom. |
| **Collections and iteration** | A list folded to a total with `itera ex`. The plainest possible read on how loops lower. |
| **A compute kernel** | A function marked `@ nucleum`. Device lanes only — this is a different kind of source, not a variant of the programs above. |

## Support is measured elsewhere {#support}

These pages *demonstrate*. For measurement — which grammar terms lower on which target, across the whole corpus — use the [target matrix](/toolchain/target-matrix.html). It is the numeric authority; this section is the worked example.
