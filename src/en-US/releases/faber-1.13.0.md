+++
title = "Faber 1.13.0"
description = "Release notes and install details for Faber 1.13.0."
section = "releases"
order = 15
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Faber |
| **Version** | 1.13.0 |
| **Tag** | `faber-v1.13.0` |
| **GitHub** | [faber-v1.13.0](https://github.com/faberlang/releases/releases/tag/faber-v1.13.0) |
| **Published** | 2026-10-12 |
| **License** | MIT |

## Install this version {#install}

Pinned download for **Faber 1.13.0**. For the current release, use [Start](/start/) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [faber-v1.13.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.13.0/faber-v1.13.0-aarch64-apple-darwin.tar.gz) | 15.7 MB | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.13.0/faber-v1.13.0-aarch64-apple-darwin.tar.gz.sha256) |
| **Linux x64** | [faber-v1.13.0-x86_64-unknown-linux-gnu.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.13.0/faber-v1.13.0-x86_64-unknown-linux-gnu.tar.gz) | 17.6 MB | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.13.0/faber-v1.13.0-x86_64-unknown-linux-gnu.tar.gz.sha256) |

```bash
curl -fsSL -o faber.tgz \
  https://github.com/faberlang/releases/releases/download/faber-v1.13.0/faber-v1.13.0-aarch64-apple-darwin.tar.gz
tar -xzf faber.tgz
# The archive ships bin/ and share/; keep them together so the
# reader packs resolve beside the binary.
sudo mv bin/faber /usr/local/bin/faber
sudo mv share/faber /usr/local/share/faber
faber --version
```

## Release notes {#notes}

> **Status**: final — tagged `faber/v1.13.0` on 2026-10-12

Faber 1.13 turns the device route on: `faber run` can now execute `@ kernel`
functions on the CPU and on Metal, with loops, reductions, run-time shapes and
fault delivery, all in-process. Printed output finally follows the file's
locale — an English program prints `true` / `false` / `none`, a Latin one
`verum` / `falsum` / `nihil`, on every backend. The raw-bits surface is
settled (`b8` `b16` `b32` `b64`, bytes as `lista<b8>`), every type gains a
written zero (`Type {}`), `discerne` matches several subjects at once, and
reduction expressions lower across the main targets. The binary becomes
self-contained: the standard library and the explain reference are embedded,
and the separate host component is folded away. Several of these are breaking
changes; read that section before you upgrade.

This is a consolidation release: its purpose is to capture the large body of
language change that landed since 1.12 in one verifiable drop. It is good for
writing, checking, formatting and interpreting Faber. It is not yet good for
building real programs — compiled programs cannot yet touch the outside
world, there is no way to install a library beyond the built-in standard
library, and the standard library still has holes. Those limits are listed in
detail under Known issues; none of them gate this release.

### Language

**Output follows the file's locale.** The words a program prints — boolean
`true` / `false` (Latin `verum` / `falsum`), the null value `none` (`nihil`),
and the tuple head `tuple` (`iuncta`) — come from the locale pack of the file
that defines them, on every backend: the runner, Rust, Go, TypeScript, Swift,
Python, WebAssembly, LLVM and the S-expression target. A generic function
prints with the tokens of the unit that defines the template, not the caller.
Haskell keeps its native `True` / `False` / `Nothing`. Expected-output files
for corpus programs are written in the source's own locale. This closes the
1.12 defect where every locale printed the Latin words.

**Raw bits and bytes.** The bit-pattern markers `b8`, `b16`, `b32` and `b64`
are the raw-bits domain: a `bN` is exactly N bits, always. `∧ ∨ ⊻ ¬ ⇐ ⇒`
act at the type's width every time — a left shift drops bits off the top, a
right shift fills with zeros, a shift by N or more gives all zeros, `¬` flips
exactly N bits. A `bN` compares and orders by its unsigned bit pattern and
does no arithmetic. Conversions are explicit `↦`: same-width `bN` to `iN` is
two's complement, `bN` to `f16` / `bf16` / `f32` / `f64` reinterprets the bit
pattern (both ways), and a byte list and a wider-element list convert through
each other with `via Le` or `via Be` for little- or big-endian packing. The old escape hatches are gone: `via
Bits` no longer converts through a bits view, the words `byte` / `octeti` are
retired (`lista<b8>` is the byte list), and `≠` is retired in favour of `≢`
as the negation of `≡`. A bit-type value or a list window that a target has
no carrier for is refused by name at emit time, not approximated.

