+++
title = "Statements & control flow"
section = "grammar-statements"
order = 6
translate_spans = false  # rule names are the Latin identity, not a spelling
sources = [
  "faber/docs/EBNF.md",
  "faber/docs/grammar/grammar.jsonl",
  "radix/locale/en/pack.toml",
]
+++

Statements and control flow: conditionals, loops, `switch` and `match`, guards, extraction, loop and function transfer, and the diagnostic statements.

Return to the [grammar overview](/en-US/reference/grammar.html).

## Terms {#terms}

These are the words you write in this part of the language. Each links to its
page. The second column names the grammar rule the word belongs to.

| Term | Grammar rule |
|---|---|
| [`if`](/en-US/corpus/if.html) | `si_stmt` |
| [`elif`](/en-US/corpus/elif.html) | `si_tail` |
| [`else`](/en-US/corpus/else.html) | `secus_clause` |
| [`while`](/en-US/corpus/while.html) | `dum_stmt` |
| [`range`](/en-US/corpus/range.html), [`ref`](/en-US/corpus/ref.html), [`from`](/en-US/corpus/from.html), [`const`](/en-US/corpus/const.html), [`for`](/en-US/corpus/for.html), [`var`](/en-US/corpus/var.html) | `itera_stmt` |
| [`at`](/en-US/corpus/at.html) | `apud_clause` |
| [`switch`](/en-US/corpus/switch.html) | `elige_stmt` |
| [`case`](/en-US/corpus/case.html) | `casu_elige_clause` |
| [`default`](/en-US/corpus/default.html) | `ceterum_clause` |
| [`match`](/en-US/corpus/match.html), [`all`](/en-US/corpus/all.html) | `discerne_stmt` |
| [`and`](/en-US/corpus/and.html) | `discriminants` |
| [`case`](/en-US/corpus/case.html) | `casu_variant_clause` |
| [`guard`](/en-US/corpus/guard.html) | `custodi_stmt` |
| [`if`](/en-US/corpus/if.html) | `si_guard_clause` |
| [`from`](/en-US/corpus/from.html), [`const`](/en-US/corpus/const.html), [`var`](/en-US/corpus/var.html) | `ex_stmt` |
| [`as`](/en-US/corpus/as.html) | `extract_field` |
| [`rest`](/en-US/corpus/rest.html) | `ceteri_field` |
| [`return`](/en-US/corpus/return.html) | `redde_stmt` |
| [`return_await`](/en-US/corpus/return_await.html) | `reddet_stmt` |
| [`await`](/en-US/corpus/await.html) | `tacebit_stmt` |
| [`yield`](/en-US/corpus/yield.html) | `cede_stmt` |
| [`break`](/en-US/corpus/break.html) | `rumpe_stmt` |
| [`continue`](/en-US/corpus/continue.html) | `perge_stmt` |
| [`pass`](/en-US/corpus/pass.html) | `tacet_stmt` |
| [`assert`](/en-US/corpus/assert.html), [`panic`](/en-US/corpus/panic.html) | `adfirma_stmt` |
| [`throw`](/en-US/corpus/throw.html), [`require`](/en-US/corpus/require.html) | `requirit_stmt` |
| [`throw`](/en-US/corpus/throw.html), [`reject`](/en-US/corpus/reject.html) | `reice_stmt` |
| [`warn`](/en-US/corpus/warn.html), [`write`](/en-US/corpus/write.html), [`debug`](/en-US/corpus/debug.html) | `nota_stmt` |
| [`while`](/en-US/corpus/while.html), [`do`](/en-US/corpus/do.html) | `fac_stmt` |

## Formal grammar {#formal-grammar}

The rules for this part of the language are the parser's own definition of it.
They are written for models and tools, so this page does not repeat them; the
full list is at [every production](/agents/grammar/productions.md).
