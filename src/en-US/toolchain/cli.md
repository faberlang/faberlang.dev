+++
title = "The faber CLI"
section = "toolchain"
order = 1
sources = [
  "faber/README.md",
  "faber/AGENTS.md",
  "faber/src/cli/mod.rs",
  "faber/docs/release/v1.6.0.md",
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
| `faber run <path>` | Interpret and run a source file, package, or archive on the MIR runner (never compiles); `--target` builds for a target and runs the result |
| `faber test <path>` | Run proba cases on the MIR runner |
| `faber format <path>` | Report files whose layout differs from canonical formatting; `--write` applies it |
| `faber convert <path> --to <locale>` | Convert source between reader-locale surfaces (report-only unless `--write`) |
| `faber explain <term>` | Explain a glyph, keyword, grammar term, or diagnostic code |
| `faber emit <path>` | Compile to a target surface for stdout |
| `faber targets` | Show supported targets and capability notes |
| `faber update` | Check for (`--check`) or install a newer release; `--version <V>` switches to an exact version, rolling back included |
| `faber versions` | List the installed versions and the active one |
| `faber init` | Create a new Faber package |
| `faber repl` | Interactive MIR runner REPL |
| `faber verify <file>` | Run aspect verification on a single file |
| `faber verify-library <input>` | Verify a library package's target binding manifest |
| `faber model inspect <path>` | Inspect model-file metadata (safetensors) |
| `faber lex` / `parse` / `hir` / `mir` / `cli-ir` | JSON phase dumps (compatibility aliases for `radix <phase>`) |
| `faber host manifest` | Script host introspection (kernel manifest) |

### Building a package {#building}

```text
faber build my-package/ -t rust
```

The `-t` flag selects the codegen target. `faber build --help` lists the
accepted values and `faber targets` shows each target's current capability
notes. Diagnostics can be promoted to errors with `--deny-warnings` (all
warnings) or `--deny <CODE>` (a specific catalog code, repeatable).

### Device execution (Metal / CUDA) {#device-execution}

`faber run` can execute a package's device program on a real GPU. A package
carries a device program when its source declares an `@ nucleum` compute
kernel and its manifest declares a `[device]` section (`device`, and
`inputs` for the kernel's input buffers):

```bash
faber run --device metal <package>   # Apple Metal (e.g. Apple M5 Max)
faber run --device cuda  <package>   # NVIDIA CUDA (e.g. RTX 5070)
faber run --device auto  <package>   # resolve: exactly one admitted device
faber run --device reference <package>  # plain sequential code on the MIR runner
faber run --device cpu   <package>   # processor cores as a device
```

`reference` is the oracle that device results are checked against: the kernels
run as ordinary functions, single-threaded, on the MIR runner. Since 1.17 `cpu`
is a separate device. It goes through the same session and launch pipeline as
`metal` and `cuda`, and a multicore worker queue runs the kernels. `--threads N`
(or `[device] threads`) sets the worker count, and `--partitions N` selects
partitions. A package without kernels runs on the reference route. Device
selection precedence:
CLI `--device` > manifest `[device] device` > `auto`. The packaged FMIR image's `device` section carries the canonical device
program plus Metal MSL and CUDA PTX artifacts (each with a provenance hash);
`faber run` drives a real Metal/CUDA session (load → allocate → copy-in →
launch → sync → readback → release) and reports the selected device, the
artifact/module hash, and the observed outputs. An explicit GPU request never
silently falls back: unavailable backends, bad descriptors, and
entry/dtype/shape mismatches fail closed with a stable code
(`E_BACKEND_UNAVAILABLE`, `E_DEVICE_*`, `E_NO_DEVICE_PROGRAM`).

Kernel integers. Since 1.17 a kernel may use `int` (64-bit), `i64`, `u64`,
`wrapping<u64>`, `saturating<u64>` and `d64` as values: parameters, tensor
elements, lane binders, locals and stores. `faber check` stays clean, and the
old `SEM008 nucleum_wide_integer` and `nucleum_d64` refusals are gone. Whether
a device can carry them is a per-target fact in the requirement report: Metal
does; the other device targets refuse the kernel by name rather than
approximate it. An integer intermediate beyond the 64-bit range (a `d64`
intermediate beyond its 128-bit carrier) is `SEM008 nucleum_wide_intermediate`,
and `f64` is still refused in kernels (`SEM008 nucleum_f64`). Write `i32` and
`f32` to keep a kernel portable to every device:

```faber locale=en
@ kernel
@ public
fn scale(tf32[4] a, i32 k) → tf32[4] {
    return a * (k ↦ f32)
}
```

### Kernel safety tiers {#kernel-tiers}

A kernel runs at one of three ordered safety tiers, written after `@ kernel`
(la `laxus`, `intutus`):

| Tier | Written | Float math | Index checks |
|---|---|---|---|
| default | `@ kernel` | IEEE-correct; FMA contraction, reordered reductions and library transcendentals within their published bounds | every check the compiler cannot prove stays |
| relaxed | `@ kernel relaxed` | adds approximate `/` and `sqrt`, fast transcendentals, flushing denormals to zero and reassociating float expressions | as default |
| unsafe | `@ kernel unsafe` | includes `relaxed` | also drops the checks the compiler cannot prove; an out-of-range access is undefined behaviour |

```faber locale=en
@ kernel
@ public
fn scale_default(f32 x) → f32 {
    return x * 2.0
}

@ kernel relaxed
@ public
fn scale_relaxed(f32 x) → f32 {
    return x * 2.0
}

@ kernel unsafe
@ public
fn scale_unsafe(f32 x) → f32 {
    return x * 2.0
}
```

The tiers are one ordered choice, not independent flags: `@ kernel relaxed
unsafe` is refused (`PARSE018 duplicate_nucleum_tier`), as is a tier on a
`fragment`, on anything that is not a kernel function, or a word that is not a
tier. Integer results stay exact at every tier, and a check the author wrote (a
`trapping` store, an `is_finite` test, a bounds test) always runs. On Metal the
default tier emits IEEE division, precise `sqrt` and precise transcendentals,
and the relaxed and unsafe tiers emit the fast forms; a backend that cannot
honour a tier runs the default one, never a looser one.

`faber run --safe` and `faber build --safe` run every kernel at the default
tier for that command, and `safe = true` under `[device]` in `faber.toml` does
the same for the package. The switch can only lower a tier, and no environment
variable sets it. Use it to check whether a relaxed or unsafe kernel changes
an answer.

### Updating faber {#updating}

`faber update --check` reports whether a newer public release exists.
`faber update` installs it under a versioned name (`faber-<version>`) beside
the running binary and moves the `faber` link to it; `--version <V>` installs
an exact version instead, which is also how you switch back to an older one.
`faber versions` lists what is installed and which one is active.

```bash
faber update --check
faber update
faber update --version 1.15.1
faber versions
```

### Checking without emitting {#checking}

```text
faber check my-package/
faber check --lower my-package/
```

Runs the front end (lex → parse → semantic analysis) without producing output
artifacts. Use this in CI and editor integrations.

`--lower` also lowers the program to Faber's reference form, without running
it, and reports the errors that semantic analysis alone cannot see: a program
that checks but cannot run. It needs a file or package path (not stdin). Since
1.16 it covers programs with command-line (`cli`) surfaces too.

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

`faber test` runs proba cases on the MIR runner — no Cargo or rustc is
invoked for the package, so no Rust toolchain is needed. Inline `probandum`
and `proba` suites live alongside source code, and colocated `*.proba`
files are discovered as test-only sources (never imported, excluded from
Cista snapshots). See [Inline testing](/language/errors.html).

### Formatting {#formatting}

```text
faber format my-package/
```

Runs the canonical Faber formatter, a HIR re-emit at the source file's own
reader locale. By default it only reports each file that would change and
exits 1 if any would. `--write` applies the change, `--check` is the explicit
spelling of the default, and `--stdout` writes the result to stdout instead.
Formatting never translates between reader locales; use
`faber convert --to <locale>` for that.

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

`--locale <locale>` chooses the reader locale whose spellings terms are listed
and looked up by; without it `faber explain` uses the current package's
`faber.toml` `[locale]`, else English. `--diagnostics-locale` is separate: it
sets only the message language of a diagnostic explanation.

## In-process scripting

Alongside the compiled `faber build` path, `faber run` executes Faber source
in-process through the MIR runner. Without `--target` it never compiles.

### Usage {#usage}

```bash
faber run script.fab
```

This runs Faber source in-process after the normal front half of the
compiler (parse through typecheck + MIR lowering), without invoking
`rustc` or spawning a build process.

### Building a target, then running it {#run-target}

`faber run --target <target>` is the one form of `run` that compiles. It builds
the package for that target, then runs the built program with the arguments
after `--`; the program's standard streams and exit code pass straight through.

| `--target` | What it builds and runs | Needs on `PATH` |
|---|---|---|
| `ts` | a Node project, run with `node` | `tsc` and `node` |
| `go` | a Go module (vendored runtime, builds offline), run as built | `go` |
| `llvm-host` | a native program through LLVM | `llvm-as`, `opt`, `clang` |
| `clif-jit` | native code compiled in memory with Cranelift and run in this process | nothing else |

```bash
faber run --target ts my-app/ -- --flag value
faber run --target clif-jit my-app/
```

A missing tool is refused by name. `faber build --target clif-jit` and `faber
emit --target clif-jit` are refused by name: that target exists to run. Device
packages keep their own route (`--device`, above).

### How it works {#how-it-works}

The compiler produces analysed HIR, validated MIR, and a resolved
runtime-intrinsic table. The MIR runner dispatches MIR blocks straight
to a host, skipping the wasm emit/instantiate round-trip:

```
Source → Lex → Parse → Collect → Resolve → Lower → Typecheck
                                                      ↓
                                                 MIR lowering
                                                      ↓
                                              MIR runner + Host
```

### Latency {#latency}

The scripting path runs the same linear frontend as the compiled path,
plus runner time proportional to what the script actually executes:

| Phase | Cost |
|-------|------|
| Frontend (100-line script) | ~0.6 ms |
| MIR stepping | Proportional to executed statements |

The runner never invokes `rustc` or spawns a process, so startup is
fast enough to feel like a shell script.

### Limitations {#limitations}

- The MIR runner does not support all host I/O routes that the compiled
  path does — some `norma:*` wrappers remain compiled-only
- The runner is a MIR-native diagnostic/reference executor, not a
  production runtime for deployed applications
- Package compilation through Cargo remains the widest package product path
  today (Rust projection); other targets are measured separately
