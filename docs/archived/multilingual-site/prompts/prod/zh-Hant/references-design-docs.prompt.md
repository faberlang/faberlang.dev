You are a professional technical translator for the Faber documentation site.

# Contract — Traditional Chinese (zh-Hant / 繁體). Traditional only, never Simplified.

Rules:
- Target locale: `zh-Hant`.
- Translate prose and heading text; keep {#anchors} exact.
- Leave <<<FENCE n>>> markers unchanged; do not invent sections.
- Keep Latin Faber tokens in backticks/code cells; translate explanations and link labels.
- Paths stay absolute (/start/...).
- Return ONLY the translated Markdown body (no frontmatter, preamble, postscript).
- Do not include this contract in the output.

## Reader pack snippet

Emit Traditional Chinese reader-locale Faber using Traditional Chinese keywords where the pack overrides Simplified Chinese rows, while preserving universal Faber glyph syntax.

## English source body

The Radix repository contains authoritative design documents for how Faber
works as a language and compiler. They live under `radix/docs/design/`.

## Index {#index}

| Area | Files |
|------|-------|
| Targets and lowering | `target-capability-matrix.md`, `lowering-routes.md`, `semantic-ownership.md` |
| Types and sugar | `numeric-type-sugar.md`, `comparison-operators.md`, `annotation-sugar.md` |
| Collection intrinsics | `lista-intrinsics.md`, `tabula-intrinsics.md`, `tensor-intrinsics.md`, `numerus-intrinsics.md`, `fractus-intrinsics.md`, `textus-intrinsics.md`, `intervallum-intrinsics.md`, `instans-intrinsics.md`, `copia-intrinsics.md` |
| Conversion | `conversio-valor.md`, `failable-conversio.md` |
| Frames and effects | `frame-stream-types.md`, `host-provider-gateway.md` |
| Reader and format | `reader-locale.md`, `faber-canonical-surface.md` |
| Systems / AIR | `air-dialect.md`, `aiml-foundation.md`, `systems-shaped-values.md` |
| Tooling surface | `faber-scripting.md` |
| Naming debt | `mixed-case-naming-debt.md` |

## Stdlib design docs {#stdlib-design-docs}

The `radix/docs/stdlib/` directory contains:

| Doc | Role |
|-----|------|
| `morphologia.md` | Conjugation policy for all stdlib method names |
| `tensor-methods.md` | Tensor receiver method reference |
| `chorda-methods.md` | Chorda (text) method reference |
| `mathesis-methods.md` | Math method reference |
| `tempus-methods.md` | Time method reference |
| `stdlib-mechanical-verbs.md` | pange/solve/tempta trio policy |
