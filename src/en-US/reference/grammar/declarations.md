+++
title = "Declarations & bindings"
section = "grammar-declarations"
order = 3
translate_spans = false  # rule names are the Latin identity, not a spelling
sources = [
  "faber/docs/EBNF.md",
  "faber/docs/grammar/grammar.jsonl",
  "radix/locale/en/pack.toml",
]
+++

Bindings, functions, generic parameters, closures, classes, and the fields and methods a class holds.

Return to the [grammar overview](/en-US/reference/grammar.html).

## Terms {#terms}

These are the words you write in this part of the language. Each links to its
page. The second column names the grammar rule the word belongs to.

| Term | Grammar rule |
|---|---|
| [`embed`](/en-US/corpus/embed.html) | `insere_expr` |
| [`const`](/en-US/corpus/const.html), [`var`](/en-US/corpus/var.html) | `fixum_decl` |
| [`await_const`](/en-US/corpus/await_const.html), [`await_var`](/en-US/corpus/await_var.html) | `figendum_decl` |
| [`let`](/en-US/corpus/let.html) | `sit_decl` |
| [`const`](/en-US/corpus/const.html), [`var`](/en-US/corpus/var.html) | `array_destruct` |
| [`const`](/en-US/corpus/const.html), [`var`](/en-US/corpus/var.html) | `object_destruct` |
| [`fn`](/en-US/corpus/fn.html) | `functio_decl` |
| [`implements`](/en-US/corpus/implements.html) | `generic_bound` |
| [`rest`](/en-US/corpus/rest.html), [`optional`](/en-US/corpus/optional.html), [`as`](/en-US/corpus/as.html), [`coalesce`](/en-US/corpus/coalesce.html) | `parameter` |
| [`args`](/en-US/corpus/args.html), [`errors`](/en-US/corpus/errors.html), [`exit`](/en-US/corpus/exit.html), [`throws`](/en-US/corpus/throws.html), [`readonly`](/en-US/corpus/readonly.html), [`options`](/en-US/corpus/options.html) | `func_modifier` |
| [`async_generator`](/en-US/corpus/async_generator.html), [`async`](/en-US/corpus/async.html), [`generator`](/en-US/corpus/generator.html) | `callable_posture` |
| [`then`](/en-US/corpus/then.html) | `ergo_joint` |
| [`free`](/en-US/corpus/free.html), [`kernel`](/en-US/corpus/kernel.html) | `closure_modifier` |
| [`do`](/en-US/corpus/do.html) | `fac_block` |
| [`lambda`](/en-US/corpus/lambda.html) | `clausura_legacy_expr` |
| [`class`](/en-US/corpus/class.html), [`implements`](/en-US/corpus/implements.html) | `genus_decl` |
| [`const`](/en-US/corpus/const.html), [`static`](/en-US/corpus/static.html), [`optional`](/en-US/corpus/optional.html), [`var`](/en-US/corpus/var.html) | `genus_field_decl` |
| [`const`](/en-US/corpus/const.html), [`static`](/en-US/corpus/static.html), [`optional`](/en-US/corpus/optional.html), [`var`](/en-US/corpus/var.html) | `field_decl` |
| [`fn`](/en-US/corpus/fn.html) | `functio_method_decl` |

## Formal grammar {#formal-grammar}

The rules for this part of the language are the parser's own definition of it.
They are written for models and tools, so this page does not repeat them; the
full list is at [every production](/agents/grammar/productions.md).
