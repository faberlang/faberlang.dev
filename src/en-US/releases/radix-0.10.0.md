+++
title = "Radix 0.10.0"
section = "releases"
order = 89
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.10.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

The bootstrap compiler reaches completion: all 25 `.fab` source files compile and
generate valid TypeScript. On the language side this release replaces inline
modifiers with `@` annotations, replaces `//`/`/* */` comments with `#`, allows
keywords as identifiers, and simplifies the conditional keyword set.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 26 |
| Date span | 2025-12-31 |

### Major tracks

#### AST restructure as `discretio` variants (`ab88bbb07`, `be9a663de`)

Unified the AST into two single-file discriminated unions: `Expressia` (24
tag-based variants) and `Sententia` (31 tag-based variants). Deleted 18
subdirectory files under `fons-fab/ast/expressia/` and `fons-fab/ast/sententia/`.
Generated TypeScript uses `finge … qua Expressia` → `{ tag: 'Littera', … }`.
Parser files updated to use real AST imports and `finge` construction.

#### Bootstrap parser complete (`3a38320bb`, `e282e1881`, `81830d153`, `fcf206ede`)

- **Statement parsers:** Adds `fluxus.fab` (elige, discerne, custodi),
  `initus.fab` (incipit/incipiet, cura, ad), `imperium.fab` (si, dum, ex, de),
  and `declara.fab` (functio, genus, pactum, ordo, discretio, typus, importa).
  All 25 bootstrap `.fab` files compile without errors.
- **Expression parsers:** Implements `parseObiectumExpressia()` with key-value,
  computed keys, shorthand, and spread. Implements `parseLambdaExpressia()` with
  params and optional return type.
- **Parser wiring:** Introduces the `Parsator` genus (concrete `Resolvitor`
  implementation) to complete parser mutual recursion. Wires `expressia()` to
  the full precedence chain and `sententia()` to the statement dispatcher.

#### `@` annotation system (`270282151`, `b17a3e93b`, `0db5c1723`, `a0e2e1c40`, `252910bb4`, `cf9245e95`)

Replaces inline modifier keywords with line-oriented `@` annotations:

- Adds `AT` token to the tokenizer.
- Adds `Annotation` AST node with a modifiers array.
- **New syntax:** `@ publicum`, `@ privatum`, `@ abstracta`, `@ futura`,
  `@ cursor`, `@ generis`.
- **Visibility inversion:** Default visibility changes to private; exports
  require `@ publicum`.
- **Clean break:** Removes inline `functio f() futura cursor` syntax entirely.
  All codegen targets (TS, Python, Rust, Zig, C++, Fab) read async/generator
  state from annotations only.
- Updates all docs, EBNF grammar, and `grammatica/` files to use `@` syntax.

#### `#` line comment syntax (`b31a574ca`, `db818021c`, `302de08d7`, `dd7062c1c`, `3f699822b`)

Replaces C++-style `//` and `/* */` with Python/Shell-style `#`:

- Adds `#` as a line comment indicator.
- Removes `//` and `/* */` parsing entirely — this is a breaking change.
- Simplifies `CommentType` to a single `'line'` variant; no block or doc
  variants remain.
- Migrates all 55 exempla files, all 28 bootstrap compiler `.fab` files, the
  Zed grammar tree-sitter source, Zig runtime libraries, and 140+ consilia doc
  files. Roughly 3,000 lines changed across 143 files.

#### Keywords as identifiers (`37b7ae488`, `0a0b97fb6`, `d07260729`)

Keywords like `typus`, `genus`, `signum`, `textus` can now be used as variable
names, field names, and parameter names. Removes the keyword-conflicts gotcha
from documentation. Also allows `cape`/`demum` as identifiers in expression
context — these are contextual keywords that should not block ordinary names.

#### Conditional syntax cleanup (`114b2fc0f`, `961fd78b5`)

Removes the `aliter` keyword. The conditional keyword set is now:

- `si` = if
- `sin` = else if ("but if")
- `secus` = else ("otherwise")

`secus` already served double duty in ternary expressions (`sic x secus y`), so
this consolidates the "otherwise" concept to a single word. Eliminates the
duplicate `ExpectedKeywordAliter` / `ExpectedKeywordSecus` error codes.

#### Sync function syntax in bootstrap (`10d5f0637`)

Switches bootstrap compiler from `fit` (generator-wrapper semantics) to `->`
(direct returns). The compiler is fully synchronous and should not use generator
wrapping.

#### Design docs (`e58f908c3`, `54dcc142b`, `47d23a877`)

- Adds design doc for `publicus` module exports (`consilia/futura/publica.md`).
- Adds `@ generis` examples with proper Latin adjective order.
- Documents missing `longitudo` → `length` translation for property accesses on
  `lista`/`tabula`/`copia` (BUG comment).

---

[All releases](/releases/) · [Install the current release](/start/install.html)
