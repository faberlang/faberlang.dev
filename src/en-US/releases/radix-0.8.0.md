+++
title = "Radix 0.8.0"
section = "releases"
order = 91
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.8.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

Minor release spanning bootstrap Phase 5 (Faber-in-Faber compiler) and several
language-level changes including a **breaking** modifier syntax migration,
contextual keyword resolution, and new test-hook keywords.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 16 |
| Date span | 2025-12-30 → 2025-12-31 |

### Major tracks

#### Bootstrap Phase 5 — TypeScript → Faber AST port

The bootstrap compiler (`fons-fab/`) tracks all 92 TypeScript AST types as
native Faber definitions across expressia, sententia, and lexema surfaces.

- Adds `positio` (position) and `lexema` (token) types plus a Zig codegen fix
  for enum member naming (`2f1782649`)
- Renames AST files to Latin and adds `radix/expressia/{nomen,littera}` —
  identifier and literal types (`2e9eae7e9`)
- Completes the expressia subtree: `operatio` (binary), `vocatio` (call),
  `collectio` (collection), `lambda`, and `index` (`e0340a42f`)
- Latinizes all bootstrap AST type names, field names, and enums across
  expressia, lexema, positio, and radix (`d4fd17697`)
- Adds all sententia (statement) types: functio, genus, actio, discretio,
  error, imperium, ordo, proba, varia (`51c64cd5d`)
- Fills remaining expressia gaps: `ObiectumForma`, `CatenaExpressia`,
  `PraefixumExpressia` (`561dc8846`)
- Implements the bootstrap `Lexor` (tokenizer) module with keyword lookup,
  error codes, and a `lexare()` entry point; fixes Zig `getCurator()` default
  from throwing to returning `'alloc'` (`78d91db90`)
- Documents bootstrap patterns and adds inline code comments to the lexor
  (`b85a7703a`)
- Adds Phase 5 bootstrap analysis with effort estimates, structural
  challenges, and blocking issues to `consilia/bootstrap.md` (`b99ed3735`)

#### Language: postfix function modifiers and `curata` keyword

**BREAKING:** Function modifiers (`futura`, `cursor`) move from prefix to
postfix position — declarations now start with `functio` uniformly.

```text
# Before
futura functio fetch(url) -> Response

# After
functio fetch(url) futura -> Response
```

Adds the `curata` modifier for allocator-managed functions. A function
declared `curata alloc` receives an allocator bound to the given name; call
sites must be inside a `cura` block. (`14bb1368d`)

#### Language: contextual keyword resolution

Implements the `reserved-conflicts.md` design: keywords are accepted as
identifiers in positions where context disambiguates intent — field names in
genus declarations, parameter names, loop variables, catch parameters,
discerne variant bindings, lambda parameters, and object keys. Structural
contexts (statement start, declarations) remain strict. (`b4011e2e7`)

#### Test syntax: `praepara` / `postpara` test hooks

Replaces the overloaded `cura` test-hook keywords (`cura ante`, `cura post`)
with dedicated `praepara` / `postpara` keyword pairs. Adds `-bit` suffix for
async variants (`praeparabit`, `postparabit`). `cura` is now resource-
management only. Updates all codegen targets (TS, Python, Rust, C++, Zig,
Faber). (`5dc13f073`)

Corresponding bootstrap AST rename: `CuraMassa` → `PraeparaMassa` with a
`PraeparaTempus` enum (`c3987f751`).

#### Zig codegen: `self.alloc` pattern for collection fields

Structs with `lista`/`tabula`/`copia` fields automatically add an
`alloc: std.mem.Allocator` field, `init()` takes an allocator as the first
parameter, and methods use `self.alloc` for collection operations.
(`1a4793b02`)

### Other changes

- Simplifies bootstrap field names from compound workarounds to plain
  identifiers (e.g. `typusAdnotatio` → `typus`) now that contextual keyword
  resolution is available (`450f054a3`)
- Removes `consilia/futura/reserved-conflicts.md` — its design has been
  implemented in commit `b4011e2` (`1ac7617c8`)

---

[All releases](/releases/) · [Install the current release](/start/install.html)
