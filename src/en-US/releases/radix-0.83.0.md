+++
title = "Radix 0.83.0"
section = "releases"
order = 8
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.83.0 |
| **Tag** | [`v0.83.0`](https://github.com/faberlang/radix/releases/tag/v0.83.0) |
| **Faber companion** | 1.8.0 |
| **Published** | 2026-08-18 |
| **License** | MIT |

Radix is released as **source + tag** (library crates; no standalone binary).
The 0.83.0 line ships alongside [Faber 1.8.0](/releases/faber-1.8.0.html),
which is the binary product built from it.

## Highlights {#highlights}

Bulk version bump of the 34 workspace crates riding the Faber 1.8.0 release —
see the [Faber 1.8.0 notes](/releases/faber-1.8.0.html) for the compiler,
language, and format work in this line, including:

- Shape generics (contracts, glyph arms, unroll pass, guard-as-mask
  differentiable subset).
- Keyword-as-identifier semantics.
- F16 and MXFP4 storage admission; KV cache structure types.
- Packed-kernel device execution planning (R-PACK-05a) with the dense-model
  profiling harness.

## Known reds {#known-reds}

The 1.7.0 known-red suite was carried into this release per the known-red
release rule; see the Faber 1.8.0 notes for the disclosure.