**The zero of a type is written `Type {}`.** `tensor<T, [shape]> {}`,
`vector<T, N> {}`, `matrix<T, [r, c]> {}` and the short sugar `tf32[2, 2] {}`
build the typed zero: every part takes its default, including a tensor of
vectors and size-parameter extents. The bare form (`← tf32[2, 2]`) is
retired, as is `Type []`; a call-form constructor is refused at parse time.
The inferred constructor `_ {}` builds the typed zero where the type comes
from context. `empty` (Latin `vacua`) is the default empty instance of the
declared type: at a dense tensor, vector or matrix slot it *is* the typed
zero. `empty` claims zero-or-more types only — a text, character, byte,
regex or tuple slot refuses it by name. The English reader spells the marker
`empty` now; the earlier English spelling `vacua` is gone.

**Multi-subject `discerne`.** `discerne a et b` matches several subjects at
once, with one pattern per arm over all subjects. The match is over closed
sets: every arm's pattern is checked for exhaustiveness against the subjects'
constructors, width and length-shape patterns are rejected, and a match over
a value-type subject is refused by name with a hint to switch forms. It
lowers on the MIR runner as a tag-probe chain and emits on Go and TypeScript
as a column-probe chain and on Swift as a tuple pattern per arm.

**Reduction expressions.** The `reducta` reduction family is in the language
and lowered on the runner, Rust, Go and TypeScript: plain reductions fold to
a flat walk, grouped reductions (with `pro`) and the argument-extrema forms
(`argmaxima` / `argminima`) lower, an optional reduction is a native option
value, and a reduction body with statements runs in a value closure. The
`itera` statement accepts a `filum` clause, so a loop can carry a thread
argument through its body. A failable read inside a kernel's lane body may
take an inline default.

**Conversion rounding is explicit.** A conversion from a float or a decimal
to an integer, `inf` or a policy-word cell now names its rounding:
`via Floor`, `via Ceil`, `via HalfEven` or `via Trunc` (half-even is the
default everywhere else). A bare float-to-integer conversion is rejected by
name; write the hint. Convert-assign accepts the hint too (`a ↤ x via Trunc
⊥ 0`), keeping the failable error path. The runner, the S-expression,
WebAssembly and the Rust, TypeScript, Go, Swift and Python emitters honour
the four modes.

**Checked tensor access.** The method forms `accipe` (get) and `ponde` (set)
are the failable tensor reads and writes: out-of-range fails through the
ordinary error channel, on the runner, on generated Rust, TypeScript and Go,
and on the device route inside kernels. The bracket forms stay plain `T` and
trap on a bad index, and a literal index provably out of bounds stays a
compile error. A checked store is failable unless its index is proven in
range.

**Aggregates: arithmetic, aliases and ownership.** Arithmetic over lists,
queues and stacks follows one rule set: `⊙` and `⊘` (and `÷`, `%` and unary
minus where they apply) operate element-wise over two aggregates, and the
bounded-list length defects are fixed. An alias of an unmarked list, map,
object, queue or contract parameter is read-only, exactly like the parameter
itself, and the bind-alias rule is flow-aware: an unconditional re-bind of
the source detaches its stale aliases. Conversely, `own` and `copy` parameters are
writable by the callee — field stores, element stores, reassignment and
mutating methods all work on them — and mutation of a read-only binding is
counted by a warning. A device launch whose written binding overlaps another
binding is refused up front (the noalias contract).

**Smaller settled rules.**

- The right-hand side of `est` is always a type; the null words split from
  the null type. A bare `nihil` value is a named parse error that names the
  locale's word (`null` in English, `nulla` in Latin); `nihil` survives only
  as the Latin null type and in `casu nihil` patterns.
