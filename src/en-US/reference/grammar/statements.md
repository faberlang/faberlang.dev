+++
title = "Statements & control flow"
section = "reference"
order = 6
translate_spans = false  # rule names are the Latin identity, not a spelling
sources = [
  "faber/docs/EBNF.md",
  "faber/docs/grammar/grammar.jsonl",
  "radix/locale/en/pack.toml",
]
+++

Statements and control flow: conditionals, loops, `switch` and `match`, guards, extraction, loop and function transfer, and the diagnostic statements.

Rule names (`fab_file`, `itera_stmt`) are the stable Latin grammar identifiers;
the quoted words are the English reader spellings. Return to the
[grammar index](/en-US/reference/grammar.html).

## Productions {#productions}

```ebnf
# [112] si_stmt
si_stmt ::= 'if' si_tail
# [113] si_tail
si_tail ::= expression arm ('elif' si_tail | secus_clause)?
# [114] secus_clause
secus_clause ::= 'else' else_arm
# [115] arm
arm ::= (block_stmt | ergo_joint statement) cape_clause?
# [116] else_arm
else_arm ::= (block_stmt | ergo_joint statement) cape_clause?
# [117] dum_stmt
dum_stmt ::= 'while' expression (block_stmt | ergo_joint statement) cape_clause?
# [118] itera_stmt
itera_stmt ::= 'for' ('from' expression (',' expression)* | 'ref' expression | 'range' expression (',' expression)*) apud_clause? ('const' | 'var') itera_binding (block_stmt | ergo_joint statement) cape_clause?
# [119] itera_binding
itera_binding ::= array_pattern | object_pattern | IDENTIFIER (',' IDENTIFIER)*
# [120] apud_clause
apud_clause ::= 'at' '[' IDENTIFIER (',' IDENTIFIER)* ']'
# [121] elige_stmt
elige_stmt ::= 'switch' expression '{' casu_elige_clause* ceterum_clause? '}' cape_clause?
# [122] casu_elige_clause
casu_elige_clause ::= 'case' expression (block_stmt | ergo_joint statement)
# [123] ceterum_clause
ceterum_clause ::= 'default' (block_stmt | ergo_joint statement)
# [124] discerne_stmt
discerne_stmt ::= 'match' 'all'? discriminants '{' casu_variant_clause* ceterum_clause? '}'
# [125] discriminants
discriminants ::= subject_path ('and' subject_path)*
# [126] subject_path
subject_path ::= IDENTIFIER ('.' IDENTIFIER)*
# [127] casu_variant_clause
casu_variant_clause ::= 'case' patterns (block_stmt | ergo_joint statement)
# [135] custodi_stmt
custodi_stmt ::= 'guard' '{' si_guard_clause+ '}'
# [136] si_guard_clause
si_guard_clause ::= 'if' expression (block_stmt | ergo_joint statement)
# [137] ex_stmt
ex_stmt ::= 'from' expression ('const' | 'var') extract_fields
# [138] extract_fields
extract_fields ::= extract_field (',' extract_field)* (',' ceteri_field)? | ceteri_field
# [139] extract_field
extract_field ::= IDENTIFIER ('as' IDENTIFIER)?
# [140] ceteri_field
ceteri_field ::= 'rest' IDENTIFIER
# [141] redde_stmt
redde_stmt ::= 'return' expression?
# [142] reddet_stmt
reddet_stmt ::= 'return_await' expression
# [143] tacebit_stmt
tacebit_stmt ::= 'await' expression
# [144] cede_stmt
cede_stmt ::= 'yield' expression
# [145] rumpe_stmt
rumpe_stmt ::= 'break'
# [146] perge_stmt
perge_stmt ::= 'continue'
# [147] tacet_stmt
tacet_stmt ::= 'pass'
# [152] adfirma_stmt
adfirma_stmt ::= 'assert' expression ('panic' expression)?
# [153] requirit_stmt
requirit_stmt ::= 'require' expression 'throw' expression
# [154] reice_stmt
reice_stmt ::= 'reject' expression 'throw' expression
# [158] inc_dec_stmt
inc_dec_stmt ::= place ('↑' | '↓')
# [229] nota_stmt
nota_stmt ::= ('print' | 'debug' | 'warn' | 'write') expression (',' expression)*
# [238] fac_stmt
fac_stmt ::= 'do' block_stmt cape_clause? ('while' expression)?
```

## Terms {#terms}

Keywords in these productions that have a corpus term page. The production id
on the left is the Latin spine name; the links are the English reader spellings
you write.

| Production | Terms |
|---|---|
| `si_stmt` | [`if`](/en-US/corpus/if.html) |
| `si_tail` | [`elif`](/en-US/corpus/elif.html) |
| `secus_clause` | [`else`](/en-US/corpus/else.html) |
| `dum_stmt` | [`while`](/en-US/corpus/while.html) |
| `itera_stmt` | [`range`](/en-US/corpus/range.html), [`ref`](/en-US/corpus/ref.html), [`from`](/en-US/corpus/from.html), [`const`](/en-US/corpus/const.html), [`for`](/en-US/corpus/for.html), [`var`](/en-US/corpus/var.html) |
| `apud_clause` | [`at`](/en-US/corpus/at.html) |
| `elige_stmt` | [`switch`](/en-US/corpus/switch.html) |
| `casu_elige_clause` | [`case`](/en-US/corpus/case.html) |
| `ceterum_clause` | [`default`](/en-US/corpus/default.html) |
| `discerne_stmt` | [`match`](/en-US/corpus/match.html), [`all`](/en-US/corpus/all.html) |
| `discriminants` | [`and`](/en-US/corpus/and.html) |
| `casu_variant_clause` | [`case`](/en-US/corpus/case.html) |
| `custodi_stmt` | [`guard`](/en-US/corpus/guard.html) |
| `si_guard_clause` | [`if`](/en-US/corpus/if.html) |
| `ex_stmt` | [`from`](/en-US/corpus/from.html), [`const`](/en-US/corpus/const.html), [`var`](/en-US/corpus/var.html) |
| `extract_field` | [`as`](/en-US/corpus/as.html) |
| `ceteri_field` | [`rest`](/en-US/corpus/rest.html) |
| `redde_stmt` | [`return`](/en-US/corpus/return.html) |
| `reddet_stmt` | [`return_await`](/en-US/corpus/return_await.html) |
| `tacebit_stmt` | [`await`](/en-US/corpus/await.html) |
| `cede_stmt` | [`yield`](/en-US/corpus/yield.html) |
| `rumpe_stmt` | [`break`](/en-US/corpus/break.html) |
| `perge_stmt` | [`continue`](/en-US/corpus/continue.html) |
| `tacet_stmt` | [`pass`](/en-US/corpus/pass.html) |
| `adfirma_stmt` | [`assert`](/en-US/corpus/assert.html), [`panic`](/en-US/corpus/panic.html) |
| `requirit_stmt` | [`throw`](/en-US/corpus/throw.html), [`require`](/en-US/corpus/require.html) |
| `reice_stmt` | [`throw`](/en-US/corpus/throw.html), [`reject`](/en-US/corpus/reject.html) |
| `nota_stmt` | [`warn`](/en-US/corpus/warn.html), [`write`](/en-US/corpus/write.html), [`debug`](/en-US/corpus/debug.html) |
| `fac_stmt` | [`while`](/en-US/corpus/while.html), [`do`](/en-US/corpus/do.html) |
