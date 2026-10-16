+++
title = "Compiling and targets"
section = "toolchain"
order = 2
sources = [
  "docs/design/target-capability-matrix.md (40 KB)",
  "radix/README.md (Codegen Targets and HIR/MIR Split)",
  "faber targets CLI output",
  "radix/README.md (Compiler Performance section)",
]
+++

## Codegen targets

Faber has one language and many compilation contracts. Not every feature
must lower to every target. This page documents which features each target
supports, erases, warns on, or rejects.

### Policy verbs {#policy-verbs}

| Verb | Meaning |
|------|---------|
| **Support** | Lowers with intended semantics |
| **Erase** | Typechecks; codegen drops target-specific semantics |
| **Warn** | Legal Faber; no effect or degraded behaviour on target |
| **Reject** | Check or emit fails with explicit diagnostic |
| **Defer** | Parses/binds; lowering not implemented for any target |
| **Limited** | Stable contract with explicit subset gates |

### Target table {#target-table}

One front end and two intermediate representations (a typed HIR and a MIR) feed
about two dozen code generators. HIR targets emit readable source in another
language; MIR targets lower further, to IR, kernels or native code. Every
target is held to the same reference: the MIR runner (`faber run`). A generated
program is correct when its output and exit status match the runner's; a
construct a target cannot express yet is rejected by name
(`unsupported on target <t>: <construct>`), never approximated.

<!-- target-maturity:begin -->
How mature each target is, measured on the corpus (662 programs the suite runs, each with expected output; 134 more are meant to be refused). "Suite" counts are cases that pass in `corpus-suites/full` (`faber corpus`) out of the cases the suite applies to; the rest are pinned expected failures. C and Haskell have no corpus lane: each single-file program the runner passes was emitted, built with the real toolchain, and its output and exit status compared with the runner's.

| Target | `-t` | Output | Evidence | Source |
| --- | --- | --- | --- | --- |
| **Reference** | | | | |
| MIR runner | (`faber run`) | executes the program; the oracle | suite 606 / 662 (the rest are pinned expected failures) | public |
| Faber | `faber` | canonical Faber in the source's locale (`format`, `convert`) | round-trip 644 / 649 | public |
| FMIR / FHIR | `fmir`, `fhir` | serialized MIR and analyzed HIR artifacts | no corpus lane (exercised by the package build and run tests) | public |
| **Application languages** | | | | |
| Rust | `rust` | Rust source, or a full Cargo project | suite 645 / 654 | official binary |
| Go | `go` | Go source | suite 568 / 662 | official binary |
| TypeScript | `ts` | TypeScript source | suite 609 / 662 | official binary |
| Swift | `swift` | Swift source | suite 347 / 662 | official binary |
| Python | `python` | self-contained Python | suite 480 / 649 | official binary |
| Haskell | `haskell` | Haskell source | 77 of 593 single-file programs emit; 30 of those match the runner | official binary |
| **Systems and native** | | | | |
| C | `c` | C11 with a header-only runtime | preview: 223 of 593 single-file programs emit; 222 of those match the runner | public |
| LLVM | `llvm-text`, `llvm-host` | LLVM IR, or a native executable via clang | suite 535 / 662 | official binary |
| WebAssembly | `wasm`, `wasm-text` | WebAssembly text | suite 470 / 662 assemble (no host runtime yet) | official binary |
| Cranelift | `clif` | native objects with no external toolchain | preview: suite 509 / 649 | public |
| **GPU kernels** (kernel functions only) | | | | |
| Metal | `metal-text` | Metal Shading Language | kernel programs only | official binary |
| WGSL | `wgsl-text` | WebGPU compute shaders | kernel programs only | official binary |
| CUDA | (`--device cuda`) | NVVM IR through the device runtime | kernel programs only; hardware-gated, and `faber run --device cuda` fails closed in the default build | official binary |
| **Validation** | | | | |
| Racket | `sexp` | Racket s-expressions (a validation target) | suite 538 / 662 | official binary |
| **Experimental** (not in the released `faber`) | | | | |
| Fortran, COBOL, Pascal, Odin, BASIC | `fortran`, `cobol`, `pascal`, `odin`, `basic` | historical languages, a deliberate subset | default-off features; no corpus lane | private source |
<!-- target-maturity:end -->

Notes:

- Emit and match counts compare the emitted program's output and exit status
  with the runner's, for the single-file programs the runner passes; "emit"
  alone means source was produced, not that it built.