- An optional stored into a plain cell — at an argument, return, field
  initializer, throw, yield, element or tuple store — is rejected by name;
  unwrap or convert first.
- Flow narrowing works through `and`, `or` and `not` conditions, and a
  diverging or-guard ends the path.
- The keyed list method `.sorted(key)` (Latin `.ordinata(key)`) is retired in
  favour of the sort expression; the standard library's `ordered_map` module
  is renamed `sorted_map` (the Latin word is unchanged).
- A text index `s[i]` yields the Unicode character everywhere, including
  generated Rust; the optional text read `get` / `accipe` returns the
  character or `none` past the end on Rust, Go, TypeScript and Swift.
- The mean of an empty tensor is NaN (sum over count) on every runtime; the
  grammar records the sentence.
- Trailing commas in array element lists are a parse error.
- JSON parsing reads integer tokens of any length into the unbounded integer
  type; JSON documents parse and serialize in pure Faber, including
  object-rooted documents.
- `cumulate` folds into a fresh accumulator (the caller's value is no longer
  overwritten); `int ↦ f32` rounds once on Python; a map holding an enum or
  variant value prints like the runner on the S-expression target; list and
  map values convert to and from the dynamic `valor` element-wise on Rust,
  and the LLVM conversion no longer fails.

### Tooling

**A self-contained binary.** The standard library (Norma) is embedded in the
`faber` binary the way the runtime sources already were, and the explain
reference is embedded too. The library home no longer probes a build
checkout: an installed `faber` resolves the standard library with no
environment variables set, and the release smoke proves it. The native host
surface — file, network, HTTP, console — lives in this repository now; the
release manifest pins this repository alone, with no separate host component.

**`faber corpus`.** A new product command verifies target code end to end.
It runs a named suite of exemplar cases through one target per invocation
(`--target rust`, `--target runner`, …), where each case pins its expected
outcome — pass, expected-fail, or not applicable — in a checked-in
expectation file. The command validates what each target can judge, bounds
every child process, and never hides a pass behind a skipped phase; a failing
case is either a regression or a stale expectation. Suites cover the exempla
corpus, the product packages and the GPU rungs.

**`faber format`.** Formatting policy is configurable: a `[format]` section
in the package manifest sets the policy (and the CLI value wins over the
manifest, which wins over the built-in default `normalise-v1`; the
`pretty-v1` style is admitted with a rebaselined corpus). The steady-state
flags are `--write` (in place), `--stdin` / `--stdout` (one document through
the pipe; `--stdout` takes exactly one input file), and `--policy <slug>`
(unknown slugs fail clearly). `--canonical` is gone — `--locale` is the only
re-emit selector — and asking for both a policy and a locale re-emission is
rejected explicitly rather than silently switching modes.

**Installer lifecycle.** The bootstrap installer is verified end to end.
`faber self update` fetches the installer base, `faber self repair` runs a
typed repair policy, `faber self uninstall` removes only what the product
owns, and a downgrade to an incompatible pack fails closed instead of
mixing. Reinstall is idempotent. An HTTPS-to-HTTP redirect on installer or
HTTP fetch is refused.

**Locale flags.** `--locale` (formerly `--reader-locale`) selects the source
locale, and the new `--diagnostics-locale` selects the language of
diagnostics independently of it. Diagnostics carry the locale id and issue
name, and parse errors print the locale pack's own keyword spelling.

**Generated code.** Generated output prints the display tokens of the module
it was compiled from, so English source prints `true` / `false` / `none` on
every target. Every failable function in generated Swift is a `throws`
function (the result-wrapper path is gone), so regenerate Swift output. Go
carries a genus as a pointer with a zero value and `&T{}` constructors,
removing the interface-pointer workarounds. Unreachable markers and expect
calls are gone from the TypeScript, Go, Swift, Python and WebAssembly
emitters. A new default-off novelty target joins the experimental set: Odin
(`faber emit -t odin`), a fail-closed scalar-and-print subset behind the
`hir-odin` feature, listed by `faber targets` as unavailable on a default
build.

### GPU

`faber run --device …` executes device code for real.

