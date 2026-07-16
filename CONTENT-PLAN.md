# Content Plan — faberlang.dev

One page per topic below. Each page summarises and links to its source documents.
The index page provides a Wikipedia-style lead and links to each section hub.
Section hubs provide a brief overview and link to their sub-pages.

## Code block convention

All Faber source code on the site uses the following format:

```html
<pre class="faber-code" data-locale="la"><code>functio salve(textus nomen) → textus {
    redde "Salve, §!"(nomen)
}</code></pre>
```

- `class="faber-code"` — selector for CI extraction and build scripts
- `data-locale="<ISO code>"` — locale of the source (e.g. `la`, `th-TH`, `zh-Hans`, `ar`, `hi`, `vi`)
- Plain `<code>` inside — no syntax spans or inline styles
- CI validates every `faber-code` block via `faber check --reader-locale=$locale -`
- Future build script can render any block through `faber format --reader-locale=<X>` for multilingual site versions

---

## Section: History

| Page | Path | Source documents |
|---|---|---|
| History hub | `history/index.html` | TBD — no single history doc exists yet |
| Influences | `history/influences.html` | `README.md` (contrasts with AppleScript, COBOL, Rust, Go, TS, JAX), `docs/design/reader-locale.md` ("why this is not AppleScript") |
| Release history | `history/releases.html` | `radix/docs/release/` (directory of release notes) |

**Known gaps:** No coherent history document exists. Creator attribution, timeline, and
release history need to be compiled from release notes and git history.

---

## Section: Features

| Page | Path | Source documents |
|---|---|---|
| Features hub | `features/index.html` | Overview, links to sub-pages |
| Reader locale | `features/reader-locale.html` | `docs/design/reader-locale.md` (69 KB — primary), `examples/reader-locale/` (6 locale packages with localized source), `stdlib/reader/*/pack.toml` (7 installed packs), `README.md` (Reader Locale and Diagnostics section), `docs/factory/lex-nfkc-normalization/` (prerequisite) |
| Compilation lanes | `features/compilation-lanes.html` | `README.md` (Two Compilation Lanes, Compilation Pipeline sections), `docs/design/lowering-routes.md` (HIR-direct / MIR / AIR detour), `docs/design/air-dialect.md` (AIR architecture), `docs/design/semantic-ownership.md` (Faber semantic rules vs target artifact validity) |
| Latin vocabulary and structural glyphs | `features/latin-and-glyphs.html` | `README.md` (Glyphs and Words section, Why Faber, Commandments), `EBNF.md` (formal grammar), `examples/corpus/` (full keyword inventory across corpus dirs) |
| Commandments | `features/commandments.html` | `README.md` (Commandments section) |
| Canonical vs sugar surfaces | `features/canonical-vs-sugar.html` | `docs/design/numeric-type-sugar.md` (tf32, mf32, sf32, lf32), `docs/design/annotation-sugar.md` (braced records vs author shorthand), `docs/design/faber-canonical-surface.md` (author vs canonical format modes) |
| Capability calls and frames | `features/frames.html` | `docs/design/frame-stream-types.md` (sermo, scrinium, status, meus, tuus, ad), `docs/design/host-provider-gateway.md` (host routes), `examples/corpus/ad/` (sermo exempla) |
| Inline testing | `features/testing.html` | `README.md` (Exempla End-to-End Harnesses section), `examples/coreutils/packages/echo/src/main.fab` (probandum/proba/adfirma usage), `examples/corpus/proba/` and `examples/corpus/probandum/` |

---

## Section: Syntax and semantics

