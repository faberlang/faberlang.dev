+++
title = "Radix 0.23.0"
section = "releases"
order = 76
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.23.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

Release spanning **77 non-merge commits** (`v0.22.0..v0.23.0`, 2026-01-13 → 2026-01-15). This release delivers a complete CLI framework with codegen, the HAL `@subsidia` layer with full TypeScript codegen, a major Go codegen expansion for Rivus (control flow, tagged unions, expressions, error returns), `discretio`/`discerne omnia` exhaustiveness enforcement across faber and Rivus, post-function modifier support including `exitus` exit-code semantics, a Norma builtin-type reorganization, and a comprehensive exempla reorganization with Latin naming.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 77 |
| Date span | 2026-01-13 → 2026-01-15 |

### Major tracks

#### CLI framework with TypeScript codegen

- **Path-based nested subcommands** (`#156`): `faber/cli.ts` gains recursive subcommand resolution via the parser's `exClause` annotation syntax. (`ae10a8852`, `0a0f6cd45`)
- **Module-based command groups** (`#157 phase 2`): a CLI detector/resolver pipeline (`fons/faber/codegen/cli/`) discovers command modules and generates grouped subcommands. (`f93ff8b25`)
- **Help text descriptions** (`#157 phase 4`): generated CLI help text includes command descriptions from metadata. (`87c68bddf`)
- **TypeScript CLI codegen target**: the codegen pipeline emits a complete CLI framework for the TypeScript target, wrapping incipit/argumenta into command dispatch. (`ae53429ea`)
- **`faber build` command**: multi-file compilation support — the `build` subcommand compiles all sources and generates output from a project directory. (`b167360e1`)
- **`faber compile` renamed to `emit`**: the compile subcommand is renamed for clarity. (`08182170a`)
- Documentation: `fons/grammatica/cli.md` created with CLI framework docs. (`4042b0a55`)
- Coreutils example stubs (`echo`, `true`, `false`) for CLI experimentation. (`1411398f9`)
- `coreutils/bin/echo.fab` updated with keyword renames (`tenta` → `tempta`, `vel` → `secus`, `iunge` → `coniunge`). (`1a779dbd1`)
- CLI examples moved to `fons/exempla/cli/`. (`23251aac6`)

#### HAL `@subsidia` layer

- **PoC injection**: initial proof-of-concept for a new Hardware Abstraction Layer with `consolum` and `processus` modules. (`60b773f3b`)
- **Full HAL layer**: 10+ HAL modules (`aleator`, `arca`, `caelum`, `consolum`, `processus`, `crypta`, `json`, `nomenclator`, `nuncius`, `pressura`, `rete`) with TypeScript codegen covering all modules. (`e986bb6f4`, `b0fde1ac3`)
- **`@subsidia` import resolution** (`#167`): semantic-level import resolution for the `@subsidia` pattern — HAL modules are resolved through a pactum-based dependency mechanism. (`3060409fc`)
- **Pactum plumbing**: pactum declarations generate proper TypeScript interfaces and import paths for HAL dependencies. (`bda74f938`)
- Focused examples: `consolum` and `processus` exempla added. (`ad7e5b077`)
- Removed broken `norma/hal/*` import magic from the faber semantic layer. (`eab91c43a`)

#### Discretio (tagged unions) and `discerne omnia` exhaustiveness

- **Parser flag**: `discerne omnia` keyword added to parser AST for both faber and Rivus. (`da1f0907a`)
- **Faber exhaustiveness**: the faber semantic analyzer enforces that `discerne omnia` branches cover all `discretio` variants. (`abb2dda39`)
- **Rivus exhaustiveness**: Rivus semantic analyzer enforces the same exhaustiveness invariant. (`c5dbc100f`)
- **Metadata plumbing**: `discretio` declaration indices and variant metadata are exported through modules and imports in both faber and Rivus. (`52e5b7b82`, `2818ad7fa`, `372dcb361`, `5e67bc782`)
- **Go codegen for `discretio`**: Rivus generates Go tagged-union types (interface + per-variant structs). (`283ec2b41`)
- **Go codegen for `elige` and `discerne` (Phase 2)**: control-flow codegen for `elige` (type-switch pattern) and `discerne` (match expressions). (`601f4482b`)
- **Target flag and variant imports**: the `--target` flag controls output, and `discretio` variant types are properly imported in generated code. (`3cfb573b6`)
- **Variant type export fix**: variant types are exported from `discretio` union codegen in both TS and Rivus targets. (`e3d4c98c9`)

#### Post-function modifiers and `exitus`

- **`exitus` function postfix** (`#186`): a post-function modifier that marks a function as an exit-code terminal — the generated code returns a numeric exit code. Full semantic validation and TS codegen support. (`e7ef8ded1`)
- **Multiple post-function modifiers**: parser, AST, and semantic analysis extended to support stacking multiple post-function modifiers (e.g., `exitus` + custom annotations). (`d7fb09c30`)
- **Post-function modifier alignment**: docs, EBNF, and parser unified under a consistent post-modifier grammar. (`f41dbac91`)
- **Semantic validation of function modifiers**: the semantic layer validates modifier placement and compatibility. (`f3895f05c`)
- **Go errata returns** (`rivus/go`): the `exitus` pattern generates Go-style error returns from errata-bearing functions. (`3dd22ac96`)

#### Rivus Go codegen expansion

