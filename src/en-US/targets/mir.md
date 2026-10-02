+++
title = "MIR — the systems lane"
section = "targets"
order = 62
sources = []
+++

MIR is where meaning takes execution-shaped form: lower-level targets, validation surfaces, and package runtimes.

Expect large expansion ratios here and do not read them as waste. An IR names every intermediate value on purpose.

## Targets {#targets}

| Target | Emits | Scenarios shown |
|---|---|---|
| [LLVM IR](/targets/llvm-text.html) | LLVM IR text | 3 of 3 |
| [WebAssembly text](/targets/wasm-text.html) | WebAssembly text | 2 of 3 |

A target showing fewer scenarios than the others is not broken. It means the emitter declines that shape, which the pages state directly rather than hiding.

## Measured support {#support}

| Target | Capable | Analyzable | Coverage |
|---|---|---|---|
| [LLVM IR](/targets/llvm-text.html) | 334 | 373 | 90% |
| [WebAssembly text](/targets/wasm-text.html) | 263 | 373 | 71% |

The matrix also measures `runner`, `sexp`, `sexp-struct`, `wasm` — MIR emit surfaces with no page here yet.

---

[All targets](/targets/) · [Measured support per term](/toolchain/target-matrix.html)
