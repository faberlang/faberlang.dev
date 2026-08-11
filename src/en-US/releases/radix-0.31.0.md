+++
title = "Radix 0.31.0"
section = "releases"
order = 69
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.31.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

Release spanning **87 non-merge commits** (`v0.30.0..v0.31.0`, 2026-02-15 → 2026-02-16). Two major HIR language constructs graduate to dedicated nodes with Unicode glyphs, the entire operator surface migrates to Unicode core syntax, a TypeScript codegen backend lands, and Rust codegen reaches end-to-end failable pipeline support.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 87 |
| Date span | 2026-02-15 → 2026-02-16 |

### Major tracks

#### HIR: Conversio (`⇒`) and Verte (`⇢`)

- **Conversio** (`HirExprKind::Conversio`): new dedicated node for runtime value conversion (`⇒` / `numeratum` / `fractatum` / `textatum` / `bivalentum`), replacing generic casts. Codegen emits `.parse()` / `.to_string()` instead of `as` casts. Supports explicit target type, codegen hint params, and `vel` fallback (`3280b021`).
- **Verte** (`HirExprKind::Verte`): unifies `qua`, `innatum`, and `novum` into a single dispatch-on-target-type node. `novum` becomes postfix (`{} novum Type`), matching `qua`/`innatum` convention; legacy prefix form and positional constructor args removed (`3c5c8fab`).
- Promoted to unified `⇢` glyph across lexer, parser, HIR, semantic passes, and all three codegen backends (`a164c8a1`).
- Correctness fixes for Conversio codegen and resolve (`50c60478`), Verte lowering and codegen (`057313d4`).
- Improve unnecessary cast warning to handle type aliases and skip construction forms (`8db5673f`).

#### Unicode operator migration (cross-pipeline)

Full adoption of Unicode core operators from spec through codegen, covering every operator class:

| Class | Operators |
| --- | --- |
| Bitwise & shift | `∧` / `∨` / `⊻` / `≪` / `≫` (`c7a1536d`) |
| Compound assignment | `+=` → `+=` (Unicode equivalents for all compound forms) (`22d64b00`) |
| Range | `‥` (inclusive) / `…` (exclusive) (`f05f5f47`) |

Pipeline layers touched:
- Spec: EBNF adoption (`8f7ea24c`)
- Lexer: tokenization (`13c0608c`)
- Parser: operator parsing alignment (`c8285d4c`)
- Codegen: Faber backend emission (`f55ce960`)
- All downstream consumers migrated: rivus self-hosted sources (`59e92558`), nanus-rs (`83575f55`), exempla `.fab` examples (`af1fa698`), proba YAML snippets (`399722e3`), golden snapshots (`43ded524`)

#### TypeScript codegen backend (new target)

A complete new backend target in `radix-rs/src/codegen/ts/`:

- Scaffolding, type mapping, and module wiring (`f9e6b377`)
- Declarations and statements (`b80bd40f`)
- Expression emission (`4d2a3f71`)
- Norma method calls and intrinsic calls (`4f655322`)
- Integration coverage with golden TS fixtures (`b5293eeb`)

#### Rust codegen maturation

