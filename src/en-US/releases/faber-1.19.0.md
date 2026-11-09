+++
title = "Faber 1.19.0"
description = "Release notes and install details for Faber 1.19.0."
section = "releases"
order = 10
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Faber |
| **Version** | 1.19.0 |
| **Tag** | `faber-v1.19.0` |
| **GitHub** | [faber-v1.19.0](https://github.com/faberlang/releases/releases/tag/faber-v1.19.0) |
| **Published** | 2026-11-09 |
| **License** | MIT OR Apache-2.0 |

## Install this version {#install}

Pinned download for **Faber 1.19.0**. For the current release, use [Start](/start/) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [faber-v1.19.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.19.0/faber-v1.19.0-aarch64-apple-darwin.tar.gz) | 49.9 MB | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.19.0/faber-v1.19.0-aarch64-apple-darwin.tar.gz.sha256) |
| **Linux x64** | [faber-v1.19.0-x86_64-unknown-linux-gnu.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.19.0/faber-v1.19.0-x86_64-unknown-linux-gnu.tar.gz) | 56.0 MB | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.19.0/faber-v1.19.0-x86_64-unknown-linux-gnu.tar.gz.sha256) |

```bash
# The installer verifies the checksum and installs a versioned
# binary that `faber update` and `faber versions` manage.
curl -fsSL https://raw.githubusercontent.com/faberlang/faber/main/install.sh \
  | sh -s -- --version 1.19.0
export PATH="$HOME/.faber/bin:$PATH"
faber --version
```

## Release notes {#notes}

> **Status**: final — tagged `faber/v1.19.0` on 2026-11-08

Faber 1.19 follows 1.18 with a sectioned source file: one `.fab` file can now hold its program, its tests and the input and output a test run expects. Loops gain an `and` head that walks several lists in lockstep, and a comma in a loop head is now reserved for the next loop in. The kernel head is finished: `faber format` keeps it and the grammar reference lists it. A run-time size is now `let size N ← n`. `faber run` no longer falls back to the interpreter silently: a program that Cranelift declines is refused, and every slow route says so. The Norma `db` module, `do batch` and `do eligible` ship, and `f64` is legal in kernels on the routes that carry it natively. Four device-route programs that returned wrong numbers without an error now match the reference.

> **Experimental through version 1.** The language changes constantly, and breaking changes ship in minor releases. Faber 1.19 carries no stability promise, and neither does any other 1.x release. A 2.0 release is planned for when the language is largely stable.

### Language changes in this release

**File sections.** A source file may label parts of itself with whole-line markers: `+++ toml` (the header, on line 1 only), `+++ faber` (the program), `+++ faber test` (tests) and `+++ <format> <stream>` for the standard input a test run feeds the program and the output it expects. The stream formats are `text`, `json`, `jsonl` and `base64`; a `base64` marker ends with the SHA-256 of the decoded bytes. A section runs to the next marker or the end of the file, and there are no closers. A file with no markers is still all program, and the legacy `+++` … `+++` header stays valid.

```fab
+++ toml
locale = "en"

+++ faber
@ public
fn double(int x) → int {
    return x * 2
}

main {
    print double(21)
}

+++ faber test
test "doubles" {
    assert double(21) ≡ 42
}

+++ text stdout
42
```

`check`, `run`, `build` and `emit` compile only the program section. A `+++ faber test` section sees its program's `@ public` items, as a sibling file would. A file whose only Faber section is the tests is a test-only file: `faber test` runs it, and `check`, `run` and `build` refuse it with `PKG001 test_only_source`. Structural errors are `PARSE052`, one issue per error. `faber format` writes the header, the program, the tests, then stdin, stdout and stderr, and keeps every section's payload bytes.

**Loop heads.** `and` joins sources that walk together in one loop, with one binder per source joined the same way: `for from labels and values let label and value { … }` (Latin `itera ex … et …`). Any number of lists can walk in lockstep, and `at [i]` names their shared index. Sources must be lists; maps and sets are refused, and so are a range joined with `and` and sources whose lengths are known to differ (`SEM010 itera_lockstep_length_mismatch`).

```fab
main {
    let list<string> labels ← ["one", "two", "three"]
    let list<int> values ← [1, 2, 3]
    for from labels and values let label and value {
        print label
        print value
    }
}
```

A comma in a loop head now opens the next loop inward, and every clause after a comma starts with its own `from` or `range`. A bare comma source, the old lockstep spelling `for from a, b`, is refused with `PARSE001 itera_bare_comma_source`. Nested comma clauses parse, but this release does not lower them yet: `for range 0 ‥ m, range 0 ‥ n let i, j` is `SEM008 itera_nested_clause_unsupported`. Write separate nested loops for now. See "Breaking changes".

