+++
title = "Radix 0.21.0"
section = "releases"
order = 76
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.21.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

Compact release spanning 37 commits over 4 days. The main themes are: a new
**target capability validation** system that catches feature incompatibilities
before codegen, **norma stdlib expansion** with JSON/YAML/TOML serialization and
namespace import semantics, **cross-target codegen fixes** across Rust, Zig, Fab,
and TypeScript outputs, and a **test harness** with SQLite-backed recording and
feature-matrix reporting.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 37 |
| Date span | 2026-01-09 → 2026-01-12 |

### Major tracks

#### Target capability validation

A new feature-gate system that validates language-feature compatibility against
each compilation target before codegen runs. Emits structured errors with
file:line:col positions and actionable suggestions.

- **Design document:** Proposes feature-gate validation for catching target
  incompatibilities (async on Zig, generators on Rust, exceptions on Go)
  (`96e52827f`)
- **Support-level model:** Splits support vs lowering, defines emulation/mismatch
  policy (`6115bc40d`)
- **Phase 1 infrastructure:** Core `TARGET_SUPPORT` matrix, AST feature detector,
  validation logic with structured error reporting, and 28 baseline tests
  (`9b93966c9`)
- **Feature-detector bug fixes:** Fixes for `FacBlockStatement`,
  `ProbandumStatement`, and `TemptaStatement` AST iteration that reduced test
  failures from 187 to 57 (`ef2179fb8`, `6d8b37aa4`, `af8a8c003`)
- **Pipeline integration:** Validation wired into the codegen pipeline — invalid
  programs fail before any target generator runs (`32675a2f7`)
- **Phase 3+4 (testing + docs):** Feature×target matrix tests, interaction tests,
  compatibility matrix documentation (`targets.md`) (`589c29c9c`)
- **Emulated support level:** `throw`/`tryCatch` and object destructuring marked
  as emulated for Rust/Zig/CPP, reducing false-positive validation errors
  (`78e9f274d`)
- **Python destructuring emulated:** Python target added to emulated
  destructuring, aligning with existing handling (`b473aa4dc`)
- **Test suite cleanup:** Unsupported feature/target combinations now actively
  skipped via capability validation (`74a0f3e60`)

#### Norma stdlib: JSON, YAML, TOML and namespace imports

- **Serialization libraries:** `json.fab` (with pretty-printing and indexed
  access), `yaml.fab` (multi-document support), `toml.fab` (datetime support) —
  each with a consistent Latin API (`solve`/`pange`/type-checkers)
  (`c6d0e1fc6`)
- **`forma.fab` removed:** Superseded by the three format-specific libraries
  (`5b05f561a`)
- **Namespace import semantics (Phase 1):** `NamespaceType` in the semantic type
  system, `ex "norma/json" importa * ut json` import support, and member-access
  resolution through the norma registry (`abc7a4b35`)
- **Genus declaration for `json.fab`:** Enables `json.solve()` namespace calls
  via the registry (`0a0b3470f`)
- **Codegen for namespace calls:** All targets (TS, PY, RS, ZIG, CPP, FAB) emit
  registry-mapped calls, using a shared `norma-namespace.ts` helper
  (`ca024cb54`)

#### Cross-target codegen fixes

- **Rust:** Added `LegeExpression` support (stdin via `std::io::Read`) and
  `@externa` function declarations emitting `extern "C"` blocks (`50ba08284`)
- **Zig:** `@externa` functions emit `extern fn` declarations; constructors and
  methods reject `@externa` (`c2200a4d5`)
- **Fab codegen:** Fixed to output parseable Faber syntax — `#` comments,
  `et`/`aut`/`vel` operators, removed unnecessary parentheses (`d3eb1663e`,
  `0ac370601`)
- **TypeScript:** Hex escape sequences in `scriptum` calls to avoid backtick
  and `${}` template-literal conflicts (`1d09a55f8`)
- **Rivus Zig compatibility:** Replaced `+` string concatenation with `scriptum()`
  calls in littera.fab files (`46e5f05db`)
- **Rivus adfirma:** Fixed quote-escaping bug by using `.muta()` for global
  replacement (`12bd1e988`)
- **build-exempla:** Uses file paths for faber (module resolution), stdin for
  rivus/artifex (`9c5515edc`)

#### Test harness with SQLite recording

- **Extracted shared test utilities** (`compile`, `match`, YAML loading) into
  `fons/proba/shared.ts` (`9fbb550a8`)
- **SQLite-backed harness:** Schema tracks compiler, source, codegen status,
  verify status per feature/target/test — CLI runners for execution and
  feature-matrix reporting (`9fbb550a8`)
- **`test:report` script:** Runs tests, records to DB, generates feature-support
  matrix with failure details (`b4623cfe5`, `7411af224`)

#### Repository restructure and process

- **Renamed `faber-romanus` → `faber`:** GitHub repository and local directory
  renamed; `probationes` research harness split into a separate `faber-trials`
  repo (`c5e95cd26`)
- **OpenAI dependency removed:** No longer needed after the probationes split
  (`693514098`)
- **Agents restructured:** Moved from `.claude/agents/` to `agents/` directory
  with standalone CLI runner documentation; generic agents live in
  `~/github/ianzepp/agents/` (`517e33c70`)
- **AGENTS.md updated:** Workflow patterns from experience — phase decomposition,
  recon before assignment, parallel execution with lock collision, review gate,
  triage flow (`dbbe05863`)

### Other changes

- Compiler streaming API design doc: JSONL protocol for long-lived compiler
  processes with synchronous output ordering (`0e24a6e76`)
- Fix parser tests using obsolete `<<`/`>>` bitwise-shift syntax — migrated to
  `sinistratum`/`dextratum` keywords (`2bc7d3ece`)
- Fix norma constants (PI, E, TAU) failing to translate — preserved empty `params`
  arrays in the JSON registry (`1fb3fbe32`)
- Fix norma stdlib zero-argument function translations (`fractus`, `uuid`,
  `nunc`, etc.) (`da410b717`)
- Add `opifex` to generic agents list, document issue-worker workflow
  (`04d208c6d`)
- Document `test:report` command in AGENTS.md (`669b9c875`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