**Phase 1 — Control flow and expressions:**
- Go codegen for control flow (`si`, `dum`, `pro`) and `cede`/`redde` statements. (`ba6449e48`)
- Go lambda expression codegen (`fn` → anonymous Go functions). (`0d400acf6`)
- Go `novum` constructor codegen (struct constructors). (`1777d40de`)
- Go genus method codegen (method definitions on genus structs). (`21961999f`)
- Go genus struct codegen (struct type generation). (`3217d9f9d`)
- Go object literal codegen (struct literal initialization). (`cd1bea33f`)
- Go `adfirma` codegen (variable/const declaration). (`94ce5088f`)
- Go `vel` coalesce operator (`??` → Go `nil`-coalescing pattern). (`e4c46a6a5`)
- Go optional chaining (`?.` → Go nil-guard pattern). (`4f7c50795`)
- Go target integrated into `build:exempla` pipeline with improved TODO diagnostics for uncovered constructs. (`172e05a6e`)

**Fixes and refinements:**
- Respect default/private visibility for genus methods in Go (`#193`). (`4337e7752`)
- Preserve statement order in `main` function generation. (`9080ff5ce`)
- Avoid empty output files and infer slice literal types. (`4b5eb91a6`)
- Add `--target` flag to Rivus CLI for output language selection. (`3cfb573b6`)
- Artifex build failures resolved (TS preamble order, Go expression guards). (`d8c4f7f7c`)

#### Rivus parser and semantic fixes

- **Keyword disambiguation**: LPAREN lookahead distinguishes keywords from function calls in the faber parser. (`92d0cabdb`)
- **`cede` in `incipiet` blocks**: Rivus semantic analyzer now accepts `cede` (break) within `incipiet` (loop) blocks. (`993f82dea`)
- **`assignabileAd` nil crash fix**: guard against null dereference in Rivus binary expression semantic checks. (`69276ba15`)
- **`prae typus` in parameter lists**: Rivus parser handles default type annotations (`prae`) in function parameter lists. (`0c1c8f1b1`)
- **Function type annotations**: Rivus parser and semantic layer support function type annotations (`fn(T) -> U` syntax). (`3b0170b1d`)
- **`ab ubi` identifier prefixing** (TS codegen): Rivus TS codegen prefixes identifiers in `ab` (import) and `ubi` (use) contexts to avoid collisions. (`74aca1828`)
- **`ceterum` support in `discerne` parser**: the Rivus `discerne` parser handles `ceterum` (else/default) branches. (`314d38226`)
- **`curata` keyword consumption**: fix where the `curata` allocator keyword was not consumed when parsing function declarations. (`07dd0e6a0`)
- **`qua -> copia` constructor special case removed**: cleanup of an old codegen path in favor of the general constructor pattern. (`28f49e392`)
- Detector import of Sententia variants fixed. (`94b876baf`)
- `typi.fab` updated for type system consistency. (`b08bef2e0`)
- PR review feedback: CI workflow improvements, CLI detector/resolver edge cases. (`b7f93594a`)

#### Norma / stdlib reorganization

- **Builtin type reorganization** (`#168`): standard library builtin types (`copia`, `fractus`, `lista`, `numerus`, `tabula`, `textus`) moved into `fons/norma/innatum/` directory with an updated build pipeline. (`d7e374c88`)
- **Per-target registry files**: the Norma build pipeline generates separate registry files for each target language (C++, Python, Rust, TypeScript, Zig), each containing target-specific type bindings. (`0e99b94f3`)
- **Regenerated Norma** (post-organization): all generated registry files refreshed. (`51f10f434`)
- **Renaming**: `norma-registry.gen.fab` → `norma.gen.fab`; `norma-registry.ts` → `norma.ts` across all consumers. (`80698a77c`, `4ccfdad5b`)
- **Nested `elige` → data structure**: the Rivus Norma registry replaced nested `elige` (switch) chains with a data-structure-driven lookup. (`c215042c8`)
- **Old `@verte` stdlib files archived**: pre-HAL stdlib modules moved to `fons/norma/archivum/`. (`36757e517`)
- **Timestamp-free builds**: `build:norma` regenerated files without timestamp headers. (`659cc9e95`)
- **Dead code removal**: unused `index.json` and stale build artifacts removed. (`2286ef4e3`)

#### Exempla reorganization and cleanup

- **Root exempla consolidated** into `fons/exempla/` — the top-level `exempla/` directory is removed and all examples live under `fons/exempla/`. (`231a8750c`)
- **Latin naming convention**: all example files renamed to Latin (`discerne.fab`, `clausa.fab`, `adfirma.fab`, etc.) for consistency. (`291751598`)
- **Stub files** added for missing language constructs (28 files covering `abstractus`, `ad`, `ante`, `aut`, `cede`, `ceteri`, `demum`, `ego`, `et`, `figendum`, `fixum`, `futura`, `futurum`, `generis`, `implet`, `lege`, `mone`, `nexum`, and more). (`cb7849f21`)
- **`selfhost-rivus` deleted**: the self-hosted Rivus bootstrap script was removed. (`31779b755`)
- **`princeps.fab` deleted** from exempla imports. (`af0b871ee`)
- Various exempla updates (`conversio.fab`, `greet.fab`, `morphologia.fab`). (`c41f307ed`, `dda2459a5`, `b9b9a0806`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
