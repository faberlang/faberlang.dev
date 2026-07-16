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

| Page | Path | Source documents | Status |
|------|------|-----------------|--------|
| History hub | `history/index.html` | TBD — no single history doc exists yet | ✅ HTML (origins note) |
| Influences | `history/influences.html` | `README.md` (contrasts with AppleScript, COBOL, Rust, Go, TS, JAX), `docs/design/reader-locale.md` | ⬜ md |
| Release history | `history/releases.html` | `radix/docs/release/` | ⬜ md |

**Known gaps:** No coherent history document exists. Creator attribution, timeline, and
release history need to be compiled from release notes and git history.

---

## Section: Features

| Page | Path | Source documents | Status |
|------|------|-----------------|--------|
| Features hub | `features/index.html` | Overview, links to sub-pages | ✅ HTML |
| Reader locale | `features/reader-locale.html` | `docs/design/reader-locale.md` (69 KB), `examples/reader-locale/`, `stdlib/reader/*/pack.toml` | ✅ HTML |
| Compilation lanes | `features/compilation-lanes.html` | `README.md`, `docs/design/lowering-routes.md`, `docs/design/air-dialect.md`, `docs/design/semantic-ownership.md` | ✅ HTML |
| Latin vocabulary and glyphs | `features/latin-and-glyphs.html` | `README.md` (Glyphs and Words, Why Faber, Commandments), `EBNF.md`, `examples/corpus/` | ✅ HTML |
| Commandments | `features/commandments.html` | `README.md` (Commandments section) | ✅ HTML |
| Canonical vs sugar surfaces | `features/canonical-vs-sugar.html` | `docs/design/numeric-type-sugar.md`, `docs/design/annotation-sugar.md`, `docs/design/faber-canonical-surface.md` | ✅ HTML |
| Capability calls and frames | `features/frames.html` | `docs/design/frame-stream-types.md`, `docs/design/host-provider-gateway.md`, `examples/corpus/ad/` | ✅ HTML |
| Inline testing | `features/testing.html` | `README.md` (Exempla End-to-End Harnesses), `examples/coreutils/packages/echo/` | ✅ HTML |

---

## Section: Syntax and semantics

| Page | Path | Source documents | Status |
|------|------|-----------------|--------|
| Syntax hub | `syntax/index.html` | Overview, links to sub-pages | ⬜ HTML |
| Data types | `syntax/types.md` | `README.md`, `docs/design/numeric-type-sugar.md`, `docs/design/tensor-intrinsics.md`, `docs/design/lista-intrinsics.md`, `EBNF.md`, `examples/corpus/` | ✅ md |
| Variables and binding | `syntax/variables.md` | `README.md`, `examples/corpus/fixum/`, `examples/corpus/sit/` | ✅ md |
| Functions | `syntax/functions.md` | `README.md`, `examples/corpus/functio/`, `examples/corpus/de/`, `examples/corpus/in/`, `examples/corpus/ex/` | ✅ md |
| Control flow | `syntax/control-flow.md` | `README.md`, `examples/corpus/si/`, `examples/corpus/itera/`, `examples/corpus/dum/`, `examples/corpus/custodi/` | ✅ md |
| Error handling | `syntax/errors.md` | `README.md`, `examples/corpus/iace/`, `examples/corpus/fac/`, `examples/corpus/cape/` | ✅ md |
| Generics | `syntax/generics.md` | `README.md`, `examples/corpus/generic/` | ✅ md |
| Collections | `syntax/collections.md` | `README.md`, `docs/design/lista-intrinsics.md`, `docs/design/tabula-intrinsics.md`, `docs/design/tensor-intrinsics.md`, `examples/corpus/` | ✅ md |
| String and template literals | `syntax/strings.md` | `README.md`, `examples/corpus/literalia/`, `examples/corpus/scriptum/` | ✅ md |
| Conversion operators | `syntax/conversion.md` | `README.md`, `docs/design/conversio-valor.md`, `docs/design/failable-conversio.md` | ✅ md |
| Glyphs and operators | `syntax/glyphs.md` | `README.md`, `examples/corpus/operatores/`, `EBNF.md` | ✅ md |
| Nullability and optionality | `syntax/nullability.md` | `README.md`, `examples/corpus/nihil/`, `examples/corpus/sponte/` | ✅ md |

---

## Section: Tooling and compiler

| Page | Path | Source documents | Status |
|------|------|-----------------|--------|
| Tooling hub | `tooling/index.html` | Overview, links to sub-pages | ⬜ HTML |
| Faber Build Tool | `tooling/faber-build-tool.html` | `README.md` (CLI Roles, Quick Start, Package Manifest), sibling `faber/` | ⬜ HTML stub |
| Radix Compiler | `tooling/radix-compiler.html` | `README.md` (Compilation Pipeline, Compiler Performance, Codebase Index), sibling `radix/` | ⬜ HTML stub |
| Cista Package Manager | `tooling/cista-package-manager.html` | Sibling `cista/`, `README.md` | ⬜ HTML stub |
| Codegen targets | `tooling/codegen-targets.md` | `docs/design/target-capability-matrix.md`, `README.md`, `faber targets` | ✅ md |
| Compiler performance | `tooling/performance.md` | `README.md` (Compiler Performance section) | ✅ md |
| In-process scripting | `tooling/scripting.md` | `docs/design/faber-scripting.md` | ✅ md |

---

## Section: Ecosystem

| Page | Path | Source documents | Status |
|------|------|-----------------|--------|
| Ecosystem hub | `ecosystem/index.html` | Overview, links to sub-pages | ⬜ HTML |
| Norma standard library | `ecosystem/norma.md` | `README.md`, sibling `norma/`, `radix/docs/stdlib/morphologia.md` | ✅ md |
| Triga graphics | `ecosystem/triga.md` | Sibling `triga/` | ✅ md |
| Coreutils | `ecosystem/coreutils.md` | `examples/coreutils/` (38 packages), `examples/coreutils/packages/echo/` | ✅ md |
| AI Workbench | `ecosystem/ai-workbench.md` | `examples/ai-workbench/` | ✅ md |
| Reader-locale packages | `ecosystem/reader-locale-packages.md` | `examples/reader-locale/` (6 locale packages) | ✅ md |
| Language corpus | `ecosystem/corpus.md` | `examples/corpus/` (292 .fab files, 174 terms) | ✅ md |

---

## Section: References

| Page | Path | Source documents | Status |
|------|------|-----------------|--------|
| References hub | `references/index.html` | Links to external resources | ⬜ HTML |
| EBNF grammar | `references/ebnf.md` | `radix/EBNF.md` | ✅ md |
| Design documents | `references/design-docs.md` | `radix/docs/design/` (28 design docs) | ✅ md |
| GitHub repositories | `references/repositories.md` | `github.com/faberlang` | ✅ md |

---

## Page count

**Total: ~40 pages**

**Completed: 32 pages**
- Index: 1 ✅
- Section hubs: 6 ⬜ (HTML stubs exist, need content)
- Feature pages: 7 ✅
- Syntax pages: 11 ✅
- Tooling pages: 3 ✅ (+ 3 HTML stubs)
- Ecosystem pages: 6 ✅
- History: 1 ✅ (origins note, needs more)
- References: 3 ✅

**Remaining:**
- Section hub HTML pages (6): features hub ✅, rest need content
- History sub-pages (2): influences, releases
- Tooling HTML content (3): faber-build-tool, radix-compiler, cista-package-manager
---

## Implementation order (completed)

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
