+++
title = "Radix 0.68.0"
section = "releases"
order = 29
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.68.0 |
| **Tag** | `radix-v0.68.0` |
| **GitHub** | [radix-v0.68.0](https://github.com/faberlang/releases/releases/tag/radix-v0.68.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.68.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.68.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.68.0/radix-v0.68.0-aarch64-apple-darwin.tar.gz) | 2.8 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.68.0/radix-v0.68.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.68.0/radix-v0.68.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.68.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

Minor release spanning **321 commits** (`v0.67.0..v0.68.0`). The work behind
this tag is far broader than the tag theme "Go canonical backlog and cross-target
matrix cleanup" suggests. Seven interleaved themes—dominated by reader-locale
diagnostics localization and a systematic `cleanliness()` refactor—ran in
overlapping waves across two intense days of parallel execution.

Reconstruct the full log:

```bash
git log v0.67.0..v0.68.0 --oneline --no-merges
```

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 321 |
| Date span | 2026-06-28 → 2026-07-07 |
| Thematic tracks | 7 |
| `feat(...)` commits | ~155 |
| `cleanliness(...)` commits | 58 (11 modules) |
| `docs(...)` commits | ~40 |
| Go target commits | ~25 built features |
| TS target commits | ~24 built features |
| Reader-locale packs with templates | 7 (Latin + 6 non-Latin) |

### Major tracks

#### Theme 1: Reader-locale diagnostics localization (~87 commits, Jun 28–Jul 6)

The largest single thread in this release. The reader-locale system—which lets
diagnostics render in the user's locale—progressed from substrate through pack
schema, Latin template expansion, and full non-Latin localization coverage.

**Pack schema and activation** (`9c7a636b8`–`4926dab9a`):
- `feat(radix): add reader pack schema substrate` (`9c7a636b8`)
- `feat(radix): compile with reader pack source policy` (`43ff6e429`)
- `feat(radix): activate reader pack keyword lexing` (`4926dab9a`)
- `feat(radix): activate reader pack diagnostics` (`43ff6e429`)
- `feat(radix): report reader pack Latin fallback` (`59d2d72b1`)
- `feat(radix): resolve reader pack primitive types` (`ee09745f2`)
- `feat(radix): validate reader pack exemplars` (`4a97d7912`)

**Pack-aware diagnostic rendering** (`a505f26c2`–`44c2de92f`):
- `feat(radix): add pack-aware diagnostic renderers` (`a505f26c2`)
- `feat(radix): render reader pack diagnostic templates` (`44c2de92f`)

**Locale proof packages** (Thai, Vietnamese, Traditional Chinese):
- `feat(faber): add thai reader locale proof package` (`ee09745f2`)
- `feat(faber): prove thai canonical reader formatting` (`37a318f17`)
- `feat(faber): prove thai loop reader surface` (`8a8af2e3c`)
- `feat(faber): prove thai semantic diagnostics` (`ab2239435`)
- `fix(reader): disambiguate thai ut keyword` (`08b851c91`)
- `feat(faber): prove zh-Hant pack inheritance` (`06f822d76`)
- `test(reader): prove Arabic bidi diagnostics` (`8b1d62407`)

**Latin template expansion** (~20 commits expanding issue templates):
Sweeping across `PARSE001` through `PARSE050`, `SEM002` through `SEM018`,
AIR warnings, borrow lints, lexer templates, and semantic resolution templates.

**Non-Latin localization** (~30 commits, each localizing a diagnostic category):
Simple diagnostics, unavailable diagnostics, CLI diagnostics, conversion
diagnostics, annotation diagnostics, missing-type diagnostics, arity diagnostics,
undefined-type diagnostics, semantic-resolution diagnostics, parser type/import/
expression/parameter/declaration diagnostics, JSON diagnostics, numeral
diagnostics, keyword suggestions, type mismatches, unknown identifiers.

#### Theme 2: Code-first diagnostics pivot + e2e alignment (~14 commits, Jul 6)

A mid-range pivot that changed how diagnostics are identified: from human-reader
message text to stable **code identities**. This enabled deterministic test
assertions, cleaner reader-locale rendering, and a hygiene guard against text
escaping into non-renderer code.

**Code-first pivot** (`bad5b8821`–`a47ab9820`):
- `docs(factory): pivot reader-locale to code-first diagnostics` (`bad5b8821`)
- `feat(reader): make diagnostics normalization code-first` (`a47ab9820`)
- `feat(reader): default diagnostics to code identities` (`a47ab9820`)
- `feat(reader): explain diagnostic codes from packs` (`e6685ab95`)
- `feat(reader): add pack completeness gate` (`912fed8e6`)

**Legacy text removal** (`326122a8f`–`84f310d11`):
- `refactor(radix): remove catalog legacy message fallback` (`326122a8f`)
- `refactor(radix): remove typecheck legacy diagnostic sink` (`5fa8284c7`)
- `refactor(radix): structure HIR lowering diagnostics` (`1d15895c4`)
- `refactor(radix): structure lexer diagnostics` (`84f310d11`)

**Diagnostic text purge** (`bf31423af`–`fb289e20e`):
- `Complete diagnostic test text purge` (`bf31423af`)
  > Replace non-renderer diagnostic message/help assertions with stable
  > code, issue, and DiagnosticArg facts across compiler, package, MIR, AIR,
  > codegen, runtime, and e2e tests. Remove `Diagnostic::assertion_message`
  > and temporary catalog message rehydration helpers.
- `Keep diagnostics structured in tests` (`fb289e20e`)

**e2e alignment**:
- `test: align harness gates, e2e_harness split, and tiered scripta/test` (`956e5493f`)
- `test: align rust codegen tests with retired modulus and matrix policy` (`91107e584`)
- `test(go): classify e2e harness outcomes` (`531d33ebc`)

#### Theme 3: Cleanliness campaign + Go/TS features (~108 commits, Jul 6)

A systematic `cleanliness()` refactor pass across **11 compiler modules**,
interleaved with Go and TS feature implementation. The pattern: one or two
`cleanliness` commits (extract/shared/audit) followed by a batch of Go/TS
`feat` commits that used the newly shared infrastructure.

**Cleanliness scope coverage**:

| Module | Cleanliness commits |
| --- | ---: |
| `radix/tool` | 34 |
| `driver` | 4 |
| `reader-locale` | 3 |
| `lexer` | 3 |
| `diagnostics` | 3 |
| `radix/hir` | 2 |
| `radix/diagnostics` | 2 |
| `radix/driver` | 2 |
| `parser` | 2 |
| `radix/typecheck` | 1 |
| `radix/reader` | 1 |
| `faber-cli/package` | 1 |

**Go target features** (25 commits, selected):
- `feat(go): emit failable error signatures` (`086d37be0`)
- `feat(go): lower fac cape recovery` (`c28039136`)
- `feat(go): propagate failable statements` (`384e3f66e`)
- `feat(go): emit tensor sparsa carriers` (`bcef541da`)
- `feat(go): type closure block expressions` (`ec27f1180`)
- `feat(go): lower generic enum surfaces` (`95c18ce7f`)
- `feat(go): lower counted range iteration` (`cd1eb74dc`)
- `feat(go): lower lista intrinsic methods` (`629506896`)
- `feat(go): lower cursor generators` (`9208506a4`)
- `feat(go): extract valor maps into structs` (`a6ab09d87`)
- `feat(go): preserve regex pattern carriers` (`cd46aff50`)
- `feat(go): add instans time carrier` (`5d959ff9e`)
- `feat(go): honor instans precision text` (`7a5061fbb`)
- `feat(go): propagate scalar conversio errors` (`f9bafbb3b`)

**TypeScript target features** (24 commits, selected):
- `feat(ts): emit ambient externa declarations` (`bcef541da`)
- `feat(ts): preserve regex pattern carriers` (`d453b0640`)
- `feat(ts): emit variant constructors` (`ec27f1180`)
- `feat(ts): lower control-flow statements` (`cfff9f0b0`)
- `feat(ts): lower collection and numeric methods` (`71c43f171`)
- `feat(ts): lower tensor conversions` (`0dc0b39ec`)
- `feat(ts): normalize optional nullability` (`92248d7aa`)
- `feat(ts): lower failable alternate exits` (`3fdc5797b`)
- `feat(ts): support local importa modules` (`dd58b00f8`)
- `feat(ts): widen primitive comparisons` (`674f6ec3e`)
- `feat(ts): emit frame runtime helpers` (`8f887e62f`)

**Fixes interspersed**:
- `fix(go): preserve breakable fac scopes` (`f3e7a14ab`)
- `fix(go): suppress unreachable failable fallthrough returns` (`bc94155a9`)
- `fix(parser): preserve statements after minimal imports` (`e5bc3eabf`)
- `fix(hygiene-ratchet): scrubber lifetime handling + tighten budgets` (`1dea4abea`)

#### Theme 4: Core stdlib cleanse + Go/TS matrix (~40 commits, Jul 6)

A parallel thread eliminating stdlib externa, purging diagnostic text from
non-renderer code, building the script-runtime bridge, and covering Go/TS
matrix gaps discovered during the cleanliness campaign.

**Stdlib cleanse** (`92208bfb8`–`1452314cd`):
- `Complete core stdlib source cleanse stage` (`92208bfb8`)
- `Record core stdlib externa ratchet` (`1452314cd`)
- `feat(ts): emit ambient externa declarations` (`bcef541da`)
- `feat(go): elide unused externa declarations` (`a7adebc97`)
- `feat(go): elide flat norma imports` (`bc94155a9`)

**Script-runtime bridge** (`de51bbde2`–`24b9dc06f`):
- `docs(core-stdlib): record interpreted norma:* host bridge dependency` (`de51bbde2`)
- `feat(faber-cli): bridge interpreted norma:* imports to stepper kernels` (`2905a8744`)
- `feat(faber-cli): add \`faber script\` interpreted-source command` (`06287227a`)
- `docs(script-runtime): record Stage 0 delivery baseline` (`6b26a783c`)

**Matrix documentation**:
- `docs(factory): baseline go e2e matrix` (`1801a71a0`)
- `docs(factory): capture ts e2e baseline` (`f86a5a614`)
- `docs(factory): plan ts e2e harness retrofit` (`9bba0fe68`)
- `docs(factory): ready go and ts e2e campaigns` (`3db35ced0`)

#### Theme 5: Polish campaign + test infra (~20 commits, Jul 6–7)

Focused extraction of shared test infrastructure into a `test_support` crate,
consolidating helpers from driver, parser, MIR, codegen/rust, package, and
diagnostic tests.

**test_support extraction** (`27e64d6c8`–`bb118d84b`):
- `radix: extract crate test_support and migrate driver diagnostics helpers` (`27e64d6c8`)
  > Add `#[cfg(test)]` test_support with shared session, compile, diagnostic,
  > and temp-dir helpers. Driver tests use `test_session` and shared
  > `assert_compile_fails_*`; diagnostic tests use
  > `assert_diagnostic_args_eq` for normalized arg contracts.
- `radix: migrate legacy_message checks to test_support helper` (`261247e9a`)
- `radix: consolidate codegen/rust test compile helpers` (`136eaf43f`)
- `radix: consolidate MIR target-text test compile helpers` (`49147db9f`)
- `radix: consolidate parser test helpers and test_span usage` (`11acd7c47`)
- `faber-cli: extract package reader-locale render text contracts` (`08aa901a0`)
- `faber-cli: harden package MIR shared imports` (`e22cf410a`)

**Polish passes** (concurrent with test infra):
- `polish(parser): centralize mod_test helpers in test_support` (`8250158d3`)
- `polish(faber-cli): dedupe package render contract helpers` (`bb118d84b`)
- `polish(mir): document llvm_text_test and dedupe exempla analyze` (`20cf88267`)
- `polish(radix): clarify test_support helper boundaries` (`17b6ca526`)
- `polish(agents): tighten AGENTS.md for faster agent orientation` (`cfa0d61cb`)

**Exempla e2e ledger**:
- `test(exempla): add ts e2e expected ledger` (`34b6567d4`)

#### Theme 6: Docs cleanup + housekeeping (~12 commits, Jul 7)

Clean-up work: archived stale design proposals, modernized the docs tree,
added scripta tooling for housekeeping, and tightened lint/audit gates.

**Design archive and doc tree** (`452572c4b`–`f204bfb35`):
- `docs: split language design from stdlib and archive stale proposals` (`452572c4b`)
  > Move Norma method ledgers and stdlib policy to `docs/stdlib/`. Move
  > superseded frame sketches and unshipped type proposals to
  > `docs/design/archive/` with factory goals as the canonical proposal path.
- `docs: remove design archive and refresh stdlib ledgers` (`f204bfb35`)
- `docs: fix stdlib externa zombie, document reader-locale and custodi` (`c72e0622d`)

**Scripta tooling** (`bb78eaf1d`–`56ee577a7`):
- `scripta: quieter lint, safe rg wrapper, Python 3.9 exempla index` (`bb78eaf1d`)
- `scripta: add EBNF vocabulary audit to lint output` (`9f4351b5b`)
- `scripta: move EBNF vocabulary audit to static gates` (`38b4d63e5`)
- `scripta: audit exempla +++ frontmatter coverage` (`56ee577a7`)
- `scripta: advisory LLVM test coverage for housekeeping` (`38b4d63e5`)
- `scripta: add advisory diagnostic-identity audit for housekeeping` (`1f6f6d691`)
- `scripta: add factory goal status drift checker` (`32de0d142`)

**Hygiene and lint**:
- `fix(hygiene-ratchet): scrubber lifetime handling + tighten budgets` (`1dea4abea`)
- `chore: ignore *.profraw files (rust test artifacts)` (`6ab6833ec`)
- `chore: gitignore local .timing benchmark artifacts` (`e93ab407e`)
- `chore: fix workspace clippy warnings` (`ccb582abe`)

#### Theme 7: Coreutils + HIR matrix + Solum (~40 commits, Jul 7)

Three subthreads that landed in the final push: the coreutils package (utility
implementations for the `faber script` runtime), the HIR target coverage
classifier, and Solum bridge helpers.

**Coreutils package** (29 commits):
- `feat(coreutils): land scaffold and echo substrate` (`702d80ce8`)
- `feat(coreutils): add basename and dirname slices` (`e6038c6a0`)
- `feat(coreutils): extend tier zero slices` (`966f5b410`)
- `feat(coreutils): add printf and seq slices` (`53dc2073f`)
- `feat(coreutils): unblock stdin slices` (`fc83bc36e`) — enabled stdin-based
  utilities (`tee`, `paste`, `grep`, `tr`, `sort`, `cut`, `expand`, `unexpand`,
  `fold`, `nl`, `tac`, `uniq`, `tail`, `wc`)
- `feat(coreutils): extend head and tail counts` (`df298fd3e`)
- `feat(coreutils): extend sort and uniq comparisons` (`5ac05742f`)
- `feat(coreutils): extend grep and tr options` (`23a6a887d`)
- `feat(coreutils): extend seq and expand options` (`75cdfec0e`)
- `coreutils: expand/unexpand comma/list finite tab stops (Stage 4)` (`294a2be79`)
- `feat(coreutils): add yes, pwd, printenv, cksum, and od stepper slices` (`ea262bde7`)
- `feat(coreutils): add comm join and split slices` (`75cdfec0e`)
- `feat(coreutils): add file utility slices` (`dbcf1a603`)
- `test(coreutils): add inline proba coverage` (`50aff925c`)

**HIR target classifier** (`f15a5ee9e`–`3967da355`):
- `docs(factory): add proposed HIR target coverage matrix goal` (`f15a5ee9e`)
- `docs(factory/hir-target-matrix): add baseline and phase delivery specs` (`2b9b39378`)
- `Complete Phase 1: HIR classifier module with target enum and classification` (`3967da355`)

**Solum bridge** (`dcf77db53`–`64518a99c`):
- `feat(solum): add stage five bridge helpers` (`dcf77db53`)
- `feat(solum): bridge file mutation verbs` (`50a94198e`)

### Breaking / author-visible

No breaking changes in this release. The code-first diagnostics pivot changes
the text of emitted diagnostics, but naming, structure, and code fields remain
stable.

### Verification (pre-release)

Recorded on the release commit (`v0.68.0`):

```bash
# Lint gate
./scripta/lint

# Full test suite (single-threaded for LLVM link-and-run safety)
RUST_TEST_THREADS=1 ./scripta/test --full

# Release build
cargo build --locked --release -p radix --bin radix

# Version check
./target/release/radix --version   # expect radix 0.68.0
```

Notes:
- Reader-locale pack tests require installed packs; the `installed_` test group
  validates all 7 locale packs load correctly.
- LLVM host link-and-run fixtures are not parallel-safe on this host; use
  `RUST_TEST_THREADS=1` for the full exempla lane.
- The code-first diagnostics hygiene guard rejects diagnostic text assertions
  outside renderer and reference output contracts.

### Publish

1. Push `main` (includes this notes file and version bump).
2. Annotated tag: `git tag -a v0.68.0 -m "Radix v0.68.0"`
3. Push tag: `git push origin v0.68.0` (triggers `.github/workflows/release.yml`)
   or `workflow_dispatch` with tag `v0.68.0`.

---

[All releases](/releases/) · [Install the current release](/start/install.html)
