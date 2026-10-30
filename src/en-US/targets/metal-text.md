+++
title = "Metal"
description = "Metal target (Metal MSL): Apple GPU compute shader source (MSL)."
section = "targets"
order = 77
sources = []
+++

Apple GPU compute shader source (MSL).

Part of the [GPU lane](/targets/gpu.html). Every panel below is compiler output.

## How to read it {#reading}

The same kernel, a different ABI. Compare it against the WGSL beside it — one Faber function, two unrelated shading languages, neither written by hand.

## Measured support {#support}

`metal-text` is a **device-kernel emitter**, not a general-language target. It lowers `kernel` declarations and related GPU views, and deliberately nothing else, so it is not scored against the general corpus — a percentage there would read as a completion score it is not. Its measured support is the [device kernel support summary](/toolchain/target-matrix.html#device-kernel-support).

## A compute kernel {#nucleum}

A `kernel` declaration. Device lanes only — this is a different kind of source, not a variant of the programs above.

**Metal does not lower this scenario.** That is a measured gap, not an omission — the emitter rejects it rather than producing something that would not run.

---

[All targets](/targets/) · [Measured support per term](/toolchain/target-matrix.html)
