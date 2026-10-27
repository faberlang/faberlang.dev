+++
title = "Faber 1.16.0"
description = "Release notes and install details for Faber 1.16.0."
section = "releases"
order = 10
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Faber |
| **Version** | 1.16.0 |
| **Tag** | `faber-v1.16.0` |
| **GitHub** | [faber-v1.16.0](https://github.com/faberlang/releases/releases/tag/faber-v1.16.0) |
| **Published** | 2026-10-23 |
| **License** | MIT OR Apache-2.0 |

## Install this version {#install}

Pinned download for **Faber 1.16.0**. For the current release, use [Start](/start/) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [faber-v1.16.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.16.0/faber-v1.16.0-aarch64-apple-darwin.tar.gz) | 20.7 MB | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.16.0/faber-v1.16.0-aarch64-apple-darwin.tar.gz.sha256) |
| **Linux x64** | [faber-v1.16.0-x86_64-unknown-linux-gnu.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.16.0/faber-v1.16.0-x86_64-unknown-linux-gnu.tar.gz) | 23.2 MB | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.16.0/faber-v1.16.0-x86_64-unknown-linux-gnu.tar.gz.sha256) |

```bash
# The installer verifies the checksum and installs a versioned
# binary that `faber update` and `faber versions` manage.
curl -fsSL https://raw.githubusercontent.com/faberlang/faber/main/install.sh \
  | sh -s -- --version 1.16.0
export PATH="$HOME/.faber/bin:$PATH"
faber --version
```

## Release notes {#notes}

> **Status**: final — tagged `faber/v1.16.0` on 2026-10-23

Faber 1.16 follows 1.15.2 with a few new language forms and a long run of correctness fixes. A stored range can carry a step, a record literal no longer needs a declared type, any type can become a sink for the new `⇜` operator, and a matrix element reads and writes by row and column. Most of the release is not new syntax: the generated programs for every target were checked again against the corpus, and the defects that showed up were fixed, mainly in text escapes, text-to-boolean conversion, integer widths at the store, enum order and list windows. Four of the 1.15 known issues are gone. A few changes are breaking; read that section before you upgrade.

> **Experimental through version 1.** The language changes constantly, and breaking changes ship in minor releases. Faber 1.16 carries no stability promise, and neither does any other 1.x release. A 2.0 release is planned for when the language is largely stable.

### Language

**Stored stepped ranges.** A range with a step can now be stored. The step is part of the type, `range<int, 2>`. `length()` counts only the members on the step, and `contains(v)` is true only for a value on the step. Operations that cannot keep a step (`clamp`, `coercere`, `inter`, `union`) refuse a stepped range by name.

**Record literals without a declared type.** `let _ p ← { x = 1.5, y = 2 }` now runs, and so does `record<*> { … }`. A record prints without a type name, as `{ x = 1.5, y = 2 }`. A destructuring `rest` binding of a typed record is a record of the remaining fields.

**Sinks and `⇜`.** `Sink<T>` is the one contract for "take one item": a class opts in with `implements Sink<T>` and supplies `sink(T)` and `flush()`. `s ⇜ x` is the operator form of `s.sink(x)`. The method reports a failed write; the operator stops the program. The item must be exactly the sink's `T`, with no implicit conversion. Lists and sets are sinks: `⇜` appends to a list (duplicates kept) and adds a missing item to a set. On a bounded `list<T, N>` that is full, `.sink(v)` reports.

**Matrix elements.** A matrix reads and writes one element by row and column, with literal or computed coordinates: `m[[row, col]]` and `m[[row, col]] ← v`. `m.at([r, c])` reports an out-of-range coordinate, `m.get([r, c])` gives `none`, and `m.set([r, c], v)` stores. A coordinate that is provably out of range is refused at compile time. Bracket ranges on a vector or a matrix slice to a vector or a matrix, and `↦` converts between tensors, vectors and matrices.