- **Failable `iace` pipeline** (resolves #332, #333, #334): emit `Result<T, String>` for failable functions, `return Err(…)` for `iace`, propagate via `?` at call sites, suppress via `tempta`/`cape` handling (`807eba58`).
- **Name resolution context**: wire `DefId`→`Symbol` map and string interner through Rust codegen decl/expr/stmt/types signatures (`8834aac2`, resolves #319).
- Main/print codegen and decl/expr gap completion (`8889b261`).
- Assert/panic lowering and usage-driven imports (`ff5b4a36`).
- Ignored Rust exempla end-to-end harness (`684b991b`).
- Codegen identifier placeholder resolution (`d0f94a8e`).
- Various fixes: string parens and import paths (`0f3401ad`), error propagation instead of dropping (`61060151`), guard against HIR errors in Faber codegen (`07470821`), fail fast on HIR error expressions (`49706137`).

#### Lowering infrastructure

- **Collection pipeline lowering** (`84f3c2ab`, resolves #344)
- **Optional-chain lowering** (`800676e4`, resolves #342)
- **Scriptum interpolation lowering** (`502fbe0d`)
- Regex literal type through lowering and codegen (`051d0d13`)
- Proba statement lowering into test functions (`71d09d00`)
- Fix: faber-path control flow without error nodes (`b7761c0e`)
- Fix: reject unsupported `incipit argumenta` lowering (`7e906c3b`)

#### Semantic analysis and type system

New lint and significant type-checker hardening:

- **Borrow analysis**: lint `de`/`in`/`ex` mode misuse (`50ac5e73`, resolves #314); reduce false positives for normal flow (`b2466c35`).
- **Type inference**: infer empty arrays and relax `lista` literal compatibility (`e6808d37`); expression and variable inference improvements (`4b938d61`); `ab` inference through object-member collection sources (`9d2bad3d`).
- **Call/arity**: support optional params in call arity checks (`30269526`).
- **Enum handling**: allow enum variants in `elige` case values (`09934e95`).
- **Member access**: support beyond struct-only checks (`db20b0d4`).
- **Method calls**: fix condition typing and statement inference fallback (`6cc37118`).
- **Extern declarations**: support `externa` declarations and duplicate import module bindings (`54e41765`).
- **Destructuring**: fix mutable `ex` destructuring assignment type checks (`639df8b6`).
- **False positive reduction**: unknown identifier resolution (`86dbf9a8`), type mismatch in checker (`3a2b9d2d`), unknown type forms (resolves #345, `e3d75a46`).
- **Lvalue typing**: correct typing for `ego` fields and indices (`1726c748`).
- **Binary/unary operators**: support previously missing operators (`20e1ff90`).
- **Codegen gate**: allow codegen when semantic diagnostics are only warnings (`f3a8726b`).
- **Expression flows**: support `qua`, `innatum`, and `vel` expression flows (`f83f6247`); preserve numeric flow for destructures and method returns (`b7eb505b`).
- Remaining exempla long-tail failures resolved (`8489b82f`).
- Fix exempla: correct `curator` param to `curata` modifier in `validatio.fab` (`f48b6cb0`).

#### Faber codegen corrections

- Lower faber-path control flow without error nodes (`b7761c0e`)
- Preserve object fields in innatum output (`f59b443a`)
- Avoid nested `casu` blocks (`a52c748a`)
- Emit canonical `si`/`sin`/`secus` and `reddit` (`3fc1cee9`)
- Preserve parameter names (`342de036`)

#### Build and tooling

- Replace rivus-centric build script with radix-rs focused pipeline (`66b918fb`, old script preserved as `build-bootstrap.ts`).
- `Permissive mode` for semantic check (`0846ef7f`, resolves #331) — useful for partial compilation.
- Fix `rustc` verify: writable temp path and error summary (`f62f1b24`).
- HIR lowering coverage cleanup (`2ef9f57b`, resolves #316).
- Tighten `ignotum` handling and unresolved type output (`51d50dbd`, resolves #317).
- Enforce Unicode XID identifiers and NFC interning (`f2b687e2`, resolves #315).

#### Agents and documentation

- **`rust-correctness-surgeon`** agent: purpose-built Claude agent for radix-rs correctness work (`769a0cd4`).
- **`technical-writer`** agent: agent for code documentation passes (`9db8fed8`).
- **Comprehensive rustdoc pass**: `//!` module-level docs, `///` rustdoc, section dividers, and WHY-focused inline comments across all 51 non-test source files (`d54239a4`).
- Archive obsolete `faber-ts` reference implementation (`8669a4bb`).
- Update README and AGENTS.md for current project state (`fec7401a`).

#### Refactoring and code health

- Unify primitive and collection type helpers (`25f621a3`).
- Extract lexer emit/operator/radix helpers (`a3324475`).
- Simplify `RustOutput` to code-only (`2ba94de9`).
- `cargo fmt` + resolve all clippy warnings (`603a8a4d`, `9a4af321`).

#### Test coverage

- Safe CLI path coverage (`f30a7ac3`)
- Source file utility coverage (`a1016349`)
- Session config and compiler entrypoints (`8fddc80d`)
- Driver pipeline coverage for compile flow (`ee15106c`)
- Rust expr/types coverage with focused unit cases (`b9ec7443`)
- Rust codegen context wiring coverage (`eca48f0a`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
