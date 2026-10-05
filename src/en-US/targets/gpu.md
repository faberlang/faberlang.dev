+++
title = "GPU — the device lane"
section = "targets"
order = 63
sources = []
+++

A function marked `@ nucleum` is a compute kernel. The device lane links the compiler to real Metal and CUDA execution.

The shader text below is the lowering surface. Real device execution — `faber run --device metal|cuda` — is the narrower product proof, recorded in the [device kernel support summary](/toolchain/target-matrix.html#device-kernel-support).

## Targets {#targets}

| Target | Emits | Scenarios shown |
|---|---|---|
| [WGSL](/targets/wgsl-text.html) | WGSL compute shader | 1 of 1 |
| [Metal](/targets/metal-text.html) | Metal MSL | 1 of 1 |

A target showing fewer scenarios than the others is not broken. It means the emitter declines that shape, which the pages state directly rather than hiding.

## Measured support {#support}

Device-kernel emitters are not scored against the general corpus — they lower a kernel surface and nothing else. Their measured support is the [device kernel support summary](/toolchain/target-matrix.html#device-kernel-support).

---

[All targets](/targets/) · [Measured support per term](/toolchain/target-matrix.html)
