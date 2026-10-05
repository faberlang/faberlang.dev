+++
title = "Faber 1.11.0"
section = "releases"
order = 10
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Faber |
| **Version** | 1.11.0 |
| **Tag** | `faber-v1.11.0` |
| **GitHub** | [faber-v1.11.0](https://github.com/faberlang/releases/releases/tag/faber-v1.11.0) |
| **Published** | 2026-10-02 |
| **License** | MIT |

## Install this version {#install}

Pinned download for **Faber 1.11.0**. For the current release, use [Start](/start/) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [faber-v1.11.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.11.0/faber-v1.11.0-aarch64-apple-darwin.tar.gz) | 12.6 MB | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.11.0/faber-v1.11.0-aarch64-apple-darwin.tar.gz.sha256) |
| **Linux x64** | [faber-v1.11.0-x86_64-unknown-linux-gnu.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.11.0/faber-v1.11.0-x86_64-unknown-linux-gnu.tar.gz) | 14.2 MB | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.11.0/faber-v1.11.0-x86_64-unknown-linux-gnu.tar.gz.sha256) |

```bash
curl -fsSL -o faber.tgz \
  https://github.com/faberlang/releases/releases/download/faber-v1.11.0/faber-v1.11.0-aarch64-apple-darwin.tar.gz
tar -xzf faber.tgz
# The archive ships bin/ and share/; keep them together so the
# reader packs resolve beside the binary.
sudo mv bin/faber /usr/local/bin/faber
sudo mv share/faber /usr/local/share/faber
faber --version
```

## Release notes {#notes}

> **Status**: final

Faber 1.11 is a large language step. Since 1.10.0 (2 September 2026) the
language-decisions work landed: numbers now state their overflow
policy in the type, the unbounded integer `inf` exists, failure handling no
longer hides defaults, records and sum types have settled rules, concurrency is
conversations (`ad` / `sermo`), and several old forms are gone. The release
also adds float cells (`trapping<f32>` and friends), makes `faber format`
and the codemods report-only by default, and tidies the code every backend
emits. Many of these are breaking changes; read "Breaking changes" before you
upgrade a package.

### Language

**Numbers state their policy.** The outer word is the overflow policy and the
inner marker is the width: `trapping<W>`, `wrapping<W>`, `saturating<W>` (Latin
`exactus`, `modulus`, `saturatus`). A bare marker (`u8`, `i32`, `f64`) is the
trapping default and the same type as `trapping<W>`. Signed `wrapping<i8..i64>`
is allowed. The long wrapped spellings (`numerus<u8>`, `fractus<f32>`, the
`numerus<_>` holes) are rejected with `PARSE040 numeric_wrapper_retired`.

**Arithmetic is exact until the store.** Integer arithmetic runs at 64 bits or
wider, and a width limit is applied once, where the value is stored into a
narrower cell. Nothing clamps, traps, or saturates per operation. `/` and `%`
on integers floor (`7 / -2` is `-4`; `-7 % 3` is `2`); `÷` is true division
(`7 ÷ 2` is `3.5`). Implicit widening is lossless and never crosses number
families. `∷` states only what the compiler can prove; anything that can fail at
run time goes through `↦`. An integer power with a negative exponent is rejected.

**Float cells.** `trapping<W>` and `saturating<W>` now work over `f16`, `bf16`,
`f32` and `f64`, under the same store-only law. A `saturating` float cell is the
bare IEEE float: overflow gives infinity, `0.0 / 0.0` gives NaN, nothing clamps
to the largest finite value. A `trapping` cell checks only where a value is
stored or converted into it: `print t * t` prints `inf`, but
`const trapping<f32> u ← t * t` stops with "inf does not fit in `f32`". Support
by target: the MIR runner, Racket (`sexp`), Rust, Go, TypeScript, Python and
Swift emit cells; the WebAssembly and LLVM targets refuse a cell with a named
diagnostic (`wasm_target_policy_float_unsupported`,
`llvm_target_policy_float_unsupported`); Go refuses `f16` and `bf16` by name;
Haskell refuses a cell. See Known issues for the Rust half-width gap.

**Unbounded integers.** `inf` is an opt-in arbitrary-precision integer: exact
arithmetic, ruled conversions, shifts past 64 bits, any-length JSON
integers. It runs on the MIR runner, Rust (`faber::Magnus`), Go (`math/big`),
TypeScript (`bigint`), Python (`int`) and Racket. Swift and Haskell refuse it by
name (`inf_target_unsupported`). It is never the default.

