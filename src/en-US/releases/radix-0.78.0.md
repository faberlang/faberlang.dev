+++
title = "Radix 0.78.0"
section = "releases"
order = 19
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.78.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

Minor release spanning **~905 commits** (`v0.77.0..v0.78.0`, 2026-07-22→2026-07-30).
Headline: **morphology-driven async and stream surface**, plus large compiler
hygiene, AIR reverse-AD expansion, new codegen leaves (Swift, Lean), crate
extracts (`radix-parser`, `radix-air`), and performance ratchets.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | ~905 |
| `feat(...)` commits | ~77 |
| `fix(...)` commits | ~149 |
| `docs(...)` commits | ~371 |
| `test(...)` commits | ~46 |

Reconstruct the full log:

```bash
git log v0.77.0..v0.78.0 --oneline --no-merges
```

### Major tracks

#### Morphology: async / stream surface

Callable posture now has preferred morphology words while legacy annotations
remain accepted compatibility spellings. Context-dependent await-`cede` is
replaced by distinct semantic identities.

**Preferred migrations**

```text
@ futura functio f() → T       -> functio f() fiet → T
@ cursor functio f() → T       -> functio f() fiunt → T
@ futura @ cursor ...          -> functio f() fient → T
fixum T x ← cede future        -> figendum T x ← future
varia T x ← cede future        -> variandum T x ← future
redde cede future              -> reddet future
cede future                    -> tacebit future   # await and discard any success T
cede value in a cursor         -> cede value       # yield only
```

| Word / form | Posture / operation |
| --- | --- |
| (bare) | synchronous finite |
| `fiet` | asynchronous finite → `promissum<T>` |
| `fiunt` | synchronous stream |
| `fient` | asynchronous stream |
| `figendum` / `variandum` | await-bind immutable / mutable |
| `reddet` | await-return (`fiet` only) |
| `tacebit` | await-discard |
| `cede value` | yield (`fiunt` / `fient` only) |

**Two-channel promises:** `promissum<T>` is infallible shorthand for
`promissum<T ⇥ numquam>`; `promissum<T ⇥ E>` preserves success and alternate.
Infallible widens to failable; failable does not narrow.

**Backend support**

| Backend | Status |
| --- | --- |
| **Rust** | Primary path for async finite, sync stream, and `fient` via async-cursor carrier |
| **TypeScript** | `async function*` with native `await`/`yield` |
| **Go** | Sync stream works; `fient` fails closed until channel cursor lands |
| **Swift** | Async stream forms fail closed until `AsyncStream` lowering lands |
| **MIR/GPU** | Fails closed via device-function shape policy |

Reader `llm` pack maps one English surface per identity (`async`, `generator`,
`async_generator`, `await_const`, `await_var`, `return_await`, `await`, `yield`).
`@ futura` / `@ cursor` remain accepted; forma must not strip them automatically.

#### Modular words & product parity

Width-parametric modular words continue through MIR numeric treatment and
wrapping sum, Rust codegen driver policy, and product-parity goal closeout.
Related stepper/octeti range fixes land under the same hygiene wave.

#### `iuncta` (tuple product) keyword

`iuncta` is a globally reserved declaration keyword with parser type/construction
syntax, semantic checking (construct, access, destructure, Option policy), MIR
validation, Rust and LLVM codegen (tuple as LLVM struct), and reader-locale
diagnostics.

#### `adfirma` separator: `secus`

`adfirma` multi-clause separator is **`secus`** (not comma). WARN006 deprecation
path for the old separator is removed.

#### Diagnostic promotion CLI

- `--deny-warnings` and `--deny <CODE>` promote selected diagnostics to hard
  errors at the driver surface.

#### AIR reverse-AD & tensor ops

Six-layer reverse-AD VJP coverage expands across arithmetic, activations, and
shapers: Sub/Div/Neg, MatMul/Sum, Exp/Log, Sqrt, GELU/Tanh, LayerNorm/SumAxis,
Softmax, Transpose/Forma, CruxEntropia. Companion pre-resolution and FuncSig
injection validate call sites. Driver exposes `AirBackwardBundle` for CLI
companion generation. Op surface gains Gelu/Softmax/LayerNorm tracking and
rank-2 matmul WGSL native-support promotion.

#### ValidatedMir API gate

`ValidatedMir` newtype gates the public MIR emit/step entry points (PRP-010).
Callers pass a validated program instead of raw program+validation pairs.
`into_parts()` is sealed/removed so the proof boundary stays closed.

