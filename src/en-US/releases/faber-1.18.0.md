+++
title = "Faber 1.18.0"
description = "Release notes and install details for Faber 1.18.0."
section = "releases"
order = 10
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Faber |
| **Version** | 1.18.0 |
| **Tag** | `faber-v1.18.0` |
| **GitHub** | [faber-v1.18.0](https://github.com/faberlang/releases/releases/tag/faber-v1.18.0) |
| **Published** | 2026-10-31 |
| **License** | MIT OR Apache-2.0 |

## Install this version {#install}

Pinned download for **Faber 1.18.0**. For the current release, use [Start](/start/) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [faber-v1.18.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.18.0/faber-v1.18.0-aarch64-apple-darwin.tar.gz) | 33.6 MB | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.18.0/faber-v1.18.0-aarch64-apple-darwin.tar.gz.sha256) |
| **Linux x64** | [faber-v1.18.0-x86_64-unknown-linux-gnu.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.18.0/faber-v1.18.0-x86_64-unknown-linux-gnu.tar.gz) | 37.7 MB | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.18.0/faber-v1.18.0-x86_64-unknown-linux-gnu.tar.gz.sha256) |

```bash
# The installer verifies the checksum and installs a versioned
# binary that `faber update` and `faber versions` manage.
curl -fsSL https://raw.githubusercontent.com/faberlang/faber/main/install.sh \
  | sh -s -- --version 1.18.0
export PATH="$HOME/.faber/bin:$PATH"
faber --version
```

## Release notes {#notes}

> **Status**: final — published 2026-10-31

Faber 1.18 follows 1.17 with a new kernel declaration form, a compile-time refusal for copying resources and a faster default engine: a plain `faber run` now compiles in memory with Cranelift and falls back to the runner when Cranelift declines a program. Vectors and matrices now copy on assignment, and overlapping writable kernel arguments are refused. Device loops allocate less and wait on the host less often. There is also a long run of fixes to the Go, LLVM, Rust and Cranelift targets. Some features still check but cannot run on every target; the known ranges are listed below.

> **Experimental through version 1.** The language changes constantly, and breaking changes ship in minor releases. Faber 1.18 carries no stability promise, and neither does any other 1.x release. A 2.0 release is planned for when the language is largely stable.

### Language changes in this release


**A kernel declaration head.** `kernel name(params) { … }` is the canonical way to declare a kernel. It takes the tier or `fragment` word after the parameter list, and other annotations still stack above it. `@ kernel fn` stays accepted and means the same thing. Latin uses `nucleum`.

```fab
@ public
kernel halve(tf32[4] a) relaxed → tf32[4] {
    return a / 2.0
}

main {
    let tf32[4] x ← [1.0, 2.0, 3.0, 4.0] ↦ tf32[4]
    print halve(x)
}
```

A declaration that carries both heads is `PARSE018 nucleum_double_head`, and `@ conversion` on a kernel head is `PARSE018 conversio_kernel_head`. `kernel` is claimed only where a declaration can start, so a function or variable may still use the word. The form is not finished in this release: `faber format` and `faber convert` print every kernel in the annotation form, so a formatted file loses the head, and the grammar reference does not list it yet.

**`copy` refuses resources.** `copy` stays deep, and a value that holds something with identity can no longer be duplicated. Copying a channel, or a `Closable` class, or any value that reaches one through a field, collection element, union or tuple member is now `SEM066 copy_nonduplicable_member`. The message names the member path. Share the value without `copy`, or pass it with `own` where the consumer may take it over. Deep copy of ordinary classes, lists and maps is unchanged.

**`faber run` compiles by default.** Without `--target`, `faber run` tries Cranelift in memory first and uses the runner when the compiler declines the program. The choice is made before anything runs, so a program that traps or exits non-zero is never run twice. `--target runner` selects the interpreter by name, and neither `--target runner` nor `--target clif-jit` falls back. Device runs, archives, `--stats` and `--shuffle-seed` stay on the runner. The runner remains the reference for correct output. On early measurements, a 200-million-iteration loop took about 0.6 seconds against about 70 on the runner; start-up differs much less.

