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
changing meaning. Rust is the primary executable path; TypeScript, Go, LLVM,
and other targets have narrower, measured support.

Faber's public capability ladder is intentionally explicit:

- **Shipped:** reader-localized source, diagnostics, and formatting.
- **Proven now:** a bounded dual-backend training path through Metal and CUDA.
- **Building next:** Faber-owned GPU inference behind a pinned model contract
  and correctness oracle.
- **Frontier:** multi-device execution, virtual GPUs, sharding, and distributed
  training or serving are future direction, not current runtime claims.

The name derives from the Latin word for *maker* or *craftsman*. The
compiler is named Radix, from the Latin *root*. The language is
developed by Ian Zepp and released under the MIT license.

**New here?** Start with [Install and download](/start/install.html), then run
the sequenced start track: [Hello](/start/hello.html),
[Commands](/start/commands.html), and [Projects](/start/projects.html). For the
GPU path, read [device execution](/toolchain/cli.html#device-execution) and
the [target matrix](/toolchain/target-matrix.html).

## Download Faber 1.4.0 {#download}

Current release: **Faber 1.4.0** (tag `faber-v1.4.0`). Prebuilt CLI archives
for macOS and Linux; extract the `faber-v1.4.0-<target-triple>/faber` binary
and put it on your `PATH`.

| Platform | Archive | Checksum |
|---|---|---|
| **macOS arm64** (Apple Silicon) | [faber-v1.4.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.4.0/faber-v1.4.0-aarch64-apple-darwin.tar.gz) | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.4.0/faber-v1.4.0-aarch64-apple-darwin.tar.gz.sha256) |
| **Linux x64** (glibc) | [faber-v1.4.0-x86_64-unknown-linux-gnu.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.4.0/faber-v1.4.0-x86_64-unknown-linux-gnu.tar.gz) | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.4.0/faber-v1.4.0-x86_64-unknown-linux-gnu.tar.gz.sha256) |

Quick install (macOS arm64 example):

```bash
curl -fsSL -o faber.tgz \
  https://github.com/faberlang/releases/releases/download/faber-v1.4.0/faber-v1.4.0-aarch64-apple-darwin.tar.gz
curl -fsSL -o faber.tgz.sha256 \
  https://github.com/faberlang/releases/releases/download/faber-v1.4.0/faber-v1.4.0-aarch64-apple-darwin.tar.gz.sha256
expected=$(awk '{print $1}' faber.tgz.sha256)
actual=$(shasum -a 256 faber.tgz | awk '{print $1}')
test "$actual" = "$expected"
tar -xzf faber.tgz
sudo mv faber-v1.4.0-aarch64-apple-darwin/faber /usr/local/bin/
faber --version
```

