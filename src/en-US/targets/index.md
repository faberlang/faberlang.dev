+++
title = "Target lanes"
section = "targets"
order = 60
sources = []
+++

Faber compiles through lanes, and every target is a **projection** of the meaning the compiler holds — not a separate implementation. These pages put the source beside what it becomes.

Every generated panel is captured compiler output. If a page shows Rust, that is the Rust the compiler emits for the program above it.

## The lanes {#lanes}

| Lane | Carries | Targets |
|---|---|---|
| [HIR](/targets/hir.html) | the application lane | [Rust](/targets/rust.html), [Go](/targets/go.html), [TypeScript](/targets/ts.html), [Faber](/targets/faber.html) |
| [MIR](/targets/mir.html) | the systems lane | [LLVM IR](/targets/llvm-text.html), [WebAssembly text](/targets/wasm-text.html) |
| [GPU](/targets/gpu.html) | the device lane | [WGSL](/targets/wgsl-text.html), [Metal](/targets/metal-text.html) |

Three more lanes carry no source-text target of their own and so have no page here: **Locale** renders reader spellings (see [reader locales](/cheatsheet/locales.html)), **AIR** is the autograd surface between typed HIR and MIR, and **Packaging** produces the FHIR and FMIR artifacts a package ships.

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
