+++
title = "Faber"
section = ""
order = 0
sources = []
+++

**Faber** is a package-oriented programming language with a Latin
behavioural vocabulary, a small regular grammar, and a type-first static
type system. Source is compiled through the Radix compiler to reviewable
Rust and native binaries. Its defining architectural property is that
meaning lives in a semantic core — the HIR (high-level intermediate
representation) — rather than in any particular rendering.

The name derives from the Latin word for *maker* or *craftsman*. The
compiler is named Radix, from the Latin *root*. The language is
developed by Ian Zepp and released under the MIT license.

## Download Faber 1.1.1 {#download}

Current release: **Faber 1.1.1** (tag `faber-v1.1.1`). Prebuilt CLI archives
for macOS and Linux; extract the `faber` binary and put it on your `PATH`.

| Platform | Archive | Checksum |
|---|---|---|
| **macOS arm64** (Apple Silicon) | [faber-v1.1.1-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz) | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz.sha256) |
| **Linux x64** (glibc) | [faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz) | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz.sha256) |

Quick install (macOS arm64 example):

```bash
curl -fsSL -o faber.tgz \
  https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz
tar -xzf faber.tgz
sudo mv faber /usr/local/bin/
faber --version
```

All release notes and assets: [github.com/faberlang/releases · faber-v1.1.1](https://github.com/faberlang/releases/releases/tag/faber-v1.1.1).
Step-by-step: [Install guide](/start/install.html).

| | |
|---|---|
| **Paradigm** | Package-oriented; semantic staging |
| **Typing** | Static, type-first; nullable via `T ∪ nihil` |
| **Glyphs** | `← → ∴ ≡ ∪ ⇥` |
| **Designed by** | Ian Zepp |
| **First appeared** | 2024 |
| **Compiler** | Radix (Rust) |
| **Lanes** | Application (HIR) · Systems (MIR) |
| **Primary target** | Rust → native binary |
| **Reader locales** | 7 shipped (la, ar, hi, vi, th-TH, zh-Hans, zh-Hant) |
| **Standard library** | Norma (`norma:*`) |
| **License** | MIT |

## Start here {#start-here}

| Path | Who | What |
|---|---|---|
| [Install](/start/install.html) | Human | Download, PATH, first `faber check` |
| [Quick tour](/start/) | Human | Language shape in five minutes |
| [Examples](/start/examples.html) | Human + agent | Real packages: CLI apps, mailspace, GPU, corpus |
| [`/llms.txt`](/llms.txt) | Agent | Machine index — start here if you are a model |
| [Agent guide](/agents/index.md) | Agent | How to learn Faber and ship a package |
| [Agent skills](/.well-known/agent-skills/index.json) | Agent | Focused skill guides (install, language, examples, …) |

## Overview {#overview}

Faber is designed around a core insight: the intermediate representation
is the truth, and no target or human-language surface is privileged. A
Faber program written in Latin keywords can be rendered into Thai,
Arabic, or Chinese keywords through the same mechanism that renders it
into Rust, Go, or WebAssembly — because the HIR is the authority and
every output is a *rendering* of it.

The language makes three deliberate signal choices that work together:

- **Type-first declarations** — shape reads toward binding: `textus nomen`,
  not `nomen: textus`.
- **Latin behavioural words** — declarations, statements, and lifecycle:
  `functio`, `genus`, `fixum`, `redde`, `si`.
- **Structural glyphs** — value flow and type joints: `←` (bind), `→`
  (return type), `∴` (compact branch), `≡` (equality), `∪` (union).

The result is source with stable grammatical shape that can be reviewed,
transformed, and lowered without losing the reader's sense of intent.

## Documentation {#documentation}

| Section | Description |
|---|---|
| [History](/history/) | Development timeline, influences, and release history |
| [Features](/features/) | Reader locale, compilation lanes, Latin vocabulary, glyph system, design principles |
| [Syntax](/syntax/) | Complete reference: types, functions, control flow, errors, generics, collections |
| [Tooling](/tooling/) | Radix compiler pipeline, Faber CLI, codegen targets, scripting |
| [Ecosystem](/ecosystem/) | Norma, Cista, Triga, coreutils, AI Workbench, corpus |
| [Corpus](/corpus/) | Keyword and construct pages generated from the public corpus |
| [References](/references/) | EBNF grammar, design documents, repositories |

## Quick example {#quick-example}

A simple function demonstrating key Faber patterns — type-first
parameters, glyph return type, nullable union, Latin control words:

```text
functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ∴ redde nihil
    redde a / b
}
```

## Live rendering {#live-rendering}

The divide function above is rendered in the Latin pack by default. The
compiler can render the same program in seven reader locales — Thai,
Chinese, Arabic, Hindi, Vietnamese — each remapping keywords and types
to that language while glyphs and identifiers remain unchanged. This is
not a translation layer applied to the page; it is the same mechanism
the compiler uses to produce localized source.

See the [reader locale](/features/reader-locale.html) documentation for
the full discussion.

## Repositories {#repositories}

| Repo | Role |
|---|---|
| [faberlang/faber](https://github.com/faberlang/faber) | Public user CLI |
| [faberlang/releases](https://github.com/faberlang/releases) | Tagged CLI release assets |
| [faberlang/faber-runtime](https://github.com/faberlang/faber-runtime) | Runtime types for generated Rust |
| [faberlang/norma](https://github.com/faberlang/norma) | Standard library source |
| [faberlang/cista](https://github.com/faberlang/cista) | Package-store CLI/lib |
| [faberlang/triga](https://github.com/faberlang/triga) | Graphics / geometry library |
| [faberlang/examples](https://github.com/faberlang/examples) | Corpus, tracks, application packages |
| [faberlang/faberlang.dev](https://github.com/faberlang/faberlang.dev) | This documentation site |
