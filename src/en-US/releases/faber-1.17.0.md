+++
title = "Faber 1.17.0"
description = "Release notes and install details for Faber 1.17.0."
section = "releases"
order = 10
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Faber |
| **Version** | 1.17.0 |
| **Tag** | `faber-v1.17.0` |
| **GitHub** | [faber-v1.17.0](https://github.com/faberlang/releases/releases/tag/faber-v1.17.0) |
| **Published** | 2026-10-29 |
| **License** | MIT OR Apache-2.0 |

## Install this version {#install}

Pinned download for **Faber 1.17.0**. For the current release, use [Start](/start/) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [faber-v1.17.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.17.0/faber-v1.17.0-aarch64-apple-darwin.tar.gz) | 33.4 MB | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.17.0/faber-v1.17.0-aarch64-apple-darwin.tar.gz.sha256) |
| **Linux x64** | [faber-v1.17.0-x86_64-unknown-linux-gnu.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.17.0/faber-v1.17.0-x86_64-unknown-linux-gnu.tar.gz) | 37.4 MB | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.17.0/faber-v1.17.0-x86_64-unknown-linux-gnu.tar.gz.sha256) |

```bash
# The installer verifies the checksum and installs a versioned
# binary that `faber update` and `faber versions` manage.
curl -fsSL https://raw.githubusercontent.com/faberlang/faber/main/install.sh \
  | sh -s -- --version 1.17.0
export PATH="$HOME/.faber/bin:$PATH"
faber --version
```

## Release notes {#notes}

> **Status**: final — tagged `faber/v1.17.0` on 2026-10-29

Faber 1.17 follows 1.16 with list size ranges, ranged integer stores and more device execution. CPU kernels now use worker threads, Metal gains more kernel forms, and scan and grouped reductions reach the device targets. There is also a long run of fixes to generated programs, numeric stores and cross-module calls. The tools are easier to use: diagnostics show their message and help by default, `faber explain` uses the reader's spellings, and `faber run --target` can build and run Go, TypeScript and LLVM programs or compile in memory with Cranelift. Some features still check but cannot run on every target; the known ranges are listed below.

> **Experimental through version 1.** The language changes constantly, and breaking changes ship in minor releases. Faber 1.17 carries no stability promise, and neither does any other 1.x release. A 2.0 release is planned for when the language is largely stable.

### Language

**Kernel safety tiers.** A kernel has one of three ordered tiers. `@ kernel` is the default: checked indexing and IEEE-correct float math, with FMA contraction, reordered reductions and bounded library approximations allowed. `@ kernel relaxed` permits approximate division and square root, fast transcendentals, flushing denormals to zero and float reassociation. `@ kernel unsafe` includes relaxed math and permits removing unproven index checks; an out-of-range access is undefined behaviour. Explicit checks written in the source stay in force, and integer and decimal results stay exact.

`faber run --safe`, `faber build --safe` and `safe = true` under `[device]` in `faber.toml` lower every kernel to the default tier. Metal now chooses precise or fast math from the tier. The backend work is not complete: CUDA does not yet select its math by tier, and `unsafe` does not yet remove index checks. Do not treat `--safe` as a precise-math guarantee on CUDA in this release.

**64-bit values in kernels.** `i64`, `u64`, `wrapping<u64>`, `saturating<u64>` and `d64` are legal kernel values, no longer language errors. The `nucleum_wide_integer` and `nucleum_d64` check errors retire. Metal carries 64-bit integer lanes and decimal arithmetic. A decimal store rounds half-even to eight fractional digits; overflow and division by zero report a device fault. Unsupported operations and device targets refuse the program by name. CUDA 64-bit storage-buffer kernels, and wide lanes on WGSL and AMD, are not built here. `f64` remains forbidden in kernels.

**A lane-local return.** `return thread` means “end this lane”, even inside an ordinary loop nested in the lane. It takes no value; lanes publish results through stores. Plain `return` still cannot leave a thread lane. Writing `return thread` outside a lane, with a value, or inside a nested closure or reduction body is a named `SEM010` error. The syntax, placement checks and formatter are present, but execution lowering is not: a correctly placed use is still refused as `return_thread_lowering_pending`.