#### Crate extracts & new codegen leaves

| Extract / leaf | Notes |
| --- | --- |
| `radix-parser` | Dedicated sibling crate for the parser |
| `radix-air` | Dedicated sibling crate for AIR |
| `radix-codegen-swift` | SC-001…SC-009: primitives through library/SPM mode, failable, optional/dubium, enums, stdlib bridge |
| `radix-codegen-lean` | Aspect obligations, Lake template, naming contract, checked prelude, integration wiring |

HIR gains Serialize/Deserialize on nodes and FHIR load scaffold (`HirArtifactError`,
`AnalyzedUnit::from_loaded`). Structured compile benchmark framework (PRP-058).

#### Compiler hygiene & correctness (F-series + cross-backend)

Large fix wave across lexer, parser, semantic, forma, MIR, LLVM, WASM, WGSL,
Metal, stepper, host ABI, and all codegen backends (Rust/TS/Go/Swift/Faber).
Highlights:

- Cross-file `DefId` resolution in Rust and TS codegen
- Failable registration and fail-closed missing DefId
- Modular-word CLI/target policy
- F-055 panic → deferred diagnostic
- WGSL matmul workgroup origin / OOB axes; WASM no invalid `f64.tanh`
- Mutating method calls treated as receiver writes

#### Performance ratchets (PRP series)

Lexer/parser O(1) keyword maps and trivia index; TypeTable hash-cons; semantic
scope/binding indices and failable worklist; MIR dense-ID indexes and shared
validate maps; monomorphize dense index; codegen backend index maps; driver
session caches; stepper O(1) indexes + Rc share; Arc-shared lowering maps
(PRP-054). Benchmark baseline committed for PRP-058.

#### Reader locale & source locale

Per-file source locale via frontmatter; full `llm` reader pack; morphology
async keywords localized; `iuncta` keyword rows across packs.

### Breaking / author-visible

| Change | Migration |
| --- | --- |
| Preferred async/stream posture is morphological | Prefer `fiet`/`fiunt`/`fient`; annotations still work |
| Await no longer uses bare `cede future` | Use `figendum`/`variandum`/`reddet`/`tacebit` |
| `cede` in async finite is yield-only, not await | Use await morphology for futures |
| `adfirma` clauses separated by `secus` | Replace commas between `adfirma` arms |
| Public MIR probes take `ValidatedMir` | Lower/validate first; drop raw program+validation pairs |

### What is NOT included

- No general expression-form `await` operator.
- No `fit` alias for bare synchronous finite.
- No compatibility grammar for await-`cede`.
- No closure-literal or first-class function-type posture syntax.
- No deferred/cold promise morphology (`fieret`/`fierent` — reserved for follow-up).
- Go/Swift `fient` production carriers remain fail-closed.
- Metal factory campaigns remain paused.

### Version alignment

| Item | Value |
| --- | --- |
| Source tag | `v0.78.0` |
| `crates/radix` version | `0.78.0` |
| Public artifact tag | `radix-v0.78.0` on `faberlang/releases` |
| Workspace members bumped | all `0.77.0` → `0.78.0` (hygiene-ratchet stays `0.1.0`) |

### Verification (pre-release)

Recorded on the release candidate tree (2026-07-30):

| Gate | Result |
| --- | --- |
| `cargo build --locked --release -p radix --bin radix` | pass |
| `radix --version` (release binary) | `radix 0.78.0` |
| `cargo nextest run` | pass — 5216 passed, 154 skipped |

### Publish

1. Bump all workspace crate versions `0.77.0` → `0.78.0` (not hygiene-ratchet).
2. `cargo update` so `Cargo.lock` matches manifests.
3. Verify locked release build + nextest.
4. **Single commit** with version bump + lockfile (+ this notes file if still dirty):
   `release(radix): v0.78.0`
5. Annotated tag: `git tag -a v0.78.0 -m "Radix v0.78.0"`
6. Push: `git push origin main && git push origin v0.78.0`
7. Monitor: `gh run list -R faberlang/radix --limit 5`
8. Confirm `faberlang/releases` publishes `radix-v0.78.0` multi-arch archives.

**Never** tag a commit whose `Cargo.lock` is stale relative to the bumped
manifests — CI uses `cargo build --locked`.

---

[All releases](/releases/) · [Install the current release](/start/install.html)
