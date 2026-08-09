+++
title = "Radix 0.14.0"
section = "releases"
order = 83
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.14.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

Release spanning **114 non-merge commits** (`v0.13.0..v0.14.0`). This is a
high-velocity **bootstrap-compiler (Rivus) push** with the first morphology
system, multi-target codegen progress, and foundational parser expansion.
The Faber compiler received P0/P1 fixes and a build-infra rewrite.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 114 |
| Date span | 2026-01-02 → 2026-01-05 |

### Major tracks

#### Morphology system (Rivus)

The first verb-morphology system for the bootstrap compiler, using Latin verb
endings to determine collection-method semantics:

- **Verb conjugation dispatch**: Imperative endings (`-a`, `-e`, `-i`) mutate in
  place; perfect participles (`-ata`, `-ita`, `-sa`) return a new collection;
  future participles (`-atura`, `-itura`) are async returning; future indicative
  (`-abit`, `-ebit`) is async mutating (`81feafefb`)
- **Morphology registry**: Receiver-bound method dispatch with built-in `lista`
  morphology registration (add, filtr, mapp, etc.) (`300e09f07`, `e64456b66`)
- **Radices (stem dictionary)**: Central stem dictionary with TS generators
  (`81feafefb`)
- **Canonical verbum IDs**: `VerbumId` keyword dispatch expanded with dialect
  plumbing for return-verb specialization (`b33ef5750`, `665758dee`, `f8af94086`)
- **Latinized generator fields**: `codegen/radices.fab` maps Latin keyword IDs
  to generator methods (`a6212043b`)
- **Design docs**: Morphologia proposal, Opus 4.5 / GLM 4.7 / Gemini 3 reviews,
  IO-domains and Zig-codegen expansion (`13c0cb0c3`, `f30287e06`, `87bd8e4de`,
  `3760072b3`, `8c4dc480f`, `0000f559b`)

#### Rivus parser expansion

Substantial expansion of the Rivus bootstrap parser to handle more Faber
constructs:

- **Bitwise operators**: `|`, `^`, `&`, `<<`, `>>`, `>>>` with C/JS precedence in
  the expression parser (`382601b1b`)
- **`verum` / `falsum` / `nihil` literal recognition**: Fix keyword literal
  detection using `probaVerbum()` instead of token-type checking
  (`33db4d755`)
- **`verum`/`falsum` unary operators**: Prefix operators for strict boolean
  equality checks (`=== true` / `=== false`) (`4afb5c5f7`, `f54dd7c89`)
- **`innatum` keyword**: Native type construction for `lista` and `tabula`
  literals, replacing `qua` (type assertion → constructor) (`b12c00c1f`,
  `edc3d09df`)
- **Multi-discriminant pattern matching**: `discerne a, b { casu X, Y { … } }`
  with exhaustiveness checking, wildcard patterns, per-pattern binding
  (`08cbb9a2d`, `32b70d0d5`)
- **Optional chaining and primary expressions**: `?.`, `??`, short-form arrow
  bodies, catch clause parsing (`ee053486b`, `ae8c82ba0`)
- **Core expression parsing**: Ranges, unary ops, binary op chain, member access,
  chaining alignment with Faber parser (`9fa15a4b3`, `d14473b38`, `62c00d6f4`)
- **`probandum`/`proba` parsing**: Test/assert expressions in the parser
  (`0995ea0ff`)
- **`praefixum` blocks and parenthesized expressions** (`6043f1b7b`)
- **Compound assignment tokens**: `+=`, `-=`, `*=`, etc. in the lexer and parser
  (`52071ee16`)
- **Template literals**: `Exemplar` token type with backtick codegen
  (`20cc6caec`)
- **Section sign (`§`) as interpolation placeholder**: Replaces `{}` to avoid
  brace-escape issues in codegen (`98c2dbabb`, `c51add25b`, `472b84a74`)
- **Parameter parsing**: Preposition-based and type-first parameter expansion
  (`529440025`)
- **Expression fixes**: Contextual typing, finge field key typing, novum/object
  spread, unary nihil/iace alignment, short-form body parsing improvements,
  comma-token usage fix, `scriba` multi-arg parsing correction, `proba`
  `futurum` name handling (`3d1e8db37`, `9a0d9e03a`, `4af76ea34`,
  `574665f0a`, `f66b4c887`, `6d0935b9b`, `9ad7ec94c`, `02c0da02f`,
  `22b12bca9`, `a2a5e3c3a`)
- **Parser refactors**: `errores.fab` novum construction cleanup; `verum`/
  `falsum`/`nihil` tokenized as literal tokens; `VerbumId` helpers split
  with reddit shorthand mapping; `qua` casts wrapped in parentheses
  (`88cee9a65`, `eac93a02d`, `113c5eaac`, `63daebedd`, `5d07b0e7c`)
- **Parser coverage expansion**: Lambda parsing and mutation-operator
  coverage improvements (`0fa85dea0`)

#### Rivus codegen refactor

Major codebase reorganization and expansion of the bootstrap compiler's codegen:

