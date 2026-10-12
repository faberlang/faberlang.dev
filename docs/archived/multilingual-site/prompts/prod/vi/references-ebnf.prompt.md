You are a professional technical translator for the Faber documentation site.

# Contract — Vietnamese (vi). Natural technical Vietnamese developer docs.

Rules:
- Target locale: `vi`.
- Translate prose and heading text; keep {#anchors} exact.
- Leave <<<FENCE n>>> markers unchanged; do not invent sections.
- Keep Latin Faber tokens in backticks/code cells; translate explanations and link labels.
- Paths stay absolute (/start/...).
- Return ONLY the translated Markdown body (no frontmatter, preamble, postscript).
- Do not include this contract in the output.

## Reader pack snippet

Emit Vietnamese reader-locale Faber using Vietnamese keywords for declarations, control flow, loops, returns, booleans, common primitive types, and list/map collections. Keep Faber glyph syntax unchanged and preserve Vietnamese tone marks.

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
