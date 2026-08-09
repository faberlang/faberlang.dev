+++
title = "Radix 0.29.0"
section = "releases"
order = 68
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.29.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

Retrospective version marker for the **Norma/HAL multi-runtime restructure**:
systematic Latin verb standardization across all 14 HAL modules, Norma expansion
to Go and Rust runtimes, and Rivus Stage 6 self-hosting progress.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 52 |
| Date span | 2026-01-25 → 2026-01-26 |

### Major tracks

#### HAL Latin verb standardization (17 modules)

All HAL module method names were systematically reworked around Latin verb
conjugation to encode sync/async semantics:

- **Imperative** (-a, -e, -i): synchronous (blocking)
- **Future indicative** (-et, -ebit): asynchronous

Modules touched: `solum` (file I/O), `processus` (process), `consolum`
(console), `tempus` (time), `nuncius` (IPC/sync primitives), `thesaurus`
(cache/pub-sub), `aleator` (random), `crypta` (crypto), `pressura`
(compression), `arca` (database), plus serialization verbs across `json`,
`yaml`, and `toml`.

Structural renames:
- `caelum` → `http` (HTTP client/server), `rete` → `caelum` (TCP/UDP transport
  layer; "caelum" = sky/ether, counterpart to `solum` = ground/local I/O)
  (`99ed97b8a`)
- Removed `nomenclator` (DNS) — direct queries are better served by
  target-specific libraries rather than a core HAL abstraction (`71e13bc36`)
- `crypta` simplified: `cela/revela` (encrypt/decrypt), `signa/verifica`
  (asymmetric), `derivabit` (key derivation — async only); dropped compound
  convenience methods (`baadd38d7`)
- `pressura` aligned with serialization: `comprime` (compress), `solve`
  (decompress) matching `json.solve` for parse (`dcf7e8259`)
- `arca` removed SQLite/memoria convenience functions in favor of URL-based
  `connectet` (`dfe82d76e`)
- `processus` renamed `exsequi` → `exsequetur` (async), `genera`/`generabit`
  now distinguishes attached vs detached spawn (`26eb214c3`)
- Serialization verbs standardized: `pange` = serialize, `solve` = parse,
  `tempta` = try-parse, `carpe` = pluck by index, `inveni` = find by path
  (`1628c1a44`)

#### Norma multi-runtime expansion

Standard library implementations added beyond TypeScript:

- **Go HAL**: `norma-go` with `consolum`, `processus`, `solum` + `json`,
  `yaml`, `toml` serialization (`f519ab3d9`)
- **Rust HAL**: `norma-rs` with `solum`, `consolum`, `processus` using tokio
  async I/O (`360c79a89`)
- **Rust serialization**: `json` (serde_json), `yaml` (serde_yaml), `toml`
  (toml crate) (`845421ee3`)
- **Rust arca** (database): multi-backend SQL via sqlx (SQLite, PostgreSQL,
  MySQL) with async-stream cursor/generator pattern (`7e67c780a`)
- **Rust subsidia**: `.fab` directive annotations for Rust targets
  (`08a9f0402`)
- **codex module**: base64, hex, and URL encoding/decoding with safe
  try-variants (`bd6b912be`)
- Serialization moved out of HAL and into standalone modules (`0afbaf9ea`)
- TypeScript HAL moved to `norma-ts/hal/` (`b4baa355f`)

#### Rivus self-hosting — Stage 6

Progress toward rivus compiling itself:

- **Stage 6 build**: rivus compiles itself using verified compilers
  (`b4ea31e5a`):
  - `innatum.fab` with hardcoded builtin type translations
  - Replaces `norma.gen` dependency for compiler intrinsics
  - Stage 6 runs but fails at pattern binding type inference (issue #78)
- **`argumenta` binding**: CLI argument access via `incipit argumenta args`
  generates `process.argv.slice(2)` (`eb708cabc`)
- **Nullable types**: `si` prefix parsing for `fixum si textus x`; removed
  unused `in` mutation block (`c657baa0d`)
- **HAL file I/O**: `norma:solum` imports enabled for rivus, breaking the
  chicken-and-egg problem (`734d6fd7e`)
- **Subsidia resolution**: `nanus-ts` resolves `norma:*` imports to HAL
  `.fab` `@ subsidia ts` annotations (`f6da5bdaf`)
- **Test CLI entry point**: `rivus-cli/rivus.fab` (`5cfda8456`)
- **Nested function fix**: `ego` captured in closures for correct `this`
  binding (`efcf932fd`)

#### Nanus-ts codegen fixes

- `Record<K,V>` emitted instead of `Map<K,V>` for tabula types (Maps don't
  support bracket notation) (`bd3bd82bd`)
- Null checks use `(x == null)` / `(x != null)` instead of `!x`/`!!x` (failed
  for falsy values like `0`) (`1ff5af520`)
- `inter` operator emits `.includes()` for array membership (JS `in` checks
  object keys, not array values) (`1f730c410`, `82d8ff329`)
- Hex escape (`\xNN`) and `$` escaping in template literals (`794963799`)

#### Build system & cleanup

- `copyHalImplementations` renamed to `copyNorma` with recursive copy
  (`89dc6e315`, `203ec4776`)
- Rivus output directories renamed to `rivus-<compiler>/` (`98b3a589e`)
- Removed `build:norma` from build (`bff400263`)
- Deleted `go.work` (`ee29b2e82`); moved `faber-ts` to `docs/reference`
  (`a5e3bebc3`); archived full `rivus-cli` to `docs/reference/` (`82d8ff329`)
- Removed stale directories: `subsidia` (`ca7c51c7b`), `archivum`
  (`52355087d`); stale README (`b50683008`)
- Refactored `nanus-go`/`subsidia` and `nanus-rs`/`subsidia` into their own
  subtrees (`1b9dd1b71`, `c803a7fcd`)

### Other changes

- Placeholder directories for `ems`, `vfs`, `llm` modules (`51ba702fc`)
- Exempla syntax updates for rivus compatibility (`ae17af7f7`, `7c724a1e5`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
