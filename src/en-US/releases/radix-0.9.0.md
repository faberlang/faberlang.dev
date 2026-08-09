+++
title = "Radix 0.9.0"
section = "releases"
order = 88
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.9.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

Self-hosting bootstrap begins. This release pivots the bootstrap target from
Zig to TypeScript and delivers the core compiler infrastructure: a full
precedence-climbing parser skeleton in Faber itself, two-pass semantic analysis
for forward references, local module import resolution, and several language
additions (`finge`, `fac...dum`, relative imports).

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 18 |
| Date span | 2025-12-31 → 2025-12-31 |

### Major tracks

#### Bootstrap pivot: Zig → TypeScript

- **Pivots the bootstrap target from Zig to TypeScript**, renaming the original
  plan to `bootstrap-zig.md` and creating `bootstrap-ts.md` with a simplified
  plan. Rationale: TS codegen is mature, same Bun runtime, no allocator
  complexity. Estimated 14–19 days vs 20–28 for Zig. (`96d95652c`)
- **Adds `curata` keyword** to the bootstrap lexicon (needed for allocator
  annotation in Faber source). (`e4efe11ef`)

#### Self-hosted parser skeleton (fons-fab)

- **Adds the bootstrap parser skeleton** — 16 new `.fab` files implementing
  nucleus (core Parser genus with token navigation), errores (error codes
  P001–P205), typus (type annotation parsing), precedence-climbing expression
  parsers (binaria, unaria, primaria), and statement parsers (actio, massa,
  varia, index) with TODO stubs. Also fixes keyword-as-method-name and
  non-statement-keyword-as-identifier handling. (`054615ffb`)
- **Documents the Resolvitor blocker**: parser modules have mutual recursion
  (expressions need blocks, statements need expressions); the solution is a
  Resolvitor context with function pointers, but Faber lacks function type
  syntax. Creates `resolvitor.fab` in a blocked state. (`babed8287`)
- **Uses the pactum Resolvitor pattern** to break parser circular imports. The
  pactum defines method signatures; parser modules import only the Resolvitor
  interface (`r.massa()`, `r.expressia()`) — no direct imports between
  expression and statement modules. Proof-of-concept on `sententia/error.fab`.
  (`a0f0704f5`)
- **Converts all 12 parser files** to the Resolvitor pattern — they compile
  cleanly. Key changes: functions take `Resolvitor r` instead of `Parser p`,
  cross-module calls use `r.expressia()`/`r.sententia()`/`r.adnotatio()`, and
  removed `fac...dum` (do-while) in favor of regular `dum` loops. Blockers
  remain: AST types are `genus` not `discretio` variants, so they can't be
  returned as `Expressia`/`Sententia`. (`0b5c2986b`)

#### Two-pass semantic analysis

- **Implements three-phase analysis** for within-file forward references:
  Phase 1a predeclares all top-level names with placeholder types, Phase 1b
  resolves signatures, Phase 1c iteratively resolves type aliases to fixed
  point, Phase 1d detects circular type aliases, Phase 2 analyzes bodies with
  a complete symbol table. Enables forward references and mutual recursion
  within a file. (`7cd405bad`)
- **Rewrites `two-pass.md`** from a proposal into an implementation doc
  covering the five-phase structure, enabled patterns, type alias cycle
  detection, remaining work (throwability), migration plan, and test coverage.
  (`b8129ad86`)
- **Clarifies scope**: cross-file imports are handled by `modules.ts`; two-pass
  is needed for within-file forward refs. Adds Open Questions section covering
  genus method forward refs, tempta/cape throwability, pactum conformance
  timing, top-level variable ordering, and generics. (`a7fdf1903`)

#### Local imports and module resolution

- **Adds local file import resolution** for `.fab` modules: a new `modules.ts`
  handles path resolution, file loading, and export extraction. All top-level
  declarations are exports. Relative imports (`./foo`, `../bar`) resolve from
  the importing file's directory. Circular imports are detected with full cycle
  path. Diamond dependencies work via module caching. CLI now passes file path
  to the analyzer. (`746df4fcd`)
- **Converts fons-fab forward declarations to relative imports** across 22
  files, replacing duplicate `Locus` genus definitions with proper imports from
  `ast/positio.fab`. Fixes a `typus.fab` keyword conflict (renamed field
  `typus` → `adnotatio`), removes Zig-specific `curata alloc` from
  `lexor/index.fab`, and adds Symbolum/LexorType imports. (`7ddd715ad`)

#### Language additions

- **Adds `finge` keyword** (Latin: to form/shape) for discretio (tagged union)
  variant construction, distinct from `novum` (struct instantiation). Supports
  explicit type via `qua`, inferred type, and unit variants. Codegen for all 6
  targets (TS, Python, Rust, Zig, C++, Faber). (`51a34dac2`)
- **Adds `fac...dum` (do-while loop) syntax**: `fac { body } dum condition`
  with optional `cape` handler. Codegen emits idiomatic do-while in C++/TS,
  loop+break in Rust/Python/Zig. (`1b62ae062`)

#### Planning and documentation

- **Updates `bootstrap-ts.md`** removing the 'Current Blockers' section — all
  issues resolved (mutual recursion → pactum Resolvitor, discretio
  instantiation → `finge`, function hoisting → two-pass, do-while loops →
  `fac...dum`). Adds 'Discretio Variant Construction' section with `finge`
  example, renames 'Current Blockers' → 'Gotchas', updates Session 3 lessons.
  (`5ff64f33c`)
- **Updates planning docs** across `bootstrap-ts.md` and `two-pass.md`. (`1764f3f7f`)
- **Updates GRAMMAR.md** plus `grammatica/functiones.md`, `grammatica/regimen.md`,
  and `grammatica/structurae.md`. (`42bd26f3e`)
- **Updates `lambda.fab`** exemplum. (`8103feb11`)

#### Cleanup

- **Removes duplicate `nihil` keyword entry**: `nihil` serves as both a literal
  value and a unary operator, but the duplicate was dead code (Map stores one
  value per key). Keeps the value category entry with a comment explaining the
  dual usage. (`88fc03180`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
