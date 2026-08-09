+++
title = "Radix 0.56.0"
section = "releases"
order = 41
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.56.0 |
| **Tag** | `radix-v0.56.0` |
| **GitHub** | [radix-v0.56.0](https://github.com/faberlang/releases/releases/tag/radix-v0.56.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.56.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.56.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.56.0/radix-v0.56.0-aarch64-apple-darwin.tar.gz) | 1.9 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.56.0/radix-v0.56.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.56.0/radix-v0.56.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.56.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

Mid-sized release spanning **76 commits** (`v0.55.0..v0.56.0`). The tag theme is
*Conversio/instans/valor: primitive carriers, temporal HAL retyping, valor
extraction, failable recovery.* Three interlocking deliverable groups landed in
rapid succession: the **instans** absolute-time primitive replaces `Valor::Tempus`
and retypes the temporal HAL wall-clock surface; **valor extraction** ships
`FromValor` for scalar and aggregate carriers; and the **conversio** (`↦`)
surface reaches near-complete coverage across primitive, collection, and tensor
element-width arms — backed by a failable-recovery rewrite from `vel` to `⇥`
with declared `err_ty` support in Rust codegen.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 76 |
| Date span | 2026-06-27 → 2026-06-28 |
| Files changed | 151 |
| Lines inserted | 10,692 |
| Lines deleted | 1,126 |

### Major tracks

#### Instans primitive (Commits A/B/C)

- **Commit A — primitive, carrier rename, `faber::Instans`:** Add `instans` /
  `instans<ms|us|ns>` to the type system with `InstansPrecision` lowering,
  Rust codegen to `faber::Instans`, and rename `Valor::Tempus` → `Valor::Instans`
  across faber, norma, and stdlib TOML paths. (`a1ed38859`)
- **Commit B — lattice, conversio, valor extraction:** Coarse→fine precision
  assignability, explicit `instans↔instans` ↦ via `with_precision`, valor ↦
  instans lowering through `Instans::try_from_valor`, and conversio-target
  lowering that preserves `instans<ms|us|ns>` precision. (`d9602f26a`)
- **Commit C — HAL retypes, offset ingest, comparison, emit:** Retype tempus
  wall-clock verbs to `instans<N>`, extend RFC3339 parse to normalize numeric
  offsets to UTC, add cross-precision comparison, and `instans ↦ textus` emit
  at declared precision. Exempla and design doc included. (`f882934ee`)
- Multiple polish commits across the stack: precision lowering, HIR tests,
  driver tests for compare and wire emit, faber runtime parse/emit helpers,
  codegen helpers, and `Valor::Instans` carrier documentation. (`af128ada5`,
  `4297b431f`, `7055243db`, `74d3e4b2e`, `ad6bde525`, `024dc42ed`, `af76d8886`,
  `d59712b22`, `786c8fe07`, `f57b53455`, `ab6a58e3a`, `3341f32bf`, `499e1b4d3`)
- Fix: move instans corpus home from `tempus/` to `instans/` after the carrier
  rename left a stale path. (`b73687f6c`)
- Exempla: expand instans coverage (four precisions, HAL clock, offset ingest,
  TOML provenance, cross-precision compare, narrow/widen), register terms, and
  refresh corpus index. (`ebf79d00c`)
- Style: format `instans.rs` in faber (rustfmt layout, EOF newline). (`2b8f181f4`)

#### Valor extraction via FromValor (Commits A/B/C)

- **Commit A — scalar valor ↦ extraction:** Add `faber::FromValor` for scalar
  carriers (nihil, bivalens, numerus, fractus, textus, ascii) with dedicated
  Rust codegen arms; valor-scalaria exemplum and matrix tests.
  (`f5df68203`)
- **Commit B — aggregate extraction and genus boxing:** Add `FromValor` for
  `Vec` and `HashMap`, genus IIFE extraction with field-default policy,
  `Valor::Tabula` boxing for genus ↦ valor, and compose exempla for valor-genus
  roundtrip and valor↔tensor via lista bridges. (`e66d20773`)
- **Commit C — reject valor ∷ T and vertebra holdouts:** Typecheck now rejects
  `valor ∷ T` and vertebra valor construction; matrix rejection tests and
  conversio-valor boundary design doc. (`c8931d825`)
- Polish: split `valor_conversio.rs` into `mod`/`extract`/`boxing` submodules,
  deduplicate defaultable-field classification, and route scalar arms through
  shared `emit_from_valor_extract`. (`fd5a3e7eb`, `0cafd53c2`, `acf037389`,
  `419d37eb9`)
- Fix: defer vertebra source check for struct/map object literals so `∷` field
  context is preserved. (`a42e734a9`)
- Docs: refresh valor extraction goal after instans delivery; mark ready to
  implement with shipped numeric/collection/tensor conversio surface.
  (`0839ba4f7`, `a1b48deb7`, `d2f147e9a`, `2036156cc`)

#### Conversio coverage — primitives, collections, tensors

- **Numeric/bool Rust codegen:** `fractus`/`bivalens`/`ascii` numeric and
  truthiness lowering with driver tests and `numeric-bool.fab` exemplum.
  (`a7ced27bb`)
- **Reject ambiguous primitives:** `numerus`/`fractus`/`bivalens` ↔ `octeti`
  and `octeti ↦ bivalens` rejected at typecheck with clear diagnostics.
  (`d6dfefca2`)
- **Collection Tier 1 Rust codegen:** Eight cross-collection `↦` lowerings:
  `lista↔copia`, `lista↔tensor` (1-d), tensor flatten via `ad_lista`, tabula
  key/value projection, and eager `lista↔cursor` bridges. (`2321d9a3f`)
- **Reject ambiguous collections:** Typecheck validates allowed cross-collection
  `↦` pairs and rejects holdouts (`lista↦tabula`, `promissum` async boundaries);
  collection matrix regression suite. (`1fcb8a5d`)
- **Tensor element-width conversio:** `tensor<A> ↦ tensor<B>` lowers through
  `Tensor::convert_elements` with per-slot scalar casts. (`5a937c039`)
- **Validate tensor conversio:** Typecheck allows element-width tensor `↦`
  pairs on the numeric lattice, rejects scalar extraction and broadcast
  construction; tensor matrix regression tests. (`9c9159553`)
- **Exhaustive lattice matrix:** `tensor_element_lattice` pair enumeration
  (10 element types, 100 cells): 56 allowed, 44 rejected, 46 emit
  `convert_elements`. (`d94eb7ae1`, `83ba1a740`, `1179071d3`, `b2c4e4066`)

#### Conversio ⇥ recovery — alternate exit (Commit A phases 1–6)

- **Phases 1–2:** Move inline conversio failure recovery from `vel` to `⇥` at
  parse time with a migration diagnostic. Rename the slot from `fallback` to
  `recovery` across syntax, HIR, MIR, and backends. (`6a583300c`)
- **Phase 3:** Typecheck requires `↦ T ⇥ recovery` to unify with `T`;
  mismatches rejected at typecheck. (`e011d91e0`)
- **Phase 4:** Refresh Rust/Go/TS conversio ERROR POLICY and codegen golden
  tests for the `⇥` recovery contract. (`eb22c61ee`)
- **Phases 5–6:** Migrate conversio corpus, EBNF, README, and design docs off
  `↦ … vel …` to `↦ … ⇥ …`; trim `vel.fab` to nullish-only examples.
  (`3eeeb504e`)
- Polish: extract `parse_conversio_postfix` from the postfix loop so the ↦ ⇥
  grammar and vel migration diagnostic live in one place. (`5db23396f`)

#### Failable codegen: declared `err_ty` honored

- Emit `Result<T, E_rust>` from declared alternate-exit types, mark
  `⇥`-declaring functions failable without body evidence, type `fac`/`cape`
  and `iace` against `E`, and reject heterogeneous `?` propagation at direct
  call sites. (`7ee958f7e`)
- Multiple polish commits: shared HIR builders for throw/propagation, throw
  payload emission helper, failable prepass HIR walk, RustCodegen function
  indexing, and centralized heterogeneous-error checking. (`7e32b8ec8`,
  `0d2fd08a3`, `dd30b015f`, `bf3641dca`, `f01e45477`, `981757bbe`)
- Propagate bare conversio through `⇥` and `fac`/`cape` (Commit B): bare `↦`
  without inline `⇥` now lowers to `?` when the emission context permits
  propagation. (`8688bfe4c`)

#### AIR architecture design

- Add `docs/design/air-dialect.md`: AIR is a pure-functional IR entered by
  annotation (`@ graduabilis`) that forks from HIR (alongside MIR), runs ML
  transforms (autodiff, fusion), and re-lowers to MIR for backend emission.
  Two invariants: AIR owns no backend and owns no semantics — a shape-adjusting
  detour, not a parallel IR. (`34939bd73`)

#### AI/ML language foundation vision

- Add `docs/design/aiml-foundation.md`: capture the shipped numeric + tensor
  substrate (dtype-in-types, explicit ↦ conversio, `tensor<T>` shell, valor
  compose, series/census rows, `fac`/`cape` error surface) as the
  NumPy-equivalent foundation. Open seams flagged for factory goals:
  broadcasting policy, static-shape seam, views-vs-copies, MIR
  differentiability stance, backend kernel story. (`be0f582f2`)

### Other changes

- **Fix: close DEFER-004** — repair wasm e2e and HTTP codegen test; emit Wasm
  text and binary in one paired probe, pin exempla at real Wasm tier ceilings,
  rewrite `octet.fab` without em-dash lexer failures. (`458346c62`)
- **Fix: close DEFER-030** — add shared `index_projection_result_ty` so octeti
  indexes (`lista<numerus<u8>>`) pass MIR validation and Wasm/LLVM probes.
  (`424872b71`)
- **Docs: repair zombie drift** — align repo-shape READMEs with current
  workspace layout (exempla corpus, faber-cli vs faber runtime, cista/scena/
  hosts); fix checkout commands, exempla harness names, dead links.
  (`c7a7bb847`)
- **Docs: six conversio/temporal goal specs** — draft factory goals for
  conversio-numeric-bool-coverage, conversio-collection-coverage,
  conversio-valor-extraction, conversio-tensor-coverage, instans-primitive,
  and range-primitive. (`ff3cf4a90`, `43b5b72fe`, `acbe6c321`)
- **Docs: chorda cord-filter goal** — propose `retine`/`expurga` predicate
  filtering, interval helpers, and related chorda exports with explicit
  filter-vs-clamp separation. (`e7843c3cf`)
- **Docs: DEFERRED revalidation** — close DEFER-023 (fac/cape MIR CFG),
  refresh DEFER-029, close DEFER-031 (instans-primitive), triage open items.
  (`f58e0336d`, `beff8a887`)
- **Polish:** typecheck vertebra object-literal entry path extraction
  (`f012b885e`); conversio codegen fallback helper extraction (`b82bd3020`);
  Go conversio strconv deduplication (`3923eae35`); Rust conversio narrowing
  and parse helper unification (`e940201cf`); typecheck conversio/verte helper
  structuring (`f131b014d`); conversio-vs-verte shared `from_valor` emission
  routing (`fd5a3e7eb`).
- **Style/Chore:** format radix after octeti/conversio work (`7e3b59d93`);
  format norma `toml.rs` EOF fix (`1faa44622`); lint fixes and hygiene debt
  from housekeeping (`2c2a92b82`).

### Breaking / author-visible

| Change | Migration |
| --- | --- |
| Conversio failure recovery uses `⇥` instead of `vel` | Replace `↦ … vel …` with `↦ … ⇥ …`; the old spelling emits a parse-time migration diagnostic |
| `Valor::Tempus` renamed to `Valor::Instans` | Consumer match arms and JSON/SVAL wire paths must use `Instans` |

### Verification

```bash
./scripta/lint
RUST_TEST_THREADS=1 ./scripta/test --full
cargo build --locked --release -p radix --bin radix
./target/release/radix --version   # expect 0.56.0
```

---

[All releases](/releases/) · [Install the current release](/start/install.html)
