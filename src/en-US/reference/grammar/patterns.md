+++
title = "Patterns & destructuring"
section = "grammar-patterns"
order = 8
translate_spans = false  # rule names are the Latin identity, not a spelling
sources = [
  "faber/docs/EBNF.md",
  "faber/docs/grammar/grammar.jsonl",
  "radix/locale/en/pack.toml",
]
+++

Patterns and destructuring: the atoms a match arm accepts, type and alias patterns, and the object and array destructuring forms.

Return to the [grammar overview](/en-US/reference/grammar.html).

## Terms {#terms}

These are the words you write in this part of the language. Each links to its
page. The second column names the grammar rule the word belongs to.

| Term | Grammar rule |
|---|---|
| [`and`](/en-US/corpus/and.html) | `patterns` |
| [`or`](/en-US/corpus/or.html) | `pattern` |
| [`const`](/en-US/corpus/const.html), [`as`](/en-US/corpus/as.html), [`var`](/en-US/corpus/var.html) | `ut_pattern` |
| [`as`](/en-US/corpus/as.html) | `pattern_binding` |
| [`rest`](/en-US/corpus/rest.html), [`as`](/en-US/corpus/as.html) | `pattern_property` |
| [`rest`](/en-US/corpus/rest.html) | `array_pattern_element` |

## Formal grammar {#formal-grammar}

The rules for this part of the language are the parser's own definition of it.
They are written for models and tools, so this page does not repeat them; the
full list is at [every production](/agents/grammar/productions.md).
