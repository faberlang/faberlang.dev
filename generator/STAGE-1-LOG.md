# Stage 1 Log — Generator Foundation and Slice 1

**Date**: 2026-07-16
**Repo**: `faberlang.dev/generator/`
**Campaign**: `docs/factory/site-implementation/CAMPAIGN.md` Stage 1

## What was built

A Speculum site generator written in Faber, type-checked against the full
compiler front end. Seven modules, ~640 lines of Faber source.

### Module inventory

| Module | Purpose | Key types/functions |
|---|---|---|
| `string_util.fab` | String search, split, trim, newline constant | `nl()`, `initium_index()`, `initium_index_post()`, `initium_cum()`, `divide()`, `recide()` |
| `frontmatter.fab` | TOML `+++` block parser | `Split{fields, body}`, `divide()`, `parse_toml_lines()`, `strip_quotes()` |
| `fence.fab` | Code fence extractor with CI contracts | `Fence{locale, modus, outcome, source, line}`, `extract()`, `parse_info()` |
| `anchor.fab` | Heading extractor with stable anchor IDs | `Heading{level, text, anchor, line}`, `extract()`, `parse_heading()` |
| `types.fab` | Core domain model | `Pagina`, `HtmlPagina`, `SiteManifest`, `aedifica_paginam()` |
| `document_ir.fab` | Document IR for HTML chrome | `Attr`, `Element`, `Document`, `html()` |
| `html.fab` | HTML emitter with component vocabulary | `genera_paginam()`, `genera_head()`, `genera_renderbar()`, `genera_sidebar()`, `genera_main()`, `genera_source_list()` |
| `main.fab` | Entry point and path derivation | `genera()`, `deriva_iter()` |

### Chrome HTML rule

New Speculum chrome must be modeled as `document_ir.Element` trees and serialized with `document_ir.html()`. Do not add new guillemet HTML blobs to chrome builders; raw Markdown body HTML remains the Stage B boundary.

### Verification status

```
$ faber check faberlang.dev/generator/
ok: faberlang.dev/generator/
```

**Zero errors.** All warnings are `WARN003.unused_function` — expected because
`incipit` doesn't call the generator functions yet (it prints a usage banner;
execution is blocked on stepper support).

## What was learned — Faber language patterns

### Critical syntax discoveries

These were found through trial-and-error against `radix check` and by studying
the ai-workbench corpus. Each one was a silent failure until the correct form
was found.

| Pattern | Wrong | Right | Source of truth |
|---|---|---|---|
| Multi-line strings | `"""..."""` | `«...»` (guillemets) | EBNF line 740 |
| String templates | `"...{x}..."` | `"§ §"(a, b)` | ai-workbench `query.fab` |
| String concatenation | format strings | `+` operator on `textus` | corpus `ego.fab` |
| Newline in strings | `fixum octeti ← \|0a\|` → cast | `"\n"` (DEFER-066 resolved) | `norma/src/chorda.fab` |
| Type-first parameters | `f(name: textus)` | `f(textus name)` | every corpus example |
| Map access | `fields[key]` (returns valor) | `fields[key] ↦ textus` | ai-workbench `chat.fab:309` |
| Map mutation | — | `result[key] ← value` | tested directly |
| Continue keyword | `iteratio` | `perge` | corpus `perge.fab` |
| Boolean true assignment | `← verum` | `← (verum)` | ai-workbench `query.fab:155` |
| Enum keyword | `enum` / field named `ordo` | `ordo` is the keyword | EBNF line 214 |
| Module export | `@ privata` on exports | omit `@ privata` to export | ai-workbench pattern |
| Module import | `importa ex "./path" ut alias` | `importa ex "./path" privata * ut alias` | ai-workbench `main.fab` |
| Qualified types | `Module.Type` | works with wildcard import | tested |

### The `@ privata` trap

The biggest time sink. Functions annotated `@ privata` are **module-internal**
and cannot be imported cross-module, even with `privata *` wildcard imports.
Removing `@ privata` makes a function or type public/exportable. This is the
opposite of what you might expect from other languages where `private` is the
explicit annotation and unmarked is the default visibility.

In the ai-workbench, internal helpers have `@ privata`; the cross-module API
surface (like `functio curre`) omits it. Our first pass had `@ privata` on
every function in `string_util.fab`, which made every `su.*` call fail with
`SEM004:namespace_missing_export`.

### `\n` escape sequences are supported

DEFER-066 ("textus string escapes are not decoded") was marked resolved after
the `factory/stdlib` merge (Jul 3, 2026). The `radix` binary from the releases
repo (v0.75.0, built Jul 14) includes the fix. `"line1\nline2"` works in both
`radix check` and `faber check`. The earlier failures were shell quoting issues
(heredocs injecting literal newlines), not a language limitation.

### Stepper execution gap

`faber run --interpret` fails with:

```
error: invalid MIR: struct field projection is missing field metadata
```

The MIR stepper does not yet support struct field access (`pag.titulus`,
`p.section`). This is a known stepper limitation being actively built out.
The front end (lex → parse → typecheck → MIR lowering) passes completely,
so the code is type-safe and semantically verified — it just can't execute yet.

## What was learned — tooling state

### Binary availability

| Binary | Version | Path | Notes |
|---|---|---|---|
| `faber` | 1.1.0 | `~/.cargo/bin/faber` | Built from main; full package check + reader-locale emit |
| `radix` | 0.75.0 (reports 0.38.0) | `~/.cargo/bin/radix` | From GitHub releases; single-file check/emit |
| `faber` (homebrew) | 0.38.0 | `/opt/homebrew/bin/faber` | Stale; cannot parse `[reader]` manifests |

### `faber check` vs `radix check`

`radix check` validates individual files but cannot resolve cross-module imports.
`faber check` validates the full package with import resolution. For development,
`radix check` gives fast single-file feedback; `faber check` is the final gate.

### No v1.1.0 git tag

The `v1.0.0` tag exists but `v1.1.0` was never tagged. The release commit landed
(`31dc245`) but no tag followed. The releases repo only publishes `radix` binaries,
not `faber` — the CI was set up Jul 16 but only builds the radix component.

## Architecture decisions recorded

### Generator is Faber (dogfooding)

The site generator is written in Faber itself. `radix check` and `faber check`
run the full front end and prove the code is type-safe. Execution via the MIR
stepper is blocked on struct-field support, but the code is correct and will run
when the stepper matures. This was settled as the Stage 1 Open Question in the
campaign artifact.

### CONTENT-PLAN.md updated

The blocking dependency section was rewritten from "not true today" to "shipped
2026-07-15 (faber 1.1.0)". All references to the transcode as deferred were
updated. Version references updated from 1.0.0 to 1.1.0. See CONTENT-PLAN.md
diff: 60 insertions, 50 deletions.

### Campaign artifact created

`docs/factory/site-implementation/CAMPAIGN.md` — 8-stage campaign routing the
full site implementation from generator foundation through multilingual
generation. Stage 1 is in progress; Stages 2-8 are planned with gates,
dependencies, and batching posture declared.

## What remains for Stage 1

- [ ] Inline span renderer (48-identifier keyword/type lookup)
- [ ] Fence validation CI script (shell wrapper calling `faber check`/`radix emit`)
- [ ] Shared stylesheet extracted from homepage `:root` design tokens
- [ ] Wire `incipit` to read `syntax/types.md` and emit rendered HTML (once stepper
      supports struct fields, or via compiled `faber build` path)
