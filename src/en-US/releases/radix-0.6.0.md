+++
title = "Radix 0.6.0"
section = "releases"
order = 94
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.6.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

Major release spanning **313 non-merge commits** (`v0.5.0..v0.6.0`). This
release adds Python and C++23 codegen targets, a complete YAML-based cross-target
test framework (~2500+ tests), a unified stdlib registry system with explicit
allocator plumbing, the Fab (canonical Faber source) codegen target, and dozens
of new language features including regex literals, variant matching, streams,
collection filtering DSL, bitwise operators, array destructuring, spread/rest,
and break/continue. The event system and WASM codegen are removed.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 313 |
| Date span | 2025-12-24 → 2025-12-30 |
| Codegen-target commits | ~109 |
| Test-infrastructure commits | ~54 |
| Design-doc commits | ~33 |
| Parser/lexer/grammar commits | ~27 |
| Format/lint commits | ~21 |
| Preposition/keyword commits | ~21 |

### Major tracks

#### New codegen targets: Python and C++23, Fab (canonical Faber)

- **Python** codegen target with full type system, enums, preamble infrastructure,
  break/continue (rumpe/perge), lista (list), tabula (dict), copia (set) methods,
  async bindings (figendum/variandum), nexum (reactive fields), spread/rest, and
  lambda handling (`2931d5266`, `34f33f3e8`, `d06d22d92`, `6f8f78725`,
  `36dcf3104`, `181dbdad4`, `b5baa4b7c`)
- **C++23** codegen target with `===` operator support, collection stdlib, and
  auto-merge constructor (`f8e65b354`, `cfe0f07fe`)
- **Fab** codegen target for emitting canonical Faber source, with full test
  expectations across all test cases (`1dd33f8a2`, `2247115b2`)
- TypeScript codegen marked complete — all generated targets reach parity
  (`cf49a58c9`)
- Python test coverage milestones: 85% (125 tests), then 95% with async
  bindings and nexum (`1191ce716`, `d08175e06`, `5aa1de505`)
- Modular codegen architecture: extracted per-node handler files into generator
  classes for TS, Zig, C++, Rust (`ac7f52e09`, `89bff39f2`, `36189a28f`,
  `e538186e2`)
- Added `fabrica/` demo projects for TS, Zig, C++ and `fabrica/ISSUES.md`
  documenting codegen limitations (`61572652d`, `0ed270b7c`)

#### Stdlib refactor: unified registries with explicit allocators

Three-phase refactor replacing per-target ad-hoc collection implementations with
unified registries:

1. **Phase 1**: Unified `Lista` registry with explicit allocator plumbing
   (`a1fff7fbd`)
2. **Phase 2a/2b**: Unified `Tabula` and `Copia` registries (`ff2d79324`,
   `ef52d8187`)
3. **Phase 3**: Wire all targets to the unified registries — preamble generation
   uses external files and `RequiredFeatures` (`2e0605dd3`, `a48767ed2`)

Supporting changes:
- Preamble rework design document (`d76a63ff4`)
- Zig native runtime architecture proposal (`1ca9ec9fd`)
- External `build.zig` and `mod.zig` files (`85a59a0a5`)
- `aleator` (random) module for Zig, Rust, C++ (`15d8ee381`)
- `tempus` (time) module for Python, C++, Rust, Zig (`66e6ece9e`, `c80a2487d`)
- `mathesis` (math) module for Rust, Zig, C++ (`2b29f0426`, `87bf924cd`)
- I/O intrinsics for all targets (`96d8c5a47`)

#### Entry points: initium → incipit, incipiet (async entry)

- Renamed `initium` to `incipit` across all codegen targets, exempla, parser,
  AST, and lexicon (`bd221ca2b`, `58608f896`)
- Added `incipiet` (async entry point) with per-target codegen and ergo chaining
  form (`e79e5a126`)
