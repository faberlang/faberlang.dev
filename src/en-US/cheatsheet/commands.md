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
| `faber run <package>` | Build and execute an application package |
| `faber test <package>` | Run package tests when the package defines test surfaces |
| `faber explain <code>` | Read a stable diagnostic explanation |

Start with `check`. It is the cheapest command and the one agents should run
before proposing generated code as valid Faber.

## Check {#check}

```bash
faber check .
faber check examples/ai-workbench/packages/faber-ai
```

A passing check means the package is syntactically and semantically acceptable
to the compiler front end. It does not mean the final native toolchain has been
invoked.

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

Use `run` for application packages with an `incipit` entry point. Library-only
packages should be checked and tested instead.

## Explain diagnostics {#explain}

```bash
faber explain SEM001
faber explain LEX006
```

Diagnostic families are stable handles: `LEX` for lexical errors, `PAR` for
parser errors, `SEM` for semantic/type errors. In docs and agent reports, cite
the diagnostic code instead of paraphrasing a compiler failure loosely.

## Reader-locale commands {#reader-locale}

```bash
faber format --locale=la path/to/file.fab
faber format --locale=th-TH path/to/file.fab
faber emit -t faber --locale=zh-Hans path/to/file.fab
```

Reader locale output is a rendering of the compiler's semantic model, not a
browser-time translation layer. Locale work belongs after a package checks in
canonical form.

## Device execution {#device}

Packages carrying an `@ nucleum` compute kernel run on a GPU. Backend selection
is explicit and fail-closed — a named backend never silently falls back to CPU.

```bash
faber run --backend metal <package>
faber run --backend cuda <package>
faber run --backend auto <package>
```

See [device execution](/toolchain/cli.html#device-execution) for the contract.

Related: [Cheat sheet](/cheatsheet/) · [Testing](/cheatsheet/testing.html) ·
[Hello, Faber](/start/hello.html)