**Ranges on integer cells.** A store policy can carry a range: `saturating<u32, 0‥8>` clamps to 0 through 7, `trapping<i32, -2‥3>` traps outside −2 through 2, and `wrapping<u32, 0‥8>` reduces modulo eight. `‥` is half-open; `…` includes the high end. Both ends must be written, with `∞` or `-∞` for an unbounded side. Arithmetic computes before the destination applies its policy once. The runner and Rust apply these ranges; other executable targets and kernels refuse them by name.

**List lengths and short literals.** `list<T, size lo‥hi>` carries a length range. Growing past its maximum or removing below its minimum reports on `⇥`. A list whose minimum is at least one has non-optional `first()` and `last()` results. `list<T, size N>` means at most `N` elements, not exactly `N`.

A short literal now takes the destination's capacity instead of bringing a smaller, incompatible capacity of its own. A literal that is too long is still refused. Sized and length-ranged lists also keep their size rules when exported and imported.

```fab
main {
    let list<int, size 0…3> pair ← [1, 2]
    print pair
}
```

**First-match selection.** `reduce via first` selects the first matching tensor or matrix element in row-major order. Its result is always optional. The predicate runs for every element, including those after the first match, and a predicate error stays an error. It replaces the dedicated `primus_quem` / `ubi` form.

```fab
fn pick(tf32[3] xs) → f32 ∪ none {
    return reduce via first from xs let x { return x ≻ 2.0 }
}
```

Lists have a separate `xs.find(predicate)` method. It walks left to right and stops at the first match, returning the element or `none`. Finding in a list of optional elements returns one optional, not a nested optional. `xs.extend(ys)` appends a whole list in place, in order. The receiver must be an unbounded `mut list<T>`; a bounded or length-ranged receiver is refused. Extending a list with itself appends its original elements once.

**Scans and device blocks.** Ordered prefix scans are available through `scan via`, with inclusive or exclusive prefixes and grouping. They lower to the runner, Metal and CUDA. `do all` defers kernel fault delivery to the block's exit. `do device { … } catch e { … }` additionally checks the block as a device-resident region. Host effects, allocations inside the region and control flow that reads device-computed values are refused by name. This first version uses the same execution path as `do all`; it does not yet compile the region into a new device-side control-flow program. `faber check --device` reports its bindings, launches and host synchronisations.

**The store rule.** Integer arithmetic is computed before a cell traps, clamps or wraps at the store. The broader ruling that a value carries no policy, and that any destination policy can accept it directly, is recorded but not implemented in 1.17. Cross-policy stores still need `↦`; do not remove those conversions yet.

**New checks.**

- Type arguments are invariant. A named `list<u8>` cannot stand in for `list<int>`, and the same rule applies to other containers, tuples, references and function types. Fresh literals, spreads and lifted results are built by element stores.
- The checker uses integer guards, loop bounds and collection lengths to prove accesses in range. A proven list or text `at` or `slice` needs no error handler. Mutations invalidate the relevant length proofs, including mutations in conditions and loop bodies.
- A genus method keeps its enclosing type parameters rigid. Storing `T ∪ none` into a `T` cell is now refused there as it is in a free generic function.
- A function or module-level value may share a locale-pack type word, such as `list` or `tensor`. Type lookup still finds the builtin type.
- A newline ends a bare `return`. A return value must start on the same line.

**Optional calls and templates.** An optional call skips its arguments when the receiver is absent. It captures the receiver before evaluating arguments, accepts `mut` arguments and flattens an optional result. A template that mixes plain and numbered holes now warns with `WARN035 mixed_plain_numbered_template_holes`. The warning names the argument each plain hole reads and suggests numbering every hole; numbering itself is unchanged.

**Diagnostics are on by default.** `check`, `build`, `run`, `test`, `emit`, `format` and `convert` print the diagnostic message and help under the source line. Use `--no-diagnostics` for the compact form. One `faber explain` hint is printed for the first explainable error. JSON output is unchanged.