- **Split into individual files**: Monolithic `index.fab` files broken into
  per-statement and per-expression modules for both TS and Zig codegen. TS
  `sententia/index.fab` dropped from 1384→225 lines across 24 files
  (`17c3422d8`)
- **Zig codegen foundation**: Full Zig codegen with type mapping, statement
  handlers, expression handlers, `rivus-zig` CLI script (`c3f2d2f04`,
  `f7c4d39ad`, `a6212043b`, `f8388d387`)
- **`@externa` annotation**: External declaration support for FFI boundaries in
  both the TS and Zig codegen backends (`5ba1d6998`, `9fa870fdc`)
- **Flumina preamble**: Async/effect runtime preamble emission for TS targets
  (`61caadff4`, `4eeb83954`)
- **Codegen fixes**: String literal quoting, regex slash escaping, templating
  alignment, `cura` (resource) statement codegen, return-verb wrapping,
  `genus`/`tempta` codegen alignment, bootstrap test conformance, parser/
  codegen gap fixes with in-process tests (`8189d95d3`, `91b8cac56`,
  `76c3e8cbf`, `fbd3d4ca2`, `bda952455`, `f6b7b723b`, `736016eed`,
  `322f6b0ce`, `04d622d1e`, `69a46fa2a`, `87a90602a`)

#### Faber compiler fixes

Stability improvements for the reference (TypeScript) compiler:

- **P0 blocker fixes**: Parser infinite loop and semantic analysis gaps
  (`b3c54d52d`)
- **P1 fixes**: Expression type inference and `ad` statement codegen
  (`b4ed625e0`)
- **Circular imports**: Allowed in the semantic analyzer for mutually
  recursive definitions (`9de4cfc08`)
- **Preamble inlining**: External `.txt` preamble files converted to inline
  string constants for bundled binary compatibility (`0d6ba74dd`)
- **`build:exempla` script**: Compiles all exempla through both compilers
  (`c4b2c3214`)

#### Exhaustiveness and pattern matching

- **Exhaustiveness checking**: Semantic error S017 for non-exhaustive `discerne`
  statements; all variants must be handled (`32b70d0d5`)
- **Rivus `typi discerne` refactor**: 72-line reduction in the semantic
  exhaustiveness analyzer (`769437955`)
- **Discerne alias bindings**: Multi-pattern alias support (`6d0935b9b`)

#### Module system

- **Local file import resolution**: `modulus.fab` resolves `./path` imports,
  extracts exports, caches modules, pre-declares symbols (`37a22693b`)
- **Standard comments and section headers** across the Rivus codebase
  (`7428a5682`)
- **File-level test skipping**: `rivus: false` metadata to skip YAML test files
  (`16c91123d`)
- **Intrinsic function test exclusion**: `rivus: false` exclusion for intrinsic
  functions (`8e5fff425`)

#### Build infrastructure

- **Build scripts rewritten in TypeScript**: `build-faber.ts` and `build-rivus.ts`
  replace bash scripts; parallel compilation via `Promise.all` (~3× faster);
  `-t`/`--target` flag for multi-target builds (`023c2db7a`)
- **Typecheck script**: Full type error fixes across the codebase (`23a973ee3`)
- **Compiler flag to exempla script**: `-c` flag selects faber vs rivus
  (`8a3937ce9`)
- **Test rename**: `runner.test.ts` → `faber.test.ts` with `test:faber` npm
  script (`16e740304`)
- **Loose equality for null checks**: `nihil`/`nonnihil` uses `== null` / `!= null`
  for JS compatibility (`210421432`)

#### Documentation

- **Grammar regeneration**: Updated GRAMMAR.md and all `grammatica/` source files
  (`a440bd643`, `2bdc625fa`)
- **AGENTS.md restructured**: Comprehensive project layout (`b8011d816`)
- **PhD thesis**: Notes reworked into rigor plan; audience analysis and
  Claude Opus 4.5 / GLM 4.7 / GPT 5.2 reviews (`89f3ce792`, `684fc67c0`,
  `bf132441f`, `aec67bd38`)
- **Consilia updates**: Morphologia tasks moved to consilia/; implementation
  status moved to compiler-specific checklists (`f5c973d10`, `0c22c19d5`,
  `121616305`)
- **Design docs**: `externa` declarations design document; `importa-massa`
  real-world analysis; Rivus bootstrap-conformance target (`81bd6e5f5`,
  `e11097697`, `952aaa276`)
- **Code review document**: Created and updated with discerne-exhaustiveness
  status (`5de54a614`)

#### Other changes

- `@externa` annotation for Faber compiler semantic/TS codegen (`5ba1d6998`)
- `faber-lang-designer` agent updated with language reference section and
  `verba.md` cross-reference (`3d087149d`, `0e8013954`)
- `.gitignore` updated (`834341d6d`)
- `rivus` test runner made lenient about semantic errors for bootstrap
  testing (`203b9ae83`)
- `build:exempla` script with 224-line exempla compilation harness
  (`c4b2c3214`)
- Consilia cleanup / completion markers for `rivus-modules.md` and
  `discerne-multi.md` (`fffc2b23e`, `a83b15687`)
- `fons/faber` rename fix: completed incomplete rename for bundle path
  (`ef46ebda1`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
