+++
title = "Error channel"
section = "grammar-errors"
order = 9
translate_spans = false  # rule names are the Latin identity, not a spelling
sources = [
  "faber/docs/EBNF.md",
  "faber/docs/grammar/grammar.jsonl",
  "radix/locale/en/pack.toml",
]
+++

The error channel: throwing, guarded throws, and the local `catch` handler that recovers an error into a value.

Return to the [grammar overview](/en-US/reference/grammar.html).

## Terms {#terms}

These are the words you write in this part of the language. Each links to its
page. The second column names the grammar rule the word belongs to.

| Term | Grammar rule |
|---|---|
| [`throw`](/en-US/corpus/throw.html), [`panic`](/en-US/corpus/panic.html) | `iace_expr` |
| [`throw`](/en-US/corpus/throw.html), [`panic`](/en-US/corpus/panic.html), [`if`](/en-US/corpus/if.html) | `iace_guarded_expr` |
| [`catch`](/en-US/corpus/catch.html) | `cape_clause` |

## Formal grammar {#formal-grammar}

The rules for this part of the language are the parser's own definition of it.
They are written for models and tools, so this page does not repeat them; the
full list is at [every production](/agents/grammar/productions.md).
