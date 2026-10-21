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
| `faber run <package>` | Interpret and execute an application package (never compiles) |
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

Use `run` for application packages with an `incipit` entry point. It
interprets the package on the MIR runner and never compiles; `faber build -t
<target>` is the command that builds. Library-only packages should be checked
and tested instead.

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

Packages carrying an `@ nucleum` compute kernel run on a GPU. Device selection
is explicit and fail-closed — a named device never silently falls back to CPU.

```bash
faber run --device metal <package>
faber run --device cuda <package>
faber run --device auto <package>
faber run --device reference <package>
faber run --device cpu <package>
```

`reference` and `cpu` run kernels as ordinary functions on the MIR runner;
today `cpu` is the same route as `reference`. Precedence is the CLI flag, then
the manifest `[device] device`, then `auto`.

Inside a kernel, integers are 32-bit: a 64-bit `int` is refused
(`SEM008 nucleum_wide_integer`, or `nucleum_wide_intermediate` for a wide
intermediate value). Write `i32`.

See [device execution](/toolchain/cli.html#device-execution) for the contract.

Related: [Cheat sheet](/cheatsheet/) · [Testing](/cheatsheet/testing.html) ·
[Start](/start/)