**The kernel head is complete.** `kernel name(params) [relaxed|unsafe|fragment] { … }` (Latin `nucleum`) is in the grammar reference, and `faber format` and `faber convert` now keep whichever head a file uses. `@ kernel fn` stays accepted. `--normalize-kernel-heads` on `format` or `convert` rewrites the annotation form to the keyword head.

**Run-time sizes are `let size`.** `let size N ← n` (Latin `sit magnitudo N ← n`) lifts a run-time `int` into a size at the declaration, checks it there and snapshots it. It needs an initializer: a deferred `let size N`, `mut size` and `ref size` are not size witnesses. `const size N = 64` stays the static form. The old run-time `const size N ← n` is `PARSE010 runtime_const_retired`. A named range end may carry one natural offset, as in `trapping<i32, 0 ‥ A - 1>`.

```fab
fn runtime_extent(int value) → int {
    return value
}

main {
    mut int n ← runtime_extent(3)
    let size N ← n
    n ← n + 10
    print N
    print n
}
```

**`do batch` and `do eligible`.** `do batch { … } catch err { … }` (Latin `fac gregatim`) is the canonical name for deferred kernel fault delivery. `do all` stays accepted in the same slot and means the same thing; `faber fac-batch-codemod --write` rewrites it. `do eligible { … }` (Latin `fac idonea`) grants device eligibility to its body and the functions it calls synchronously, and restores the surrounding permission on exit; a closure created inside captures none. It keeps ordinary `do` fault timing, and this release does not yet place eligible code on a device. A `do` takes one modifier word; compose them with nested blocks.

**`f64` in kernels.** A kernel may use `f64`, including the `f64` result of integer `÷`. The CPU device and CUDA carry it natively. Metal and WGSL refuse such a kernel by name, and AMD refuses it until a native path is verified. No target narrows `f64` silently or emulates it, and `auto` does not move an `f64` kernel to the CPU: pass `--device cpu`.

**`main` exit values are 0 to 255.** A constant exit value outside that range is refused (`SEM010 main_exit_out_of_range`), and a run-time value outside it traps, on the runner and every target.

**End-of-line comments.** A `#` comment may follow code on a line that completes a statement or a declaration, or that ends with a block's opening `{`. `faber format` keeps it on its line. A `#` inside an unfinished expression is still `LEX007 inline_hash_after_code`.

**`lb8`.** `lb8`, `lb16`, `lb32` and `lb64` are short forms of `list<b8>` through `list<b64>`.

**Range glyphs are padded in types.** `faber format` now writes `saturating<u32, 0 ‥ 8>` and `list<int, size 1 … 8>`, with spaces around the glyph. The tight spelling still parses.

**Thread reductions.** The rule that a `thread` reduction's element count be a multiple of 32 is gone.

#### Norma

**`norma:db`.** A SQLite module: `open` returns a `Connection` with `execute`, `prepare` and `begin`; a `Transaction` has `prepare`, `commit` and `rollback`; a `PreparedWrite` has `execute` and `execute_returning_id`. Failures arrive as `DbFault` on the error channel. Connections, transactions and statements are resources, so `copy` refuses them. The module runs on the runner and on generated Rust.

#### Running programs

**No silent fallback.** Without `--target`, `faber run` still compiles in memory with Cranelift. When Cranelift declines the program, `faber run` now stops with `ENGINE001` and exit status 69 before anything runs, instead of quietly using the interpreter. `--device reference` runs a program on the MIR runner by request. Other routes that land on the interpreter (`--shuffle-seed`, a zip archive, `--stats` outside a device route) print one `ENGINE001` note. `--strict-engine`, or `[run] strict-engine = true` in `faber.toml`, makes those notes errors too.

**Kernel programs.** A program that declares kernels runs its host half on the Cranelift JIT, against the device the run selects. On `--device cpu`, kernels that the Cranelift lane compiler accepts run as native code; a kernel it declines runs on the interpreted lane engine and says so once with `ENGINE002`.

**More run targets.** `faber run --target` now also takes `python`, `c` and `swift`, which build the package for that target and run the result. `--target runner` is retired: it stops with a message that names `--device reference`.

#### Tooling

**`faber check --target T`** reports the refusals that `faber build --target T` would give, writing nothing: a program that passes it is not refused later by a build for the same target. A package may declare its target in `faber.toml` under `[build] target`; `check` and `build` use it when no flag is given.

**`--device-mode explicit|eligible`** on `check`, `build` and `run` sets the device admission policy. `explicit`, the default, admits only declared kernels.

**`faber test`** runs a file's `+++ faber test` section and test-only files beside `.proba` files. `--forbid-only` refuses every `only` test instead of letting it narrow the run.

**`faber corpus`** reads a case's expected output from its own sections. `--expected` and the `.expected` sidecar are gone.

**`faber perf`** compares the variants of a performance scenario described by a `perf.toml` in its directory.