Help text has been rewritten to say what to do next, rather than only restating the refusal. The new help rows are translated into the other seven locale packs: Latin, Arabic, Hindi, Thai, Vietnamese, Simplified Chinese and Traditional Chinese. Byte-list/tensor diagnostic names now use `list_b8_to_tensor_*` and `tensor_to_list_b8_*`, including the corresponding target-prefixed names, with no aliases for the old names.

`faber explain` also resolves terms in the reader's locale. In English, ask for `fn` or `list`; a term from another locale gets a hint naming the reader's spelling.

### Targets

**Runner.** Integer constant expressions stored in float cells now print as floats, rather than integers. A wrong-length list-to-tensor conversion is catchable, and bounded-list append checks also apply through a field or index. Wrapping integer expressions no longer trap before reaching their destination store. Calls reuse frame buffers and precomputed parameter modes, reducing overhead in call-heavy programs.

**Rust.** A declared tensor `copy` now allocates independent storage. Wrapping and saturating integer stores, including conversions to decimal, have several wrong-result and unbuildable-code fixes. Explicit `ref` and `mut` list parameters now use checked indexing and borrowed iteration; more field, slice and lane-loop combinations compile without borrow conflicts. Imported failable functions keep the error type declared by their module, and union type tests emit correctly. Read-only list and class arguments can be borrowed instead of cloned, and reading a scalar field from a list element no longer clones the whole element.

**Go.** Imported failable calls return their errors to `catch`, including leaf faults and declared error conversions. Imported classes keep their field defaults, sized tensor coordinates compile, and names that differ only by casing no longer collide in the crypto library. Host float multiplication is kept separate from addition where Faber requires separate rounding. `faber build --target go` produces a movable project with its runtime included, and `faber run --target go` builds and runs it. Norma gains Go implementations for filesystem, networking, process and machine services.

**TypeScript.** An `if`/`elif` arm inside a loop no longer returns from a generated closure or loses a `continue`. Integer expression trees containing `wrapping<u64>` use `bigint`, rather than passing through JavaScript doubles. Printed templates keep their trailing newline, and library export lists preserve callable public names. `faber build --target ts` produces a Node project with the runtime included; `faber run --target ts` builds and runs it. These routes require `tsc` and Node.

**Float sums.** On the runner, Rust, Go and TypeScript, an `f32` tensor sum accumulates in a wider float and rounds once at the result. It no longer loses small additions through a sequential `f32` fold.

**Swift.** Mutable value parameters now use Swift's `inout` calling convention, so writes reach the caller instead of being refused or detached into a local copy. Mutable interface parameters retain their shared class identity without an unnecessary `inout`. This also admits more functions and closures with mutable parameters. Tensor support is still incomplete.

**Python.** Norma imports now emit Python module imports instead of failing merely because the resolved path contains a library prefix. Appending past a bounded list's capacity raises `FaberError`, including through a field or index, and a Faber handler can catch it. Tensor and kernel lowering still have unsupported cases.

**LLVM.** Records constructed in a callee and stored in a list keep their contents after the callee returns. A mutable binding from a list element aliases that element, and field-then-index stores now emit. Long loops no longer grow the stack with fixed-size temporary allocations on every iteration. Interface and union values gain tagged type tests and member narrowing, including `ref` and `mut` parameters. There is initial `d64` storage and addition, subtraction and multiplication support; other decimal operations remain incomplete. Multi-hole float formatting, imported failable calls, dynamic panic messages and trap exit classes also have fixes.

`faber run --target llvm-host` now uses the native build route. Build recipes are configurable, and release binaries include the runtime archive for supported host platforms, so building a program needs LLVM tools but not Cargo. Norma leaf calls remain unsupported on this target.

**Cranelift (`clif` and `clif-jit`).** `f32` arithmetic, conversions and stores now round to single precision. Container cells retain their `f32` width for display and comparison, rather than treating every float as `f64`. Printed templates keep their newline, and traps share the runner's messages and exit classes. The new `faber run --target clif-jit` compiles and runs in memory, without an object file or system linker. It has the same language limits as `clif`; build and emit commands refuse `clif-jit` by name.

**WebAssembly and Racket (`sexp`).** WebAssembly can box and unwrap optional floating-point values without losing their bit pattern. It also gains initial `d64` storage, addition, subtraction and half-even multiplication stores; decimal division, conversion and formatting remain unsupported. Racket now checks bounded-list append capacity, and its generated append guard no longer contains stray backslash symbols.

