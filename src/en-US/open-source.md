+++
title = "Open source"
section = "open-source"
order = 6
sources = [
  "github.com/faberlang",
]
+++

Faber is open source. The compiler front end, the MIR runner, the standard
library (Norma), the grammar, the reader-locale packs and the corpus live in one
public repository, [faberlang/faber](https://github.com/faberlang/faber), under
either the **MIT** or the **Apache-2.0** license, at your option. The sibling
libraries, the examples and this documentation site are public too. The
repository does not accept pull requests: file an issue instead.

## What is in the public repository {#what-is-open}

| Component | What it is |
|---|---|
| **Compiler front end and middle** | Lexer, parser, semantic analysis, the typed HIR and MIR intermediate representations and the checks that run on them |
| **MIR runner** | Executes Faber programs directly (`faber run`); the reference every other target is checked against |
| **Faber re-emitter** | The HIR-backed canonical emitter behind `faber format` and `faber convert` |
| **C code generator** | Readable C11 whose output matches the runner; a public preview that covers a growing subset of the language |
| **The `faber` command** | `check`, `run`, `test`, `format`, `convert`, `explain` and the rest |
| **Norma** | The standard library (`lib/norma`): files, processes, time, text, JSON, TOML, HTTP and more |
| **Grammar and locale packs** | The formal grammar and the eight reader-locale packs |
| **Corpus** | Several hundred small programs, each with expected output, that document and test the language, and the suites that run them |

## What ships in the official binary {#what-is-in-the-binary}

The official `faber` release also includes the code generators that are not in
the public repository: Rust, Go, TypeScript, Swift, Python, Haskell, LLVM,
WebAssembly, the GPU kernel targets and the historical and novelty targets. The
[target table](/toolchain/compiling.html#target-table) says which is which and
how mature each one is.

A native backend built on Cranelift is in progress, so that a build from the
public source alone produces executables. Until it lands, the public source
builds `faber check`, `faber run`, `faber test`, `faber format` and
`faber convert`, and emits C.

## Public repositories {#public-repositories}

Everything below lives under the [faberlang](https://github.com/faberlang)
organisation.

<!-- TODO(cut): verify this list at the cut. faber-1.x exists only after the rename step; norma, cista, hosts and releases are archived by a later step, after the cut. -->

| Repository | Description |
|---|---|
| [faber](https://github.com/faberlang/faber) | The language: compiler front end, MIR runner, Faber re-emitter, C target preview, Norma, grammar, locale packs, corpus |
| [faber-1.x](https://github.com/faberlang/faber-1.x) | The archived 1.x line: runtime and grammar record, old release tags |
| [releases](https://github.com/faberlang/releases) | Tagged CLI release assets and prebuilt archives |
| [triga](https://github.com/faberlang/triga) | Graphics and geometry library |
| [gradus](https://github.com/faberlang/gradus) | Autograd and ML library: gradients, loss, optimizers, NN primitives, training |
| [examples](https://github.com/faberlang/examples) | Coreutils, AI Workbench, reader-locale packages, GPU workload and training tracks |
| [tree-sitter-faber](https://github.com/faberlang/tree-sitter-faber) | Tree-sitter grammar and editor packaging for syntax highlighting |
| [faberlang.dev](https://github.com/faberlang/faberlang.dev) | This website |

## Reporting issues {#reporting-issues}

GitHub Issues is the fastest way to reach the project. File against the repo
that owns the problem:

| Problem | Where to report |
|---|---|
| Compiler or CLI behaviour (bugs, diagnostics, crashes), standard library | [faberlang/faber · Issues](https://github.com/faberlang/faber/issues) |
| Documentation or website problems | [faberlang/faberlang.dev · Issues](https://github.com/faberlang/faberlang.dev/issues) |
| A sibling library | The matching repository above |

Include the `faber` version and a minimal reproducing package.

## Maintainer {#maintainer}

Faber is designed and maintained by **Ian Zepp**.

| | |
|---|---|
| **Email** | [ian.zepp@protonmail.com](mailto:ian.zepp@protonmail.com) |
| **X / Twitter** | [@faberlang](https://x.com/faberlang) |
| **GitHub** | [github.com/faberlang](https://github.com/faberlang) |

For anything reproducible — a bug, a broken page, a package that will not
build — an issue on the owning repository will get a faster and more useful
answer than email, because it lands next to the code and stays searchable for
whoever hits it next.