**Decimals.** `d64` is the only decimal width (`d32` is removed:
`SEM008 removed_decimal_width_d32`). A `d64` is `i64 × 10⁻⁸`, arithmetic is
exact until the store, division rounds half-even, and untyped constants join by
exact value. Display prints the shortest form (`12.5`, `12`); a `¶` format spec
prints exactly what it says (`12.5 ¶ ".2"` is `12.50`). Decimal display and
decimal-operand repairs landed on the runner, Rust, Go, TypeScript, Swift,
Python and Racket.

**Failure handling has no silent defaults.** `⇥` only ever names an error type.
The inline recovery `↦ T ⇥ value` is gone (`PARSE030 recovery_uses_exit_arrow`).
A default is written with the `⊥` channel: `"abc" ↦ int ⊥ 0`, and also on
failable calls. A failable conversion must be handled, by `⊥`, an enclosing
`fac { } cape`, `capta { }`, or a function that declares `⇥ E`; `main` is
exempt. An unhandled failable call directly in `main` panics on every backend.
Conversions have a `via` clause for hints: `"ff" ↦ u8 via Hex`, `65 ↦ char via
Code`; the type-argument hint is gone. A registered `@ conversio` pair also
serves explicit `↦`, and `ordo` has built-in `↦` rows.

**One conditional expression.** `c ✓ a ✗ b` is the only conditional
expression, one level deep, the same in every locale. `c ? a : b` and
`c sic a secus b` are removed (`PARSE030 conditional_question_colon_removed`).

**Null words are split.** In the English reader the null value is `null` and
the null type is `none` (Latin `nulla` / `nihil`). `est` / `non est` (`is` /
`is not`) is a type test only; a value on its right-hand side is
`SEM011 est_value_rhs`. An imported type is a legal `est` target.

**Records.** Every `class` (`genus`) field declares exactly one of `const`, `var`,
`static` (Latin `fixum`, `varia`, `generis`); an unmarked field is `PARSE010`.
`nexum` is removed. Copy-with-changes is `Genus { x = 1 } from p` (Latin `ex`);
`sparge` is gone from construction literals. Members are public by default, and
`@ privata` is enforced. Class inheritance (`extends`, `abstract`; Latin `sub`,
`abstractus`) is removed: contracts are `interface` and `implements`
(`implendum`, `implet`), shared data is composition. A bound on a type
parameter uses `implements`, and `implements` takes type arguments. The `Orderable`
contract drives every ordering glyph; tuples order lexicographically; `sort`
(`ordina`) takes a key selector; whole-string `≺` compares code points. Recursive types
box automatically on Rust. Declarations inside a function body are rejected.

**Modules and constants.** A top-level runtime `←` binding is an error
(`SEM062 top_level_binding`). The module constant is `const T X = e`
(`fixum T X = e`); `static T X = e` at statement start is
`PARSE010 static_decl_retired`. `const T x = e` is also a typed local
compile-time constant. `comptime { … }` (`praefixum`) initializes constants at
build time, `embed` (`insere`) reads a neighbouring file at build time, and
`module` (`regio`) names a file. Executable top-level statements beside an
explicit entry point are rejected (`SEM008 top_level_statement_beside_entry`);
move them into `main`. Selective imports bind types as well as values.

**Matching.** `case A or B` (`casu A aut B`) or-patterns bind the same names and
types. `match` (`discerne`) matches closed sets only (enums, unions); width and
length-shape type patterns are retired, and signed literal patterns work. NaN
patterns are rejected. `enum` (`ordo`) and `union` (`discretio`) are pure data:
no methods, no `implements`.

**Iteration.** `at` (`apud`) iterates lists and maps as well as tensors:
`for from xs at [i] const x`. Composite keys are tuple keys
(a map keyed by `iuncta<K1, K2>`), and map keys must be hashable (checked).
Sets and maps iterate in unspecified order; sort when order matters.
`itera` binds real element types, and a non-iterable is rejected.

**Concurrency is conversations.** `@ ad` (`call`) serves a route from Faber code, with a
static route table, a task per local handler, and copies across the boundary.
The conversation type is `channel<O, R>` (`sermo<O, R>`); the English names
are `channel`, `frame`, `send<T>`, `recv<T>`. A channel closes itself when its conversation completes,
and `Closable` / `close()` exist on all four backends. Sync generators (`generator`, `fiunt`)
are lazy on the runner and TypeScript, and on Rust and Go for most forms. `perge` passes through a `fac`
block to the enclosing loop. `cura` / `curata` are removed.