**Canonical Faber.** Re-emitted source preserves union-typed closure parameters, optional aliases, qualified variant paths and union type tests. It also keeps the fourth-root glyph, template hole labels and authored range spellings, including inclusive endpoints and infinity. These forms can be parsed and analysed again without changing their meaning or becoming ambiguous.

**Shared fixes and other targets.** Optional calls on the runner, Rust, Go and TypeScript flatten an optional result, pass mutable arguments and capture the receiver before evaluating arguments. List `find` over optional elements returns one optional, not a nested one. `main exit` now supplies the process status across targets; C and COBOL also use the result when the exit expression is a function call. Haskell continues to refuse a plain return inside a loop by name. These fixes do not make the preview targets complete implementations of Faber.

### GPU and devices

**Correct output on Metal.** A reduction split out of a fused kernel now indexes by the global thread ID, fixing wrong means once the input spans multiple workgroups. Whole-tensor writes into mutable output parameters, including a plain tensor copy, no longer disappear. Fused matmul tails stay attached to their matmul. Signed integer division and remainder, floating remainder, and decimal comparisons with literals now follow Faber's rules rather than the shader language's defaults.

**Correct output on CUDA.** Fused tails use the correct accumulator after ordinary, quantized and grouped matmuls. Return-form tails store at the guarded row-and-column position, and non-matmul output-parameter kernels now write their result instead of leaving zeros. Bounds checks widen unsigned coordinates without sign-extending them. Scalar kernel parameters, native math and device fault handling also gain fixes.

**Launches and tensor views.** A one-element lane domain now launches with the data tensor's extent. An empty grid reduction writes its coalesce fallback without launching a kernel. In-place updates inside host loops are recognised as loop carries, not rejected as cycles. Contiguous tensor views can bind their own byte range of an uploaded backing, so disjoint views of one backing can be used together. Non-contiguous or improperly aligned views are still refused by name.

**More kernel forms.** Ordered prefix scans and grouped grid reductions now lower through the device pipeline to Metal and CUDA, with reference execution on the runner. Decomposed forward and generated backward kernels run as ordered sequences, including the combination of multi-workgroup reduction partials. Metal also gains whole-tensor elementwise kernels with run-time extents, elementwise `sqrt` and `exp`, and constructed tuples of tensor results.

**Wide values on Metal.** Kernels can use 64-bit integer lanes and `wrapping<u64>`/`wrapping<i64>`. Metal also implements `d64` with a 128-bit intermediate carrier, half-even stores and device faults for overflow. Decimal multiplication and division use faster exact helpers. Metal and CUDA can read fixed-layout record tensor fields directly, widening `f16`, `i8` and `u8` fields without first copying the whole record. Wide-type support is still target-specific; an unsupported device refuses the kernel by name.

**Kernel math choices.** Metal's default kernel tier uses precise division, square root and transcendental forms. `@ kernel relaxed` and `@ kernel unsafe` select faster float forms. `faber run --safe`, `faber build --safe`, or `safe = true` under `[device]` lower every kernel to the default tier. This does not loosen host arithmetic. Metal also reduces bounds-check branching, reuses extent loads, binds proven read-only inputs in constant address space, and fuses suitable max/min reductions into the producing kernel. More square and tall `f32` matmuls use tiled SIMD-group execution.

**CPU device.** `--device cpu` now runs through the same session and launch pipeline as the GPU devices, using a multicore worker queue. Set `threads` under `[device]` to control the worker count. `--partitions` creates virtual partitions on CPU; on Metal it partitions one physical GPU with shared buffers, not several GPUs.

**Multiple NVIDIA GPUs.** `--device cuda --partitions N` can span the requested number of healthy GPUs, assigning a lane range to each. Peer copies use event ordering, and fault results are combined when the host next needs them rather than after every launch. A data-parallel training probe was 1.55× faster on two L40S GPUs than on one, with byte-identical results; a transfer-heavy stencil probe was slower. This is not a general scaling claim.