- The C and Cranelift targets are previews and are on by default in `faber`.
  Neither runs under `faber run`, and a construct either cannot express yet is
  rejected by name. `faber targets` on the binary you are running is the
  authority on what that binary can emit, and a target missing from the build
  is rejected with `PKG001 target_not_in_this_build`.
- The experimental historical targets (Fortran, COBOL, Pascal, Odin, BASIC)
  cover a deliberate subset (scalars, text, simple collections) and reject the
  rest by name. They exist partly as a test of the rule that targets implement
  Faber and never the reverse. They are default-off features and are not in the
  released `faber`.
- Standard-library I/O (files, processes, clocks, network) is wired on the Rust
  target today; most other targets reject programs that use it, which accounts
  for much of the gap between their counts and Rust's.
- "Public" means the generator's source is in the public repository. "Official
  binary" means it ships in the released `faber` but its source does not.
- The GPU rows are kernel functions only. `faber run --device metal` launches
  `@ kernel` functions on a real GPU (Apple silicon); `--device cuda` is
  selectable but hardware-gated and not enabled in the released binary: no CUDA
  runtime is registered, so it fails closed. `-t metal-text`, `-t wgsl-text`
  and `-t llvm-text` themselves remain emit-only.
- The table is generated from the corpus suite at release time, not edited by
  hand.

### What the CLI does with each target {#cli-capabilities}

`faber targets` prints the live capability flags. In the pinned build:

| Target | Build | Run | Package |
|--------|-------|-----|---------|
| `rust` | yes | yes | yes (Cargo project) |
| `fhir`, `fmir-text`, `fmir`, `fmir-bin` | yes | yes | yes |
| `llvm-host` | yes | yes | yes (native executable via clang) |
| `llvm-text`, `metal-text` | yes | device only | yes |
| `faber`, `ts`, `go`, `python`, `haskell`, `swift` | yes | no | no |
| `wasm`, `wasm-text`, `wgsl-text`, `sexp` | yes | no | no |
| `c`, `clif` | yes (preview) | no | no |
| `pascal`, `cobol`, `fortran`, `odin`, `basic` | default-off features | — | — |

### Pipeline routing {#pipeline-routing}

```
Source → Lex → Parse → Collect → Resolve → Lower → Typecheck → Analysis
                                                              ↓
                                    ┌─────────────────────────┴──────────┐
                                    │                                    │
                              HIR backends                        MIR backends
                                    │                                    │
   Rust · Faber · TS · Go · Swift · Python · Haskell · C       fmir · wasm · llvm · metal · wgsl · sexp · basic
```

