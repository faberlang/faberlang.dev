+++
title = "Radix 0.35.0"
section = "releases"
order = 62
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.35.0 |
| **Tag** | `radix-v0.35.0` |
| **GitHub** | [radix-v0.35.0](https://github.com/faberlang/releases/releases/tag/radix-v0.35.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.35.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.35.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.35.0/radix-v0.35.0-aarch64-apple-darwin.tar.gz) | 992.8 KB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.35.0/radix-v0.35.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.35.0/radix-v0.35.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.35.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

Minor release spanning 69 commits across the compiler front-end, standard library,
and package tooling. Introduces `sponte`/`fixus` declaration markers with `T ∪ nihil`
nullable union syntax (phases 0-7), completes the `⇢`-only cast spelling convention,
narrows the keyword surface to canonical forms, and adds target-neutral `norma`
library import resolution with JSON/TOML runtime value groundwork.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 69 |
| Date span | 2026-05-21 → 2026-05-22 |

### Major tracks

#### sponte/fixus declaration markers + T ∪ nihil (phases 0-7)

The largest track this release. `sponte` (opt-in) and `fixus` (late-init) declaration
markers replace the old `si`-prefix convention for optional declarations. The
`T ∪ nihil` inline union syntax supersedes `si T?` as the nullable type form.

- Phase 0-2: planning, inventory, lexer/parser/AST shim + bridge (`a2b79f823`)
- Phase 3: semantic lowering with review feedback (`8b93cd523`, `af1c52e55`)
- Phase 4: Rust codegen support for declaration markers (`eadae9a6f`)
- Phase 5: migrate examples, stdlib sources, and test fixtures (`7f649e434`)
- Phase 6: explain union doc item and teaching docs (`fd226e0da`, `cb74f8fb2`)
- Phase 7: guardrails, validation, and residue clean-up (`69b70742a`, `a754af7c4`, `6656f6f9a`)
- Fixes: nullable genus field defaults (`e09c14e78`), nullable cast doc example (`678ba9e45`),
  exempla nullable cast syntax (`d772c192c`), Rust `verte` struct emission (`aac89d508`),
  tightening compiler correctness gaps in parser/typecheck/codegen (`19713f8a3`)

#### Verte alias clean break

`⇢` is now the sole postfix cast spelling. All ASCII and Latin aliases removed
from compiler source, tests, and teaching documentation.

- Planning and scope (`2628ace2f`, `6d56509a7`, `d9ba2c714`)
- Phases 2-4: rewrite all test aliases, update EBNF/grammatica, negative tests + residue guardrails (`f186727aa`)

#### Language-surface narrowing

- **`nota`** is the canonical diagnostic statement; legacy `scribe` exempla renamed and all docs migrated (`91ac588b0`)
- **Inline exit keywords removed**: `moritor`, `reddit`, `tacet` no longer recognized; all sites migrated to `si … ergo redde` / `nota` forms (`ef358728c`)
- **Runtime conversion keyword aliases removed**: `bivalentum`, `fractatum`, `numeratum`, `textatum` eliminated in favor of `verte` + `⇢` (`5ab6b4a04`)
- **Test grammar**: test names required before modifiers; modifier-only syntax rejected (`96339ecae`)

#### Contextual keyword inventory

Phase 0-1 of contextual keyword scope analysis: exhaustive keyword classification
(852-row ledger) plus lexer test additions for every keyword token (`67468af13`,
`c44e0c684`, `d9ba2c714`).

#### Stdlib canonicalization and HAL documentation

- Function return arrows normalized from ASCII `->` to Unicode `→` across all 21 stdlib source files (`e50ac0039`)
- Nullable types and arrow forms canonicalized in `innatum/`, `hal/`, and top-level contracts (`9f599f109`)
- Transaction single-row query form added to `norma::hal::arca` (`95c113818`)
- Documentation resolutions: `nuncius` receive (`eb0511860`), `caelum` socket (`21131e28f`),
  HTTP async-only (`ac72f6f72`), `processus` execution (`9f14cfcdb`), `solum` line collection
  (`dfa8ce58c`), `arca` single-row retrieval (`c671aaee7`)
- Latin conjugation and async-generator policies recorded (`ad4c2a250`, `c0362e1f5`,
  `b518c68bc`, `5c9307cec`); thesaurus messages use real future plural (`2651d5ddd`)

#### Target-neutral library import resolution

- `faber` discovers built-in `norma` modules directly from the stdlib path (`c9a66e80b`)
- `norma::hal::consolum` imports backed by Rust runtime, with typechecked call lowering (`4443151bc`)
- Target-neutral resolution pipeline: inventory, import graph, and resolver integration (`82fea23ad`)

#### Stdlib data format integration (JSON + TOML)

- Planning and narrowing to JSON + TOML (`142324af7`, `846b136bf`)
- Phase 0: baseline ledger for `json.fab`/`toml.fab` (`33b2956ec`)
- Phase 1: TOML front matter parser support for explain corpus (`88393ac9f`)
- Phase 2: `datum::Valor` — canonical runtime data value with serde_json/toml adapters (`3b0c3df6f`)
- Phase 3: type/call bridge — `Primitive::Valor` wired through type system, codegen, and method call lowering (`36ef1388b`)

#### TOML front matter corpus migration

The `explain/` corpus and teaching docs migrated to TOML front matter:

- Phase 0: baseline (`5ef705f26`)
- Phase 1: TOML parser support (`88393ac9f`)
- Phase 2: corpus migration — 167 files (`024986637`)
- Phase 3: docs migration (`cede93ea0`)
- Phase 4: residue cleanup (`49f818b76`)
- Phase 5: validation and closeout (`206de5eb7`)

### Other changes

- Factory planning artifacts removed after completion (`780bc1e94`)
- Release preparation and tag (`bdf18d450`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