**`faber debug`.** `lex`, `parse`, `hir`, `mir`, `cli-ir` and `abi` move under a hidden `faber debug` group. The old top-level names stay as hidden aliases for this release.

**`faber build --threads N`** and `faber run --threads N` bake a worker count into the emitted `python`, `c`, `swift`, `go` and `ts` programs. Without it the program uses `[device] threads`, or half the host's cores.

#### Simulations

The simulations moved from `corpus-simulations/` to `corpus/simulations/`. Beside the four from 1.18, the directory now has `a2-flood`, a regional flood solver with run-time extent stencil kernels; `chemical-diffusion`, coupled spatial chemistry checked against an independent reference; `rocket-nozzle-flow`, a quasi-one-dimensional nozzle flow solver; and `structural-fea`, static linear elasticity solved matrix-free. The last two are paused spikes. Each has a README and a `PROVENANCE.md`. Device execution and the native Rust emitter are in the released `faber` binary, not the open-source build.

### Fixes

**Device routes no longer return wrong numbers silently.** Four programs ran to completion on `--device cpu` or `--device metal` with results that differed from `--device reference`. Each now matches the reference, and each has a corpus case or a regression test that runs it on every available route:

- `wrapping<u32>` arithmetic inside a CPU-device kernel (shifts, xors, multiplies and a mask, as in a per-lane hash) is reduced to 32 bits again. Unreduced values used to reach the kernel's output.
- `wrapping<u64>` arithmetic in the host half of a device program, which runs on the Cranelift JIT, keeps its wrapping policy. A `splitmix64` stream returned zeros, then garbage, from its second draw. A conversion from a wrapping value into an exact range still traps when the value is out of range.
- A `mut tensor<u64>` that a kernel advances on `--device cpu` keeps its state from one launch to the next. It used to read back as zero after every launch.
- A host copy-into (`<==`) between device regions now updates the device buffer, or is refused by name when it cannot. Before, the buffers kept their first-round contents.

**Targets.** `ordo` is now fully supported on LLVM. Twelve corpus cases that failed on one target now pass: on C (`generic-call-type-args`, `instans`, `reperta`), Go (`tensor-shape-generic`, `empty-match`, `lista-tensor-padded`), LLVM (`ordo`, `d64`, `d64-arithmetic`), TypeScript (`importa`), Python (`tensor`) and Cranelift (`valor-collection-defaults`). On LLVM, a chained call on a method that returns `self` keeps the receiver's identity. The runner keeps exact `u64` subtraction traps.

**Formatting.** `faber format` and `faber convert` keep record construction fields in source order, and keep static size declarations.

**`faber check`** reports a missing package path with its own diagnostic, which names the path.

### Breaking changes

1. **Lockstep loops use `and`.** Rewrite `for from a, b let x, y` as `for from a and b let x and y`. A range product written `for range 0 ‥ m, 0 ‥ n` is refused; write two nested `for range` loops.

2. **`faber run` refuses what Cranelift declines.** A script that relied on the silent fallback to the interpreter gets `ENGINE001` and exit 69. Pass `--device reference` to run on the MIR runner, and replace `--target runner` with `--device reference`.

3. **Run-time sizes.** Replace `const size N ← n` with `let size N ← n`.

4. **`main` exit values.** A `main` that exits with a value outside 0 to 255 is refused at compile time or traps at run time.

5. **Corpus expectations.** Move `.expected` sidecars into `+++ text stdout` sections; `faber corpus --expected` is gone.

6. **Inspection commands.** Call `faber debug lex` (and `parse`, `hir`, `mir`, `cli-ir`, `abi`). The top-level names are hidden and go away in a later release.

### Known issues

- **Nested loop clauses are not lowered.** `for range 0 ‥ m, range 0 ‥ n let i, j` parses and is refused with `SEM008 itera_nested_clause_unsupported`.
- **`return thread` is still check-only.** Code generation refuses it with `return_thread_lowering_pending`.
- **`do eligible` does not move work to a device yet.** The modifier and `--device-mode eligible` check and run with ordinary `do` semantics.
- **A `u64` above 2⁶³ on `--device cpu`.** The Cranelift JIT host half prints such a value as signed when it is read back from a tensor, and refuses a `u64` literal that large. `--device reference` prints it correctly. A fix is in progress.

### How this release was gated

A release is blocked by the Rust workspace tests and clippy, on the source tree and on the public export, and by the export's leakage check. The corpus is not a release gate: not every target supports every construct, and the corpus records which ones do.

### Not in this release

- Code generation for `return thread`.
- Device placement for `do eligible`.
- Nested comma clauses in loop heads, and lockstep heads on `reduce`.
- A public EVM target. The `evm` target is experimental, off by default and not in the released `faber`.
- A package manager and library install command.

---

[All releases](/releases/) · [Start](/start/)
