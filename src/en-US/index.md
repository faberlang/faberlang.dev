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

The language, public libraries, examples, and user tooling ship under the
**MIT** license. **Radix**, the compiler, is closed source for now and is
planned for open release once the language has clearer market demand — not as
a permanent fence around Faber. See [Open source](/open-source.html).

Faber's public capability ladder is intentionally explicit:

- **Shipped:** reader-localized source, diagnostics, and formatting.
- **Proven now:** bounded dual-backend device training on Metal and CUDA
  (device-resident steps with gradient mapping and numeric comparison on an
  accepted MLP path).
- **Building next:** Faber-owned GPU inference behind a pinned model contract
  and correctness oracle (CPU oracle stack exists; end-to-end device inference
  is not shipped).
- **Frontier:** multi-device execution, virtual GPUs, sharding, and distributed
  training or serving are future direction, not current runtime claims.

The name derives from the Latin word for *maker* or *craftsman*. The
compiler is named Radix, from the Latin *root*. Developed by Ian Zepp.
Language and supporting libraries are MIT open source; Radix remains closed
source until there is clearer demand for an open compiler (see the note
above).

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
| **License** | MIT |

## Start here {#start-here}

| Path | Who | What |
|---|---|---|
| [Start](/start/) | Human | One link to hand your model; it installs Faber for you |
| [Commands](/cheatsheet/commands.html) | Human + agent | Daily CLI loop: check, build, run, test, explain |
| [`/install.md`](/install.md) | Agent | Install route — start here if you are a model |
| [Agent guide](/agents/index.md) | Agent | How to learn Faber and ship a package |
| [Agent skills](/.well-known/agent-skills/index.json) | Agent | Focused skill guides (install, language, examples, …) |

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
  `fn`, `class`, `const`, `return`, `if`.
- **Structural glyphs** — value flow and type joints: `←` (bind), `→`
  (return type), `∴` (closure joint), `≡` (equality), `∪` (union).

The result is source with stable grammatical shape that can be reviewed,
transformed, and lowered without losing the reader's sense of intent.

## GPU device execution {#gpu-device-execution}

Faber now runs device programs on real GPUs. A package carries a device
program when its source declares a compute kernel with `@ kernel` and its
manifest declares a `[device]` section; the packaged image embeds Metal MSL
and CUDA PTX artifacts, each with a provenance hash. `faber run` selects the
device explicitly and fails closed with a stable code rather than silently
falling back to CPU:

```bash
faber run --device metal <package>   # Apple Metal (e.g. Apple M5 Max)
faber run --device cuda  <package>   # NVIDIA CUDA (e.g. RTX 5070)
faber run --device auto  <package>   # resolve: exactly one admitted device
```

The accepted device proof covers forward kernels and a bounded training path —
including a Gradus-backed dual-backend MLP path with device-resident state,
per-step observation cadence, gradient-slot → buffer mapping, end-of-run
readback, and numeric comparison against a pinned CPU oracle on both Metal and
CUDA. It is a real-device proof, not a general training framework or a broad
hardware-coverage claim. Starter fixture:
[`examples/training/device-summa`](https://github.com/faberlang/examples/tree/main/training/device-summa);
MLP dual-backend oracle authority also lives under
[`examples/training/mlp`](https://github.com/faberlang/examples/tree/main/training/mlp).
See [device execution](/toolchain/cli.html#device-execution),
[Compiling and targets](/toolchain/compiling.html), and the
[device kernel support summary](/toolchain/target-matrix.html#device-kernel-support)
(product GPU view — separate from the full-language corpus % tables).

### Inference and multi-device status {#inference-and-multi-device}

Faber-owned GPU inference is in active development behind a pinned model
contract (currently SmolLM2-class GGUF admission for the oracle track) and a
correctness oracle. The **CPU** oracle path — admission, dequant, decoder ops,
and greedy decode agreement on a pinned run — is engineering-real; **end-to-end device inference is not shipped**, and this is not a general GGUF product claim.

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
    si b ≡ 0 ergo redde nihil
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
| [faberlang/faber](https://github.com/faberlang/faber) | Public target APIs and project home |
| [faberlang/releases](https://github.com/faberlang/releases) | Tagged CLI release assets |
| [faberlang/norma](https://github.com/faberlang/norma) | Standard library source |
| [faberlang/cista](https://github.com/faberlang/cista) | Package-store CLI/lib |
| [faberlang/triga](https://github.com/faberlang/triga) | Graphics / geometry library |
| [faberlang/examples](https://github.com/faberlang/examples) | Corpus, tracks, application packages |
| [faberlang/faberlang.dev](https://github.com/faberlang/faberlang.dev) | This documentation site |

The full list — including the private compiler and where to file issues — is
on the [Repositories](/open-source.html) page.
