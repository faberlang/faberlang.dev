+++
title = "Radix 0.18.0"
section = "releases"
order = 81
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.18.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

Substantial standard library expansion — new HTTP, serialization, database, and
string modules — alongside collection-type morphology validation, receiver
ownership inference, and per-target helper library support.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 33 |
| Date span | 2026-01-07 |

### Major tracks

#### Standard library: new modules

- **caelum** — HTTP client (`pete`, `mitte`, `pone`, `dele`, `muta`, `roga`)
  and server (`exspecta`, `Servitor`) with `@ futura` async annotation
  (`074d16694`)
- **arca** — Database adapter protocol with `Connexio`/`Transactio` pacta,
  TypeScript PostgreSQL and SQLite drivers (`6fc5f8364`)
- **forma** — Serialization/deserialization: `solve(valor, "json")` → `octeti`,
  `pange(bytes, "json")` → `T`; supports JSON, YAML, TOML, CSV
  (`4c343d66e`)
- **textus** — String methods (`longitudo`, `sectio`, etc.) and type
  propagation for string codegen (`4fbf01ab8`)
- **numerus** / **fractus** — Math operations (`absolutum`, `signum`,
  `rotunda`, etc.) and float literal typing fix (`f02c386d7`)

#### HTTP API consolidation

- Rename `responsum`/`rogatum` → `Replicatio`/`Rogatio` to avoid collision
  with the language-level `Responsum` async protocol (`4c084a545`)
- Simplify server API: `exspecta(handler, port)` replaces
  `creaServitorem()`+`exspecta()` (`1f7c05467`)
- Remove convenience response builders (`replica`, `replicaJSON`,
  `replicaErrorem`); keep only `replicatio(status, capita, corpus)` for full
  control (`459da8246`)
- Remove `peteCum`/`mitteCum` convenience methods; use `roga(modus, url,
  capita, corpus)` instead (`a04b0d07a`)

#### Collection types: morphology validation and codegen

- Add `@ radix` annotations to collection methods (lista, tabula, copia,
  solum, aleator) for morphology/behavior alignment (`e93755f75`)
- Rename methods to match perfectum semantics: `selige`→`selecta`,
  `omit`→`omissa`, `confla`→`conflata`, `misce`→`miscita` (`e93755f75`)
- Add receiver ownership inference from verb morphology: imperative/future
  indicative → `in` (mutable), perfectum → `de` (immutable) (`521676930`)
- Add Latin morphology validation (morphology.ts) wired into all 5 codegen
  targets (TypeScript, Python, Rust, C++, Zig); invalid forms emit warning
  comments (`e2944c58b`)
- Add collection helper libraries for Rust and C++ targets to replace complex
  inline lambdas in codegen templates (`6520dede3`)
- Fix parameter substitution bugs where single-param templates with multiple
  `§` references relied on auto-increment instead of explicit `§0`
  (`2e3387827`)
- Add missing parameter and return types to mathesis (21), solum (27), and
  tempus (5) stdlib functions (`f8003c61b`)
- Update test coverage: 27 new lista cases, 7 new tabula cases
  (`b0eb879f4`)

#### Support libraries per target

- TypeScript: full HTTP client/server implementation using fetch API and
  Node.js http module (`d8d673e9c`)
- Rust and Zig: compile-time stubs (`unimplemented!()` / `@compileError`) with
  clear messages (`ec18ed93a`)
- Python: runtime stub raising `NotImplementedError` (`98b266bee`)
- C++: runtime stub throwing `std::runtime_error` (`6df23fc65`)

#### Semantic analysis and type propagation

- Cross-module type propagation for codegen: fix `dicserne` pattern alias for
  variant field access, fix `EgoExpression` to resolve enclosing genus,
  restrict mathesis constant lookup to zero-arg functions (`4fbf01ab8`)
- Add `textus` as a primitive type in the codegen translation layer with
  property mapping (`longitudo` → `length`) (`4fbf01ab8`)
- Infer float literals as `fractus` type in semantic analysis (`f02c386d7`)

### Other changes

- Regenerate norma registry from updated stdlib specs (`3964f8a54`,
  `0b7b5d09e`)
- Add stats generation script (`scripta/stats.ts`) for README automation
  (`7e30c3b2b`)
- Add project statistics table to README (`d0a6d26e9`)
- Restructure `AGENTS.md` with elevated CRITICAL RULES section
  (`e48be0f00`)
- Update docs for renamed stdlib methods across 9 documentation files
  (`842329415`)
- Add `@ proprietas` design proposal for property-style access
  (`dd07b8b0b`)
- Add `test-fixer` and `typescript-fixer` agent configurations
  (`b0eb879f4`, `b7dcc2b24`)
- Add brief test data for agent evaluation (`4a106b190`)
- Fix strict null checks across test and script files (`cb4a78ec7`)
- Style cleanup in faber compiler tokenizer and assignment expression
  (`0aba080ca`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
