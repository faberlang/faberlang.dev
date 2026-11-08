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
faber run my-app/          # run in-process on clif-jit; --device reference for the MIR runner
faber build my-app/ -t rust  # compile to a target
faber test my-app/         # run inline proba suites
faber format my-app/       # report files that would change (--write applies)
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
| `run` | run a single file, package, or archive in this process; with `--target`, pick the engine |
| `repl` | interactive MIR runner, re-lowering each line |
| `test` | run `+++ faber test` sections and `proba` cases on the runner, no Cargo or rustc |
| `format` | report (or `--write`) canonical formatting at the source's own locale |
| `convert` | convert source between reader-locale surfaces (`--to <locale>`) |
| `explain` | explain a glyph, keyword, or grammar term |
| `targets` | list targets and their current capability notes |
| `verify` | aspect verification on a single file |
| `emit`, `debug lex`, `debug parse`, `debug hir`, `debug mir` | compiler-phase inspection (`debug` is hidden; the bare phase names are hidden aliases for 1.19) |

`faber` is for packages. `radix` is the developer tool for single files and
compiler-phase inspection — see [Inside Radix](/toolchain/radix.html).

## Run, or build {#two-lanes}

| Command | What happens | When |
|---|---|---|
| `faber run` | parse → typecheck → MIR, then compiles in memory with Cranelift and runs in-process; `--device reference` runs the MIR itself, `--target` builds for a target first | iterating, scripting, tests |
| `faber build -t <target>` | lowers to the chosen target and writes the output | shipping, benchmarking |

Both run the same frontend, so `run` typechecks exactly as strictly as
`build`. `run` writes nothing to disk and needs no linker.

## Where the rest lives {#deeper}

| Page | What it covers |
|---|---|
| [The faber CLI](/toolchain/cli.html) | every command in depth, plus scripting and the REPL |
| [Compiling and targets](/toolchain/compiling.html) | the HIR/MIR/AIR lanes and what each backend supports |
| [Target matrix](/toolchain/target-matrix.html) | generated: every corpus term × every backend |
| [Packages with Cista](/toolchain/packages.html) | `faber.toml`, lockfiles, the package store |
| [Inside Radix](/toolchain/radix.html) | compiler architecture, for people changing it |
