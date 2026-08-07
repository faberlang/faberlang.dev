+++
title = "device-summa"
section = "examples"
order = 51
sources = []
+++

The smallest complete device package. A function marked `@ nucleum` is a compute kernel; the manifest's `[device]` section is what makes the packaged image carry Metal MSL and CUDA PTX artifacts. This is the starter fixture behind the `faber run --backend metal|cuda` path.

Source: [`examples/training/device-summa`](https://github.com/faberlang/examples/tree/main/training/device-summa)

## `src/device_summa.fab` {#src-device_summa-fab}

```faber
# =============================================================================
# device-summa — S1-6 vertical-slice proof kernel (gpu-training-lowering)
# =============================================================================
#
# What this proves:
#   • One already-proven collection kernel — a tree reduction (`summa`) over a
#     tf32[256] buffer, the R2 `summa` receipt floor — carried from Faber
#     source through the common device program (S1-1), the packaged FMIR
#     image's `device` section (S1-2), the composite host (S1-4), and real
#     Metal/CUDA sessions (S1-6) via the SAME ordinary command:
#
#       faber run --backend metal <package>    # Apple M5 Max (burgus)
#       faber run --backend cuda  <package>    # NVIDIA RTX 5070 (pharos)
#
#   • The kernel body is the proven `summa` proof shape (input buffer + output
#     buffer + u32 id → `workgroup_id.x`); the reduction recipe is the shared
#     `CollectionKernelPlan::TreeReduction` with a 256-lane workgroup, so a
#     single workgroup covers the whole tensor and the output buffer is one
#     element — the exact sum.
#
# The host input values live in faber.toml `[device] inputs` (pinned with the
# oracle); the CPU reference is pinned in oracle/ (numeric-policy v1.0.0,
# reduction-sum row: atol=1e-6, rtol=1e-6).
#
# See also: nucleum, tensor, cuda
# =============================================================================

@ nucleum
functio summa(tf32[256] a, tf32[1] out, u32 id) → vacuum {
    fixum f32 total ← a.summa()
    out[id] ← total
}
```

---

[All examples](/examples/) · [Install](/start/install.html) · [Cheat sheet](/cheatsheet/)
