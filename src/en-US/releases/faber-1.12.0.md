+++
title = "Faber 1.12.0"
section = "releases"
order = 13
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Faber |
| **Version** | 1.12.0 |
| **Tag** | `faber-v1.12.0` |
| **GitHub** | [faber-v1.12.0](https://github.com/faberlang/releases/releases/tag/faber-v1.12.0) |
| **Published** | 2026-10-02 |
| **License** | MIT |

## Install this version {#install}

Pinned download for **Faber 1.12.0**. For the current release, use [Start](/start/) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [faber-v1.12.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.12.0/faber-v1.12.0-aarch64-apple-darwin.tar.gz) | 12.8 MB | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.12.0/faber-v1.12.0-aarch64-apple-darwin.tar.gz.sha256) |
| **Linux x64** | [faber-v1.12.0-x86_64-unknown-linux-gnu.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.12.0/faber-v1.12.0-x86_64-unknown-linux-gnu.tar.gz) | 14.4 MB | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.12.0/faber-v1.12.0-x86_64-unknown-linux-gnu.tar.gz.sha256) |

```bash
curl -fsSL -o faber.tgz \
  https://github.com/faberlang/releases/releases/download/faber-v1.12.0/faber-v1.12.0-aarch64-apple-darwin.tar.gz
tar -xzf faber.tgz
# The archive ships bin/ and share/; keep them together so the
# reader packs resolve beside the binary.
sudo mv bin/faber /usr/local/bin/faber
sudo mv share/faber /usr/local/share/faber
faber --version
```

## Release notes {#notes}

