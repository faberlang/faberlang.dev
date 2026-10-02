+++
title = "Annotations & directives"
section = "grammar-annotations"
order = 4
translate_spans = false  # rule names are the Latin identity, not a spelling
sources = [
  "faber/docs/EBNF.md",
  "faber/docs/grammar/grammar.jsonl",
  "radix/locale/en/pack.toml",
]
+++

The `@` annotation family: the generic shape, the kernel (`@ kernel`), compiler-lane (`@ radix`), and capability (`@ call`) directives.

Return to the [grammar overview](/en-US/reference/grammar.html).

## Terms {#terms}

These are the words you write in this part of the language. Each links to its
page. The second column names the grammar rule the word belongs to.

| Term | Grammar rule |
|---|---|
| [`kernel`](/en-US/corpus/kernel.html) | `nucleum_sugar` |
| [`kernel`](/en-US/corpus/kernel.html) | `nucleum_braced` |
| [`false`](/en-US/corpus/false.html), [`true`](/en-US/corpus/true.html) | `nucleum_field` |
| [`mut`](/en-US/corpus/mut.html), [`type`](/en-US/corpus/type.html) | `radix_directive` |
| [`call`](/en-US/corpus/call.html) | `ad_annotation` |

## Formal grammar {#formal-grammar}

The rules for this part of the language are the parser's own definition of it.
They are written for models and tools, so this page does not repeat them; the
full list is at [every production](/agents/grammar/productions.md).