Memory spanning is not finished. Placement analysis can identify slab candidates and report them through `faber check --device cuda --partitions N`, but real launches still fall back to full replicas. Do not count the GPUs' combined memory as usable capacity yet.

**Device statistics.** Metal gains per-entry GPU timing through stage-boundary counter sampling on supported Apple GPUs. `--stats` separates encode-only `host_encode_ns` from `host_blocked_ns`, so time blocked while committing work is no longer reported as encoding. CUDA's libdevice path is configured with `[device] cuda_libdevice`; the `FABER_CUDA_LIBDEVICE` environment variable is retired.

### Tooling

**Diagnostics are expanded by default.** `check`, `build`, `run`, `test`, `emit`, `format` and `convert` now show the diagnostic message and help below the source line. `--no-diagnostics` selects the compact form. The old `--diagnostics` flag is gone; remove it from scripts. JSON output is unchanged.

**`faber explain` uses the reader's spellings.** `faber explain fn`, `faber explain list`, search and listing now use the selected locale throughout the reference's terms, syntax and cross-references. `--locale` overrides the package setting; outside a package the default is English. A query using another locale's identity spelling gets a hint naming the reader's spelling, not a silent alias. Source without a locale setting also defaults to English.

**Build and run compiled packages.** `faber run --target go`, `--target ts` and `--target llvm-host` build the package, then run it with its arguments, standard streams and exit status passed through. Go output carries a local copy of its runtime and the reached Norma modules. TypeScript output is a Node project with the reached modules and runtime support. Build settings can be supplied in `[target.go]`, `[target.ts]` and `[target.llvm-host]`. Missing target tools are reported by name.

**Cranelift in memory.** `faber run --target clif-jit` compiles to native code in the running process. It needs no object file, linker or Rust toolchain. It covers the same language subset as the Cranelift object target; selecting the JIT does not remove that target's limits. `build` and `emit` refuse `clif-jit` by name.

**Device controls.** `faber run --device cpu --threads N` now runs package kernels on CPU workers, rather than using the sequential reference route. `[device] threads` supplies the package default. `--partitions N` selects partitions for CPU, Metal or CUDA execution. `faber check --device cpu|metal|cuda` builds the device image without running it and prints `INFO001` advice about serialized or unplaceable kernels; `--partitions` also asks for partition advice. These are informational diagnostics, not errors.

**Verify at the default kernel tier.** `faber build --safe` and `faber run --safe` lower every relaxed or unsafe kernel to the default tier. `[device] safe = true` sets this for a package. The switch only lowers a tier; it never raises one.

**`faber test` does less repeated work.** A package is analysed once, and each test unit uses its import closure from that analysis. Setup failures are reported separately from MIR link failures. Package kernel tests can use `--device cpu --threads N`, or `--device reference` for sequential execution. Metal and CUDA are still not served by `faber test`. Rename `--solum-in` to `--only-in` in test commands.

**Formatting width is opt-in.** `faber format --width N` wraps at legal token boundaries, counting indentation in the width. `[format] width = N` supplies a package default, and the flag wins. With neither set, output remains unwrapped. A string, comment or protected span that cannot safely break is allowed to exceed the width. Formatting also keeps authored range spellings, including inclusive ranges and infinity bounds, instead of replacing them with resolved bounds.

**Corpus selection.** `faber corpus` gains `--domain`, `--category` and `--case`. These selectors and `--filter` add together: a case runs if any selector names it. They do not narrow one another. Domain and category selection require a suite that declares domains; an unknown exact case ID is an error.

**Exit statuses and statistics.** Tool failures now distinguish bad arguments (`64`), source errors (`65`), missing input (`66`), unavailable compiled support (`69`), internal failures (`70`), unwritable output (`73`) and bad configuration (`78`). Failed tests and formatting drift still return `1`; a program's own exit status passes through. Device statistics separate `host_encode_ns` from `host_blocked_ns`, and Metal can report per-entry GPU time where counter sampling is available.

**Packaging and installation.** The install script defaults to 1.17.0; `--version` still selects another published release. Release binaries carry the prebuilt LLVM host runtime, so building an LLVM program needs the LLVM tools but not a Rust toolchain. The `fmir-bin` build target is retired. `fmir` and `fmir-text` remain image outputs, not inputs to the public `faber run` command; run the source package instead.

