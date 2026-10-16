+++
title = "Open source"
section = "open-source"
order = 6
sources = [
  "github.com/faberlang",
]
+++

Faber's source is open. The compiler front end, the reference runner, the
standard library (Norma), the grammar, the locale packs and the corpus are in
[faberlang/faber](https://github.com/faberlang/faber) under
`MIT OR Apache-2.0`. The repository builds a working `faber` that checks,
formats and runs programs.

**Faber is experimental through version 1.** The language changes constantly,
and breaking changes ship in minor releases. Pin an exact version and read the
release notes before you upgrade.

## What is open {#what-is-open}

| Component | What it is |
|---|---|
| **Compiler front end and middle** | Lexer, parser, semantic analysis, the typed intermediate representations (HIR and MIR) and the checks that run on them |
| **The MIR runner** | Executes Faber programs directly; the reference every other target is checked against |
| **C and Cranelift code generators** | Readable C and native objects through Cranelift. Both are previews that cover a growing subset of the language and reject the rest by name |
| **Artifact formats** | FHIR and FMIR: serialized analyzed HIR and MIR images that `faber` can load and run |
| **The `faber` command** | `check`, `run`, `test`, `build`, `format`, `convert`, `corpus` and `targets` |
| **Norma** | The standard library: files, processes, time, text, JSON, TOML, HTTP and more |
| **Grammar and locale packs** | The grammar and the reader-locale packs |
| **Corpus** | Several hundred small programs with expected output, and the suites that run them |
| **Agent skills** | Two guides for coding agents: writing Faber, and changing the repository |
| **Documentation** | This site, its Markdown sources, and the generator that renders it |

## What is not in the public source {#what-is-closed}

The official `faber` release also carries code generators that are not part of
the public source: Rust, Go, TypeScript, Swift, Python, Haskell, LLVM,
WebAssembly and the GPU emitters. Installing a release, not building the public
tree, is the way to get every target. See the
[target matrix](/toolchain/target-matrix.html) for what each target covers.

## Public repositories {#public-repositories}

Everything below lives under the [faberlang](https://github.com/faberlang)
organisation. Each repository's README states its own status and licence.

| Repository | Description |
|---|---|
| [faber](https://github.com/faberlang/faber) | The open-source core: compiler front end, runner, standard library, grammar |
| [releases](https://github.com/faberlang/releases) | Tagged CLI release assets and prebuilt archives |
| [triga](https://github.com/faberlang/triga) | Graphics and geometry library |
| [gradus](https://github.com/faberlang/gradus) | Autograd and ML library: gradients, loss, optimizers, NN primitives, training |
| [tela](https://github.com/faberlang/tela) | UI and view library |
| [tree-sitter-faber](https://github.com/faberlang/tree-sitter-faber) | Tree-sitter grammar and editor packaging for syntax highlighting |
| [faberlang.dev](https://github.com/faberlang/faberlang.dev) | This website |

Three archived repositories are kept for history: `faber-1.x` held Faber 1.0 to
1.12 (its version tags were carried into `faber`, so a project pinned to a 1.x
tag keeps resolving), and `norma` and `hosts` are superseded. The standard
library now lives in `faber` under `lib/norma`.

## Reporting issues {#reporting-issues}

GitHub Issues is the fastest way to reach the project. The repositories do not
take outside pull requests.

| Problem | Where to report |
|---|---|
| Compiler or CLI behaviour (bugs, diagnostics, crashes) | [faberlang/faber · Issues](https://github.com/faberlang/faber/issues) |
| Standard library | [faberlang/faber · Issues](https://github.com/faberlang/faber/issues) |
| Documentation or website problems | [faberlang/faberlang.dev · Issues](https://github.com/faberlang/faberlang.dev/issues) |
| A library or tool | The matching repository above |

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
