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

Reference material for the Faber language: formal grammar, design
documents, and repository index.

## EBNF grammar {#ebnf}

The formal grammar for Faber syntax. Every production rule with
annotations. [Read more →](/references/ebnf.html)

## Design documents {#design-docs}

Architecture decisions, deferred feature tracking, and design rationale.
[Read more →](/references/design-docs.html)

## Repositories {#repositories}

The faberlang organization: compiler (`radix`), CLI (`faber`), runtime
(`faber-runtime`), package manager (`cista`), stdlib (`norma`), and
graphics (`triga`). [Read more →](/references/repositories.html)
