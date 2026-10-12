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