> **Status**: draft (release candidate; final at the operator's release commit)

Faber 1.12 adds text processing and a cleaner set of operators to the language,
and it changes what generated code looks like. Since 1.11.0 (1 October 2026)
the language gained regular-expression operations (`find`, `find_all`, `split`,
`replace`, `escape`) on a regex that is checked when it is built, the
membership glyphs `∈` and `∉`, and a set of settled numeric and loop rules:
width limits apply only at the store for `wrapping<W>` too, a range `step` is a
positive stride, and a tensor bracket read is a plain `T`. Four experimental
code-generation targets (BASIC, Pascal, COBOL, Fortran) ship, default-off.
Generated Rust, Go and TypeScript now import a named runtime package instead of
carrying helper code in every file. Several of these are breaking changes; read
"Breaking changes" before you upgrade a package or regenerate code.

### Language

**Regex operations.** A regex built with `↦ regex` now supports the operations a
text-processing program needs. The dialect is RE2: leftmost-first matching,
linear-time where the target's engine allows it, no lookaround, no
backreferences. A pattern that uses a rejected construct fails the conversion
with a diagnostic that names the construct.

- `r.matches(text)` is the existing boolean test.
- `r.find(text)` returns `match ∪ none`: the leftmost match, or `none`.
- `r.find_all(text)` returns every non-overlapping match as a list.
- `r.split(text)` returns the pieces between matches. Capture groups are not
  spliced into the result, and leading and trailing empty pieces are kept.
- `r.replace(text, with)` replaces every match. `with` is either a text, taken
  literally (`$1`, `${name}` and `\1` are plain text), or a closure from the
  match to a text: `r.replace(text, _ m ∴ m.text().uppercase())`.
- `text.escape()` returns a pattern text that matches the text literally.
- A match is read with `text()`, `start()`, `end()`, `group(n)` and `named(name)`.
  Offsets are code points, half-open, never bytes. `group(0)` is the whole
  match; a group that did not take part, an index past the last group, and an
  unknown name are all `none`. The match has no source-level type name: hold it
  in an inferred binding (`const _ m ← …`) or take it as an inferred closure
  parameter.
- Latin spellings are `consentit`, `inventa`, `collecta`, `divide`, `muta`,
  `inventum`, `principium`, `terminus`, `coetus`, `nominatus` and `munita`.

`↦ regex` is failable: it fails when the pattern does not compile, through the
ordinary `⇥ textus` channel, and the 1.11 handling rules apply (a `⊥` default,
an enclosing `fac { } cape`, `capta { }`, or a function declaring `⇥ E`; `main`
is exempt). The old 1024-byte literal-pattern cap is gone.

Each target uses its own native regex engine; Faber does not ship a matcher.
Where an engine cannot express a construct, the target reports it by name rather
than approximating. Support: the MIR runner, Rust (`faber::regex`), Go
(`regexp`), TypeScript (`RegExp`, through `@faber/runtime/regex`), Swift
(`Regex`), Python (`re`), LLVM and WebAssembly (through host rows) run every
operation. The Racket (`sexp`) target names the whole family unsupported
(`regex_engine_diverges`), and the Haskell target fails every regex construct
(`regex_engine_unavailable`). The named gaps are listed under "Known issues".

**Membership glyphs.** `x ∈ xs` tests membership and `x ∉ xs` negates it. The
right operand is a list, a set, a map (the test is on the keys), an enum value
set (`c ∈ [Color.rubrum, Color.viridis]`), or a range (`age ∈ 18‥65`). The
keyword forms `between` and `within` (Latin `inter` and `intra`) are retired:
they now draw `PARSE001 membership_keyword_retired`, which names the glyph to
write. Membership never applies to text: `"a" ∈ "abc"` is
`SEM010 membership_over_text`, and a substring test is `haystack.contains(needle)`.
A scalar, nullable or unresolved right operand is also rejected by name.

**Numbers: width limits apply only at the store, wrapping included.**
`wrapping<W>` now follows the rule `trapping` and `saturating` already followed.
An expression over wrapping operands is computed exactly and reduced only where
the value is stored into a cell. With `wrapping<u8>` values 200 and 100,
`(a + b) / 2` is 150 and `print a + b` prints 300; the sum wraps to 44 only if
it is stored into a `wrapping<u8>` cell. Chains of `+`, `-`, `*`, shifts, bit
operators and unary minus that feed a wrapping store may still be reduced step
by step, because that cannot be observed. The MIR runner and the Python target
follow the rule; see Known issues for TypeScript.

**Literals beside policy cells.** An untyped constant adopts the cell type
under `≡` and `≠` next to a `saturating` or `wrapping` integer cell and next to a
`saturating` or `trapping` float cell, as it already did next to a bare width:
`saturating<u8> ≡ 250` now checks. A typed operand of another type still needs
`↦`, and the diagnostic text now names `≅` and `↦`.

**Integer to `f32` rounds once.** `int ↦ f32` on the MIR runner rounds directly
from the integer instead of through `f64`.

**Ranges.** A range `step` is a positive stride and the direction comes only
from the bounds: `10‥0 step 2` yields 10 8 6 4 2 and `0‥10 step 2` yields
0 2 4 6 8 (Latin `per`). A literal zero or negative step is the new compile
error `SEM011 range_step_not_positive`; a computed one traps at run time. A `var`
range binder is a fresh copy at the top of each iteration, so writing to it no
longer steers the loop. Rust, Go, TypeScript and Swift emission follow the same
rules.

**`copy`.** `copy` marks how a binding is initialized: `var copy Point b ← a`
duplicates `a` at the declaration, and a later `b ← c` of a class value assigns
by reference like any class assignment. After a `copy` parameter makes its
duplicate, the callee mutates it only as far as the ordinary `const` / `var`
declaration allows, and a field write and a mutating method call follow one
rule: a method that changes its receiver in place (directly, through a sibling
method, or through an in-place verb on a field), called on a `const` binding or
on a parameter that is not `mut`, is `SEM020`
(`imperativus_operator_method_requires_varia_receiver`), exactly as a field write
would be. A `copy` tensor binding or parameter keeps element writes and
arithmetic, and a rank-2 `copy` tensor reads by `t[[r, c]]`.

**`mut` parameters.** A `mut` scalar parameter requires an argument of exactly
its type: passing a `u8` variable to a `mut int` parameter is
`SEM010 mut_argument_type_mismatch` (a store through the parameter lands in the
caller's cell, so a narrower cell could otherwise hold a value it cannot).
Assigning from one `mut` scalar parameter to another copies the value and
creates no borrow, so swapping two `mut int` parameters through a held `const`
no longer trips `SEM052`; real aliasing such as `swap(x, x)` still does.

**Tensors and vectors.** A tensor bracket read `t[i]` (and `t[[r, c]]`) is `T`
and traps on a bad index, like a list index; a literal index provably out of
bounds stays a compile error. The `get` / `accipe` method form is the nullable
read. A `vector<T, N>` indexed with a constant lane is a lane read, write and
`v![k]` form (a constant outside the width is a compile error), and a run-time
index is a checked lane select that fails like an out-of-range list index.

**Fixes to existing forms.**

- `match` alternatives (`case A or B`) now lower and run on the MIR runner; they
  passed `faber check` and then failed with an unsupported-lowering error.
- A repeated numeric or text switch case value is `SEM042 duplicate_literal`
  naming the value, instead of an invalid-MIR failure at run time.
- `assert cond "msg"` on one line is `PARSE001 adfirma_message_particle` (the
  message was silently dropped); write `assert cond panic "msg"`. A string on
  the next line is still its own statement.
- A payload-free `enum` no longer draws `WARN025` (`union_no_common_members`);
  an enum is not a written union.
- `reduce` (Latin `reducta`) folds into a fresh accumulator, so the caller's
  initial value is no longer overwritten by the result.
- An enum variant stored into a `T ∪ none` slot or an optional class field, and
  a payload variant of a generic union (`Opt<int>`), now check, lower and run
  on the runner.
- A declared enum annotation no longer draws the union guardrail warning.
- The MIR runner grows its native stack per call and stops a runaway recursion
  at a depth of 10,000 calls with the named failure `runner_call_depth_exceeded`
  instead of aborting the process. The runner gained the `stacker` dependency
  for this.
- `faber hir` lexes under the file's frontmatter locale and resolves imports like
  `faber check`; an English-locale file or a file importing a library type no
  longer fails under `hir`.
- Swift emits postfix `!` for the explicit non-null assertion.
- The six long-retired words `positivum`, `negativum`, `nonnihil`, `nonnulla`,
  `prae` and `sic` are no longer reserved: they are ordinary identifiers. A use
  of `sic` as the old conditional is still recognized and draws
  `conditional_sic_removed`; that migration diagnostic and the retired-membership
  one are scheduled for deletion at the Faber 2 cut.

### Experimental targets

Four new code-generation targets ship as default-off Cargo features outside the
default build. Each emits a fail-closed subset: a Faber feature is supported only
where it maps directly onto a native construct of the target; anything that
would need emulation or a runtime library is rejected by name
(`unsupported on target <name>: <construct>`), and an emitted program prints what
`faber run` prints.

| Target | Source | Output | Tool that runs it |
| --- | --- | --- | --- |
| `basic` | MIR | line-numbered BASIC listing (C64 BASIC V2 compatible) | `cbmbasic` |
| `pascal` (alias `pas`) | HIR | Free Pascal program | `fpc` |
| `cobol` (alias `cob`) | HIR | GnuCOBOL 3.2 free-format source | `cobc` |
| `fortran` (alias `f90`) | HIR | Fortran 2008 free-form source | `gfortran` |

On a default build `faber targets` lists all four with `available=no`, and
`faber emit -t <name>` fails with `target_unavailable` naming the feature to
enable (`mir-basic`, `hir-pascal`, `hir-cobol`, `hir-fortran`). Emitting needs no
external tool; the tools above are only for running or checking the emitted
program. The four targets are `emit` only (no `run` or `package`), and they are
outside the ordinary `scripta/e2e` fleet. Each supports a small subset: integers
and floats of the widths it can represent exactly, control flow, text, enums,
simple records, and rank-1 and rank-2 tensors, with `copy` bindings of records
and tensors on the targets that can copy. None supports collections, closures,
the error channel, async, or the numeric policy words beyond what its README
lists.

### Targets

**Runtime packages (breaking for generated code).** Generated Rust, Go and
TypeScript no longer carry per-file helper code (exact-integer arithmetic,
decimals, `inf`, the `¶` formatter, display helpers, generators, tensor and
vector carriers). They import a runtime package, spelled by one rule per target
from one table:

- **Rust**: the `faber` crate's namespaces `faber::exact`, `faber::inf`,
  `faber::dec`, `faber::format`, `faber::display`, `faber::r#gen`, `faber::float`,
  plus `faber::regex` and `faber::Match`. `faber::exact::store` takes two
  arguments, the three transitional display root aliases are removed, and
  `faber::Regex::new` returns a `Result`. The async cursor carriers and
  `block_on` live in the crate; an optional, non-default `tokio` feature adds
  a tokio `block_on`. The `regex` feature is on by default.
- **Go**: one flat `rt` package (import path `faber/rt`), spelled
  `rt.<Namespace><Name>`: for example `rt.ExactStore`, `rt.InfI`, `rt.DecAdd`,
  `rt.FormatInt`, `rt.TensorTensor`, `rt.VectorVector`, `rt.RegexRegex` and
  `rt.SermoConversation`.
  `rt.Verum`, `rt.ListDisplay` and `rt.ValorDisplay` are removed
  (`rt.DisplayVerum`, `rt.DisplayList`, `rt.DisplayValor`).
- **TypeScript**: `import { display, exact, dec, inf, format } from
  "@faber/runtime"` (only the namespaces a file uses), and
  `import * as regex from "@faber/runtime/regex"`. A TypeScript file that uses no
  runtime namespace has no import and is emitted as a script; a script that
  declares top-level names gets an `export {};` marker so its names stay out of
  the global scope.

Regenerate any generated code you keep; output from 1.11 and earlier does not
compile against the new runtimes, and the new output does not compile without
them. Generated Rust that uses exact integers, decimals, `inf`, display or the
formatter needs the `faber` crate as a dependency (it can no longer be built
with bare `rustc` as a single file).

**Readability.** Generated code reads closer to hand-written code.

- Rust: a function-tail `match` writes expression arms, a sole-`print` arm and a
  bound-cursor loop body drop their redundant block, a `fac` / `cape` body drops
  its dead one-shot loop and `let ok` rebinding, and compiler temporaries follow
  one naming scheme.
- Go: a statement `if` drops an `else` after a terminating arm, a `discerne` arm
  body writes no redundant block, an empty class is `struct{}`, an enum type
  switch drops `any()`, the `fac` wrapper drops its dead one-shot loop, and
  temporaries follow one naming scheme. The Go runtime is flat, as above.
- TypeScript: no dead trailing return after an exiting body, and temporaries
  follow one naming scheme.

**Other target changes.**

- LLVM and WebAssembly hosts spell the regex operations through versioned rows:
  `__faber_rt_v1_regex_*` for the regex value, `__faber_rt_v1_text_escape` for
  `text.escape()` and `__faber_rt_v1_match_*` for the match accessors. The ABI
  spelling is `__faber_rt_v1_<family>_<op>`, named for the receiver family.
- A vector lane read runs on the runner, Rust, LLVM, Racket and TypeScript;
  WebAssembly refuses it by name (no vector carrier), and Go and Swift carry
  named gaps.
- Swift map-key and literal-key membership emit the native test, and Python
  follows the store-only wrapping rule.

### Tooling

- `faber explain --json` carries each exemplum's grammar production ids, and
  `faber explain --list --json` emits the index as records.
- `faber check`, `check-library` and the package build now share one manifest
  target resolver. An unreadable or unsupported `build.target` fails closed
  instead of falling back silently, so a `build.kind = "lib"` package no longer
  checks clean and then fails to build.
- The package builder's path-override probe now requires the Faber runtime
  checkout, so a release runner with only the hosts checkout resolves the tag pin
  instead of a dead path.
- `faber format`, `convert` and the codemods stay report-only by default
  (`--write` applies), as in 1.11.

### GPU

This release makes no GPU product claim. No Faber program drives the GPU through
`faber run`, and the GPU campaign remains paused. The language-level work from
1.11 is unchanged; the vector lane read above is a language and runner feature.

### Breaking changes

1. **`↦ regex` is failable.** A `textus ↦ regex` (or `ascii ↦ regex`) outside
   `main` needs a handler: give it a `⊥` default, wrap it in `fac { } cape` or
   `capta { }`, or declare `⇥ textus` on the function. In Rust,
   `faber::Regex::new` returns `Result<Regex, RegexError>`; there is no
   infallible alias.
2. **`between` / `within` (Latin `inter` / `intra`) are retired.** Write `x ∈ xs`,
   `x ∈ a‥b`, and `x ∉ …` for the negation. Membership over text is rejected;
   use `.contains(…)`.
3. **`wrapping<W>` reduces only at the store.** An unstored expression over
   wrapping operands (a division, remainder, comparison, `print`, or `↦`) is
   now computed exactly instead of wrapping first. To keep the wrapped value,
   store the expression into a `wrapping<W>` cell and use the cell.
4. **Range `step` is a positive stride.** Rewrite `step -1` to `step 1` on a
   descending range (`10‥0 step 1`); a zero or negative step is
   `SEM011 range_step_not_positive`. A `var` range binder is a per-iteration copy
   and no longer steers the loop.
5. **A tensor bracket read is `T`.** `t[i] coalesce 0.0` and `t[i] vel 0.0` no
   longer have a nullable operand: write `t[i]` for a trapping read, or
   `t.get([i]) coalesce 0.0` (Latin `accipe`) for a nullable one.
6. **A mutating method call needs a `var` receiver.** Calling a user method that
   changes `self` on a `const` binding or on a parameter that is not `mut`
   (copy parameters included) is `SEM020`; bind the value to a `var` local first.
7. **A `mut` scalar parameter needs an argument of exactly its type**
   (`SEM010 mut_argument_type_mismatch`): convert the argument with `↦` first.
8. **A repeated switch case value is a check error** (`SEM042`); previously it
   failed at run time.
9. **`assert cond "msg"` on one line is a parse error**; write
   `assert cond panic "msg"`.
10. **Regenerate generated code.** Rust, Go and TypeScript output now imports the
    runtime packages (see Targets); older output and older runtimes do not
    match. Hand-written code that called the removed Rust and Go spellings
    (`faber::exact::store` with three arguments, the display root aliases,
    `rt.Verum`, `rt.ListDisplay`, `rt.ValorDisplay`) must use the namespaced names.
11. **LLVM and WebAssembly host authors**: the regex and match rows are
    `__faber_rt_v1_regex_*`, `__faber_rt_v1_text_escape` and
    `__faber_rt_v1_match_*`; the host-side display helpers moved to
    `faber::display::*`.

### Known issues

- **TypeScript and `wrapping<W>`.** The TypeScript emitter still reduces a
  `wrapping<W>` expression per operation, so an unstored expression differs from
  the runner. The `wrapping<u64>` corpus program fails `tsc` (a `bigint` compared
  with a `number`).
- **Regex gaps by target.** Each is the target's own engine, recorded rather
  than emulated:
  - Go has no Unicode `\b`: a pattern with `\b` or `\B` fails the conversion on
    Go with `unicode_word_boundary`.
  - TypeScript clears a repeated group's captures at every iteration, so
    `((a)|b)*` over `ab` reads group 2 as `none`; no diagnostic is issued.
  - Swift differs from the dialect on `(?m)` with CR and U+2028 line ends, on
    `\b` next to combining marks and digits, and on `(?i)` folding of a few
    letters (`σ` / `ς`).
  - Python rejects script and binary-property classes (`\p{Greek}`,
    `\p{Alphabetic}`) with `unicode_property`, and rebinds a nullable repeated
    group's capture to the empty text.
  - The linear-time guarantee holds on Rust, Go, LLVM and WebAssembly. TypeScript,
    Python and Swift use backtracking engines, so a pattern such as `^(a+)+$`
    can take exponential time there.
  - Unicode property classes follow each engine's Unicode version.
  - On WebAssembly, a `fac { } cape` around `↦ regex`, the `char` carrier and
    a template with more than three operands are unsupported (`try_call`,
    `littera` and `text format arity` diagnostics); no Wasm host ships, so
    Wasm run tiers are unmeasured.
  - Racket (`sexp`) and Haskell name every regex construct unsupported.
- **Range containment `∈ a‥b` / `∉ a‥b`** has no MIR lowering: it does not run
  on the MIR runner, Racket, LLVM or WebAssembly. The HIR targets emit it.
- **Rust half-width float cells.** `trapping<f16>`, `saturating<f16>`, the `bf16`
  forms and bare `f16` / `bf16` emit through `faber emit --target rust`, exit 0,
  and then fail at `rustc`.
- **Rust corpus builds.** Two corpus programs still fail to build on Rust (one
  stores an awaited promise at a `←` binding, one converts composite values behind
  a `valor`).
- **Print and templates.**
  - `print a, b` lays out one value per line on the MIR text targets (runner
    and Racket) when an argument is a sized integer, enum, class, union, `d64`,
    `inf` or tensor, and the first argument is not a literal; the other targets
    join with spaces. The layout also depends on the argument count. The comma
    form is under review for removal; prefer a string template,
    `print "§ §"(a, b)`, which joins uniformly.
  - LLVM has no template format rows for sized integers (`i8`, `i16`, `i32`,
    `u8`, `u16`, `u32`), enums and several composites, and `print` of an `i16`
    does not link; a `u64` above the `i64` maximum prints signed in a template.
  - Haskell rejects every string template, and a program with two or more
    output statements runs only the last.
  - These gaps were measured on the 2 October tree.
- **`print` tokens are Latin in every locale.** Booleans, `none` and the tuple
  head print as `verum` / `falsum` / `nihil` / `iuncta` even in an English file.
  The ruling is that they follow the code locale (`true` / `false` / `none` /
  `tuple`); the change is not made yet.
- **Enum and union residuals.** The Racket target prints a map holding an enum
  or generic union variant as a raw hash; Go fails to compile a generic unit
  variant; Python and Swift reject generic enums and maps.
- **Other open defects.** `cumulate` (Latin `cumulata`) folds into the caller's
  own accumulator the way `reduce` used to. The checker accepts narrowing an
  inferred error result with `is` and `✓ ✗` without an explicit `T ∪ E`
  annotation, and only MIR validation rejects it. `int ↦ f32` still rounds twice
  on Python, and WebAssembly types the local as `f64`. `faber convert` does not
  resolve imports (a file that imports a library type fails with `SEM002`).
- **WebAssembly.** Programs that use a `lista` are refused by the Wasm emitter
  (`BoundedArray` unsupported); carried from 1.11.
- **Experimental targets differ from `faber run` where the target's arithmetic does.** COBOL checks only stored values, Pascal traps per operation at its own
  native 64-bit limit (run-time error 215) where the runner checks at the store,
  and BASIC numbers are the C64 40-bit float. Targets that print a boolean print
  `verum` / `falsum`. Each target rejects the cases it cannot match by name.
- **Library and gate status.** No gate runs the Gradus library's proba suites,
  and several remain red or blocked; Tela's concatenating gates were red before
  the TypeScript runtime change and have not been re-run on this tree.
- **Public compatibility matrices.** The measurement data and the rendered
  matrices in the public Faber repository are regenerated for this release
  (the keyword rows `intra` and `inter` are gone).
- **Per-target conformance gaps** against the 601-program corpus, measured on the
  release tree: Go has 14 unexpected failures (ceiling 31 expected), Swift 17,
  TypeScript 5 (plus 4 recorded gaps that now pass), Racket (`sexp`) 5, the Faber
  re-emit round trip 8 files, and Wasm 17 per-program tier regressions. LLVM
  refuses 59 programs with a named diagnostic. The MIR runner passes 428
  programs end to end; Rust passes 492. The Swift float-cell exemplum stays a
  Swift expected failure because it also uses `inf`.
- Carried from 1.10: the Gather reverse-mode check, environment-gated device
  checks, and package checks that need the optional Triga provider.

### Not in this release

- Multi-subject `discerne a et b` is not checked or lowered; do not rely on it.
- Character ranges as set bounds (`x ∈ '0'…'9'`) are not supported; interval
  bounds are numbers. Text membership stays `.contains`.
- The slash regex literal and per-group spans are not shipped; read group spans
  from the match with `start()` and `group(n)`.
- Collection-ergonomics rewrite, set-algebra glyphs, superscript powers,
  `reducta` / `filum` kernel forms, and `fac omnia` remain planned.
- `externa` typing and conditional-compilation enforcement stay held; there is no
  LSP.
- Translated reader packs (`ar`, `hi`, `th-TH`, `vi`, `zh-Hans`, `zh-Hant`) keep
  their own spelling for the null type until the word is chosen.
- A `print` display-locale change (Latin tokens to the code locale), and removal
  of the comma `print` form, are decided in direction only.
- Public publication of the Go runtime module and `@faber/runtime` waits for the
  Faber 2 migration; they are consumed by path here.
- No GPU program runs through `faber run`.
- Cista stays on the 0.1.0 line; Radix stays at 0.84.0 (no separate Radix
  release).

### Candidate evidence (operator record)

This section records the local gates run on the candidate tree. It is for the
operator and is omitted from public rendering. Paths are relative; the lane is a
worktree packet (own `target/`) on an 18-core Mac. Gate results quote the run as
it happened. Commands that call `rm` (the release scripts' cleanup) ran with a
no-op `rm` shim on `PATH`.

**Pins.** Radix source commit the candidate is cut from: `6d10e722e` (main when
the lane was created), plus one bump commit (`26026812e`), one pack-digest commit
(`f25c317bc`) and this notes commit. Hosts pin moved `e755e5c969fe` to
`3002760912f3` (the packet sibling; manifest and the build-stamped
`HOSTS_PINNED_REV` agree). Public Faber target API: `faberlang/faber` main with
the matrices commit `e812b44` (`v1.12.0` is the tag the generated manifests
resolve; the tag does not exist yet, which `verify-dev-kit` reports as its one
RESIDUAL). It carries the new runtime namespaces (`faber::exact`, `inf`, `dec`,
`format`, `display`, `gen`, `float`, `regex`), which `v1.11.0` does not.
Radix crate version stays 0.84.0; the faber crate is 1.12.0.

**Runbook local proof.** `validate-release-manifest` ok;
`faber-regen-lock --pinned-siblings --check` ok (hosts pin match, lock fresh);
`cargo build --locked --release -p faber --bin faber` ok (48 s cold);
release-gate recipe (remapped, `--locked --release`) ok (47 s);
`faber --version` prints `faber 1.12.0`; `scan-release-leakage` clean (0
workspace paths, 0 registry paths); `assemble-dev-kit` ok; `verify-dev-kit`
PASSED (all positives and negatives; one RESIDUAL: the D1 git-dependency build
needs the faber tag, and the emitted form is
`faber = { package = "faber", git = "https://github.com/faberlang/faber", tag = "v1.12.0" }`);
`package-archive` ok; `smoke-test-release-archive` RELEASABLE. Local archive
`faber-v1.12.0-aarch64-apple-darwin.tar.gz`; launcher digest `376b9f47…e76af`
(reproduced identically on a second assemble from the final candidate), and
reference-pack digest `a00e996d…cc4c`; both are recorded in the manifest. The
reference-pack digest depends on the commit stamped into `PACK.toml`, so it is
the digest at the manifest's radix pin (`6d10e722e`); a later commit changes it.
CI rebuilds the launcher, so its digest may differ.

**`release-gate --locked-release-build`** (run once on the candidate, 57 s):
locked release build ok, leakage scan clean, `cargo test -p faber --test hygiene`
1 passed, `cargo test -p faber` 1182 passed, 0 failed, 23 ignored;
`=== release-gate · ok ===`.

**Ladder.** Stage 1 ok (18 s, fmt clean, all 53 workspace members checked).
Stage 2 ok (15 s, 0 errors). Stage 3 ok (1 canary package, 2 s). Stage 4a ok
(82 s: reader pack, compat measurement fresh, MIR and HIR coverage). Stage 4b ok
(979 s; over the 548 s of 1.11.0, a slow-gate finding): `genuine FAILs 0 across 0
crate(s)`, 53 crates ok. Stage 4c ok (107 s). Stage 4d ok (9 s, Metal spike on
Apple M5 Max). Stage 4e ok (6 s). Stage 5 ok (18 s, no grammar disagreement
outside the baseline).

**E2E (one lane at a time).** runner ok (428/601 pass, 368/368 pinned goldens;
25 s). Rust ok (492/601 pass, 599/601 accepted, 2 ledger-known build failures,
`await-assignment` and `valor-composita-deep`; 293 s). canonical RED (the same two
miscompiling members). Go: emit stage unexpected (`defectus`, `fient`); golden
407/601 pass, 587/601 accepted, 14 unexpected, expected failures 31 at ceiling
31. TypeScript: lint 3 unexpected; golden 188/193 expected outcomes accepted, 5
unexpected, 4 stale. Swift: emit stage red; golden 584/601 accepted, 253 run, 17
unexpected. Wasm: parse, emit, lint, build ok; golden RED (17 tier regressions,
322/601 emitted, 0 runnable: no stub host ships). LLVM golden ok (verifier-valid
420, runnable 327, output-checked 270, unsupported 59 at ceiling 59; only golden
run, as in 1.11). Racket `sexp`: emit 357/601, lint 348/601, golden 5
unexpected. roundtrip: 502/601 stabilize, 8 unexpected files. mir ok. The
optional `gpu` lane was not run. The packet carries all siblings (`examples`,
`tela`, `norma`), so no `CONVERSIO_MATRIX_FIXTURES` or `FABER_TELA_HOME`
override was needed.

**Public matrices.** `scripta/emit-compat-json.py` regenerated nothing new (the
committed measurement is current). `render-matrices.py --check` was stale and was
re-rendered in the faber repo (`e812b44`, with the README support percentages).

**Operator steps the runbook requires.** (1) Push `faberlang/hosts` main (the
manifest hosts pin must exist on the remote) and `faberlang/faber` main. (2) Tag
`faberlang/faber` `v1.12.0` at `e812b44`. (3) Merge the release branch to Radix
main, then tag `faber/v1.12.0` on the release commit and push it to start the
release workflow. (4) After the workflow, verify downloaded archives by checksum
and smoke before promotion. Known-red items above need the operator's
acknowledgement, per the release protocol.

---

[All releases](/releases/) · [Start](/start/)
