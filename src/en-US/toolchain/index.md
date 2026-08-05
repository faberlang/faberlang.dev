+++
title = "Toolchain"
section = "toolchain"
order = 0
sources = []
+++

One binary does everything: `faber`. It bundles the Radix compiler, the Cista
package resolver, a formatter, a test runner, and an in-process interpreter.
There is no separate build tool to install.

## The commands you will actually use {#daily}

```bash
faber init my-app          # create a package
faber check my-app/        # typecheck, no output written
faber run my-app/          # build if needed, then run
faber run --interpret .    # run in-process, no rustc, ~4 ms
faber test my-app/         # run inline proba suites
faber format my-app/       # format in place
faber explain redde        # what does this keyword do?
```

`check` is the one you run constantly — it is the full frontend (parse,
resolve, typecheck) with nothing written to disk.

## Everything `faber` exposes {#all-commands}

| Command | Does |
|---|---|
| `init` | create a new package |
| `check` | semantic analysis on a file or package |
| `build` | compile and write output for a target |
| `run` | build if needed, then execute |
| `script` | run source through the interpreter — single file, package, or archive |
| `repl` | interactive MIR stepper, re-lowering each line |
| `test` | run `proba` cases on the stepper, no Cargo or rustc |
| `format` | format source; `--locale` renders another reader surface |
| `explain` | explain a glyph, keyword, or grammar term |
| `targets` | list targets and their current capability notes |
| `install` | install a library package into the Cista store |
| `verify` | aspect verification on a single file |
| `emit`, `lex`, `parse`, `hir`, `mir` | compiler-phase inspection (aliases for `radix`) |

`faber` is for packages. `radix` is the developer tool for single files and
compiler-phase inspection — see [Inside Radix](/toolchain/radix.html).

## Two ways to run a program {#two-lanes}

| Lane | Command | What happens | When |
|---|---|---|---|
| **Compiled** | `faber run` | lowers to Rust, invokes `rustc`, produces a native binary | shipping, benchmarking |
| **Interpreted** | `faber run --interpret` | parse → typecheck → MIR, then steps MIR in-process | iterating, scripting, tests |

Both run the same frontend, so the interpreted lane typechecks exactly as
strictly as the compiled one. It just skips code generation and linking.

## Where the rest lives {#deeper}

| Page | What it covers |
|---|---|
| [The faber CLI](/toolchain/cli.html) | every command in depth, plus scripting and the REPL |
| [Compiling and targets](/toolchain/compiling.html) | the HIR/MIR/AIR lanes and what each backend supports |
| [Target matrix](/toolchain/target-matrix.html) | generated: every corpus term × every backend |
| [Packages with Cista](/toolchain/packages.html) | `faber.toml`, lockfiles, the package store |
| [Inside Radix](/toolchain/radix.html) | compiler architecture, for people changing it |
