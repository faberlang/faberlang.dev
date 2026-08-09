+++
title = "Radix 0.22.0"
section = "releases"
order = 75
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.22.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

Compact release spanning **37 non-merge commits** over a single day. Faber is
narrowed to a TypeScript-only reference compiler; rivus gains a Go codegen target
and a formal capability-validation system. The static-archive boundary is drawn:
broken RS/Zig/CPP codegens are moved out of the active tree, and the Faber
multi-target codegen is archived alongside them.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 37 |
| Date span | 2026-01-12 → 2026-01-13 |

### Major tracks

#### Faber: TypeScript-only, parser modularized

Faber is reduced from a multi-target compiler to a single TS-only reference
implementation. The full compiler-roles separation from the audit is now
enforced at the file-tree level.

- Archive 256 files (~14K lines) of Zig/Python/Rust/CPP/Faber codegen into
  `archivum/faber-codegen/` (`c7cd48c8e`)
- Simplify `CodegenTarget` to a single `'ts'` value; remove `-t/--target`
  from the CLI (`c7cd48c8e`)
- Simplify test runner to TS-only: 931 tests pass, no `@target` loops
  (`e1620d603`)
- Simplify test harness (`runner.ts`, `verify.ts`, `schema.ts`, `report.ts`)
  to single-target; delete `CHECKLIST.md` (`01e074140`)
- Delete unused `capabilities.ts`, `validator.ts`, and `feature-detector.ts`
  (`f7053c493`, `45fbf702f`)
- Extract TS-only `norma.gen.ts` from the full multi-target registry
  (`9ea12d25f`)

The parser is split from a 5778-line monolithic `index.ts` into 13 module
files, following the rivus parser pattern:

- Infrastructure: `resolver.ts`, `context.ts`, `types.ts`
- Expression modules: `binary.ts`, `unary.ts`, `primary.ts`, `dsl.ts`
- Statement modules: `declarations.ts`, `loops.ts`, `control.ts`, `variables.ts`
  (`868d38673`)

Modules are wired into `index.ts` and ~4000 lines of duplicated legacy code is
removed (`fe5594471`).

#### Rivus: Go codegen target

A full Go codegen target is added to rivus:

- Expression codegen (`index.fab`, `littera.fab`, `scriptum.fab`)
- Statement codegen (`functio.fab`, `incipit.fab`, `index.fab`, `redde.fab`,
  `scribe.fab`)
- Type system (`typus.fab`), nucleus, and capability registration
  (`4e084522a`)

Broken RS/Zig/CPP rivus codegens are archived out of the active tree into
`archivum/rivus-codegen/` (`4f3a4c5a3`).

#### Rivus: target capability system

A formal capability-validation system prevents codegen from producing invalid
output for targets that lack source-language features.

- `capacitas.fab`: Support matrix with four levels
  (Sustentum/Emulatum/Discrepans/Insustentum) and lowering models for all six
  targets (`38579ee9f`)
- `detector.fab`: AST visitor that detects used language features
  (`38579ee9f`)
- `validitor.fab`: Validates detected features against target capabilities
  (`38579ee9f`)
- `index.fab`: Public API (`generate()`, `validateOnly()`, `isCompatible()`)
  (`38579ee9f`)

Exhaustiveness checks added across the rivus codebase — silent `casu _ { }`
fallbacks replaced with explicit `ceterum { }` blocks so new AST variants cause
compile-time failures instead of silent fallthrough (`8bc7c8ece`, fixes #113).

#### iacit and moritor inline keywords

New inline `iacit` (throw) and `moritor` (return) keywords for case-body
expressions, letting case arms terminate concisely without block braces.

- Lexer tokens and parser integration in `fluxus.fab` and `initus.fab`
  (`448f47db9`)
- Support within control-flow expressions in `imperium.fab` (`078b2fbbb`)
- EBNF updated (`448f47db9`)
- Full YAML test suites: `iacit.yaml` (203 lines) and `moritor.yaml`
  (237 lines) (`d22797055`)

#### Rivus fixes

- **Discerne typing**: Export `discretio` variants and `pactum` method
  signatures so `discerne` bindings keep field types for `norma` translations
  (`fb08016e1`)
- **Ego resolution**: `ego` now uses `quaereSymbolum` to search parent scopes,
  fixing self-hosting inside method bodies (`2dfb1622f`)
- **Genus instantiation**: Use `novum` instead of implicit construction
  (`a80163b0c`, fixes #112)
- **Validation guards**: Add missing-type-information guards before codegen
  (`0673e5347`, fixes #115)
- **Silent fallbacks**: Replace comment-based fallbacks with `mori()` across
  all codegen targets (`a6be68bfb`, fixes #114)
- **de iteration**: Fix `de pro` iteration over `tabula` and `innatum tabula`
  keys (`01941e4be`)
- **Type narrowing**: Fix narrowing in namespace call handlers; resolve merge
  conflict markers in `vocatio.fab` (`bfcd3d76d`, `7aa1233ec`)

#### Lexor and parser extraction (rivus)

- Extract escape sequence and string-interpolation helpers from the lexor
  (`1c89b982d`)
- Extract numeric radix parsing helper (`2ff69b82d`)
- Extract variant and object-property parsing helpers from `primaria.fab`
  and `declara.fab` (`dc421d261`)

#### Null-check standardization

Null-check patterns across rivus unified to `nihil`/`nonnihil`. Updates span
lexicon, parser morphology, type semantics, and all codegen targets
(`e1928eeb6`).

#### Compiler audits and docs

- Comprehensive `faber` vs `rivus` audit results in `consilia/compiler-roles.md`
  (`827e64a0d`)
- `parser-gap-analysis.md` retained; redundant audit files removed
  (`f95e965b7`)

### Other changes

- Remove `nexum` reactive field modifier from lexer, parser, AST, codegen, and
  test expectations (`094214e69`)
- Fix `cape` (try-catch) codegen in both faber and rivus — wrap full if-else
  chain, add braces around catch body (`3a1d76204`)
- Fix `qua`/`copia` test expectations (`dcd9fc6e2`)
- Add test coverage for ternary, bitwise, `abstractus`, `nexum`, and `de` loop
  patterns (`b3eeae8b8`)
- Align EBNF unary grammar; document `~` unary operator (`24651f0a7`,
  `afafe4a68`)
- Fix grammar drift and `ab ubi` rewrite (`26515b8b7`)
- Update CI configuration (`f50ac1e32`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