- Added `initium` entry point statement (pre-rename) (`5e57ce509`)
- Tests for incipit and incipiet (`ef6e2968e`)
- Incipit facade examples for all codegen targets (`dc626d1f3`)

#### Resource management (cura/curator)

- Redesigned `cura` syntax with explicit curator kinds: arena and page
  (`eb4a5ac6f`, `0a739faf1`)
- Curator auto-injection for Zig target: semantic analyzer propagates arena
  allocator through call chains (`7e8b824e3`, `f5a367c95`)
- Require explicit `cura` blocks for Zig allocating operations (`d25da9092`)
- Arena/page allocator tests and semantic analyzer fixes (`e7cb39dbd`)
- Design docs: allocators, cura/curator/curatum roles (`92874360b`,
  `417c14eb9`, `7ffb12c65`, `67d2ffc4f`)
- Updated exempla to use `incipit ergo cura arena` for Zig compatibility
  (`506431554`)

#### Language features

**Regex literals**: Implemented `sed` /pattern/flags syntax with per-target
codegen support and design doc (`8092193b2`, `921f43750`, `ea2048316`,
`10ca81cf2`). Removed `g` flag from regex design (`854d08a05`).

**Database DSL**: Renamed `tabularium` to `arca` for database DSL (`505e032a3`)

**Variant matching**: `discerne` statement for variant matching, paired with
`discretio` for tagged union patterns (`d4c820d98`, `ee0ecbdb9`)

**Streams (flumina)**: Three-phase flumina protocol — `fiunt` (multi-value
streams), `fiet`/`fient` (async streams), TS codegen for `fit` functions,
streams-first design doc (`a6167aec1`, `a0eb16e4a`, `a99915709`, `f3ac0f68e`)

**Dispatch (ad)**: `ad` statement for dispatch with design doc and per-target
codegen (`584cc71b9`, `7ffb12c65`)

**Collection filtering DSL**: `ab` expression for collection filtering with
design doc (`b16d5a794`, `a46303860`)

**Sequence operators**:
- Compound assignment (`+=`, `-=`, `*=`, `/=`, `&=`, `|=`) (`809e5a829`)
- Bitwise operators (`&`, `|`, `^`, `~`, `<<`, `>>`) (`606021a55`)
- `ante`/`usque` range operators for explicit exclusive/inclusive semantics
  (`9a6f1efce`)
- Change range expressions to exclusive-end semantics (`17528cdd0`)
- Negative indices and slicing support for all targets (`bea7c1799`)
- Array destructuring support for all targets (`d1447c146`)
- `sparge` (spread) and `ceteri` (rest) operators (`0fa8b9b40`)
- `vel` nullish coalescing operator and CLI stdin support (`f41b74a46`)
- `?.` optional chaining and `!.` non-null assertion (`3d7eb61ff`, `910d694a7`)
- Hex literal support (`0xFF`, `0xFFn`) (`00d40b94a`)
- `:` shorthand for lambda expressions (`pro x: expr`) (`027408abf`)
- Lambda return type annotation syntax (`pro x -> Type: expr`) (`df4d3ac4e`)
- Async lambda syntax: `fiet x: expr`, `fit x: expr` (`84289ddb5`)
- Default parameter values with `vel` (`83b36e535`)
- Dual parameter naming with `ut` alias (`efcc1e99e`)
- Separate arrow and verb syntax for function return types (`373f4aed7`)
- `break`/`continue` (`rumpe`/`perge`) for all targets, including Zig codegen
  (`da17263ac`, `806f44d1e`)

**Compile-time evaluation**: `prae` compile-time evaluation (`prae typus`,
`praefixum`) with design doc (`b772b0898`, `fc4fde49e`). Graceful degradation
for TS/Python (`3374ff7ed`).

#### Type system

