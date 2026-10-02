+++
title = "Expressions & operators"
section = "grammar-expressions"
order = 7
translate_spans = false  # rule names are the Latin identity, not a spelling
sources = [
  "faber/docs/EBNF.md",
  "faber/docs/grammar/grammar.jsonl",
  "radix/locale/en/pack.toml",
]
+++

Expressions and the operator stack, from the assignment root down through the precedence ladder to calls, literals, and the collection and JSON forms.

Return to the [grammar overview](/en-US/reference/grammar.html).

## Terms {#terms}

These are the words you write in this part of the language. Each links to its
page. The second column names the grammar rule the word belongs to.

| Term | Grammar rule |
|---|---|
| [`or`](/en-US/corpus/or.html) | `aut_expr` |
| [`and`](/en-US/corpus/and.html) | `et_expr` |
| [`is`](/en-US/corpus/is.html), [`is`](/en-US/corpus/is.html), [`not`](/en-US/corpus/not.html) | `equality_tail` |
| [`before`](/en-US/corpus/before.html), [`step`](/en-US/corpus/step.html), [`until`](/en-US/corpus/until.html) | `range_tail` |
| [`coalesce`](/en-US/corpus/coalesce.html) | `vel_expr` |
| [`before`](/en-US/corpus/before.html), [`step`](/en-US/corpus/step.html), [`until`](/en-US/corpus/until.html) | `vel_range_tail` |
| [`not`](/en-US/corpus/not.html) | `unary_expr` |
| [`spread`](/en-US/corpus/spread.html) | `argument` |
| [`spread`](/en-US/corpus/spread.html) | `template_argument` |
| [`false`](/en-US/corpus/false.html), [`null`](/en-US/corpus/null.html), [`true`](/en-US/corpus/true.html) | `literal` |
| [`self`](/en-US/corpus/self.html) | `primary` |
| [`call`](/en-US/corpus/call.html) | `ad_expr` |
| [`tuple`](/en-US/corpus/tuple.html) | `iuncta_expr` |
| [`from`](/en-US/corpus/from.html) | `construction_source` |
| [`variant`](/en-US/corpus/variant.html) | `finge_expr` |
| [`comptime`](/en-US/corpus/comptime.html) | `praefixum_expr` |
| [`format`](/en-US/corpus/format.html) | `scriptum_expr` |
| [`read`](/en-US/corpus/read.html), [`line`](/en-US/corpus/line.html) | `lege_expr` |
| [`primus_quem`](/en-US/corpus/primus_quem.html) | `first_match_expr` |
| [`from`](/en-US/corpus/from.html), [`const`](/en-US/corpus/const.html), [`sum`](/en-US/corpus/sum.html), [`var`](/en-US/corpus/var.html) | `summa_expr` |
| [`from`](/en-US/corpus/from.html) | `extrema_expr` |
| [`coalesce`](/en-US/corpus/coalesce.html) | `extrema_identity` |

## Formal grammar {#formal-grammar}

The rules for this part of the language are the parser's own definition of it.
They are written for models and tools, so this page does not repeat them; the
full list is at [every production](/agents/grammar/productions.md).
