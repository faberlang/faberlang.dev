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
| `host-kernel-rs` | Thin router: Frame, Conversation, prefix dispatch, structured errors |
| `host-native-rs` | Native attach: workers, register_providers hook |
| `host-providers-rs` | Provider implementations: solum, processus, consolum, tempus, aleator, http |
