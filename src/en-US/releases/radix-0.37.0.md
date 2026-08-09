+++
title = "Radix 0.37.0"
section = "releases"
order = 60
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.37.0 |
| **Tag** | `radix-v0.37.0` |
| **GitHub** | [radix-v0.37.0](https://github.com/faberlang/releases/releases/tag/radix-v0.37.0) |
| **Published** | 2026-07-16 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

Pinned download for **Radix 0.37.0**. For the current release, use [Install](/start/install.html) instead.

| Platform | Archive | Size | Checksum |
|---|---|---|---|
| **macOS arm64** | [radix-v0.37.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/radix-v0.37.0/radix-v0.37.0-aarch64-apple-darwin.tar.gz) | 1.1 MB | [sha256](https://github.com/faberlang/releases/releases/download/radix-v0.37.0/radix-v0.37.0-aarch64-apple-darwin.tar.gz.sha256) |

```bash
curl -fsSL -o radix.tgz \
  https://github.com/faberlang/releases/releases/download/radix-v0.37.0/radix-v0.37.0-aarch64-apple-darwin.tar.gz
tar -xzf radix.tgz
sudo mv radix-v0.37.0-aarch64-apple-darwin/radix /usr/local/bin/
radix --version
```

## Release notes {#notes}

Release spanning **113 non-merge commits** (`v0.36.0..v0.37.0`, 2026-05-23 → 2026-05-24).
The theme is **Rust backend cleanup and writer refactor, with closure/codegen fixes** — the
largest single wave of Rust codegen bug fixes in the project's history, paired with a
wholesale migration from a monolithic writer to an `ExprEmitter`-based dispatch architecture.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 113 |
| `refactor(...)` commits | 15 |
| `fix(...)` commits | 33 |
| `docs(...)` commits | 10 |
| Date span | 2026-05-23 → 2026-05-24 |

### Major tracks

#### Rust codegen writer → ExprEmitter refactor

Extracted an `ExprEmitter` context and migrated every expression-emitting path from the
monolithic writer to the new emitter pattern:

- Introduced the expression emitter context (`f1873ca8a`)
- Migrated expression helpers (`96cba70f4`), operators (`f49baa18b`), access emission
  (`a35c15b3b`), verte emission (`792edabe2`), match expressions (`7aebe1ae9`),
  iteration (`d35549ec4`), branch emission (`ac9e1205a`), and control expressions
  (`937859cb8`)
- Split call expression emitter (`3a5ca1a9f`) and control expression emitter
  (`975db2382`)
- Centralized optional and dynamic emission (`ed515a658`) and type shape predicates
  (`67055390e`)
- Extracted generated prelude helpers (`c6893f534`)
- Made the expression dispatcher emitter-native (`4b438523e`)
- Capped by the **Complete Rust codegen writer cleanup** (`fd7617295`, +1008/−832 lines
  across 12 files), which also moved CLI, declaration, statement, and MIR probe modules
  to the new shape

#### Closure/codegen fix wave (33 fix commits)

The largest cluster of Rust codegen fixes in a single release. Covers:

- **Optional types**: optional map members (`747ca5a15`), optional chain lowering over
  plain receivers (`dae54c04b`), optional parameter defaults (`4b58d34c1`), optional
  if-branch coercion (`40b96bda6`)
- **Dynamic values**: dynamic value emission (`850c906ff`), dynamic context coercion
  (`759f5fcd2`)
- **Collections**: typed innatum collections (`480416a5f`), cursor functions as
  iterables (`3b16b140e`), array borrows in itera ex (`0cff1abed`), array spread sources
  (`22dff5638`), indexed destructuring clones (`3d25a9e84`), lista index casts
  (`23045999b`), lista morphology methods (`abb059606`)
- **Control flow**: nullable return wrapping (`c1e0f52eb`), elige match exhaustiveness
  (`7932a548f`), textus match operations (`58fca4c3d`), itera de keys and indices
  (`cbfb20c5a`), text concatenation safety (`5882610d2`), iterable itera pro ranges
  (`1ec5fcc6d`)
- **Calls and binding**: owned call argument cloning (`a4c04de54`), vel operand
  consumption avoidance (`d6fe93e37`), self receiver emission for methods
  (`149c2ded8`), self-returning method bridging (`743ff2d08`), spread call argument
  preservation (`31a282e1c` — HIR + all backends)
- **Numeric/type**: enum variant qualification (`1724e0028`), fractus arithmetic operand
  casting (`31a282e1c`), conversio radix hints (`fc2f29a4b`)
- **Async/genus**: async incipiet entries (`caa2fa377`), genus creo hooks
  (`fce6e6ede`)
- **Parser**: empty typed constructors (`b0cebda79`)

The closure ergo factory was marked complete (`3fbd74f67`), with exempla modernized
(`4119d75cb`) and made standalone (`3efcfa8a2`).

#### Ad capability channel

Adopted a **type-first ad channel syntax** (`2d0b23115`, 19 files, +198/−78) and
implemented **non-strict ad capability calls** (`fd8157e22`, 15 files, +538/−41),
establishing the grammar and Rust codegen path for capability ad-invocations. Capability
call policy was recorded (`6a51785e4`) and the ad exemplar category clarified
(`40df5ea81`).

#### HIR visitor

Added a **mutable HIR visitor** (`0cc6e23b0`, 422-line `hir::visit` module), replacing
~281 lines of manual finalization traversal in the typecheck pass. The visitor was
adopted in codegen error scanning (`87c3d5acc`), semantic analyses (`a8ea63c46`), and
codegen analyses (`933da3102`). Decomposition analysis was refreshed after the visitor
landed (`50f7ac3e1`).

#### Legacy removal

Executed **execution roadmap epic 1** (`6b8950c38`, +400/−1121 lines): removed the `ab`
collection DSL from the Lexer, parser, HIR, all three codegen backends (Rust, Go, TS),
exempla, and explain docs. Removed legacy Go runtime binaries (`707bc6cb4`) and the
entire `runtimes/norma-go/` and `runtimes/norma-py/` directories (`b6d3b271d`, −2901
lines). Planned the removal of the ab collection DSL (`8bc2fc8c5`).

#### Phase-aware diagnostics

Added **phase-aware diagnostics mode** (`054554510`, 13 files, +646/−18): diagnostics
now carry a phase tag, rendered in the driver and CLI bin, with the tool surface updated
to filter by phase. Constrained by a diagnostics mode plan (`bdeca3155`).

#### Ascription glyph realignment

Switched the static ascription glyph from a dedicated `∴` keyword to `:proportion`
syntax (`a01941078`, 37 files, +165/−145). Renamed `explain/∴.md` → `explain/ascription.md`
and fixed active doc references (`0dc1fb016`).

#### Documentation factory

Planned and produced the complete **Radix documentation factory** (`7647d44cf`) covering:
surface and diagnostics (`0bec5e8f7`), front-end syntax phases (`a4368371c`), HIR
lowering boundary (`e589e6eda`), semantic core passes (`8e78d9a22`), typecheck
subsystem (`3eb11ba70`), MIR subsystem (`0c6aa0573`), shared codegen and TypeScript
backend (`f74c06511`), Rust backend (`af1cecfb0`), Go backend (`c0c0b450d`), and
canonical Faber backend (`c58b6a0e8`).
Standardized TOML frontmatter on `+++` delimiters (`5be70b433`, matching the
`explain/` corpus). Seeded the monorepo documentation site home (`1d8b6170e`).

### Other changes

- Added Faber execution roadmap goal (`9f4263608`)
- Captured macOS host architecture direction (`93af65a85`)
- Modeled host capabilities as syscalls (`b056505ea`)
- Required high-thinking poker-face gates (`c038c5520`)
- Merged language overview into README (`fab0f09cb`)
- Added Faber language comparison guide (`fce50ccae`)
- Updated Faber language critique (`45ea8a85d`)
- Applied documentation baseline across the `faber` crate (`6083ebdd0`)
- Strengthened faber file headers (`c8c9792d2`)
- Compacted private front matter schema (`9a9a94ace`)
- Tidied explain entry field docs (`28131a5d4`)
- Documented explain registry internals (`3d20dee44`)
- Refined explain documentation baseline (`353cc6802`)
- Isolated type rendering tests (`483c443f9`)
- Covered optional emission predicate (`9f22c3348`)
- Split backend test clusters (`27fcb30fc`)
- Accepted driver rustfmt (`c91faf616`)
- Enforced epic 2 corpus boundary in exempla (`9f59f39b6`)
- Audited epic 2 housekeeping (`d700bf7f1`)
- Clarified epic 2 cleanup targets (`9eee4bd16`)
- Tightened epic 2 cleanup checks (`c8e2badd8`)
- Reframed epic 4 host kernel plan (`4282c4b98`)
- Documented frame-native concurrency vision (`387204186`)
- Corrected website frontmatter from YAML to TOML (`40ac9db21`)
- Removed stale mechanics review (`b143f0186`)
- Updated WASM plan for MIR closeout (`69e94a5ca`)
- Clarified exempla single-file corpus policy (`bc9978d84`)
- Documented compiler engineering rules refresh (`0bef5b79b`)
- Split capability call goal from e2e plan (`34441bdb4`)
- Removed completed radix docs factory plan (`98feb227e`)
- Fixed active docs for ascription glyph (`0dc1fb016`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
