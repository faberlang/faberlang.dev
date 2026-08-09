+++
title = "Radix 0.39.0"
section = "releases"
order = 58
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.39.0 |
| **Tag** | `radix-v0.39.0` |
| **GitHub** | [radix-v0.39.0](https://github.com/faberlang/releases/releases/tag/radix-v0.39.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.39.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.39.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.39.0/radix-v0.39.0-aarch64-apple-darwin.tar.gz) | 1.3 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.39.0/radix-v0.39.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.39.0/radix-v0.39.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.39.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

Marker tag spanning the Norma HAL expansion (HTTP client, tempus clock/sleep,
aleator randomness), library import provenance metadata, MIR enum/const/pattern
lowering, and the first wave of LLVM and Wasm codegen phases.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 73 |
| Date span | 2026-06-02 → 2026-06-04 |

### Major tracks

#### Norma HAL expansion

- **HTTP client runtime**: `hal/http.rs` backed by `ureq`, with a tightened
  stdlib interface (`stdlib/norma/hal/http.fab`) and Radix codegen bridge that
  lowers `norma:hal/http` calls to the Rust runtime (`0832baa86`, `4a5fd1859`,
  `7dcb6a322`).
- **Tempus (clock/sleep)**: `hal/tempus.rs` exposing wall clock, monotonic
  clock, process uptime, async dormiet, and millisecond duration constants;
  `destina`/`repete`/`siste` gated behind `@ nondum` (`7aea83903`).
- **Aleator (random)**: `hal/aleator.rs` with subsidia-backed
  fractum/sortire/octetos/uuid/semina, plus YAML Valor ABI migration that
  pushes `yaml.rs` through `TryFrom`/`try_to_yaml` via `norma::datum::Valor`
  (`0cab42ab9`).
- **Nondum availability annotation**: `@ nondum` gating syntax, parser,
  semantic availability check, and `faber check` enforcement so HAL stubs
  yield clear diagnostics (`012d371cd`).
- **Promissum/cursor lowering and HAL type alignment**: semantic
  `Type::Promissum`/`Type::Cursor` variants; `series` → `tabula<textus, valor>`;
  `arca` bind params → `lista<valor>` (`3610b8f75`).
- Factory plans and exempla for the HTTP HAL, aleator, and the general HAL
  expansion pattern (`4f77f1c3f`, `a71eff9a5`, `f651690c0`, `dfa2662d6`,
  `d41ea9efa`, `bb795e1b8`).

#### Library import provenance

- **Provenance analysis**: HIR nodes carry which `norma` library (e.g.
  `norma:hal/http`) an import originates from. The analysis propagates through
  the compiler front-end (`e965c840d`).
- **Bridge by provenance**: Rust codegen routes calls to the correct runtime
  symbol by provenance rather than string-matching call paths (`3fe3acc0c`).
- **Metadata-driven linkage**: The `faber` package layer reads library metadata
  to drive runtime symbol resolution, replacing ad-hoc path matching
  (`0018923f9`).
- **Provider syntax**: Stdlib imports hard-cut to `@ subsidia rs` provider
  syntax (`b4b21aeb1`).
- **Solum provenance test**: proves `norma:solum` linkage through the full
  provenance pipeline (`32bc84c09`).
- **Runtime method symbols**: Package metadata encodes method arity and symbols
  so generated code maps `tempus.*` verbs to `sleep`, `clock` etc.
  (`14c6f8909`).

#### MIR lowering (enum, const, pattern)

- **Top-level consts**: Lower constants into entry MIR so they appear in the
  MIR image (`b646c1658`).
- **Unit variant discerne**: Lower `discerne` on unit variants to MIR dynamic
  switch (`1ec11b2c2`).
- **Payload discerne patterns**: Lower destructing `discerne` with payload
  bindings (`13c235d86`).
- **Enum paths and inter membership**: Lower qualified enum paths and
  `est inter` membership checks to MIR (`6afade453`).
- **Filtrata/mappata**: Lower list `filtrata`/`mappata` via synthetic closure
  functions and indexed loops. Harness 75/101 MIR lowered (was 72), 74
  runnable (was 71) (`0d3b97650`).
- **Nested collection callbacks**: Preserve MIR for collection callbacks that
  contain nested collection intrinsics (`88de16dd5`).

#### LLVM codegen (phase 002–008)

- **Exempla e2e harness**: LLVM target runner in the exempla e2e suite
  (`2a4ab115c`).
- **Scalar operations**: Arithmetic, comparison, and type operation coverage
  with `scalaria.fab` exempla (`aa0ed33c5`).
- **Scalar CFG and calls**: Direct scalar calls and CFG lowering
  (`5185b9a55`, `d74a457a7`).
- **Scalar switches**: LLVM `switch` emission for discerne patterns, including
  failable control flow (`966ba9a88`).
- **Nullable operations**: LLVM lowering for nullable (`?T`) operations
  (`d50f9cfe7`).
- **Handle ABI lowering**: Text aggregate handle ABI and `promissum`/`cursor`
  handle types (`f16db2930`).
- **Runtime calls**: Lower runtime intrinsic calls to LLVM (`702ff8cc1`).
- **Entrypoint symbol**: Named LLVM entrypoint (`aa6bcbe1b`).
- **Verifier policy**: LLVM IR verifier integration (`3b5bddd95`).
- **Option operand projections fix**: LLVM `Option` operand field projections
  (`aa658f705`).

#### Wasm codegen (phase 022–028)

- **Phase 022**: In-process wasmtime instantiation harness with compile-valid
  bucket classification (`3aaa5abfb`).
- **Phase 023**: Default-value Wasm import stub host; all compile-valid
  exempla reach instantiate-valid (`655765e53`).
- **Phase 024**: Export incipit entrypoints and harness run tiers with
  behavior fixtures (`609f0aced`).
- **Phase 025**: Runtime collection MIR and Wasm emission for array stdlib
  methods (primus, ultimus, inversa, inverte, ordinata, appende); `innatum`
  reaches compile-valid Wasm 72/101 (`331400b1a`).
- **Phase 028 adjunct**: Wasm option map union shapes emitted from MIR
  adjunct (`3d475a012`).
- **Optional member correctness**: Wasm optional member handling advanced
  (`07bdce389`).

#### Itera `ab` range syntax

- Refactor range syntax from `pro` to `ab`: `ab 0 usque 10` replaces
  `pro 0 usque 10`, with lexer/parser/HIR/MIR/codegen/cross-target changes
  across 41 files (`01d767caa`).
- Latin naming boundary enforced so `ab` keeps Latin mode naming (`805c8f21e`).

#### Language and naming boundary

- **Contextual keywords as identifiers**: `parse_contextual_ident` driven by
  `KeywordOwner` policy allows `solum`, `argumenta`, `publica`, `incipiet` in
  pactum declarations and parameter positions (`2107735dc`).
- **Naming boundary alignment**: Compiler enum variants renamed to match Faber
  source markers (`de`/`in`/`ex`, `privata`/`publica`); parser-level enums
  aligned, semantic/MIR families kept English (`62a012fff`).

#### Stdlib hygiene

- HIR lowering tracks lexical type parameters in function/genus/pactum/discretio
  signatures so `innatum` specs use `T`/`K`/`V`/`U` without spurious unknown-type
  errors. Stdlib fixes across `tempus`, `innatum` (copia, lista, tabula, textus),
  `yaml`, and `nuncius` (`6b1e4e1bf`).

### Other changes

- **CLI restructuring**: `faber` commands split into `init`, `explain`, `run`,
  `test` modules (`beb601adc`). `radix` tool commands split into focused
  submodules (`d901e0de9`). Both aligned with operator-cli help/layout patterns
  including LLM-oriented `after_long_help` markdown (`975bc5075`).
- **Handoffs runner**: `handoffs/handoff.sh` spawn/list/status/kill/attach/log
  with `+++` TOML front-matter parsing and migrated handoff specs
  (`f0a9bfb66`).
- **Exempla e2e harness**: Monolithic `exempla_e2e_test.rs` split into
  per-target modules (rust, go, ts, wasm) with shared types
  (`505e1dba7`).
- **Docs**: Pruned historical factory/epic artifacts (`832c8b8c4`). Refreshed
  Wasm/LLVM factory plans (`b844b5846`). Expanded README with multi-target
  codegen orientation (`88cd51d4b`, `9a5dd996d`, `d93fef284`). Documented
  llvm-mir continuation, wasm-mir continuation, futura proba delivery plan,
  and library provenance validation gate (`a8af99714`, `b6b79b40a`,
  `0da78e44a`, `a0a60f316`).

---

[All releases](/releases/) · [Install the current release](/start/install.html)