```fab
main {
    let range<int, 2> evens ← 0…10 step 2
    print evens.length(), evens.contains(4), evens.contains(3)

    let _ point ← { x = 1.5, y = 2 }
    print point.y
    print point

    mut list<string> log ← []
    log ⇜ "start"
    log ⇜ "start"
    print log

    mut matrix<f32, [2, 2]> m ← [[1.0, 2.0], [3.0, 4.0]] ↦ matrix<f32, [2, 2]>
    let int row ← 1
    m[[row, 0]] ← 7.5
    print m[[0, 1]], m[[row, 0]]
    print m.transpose()
}
```

```text
6 true false
2
{ x = 1.5, y = 2 }
["start", "start"]
2.0 7.5
[[1.0, 7.5], [2.0, 4.0]]
```

**Text in bounded cells.** `+` and the ordering operators on `ascii<N>` values are text operations: `+` joins and `≺` compares as text.

**Target-native import values.** A value from a target-native import (`import python "re" re`) flows into a scalar cell such as `f64` directly. Storing it into a list, map or other structural cell needs an explicit `↦` (`SEM010 import_conversion_required` otherwise).

**The error carrier has a name.** The value that travels on a `⇥ T` channel is the compiler-owned carrier `error<T>` (Latin `erratum<T>`), with one field, `payload`. `catch` still binds the payload `T`. Nothing changes in programs that do not name the carrier.

**New checks.** Writing through a field of a record value is refused (`SEM020 assignment_to_fixum_field`); records are values. Importing a Norma module that does not exist is `PKG001 unknown_library_module` on every target, before any code is emitted. A local named `true`, `false`, `null` or another value word is allowed and warns (`WARN021`). New reject exemplars pin the diagnostics for format templates, string templates, map and list misuse, decimal literals, copy-into targets and type-alias cycles.

### Code generation

Every target was re-run over the whole corpus after the 2026-10-23 integration. The fixes below make the generated programs agree with `faber run`:

- **Text escapes.** An escaped quote or backslash in a string literal prints correctly in Go, LLVM and Swift.
- **Text to boolean.** `"true" ↦ bool` and `"false" ↦ bool` parse the code locale's words on every target; any other text fails and takes the `⊥` value. Go, TypeScript, Swift, LLVM and Racket used to test truthiness or non-emptiness instead. LLVM stops the program at a failed conversion with the same message as the runner.
- **Widths at the store.** A sum or product over a list of narrow or `wrapping`/`saturating` integers is computed exactly and fitted once, where it is stored, in LLVM, Rust, Go and Swift. A narrowing store into a tensor element checks every element in TypeScript and Racket. Integer tensor sums, matrix products and inner products in Rust and LLVM are exact and trap at the cell store.
- **Enums.** `for from Color let c` walks the members in declaration order in Go, Swift, TypeScript and Python, and ordering compares by declared position.
- **List windows.** `xs[lo‥hi]`, with or without a step, now emits for Go, TypeScript, Swift and Python. `take` and `slice` report a window that runs past the end in TypeScript and Python, as they already did on the runner and in Rust.
- **Defaults across modules.** A call that leaves out an optional or defaulted parameter of an imported function fills in the default the module declared, from any caller.
- **LLVM and WebAssembly.** LLVM aborts at a failed index or conversion with the runner's message, refuses a type-invalid pointer conversion before emission, and reads a strict map index with the strict lookup. WebAssembly reads a strict map index with the strict row.
- **C preview.** The C target gains raw bits (`b8` … `b64`) at their own width, `list<bN>` and its conversion to and from text, failable functions with `throw` and propagation, and `do { } catch`. It is still a preview that refuses what it does not cover, by name.

### Tooling

**`faber check --lower`.** Also lowers the program to Faber's reference form without running it, and reports the errors that semantic analysis alone cannot see (a program that checks but cannot run).

**Diagnostics carry their issue.** `faber mir` and the `faber corpus` emit lanes print `code:issue` for front-end errors, so a refusal names its reason.

### GPU

**Batched run-time matmul on Metal.** A dense matmul with a batch axis and extents known only at run time is admitted and runs on Metal, with a batch-major output and no aliasing between batches.