**Do not read Metal/WGSL percentages on the [target matrix](/toolchain/target-matrix.html) as product completeness.** Those
rows score *full-language corpus terms* against a *kernel-only* emitter. Device
runs go through `faber run --device metal` (CUDA is hardware-gated and fails closed in the released binary; see
[device execution](/toolchain/cli.html#device-execution)).

For the **device-kernel summary** (how a device program runs and what each
device target emits) see
[Target matrix · Device kernel support](/toolchain/target-matrix.html#device-kernel-support).

For live capability flags, run `faber targets`.

### Full lowerability matrix {#full-matrix}

The large term × target tables (HIR application lane and MIR systems lane)
live on the [Target compatibility](/toolchain/target-matrix.html) page. That matrix
is generated from `grammar/EBNF_MATRIX.md` and reports **term lowerability only** —
not erase/warn policy, and not GPU product health. GPU backends and the “why
no CUDA column?” note are explained in that page’s summary.

## Compilation lanes

Faber has a single shared frontend — lex, parse, typecheck — and then forks into
multiple lowering routes depending on what the target needs. The intermediate
representations form a pipeline: source is analysed into HIR, optionally lowered
to MIR, and optionally detoured through AIR before final emission. Each IR serves
a distinct purpose, and each target consumes from whichever IR matches its needs.

### Pipeline overview {#overview}

```text
Source (.fab)  →  Lex  →  Parse  →  Collect  →  Resolve  →  Lower  →  Typecheck  →  Analysis
                                                              │
                                                    HIR (semantic core)
                                                    ┌─────┴─────┐
                                                    │           │
                                              Reader locale    MIR lowering
                                              (input/output)    │
                                                                │
                                                      ┌─────────┴─────────┐
                                                      │                   │
                                                CPU lanes           GPU lanes
                                                      │                   │
                                            ┌────┬────┼────┬────┐     ┌───┴───────┐
                                            │    │    │    │    │     │           │
                                          FMIR LLVM WASM  TS  Go   WGSL   Metal
```

The same frontend serves every target. After semantic analysis produces the HIR,
the compiler chooses a route based on the target:

- **HIR-direct** — emit directly from typed HIR for language-shaped backends (Rust, Faber, TypeScript, Go, Swift, Python, Haskell, C)
- **HIR → MIR** — lower to execution-shaped MIR, then emit for systems and low-level targets
- **HIR → MIR → AIR → MIR** — detour through pure-functional AIR for autodiff and fusion transforms, then rejoin MIR

### HIR — High-Level Intermediate Representation {#hir}

The HIR is the truth. It is a typed, language-shaped IR that preserves
declarations, type information, and structural relationships. Every Faber
program, regardless of its original locale or target destination, passes
through this representation.

#### Reader locale integration {#reader-locale-integration}

Reader locale operates through the HIR. A Faber source file written in Thai
keywords is parsed and lowered into the same HIR as the equivalent Latin
source. The locale is a surface rendering of the HIR, not a fork in the
semantic core.

- **Input:** localised source (Thai, Chinese, Arabic, etc.) → normalised HIR — **shipped**
- **Output:** HIR → localised source re-emission — **shipped** (`faber convert --to <locale>`)

`faber convert --to th-TH` round-trips any Faber source through the HIR and
emits it with Thai keywords, completing the symmetry: the same HIR can produce
any locale surface, just as it can produce any target backend. `faber format`
re-emits through the same HIR at the file's own locale and does not translate.

#### HIR-direct backends {#hir-direct-backends}

These targets emit directly from the typed HIR without lowering to MIR. They
preserve source-level structure longer and are suited for language-shaped output:

| Target | Status | Role |
|---|---|---|
| `Rust` | **Support** | Widest package product surface today (a Cargo project; the best-covered standard-library I/O). One projection of HIR — not the semantic center. |
| `Faber` | **Support** | Canonical source view through the HIR-backed re-emitter (`faber format` / `faber convert`). Round-trip stability. |
| `TypeScript` | Probe | HIR-direct file emission; see the target table for measured counts. Not a package product path yet. |
| `Go` | Erase | HIR-direct file emission; see the target table for measured counts; borrow modes erased. |
| `Swift`, `Python`, `Haskell` | Probe | HIR-direct file emission; see the target table for measured counts. |
| `C` | Preview | HIR-direct C11 with a header-only runtime; its source is in the public repository. |

### MIR — Mid-Level Intermediate Representation {#mir}

MIR is the execution-shaped IR. It represents control flow, locals, runtime
calls, places, branches, and error edges — the facts that low-level targets
need. Where HIR preserves source structure, MIR flattens it into a
control-flow graph.

HIR → MIR lowering translates language-shaped constructs into execution steps.
MIR is validated after lowering to catch structural issues before any backend
attempts emission.

> **Semantic ownership.** Faber maintains a clear boundary between rules
> enforced in the HIR/MIR (type checking, definite assignment, borrow mode
> lints) and rules left to target toolchains (Rust lifetime analysis, Go type
> safety). This prevents the compiler from duplicating work that target
> compilers already do correctly.

### AIR detour {#air}

AIR (Autograd / AI Representation) is a pure-functional transform detour off
the HIR → MIR path. It is entered by explicit annotation on individual
functions:

```faber locale=en mode=package
@ radix lane "air"
fn identity(bool value) → bool {
    return value
}

main {
    print identity(true)
}
```

The annotation needs a package whose `[build] target` is a MIR target (here
`target = "fmir"`); on a bare file the default Rust target reports
`TARGETLANE001 lane_requires_mir_backed_target`.

AIR-lane functions must satisfy a purity policy — no mutation, no effects,
no loops. Functions that violate this are rejected with a diagnostic before
AIR lowering begins. The rest of the program continues to use ordinary Faber
with mutation, effects, and loops.

After the AIR transforms complete their work (autodiff and fusion — both
shipped), the result is re-lowered to MIR and rejoins the ordinary MIR
backend pipeline. AIR owns no backends and no independent typechecker — it
is a transform checkpoint, not a parallel IR.

```text
HIR  →  AIR purity check  →  HIR to AIR lowering  →  AIR validation  →  AIR to MIR re-lowering  →  MIR backend
```

This architecture mirrors JAX's approach: keep a pure-functional
representation for transforms, lower to imperative IR only at the end.
AIR exists because running autodiff over imperative MIR would require
reconstructing purity from code that was lowered into mutation.

### CPU target lanes {#cpu}

CPU targets consume MIR and produce either executable artifacts or text for
external toolchains. Faber emits text where possible and relies on lower-level
toolchains for the final compilation step — analogous to how a C compiler
emits assembly for the assembler and linker.

#### FMIR — Faber's own MIR runtime {#fmir}

FMIR is the MIR-native package executor. The compiler extracts MIR into a
binary payload and wraps it with a short Rust kernel loader. This produces
a self-contained executable that runs the MIR through Faber's in-process
runner — no separate runtime installation required.

| Format | Description |
|---|---|
| `fmir-text` | Inspectable FMIR text image at `target/faber-mir/image.fmir.txt` |
| `fmir` | Compact binary FMIR image at `target/faber-mir/image.fmir` |
| `fmir-bin` | Self-contained runner at `target/faber-mir/exe/run` — embeds FMIR bytes |

#### LLVM text {#llvm}

Faber emits LLVM IR as text (`.ll`), not as integrated LLVM codegen.
The emitted IR is intended for external toolchain steps — verification,
optimisation, and native code generation are handled by downstream LLVM tools.
This is a staging and validation target, not a native codegen path embedded in
the compiler.

#### WASM {#wasm}

Faber emits WebAssembly text (`.wat`). `-t wasm-text` is the name; `-t wasm`
is an alias kept for compatibility, and converting the text to a binary module
is an external-tool step (`wat2wasm` or `wasm-tools`). The emitted module uses
external host imports (`faber_*` runtime symbols). Wasm is a
supported-with-limitations target: it proves the MIR lowering pipeline for an
open standard format, but there is no host runtime yet and it is not a package
delivery runtime.

#### TypeScript, Go, Swift, Python and Haskell (HIR-direct) {#typescript-go}

These are HIR-direct file-emission targets: they validate that Faber's
semantics translate into widely used type systems. Measured counts are in the
target table above. Full package build and run workflows center on the Rust
package path today, and standard-library I/O is wired on the Rust target — that
is a packaging convenience, not a claim that HIR meaning lives in Rust.

#### C (preview) {#c}

The C target emits one C11 translation unit from the typed HIR, with a
header-only runtime (`runtime/c/faber.h`). It lives in the public repository and
is a preview: it covers a growing subset (exact integer arithmetic, control
flow, functions, text, lists, classes and floats) and rejects everything else
by name (`unsupported on target c: <construct>`). The emitted program never
reaches undefined behavior; the corpus checks it under the undefined-behavior
and address sanitizers. It is on by default in `faber`, and
a GCC or Clang compiler builds the output.

```faber locale=en
fn fib(int n) → int {
    if n ≺ 2 then return n
    return fib(n - 1) + fib(n - 2)
}

main {
    mut int total ← 0
    mut int i ← 0
    while i ≺ 10 {
        total ← total + fib(i)
        i ← i + 1
    }
    print "sum of the first ten Fibonacci numbers: §"(total)
    print -7 / 2
}
```

`faber emit -t c fib.fab` writes this (the runner prints `88` and `-4`; the
built program prints the same):

```c
/* Generated by radix; do not edit. Needs the Faber C runtime header:
   compile with -I <runtime>/c (runtime/c in the Faber tree). */
#include "faber.h"

static int64_t f_fib(faber_arena *, int64_t);

static int64_t f_fib(faber_arena *faber_a, int64_t p_n) {
    if (p_n < INT64_C(2)) {
        return p_n;
    }
    return faber_store_i64((__extension__ ({ int64_t faber_t0 = f_fib(faber_a, (__extension__ ({ int faber_o = 0; int64_t faber_r = faber_sub_o(p_n, INT64_C(1), &faber_o); faber_o ? faber_store_i64(faber_sub(p_n, INT64_C(1)), "argument") : faber_r; }))); int64_t faber_t1 = f_fib(faber_a, (__extension__ ({ int faber_o = 0; int64_t faber_r = faber_sub_o(p_n, INT64_C(2), &faber_o); faber_o ? faber_store_i64(faber_sub(p_n, INT64_C(2)), "argument") : faber_r; }))); faber_add(faber_t0, faber_t1); })), "return");
}

int main(void) {
    faber_arena faber_root = {0};
    faber_arena *const faber_a = &faber_root;
    int64_t l_total = INT64_C(0);
    int64_t l_i = INT64_C(0);
    while (l_i < INT64_C(10)) {
        l_total = faber_store_i64((__extension__ ({ int64_t faber_t2 = l_total; int64_t faber_t3 = f_fib(faber_a, l_i); faber_add(faber_t2, faber_t3); })), "assignment to `total`");
        l_i = (__extension__ ({ int faber_o = 0; int64_t faber_r = faber_add_o(l_i, INT64_C(1), &faber_o); faber_o ? faber_store_i64(faber_add(l_i, INT64_C(1)), "assignment to `i`") : faber_r; }));
    }
    printf("%s\n", faber_join(faber_a, 2, "sum of the first ten Fibonacci numbers: ", faber_int_text(faber_a, l_total)));
    printf("%" PRId64 "\n", -INT64_C(4));
    return 0;
}
```

Build it with `cc -std=c11 -I <runtime>/c fib.c -o fib -lm`.

### GPU target lanes {#gpu}

#### WGSL (via WGPU) {#wgsl}

Faber emits WGSL compute shader source through the MIR pipeline. The emitted
WGSL is validated through `naga` (30.x) and includes a reflection
sidecar for bind-group metadata. This covers the device-safe kernel subset:
rank-1 `f32` device views are supported; rank-2 views reject. WGSL
is not a GPU launch runtime — Faber emits the shader source, but execution
requires an external WebGPU runtime. The [Triga](/libraries/triga.html)
library supplies the typed geometry, scene, and resource contracts consumed
by a WebGPU host.

#### Metal {#metal}

Metal compute shader text emission follows the same pattern as WGSL: Faber
emits Metal Shading Language source for the device-safe kernel subset. Metal
is the **device execution** path that runs today (`faber run --device metal`).
Metal is the Apple Silicon local-dev and API-parity host. CUDA (`--device
cuda`) is the planned NVIDIA host: it is hardware-gated and not enabled in the
released binary. WebGPU remains a browser graphics and headless lane (Triga),
not a package device-execution path.

#### Device execution (Metal; CUDA is hardware-gated) {#device-execution}

A package carries a device program when its source declares an `@ kernel`
compute kernel and its manifest declares a `[device]` section. `faber run
--device reference|cpu|metal|cuda|auto` runs it through the host driver and
fails closed with stable codes (`E_BACKEND_UNAVAILABLE`, `E_DEVICE_*`,
`E_NO_DEVICE_PROGRAM`) instead of silently falling back to the CPU. `reference`
runs kernels as ordinary functions on the MIR runner and is the oracle device
results are checked against. `cuda` is selectable but no CUDA runtime is
registered in the released binary, so it fails closed with `E_DEVICE_UNAVAILABLE`.

### Architecture note {#comparison}

Faber's compilation architecture is similar in spirit to how the Rust compiler
works. Rust lowers through HIR → MIR → LLVM IR, embedding the LLVM toolchain
directly for final native codegen. Faber takes a softer approach: it emits
text for external toolchains (LLVM text, WGSL, Metal, WAT) rather than embedding
them, while reserving direct code emission for its own runtime (FMIR) and its
widest package product surface today (Rust, where Cargo and rustc handle the downstream
pipeline).

The text-emission approach means Faber never needs to bundle LLVM, a Wasm
runtime, or a GPU driver — those remain external dependencies chosen by the
user. The tradeoff is that Faber cannot offer a single-command build for every
target; the user must install the appropriate toolchain for their chosen
backend.

### Target summary {#matrix}

The [target table](#target-table) above is the summary: what each target
emits and how well it matches the runner. `build`, `run`, and `package`
describe Faber workflows; external toolchains (rustc, wasm-tools, naga, clang)
handle final compilation for text-emission targets.

Full measured grammar × target lowerability (every corpus term, HIR and MIR
columns): [Target compatibility](/toolchain/target-matrix.html).

## Compiler performance

Radix's front end runs in-process and single-threaded, and `faber check` and
`faber run` never invoke an external toolchain. For `faber build -t rust` the
user-perceived time is dominated by Cargo and rustc, not by Faber's front end.
Reuse one Cargo target directory across builds so the compiled runtime crate
stays cached; building each program into a fresh `target/` pays the runtime
crate's compile cost every time.