**What `repeat N` means.** A `repeat N` test runs N times and passes only if every run passes. It does not retry until a pass. The reference now also says that `expect_failure` passes only when the body escapes through the error channel, and that `flaky` cases are rejected and their bodies do not run.

**`trap` returns a tagged result.** `trap { … }` yields `trapped<R, T>`, with variants `returned { value }` and `thrown { error }`, read with an ordinary `match`. A string success with a string error becomes legal, because the variants carry the difference. Matching the member types (`case int`, `case string`) stops working; see "Breaking changes".

**`expect_failure` means what it says.** A test marked `expect_failure` (Latin `erratur`) now passes when its body fails by a failed assertion or a runtime fault, and fails if the body passes cleanly. Timeouts and step-budget exhaustion keep their normal outcomes.

**`repeat N` is documented correctly.** A test with `repeat N` runs N times and passes only if every run passes. `flaky` is documented as rejected by the runner.

### More language rules

**Vectors and matrices copy on assignment.** `mut vf32[3] b ← a` is now an independent value on the runner, Cranelift, LLVM, Rust, Go and TypeScript; before, some targets shared it and others copied. Matrices follow the same rule wherever the target can store to a matrix element (see "Known issues"). `ref` over a vector or matrix local is refused as `SEM008 scalar_access_marker`.

**Kernel arguments must not overlap.** A kernel call whose writable argument may share storage with another argument is `SEM057 kernel_argument_overlap`, whether the overlap comes from the same tensor, an alias or a view. Read-only duplicates and overlapping read-only views stay legal. Device code generation now relies on this rule.

**Lanes can own scratch rows.** A lane may write `scratch[[lane, k]]`, its own row of a scratch tensor. The flattened form `h[[lane * pitch + j]]` is also admitted when loop bounds prove `j` stays below the pitch. `scratch[[i, i]]`, `h[[k + j]]` and any shorter stride stay refused, and a two-coordinate lane domain does not count as a flattened row.

**Borrow regions have no silent fallback.** Region inference now covers every construct the corpus and Norma use, including closures nested in value positions, compile-time blocks and `if … catch … else`. A construct that still has no region facts is `SEM008 region_facts_not_built` where the answer matters, not a quiet return to the old block-scope rule.

**Bounded buffers hold typed zero.** Unused slots in a bounded list are typed zero after construction and after any operation that shrinks it. Reading past the length is still an error. On Rust this removes the uninitialised slots the carrier used to expose.

**Better advice.** `WARN013` no longer suggests `let`, and `WARN008` no longer flags `mut`, for a source that is mutated through an alias, including a chained alias.

### Targets

**Cranelift (`clif` and `clif-jit`).** Vector operations and `is inf` type tests now compile, and a single-file program can call an imported module or read its constants. Value loops over a list with a capacity above ten work on the MIR routes. The Cranelift and LLVM runtimes now allocate from one root arena created at program entry. Tensors, matrices and other device values stay outside the supported subset; `clif-jit` refuses them, and a plain `faber run` hands them to the runner.

**LLVM.** Records keep their declared field order, which fixes `list<record>` elements and records passed between modules. A generic class instantiated in another module now links, and printing a class lists fields in declaration order. Decimal division works on `llvm-host`, and decimal comparison is exact, without rounding into a stored decimal first. Dense tensor `copy` allocates independent storage, and a wrapping expression no longer traps before its destination store. Appending past a bounded list's capacity now traps with exit 70.

**Rust.** Proven small integer arithmetic now uses native widths without the `i128` path. Anything the range proof cannot show keeps the exact route. Fixes cover imported `mut` calls, narrowed optional payloads, raw-bit shift grouping, numeric cast grouping, owned record field reads, `@ cli` argument binders used by a dynamic exit, and list literals in `list<T, size N>` fields. `mut list<f32>` parameters can be read with an `int` index, and a generic class with a map field builds again.

**Go.** Lists now alias as they do on every other target, including length changes through a second name. Tensor `copy` works. Float products no longer fuse into FMA on arm64, including nested products under a contextual float destination. Bounded-list spare slots are initialised.

**Python and Racket.** Appending past a bounded list's capacity now traps with exit 70 in the direct, field and index forms, where it used to succeed silently.

**C.** Lists of classes now emit C. The C target has its own corpus leg, which builds each program under the undefined-behaviour and address sanitizers and compares it with the runner. It remains a preview.