**Norma.** `norma:console` exports a callable `print(string)` that writes one line and reports an I/O failure, like `write_line`. It is distinct from the `print` statement; calling `print(...)` without an imported or local function gets `SEM001 scribe_callee`, with help naming the import. Norma's text, encoding, JSON, TOML and HTTP code now handles reporting text slices explicitly. The Rust crypto HMAC build is fixed. Tensor construction examples use `tensor.construct`, and vector signatures use the explicit `size` marker. A relative `--library-home` is now resolved against the working directory before package resolution.

### Breaking changes

1. **English is the default code locale.** Latin source that relied on the implicit default must declare `locale = "la"` or select Latin explicitly in its configuration. `RADIX_DEFAULT_CODE_LOCALE` is removed.

2. **Sizes need `size`.** Rewrite `list<T, N>` as `list<T, size N>`, and do the same for `queue`, `stack`, `string` and `ascii` capacities. Rewrite the long vector form `vector<f32, 4>` as `vector<f32, size 4>`. The `vf32[4]` shorthand, bracketed vector extents and `_` holes are unchanged. Missing markers are named `SEM008` errors.

   Explicit generic call arguments need the marker too: rewrite `mk<int, 4>(xs)` as `mk<int, size 4>(xs)` and a shape argument as `size [2, 3]`. A missing marker is `SEM057 size_marker_required`.

3. **Byte type words are gone.** Rewrite `bytes` / `octeti` as `list<b8>`, and bounded forms as `list<b8, size N>`. Use `b8` for raw byte bits or `u8` for a numeric byte instead of `byte` / `octetus`. The retired words are ordinary unknown names, not compatibility aliases.

4. **Use the reader's method and import words.** English tensor edge policy calls use `.edge<clamp>()`, not `.limes<clamp>()`; Latin keeps `limes`. The math intrinsics are `rank` and `norm` in every locale. Record-form imports must use the current reader's field words; English uses `from`, `visibility`, `name`, `as` and `all`. A field word from another locale is `PARSE050 wrong_locale_import_field`.

5. **Replace dedicated first-match expressions.** Rewrite `primus_quem` with its `ubi` predicate as `reduce via first from … let … { return … }` in English, or the corresponding locale spelling. Use `find` for a list. Tensor first-match selection still evaluates every predicate.

6. **Do not implicitly change a container's element type.** A whole `list<u8>` no longer passes where `list<int>` is wanted. Write an explicit `↦ list<int>` conversion, or construct a fresh destination list. Optional values incorrectly accepted into a generic genus method's plain `T` cells must now be handled or defaulted.

7. **Put a return value on the return line.** A value on the next line is now a separate statement. Move it onto the `return` line if it is meant to be returned.

8. **Update diagnostic scripts.** Remove `--diagnostics` from `faber check` and `faber emit`; the expanded form is now the default. Add `--no-diagnostics` where a script needs compact text. Update filters for the renamed byte-list/tensor diagnostic names. `faber test --solum-in` becomes `faber test --only-in`.

9. **Update target and exit-status scripts.** `faber build --target fmir-bin` is removed; `fmir` and `fmir-text` remain. Source errors now exit 65, argument errors 64 and configuration errors 78. Runner and Cranelift traps use their failure class rather than always exiting 1; Rust traps no longer use panic status 101. Test for the failure class you need, or for any non-zero status, rather than assuming 1.

### How this release was gated

The full release gate ran on the release source: the test ladder (stages 1 to 5) and every corpus target leg, with no failing case. Cases a target cannot handle yet are pinned as expected failures, and each finding was classified the way an audit is. A `residual` finding blocks nothing material and ships as a known issue. A `block_range` finding blocks a defined feature, or a feature on some targets; it ships, and the range is listed below as unsupported. Only a `block_release` finding (a regression or silent wrong output in core functionality on a major target, a crash in a common path, broken install or packaging, or a security issue) holds a release. This release has no `block_release` findings.

Corpus results per target (cases that pass in `corpus-suites/full`; the rest are pinned expected failures or not applicable): runner 892, Faber canonical 868, MIR 863, Faber round-trip 861, Rust 854, TypeScript 804, Go 730, LLVM 692, Racket 673, Cranelift 646, Python 640, WebAssembly 605, Swift 468.

