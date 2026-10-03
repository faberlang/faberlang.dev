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

The lexer turns a file into tokens before the parser builds a tree. This
page is those tokens: identifiers, numbers, strings, the width markers
(`i32`, `f32`, …), and the frontmatter delimiter.

Identifiers are the names you write — `score`, `divide`, `Span`. Numbers
are the integer and floating literals. A `"…"` string is Unicode text.
Width markers are the bare type tokens for sized numerics. None of these
are keywords. The reserved words on the other family pages are already
known to the parser; everything else that looks like a name is an
identifier.

There is no keyword table here: these productions are the terminal
shapes, not the vocabulary of the language. A short program that is
mostly those tokens:

```faber locale=en
main {
    const i32 narrow ← 7 ∷ i32
    const f32 single ← 1.5 ∷ f32
    const string name ← "Marcus"
    print name
    print narrow
    print single
}
```

Return to the [grammar overview](/en-US/reference/grammar.html).

## Formal grammar {#formal-grammar}

The rules for this part of the language are the parser's own definition of it.
They are written for models and tools, so this page does not repeat them; the
full list is at [every production](/agents/grammar/productions.md).