### GPU and devices

**Fewer allocations in steady loops.** After the first iteration, a loop that repeats the same kernels with the same shapes allocates and releases no device buffers on CPU and Metal. A shape change or a new kernel may allocate once and then settle again. Fresh kernel outputs no longer allocate a host copy until the host reads them.

**Fewer waits on the host.** The host now synchronises only at observation points and explicit reads. Metal keeps command buffers in flight and encodes the next step while the previous one runs. CUDA moves uploads and downloads to their own stream, ordered by events, so they can overlap kernel compute. Outputs are unchanged, but a kernel fault can now reach the program at the first read of the launch's output rather than at the end of the run.

**More kernel forms.** Metal and the CPU device admit vector kernel parameters, including a kernel with a single vector parameter. Packed `u8` and `i8` vectors keep their storage width, which fixes wrong lane values. CUDA code generation admits the same shapes.

**Kernel math on CUDA.** NVVM now selects `f32` division and square root by kernel tier: correctly rounded at the default tier, approximate at `relaxed` and `unsafe`. Transcendentals are not selected by tier yet. NVVM buffer parameters also carry `noalias` and `readonly`, justified by the new argument rule. Grouped reductions skip the device guard on key reads the checker has already proved, and CUDA helpers now guard unproven reads and fault as Metal's do.

**Decimals on Metal.** `d64` multiply-add is about 60 to 80 percent faster on the measured mixes through a faster rescale. It is still about 20 to 165 times slower than `f32`, depending on the iteration count. Division did not change measurably.

**Statistics and output.** Device statistics now report `buffer_alloc_count`, `buffer_release_count` and the buffer pool's hits, buffers and bytes. CUDA reports `gpu_busy_ns` from its own events instead of zero. A kernel fault exits 70 on CPU, Metal and CUDA, as it does on the reference device. The `device: selected backend` line moved to stderr, so stdout carries only program output.

### Simulations

Four complete programs now ship in `corpus-simulations/`, each with a README, a small smoke and its provenance. They show the same Faber source running on the reference route, on CPU workers and on Metal where each README says so.

- **fusion-containment:** particle orbits in Latin, with an English rendering beside the source, on the reference route, multicore CPU and Metal.
- **drone-mission:** a branchy mission simulation where each GPU lane flies a whole mission.
- **swarm-decimal:** a deterministic many-actor simulation in fixed-point decimals.
- **h264-encoder:** a constrained-baseline H.264 encoder on native multicore CPU workers. It makes no claim of GPU acceleration.

Device routes are in the released `faber` binary, not the open-source build.

### Tooling

**Choosing an engine.** `faber run --target runner` names the interpreter, and `--debug` reports when `clif-jit` declines a program. `faber corpus` also verifies the `clif-jit` and `c` targets.

**Locale flags do what they say.** `--diagnostics-locale` changes only the language of diagnostics, not the code locale. `--locale` now takes effect on a single-file `faber build` and wins over frontmatter. An installed `faber` reads Latin frontmatter correctly on `faber build -t llvm-text` and on the single-file `faber emit` routes. A frontmatter locale that is invalid, empty, not a string or cannot be loaded is now an error rather than silent English: `LOCALE003` on `faber run`, and `PKG001` on `faber check` and `faber build`.

**The public source builds again.** `cargo build -p faber` works from the open-source repository, and a release-gate step now builds the export so it stays that way. `faber format`, `convert` and `doc` keep comments on union variants, enum members and shared fields.

**`faber format` and `faber convert`.** Formatting no longer reports a false `SEM057 call_marker_on_read_only` on a valid imported `mut` call. `faber convert --to la` fixes three files that passed `check` but failed re-validation. Multi-file packages are still converted file by file (see "Known issues").

**LLVM runtime builds.** A reused build directory now keeps the runtime archive and its receipt together, the stale-archive check covers every crate the archive is built from, and the rebuild has a timeout again. Foreign changes to an archive still fail closed.

### Breaking changes

1. **`copy` of a resource is an error.** Remove `copy` where a value holds a channel or `Closable` class, or pass the value with `own`. The new diagnostic is `SEM066 copy_nonduplicable_member`.

