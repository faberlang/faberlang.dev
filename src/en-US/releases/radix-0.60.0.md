+++
title = "Radix 0.60.0"
section = "releases"
order = 37
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.60.0 |
| **Tag** | `radix-v0.60.0` |
| **GitHub** | [radix-v0.60.0](https://github.com/faberlang/releases/releases/tag/radix-v0.60.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.60.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.60.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.60.0/radix-v0.60.0-aarch64-apple-darwin.tar.gz) | 1.9 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.60.0/radix-v0.60.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.60.0/radix-v0.60.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.60.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

Synthetic tag spanning **178 commits** between v0.59.0 (indexed tensor types) and
this consolidation point. Crate manifests remain at `0.38.0` throughout this
range — this tag documents the historical release consolidation: the **forma formatter** extraction and closure, **mathesis** numeric operator library,
**tensor** type sugar and arithmetic family, **LLVM staging** for GPU-ready IR
lowering, **chorda** morphologia alignment, **numeric value equality** operators,
**transitive library imports** with CSV v1, **tempus** stdlib, **DEFER-049**
method call resolution, batch DEFER completions, and a major deferred-item
documentation restructuring.

### Scale
| Signal | Count |
| --- | ---: |
| Commits (no merges) | 178 |
| Date span | 2026-06-28 → 2026-06-29 |

### Major tracks

#### Forma formatter: extraction, SC-10 closure, and verification

The Faber formatter is extracted from the compiler into `crates/forma` as an
end-to-end crate, with shared author gates, per-family tests, and verification
evidence capture. The SC-10 author idempotency round-trip ratchet is raised to
230/252 corpus acceptance. The formatter is applied to the stdlib, and the
`faber-cli format` command preserves frontmatter. Verification scripts
(`scripta/verify-faber-format-run`) and ledger documentation close out the
forma factory campaign.

- Extract formatter into `crates/forma` end-to-end (`0953bedb4`)
- CI green, ratchet 230/252, ledger sync (`d7cec83de`)
- Close SC-10 author idempotency and raise round-trip ratchet (`79ec5edb9`)
- Shared author gates, per-family tests, evidence capture (`93426077d`)
- Fix forma emit and apply faber format to stdlib (`e02034f94`)
- Preserve multiline literal blank lines (`bbb8c1723`)
- Preserve unsupported forma captures (`ea93250ce`)
- Polish canonical operator imports, emitter tests, trivia trimming,
  roundtrip failure reporting, test gate output, and author formatter
  tests (`bab73d640`, `2252ed143`, `8a171838a`, `791941e20`, `6d0230d63`,
  `f607e6b0d`, `0cecf3ca6`)
- Preserve device roles for annotated genus methods (`bee8b3b06`)
- Preserve frontmatter during format (`96214795b`)
- Add `verify-faber-format-run` script for plan steps 1–8 (`c68c74127`)
- Close RUN.md skeptic gaps and verify evidence (`2758b5b2e`)
- Make forma goal autonomous-run-ready (`88838e676`)

#### Mathesis: numeric operator library (Commits A–D)

Native Faber operator catalog with modulus, transcendental functions, receiver
methods, approximata, and shift operator morphologia (sinistra/dextra). Four
commits close out the mathesis morphology goal and DEFER-036 (method-only
approximate equality).

- Native modulus with operator catalog and constants — Commit A (`c1db97e21`)
- Transcendental native catalog in Faber — Commit B (`119b1d10c`)
- Numeric operator receiver methods and approximata — Commit C (`72677dae0`)
- Shift operator morphologia (sinistra/dextra) — Commit D (`87b42fd37`)
- Route receiver potentia through catalog when linked (`77830544e`)
- Address review — potentia parity, domain docs, test coverage (`aaad44e77`)
- Annotate internal modulus helpers with `@ privata` (`a8bdbb957`)
- Design docs, exempla, DEFER-036 closeout (`93c394189`)
- Lock minime/maxime and note operator chaining is free (`7711eaafb`)
- Prefer math-block ⋆ over Arrows ↑ for potentia glyph (`4ae5e9164`)
- Add potentia-glyph goal for ↑ exponentiation (`f749ea638`)

#### Tensor arithmetic and type sugar

Width and tensor type sugar (`f32`, `tf32[2, 3]`) lands in the semantic layer,
closing the indexed-types-foundation goal. Elementwise arithmetic family
(addita/subtrahe/multiplica) and reduction family (summa/media) ship for
`norma:tensor`. The tensor bridge runtime is renamed to structa/planata.

- Add width and tensor type sugar (`f32`, `tf32[2, 3]`) (`4170a18f6`)
- Elementwise arithmetic family (addita/subtrahe/multiplica) (`e9ee9e7aa`)
- Reduction family summa/media — Commit B (`166de4ff5`)
- Tensor applicata/summa catalog and design doc — Commit B (`ac8782dda`)
- Ship `norma:tensor` bridge catalog — Commit A (`bb93c0df7`)
- Rename bridge runtime to structa/planata (`96b4e851b`)
- Migrate exempla and retire ex/ad bridge parser fold (`e67b3df74`)
- Complete rename, route shape ops through outcome ladder (`7279fc560`)
- Migrate `shape.fab` to f32 and tf32 sugar (`313f79a4b`)
- Bring tensor-intrinsics.md current with shipped compiler surface (`98805586e`)
- Polish tensor shape unification, element gate, type rendering,
  conversio constants, and index helpers (`7ee2e7863`, `d2ee6d475`,
  `6cc958f17`, `935922597`, `ab17c9e87`, `d57a03f7d`, `af520d7a5`,
  `9a56c81f3`)

#### LLVM staging: GPU-ready IR lowering (Stages 0–5)

The LLVM staging campaign completes Stages 0–5: verifier floors, kernel
attribute annotation in MIR, leaf-strategy consolidation, and Tier E proof
delivery. Device roles are moved off `MirFunction` into `llvm_text/device`,
staging gates are split, and corpus guards are added.

- Complete campaign Stages 0–5 (verifier floors, kernel attrs, Tier E)
  (`3ef04fb2f`)
- Move device roles off MirFunction into llvm_text/device (`95234ef3f`)
- Consolidate device emit entry in llvm_text (`c7fe26252`)
- Split staging gates, corpus guards, gate script (`3dbcd8a36`)

#### Chorda morphologia: Perfectum and modulus alignment

Perfectum morphologia lands with modulus method overloads, exempla,
documentation, and verification gates. The chorda morphologia goal is
semantic-first.

- Perfectum morphologia + modulus method overloads (`f972bad9e`)
- Exempla, docs, and verification gates (`5288831d0`)
- Polish overload selection and typecheck dispatch (`7f0fa0775`)

#### Numeric value equality (`≈` `≉` operators)

Parse, typecheck, and Rust codegen for the approximate equality operators
(`≈` `≉`). Includes policy documentation, probe matrix, and exempla.

- Parse and typecheck numeric value equality (`≈` `≉`) (`a3b3f4a8d`)
- Codegen and exempla for numeric value equality (`d451e7135`)
- Numeric value equality policy and probe matrix (`513fbfa0e`)

#### Transitive library imports and CSV v1

`faber-cli` gains transitive `norma` library import closure and splice,
resolving DEFER-006 (map value iteration). `norma:csv` v1 ships with a
transitive chorda dependency. Review findings are hardened.

- Transitive norma library import closure and splice (`83242b60f`)
- Ship `norma:csv` v1 with transitive chorda dependency (`a9552c9db`)
- Harden transitive library import review findings (`e4b3910c9`)
- Resolve DEFER-006 map value iteration; clarify DEFER-001 scope (`a98485f05`)
- Polish package.rs, csv.fab, and test helpers (`bb132e158`, `f610c99ef`,
  `853aa571a`, `c7a6948a4`)

#### Tempus stdlib (time library)

Lower `textus↦instans` and nested modulus valor for tempus, enforce fixum
write-once inside stream ad arms. Close Commit A with native Faber bodies;
defer HAL effect wrappers.

- Lower textus↦instans and nested modulus valor for tempus (`b393173c6`)
- Enforce fixum write-once inside stream ad arms (`69cacbbf8`)
- Close Commit A; defer HAL effect wrappers (`897ab63f4`)
- Harden tempus-stdlib goal for native Faber only (`e5965503d`)
- Polish instans runtime: time constants and RFC3339 byte checks (`1e97f35a8`)

#### DEFER-049: Failable method calls by owner DefId

Three-phase resolution: scope modulus methods to namespace owners (Phase 1),
scope library provenance by import binding (Phase 2), resolve failable method
calls by owner DefId (Phase 3).

- Phase 1: scope modulus methods to namespace owners (`70f85f684`)
- Phase 2: scope library provenance by import binding (`fd773a260`)
- Phase 3: resolve failable method calls by owner DefId (`fadfdd7c8`)

#### DEFER batch completions and fixes

Close DEFER-055 (release atomicity), DEFER-057 (runtime hygiene coverage), and
a batch of easy deferred items (056, 035, 020, 003, 037). Fixes land for
DEFER-048 (comparison and membership emit), DEFER-050 (instans ordering and
precision), DEFER-052 (MIR typed conversio truthiness in stepper), DEFER-053
(process HAL gate on canonical module identity), and DEFER-054 (closure
return-path checks). Instans precision naming is refactored to Latin
(`cum_praecisione` → `ad_praecisionem`).

- Complete DEFER-055 release atomicity (`58e6739b9`)
- Complete DEFER-057 runtime hygiene coverage (`8ccaa262c`)
- Close easy DEFER batch (056, 035, 020, 003, 037) (`f55e89c81`)
- Fix DEFER-048 comparison and membership emit bugs (`5addc23dc`)
- Fix DEFER-050 ordering and precision bugs (`b3142efda`)
- Fix DEFER-052 MIR typed conversio and adfirma in stepper (`d8daf397b`)
- Fix DEFER-053 gate process HAL on canonical module identity (`aacfbdf03`)
- Fix DEFER-054 closure return-path checks (`3fa4ffc3f`)
- Rename `cum_praecisione` → `ad_praecisionem` (`408908e87`)
- Rename `InstansPrecision` → Latin `InstansPraecisio` (`5a6ea5a7b`)
- Polish stepper bivalens conversio truthiness, return-path reporting,
  nil equality and membership lowering, instans codegen tokens and
  nanosecond unit constants (`b942317cc`, `dd5457f3e`, `05f70f2cc`,
  `c93319219`, `cfc2b1cfe`)

#### MIR refactoring: submodule split

Split MIR `llvm_text` and `wasm_text` into submodules (~4959 insertions).
Device entry points are consolidated into the `llvm_text` root.

- Split MIR llvm_text and wasm_text into submodules (`c135a6bb1`)
- Alphabetize keyword lists within semantic groups (`e82f52905`)
- Replace production `.expect` with real error paths (`f24eb411d`)

#### Documentation restructuring and deferred-item triage

`docs/factory/DEFERRED.md` is split into individual `docs/factory/deferred/defer-NNN.md`
files (87 files, 1621 insertions, 1351 deletions). Triage notes are added for
DEFER-007–010, 012, 014–019, 024–027, 034, 039–047, 051, 058, and 059. Factory
goals are firmed up for forma, llvm-staging, tempus-stdlib, tensor shape items,
chorda, mathesis, transitive imports, and numeric value equality. Regex literal
Part B is indefinitely deferred.

- Split DEFERRED.md into deferred/defer-NNN.md files (`a365493dd`)
- Triage notes for DEFER-007–010, 012, 014–016 (`cb76d27b5`)
- Triage notes for DEFER-017–019, 024 (`94b6c1d58`)
- Triage notes for DEFER-025–027 (`6b711d35f`)
- Triage notes for DEFER-034, 039–041 (`51e64cf7f`)
- Triage notes for DEFER-042–045 (`77830544e`)
- Triage notes for DEFER-046, 047, 051 (`f7f954147`)
- Triage notes for DEFER-058, 059 (`773cd55f0`)
- DEFER-059 unifier `Type::Param` widening (`7279fc560`)
- Indefinitely defer regex literal Part B (`c40e87485`)
- Record recent review deferred items (`ac0ff90d9`)

#### Release and versioning

The `v0.38.0` annotated tag lands (manifest bump: `Cargo.toml` `0.37.0` →
`0.38.0`). `v0.38.0` release notes are added. The release scripts
(`scripta/release`, `scripta/release-build`, `scripta/verify-native-stdlib`)
are polished for the local Docker build lane.

- Release v0.38.0 (`7c5d2557c`)
- Add v0.38.0 release notes (`b49b60416`)
- Polish scripta release, build, and verify-native-stdlib scripts (`0fb43c6d9`)
- Polish validate map snapshot call helper (`ac57c2e1a`)

### Other changes

- Add per-function Why/Verb comments to native Faber stdlib modules (`2b60e9a51`)
- Extract inline radix tests and tighten hygiene budgets (`3e3bcca7b`)
- Polish method call emission: dedupe qualified calls, collapse struct
  owner type peeling, improve module method bind error spans, extract
  bind and registration helpers (`db110b9d0`, `842348d23`, `c04c37e47`,
  `bb6871b34`, `aa03b2894`, `de5b863b7`)
- Polish collection test formatting, type predicate grouping, map
  for-loop emission, rust decl helpers, breakable.rs helper ordering
  (`2bb5f182d`, `96082481e`, `b7cdaf030`, `7f9737bfe`, `c1405bc9f`)
- Polish exempla corpus: full `+++` frontmatter and index linkage
  (`d496de19f`)
- Polish lower/control map iteration helpers and array type prep
  (`0130b17d8`, `daa8b34dd`, `006314e77`)
- Polish native-civil probe layout, tempus.fab section comments, and
  tempus-civil exemplum incipit layout (`ec3952e63`, `ff99bcc84`,
  `3be33728d`)
- Polish faber hygiene test `scan_config` naming (`1bfe276bd`)
- Run `cargo fmt` after stdlib merge and after llvm_text probe edits
  (`807eac8f2`, `d73eac187`)
- Fix `scripta`: pass command to docker create for scratch release images
  (`2eef431db`)
- WIP foreign session changes (codegen/wasm/llvm/typecheck refactor)
  (`c40f904ef`)
- Docs: bring tensor-intrinsics.md current, record recent review
  campaign, close transitive-imports and numeric-value-equality ledgers

---

[All releases](/releases/) · [Install the current release](/start/install.html)
