+++
title = "Programs, regions & imports"
section = "grammar-program"
order = 2
translate_spans = false  # rule names are the Latin identity, not a spelling
sources = [
  "faber/docs/EBNF.md",
  "faber/docs/grammar/grammar.jsonl",
  "radix/locale/en/pack.toml",
]
+++

The shape of a source file: optional frontmatter, the optional `module` region, the top-level statement spine, imports, and the program entry points and test suites.

Return to the [grammar overview](/en-US/reference/grammar.html).

## Terms {#terms}

These are the words you write in this part of the language. Each links to its
page. The second column names the grammar rule the word belongs to.

| Term | Grammar rule |
|---|---|
| [`import`](/en-US/corpus/import.html) | `importa_record` |
| [`from`](/en-US/corpus/from.html) | `ex_field` |
| [`as`](/en-US/corpus/as.html) | `ut_field` |
| [`all`](/en-US/corpus/all.html) | `omnia_field` |
| [`from`](/en-US/corpus/from.html), [`import`](/en-US/corpus/import.html) | `importa_sugar` |
| [`public`](/en-US/corpus/public.html) | `publica` |
| [`as`](/en-US/corpus/as.html) | `named_import` |
| [`as`](/en-US/corpus/as.html) | `wildcard_import` |
| [`const`](/en-US/corpus/const.html) | `selective_import` |
| [`as`](/en-US/corpus/as.html) | `import_value_binding` |
| [`args`](/en-US/corpus/args.html), [`exit`](/en-US/corpus/exit.html) | `entry_header` |
| [`main`](/en-US/corpus/main.html) | `incipit_stmt` |
| [`async_main`](/en-US/corpus/async_main.html) | `incipiet_stmt` |
| [`describe`](/en-US/corpus/describe.html) | `probandum_decl` |
| [`test`](/en-US/corpus/test.html) | `proba_stmt` |
| [`expect_failure`](/en-US/corpus/expect_failure.html), [`flaky`](/en-US/corpus/flaky.html), [`todo`](/en-US/corpus/todo.html), [`bench`](/en-US/corpus/bench.html), [`skip`](/en-US/corpus/skip.html), [`repeat`](/en-US/corpus/repeat.html), [`only`](/en-US/corpus/only.html), [`only_in`](/en-US/corpus/only_in.html), [`tag`](/en-US/corpus/tag.html), [`timeout`](/en-US/corpus/timeout.html) | `proba_modifier` |
| [`all`](/en-US/corpus/all.html), [`teardown`](/en-US/corpus/teardown.html), [`async_teardown`](/en-US/corpus/async_teardown.html), [`setup`](/en-US/corpus/setup.html), [`async_setup`](/en-US/corpus/async_setup.html) | `praepara_block` |

## Formal grammar {#formal-grammar}

The rules for this part of the language are the parser's own definition of it.
They are written for models and tools, so this page does not repeat them; the
full list is at [every production](/agents/grammar/productions.md).
