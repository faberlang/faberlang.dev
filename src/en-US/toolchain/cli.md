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
| `faber run <path>` | Run a source file, package, or archive: compiled in memory with Cranelift (`clif-jit`); `--device reference` runs it on the MIR runner, `--target` builds for a target and runs the result |
| `faber test <path>` | Run test cases on the MIR runner: `+++ faber test` sections, test-only `.fab` files and `.proba` files |
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
| `faber perf <dir>` | Compare the variants of a performance scenario described by its `perf.toml` |
| `faber fac-batch-codemod <path>` | Rewrite legacy `do all` as `do batch` (report-only unless `--write`) |
| `faber debug lex` / `parse` / `hir` / `mir` / `cli-ir` / `abi` | Hidden developer group: phase dumps and the host ABI contract. The top-level `faber lex` … `faber cli-ir` names stay as hidden aliases for 1.19 |
| `faber host manifest` | Script host introspection (kernel manifest) |

### Building a package {#building}

```text
faber build my-package/ -t rust
```

The `-t` flag selects the codegen target. `faber build --help` lists the
accepted values and `faber targets` shows each target's current capability
notes. Without `-t`, `faber build` uses the manifest's `[build] target` when the
package declares one, and `rust` otherwise. Diagnostics can be promoted to
errors with `--deny-warnings` (all warnings) or `--deny <CODE>` (a specific
catalog code, repeatable).

`--threads N` bakes a worker count into the program emitted for `python`, `c`,
`swift`, `go` and `ts`. Without it the program uses `[device] threads` when the
manifest sets it, and otherwise half the host's cores, at least one.

### Device execution (Metal / CUDA) {#device-execution}

`faber run` can execute a package's device program on a real GPU. A package
carries a device program when its source declares a `kernel` and its manifest
declares a `[device]` section (`device`, and
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
partitions. A program without kernels opens no device: `--device reference`
runs it on the MIR runner, and `cpu`, `metal` or `cuda` run it on the default
host engine. Device
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
intermediate beyond its 128-bit carrier) is `SEM008 nucleum_wide_intermediate`.

Since 1.19 `f64` is legal in a kernel too, including the `f64` result of
integer `÷`. The CPU device and CUDA carry it natively; Metal and WGSL refuse
the kernel by name, naming the `f64` value and its line, and AMD refuses it
until a native path is verified. No device narrows `f64` silently or emulates
it, and `--device auto` does not move such a kernel to the CPU: pass `--device
cpu`. Write `i32` and `f32` to keep a kernel portable to every device:

```faber locale=en
@ public
kernel scale(tf32[4] a, i32 k) → tf32[4] {
    return a * (k ↦ f32)
}
```

### Kernel safety tiers {#kernel-tiers}

A kernel runs at one of three ordered safety tiers. The tier word follows the
parameter list of the `kernel` head (la `laxus`, `intutus`):

| Tier | Written | Float math | Index checks |
|---|---|---|---|
| default | `kernel name(…)` | IEEE-correct; FMA contraction, reordered reductions and library transcendentals within their published bounds | every check the compiler cannot prove stays |
| relaxed | `kernel name(…) relaxed` | adds approximate `/` and `sqrt`, fast transcendentals, flushing denormals to zero and reassociating float expressions | as default |
| unsafe | `kernel name(…) unsafe` | includes `relaxed` | also drops the checks the compiler cannot prove; an out-of-range access is undefined behaviour |

```faber locale=en
@ public
kernel scale_default(f32 x) → f32 {
    return x * 2.0
}

@ public
kernel scale_relaxed(f32 x) relaxed → f32 {
    return x * 2.0
}

@ public
kernel scale_unsafe(f32 x) unsafe → f32 {
    return x * 2.0
}
```

The tiers are one ordered choice, not independent flags: a head takes one mode
word, and the annotation form `@ kernel relaxed unsafe` is refused (`PARSE018
duplicate_nucleum_tier`), as is a tier on a `fragment`, on anything that is not
a kernel function, or a word that is not a tier. Integer results stay exact at
every tier, and a check the author wrote (a `trapping` store, an `is_finite`
test, a bounds test) always runs. On Metal the default tier emits IEEE division,
precise `sqrt` and precise transcendentals, and the relaxed and unsafe tiers
emit the fast forms. Since 1.18 CUDA selects `f32` division and `sqrt` by tier
too: correctly rounded at the default tier, approximate only at relaxed and
unsafe. A backend that cannot honour a tier runs the default one, never a
looser one.

`faber run --safe` and `faber build --safe` run every kernel at the default
tier for that command, and `safe = true` under `[device]` in `faber.toml` does
the same for the package. The switch can only lower a tier, and no environment
variable sets it. Use it to check whether a relaxed or unsafe kernel changes
an answer.

### Device admission {#device-mode}

`--device-mode explicit|eligible` on `faber check`, `build` and `run` sets the
device admission policy at compile time. `explicit`, the default, admits only
declared kernels. `eligible` also lets analysis admit proved ordinary functions
as device variants inside a `do eligible { … }` block. The policy does not choose
where code runs, and 1.19 does not yet place eligible code on a device.

### Device output and exit status {#device-output}

Since 1.18 the `device: selected backend` line goes to standard error, so
standard output carries only what the program prints. A kernel fault exits with
the same status on every device as on `reference`: 70. The host no longer waits
on each launch, so a fault can reach the program at the first read of that
kernel's output, before later program output.

`faber run --stats` and `--stats-file` report the device buffer counters under
`device.runtime`: allocations, releases, pool hits, and the buffers and bytes
parked in the pool. A steady kernel loop, the same kernels at the same shapes,
makes no device buffer allocations or releases once it has warmed up. The first
iterations of a shape can allocate; a new shape can allocate once, then settles
again.

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

