+++
title = "Faber"
section = ""
order = 0
sources = []
+++

**Faber** is a developer tool for writing typed compute programs that remain
readable across human-language surfaces and portable across measured
compilation and device paths.

> One semantic program. Readable in your language. Built for application code
> and real GPU work.

The same analyzed program can feed application targets or a device program.
Reader locales change keywords, primitive types, and diagnostics without
changing meaning. Every codegen target is a **projection** of HIR meaning —
support is stated **target by target** (see the
[target matrix](/toolchain/target-matrix.html)). There is no privileged
executable path; package workflows that use Rust today are one measured
product surface among several, not the language’s semantic center.

The compiler front end, the reference runner, the standard library, the grammar
and the locale packs are open source under `MIT OR Apache-2.0` in
[faberlang/faber](https://github.com/faberlang/faber). The official `faber`
release also carries code generators that are not in the public source. Faber
is experimental through version 1. See [Open source](/open-source.html).

Faber's public capability ladder is intentionally explicit:

- **Shipped:** reader-localized source, diagnostics, and formatting.
- **In development:** device execution. A package can carry a device program and
  run it with `faber run --device`; the route fails closed rather than falling
  back to the CPU.
- **Frontier:** multi-device execution, virtual GPUs, sharding, and distributed
  training or serving are future direction, not current runtime claims.

The name derives from the Latin word for *maker* or *craftsman*. The
compiler is named Radix, from the Latin *root*. Developed by Ian Zepp.

**New here?** Go to [Start](/start/): give your model one link and it
installs Faber for you. Then read the [Commands](/cheatsheet/commands.html).
For the GPU path, read [device execution](/toolchain/cli.html#device-execution)
and the [target matrix](/toolchain/target-matrix.html).

| | |
|---|---|
| **Paradigm** | Package-oriented; semantic staging |
| **Typing** | Static, type-first; nullable via `T ∪ none` |
| **Glyphs** | `← → ∴ ≡ ∪ ⇥` |
| **Designed by** | Ian Zepp |
| **First appeared** | 2025 |
| **Compiler** | Radix (Rust) |
| **Lanes** | Application (HIR) · Systems (MIR) · GPU device path |
| **Targets** | Projections of HIR/MIR — measured per target (Rust, Faber, TS, Go, …) |
| **Reader locales** | 8 shipped (en, la, ar, hi, vi, th-TH, zh-Hans, zh-Hant) |
| **Standard library** | Norma (`norma:*`) |
| **License** | MIT OR Apache-2.0 |

## Start here {#start-here}

| Path | Who | What |
|---|---|---|
| [Start](/start/) | Human | One link to hand your model; it installs Faber for you |
| [Commands](/cheatsheet/commands.html) | Human + agent | Daily CLI loop: check, build, run, test, explain |
| [`/install.md`](/install.md) | Agent | Install route — start here if you are a model |
| [Agent guide](/agents/index.md) | Agent | How to learn Faber and ship a package |
| [Agent skills](/.well-known/agent-skills/index.json) | Agent | Focused skill guides (install, language, packages, corpus) |

## Readable in your language {#locale-coverage}

English is complete. The other seven locales ship reader-locale packs and
generated corpus pages; their authored prose still falls back to English
while translation lands. Every locale is listed on the
[language portal](/porta/).

## One semantic program across surfaces {#overview}

Faber is designed around a core insight: the intermediate representation is
the truth, and no target or human-language surface is privileged. A Faber
program written in one reader locale can be rendered into another locale, or
lowered toward Rust, TypeScript, Go, LLVM, or a device program, because the HIR
is the shared semantic authority.

These paths are not equal promises. HIR is the semantic authority; each target
emits, validates, runs, or remains limited on its own terms. TypeScript and Go
are HIR-direct file-emission (and e2e) surfaces with rising measured floors.
GPU support is split between shader lowering and the narrower real-device route
documented below. The [target matrix](/toolchain/target-matrix.html) records
the current support boundary.

The language makes three deliberate signal choices that work together:

- **Type-first declarations** — shape reads toward binding: `string name`,
  not `name: string`.
- **Behavioural words** — declarations, statements, and lifecycle:
  `fn`, `class`, `let`, `return`, `if`.
- **Structural glyphs** — value flow and type joints: `←` (bind), `→`
  (return type), `∴` (closure joint), `≡` (equality), `∪` (union).

The result is source with stable grammatical shape that can be reviewed,
transformed, and lowered without losing the reader's sense of intent.

## GPU device execution {#gpu-device-execution}

A package carries a device program when its source declares a compute kernel
with `@ kernel` and its manifest declares a `[device]` section. `faber run`
selects the device explicitly and fails closed with a stable code rather than
silently falling back to the CPU:

```bash
faber run --device reference <package>  # plain sequential code on the MIR runner
faber run --device metal <package>      # Apple Metal
faber run --device cuda  <package>      # NVIDIA CUDA
faber run --device auto  <package>      # resolve: exactly one admitted device
```

`reference` is the oracle that device results are checked against. Device
execution is under active development; end-to-end device inference is not
shipped, and this page makes no claim about training on it. See [device execution](/toolchain/cli.html#device-execution),
[Compiling and targets](/toolchain/compiling.html), and the
[device kernel support summary](/toolchain/target-matrix.html#device-kernel-support).

Multi-device execution is a frontier direction. Virtual GPUs, tensor/model or
pipeline sharding, collectives, and distributed serving require their own
accepted topology and runtime contracts. They are not current Faber runtime
capabilities.

## Documentation {#documentation}

Five sections, in the order most people need them.

| Section | What is in it |
|---|---|
| [Start](/start/) | One link to hand your model; it installs Faber for you |
| [Language](/language/) | The whole language: types, functions, errors, glyphs, reader locales, capabilities |
| [Toolchain](/toolchain/) | The `faber` CLI, compilation lanes and targets, Cista packages, Radix internals |
| [Libraries](/libraries/) | Norma (bundled), Triga (graphics), and the language corpus |
| [Reference](/reference/) | Grammar, generated target matrix, releases, design notes, repositories |

If you only read one page, read [The Faber language](/language/) — it contains a
complete program and the meaning of every token in it.

## Quick example {#quick-example}

A simple function demonstrating key Faber patterns — type-first
parameters, glyph return type, nullable union, and control flow:

```faber
functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ergo redde nulla
    redde a / b
}
```

## Live rendering {#live-rendering}

The divide function above renders in your reader locale — the English
reader spelling on this page. The compiler can render the same program in
eight reader locales — English, Latin, Thai, Simplified Chinese,
Traditional Chinese, Arabic, Hindi, and Vietnamese — each remapping
keywords and types (Latin is the canonical compiler surface; the others
render the same program in that language) while glyphs and identifiers
remain unchanged. This is not a translation layer applied to the page; it is the
same mechanism the compiler uses to produce localized source.

See the [reader locale](/language/reader-locales.html) documentation for
the full discussion.

## Repositories {#repositories}

| Repo | Role |
|---|---|
| [faberlang/faber](https://github.com/faberlang/faber) | The open-source core: compiler front end, runner, standard library, grammar |
| [faberlang/releases](https://github.com/faberlang/releases) | Tagged CLI release assets |
| [faberlang/triga](https://github.com/faberlang/triga) | Graphics / geometry library |
| [faberlang/gradus](https://github.com/faberlang/gradus) | Autograd and ML library |
| [faberlang/tela](https://github.com/faberlang/tela) | UI and view library |
| [faberlang/tree-sitter-faber](https://github.com/faberlang/tree-sitter-faber) | Editor syntax highlighting |
| [faberlang/faberlang.dev](https://github.com/faberlang/faberlang.dev) | This documentation site |

The full list, and where to file issues, is on the [Open source](/open-source.html) page.