- `--device cpu` runs `@ kernel` functions on the MIR runner in host form —
  device programs are testable without a GPU.
- `--device metal` runs them on Metal through an in-process device session;
  the child-process route is retired. The device route serves `--stats`,
  program arguments and every input kind, and its output matches the CPU
  route.
- `--device auto` prepares the package once and reuses the lowered unit.
- `faber test --device cpu` runs a package's kernel rows in host form; the
  `auto`, `metal` and `cuda` selections refuse with a clear exit for now.
  Run and test share one device-selection precedence.

Kernel launches support lane-form bodies with loops, `break`, `continue` and
early return; run-time extents flow through the dispatcher, so a kernel can
take N-dimensional tensor indices and shapes decided at launch; a genus
parameter rides along as a packed parameter block read on the GPU; and
vector-element tensors (width 2 and 4) upload and read back. Whole-grid
reductions run on the device, and matmul accepts run-time dimensions on
Metal, verified against the CPU oracle across the tiled, one-row, gemv and
simdgroup shapes. Every buffer binding is 16-byte aligned and refused before
encoding if it is not.

Faults are part of the contract: a kernel declaring an error channel can
throw a constant text, an unproven index guards with an unsigned compare and
a lowest-lane-wins fault word, and the fault is delivered to the enclosing
`fac omnia` or plain `fac` on the real Metal route. `fac omnia … dum` is
legal grammar, and a host read after a faulting launch delivers the fault
before the read completes.

### Breaking changes

1. **`≠` is retired.** Write `≢` for the negation of `≡`; `≠` draws the
   named parse error that names its replacement.
2. **`via Bits` is retired.** Convert through the bit markers: `x ↦ b32`,
   `u16 ↦ b16 ↦ f16`, and the `bN` conversion table above.
3. **`byte` / `octeti` are retired.** Bytes are `lista<b8>`; the byte literal
   and byte insertion produce a `lista<b8>` everywhere.
4. **A bare float-to-integer conversion is rejected.** Name the rounding:
   `via Floor`, `via Ceil`, `via HalfEven` or `via Trunc` (the error names
   them).
5. **The typed zero is `Type {}`.** Rewrite the bare form `← tf32[2, 2]` as
   `tf32[2, 2] {}`; `Type []` and call-form constructors are refused.
6. **A bare `nihil` value is retired.** Write `null` (Latin `nulla`); the
   parse error names the locale's word.
7. **English `vacua` is retired.** The English empty-instance marker is
   `empty`; Latin keeps `vacua`.
8. **`.sorted(key)` is retired** in favour of the sort expression, and the
   `ordered_map` module is renamed `sorted_map`.
9. **CLI renames.** `--reader-locale` is `--locale`; diagnostics move to the
   new `--diagnostics-locale`; `faber format --canonical` is gone (`--locale`
   is the only re-emit selector).
10. **The file-copy verbs in the native host surface are renamed**: `copy` /
    `copy_async` are `exscribe` / `exscribet`.
11. **Regenerate generated code.** Swift output from 1.12 does not match the
    new `throws` emission, and Go genus output changed shape. Older output
    and this release's runtimes do not mix.
12. **Trailing commas in array element lists are a parse error.**

### Known issues

The three limits below shape what 1.13 is for. It is for people who want to
read, write and check the language as it now stands, and run scripts through
the interpreter. Anyone who wants to ship a compiled program that reads a
file, or use the graphics, autograd or UI libraries, should wait for the
releases that close those limits.

- **A built program cannot touch the outside world.** `faber build --target
  rust` works for pure code — math, text, print. The moment a program uses
  the file-system, console, process or random modules, the build stops with
  `PKG001 package_host_selection_required`, and `host = "native"` answers
  `host_provider_unsupported`: the native host provider was retired on
  purpose and its replacement has not landed. Interpreted runs keep script
  I/O — `faber run` covers file read and write, console, the current
  directory, environment variables and random.
- **There is no way to add a library.** The graphics, autograd and UI
  libraries cannot be installed; `faber doctor` reports all three
  not-found. Only the built-in standard library ships with the binary, and
  the package manager is not released yet, so there is no install command.
