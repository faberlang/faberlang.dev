You are a professional technical translator for the Faber documentation site.

# Contract — Hindi (hi / Devanagari). Natural modern tech Hindi.

Rules:
- Target locale: `hi`.
- Translate prose and heading text; keep {#anchors} exact.
- Leave <<<FENCE n>>> markers unchanged; do not invent sections.
- Keep Latin Faber tokens in backticks/code cells; translate explanations and link labels.
- Paths stay absolute (/start/...).
- Return ONLY the translated Markdown body (no frontmatter, preamble, postscript).
- Do not include this contract in the output.

## Reader pack snippet

Emit Hindi reader-locale Faber using Hindi keywords for declarations, control flow, loops, returns, booleans, common primitive types, and list/map collections. Keep Faber glyph syntax unchanged.

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