All release notes and assets: [github.com/faberlang/releases · faber-v1.4.0](https://github.com/faberlang/releases/releases/tag/faber-v1.4.0).
Step-by-step: [Install guide](/start/install.html). Full historical inventory:
[Releases](/reference/releases.html).

### Radix compiler {#download-radix}

The **Radix** compiler (v0.79.0) is bundled inside Faber. If you need Radix
as a standalone CLI, prebuilt binaries are available:

- Release: [github.com/faberlang/releases · radix-v0.79.0](https://github.com/faberlang/releases/releases/tag/radix-v0.79.0)

Radix source is private. The public release artifacts include the compiler
binary and checksums.

| | |
|---|---|
| **Paradigm** | Package-oriented; semantic staging |
| **Typing** | Static, type-first; nullable via `T ∪ nihil` |
| **Glyphs** | `← → ∴ ≡ ∪ ⇥` |
| **Designed by** | Ian Zepp |
| **First appeared** | 2025 |
| **Compiler** | Radix (Rust) |
| **Lanes** | Application (HIR) · Systems (MIR) · GPU device path |
| **Primary target** | Rust → native binary |
| **Reader locales** | 8 shipped (la, ar, en, hi, vi, th-TH, zh-Hans, zh-Hant) |
| **Standard library** | Norma (`norma:*`) |
| **License** | MIT |

## Start here {#start-here}

| Path | Who | What |
|---|---|---|
| [Install](/start/install.html) | Human | Download, PATH, first `faber check` |
| [Hello](/start/hello.html) | Human | Create and run `salve-munde` |
| [Commands](/start/commands.html) | Human + agent | Daily CLI loop: check, build, run, test, explain |
| [Projects](/start/projects.html) | Human + agent | Move from hello-world into real packages |
| [Quick tour](/start/) | Human | Language shape in five minutes |
| [Examples](/start/examples.html) | Human + agent | Real packages: CLI apps, mailspace, GPU, corpus |
| [`/llms.txt`](/llms.txt) | Agent | Machine index — start here if you are a model |
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

These paths are not equal promises. Rust is the primary executable application
target. TypeScript and Go are file-emission surfaces. GPU support is split
between shader lowering and the narrower real-device route documented below.
The [target matrix](/toolchain/target-matrix.html) records the current support
boundary.

The language makes three deliberate signal choices that work together:

- **Type-first declarations** — shape reads toward binding: `textus nomen`,
  not `nomen: textus`.
- **Latin behavioural words** — declarations, statements, and lifecycle:
  `functio`, `genus`, `fixum`, `redde`, `si`.
- **Structural glyphs** — value flow and type joints: `←` (bind), `→`
  (return type), `∴` (clausura joint), `≡` (equality), `∪` (union).

The result is source with stable grammatical shape that can be reviewed,
transformed, and lowered without losing the reader's sense of intent.

## GPU device execution {#gpu-device-execution}

Faber now runs device programs on real GPUs. A package carries a device
program when its source declares an `@ nucleum` compute kernel and its
manifest declares a `[device]` section; the packaged image embeds Metal MSL
and CUDA PTX artifacts, each with a provenance hash. `faber run` selects the
backend explicitly and fails closed with a stable code rather than silently
falling back to CPU:

```bash
faber run --backend metal <package>   # Apple Metal (e.g. Apple M5 Max)
faber run --backend cuda  <package>   # NVIDIA CUDA (e.g. RTX 5070)
faber run --backend auto  <package>   # resolve: exactly one admitted backend
```

The accepted device proof covers forward kernels and a bounded training path —
a library-backed `train_step` / companion VJP with per-step observation cadence,
gradient-slot → buffer mapping, and end-of-run readback. It is a real-device
proof, not a general training framework or a broad hardware-coverage claim.
Proof fixture:
[`examples/training/device-summa`](https://github.com/faberlang/examples/tree/main/training/device-summa).
See [device execution](/toolchain/cli.html#device-execution) and
[Compiling and targets](/toolchain/compiling.html) for the full target
posture.

### Inference and multi-device status {#inference-and-multi-device}

Faber-owned GPU inference is in active development behind a pinned model
contract and a correctness oracle. It is not yet a shipped inference server or
a general GGUF support claim.

Multi-device execution is a frontier direction. Virtual GPUs, tensor/model or
pipeline sharding, collectives, and distributed serving require their own
accepted topology and runtime contracts. They are not current Faber runtime
capabilities.

## Documentation {#documentation}

Five sections, in the order most people need them.

| Section | What is in it |
|---|---|
| [Start](/start/) | Install, hello world, the daily commands, your first package, real examples |
| [Language](/language/) | The whole language: types, functions, errors, glyphs, reader locales, capabilities |
| [Toolchain](/toolchain/) | The `faber` CLI, compilation lanes and targets, Cista packages, Radix internals |
| [Libraries](/libraries/) | Norma (bundled), Triga (graphics), and the language corpus |
| [Reference](/reference/) | Grammar, generated target matrix, releases, design notes, repositories |

If you only read one page, read [The Faber language](/language/) — it contains a
complete program and the meaning of every token in it.

## Quick example {#quick-example}

A simple function demonstrating key Faber patterns — type-first
parameters, glyph return type, nullable union, Latin control words:

```text
functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ergo redde nihil
    redde a / b
}
```

## Live rendering {#live-rendering}

The divide function above is rendered in the Latin pack by default. The
compiler can render the same program in eight reader locales — English,
Thai, Simplified Chinese, Traditional Chinese, Arabic, Hindi, Vietnamese —
each remapping keywords and types
to that language while glyphs and identifiers remain unchanged. This is
not a translation layer applied to the page; it is the same mechanism
the compiler uses to produce localized source.

See the [reader locale](/language/reader-locales.html) documentation for
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

The full list — including the private compiler and where to file issues — is
on the [Repositories](/reference/repositories.html) page.
