+++
title = "Lexical structure & glyphs"
section = "grammar-lexical"
order = 10
translate_spans = false  # rule names are the Latin identity, not a spelling
sources = [
  "faber/docs/EBNF.md",
  "faber/docs/grammar/grammar.jsonl",
  "radix/locale/en/pack.toml",
]
+++

The terminal tokens the lexer produces: identifiers, numbers, strings, width markers, and the frontmatter delimiter.

Return to the [grammar overview](/en-US/reference/grammar.html).

## Formal grammar {#formal-grammar}

The rules for this part of the language are the parser's own definition of it.
They are written for models and tools, so this page does not repeat them; the
full list is at [every production](/agents/grammar/productions.md).
