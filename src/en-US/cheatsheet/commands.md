+++
title = "Commands"
section = "cheatsheet"
order = 42
sources = []
+++

The `faber` CLI, as a command index. For flags and compiler pipeline detail,
open [The faber CLI](/toolchain/cli.html).

## Daily loop {#daily-loop}

| Command | Use it for |
|---|---|
| `faber check <package>` | Fast front-end validation: lex, parse, type check, lower |
| `faber build <package> -t rust` | Emit a Rust project for review or native compilation |
| `faber run <package>` | Run an application package in this process: `clif-jit` when it accepts the program, otherwise the MIR runner |
| `faber test <package>` | Run package tests when the package defines test surfaces |
| `faber explain <code>` | Read a stable diagnostic explanation |
| `faber update --check` | See whether a newer release exists; `faber update` installs it |

Start with `check`. It is the cheapest command and the one agents should run
before proposing generated code as valid Faber.

## Check {#check}

```bash
faber check .
faber check path/to/package
```

A passing check means the package is syntactically and semantically acceptable
to the compiler front end. It does not mean the final native toolchain has been
invoked.

`faber check --lower .` goes one step further: it also lowers the program to
the reference form that `faber run` executes, without running it, and reports
the errors a plain check cannot see.

## Build {#build}

```bash
faber build . -t rust
```

The Rust target is intentionally reviewable. Generated Rust is a compiler
artifact, not source of truth; edit the Faber package and rebuild rather than
patching emitted Rust by hand.

## Run {#run}

```bash
faber run .
```

Use `run` for application packages with an `incipit` entry point. Since 1.18
it compiles the package to native code in memory (the `clif-jit` engine), and
falls back to the MIR runner when that lane declines the program; the fallback
is decided before anything runs. `faber run --target runner` picks the MIR
runner, and `--target clif-jit|ts|go|llvm-host` picks that engine with no
fallback. `faber build -t <target>` is the command that writes a build. Library-only
packages should be checked and tested instead.

## Explain diagnostics {#explain}

```bash
faber explain SEM001
faber explain LEX006
```

Diagnostic families are stable handles: `LEX` for lexical errors, `PARSE` for
parser errors, `SEM` for semantic/type errors. In docs and agent reports, cite
the diagnostic code instead of paraphrasing a compiler failure loosely.

## Reader-locale commands {#reader-locale}

```bash
faber convert --to la path/to/file.fab
faber convert --to th-TH path/to/file.fab
faber convert --to zh-Hans --write path/to/file.fab
```

`faber convert` reports by default and `--write` rewrites the file. Reader
locale output is a rendering of the compiler's semantic model, not a
browser-time translation layer. Locale work belongs after a package checks in
canonical form. `faber format` does not translate; it reports (or with
`--write`, applies) canonical layout at the file's own locale. On `faber
emit`, `--locale` selects the input locale pack, not the output surface.

## Device execution {#device}

Packages carrying a `kernel` run on a GPU. Device selection
is explicit and fail-closed — a named device never silently falls back to CPU.

```bash
faber run --device metal <package>
faber run --device cuda <package>
faber run --device auto <package>
faber run --device reference <package>
faber run --device cpu <package>
```

`reference` runs kernels as ordinary functions, single-threaded, on the MIR
runner. Since 1.17 `cpu` is a device of its own: the same launch pipeline as
`metal` and `cuda`, run by worker threads (`--threads N`, or `[device] threads`
in `faber.toml`). `--partitions N` selects partitions on `cpu`, `metal` or
`cuda`. Precedence is the CLI flag, then the manifest `[device] device`, then
`auto`.

`faber check --device cpu|metal|cuda` builds the device image without running
it and prints `INFO001` advice: the tier of each kernel, serialized or
unplaceable kernels, and a report for every `do device` region. See
[Tensor computation](/language/tensor-compute.html#device-regions).

`faber check|build|run --device-mode eligible` lets the compiler use proved
device variants of unmarked functions, in kernels and inside `do eligible`. The
default, `explicit`, does not. See
[device mode](/toolchain/cli.html#device-mode).

A kernel runs at one of three safety tiers: `kernel name(…)` (IEEE-correct float
math, the default), `kernel name(…) relaxed` (approximate `/` and `sqrt`, fast
transcendentals) and `kernel name(…) unsafe` (also drops the index checks the
compiler cannot prove). `--safe` on `faber run` or `faber build`, or `safe =
true` under `[device]` in `faber.toml`, runs every kernel at the default tier.

Inside a kernel, `i64`, `u64`, `wrapping<u64>` and `d64` are admitted values
since 1.17; the target decides whether it can carry them (Metal does, the other
device targets refuse by name). `f64` is still refused.

See [device execution](/toolchain/cli.html#device-execution) for the contract.

Related: [Cheat sheet](/cheatsheet/) · [Testing](/cheatsheet/testing.html) ·
[Start](/start/)