**CUDA.** The CUDA image builds matmul with run-time extents, and lane-form kernels now lower to the CUDA image instead of being refused. Lane-form kernels on NVIDIA hardware are not verified in this release.

**Device memory budget.** The device memory budget is derived from what the selected device reports, instead of a fixed 8 GiB.

No GPU throughput claim is made here.

### Breaking changes

1. **Record fields are read-only.** `r.x ← v` on a record value is now `SEM020 assignment_to_fixum_field`. Build a new record, or use a class with a `mut` field.
2. **Unknown Norma modules.** An import of a Norma module that does not exist used to pass the checker; it is now `PKG001 unknown_library_module`.
3. **Text to boolean on targets.** Generated Go, TypeScript, Swift, LLVM and Racket programs now parse `"true"`/`"false"` instead of testing truthiness, so `"yes" ↦ bool` fails there as it always did on the runner.
4. **List windows report on targets.** Generated TypeScript and Python no longer clamp a `take` or `slice` that runs past the end.
5. **Target-native values into structures.** Storing a target-native import value into a structural cell needs an explicit `↦`.

### How this release was gated

The full release gate passed on the release source: the test ladder, and every corpus target leg with no failing case. Cases a target cannot handle yet are pinned as expected failures, and each one was classified the way an audit is. A `residual` finding blocks nothing material and ships as a known issue. A `block_range` finding blocks a defined feature, or a feature on some targets; it ships, and the range is listed below as unsupported. Only a `block_release` finding (a regression or silent wrong output in core functionality on a major target, a crash in a common path, broken install or packaging, or a security issue) holds a release. This release has no `block_release` findings.

Corpus results per target (cases that pass in `corpus-suites/full`; the rest are pinned expected failures or not applicable): runner 774, Rust 750, Faber canonical 760, Faber round-trip 753, MIR 756, Go 646, TypeScript 710, LLVM 598, Racket 606, Python 575, Cranelift 570, WebAssembly 536, Swift 408.

### Known issues

#### Unsupported ranges (`block_range`)

- **Rust: optional class cursors.** A `ref` cursor over an optional class value (a linked list walked through `T ∪ none`) does not build on Rust or through the canonical Faber leg.
- **Rust: list windows of class elements.** A list window `xs[lo‥hi]` over class elements copies the elements on Rust instead of sharing them, so a write through the window does not reach the original list. Windows over value elements are not affected.
- **Rust: matrix element access.** `m[[r, c]]`, `m.at([r, c])`, `m.get([r, c])` and `m.set([r, c], v)` are not supported on Rust yet.
- **New 1.16 forms on other targets.** These run on the runner and are refused by name, not approximated, on the targets listed:
  - `⇜` sink-into: Go, TypeScript, Swift, WebAssembly, Racket, Python and Cranelift.
  - Matrix glyph operations and matrix element access: TypeScript, Swift, LLVM and several other targets.
  - `@ call` handlers that throw and catch: LLVM, Swift, WebAssembly, Racket, Python and Cranelift.
- **List windows on other targets.** LLVM, WebAssembly and Racket refuse a list window `xs[lo‥hi]` by name; Cranelift refuses a stepped one.
- **Record and class conversion.** `r ↦ Point` and `p ↦ record<…>` pass the checker when the fields match, but `faber run` refuses the conversion.

#### Residual

- **Integer extremes in formatting.** Formatting integers at the 64-bit extremes fails on LLVM, Swift, TypeScript and WebAssembly.
- **Norma's `Collector`.** `Sink<T>` declared in your own file works, but `faber run` refuses a program that imports `norma:sink` for its `Collector` sink (`PKG001`).
- **Libraries cannot be installed.** The graphics, autograd and UI libraries still have no install command, and `faber doctor` reports them not found.

### Not in this release

- A package manager and library install command.
- Lane-form CUDA kernels verified on NVIDIA hardware.
- The C and Cranelift targets remain previews that cover a subset of the language and refuse the rest by name.

---

[All releases](/releases/) · [Start](/start/)
