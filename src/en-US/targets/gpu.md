+++
title = "GPU — the device lane"
section = "targets"
order = 63
sources = []
+++

A function marked `@ nucleum` is a compute kernel. The device lane links the compiler to real Metal and CUDA execution.

The shader text below is the lowering surface. Real device execution — `faber run --backend metal|cuda` — is the narrower product proof, recorded in the [device kernel support summary](/toolchain/target-matrix.html#device-kernel-support).

## Targets {#targets}

| Target | What it is | Scenarios shown |
|---|---|---|
| [WGSL](/targets/wgsl-text.html) | WebGPU compute shader source. | 1 of 1 |
| [Metal](/targets/metal-text.html) | Apple GPU compute shader source (MSL). | 1 of 1 |

A target showing fewer scenarios than the others is not broken. It means the emitter declines that shape, which the pages state directly rather than hiding.

---

[All lanes](/targets/) · [Measured support per term](/toolchain/target-matrix.html)