**Text and bytes.** `littera` (`char`) is a Unicode scalar; `octetus` (`byte`)
is `u8`; `octeti` is `lista<octetus>`; indexing a string gives `littera`.
Numbers convert to digits, not code points. `value ¶ "spec"` formats a value
(width, fill, precision, sign, hex/bin/oct) with a literal spec checked against
the value's type. `print` shows a `genus` as its construction literal, lists as
`[0, 1, 2]`, maps as `{"k": v}`, tuples as `iuncta [..]`, uniformly across
backends.

**Tensors and kernels.** Scalar operators lift over tensors elementwise, and
`abs sqrt exp ln log10 sin cos tan` lift over tensors. Kernel legality is a
checked pass: thread-id builtins are rejected in user code, builtin-named kernel
parameters are rejected, and `gather` takes `tensor<u32, [n]>` ids. Stage
bodies for shaders can bind resources and reflect them (WGSL text).

**Keyword and naming sweep.** `en` names for the conversation family,
`bytes`/`byte`/`char`, and `wrapping` for the modulus family. A leading `_` on
an identifier warns (`WARN030`). The `LOCALE002` near-keyword suggestion fires
only at an error span.

### Tooling

- **`faber format`, `faber convert`, `output-transfer-codemod` and `field-modifier-codemod` report by default.** They list the files that would
  change and exit 1 if any would; `--write` applies the change, `--stdout`
  prints it. The retired `--locale` and `--canonical` flags are gone from
  `format` (use `faber convert --to <LOCALE>` to change locales). A script that
  relied on the old in-place default must add `--write`.
- `faber format` refuses to drop source constructs the HIR cannot carry, keeps
  in-place numeric twins and the transpose glyph, and re-emits the long numeric
  forms as bare width markers.
- `faber doc` renders the exported API with its doc comments. A comment block
  directly above a declaration is its documentation.
- `faber run` prints `abort: <reason>` for runner traps, once.
- Manifests reject unknown `[target.<key>]` tables with a structured
  diagnostic; a binding manifest has one schema with a types table.
- `faber check` rejects mutating intrinsics on immutable bindings and unknown
  methods on scalar numeric receivers.

### Targets

Generated code is cleaner and more uniform; these are repairs, not new claims.

- **Rust.** Unit-returning signatures omit `-> ()`, index casts drop redundant
  parentheses and `0usize`, and reserved words emit as raw identifiers.
- **Go.** The generated header is the one Go tooling recognises; `else { if }`
  emits as `else if`; every imported package name and `rt` is reserved for user
  bindings, so a user name no longer collides with a package; bounded arrays
  are typed slices with the capacity trap; maps print as `{"k": v}`.
- **TypeScript.** Identity lambdas, single-expression IIFEs, dead one-shot
  loops and redundant numeric casts are gone; a statically non-optional `textus`
  prints without the display helper; reserved-word fields and methods are one
  property name everywhere.
- **Swift.** Keyword identifiers are escaped with backticks, tuples lower to
  Swift tuples, and numeric list arithmetic is elementwise.
- **Python.** Decimal values display correctly, integers are exact, and `inf`
  rides Python's `int`.
- **Racket (`sexp`).** `d64` is an exact rational, composites behind a `valor`
  work, and `inf` is uncapped.

### GPU

This release makes no GPU product claim. No Faber program drives the GPU
through `faber run` yet; the device work from earlier releases is a developer
surface and the GPU campaign is paused. What does ship is language-level:
kernel legality checks, tensor elementwise lifting, and shader stage binding
declarations.

### Breaking changes

1. **Report-only tooling.** `faber format`, `convert`, `output-transfer-codemod`
   and `field-modifier-codemod` no longer write by default; add `--write`.
   `--locale` and `--canonical` are removed from `faber format`.
2. **Wrapped numeric spellings** (`numerus<u8>`, `fractus<f32>`, `numerus<_>`,
   `numerus<inf>`) are rejected; write `u8`, `f32`, `inf`.
3. **`d32` is removed**; use `d64`.
4. **Inline recovery is removed**: `↦ T ⇥ value` and `↤ … ⇥ value` become
   `↦ T ⊥ value`. A failable conversion with no handler is a compile error.
5. **`c ? a : b` and `c sic a secus b` are removed**; write `c ✓ a ✗ b`.
6. **`static T X = e` is removed**; write `const T X = e`. A top-level
   `const x ← e` (runtime binding) is `SEM062`.
7. **Every `genus` field needs `const`, `var`, or `static`** (`fixum`,
   `varia`, `generis`); `nexum` and `sparge` in construction literals are
   removed. `faber field-modifier-codemod --write` migrates source.