- `unio<A, B>` union types for TS, Python, and Zig (`7c43c4217`, `af02493f9`)
- `discretio` (tagged unions) with pattern matching (`6ad3e15fc`)
- `magnus` (bigint) type for TS and Python (`13f55efca`, `6208cca00`)
- `ignotum` (unknown) type mapping for TS and Python (`2fd03da4e`)
- `numquam` (never) type mapping for TS and Python (`6c2f3eba1`)
- `est` type checking operator, `typus` RHS typeof, `nihil`/`nonnihil` operators
  (`660cd4b66`)
- `ut` (type cast) operator for type assertions (`a13efa238`)
- `supra()` as Latin equivalent of `super()` (`c76140dfb`)
- Design docs: new type features (`cd2570cb6`), aperit keyword for index
  signatures (`5255afeba`)

#### Preposition system (praepositiones)

- Unified Latin preposition system with `praepositiones.md` design doc
  (`e89cebe47`)
- Refined roles: `ad` for dispatch, `pro` for binding; removed `ad` from params
  (`425d84f5d`)
- `qua` replaces `ut` for type assertions, `ut` for aliasing
  (`d1a151b8f`, `33a4fdffb`, `95907fdd1`, `b3597aede`)
- `de`/`in` ownership prepositions for Rust and Zig codegen (`670a069ed`,
  `82f2738dd`)
- Removed `cum` keyword entirely; `in` for mutation blocks, `de` for for-in loops
  (`84be77479`, `05a46950a`)
- Ban `cum` from the language (`33a4fdffb`)
- `per` replaces `ad` for property shorthand in collections DSL (`dabdf8297`)
- Wildcard import alias support (`5b29247cc`)

#### Semantic analysis

- Validation for `cede`/`figendum`/`variandum` context (`a8543d18b`)
- Semantic analysis for `enum`, `genus`, and `pactum` declarations
  (`10c36c02c`)
- Fix semantic analyzer issues and exempla variable collision (`d8676f0bd`)
- `scriptum()` for cross-target string formatting (`f796021fb`)
- `@target` filter syntax and implementation stats (`adffc28fc`)

#### Removals

| Removal | Commit |
| --- | --- |
| Event system (`ausculta`/`emitte`) | `1242ac75f`, `88ef66da9` |
| WASM codegen target (862 lines removed) | `938f32529` |
| `cum` keyword | `05a46950a`, `33a4fdffb` |
| Computed properties (getters) | `25f78d9a2`, `6e48dd709` |
| `jsType` from lexicon (use `meaning` instead) | `a92766c30` |
| `<T>` array syntax (replace with `T[]`) | `2907601f4` |
| Old exempla directories | `c38ca847b` |
| Redundant legacy test files | `fc4ad1928` |
| Test fabrications | `a8108dc99` |

#### Design docs and consilia reorganization

- Reorganized `consilia/`: moved 10 completed docs to `consilia/completa/`, 3
  planned docs to `consilia/futura/`, merged `fasciculus.md` into `solum.md`
  (`7cbef99ae`)
- Moved stdlib designs to `norma/` subdirectory (`bf4a4277c`)
- Moved and compressed `flumina.md` to main consilia directory (`9f7243319`)
- Archived `eventus.md` design doc (`2398e79c7`)
- Added design docs: Zig async via Responsum state machines (`37e27a5f5`),
  comment preservation (`73189f77d`), Faber codegen target (`579d8eac1`),
  TS-to-Faber transpiler (`d06be1cf8`, `4075e9b26`), two-pass compilation
  (`565f112a2`), array destructuring (`00ebefc41`), operators (`4aa09c071`),
  test syntax (`ae03ba520`)
- Nucleus design: micro-kernel runtime for unified async/I/O (`2eec2c5e1`),
  Monk OS analysis (`0040e3931`), Responsum protocol (`707d1ea2e`)
- Updated `binario.md` final design decisions (`1eb9d655e`)
- Rewrote `operators.md` with complete reference (`a6c158417`)
- Updated `consilia/clausura.md` with target-by-target implementation status
  (`aa82c1e78`)