2. **Writable kernel arguments must be disjoint.** A call where a writable argument overlaps another is now `SEM057 kernel_argument_overlap`. Pass disjoint tensors, or bind an independent copy.

3. **Vector and matrix assignment copies.** Code that relied on `b ← a` sharing a vector on the runner, TypeScript or Go must write back through `a`, or pass `mut`. Remove `ref` from vector and matrix locals.

4. **`faber run` is no longer always interpreted.** Output is meant to match the runner, but a script that needs the interpreter should say `--target runner`.

5. **Update device scripts.** Read the `device: selected backend` line from stderr. Expect exit 70 for a kernel fault on a device instead of 1. A fault may now arrive at the first read of a kernel's output, before later program output.

6. **Locale errors are real.** Fix any frontmatter locale that used to compile silently as English. Scripts that used `--diagnostics-locale` to change the code locale should use `--locale`. A single-file `faber build --locale` now overrides frontmatter.

7. **Borrow results can change.** With region inference total, a program may be accepted or refused differently than under the block-scope rule, and an uncovered construct is `SEM008 region_facts_not_built`.

8. **`trap` results.** Rewrite `case int` and `case string` arms on a `trap` result as the `returned` and `thrown` variants.

### How this release was gated

The release is gated by `./scripta/release-gate --locked-release-build` on the exact candidate, after the cheap gates pass. Corpus verification is `scripta/corpus-release`, with one `corpus-suites/full` leg per target: `runner`, `rust`, `canonical`, `go`, `ts`, `wasm`, `llvm`, `roundtrip`, `mir`, `sexp`, `python`, `clif`, `gpu` and `swift`. Each leg must report no failures. `swift` is optional, and `gpu` needs a Metal host. The `c` and `clif-jit` legs are not part of `corpus-release`.

Each finding is classified as an audit finding would be. A `residual` finding blocks nothing material and ships as a known issue. A `block_range` finding blocks a defined feature, or a feature on some targets; it ships, and the range is listed below as unsupported. Only a `block_release` finding holds a release.

Results on the candidate: `release-gate --locked-release-build` passed, including the public export build and the leakage scan. `corpus-release` passed: no failures on any target leg.

| Leg | Passed | Expected failures |
| --- | --- | --- |
| `runner` | 901 | 5 |
| `canonical` | 878 | 28 |
| `roundtrip` | 872 | 4 |
| `mir` | 870 | 6 |
| `rust` | 864 | 34 |
| `ts` | 812 | 93 |
| `go` | 741 | 164 |
| `llvm` | 701 | 204 |
| `sexp` | 680 | 207 |
| `clif` | 666 | 210 |
| `python` | 642 | 235 |
| `wasm` | 611 | 294 |
| `swift` | 469 | 436 |

The `gpu` leg ran no cases in this release: all 1,212 reported not applicable, so it proves nothing here. Metal and CUDA behaviour rests on the device tests and on each change's own receipts.

### Known issues

#### Unsupported ranges (`block_range`)

These are target-specific limits, not promises made by a successful check. Some stop at a named refusal. Others fail to build or produce a result that differs from the reference.