8. **Class inheritance is removed** (`extends`, `abstract`, bodyless abstract
   methods). Use `interface` / `implements` and composition.
9. **`est` is a type test only.** `x is null` and `x is CONST` are errors; the
   English null type is `none`, the null value is `null`.
10. **Executable top-level statements beside `incipit` / `main` are rejected**
    (`SEM008`); they were previously dropped silently.
11. **`cura` / `curata`** allocator syntax is removed.
12. **`match` (`discerne`) matches closed sets only**; width and length-shape
    type patterns are rejected.
13. **Declarations inside a function body are rejected.**
14. **Integer `/` floors and `%` is the floor remainder** on every number
    family; integer `^` rejects a negative exponent. Programs that relied on
    truncating division must be rewritten.
15. **`print` output changed** for decimals, `genus` values, maps and tuples
    (see Language); golden files that capture it need regenerating.

### Known issues

- **Rust half-width float cells.** `trapping<f16>`, `saturating<f16>`, and the
  `bf16` forms (and bare `f16` / `bf16`) emit through `faber emit --target
  rust` and exit 0, then fail at `rustc`. Rust does not refuse them by name.
- **Rust corpus builds.** Two programs still fail to build on Rust: one that
  stores an awaited promise at a `←` binding, and one that converts composite
  values behind a `valor` (the same program fails the canonical-Rust compile
  floor).
- **Range containment** (`x intra a‥b`, the `intra` keyword) has no MIR
  lowering: it does not run on the MIR runner or the Racket target.
- **WebAssembly.** Programs that use a `lista` are refused by the Wasm emitter
  (`type BoundedArray` unsupported); seventeen corpus programs sit below their
  recorded Wasm tier. No stub host ships, so Wasm run tiers are unmeasured.
- **Per-target conformance gaps** against the 570-program corpus: Go has 14
  unexpected failures, Swift 17, TypeScript 5 (plus 4 recorded gaps that now
  pass), Racket 5, and the Faber re-emit round trip 8 files. LLVM refuses 58
  programs with a named diagnostic. The MIR runner passes 398 programs end to
  end; Rust passes 462.
- **Swift and `inf`.** The float-cell exemplum remains a Swift expected failure
  because it also uses `inf`.
- **Stage-2 lint and one ratchet are red on the release tree**: seven clippy
  findings under `-D warnings` in the Go, Rust, Swift, TypeScript, Faber and MIR
  crates, and the generated-Rust helper-spelling budget (258 against 254). The
  emitted-Metal spike gate still uses a retired wrapped spelling.
- **Compat measurement is not recommitted.** The corpus measurement JSON and the
  public compatibility matrices lag the tree (additive drift, and the `intra`
  capability loss).
- Carried from 1.10: the Gather reverse-mode check, environment-gated device
  checks, and package checks that need the optional Triga provider.

### Not in this release

- Multi-subject `discerne a et b` is partly landed (header parsing and
  re-emit) but not checked or lowered; do not rely on it.
- Regex operations (`find`, `captures`, `split`, `replace`, failable
  `↦ regex`) and the membership glyph (`∈` / `∉` replacing `intra` / `inter`)
  are designed and not shipped.
- Collection-ergonomics rewrite, set-algebra glyphs, superscript powers,
  `reducta` / `filum` kernel forms, and `fac omnia` remain planned.
- `externa` typing and conditional-compilation enforcement stay held; there is
  no LSP.
- Translated reader packs (`ar`, `hi`, `th-TH`, `vi`, `zh-Hans`, `zh-Hant`) keep
  their own spelling for the null type until the word is chosen.
- No GPU program runs through `faber run`.
- Cista stays on the 0.1.0 line; Radix stays at 0.84.0 (no separate Radix
  release).

### Candidate evidence (operator record)

This section records the local gates run on the candidate tree. It is for the
operator and is omitted from public rendering. Paths are relative; the lane is a
detached packet on an 18-core Mac. Gate results quote the run as it happened.

**Pins.** Radix source commit the candidate is cut from: the batch 18 merge
(`2fe88fb3b`), plus one bump commit and this notes commit. Hosts pin moved
`46b235209469` to `e755e5c969fe` (the packet sibling; manifest and
`HOSTS_PINNED_REV` agree). Public Faber target API: `faberlang/faber` main
`ca6939426a51` (`v1.11.0` is the tag the generated manifests resolve; the tag
does not exist yet, which `verify-dev-kit` reports as its one RESIDUAL). Radix
crate version stays 0.84.0; the faber crate is 1.11.0. Regex aggregate and
`faber::exact` emission are not in this tree.