`--target T` checks against compilation target `T` with the refusal logic
`faber build --target T` uses, writing nothing: what passes `check --target T`
is not refused later by a build for the same target. Without the flag, a
package whose manifest declares `[build] target` is checked against that
target; with neither, `check` runs semantic analysis only.

```text
faber check --target go my-package/
```

Since 1.18 borrow-region inference is total. A construct it cannot yet reason
about is refused by name (`SEM008 region_facts_not_built`) instead of being
approximated.

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
faber test . --forbid-only        # refuse every `only` test instead of focusing on it
```

`faber test` runs test cases on the MIR runner, whatever engine `faber run`
would pick — no Cargo or rustc is invoked for the package, so no Rust toolchain
is needed. Since 1.19 a source file can carry its own tests in a `+++ faber
test` section after its program; the section sees the program's `@ public`
items, as a sibling file would. A file whose only Faber section is the tests is
a test-only file: `faber test` runs it, and `check`, `run` and `build` refuse it
(`PKG001 test_only_source`). Inline `probandum` and `proba` suites still live
alongside source code, and colocated `*.proba` files are discovered as
test-only sources (never imported, excluded from Cista snapshots). See [Inline
testing](/language/errors.html).

`faber corpus <case>` runs a case and compares its output with the file's own
`+++ text stdout` (or `json`, `jsonl`, `base64`) and stderr sections, feeding
any `+++ … stdin` section to the program. Since 1.19 there is no `--expected`
flag and no `.expected` sidecar.

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

Since 1.19 `faber format` and `faber convert` keep whichever kernel head a file
uses. `--normalize-kernel-heads` rewrites every `@ kernel fn name(..)` as
`kernel name(..) [mode]`. Formatting also writes a file's sections in canonical
order (the `+++ toml` header, the program, `+++ faber test`, then stdin, stdout
and stderr) without touching their payload bytes, keeps an end-of-line `#`
comment on its line, and spaces range glyphs in types (`0 ‥ 8`).

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

The same split holds on every command. Since 1.18 `--diagnostics-locale` never
changes how source is read, and `faber build --locale` applies to a single file
and wins over its frontmatter. A frontmatter locale that is invalid or cannot be
loaded is an error, not silent English: `LOCALE003` on `faber run`, `PKG001` on
`faber check` and `faber build`.

## In-process execution

Alongside the compiled `faber build` path, `faber run` executes Faber source
in this process, with no external toolchain.

### Usage {#usage}

```bash
faber run script.fab
```

This compiles the program to native code in memory with Cranelift, the
`clif-jit` engine, and runs it. There is no object file, no linker and no
`rustc`. Since 1.19 there is no silent fallback: when the Cranelift lowering
declines the program, `faber run` stops with `ENGINE001` and exit status 69
before anything runs. `faber run --device reference` runs a program on the MIR
runner by request, and never draws that refusal. A program that traps or exits
nonzero is never run a second time.

A program that declares kernels runs its host half on `clif-jit` too, against
the device the run selects. On `--device cpu`, a kernel the Cranelift lane
compiler accepts runs as native code; one it declines runs on the interpreted
lane engine and prints one `ENGINE002` note.

A zip archive, `--shuffle-seed`, and `--stats` outside a device route still run
on the MIR runner, and say so once with an `ENGINE001` note.
`--strict-engine`, or `[run] strict-engine = true` in `faber.toml`, turns those
notes into refusals with exit status 69. `--debug` reports the engine on
standard error.

```bash
faber run --device reference script.fab   # the MIR runner, by request
faber run --strict-engine my-app/         # refuse every slow route
```

### Choosing the engine {#run-target}

`faber run --target <target>` picks the engine and takes no fallback: a program
the engine refuses stops with that diagnostic. `clif-jit` runs in this process.
The others build the package for that target, then run the built program. Every engine takes the program's arguments after `--`, and the
program's standard streams and exit code pass straight through.

| `--target` | What it runs | Needs on `PATH` |
|---|---|---|
| `clif-jit` | native code compiled in memory with Cranelift | nothing else |
| `ts` | a Node project, run with `node` | `tsc` and `node` |
| `go` | a Go module (vendored runtime, builds offline), run as built | `go` |
| `llvm-host` | a native program through LLVM | `llvm-as`, `opt`, `clang` |
| `python` | a Python program | the target's own toolchain |
| `c` | a C program | the target's own toolchain |
| `swift` | a Swift program | the target's own toolchain |

```bash
faber run --target ts my-app/ -- --flag value
faber run --target python my-app/
```

Since 1.19 `--target runner` is retired: it stops with a message that names
`--device reference`. A missing tool is refused by name. `faber build` and
`faber emit` refuse `--target clif-jit` by name: that engine exists to run.
Device packages keep their own route (`--device`, above).

### How the runner works {#how-it-works}

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

The runner path runs the same linear frontend as the compiled path,
plus runner time proportional to what the script actually executes:

| Phase | Cost |
|-------|------|
| Frontend (100-line script) | ~0.6 ms |
| MIR stepping | Proportional to executed statements |

The runner never invokes `rustc` or spawns a process, so startup is
fast enough to feel like a shell script.

### Limitations {#limitations}

- `clif-jit` has the language limits of the `clif` target; a program it
  declines needs `--device reference` to run on the MIR runner
- The MIR runner does not support all host I/O routes that the compiled
  path does — some `norma:*` wrappers remain compiled-only
- The runner is a MIR-native diagnostic/reference executor, not a
  production runtime for deployed applications
- Package compilation through Cargo remains the widest package product path
  today (Rust projection); other targets are measured separately