### Known issues

#### Unsupported ranges (`block_range`)

These are target-specific limits, not promises made by a successful check. Some stop at a named refusal. Others fail to build or produce a result that differs from the reference.

- **`return thread` is check-only.** The checker accepts it in a valid lane body, but execution and code generation are not implemented. Lowering refuses it with `return_thread_lowering_pending`.
- **AIR execution on source-emitting targets.** Programs that require the AIR route cannot use the runner, Rust, Go or TypeScript route in its place. They need a supported MIR-backed target.
- **Rust, including the canonical Rust route.** Optional class cursors, optional method calls, matrix element access and bounded-text methods remain incomplete. A list window of class elements does not preserve shared mutation. Some mutable union parameters and captured closures do not build. Causal softmax is missing from the tensor runtime.
- **Go.** Much of the lifted list, vector, matrix and tensor arithmetic is not lowered, nor are tensor copy-into and sink-into. List length ranges and ranged integer store policies are unsupported. Shared list-length changes through a second name are refused. Some mutable interface or union parameters, optional method calls and failable calls nested inside another operand do not build.
- **TypeScript.** General `int` values remain limited by JavaScript's exact-number range. Ranged integer stores, list length ranges, bounded-list append and sink-into are not supported. Several matrix, vector and tensor glyph operations, generic tensor shapes and activation methods remain incomplete. Optional method calls can lose their receiver.
- **LLVM.** Matrix-register operations, unbounded integers, much of decimal conversion and formatting, several tensor operations, indirect closure calls and optional calls remain incomplete. Native Norma I/O routes are still refused. Some generic programs produce LLVM that fails verification.
- **Swift.** Tensors, vectors, matrices, sparse tensors, bounded buffers, unions, references, several deferred or generator forms, and many imports remain unsupported.
- **Python.** Tensor values and device kernels are not supported. Several structural and bounded-container conversions, list length ranges, ranged integer stores and sink-into are also missing.
- **WebAssembly.** List windows, several bounded and aggregate conversions, interfaces, unbounded integers, matrix and vector operations, optional calls and device launches remain incomplete.
- **Racket.** List windows, shared mutable-container aliases, several tensor shape and copy operations, channels and device launches remain incomplete. Some regular-expression behaviour differs from the reference engine.
- **Cranelift, including the JIT.** Tensor, matrix and other device values remain outside the supported subset. Stepped list windows, list length ranges, ranged integer stores, several provider calls and native I/O routes are also missing.
- **Numeric expressions and input on other targets.** A wrapping unsigned xor-then-multiply expression can trap before its destination store on Rust, LLVM, Python, Racket and Swift. A plain read of all standard input still reads only one line on Rust, Go and TypeScript.
- **Source round-tripping and inspection.** Canonical source output still has gaps around generic class arguments, lifecycle hooks and stored stepped ranges. Single-file MIR inspection also has gaps for some cross-module constants and compile-time values.

#### Residual

- **Sibling libraries need the `size` marker.** The graphics library (triga) still writes bare vector and list capacities such as `vector<f32, 3>`, which 1.17 refuses (`SEM008`). Library sources must add the marker (`vector<f32, size 3>`) before they build with this release.

- **Metal hardware tests under load.** Hardware tests can time out on a busy shared machine. Repeat a timeout without competing workloads before treating it as a reproducible device failure.
- **Display details.** Bounded byte lists do not consistently print as bit-token lists across targets. The runner can print their raw bytes, and Rust can expose an internal carrier representation. Stored ranges also print in internal or noncanonical forms on several generated targets.
- **Library installation is manual.** There is still no library install command for the graphics, autograd and UI libraries.

### Not in this release

- Code generation for `return thread`: it is checked, but lanes that use it are refused until lowering lands.
- Kernel tier selection on CUDA, and index-check removal for `@ kernel unsafe`.
- A package manager and library install command.
- Memory spanning across multiple GPUs (lanes span GPUs; tensors are still replicated).

---

[All releases](/releases/) · [Start](/start/)