| Page | Path | Source documents |
|---|---|---|
| Syntax hub | `syntax/index.html` | Overview, links to sub-pages |
| Data types | `syntax/types.html` | `README.md` (Core Type Surfaces, Numeric Widths, Tensors And Sparsa, GPU Core Types sections), `docs/design/numeric-type-sugar.md`, `docs/design/tensor-intrinsics.md`, `docs/design/lista-intrinsics.md`, `docs/design/numerus-intrinsics.md`, `docs/design/fractus-intrinsics.md`, `docs/design/comparison-operators.md`, `EBNF.md`, `examples/corpus/typi/`, `examples/corpus/tensor/`, `examples/corpus/sparsa/`, `examples/corpus/lista/`, `examples/corpus/tabula/` |
| Variables and binding | `syntax/variables.html` | `README.md` (Runtime binding vs structural definition, Language Orientation sections), `examples/corpus/fixum/`, `examples/corpus/varia/`, `examples/corpus/sit/` |
| Functions | `syntax/functions.html` | `README.md` (Language Orientation — Borrowing and Mutability, How Faber Feels sections), `examples/corpus/functio/`, `examples/corpus/de/`, `examples/corpus/in/`, `examples/corpus/ex/`, `docs/design/semantic-ownership.md` |
| Control flow | `syntax/control-flow.html` | `README.md` (Control Flow Shape section), `examples/corpus/si/`, `examples/corpus/itera/`, `examples/corpus/dum/`, `examples/corpus/custodi/`, `examples/corpus/discerne/`, `examples/corpus/elige/` |
| Error handling | `syntax/errors.html` | `README.md` (Return and Error Channels section), `examples/corpus/iace/`, `examples/corpus/fac/`, `examples/corpus/cape/`, `docs/design/failable-conversio.md` |
| Generics | `syntax/generics.html` | `README.md` (Type and Size Generics section), `examples/corpus/generic/`, `examples/corpus/functio/generic-call-type-args.fab` |
| Collections | `syntax/collections.html` | `README.md` (Tensors And Sparsa section), `docs/design/lista-intrinsics.md`, `docs/design/tabula-intrinsics.md`, `docs/design/copia-intrinsics.md`, `docs/design/intervallum-intrinsics.md`, `docs/design/instans-intrinsics.md`, `examples/corpus/lista/`, `examples/corpus/tabula/`, `examples/corpus/tensor/`, `examples/corpus/sparsa/` |
| String and template literals | `syntax/strings.html` | `README.md` (String and Template Literals, String-template application, Inline JSON sections), `examples/corpus/literalia/`, `examples/corpus/scriptum/`, `docs/factory/textus-literal-family/` |
| Conversion operators | `syntax/conversion.html` | `README.md` (Conversion and Construction section), `docs/design/conversio-valor.md`, `docs/design/failable-conversio.md` |
| Glyphs and operators | `syntax/glyphs.html` | `README.md` (Glyphs and Words section), `examples/corpus/operatores/`, `examples/corpus/assignatio/`, `EBNF.md` |
| Nullability and optionality | `syntax/nullability.html` | `README.md` (Nullability and Optionality section), `examples/corpus/nihil/`, `examples/corpus/sponte/`, `examples/corpus/nonnihil/` |

---

## Section: Tooling and compiler

| Page | Path | Source documents |
|---|---|---|
| Tooling hub | `tooling/index.html` | Overview, links to sub-pages |
| Faber Build Tool | `tooling/faber-build-tool.html` | Stub exists. `README.md` (CLI Roles, Quick Start, Package Manifest sections), sibling `faber/` |
| Radix Compiler | `tooling/radix-compiler.html` | Stub exists. `README.md` (Compilation Pipeline, Compiler Performance, Codebase Index sections), sibling `radix/` |
| Cista Package Manager | `tooling/cista-package-manager.html` | Stub exists. Sibling `cista/`, `README.md` (mentions as "future distribution mechanism") |
| Codegen targets | `tooling/codegen-targets.html` | `docs/design/target-capability-matrix.md` (40 KB — primary), `README.md` (Codegen Targets and HIR/MIR Split section), `faber targets` CLI output |
| Compiler performance | `tooling/performance.html` | `README.md` (Compiler Performance section — benchmark tables) |
| In-process scripting | `tooling/scripting.html` | `docs/design/faber-scripting.md` (MIR stepper, interpreted execution) |

---

## Section: Ecosystem

| Page | Path | Source documents |
|---|---|---|
| Ecosystem hub | `ecosystem/index.html` | Overview, links to sub-pages |
| Norma standard library | `ecosystem/norma.html` | `README.md` (Standard Library section), sibling `norma/`, `norma/exempla/` |
| Triga graphics | `ecosystem/triga.html` | `README.md` (mentions triga), sibling `triga/` |
| Coreutils | `ecosystem/coreutils.html` | `examples/coreutils/` (38 packages, README.md with campaign docs), `examples/coreutils/packages/echo/src/main.fab` (representative exemplar) |
| AI Workbench | `ecosystem/ai-workbench.html` | `examples/ai-workbench/` (README.md, package, harness) |
| Reader-locale packages | `ecosystem/reader-locale-packages.html` | `examples/reader-locale/` (6 locale packages with localized Faber source) |
| Language corpus | `ecosystem/corpus.html` | `examples/corpus/` (292 .fab files, 174 registry terms, index.toml), `examples/corpus/README.md` |

---

## Section: References

| Page | Path | Source documents |
|---|---|---|
| References hub | `references/index.html` | Links to external resources |
| EBNF grammar | `references/ebnf.html` | `radix/EBNF.md` (canonical grammar) |
| Design documents | `references/design-docs.html` | `radix/docs/design/` (28 design docs), `radix/docs/design/README.md` |
| GitHub repositories | `references/repositories.html` | `github.com/faberlang` (faber, radix, faber-runtime, norma, triga, cista, examples) |

---

## Page count

**Total: ~40 pages**
- Index: 1
- Section hubs: 6
- Sub-pages: ~33

---

## Implementation order

1. **Features: Reader locale** — the headline feature with the richest source material
2. **Features: Compilation lanes** — the compiler's spine
3. **Features: Latin vocabulary and glyphs** — the three signal choices (short page)
4. **Features: Commandments** — the design laws (short page)
5. **Syntax: Functions** — practical reference, high interest
6. **Syntax: Types** — foundation for everything else
7. **Syntax: Control flow** — practical reference
8. Then remaining syntax, tooling, ecosystem, history, references

This order front-loads the most distinctive content (features) and the most practical
reference (syntax), deferring history and references to the end.
