+++
title = "HIR — the application lane"
section = "targets"
order = 61
sources = []
+++

HIR is the semantic core. Every target in this lane is a projection of the meaning held there, emitted as source you can read.

These are host languages. The emitter's job is to produce something a human would accept in review, which is why the Rust output stays close to the original shape while TypeScript expands.

## Targets {#targets}

| Target | Emits | Scenarios shown |
|---|---|---|
| [Rust](/targets/rust.html) | Rust source | 3 of 3 |
| [TypeScript](/targets/ts.html) | TypeScript source | 3 of 3 |
| [Go](/targets/go.html) | Go source | 3 of 3 |
| [Faber](/targets/faber.html) | Canonical Faber | 3 of 3 |

A target showing fewer scenarios than the others is not broken. It means the emitter declines that shape, which the pages state directly rather than hiding.

## Measured support {#support}

| Target | Capable | Analyzable | Coverage |
|---|---|---|---|
| [Rust](/targets/rust.html) | 373 | 378 | 99% |
| [TypeScript](/targets/ts.html) | 378 | 378 | 100% |
| [Go](/targets/go.html) | 347 | 378 | 92% |
| [Faber](/targets/faber.html) | 378 | 378 | 100% |

---

[All targets](/targets/) · [Measured support per term](/toolchain/target-matrix.html)