**Runbook local proof.** `validate-release-manifest` ok;
`faber-regen-lock --pinned-siblings --check` ok; `cargo build --locked -p faber`
ok (23 s); release-gate recipe (remapped, `--locked --release`) ok (42 s);
`faber --version` prints `faber 1.11.0`; `scan-release-leakage` clean (0
workspace paths, 0 registry paths); `assemble-dev-kit` ok; `verify-dev-kit`
PASSED (all positives and negatives; one RESIDUAL: the D1 git-dependency build
needs the faber tag); `package-archive` ok; `smoke-test-release-archive`
RELEASABLE. Local archive `faber-v1.11.0-aarch64-apple-darwin.tar.gz` sha256
`b7bec5239e1580128da153ba83cb3cf9d784275f4e029be6819f25ece13d0dc8`; local
launcher digest `933f8f1b…c320529`; reference-pack digest `3b0d29c5…5416` (both
recorded in the manifest; CI rebuilds the launcher, so its digest will differ).
`release-gate` equivalent (run by hand, because the script's own cleanup uses
`rm`): `cargo test -p faber --test hygiene` 1 passed; `cargo test -p faber` 1170
passed, 0 failed, 23 ignored.

**Ladder.** Stage 1 ok (18.6 s, 49 members fmt clean). Stage 2 RED: 7 clippy
errors (`needless_lifetimes` hir-faber `expr.rs:66`; `match_like_matches_macro`
hir-go `decimal.rs:36`, hir-rust `decimal.rs:32`, hir-ts `ops.rs:74`;
`too_many_arguments` hir-swift `control.rs:363`, hir-ts `access.rs:411`;
`collapsible_if` mir `vector_expand.rs:228`). Stage 3 ok (1 canary package).
Stage 4a: reader-pack ok; compat JSON freshness RED (capability loss for
`intra`, plus additive drift); MIR coverage ok; HIR coverage ok. Stage 4b (9 min
8 s, over the 300 s estimate): 2 crates FAIL: `faber` (1 test needs `tela`
beside radix, passes with `FABER_TELA_HOME`) and `radix-codegen-shared`
(`legacy_helper_spellings_stay_within_budget`, 258 against 254); all 47 other
crates pass. Stage 4c ok. Stage 4d RED (`scripta/metal-faber-spike` still writes
`fractus<f32>`, `PARSE040`). Stage 4e ok. Stage 5 ok. The packet has no
`examples` or `tela` sibling; the conversio fixtures and `tela` were read from
the main checkout (`CONVERSIO_MATRIX_FIXTURES`, `FABER_TELA_HOME`).

**E2E (one lane at a time).** runner ok (398/570 pass; 35 s). Rust ok (462/570
pass, 568/570 accepted, 2 ledger-known build failures; 4 min 22 s), run against
`faberlang/faber` main. canonical RED (2 miscompiling members, the same two Rust
build failures). Go: parse ok, emit stage 2 unexpected (`defectus`, `fient`),
golden 381/570 pass, 556/570 accepted, 14 unexpected. TypeScript: lint 3
unexpected; golden 186/191 expected outcomes, 5 unexpected, 4 stale. Swift: emit
stage red; golden 553/570 accepted, 225 run, 17 unexpected. Wasm: parse, emit,
lint, build ok; golden RED (17 tier regressions, 314/570 emitted, 0 runnable).
LLVM golden ok (verifier-valid 391, runnable 309, output-checked 252,
unsupported 58 at ceiling 58; only golden run: the full emit stage is a known
slow gate). Racket `sexp`: 327/570 pass, 5 unexpected. roundtrip: 472/570
stabilize, 8 unexpected files. mir ok. The optional `gpu` lane was not run.

**Operator steps the runbook requires.** (1) Push `faberlang/hosts` main (6
commits; the manifest hosts pin must exist on the remote) and `faberlang/faber`
main (8 commits). (2) Tag `faberlang/faber` `v1.11.0` at the commit named in the
hand-off. (3) Merge the release branch to Radix main, then tag `faber/v1.11.0`
on the release commit and push it to start the release workflow. (4) After the
workflow, verify downloaded archives by checksum and smoke before promotion.
(5) Refresh the public matrices in the faber repo only after fresh Radix
measurement is committed. Known-red items above need the operator's
acknowledgement, per the release protocol.

---

[All releases](/releases/) · [Start](/start/)
