+++
title = "Repositories"
section = "reference"
order = 4
sources = [
  "github.com/faberlang",
]
+++

Faber is developed across multiple repositories under the
[faberlang](https://github.com/faberlang) organisation. Everything below is
public except the compiler itself.

## Reporting issues {#reporting-issues}

There is no mailing list or support email — GitHub Issues is the way to get
in touch. File against the repo that owns the problem:

| Problem | Where to report |
|---|---|
| Compiler or CLI behaviour (bugs, diagnostics, crashes) | [faberlang/faber · Issues](https://github.com/faberlang/faber/issues) |
| Documentation or website problems | [faberlang/faberlang.dev · Issues](https://github.com/faberlang/faberlang.dev/issues) |
| Standard library | [faberlang/norma · Issues](https://github.com/faberlang/norma/issues) |
| Anything else | The matching repository below |

The compiler (`radix`) is closed-source, but compiler bugs are still
reported publicly through [faberlang/faber · Issues](https://github.com/faberlang/faber/issues)
— include the `faber` version and a minimal reproducing package.

## Public repositories {#public-repositories}

| Repository | Description |
|-----------|-------------|
| [faber](https://github.com/faberlang/faber) | User-facing CLI: check, build, run, test, format, explain |
| [releases](https://github.com/faberlang/releases) | Tagged CLI release assets and prebuilt archives |
| [faber-runtime](https://github.com/faberlang/faber-runtime) | Core runtime types (Valor, tensors, frames); crate name `faber` |
| [norma](https://github.com/faberlang/norma) | Standard library source (`norma:*` modules) |
| [triga](https://github.com/faberlang/triga) | Optional graphics/geometry library |
| [cista](https://github.com/faberlang/cista) | Package manager and store (experimental) |
| [examples](https://github.com/faberlang/examples) | Coreutils, AI Workbench, reader-locale packages, GPU workload tracks (language corpus now lives in the private `radix` tree) |
| [tree-sitter-faber](https://github.com/faberlang/tree-sitter-faber) | Tree-sitter grammar and editor packaging for syntax highlighting |
| [faberlang.dev](https://github.com/faberlang/faberlang.dev) | This website |

## Private repositories {#private-repositories}

| Repository | Description |
|-----------|-------------|
| `radix` | The compiler — lexing, parsing, semantic analysis, HIR/MIR/AIR, diagnostics, codegen. Closed-source; not on GitHub publicly. Report compiler bugs via [faberlang/faber · Issues](https://github.com/faberlang/faber/issues). |

## Host platform repositories {#host-platform-repositories}

| Repository | Description |
|-----------|-------------|
| [host-kernel-rs](https://github.com/faberlang/host-kernel-rs) | Thin router: Frame, Conversation, prefix dispatch, structured errors |
| [host-native-rs](https://github.com/faberlang/host-native-rs) | Native attach: workers and the `register_providers` hook |
| [host-providers-rs](https://github.com/faberlang/host-providers-rs) | Provider implementations: solum, processus, consolum, tempus, aleator, http |