#### Test infrastructure (proba/)

- YAML-based cross-target codegen tests: shared format running same cases against
  multiple targets, 250+ tests across 8 domains (`557f97e9c`)
- Complete YAML test migration with per-target expectations for TS, Zig, Python,
  C++ (`f21f8072b`, `e38b36e0a`, `7d21cd9e6`, `417c83dc7`, `0275afdb3`)
- Comments on every YAML test describing each case (`e0b660c11`)
- Recursive test structure with modern format support (`300d4c32a`)
- Expression test files in modern format (`c901c2c6e`)
- Comprehensive statement codegen tests — 816 tests (`617bf6de4`)
- 200+ edge case tests across all codegen test files (`502b9bb28`)
- Errata test support for expected compilation errors (`a08647b5e`)
- Coverage reports and strict mode (`48ff2b4cf`, `113f9aa00`)
- Rust test expectations and validation pipeline (`e30570bd1`)
- Zig test expectations and dead code removal (`5d4d4fa3c`)
- Move codegen tests to `proba/` at project root (`77cf944d0`)
- `proba/README.md` documenting test framework (`8a2355996`)
- Updated proba README with `norma/` directory structure (`abd0e245f`)
- Moved stdlib tests to `proba/norma/` (`2863e6918`)
- Expect-failure tests for invalid syntax patterns (`a355ba852`)
- TS codegen tests split into modular domain files (`15d9bda69`)
- Zig expectations added to cura tests (`6ea7e0a40`)

#### Zig codegen

- Error handling: `iace` → error unions, `mori` → panic (`5acd4a68d`)
- Collection methods (lista, tabula, copia) (`b16b28142`, `955130e1d`)
- For-range native syntax (`8fb7a169d`)
- Remove auto-generated `main()` and `m_` prefix (`300b75283`)
- Preamble emits imports instead of inlining stdlib (`44fba8526`)
- Emit compile error for `objectum`/`anytype` return types (`df4d3ac4e`)
- String switch detection by checking case literals (`5beb90408`)
- If-else chains instead of switch (`1f27b2aca`)
- Division/modulo operators and exempla script fix (`a062f3feb`)
- Unused alloc warning and stepped range redeclaration fix (`cd6e6397d`)
- Array literals: `[_]T{}` when element type is known (`dd543633c`)
- All 44 exempla passing (100%) (`6b1e7e495`)
- Refactored expressions to guard clauses with tests (`e71c24572`)
- Module constants prefix with `m_` to avoid parameter shadowing
  (`72c48eb54`)
- Map `===` to `==` and `!==` to `!=` (`43152756e`)
- Zig codegen failure categories documented in `consilia/codegen/zig.md`
  (`d125a9c38`)

#### Rust codegen

- Full collection methods: lista (Vec), tabula (HashMap), copia (HashSet)
  (`9bb34cc9f`, `80e12df45`, `0eb491aab`, `0bdef6f2b`, `70f250a84`)
- `de`/`in` preposition handling for ownership (`670a069ed`)
- Lambda return types and numerus type mapping fix (`a57a98e8d`)
- Main wrapper, println format, test updates (`dbf88f526`)
- Fix Rust lista `RsGenerator` type signature (`5999e79ed`)

#### CLI and tooling

- Default to stdin with flexible option order (`10e24783d`)
- `faber check -t zig` target validation (`f6e976734`)
- `verify:exempla` script for quick pass/fail per target (`e709f6d48`)
- `--force` flag to continue despite test failures (`9fc897b06`)
- Unbundled CLI for exempla script (`59ae3328a`)
- `prettier` for formatting (`20432d549`, `502b9bb28`)

#### Rivus

- Added `rivus/` directory as a Faber language compiler with lexicon files:
  nomina, typi, typi_constructi, verba, verba_clavium (1479 lines) (`1e460c3dc`)

