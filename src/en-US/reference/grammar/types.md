+++
title = "Types & contracts"
section = "grammar-types"
order = 5
translate_spans = false  # rule names are the Latin identity, not a spelling
sources = [
  "faber/docs/EBNF.md",
  "faber/docs/grammar/grammar.jsonl",
  "radix/locale/en/pack.toml",
]
+++

Type syntax and the declarations built on it: interfaces, type aliases, enums, tagged unions, and relational schemas.

Return to the [grammar overview](/en-US/reference/grammar.html).

## Terms {#terms}

These are the words you write in this part of the language. Each links to its
page. The second column names the grammar rule the word belongs to.

| Term | Grammar rule |
|---|---|
| [`interface`](/en-US/corpus/interface.html) | `implendum_decl` |
| [`fn`](/en-US/corpus/fn.html) | `implendum_method_decl` |
| [`type`](/en-US/corpus/type.html) | `typus_decl` |
| [`enum`](/en-US/corpus/enum.html) | `ordo_decl` |
| [`union`](/en-US/corpus/union.html) | `discretio_decl` |
| [`schema`](/en-US/corpus/schema.html) | `schema_decl` |
| [`column`](/en-US/corpus/column.html) | `schema_column` |
| [`ref`](/en-US/corpus/ref.html), [`mut`](/en-US/corpus/mut.html) | `union_hole_type` |
| [`ref`](/en-US/corpus/ref.html), [`mut`](/en-US/corpus/mut.html) | `owned_type` |
| [`record`](/en-US/corpus/record.html) | `ratio_type` |

## Formal grammar {#formal-grammar}

The rules for this part of the language are the parser's own definition of it.
They are written for models and tools, so this page does not repeat them; the
full list is at [every production](/agents/grammar/productions.md).