- **`return thread` is check-only.** The checker accepts it in a valid lane body, but execution and code generation are not implemented. Lowering refuses it with `return_thread_lowering_pending`.
- **The kernel head does not survive formatting.** `faber format` and `faber convert` rewrite `kernel name(..)` to the `@ kernel fn` form. The result means the same thing.
- **Kernels that return a scalar from tensors.** A public kernel with tensor arguments and a scalar return is refused when launched on the device routes, because the return buffer supports elementwise kernels only. `--device reference` runs it.
- **Matrix copy on assignment.** Rust builds of the copy-on-assign exemplar fail at the matrix element store. Go, LLVM, Python, Swift, Cranelift and C cannot construct the matrix value at all.
- **AIR execution on source-emitting targets.** Programs that require the AIR route cannot use the runner, Rust, Go or TypeScript route in its place. They need a supported MIR-backed target.
- **Rust, including the canonical Rust route.** Optional class cursors, optional method calls, matrix element access and bounded-text methods remain incomplete. A list window of class elements does not preserve shared mutation. Some mutable union parameters and captured closures do not build. Causal softmax is missing from the tensor runtime.
- **Go.** Much of the lifted list, vector, matrix and tensor arithmetic is not lowered, nor are tensor copy-into and sink-into. List length ranges and ranged integer store policies are unsupported. Some mutable interface or union parameters, optional method calls and failable calls nested inside another operand do not build.
- **TypeScript.** General `int` values remain limited by JavaScript's exact-number range. Ranged integer stores, list length ranges, bounded-list append and sink-into are not supported. Several matrix, vector and tensor glyph operations, generic tensor shapes and activation methods remain incomplete. Optional method calls can lose their receiver.
- **LLVM.** Matrix-register operations, unbounded integers, decimal conversion and much decimal formatting, several tensor operations, indirect closure calls and optional calls remain incomplete. Native Norma I/O routes are still refused. Some generic programs produce LLVM that fails verification.
- **Swift.** Tensors, vectors, matrices, sparse tensors, bounded buffers, unions, references, several deferred or generator forms, and many imports remain unsupported.
- **Python.** Tensor values and device kernels are not supported. Several structural and bounded-container conversions, list and vector conversions, list length ranges, ranged integer stores and sink-into are also missing.
- **WebAssembly.** List windows, several bounded and aggregate conversions, interfaces, unbounded integers, matrix and vector operations, optional calls and device launches remain incomplete.
- **Racket.** List windows, shared mutable-container aliases, several tensor shape and copy operations, channels and device launches remain incomplete. Some regular-expression behaviour differs from the reference engine.
- **Cranelift, including the JIT.** Tensor, matrix and other device values remain outside the supported subset. Stepped list windows, list length ranges, ranged integer stores, several provider calls, integer constants beyond `i64` and native I/O routes are also missing. Explicit `--target clif-jit` refuses these; a plain `faber run` falls back to the runner.
- **Numeric expressions and input on other targets.** A wrapping unsigned xor-then-multiply expression can trap before its destination store on Rust, Python, Racket and Swift. A plain read of all standard input still reads only one line on Rust, Go and TypeScript.
- **Source round-tripping and inspection.** Canonical source output still has gaps around generic class arguments, lifecycle hooks and stored stepped ranges. Single-file MIR inspection also has gaps for some cross-module constants and compile-time values.

#### Residual

- **Metal A2 under load.** The A2 reduced-grid oracle test produced a non-finite cell twice on a loaded machine and passes alone. A2 is not a public simulation. This is under investigation.
- **`trap_text_parity_test` under load.** The test timed out once at 600 s on a loaded machine and takes 32 s alone.
- **Two Swift cases.** `bounded/itera-ex-bounded-lista-above-ten` and `product/generic-class-import` fail on the Swift target and are pinned as known failures.
- **Multi-file package conversion.** `faber convert` analyses a package file by file, so a package whose files depend on each other can report per-file failures.
- **Metal hardware tests under load.** Hardware tests can time out on a busy shared machine. Repeat a timeout without competing workloads before treating it as a reproducible device failure.
- **Display details.** Bounded byte lists do not consistently print as bit-token lists across targets. The runner can print their raw bytes, and Rust can expose an internal carrier representation. Stored ranges also print in internal or noncanonical forms on several generated targets.
- **Library installation is manual.** There is still no library install command for the graphics, autograd and UI libraries.

### Not in this release

- Code generation for `return thread`: it is checked, but lanes that use it are refused until lowering lands.
- Index-check removal for `@ kernel unsafe`, and tier selection for CUDA transcendentals.
- Native compiled kernels on `--device cpu`. The chunk boundary for them exists, but CPU kernels are still run by the interpreter on worker threads.
- A public EVM target. The `evm` target is experimental, off by default and not in the released `faber`.
- `do eligible` and `--device-mode`, and the rest of kernel eligibility inference. They are approved and move to 1.19.
- The Norma `db` module. It is approved and moves to 1.19.
- Always space-padded range glyphs in types. Approved; moves to 1.19.
- The store ruling (a value carries no policy; the destination decides at every store). `docs/design/numeric-model.md` describes it, but the compiler does not fully follow it yet.
- A package manager and library install command.
- Memory spanning across multiple GPUs (lanes span GPUs; tensors are still replicated).

---

[All releases](/releases/) · [Start](/start/)
