+++
title = "Compiler performance"
section = "tooling"
order = 2
sources = [
  "radix/README.md (Compiler Performance section)",
]
+++

Radix's frontend scales roughly linearly with source size, in-process and
single-threaded.

## Frontend compile times {#frontend-compile-times}

| Program size | Source | Median compile |
|-------------|--------|---------------|
| 100 functions / ~650 lines | ~10 KB | ~0.6 ms |
| 500 functions / ~3.3K lines | ~52 KB | ~3 ms |
| 1,000 functions / ~6.5K lines | ~105 KB | ~6 ms |
| 5,000 functions / ~32K lines | ~530 KB | ~37 ms |

The largest real example today is ~140 lines, well below the noise floor.

## Backend costs (Rust target) {#backend-costs-rust-target}

For `faber build`, the user-perceived time is dominated by Cargo/rustc,
not by Faber's frontend:

| Phase | Cost |
|-------|------|
| Cold `faber` dep compile (once per target dir) | ~2.8 s |
| Cold `tokio` dep compile (only when needed) | ~2.3 s |
| Warm per-program build (cached deps) | ~30–110 ms |
| Per-program Cargo invocation overhead | ~400 ms |

## Incremental compilation {#incremental-compilation}

The `faber-runtime` crate compiles once per target directory and is cached
as `.rlib` artifacts:

| You change | faber-runtime crate | Your program |
|-----------|-------------------|-------------|
| Your program source | cached | recompiles |
| `norma/src/*.fab` (Faber source) | cached | recompiles |
| `faber-runtime/src/*.rs` | recompiles once | recompiles |

The trap to avoid is building each program into a fresh `target/`.
Reuse a shared `--target-dir` to keep cached `.rlib`s warm.
