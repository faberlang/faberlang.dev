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

The canonical Faber grammar is defined in the Radix repository at
`radix/EBNF.md`. It is the formal authority for all language syntax.

The grammar covers:

- Lexical structure (glyphs, keywords, literals, comments)
- Declarations (functio, genus, implendum, typus, discretio, ordo)
- Statements (binding, control flow, returns, iteration)
- Expressions (calls, operators, conversions, literals)
- Annotations (@ syntax)
- CLI annotations (@ cli, @ optio, @ operandus, @ imperium)
- Type expressions (primitives, generics, sugar forms)
- Module system (importa)

<<<FENCE 0>>>