#### Agent and documentation

- `AGENTS.md` symlink (`300a44a2c`)
- Rewrote `CLAUDE.md` for accuracy and conciseness, trimmed from 235 to 163
  lines, added Latin phrase guidance and agent delegation guidance (`09958958e`,
  `2cb19d9e8`, `8b9203714`, `e6b3b3ef9`)
- Added `pragmatic simplicity` to project philosophy (`6fd506610`)

#### Exempla restructuring

- Relocated `ex-pro` to `ex` (`ec8f8b63d`)
- Added `exempla/expressions/` with buildable program files (`a9f425c5f`)
- Added `exempla/statements/` with comprehensive buildable files for all
  statements (`4f62a5f86`, `496f17719`, `06a57d1f5`)
- Added `exempla/errores/` for 1:1 mapping with grammatica/ (`af46095c1`)
- Added `grammatica/` directory and `GRAMMAR.md` for language reference
  (`8edf0ec60`)
- Cleaned up exempla/ files and added `ego.fab` (`1d40b3fdb`)
- Fixed exempla compilation errors (`74c80073a`)

#### Grammar updates

- Updated `GRAMMAR.md` and grammar extraction (`efd059b1b`, `12248482e`,
  `8463039eb`, `89bf930fe`, `96f582057`, `8bc31e952`, `e7b45cca1`,
  `2362e59ac`, `c0b8fd46e`)
- Fix grammar extraction to preserve whitespace correctly (`f8865a523`)
- Renamed AST node types to Latin-facing names (`91b28aeca`)
- Renamed parser functions to match Latin keywords (`9897368c7`)
- Added target mappings to AST node documentation (`90f5fd7e4`)

#### README documentation

- Added implementation completion summary table (`58ee671d4`)
- Fixed feature coverage metric: use feature coverage instead of exempla pass
  rate (`9626d173c`)
- Updated README implementation status with comprehensive corrections and
  additions (`dcc5e5d72`)
- Multiple progress updates: Python milestones, Rust stdlib, C++ mathesis
  (`48f5e8d9c`, `18b785355`)

### Other changes

- Make keywords and types case-sensitive (`2690e5310`)
- Document indexed iteration syntax and `per` property shorthand (`8111ec987`)
- Fix 73 failing tests across tokenizer, parser, and codegen (`0e0ffc039`)
- Fix keyword collision in member expressions (`09e1d6208`)
- Fix TS strict mode errors in source files (`302f704d6`, `639197134`,
  `e0d4ecd64`)
- Fix parser infinite loop on invalid syntax (`b5baa4b7c`)
- Fix custom type parsing (`5b29247cc`)
- Fix method handler architecture to preserve argument boundaries (`2dc8abdc7`)
- Use Latin keywords in parser error enum names and messages (`33a4fdffb`)
- Comment pass-through in codegen (`97502682a`)
- Arrow binding for direct codegen escape hatch (`d74a23a80`)
- Document borrowed return types with `ex` source specifier (`41c68dd82`)
- Reframe project as LLM intermediate language (`a334deae4`)

### Breaking / author-visible

| Change | Migration |
| --- | --- |
| `initium` renamed to `incipit` | Rename all `initium` keywords to `incipit` |
| Event system removed (`ausculta`/`emitte`) | Remove usage; no replacement |
| WASM codegen target removed | Use another target |
| `cum` keyword banned | Use `novum X { }` or `novum X de expr` |
| Computed properties (getters) removed | Use methods instead |
| `ut` changed from type cast to alias | Use `qua` for type assertions |
| `<T>` array syntax removed | Use `T[]` syntax |
| Range expressions now exclusive-end by default | Remove `- 1` from end bounds |
| JavaScript `jsType` field removed from lexicon | Use `meaning` field instead |

---

[All releases](/releases/) · [Install the current release](/start/install.html)
