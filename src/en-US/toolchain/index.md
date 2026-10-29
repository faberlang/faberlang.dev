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
faber run my-app/          # interpret in-process (compiles only with --target)
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
| `run` | interpret a single file, package, or archive; with `--target`, build for a target and run it |
| `repl` | interactive MIR runner, re-lowering each line |
| `test` | run `proba` cases on the runner, no Cargo or rustc |
| `format` | report (or `--write`) canonical formatting at the source's own locale |
| `convert` | convert source between reader-locale surfaces (`--to <locale>`) |
| `explain` | explain a glyph, keyword, or grammar term |
| `targets` | list targets and their current capability notes |
| `verify` | aspect verification on a single file |
| `emit`, `lex`, `parse`, `hir`, `mir` | compiler-phase inspection (aliases for `radix`) |

`faber` is for packages. `radix` is the developer tool for single files and
compiler-phase inspection — see [Inside Radix](/toolchain/radix.html).

## Run, or build {#two-lanes}

| Command | What happens | When |
|---|---|---|
| `faber run` | parse → typecheck → MIR, then runs the MIR in-process; compiles only with `--target` | iterating, scripting, tests |
| `faber build -t <target>` | lowers to the chosen target and writes the output | shipping, benchmarking |

Both run the same frontend, so `run` typechecks exactly as strictly as
`build`. `run` just skips code generation and linking.

## Where the rest lives {#deeper}

| Page | What it covers |
|---|---|
| [The faber CLI](/toolchain/cli.html) | every command in depth, plus scripting and the REPL |
| [Compiling and targets](/toolchain/compiling.html) | the HIR/MIR/AIR lanes and what each backend supports |
| [Target matrix](/toolchain/target-matrix.html) | generated: every corpus term × every backend |
| [Packages with Cista](/toolchain/packages.html) | `faber.toml`, lockfiles, the package store |
| [Inside Radix](/toolchain/radix.html) | compiler architecture, for people changing it |
