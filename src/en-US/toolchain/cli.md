+++
title = "The faber CLI"
section = "toolchain"
order = 1
sources = [
  "faber/README.md",
  "faber/AGENTS.md",
  "faber/src/cli/mod.rs",
  "faber/docs/release/v1.5.0.md",
  "radix/docs/design/faber-scripting.md",
]
+++

## Faber build tool

The `faber` CLI is the primary entry point for building, checking, running,
formatting, and testing Faber source. It wraps the Radix compiler into an
ergonomic developer tool.

### Core commands {#core-commands}

| Command | Purpose |
|---|---|
| `faber build <path>` | Compile a package to a target backend (default: Rust) |
| `faber check <path>` | Type-check without emitting code |
| `faber run <path>` | Build (if needed) and run a compiled package |
| `faber test <path>` | Run proba cases on the MIR stepper |
| `faber format <path>` | Apply canonical formatting (author mode by default) |
| `faber explain <term>` | Explain a glyph, keyword, grammar term, or diagnostic code |
| `faber emit <path>` | Compile to a target surface for stdout |
| `faber targets` | Show supported targets and capability notes |
| `faber init` | Create a new Faber package |
| `faber install` | Install a library package into the Cista store |
| `faber script <path>` | Run Faber source through the interpreter (never compiles to Rust) |
| `faber repl` | Interactive MIR stepper REPL |
| `faber verify <file>` | Run aspect verification on a single file |
| `faber verify-library <input>` | Verify a library package's target binding manifest |
| `faber model inspect <path>` | Inspect model-file metadata (safetensors) |
| `faber lex` / `parse` / `hir` / `mir` / `cli-ir` | JSON phase dumps (compatibility aliases for `radix <phase>`) |
| `faber host manifest` | Script host introspection (kernel manifest) |

### Building a package {#building}

```text
faber build my-package/ -t rust
```

The `-t` flag selects the codegen target: `rust` (default), `typescript`
(`ts`), `go`, `swift`, `faber` (`fab`, canonical re-emission), `fhir`
(portable FHIR package envelope), `wasm` /
`wasm-text` (`wat`), `llvm-text` (`llvm`), `metal-text` (`metal`),
`wgsl-text` (`wgsl`), and `sexp` (`racket`). Diagnostics can be promoted to
errors with `--deny-warnings` (all warnings) or `--deny <CODE>` (a specific
catalog code, repeatable).

### Device execution (Metal / CUDA) {#device-execution}

`faber run` can execute a package's device program on a real GPU. A package
carries a device program when its source declares an `@ nucleum` compute
kernel and its manifest declares a `[device]` section (`backend`, and
`inputs` for the kernel's input buffers):

```bash
faber run --backend metal <package>   # Apple Metal (e.g. Apple M5 Max)
faber run --backend cuda  <package>   # NVIDIA CUDA (e.g. RTX 5070)
faber run --backend auto  <package>   # resolve: exactly one admitted backend
```

Backend selection precedence: CLI `--backend` > manifest `[device] backend` >
`auto`. The packaged FMIR image's `device` section carries the canonical device
program plus Metal MSL and CUDA PTX artifacts (each with a provenance hash);
`faber run` drives a real Metal/CUDA session (load → allocate → copy-in →
launch → sync → readback → release) and reports the selected device, the
artifact/module hash, and the observed outputs. An explicit GPU request never
silently falls back: unavailable backends, bad descriptors, and
entry/dtype/shape mismatches fail closed with a stable code
(`E_BACKEND_UNAVAILABLE`, `E_DEVICE_*`, `E_NO_DEVICE_PROGRAM`).

### Checking without emitting {#checking}

```text
faber check my-package/
```

Runs the full front end (lex → parse → typecheck → MIR lowering) without
producing output artifacts. Use this in CI and editor integrations.

### Running tests {#testing-command}

```text
faber test my-package/
faber test . --filter smoke       # substring filter on case path or title
faber test . --include math       # load only *.proba sources matching a path pattern
faber test . --exclude 'nested/*' # skip *.proba sources matching a path pattern
faber test . --name my_case       # select by proba name
faber test . --suite suite/path   # select by probandum suite path
faber test . --tag slow           # select by tag modifier
```

`faber test` runs proba cases on the MIR stepper — no Cargo or rustc is
invoked for the package, so no Rust toolchain is needed. Inline `probandum`
and `proba` suites live alongside source code, and colocated `*.proba`
files are discovered as test-only sources (never imported, excluded from
Cista snapshots). See [Inline testing](/language/errors.html).

### Formatting {#formatting}

```text
faber format my-package/
```

Applies the canonical Faber formatter in author mode by default. The
formatter enforces consistent layout: one declaration per line, canonical
spacing, and standardized keyword surfaces. `--locale <locale>` re-emits in
a reader-locale surface (`--locale la` reproduces the former `--canonical`
path), `--check` verifies without writing, and `--stdout` writes to stdout
instead of updating files.

### Explaining diagnostics {#explaining}

```text
faber explain functio     # keyword reference
faber explain SEM001      # diagnostic explanation
faber explain ≡           # glyph reference
faber explain --search query
```

`faber explain` explains a Faber glyph, keyword, or grammar term, with
diagnostic codes as a subset. It reads from the language corpus
(`radix/corpus/`).

## In-process scripting

Alongside the compiled Rust path, Faber supports in-process interpreted
execution through the MIR stepper.

### Usage {#usage}

```bash
faber run --interpret script.fab
```

This runs Faber source in-process after the normal front half of the
compiler (parse through typecheck + MIR lowering), without invoking
`rustc` or spawning a build process.

### How it works {#how-it-works}

The compiler produces analysed HIR, validated MIR, and a resolved
runtime-intrinsic table. The MIR stepper dispatches MIR blocks straight
to a host, skipping the wasm emit/instantiate round-trip:

```
Source → Lex → Parse → Collect → Resolve → Lower → Typecheck
                                                      ↓
                                                 MIR lowering
                                                      ↓
                                              MIR stepper + Host
```

### Latency {#latency}

The scripting path runs the same linear frontend as the compiled path,
plus stepper time proportional to what the script actually executes:

| Phase | Cost |
|-------|------|
| Frontend (100-line script) | ~0.6 ms |
| MIR stepping | Proportional to executed statements |

The stepper never invokes `rustc` or spawns a process, so startup is
fast enough to feel like a shell script.

### Limitations {#limitations}

- The MIR stepper does not support all host I/O routes that the compiled
  path does — some `norma:*` wrappers remain compiled-only
- The stepper is a MIR-native diagnostic/reference executor, not a
  production runtime for deployed applications
- Package compilation through Cargo remains the widest package product path
  today (Rust projection); other targets are measured separately
