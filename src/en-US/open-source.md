+++
title = "Open source"
section = "open-source"
order = 6
sources = [
  "github.com/faberlang",
]
+++

Faber is open source, with one stated exception. The language, its standard
library, its build and package tooling, every public library, all code
examples, and this documentation site are **MIT licensed** and developed in
public on GitHub. **Radix**, the compiler, is closed source for now.

That exception is meant to end. Radix is planned for open release once the
language has clearer market demand — it is a timing decision, not a permanent
fence around Faber.

## What is open {#what-is-open}

| Component | What it is |
|---|---|
| **Public Faber target APIs** | Rust, TypeScript, Go, and Swift support packages for generated programs |
| **Cista** | The package manager and package store |
| **Norma** | The standard library (`norma:*` modules) |
| **Triga** | The graphics and geometry library |
| **Gradus** | The autograd and ML library |
| **faber-runtime** | Runtime types backing generated Rust |
| **Examples** | Every sample package, application campaign, and workload track |
| **Documentation** | This site, its Markdown sources, and the Speculum generator that renders it |

All of the above are MIT. You can read them, fork them, vendor them, and ship
work built on them without asking.

## What is closed {#what-is-closed}

| Component | Status |
|---|---|
| **Radix and the Faber product** | Compiler, package workflow, CLI, diagnostics, and code generation. Closed source; released as the `faber` binary. |

Radix being closed does not make it opaque. Compiler bugs are reported
publicly, release binaries are checksummed and tagged, and the grammar,
[target matrix](/toolchain/target-matrix.html), and
[design notes](/reference/design.html) are published from the compiler tree
itself.

## Public repositories {#public-repositories}

Everything below lives under the [faberlang](https://github.com/faberlang)
organisation.

| Repository | Description |
|---|---|
| [faber](https://github.com/faberlang/faber) | Public Rust, TypeScript, Go, and Swift target APIs; project and issue routing |
| [releases](https://github.com/faberlang/releases) | Tagged CLI release assets and prebuilt archives |
| [norma](https://github.com/faberlang/norma) | Standard library source (`norma:*` modules) |
| [triga](https://github.com/faberlang/triga) | Graphics and geometry library |
| [gradus](https://github.com/faberlang/gradus) | Autograd and ML library: gradients, loss, optimizers, NN primitives, training |
| [cista](https://github.com/faberlang/cista) | Package manager and store (experimental) |
| [examples](https://github.com/faberlang/examples) | Coreutils, AI Workbench, reader-locale packages, GPU workload and training tracks |
| [tree-sitter-faber](https://github.com/faberlang/tree-sitter-faber) | Tree-sitter grammar and editor packaging for syntax highlighting |
| [faberlang.dev](https://github.com/faberlang/faberlang.dev) | This website |

### Host platform repositories {#host-platform-repositories}

| Repository | Description |
|---|---|
| [host-kernel-rs](https://github.com/faberlang/host-kernel-rs) | Thin router: Frame, Conversation, prefix dispatch, structured errors |
| [host-native-rs](https://github.com/faberlang/host-native-rs) | Native attach: workers and the `register_providers` hook |
| [host-providers-rs](https://github.com/faberlang/host-providers-rs) | Provider implementations: solum, processus, consolum, tempus, aleator, http |

## Reporting issues {#reporting-issues}

GitHub Issues is the fastest way to reach the project. File against the repo
that owns the problem:

| Problem | Where to report |
|---|---|
| Compiler or CLI behaviour (bugs, diagnostics, crashes) | [faberlang/faber · Issues](https://github.com/faberlang/faber/issues) |
| Documentation or website problems | [faberlang/faberlang.dev · Issues](https://github.com/faberlang/faberlang.dev/issues) |
| Standard library | [faberlang/norma · Issues](https://github.com/faberlang/norma/issues) |
| Anything else | The matching repository above |

Radix is closed source, but compiler bugs are still reported publicly through
[faberlang/faber · Issues](https://github.com/faberlang/faber/issues) — include
the `faber` version and a minimal reproducing package.

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