- **The standard library has holes.** `time.now()` fails under `faber run`;
  there is no working HTTP route and no WebSocket surface; and roughly
  seventy standard-library lines are marked deferred — functions that exist
  by name and fail when called, with text, encoding, toml and net among
  them.
- **Some shipped exemplars are stale.** One imports `norma:solum`, a module
  name that no longer exists; three exemplar packages fail `faber check`,
  and that failure reports a line far beyond the end of the file, so the
  diagnostic points at the wrong place.

Beyond those limits:
- **The largest device acceptance case cannot meet its bound as written.**
  The full-grid flood simulation (roughly 1,227 by 1,132 cells) completes on
  Metal, but its f32 depth field differs from the reference by more than the
  0.01 m bound allows — the bound presumes arithmetic bit-identical to the
  donor program, and a one-ulp change of one input cell moves the field by
  metres between runs. The reduced-grid oracle passes on Metal within the
  bound.
- **A throwing kernel can throw only a constant text**, and kernel-to-kernel
  inlining of a throwing kernel is not implemented.
- **Regex engine gaps by target** (carried from 1.12): Go has no Unicode
  `\b`; TypeScript clears repeated-group captures per iteration; Swift and
  Python differ from the dialect on named constructs; the backtracking
  engines (TypeScript, Python, Swift) can take exponential time on hostile
  patterns; Racket and Haskell name every regex construct unsupported.
- **Range containment `∈ a‥b` still has no MIR lowering**; it emits on the
  HIR targets only.
- **Rust corpus builds.** One corpus program still fails to build on Rust (it
  stores an awaited promise at a `←` binding); it is recorded as an expected
  failure. The half-width float cells (f16, bf16 and their policy words)
  build again on Rust; bare `f16` / `bf16` ride an f32 carrier.
- **Print and templates** (carried): the comma form `print a, b` still lays
  out differently on the MIR text targets than elsewhere; LLVM still lacks
  template rows for some sized integers and composites; Haskell still rejects
  string templates. Prefer a template, `print "§ §"(a, b)`.
- **`faber convert` still does not resolve imports**; a file importing a
  library type fails with the resolution error.
- **Checker residuals** (carried): narrowing an inferred error result with
  `is` and `✓ ✗` is still accepted by the checker and rejected only at MIR
  validation; WebAssembly still types one conversion local as `f64`; the Go,
  Python and Swift generic-enum and generic-map gaps remain.
- **Device-row test debt.** A sizable slice of the kernel proba rows for the
  autograd library fails under `faber test --device cpu` on empty-initialised
  tensors — a library-side initialization issue, not a launch refusal.
- **Experimental targets differ from `faber run` where their arithmetic does** (carried): COBOL checks only stored values, Pascal traps per
  operation, BASIC floats are the C64's. Each target rejects the cases it
  cannot match by name.
- **Sibling-library gates.** No gate in this repository runs the autograd or
  UI libraries' suites; the optional graphics provider package checks and the
  environment-gated device checks remain skipped (carried from 1.10).

### Not in this release

- Character ranges as set bounds (`x ∈ '0'…'9'`) are still not supported;
  interval bounds are numbers, and text membership stays `.contains`.
- The slash regex literal and per-group spans are not shipped; read group
  spans with `start()` and `group(n)`.
- The collection-ergonomics rewrite, set-algebra glyphs and superscript
  powers remain planned.
- Removal of the comma `print` form is still decided in direction only.
- `externa` typing and conditional-compilation enforcement stay held; there
  is no LSP.
- Translated reader packs keep their own spelling for the null type until
  the word is chosen.
- Public publication of the Go runtime module and `@faber/runtime` waits for
  the Faber 2 migration; they are consumed by path here.
- The CUDA backend exists behind hardware-gated checks; no CUDA route is
  enabled for `faber run`.
- The Lean leaf is not a discoverable target or package backend.
- Radix stays at 0.84.0 (no separate Radix release); Cista is unchanged and
  not part of this release.

---

[All releases](/releases/) · [Start](/start/)
