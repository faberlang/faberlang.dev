+++
title = "HIR — the application lane"
section = "targets"
order = 61
sources = []
+++

HIR is the semantic core. Every target in this lane is a projection of the meaning held there, emitted as source you can read.

These are host languages. The emitter's job is to produce something a human would accept in review, which is why the Rust output stays close to the original shape while TypeScript expands.

## Targets {#targets}

| Target | What it is | Scenarios shown |
|---|---|---|
| [Rust](/targets/rust.html) | HIR projection. The package product path compiles this through Cargo. | 3 of 3 |
| [Go](/targets/go.html) | HIR projection with file emission and end-to-end floors. | 3 of 3 |
| [TypeScript](/targets/ts.html) | HIR projection with file emission and end-to-end floors. | 3 of 3 |
| [Faber](/targets/faber.html) | Canonical re-emission — the compiler printing the program back. | 3 of 3 |

A target showing fewer scenarios than the others is not broken. It means the emitter declines that shape, which the pages state directly rather than hiding.

---

[All lanes](/targets/) · [Measured support per term](/toolchain/target-matrix.html)
