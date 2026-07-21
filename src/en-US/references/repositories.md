+++
title = "Repositories"
section = "references"
order = 3
sources = [
  "github.com/faberlang",
]
+++

Faber is developed across multiple repositories under the `faberlang`
organisation.

## Public repositories {#public-repositories}

| Repository | Description |
|-----------|-------------|
| `faber` | User-facing CLI: check, build, run, test, format, explain |
| `faber-runtime` | Core runtime types (Valor, tensors, frames); crate name `faber` |
| `norma` | Standard library source (`norma:*` modules) |
| `triga` | Optional graphics/geometry library |
| `cista` | Package manager and store (experimental) |
| `examples` | Language corpus, coreutils, AI Workbench, reader-locale packages |
| `faberlang.dev` | This website |

## Private repositories {#private-repositories}

| Repository | Description |
|-----------|-------------|
| `radix` | Compiler: lexing, parsing, semantic analysis, HIR/MIR/AIR, diagnostics, codegen |

## Host platform repositories {#host-platform-repositories}

| Repository | Description |
|-----------|-------------|
| `hosts` | Host monorepo: `crates/host-kernel`, `crates/host-native`, providers, `macos-arm64`, `webgpu-browser` |
