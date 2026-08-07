+++
title = "MIR — the systems lane"
section = "targets"
order = 62
sources = []
+++

MIR is where meaning takes execution-shaped form: lower-level targets, validation surfaces, and package runtimes.

Expect large expansion ratios here and do not read them as waste. An IR names every intermediate value on purpose.

## Targets {#targets}

| Target | What it is | Scenarios shown |
|---|---|---|
| [LLVM IR](/targets/llvm-text.html) | MIR staging text for external LLVM tools. Also the route CUDA device programs take, via NVVM → PTX. | 3 of 3 |
| [WebAssembly text](/targets/wasm-text.html) | WAT emission from the same MIR. | 2 of 3 |

A target showing fewer scenarios than the others is not broken. It means the emitter declines that shape, which the pages state directly rather than hiding.

---

[All lanes](/targets/) · [Measured support per term](/toolchain/target-matrix.html)
