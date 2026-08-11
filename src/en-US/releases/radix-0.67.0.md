+++
title = "Radix 0.67.0"
section = "releases"
order = 33
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.67.0 |
| **Tag** | `radix-v0.67.0` |
| **GitHub** | [radix-v0.67.0](https://github.com/faberlang/releases/releases/tag/radix-v0.67.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.67.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.67.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.67.0/radix-v0.67.0-aarch64-apple-darwin.tar.gz) | 2.6 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.67.0/radix-v0.67.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.67.0/radix-v0.67.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.67.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

GPU core type foundation (atomic, matrix, f16), GPU workload floor harness with
fixture parity across MIR and Rust targets, stepper alignment completion, and
a structured Rust e2e failures matrix with ratchetted expected-failure cells.
Retires the legacy modulus compiler path and library source splicing.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 138 |
| `feat(...)` | 18 |
| `fix(...)` | 29 |
| `test(...)` | 25 |
| `docs(...)` | 53 |
| `polish(...)` | 10 |
| `stepper-alignment(...)` | 2 |
| Date span | 2026-07-05 → 2026-07-06 |

### Major tracks

#### GPU core types (atomic, matrix, f16)

New scalar and aggregate numeric foundation for GPU targets.

- **f16 scalar width:** EBNF, parser, semantic resolution, MIR layout, stepper
  value carrier, LLVM/Metal/WGSL emit foundation, tensor goal gate
  (`ff7e21066`)
- **Matrix core type:** register type + parser, reject materialization (no heap
  allocation), typecheck elementwise operations, lower elementwise MIR, MIR
  layout entries across all backends (`d1da44d04`, `3f751859f`, `ed8bdf81e`,
  `603bef9c2`)
- **Atomic type foundation:** parser, MIR layout and device gating, codegen
  entries for Rust/Faber/Go/TS, WGSL/Metal/LLVM/Sexp emit, target gate tests
  (`63c8c37fb`, `42d8d8a5c`, `91c7bb5d2`, `cbb8c3841`, `480e448fc`)
- GPU core target coverage alignment and stage-4/closeout deliveries
  (`9bb7819ca`, `e9e0f8277`, `475ca24a7`)

#### GPU workload floor

Runnable GPU workload fixtures establishing a baseline floor for compiler
correctness across MIR stepper and Rust codegen targets.

- Five workload rungs as Faber source + expected/ref.json: `rung-0-matmul`,
  `rung-1-softmax`, `rung-2-mlp-forward`, `rung-3-linear-backward`,
  `rung-4-toy-train` (`69913c957`)
- Workload fixture parity enforcement across MIR and Rust emit targets
  (`56acad3d9`)
- Numeric comparison and reference validation for GPU output
  (`31a89be77`, `9610f103f`)
- Union zero-init policy lock for device-side layout (`d1e91b537`)
- Factory goal and baseline ledger (`5100edd4a`, `69913c957`)

#### Stepper alignment (SA-002, SA-003, phase-6 closeout)

Completes the stepper-alignment campaign with stages 3 and 4 plus factory
closeout.

- **Stage 3 (SA-002):** Conversion target-width fidelity — range-checks parsed
  numeric literals against the target `NumericWidth` so the stepper matches Rust
  codegen's fallible `parse::<T>()` behavior (`8dcfa00e8`)
- **Stage 4 (SA-003):** Cede / CursorStream stepper handlers — `Cede` is
  dual-mode (synchronous await vs generator yield); `CursorStream` collects a
  `@cursor` generator's yields into `lista<T>` (`f9782d0aa`)
- Phase-6 ratchet closeout and capability matrix updates (`bdd03e0ff`)

#### Rust e2e failures matrix

Structured classification of expected Rust compile/runtime failures with a
ratchetted regression ledger.

- Expected compile failure classification for script kernel, vector builtins,
  matrix host, AD runtime, library imports (`132f524af`, `c249dbbe4`,
  `9589c1957`, `98ae481f3`, `b52f1a037`)
- Expected runtime failure classification and exit-code acceptance
  (`9fb805ebb`, `24b08f815`)
- Ratchet MIR baseline floors and mathesis rows (`ef6875853`, `5e6ba738a`)
- Declaration-only Rust fixtures batch (`17e075295`, `b3f64687c`,
  `fd5520800`)
- Failure matrix delivery with baseline document (`2000077fe`,
  `4afb221e8`)
- Ledger closeout after matrix population (`e36af60cd`)

#### File interface / Package / Library retirements

- **File namespace calls from interfaces:** typecheck and compile `path:method()`
  syntax through file interfaces (`2dd8c9fed`)
- **File interface remapper substrate:** substrate for remapping file-interface
  paths at compile time (`055069a76`)
- **File interface cache:** `faber-cli` caches extracted file interfaces across
  compilations (`b64d324bc`)
- **Library source splicing retired:** removes the old source-assembly path for
  library packages (`c9ff93528`, `30e29c0d7`)
- **Modulus compiler path retired:** removes the dedicated modulus operator
  lowering, frame shim, and runtime intrinsics — replaced by numeric widening
  casts and library-based iteration (`c9798859b`, `a4fd3bf1d`, `2a84cfa8d`,
  `6ad8f7ac2`, `735e103b4`)
- Stdlib file interfaces migrated to the new package path (`2033a1371`)
- Factory campaign lock and delivery docs (`d0ca3d7bb`, `f06f81330`,
  `bf6b07883`, `a4fd3bf1d`, `5100edd4a`)

#### MIR / Rust codegen fixes

A broad sweep of Rust emit fixes across valor carriers, call propagation, and
builtin lowering.

- **Failable call propagation:** lowers failable call-site propagation through
  MIR (`2fe9e825d`)
- **Valor boxing:** box sized numerics and lista literals through valor carriers
  (`030f4d592`, `e31e8f932`); check sized numerus valor extraction
  (`ba5f73236`); reject unsupported valor sized extraction (`79e8ab33e`)
- **Vector intrinsics:** lower vector intrinsics to Rust arrays
  (`fece8bc53`)
- **Captured callbacks:** emit wasm captured callback closures, captured
  collection callbacks, and sexp probe handlers (`8a9f6a6bf`,
  `008b18ce7`, `f785acdc9`)
- **Numeric cast and interval helpers:** emit numeric widening casts, interval
  list materialization helper, reject unsupported sized interval helpers
  (`6ad8f7ac2`, `735e103b4`, `871f34c91`)
- **Stepped/rejected values:** reject stepped interval values, reject nested
  tensor shape holes, reject truthiness recovery arms, reject failable closure
  rust emit (`11539a4b4`, `ccbc5c872`, `6bcc78941`, `06b34c68b`)
- **Misc:** clone octeti call args, enforce aggregate numeric target direction,
  close lista filter lowering, preserve frame trace conversions, clone octeti
  call args, align exempla stdout with fractus display
  (`963f1a787`, `2a84cfa8d`, `98f99a81c`, `d7198ab9d`, `ccce2199c`,
  `98d2c9122`, `ca3fa3c82`, `e9cceb46e`)

#### Reader locale packs

- Add locale pack TOML assets for `ar`, `hi`, `la`, `th-TH`, `zh-Hans` with
  keyword/type entries (`32696f4fa`)
- Reader locale pack campaign docs and audit (`de2578e86`, `aa4a4172f`)

#### Polish (code extraction)

Ten structural extractions isolating compiler modules for future crate
extraction:

- `polish(parser):` extract lex error conversion, drop dead annotation span
  merge (`9816e6f04`, `670e3bbc1`)
- `polish(radix):` extract sexp storage defaults, centralize HIR call argument
  walks, derive MIR program default, isolate Rust redde emission, extract emit
  reflection output (`3ed9cc64a`, `81eba92ff`, `ee60b1d32`, `ee2f5bc58`,
  `ea031e19f`)
- `polish(faber-cli):` extract package unit Rust generation, extract package
  source loading, name package MIR dispatch lookup (`74b5f5457`,
  `ccda71a81`, `36a96b818`)

#### Deferred audit trail

Thirty-three docs commits recording and narrowing deferred items across the
compiler surface:

- Defer audits: frame valor, JSON build, import path, chorda regex, recursion,
  import, sparse MIR, intervals, LLVM leaf, regex guard, curata allocator,
  collection conversion source (`8020c4651`, `3576ab89d`, `0a336e90f`,
  `522a29653`, `e48f2bdb7`, `731a8fd53`, `8f0f786f0`, `8c3afd086`,
  `6113ac845`, `12444481b`, `cc396d64d`, `1cf9b4bef`)
- Narrowed defer notes: interval direction, CLI MIR, interval algebra
  (`0a336e90f`, `5232ec6cf`, `8c3afd086`)
- Extern trust verification, Go status defer, stream sequencing defer, sized
  numeric defer, scrinium Go shim defer, captured closure defer
  (`241d62b0c`, `fb588d1fa`, `e77ea2bbd`, `21db0fcdf`, `bdf7924eb`,
  `755d3e0e`)
- Deferred CLI MIR refresh, sparse MIR refresh, JSON build blocker reframe
  (`28ea0f3c8`, `d98236194`, `460ff5c6c`)
- Resolved deferred audit batch closeout (`5c02503c7`)

### Other changes

- **Faber runtime script campaign:** add Faber script runtime campaign
  (`111a8d790`)
- **Unified lookup delivery:** add unified lookup delivery (`0b54584a7`)
- **Go and TS e2e exempla campaigns:** add factory docs for Go and TS e2e
  exempla campaigns (`ab67c9519`), file-interface campaign closeout
  (`940fe3723`)
- **Type-call constructor clean break:** close type-call constructor clean break
  goal (`b2ab4b0dd`)
- **Faber runtime extraction:** bridge runtime valor extraction from exempla
  (`2616475da`)
- **Document reader locale pack upkeep** (`bdd03e0ff`)
- **Numeric trap defer closeout** (`0430a3754`)
- **Unify stepper coverage traps** (`f3cc3265e`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
