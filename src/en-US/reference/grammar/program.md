+++
title = "Programs, regions & imports"
section = "reference"
order = 2
translate_spans = false  # rule names are the Latin identity, not a spelling
sources = [
  "faber/docs/EBNF.md",
  "faber/docs/grammar/grammar.jsonl",
  "radix/locale/en/pack.toml",
]
+++

The shape of a source file: optional frontmatter, the optional `module` region, the top-level statement spine, imports, and the program entry points and test suites.

Rule names (`fab_file`, `itera_stmt`) are the stable Latin grammar identifiers;
the quoted words are the English reader spellings. Return to the
[grammar index](/en-US/reference/grammar.html).

## Productions {#productions}

```ebnf
# [001] fab_file
fab_file ::= frontmatter? program
# [002] frontmatter
frontmatter ::= FRONTMATTER_DELIMITER NEWLINE TOML_LINES FRONTMATTER_DELIMITER NEWLINE?
# [003] program
program ::= regio_decl? statement*
# [004] regio_decl
regio_decl ::= 'module' IDENTIFIER
# [005] statement
statement ::= annotation* statement_core | ad_handler_decl
# [006] ad_handler_decl
ad_handler_decl ::= annotation* ad_annotation annotation* functio_decl
# [007] statement_core
statement_core ::= importa_decl | binding_decl | functio_decl | genus_decl | implendum_decl | typus_decl | ordo_decl | discretio_decl | schema_decl | si_stmt | dum_stmt | itera_stmt | elige_stmt | discerne_stmt | custodi_stmt | fac_stmt | redde_stmt | reddet_stmt | tacebit_stmt | cede_stmt | rumpe_stmt | perge_stmt | tacet_stmt | iace_stmt | adfirma_stmt | requirit_stmt | reice_stmt | nota_stmt | incipit_stmt | incipiet_stmt | ex_stmt | probandum_decl | proba_stmt | block_stmt | inc_dec_stmt | expr_stmt
# [077] importa_decl
importa_decl ::= importa_record | importa_sugar
# [078] importa_record
importa_record ::= 'import' '{' import_field_list '}'
# [079] import_field_list
import_field_list ::= import_field (',' import_field)*
# [080] import_field
import_field ::= ex_field | visibilitas_field | nomen_field | ut_field | omnia_field
# [081] ex_field
ex_field ::= 'from' '=' STRING
# [082] visibilitas_field
visibilitas_field ::= 'visibilitas' '=' publica
# [083] nomen_field
nomen_field ::= 'name' '=' IDENTIFIER
# [084] ut_field
ut_field ::= 'as' '=' IDENTIFIER
# [085] omnia_field
omnia_field ::= 'all' '=' IDENTIFIER
# [086] importa_sugar
importa_sugar ::= 'import' 'from' STRING publica? (named_import | wildcard_import | selective_import)?
# [087] publica
publica ::= 'public'
# [088] named_import
named_import ::= IDENTIFIER ('as' IDENTIFIER)?
# [089] wildcard_import
wildcard_import ::= '*' 'as' IDENTIFIER
# [090] selective_import
selective_import ::= 'const' import_value_binding (',' import_value_binding)*
# [091] import_value_binding
import_value_binding ::= IDENTIFIER ('as' IDENTIFIER)?
# [230] entry_header
entry_header ::= ('args' IDENTIFIER)? ('exit' expression)?
# [231] incipit_stmt
incipit_stmt ::= 'main' entry_header block_stmt
# [232] incipiet_stmt
incipiet_stmt ::= 'async_main' entry_header block_stmt
# [233] probandum_decl
probandum_decl ::= 'describe' STRING proba_modifier* '{' probandum_body '}'
# [234] probandum_body
probandum_body ::= (praepara_block | probandum_decl | proba_stmt)*
# [235] proba_stmt
proba_stmt ::= 'test' STRING proba_modifier* block_stmt
# [236] proba_modifier
proba_modifier ::= 'expect_failure' | 'skip' STRING | 'todo' STRING | 'only' | 'tag' STRING | 'timeout' NATURAL | 'bench' | 'repeat' NATURAL | 'flaky' NATURAL | 'only_in' STRING
# [237] praepara_block
praepara_block ::= ('setup' | 'async_setup' | 'teardown' | 'async_teardown') 'all'? block_stmt
```

## Terms {#terms}

Keywords in these productions that have a corpus term page. The production id
on the left is the Latin spine name; the links are the English reader spellings
you write.

| Production | Terms |
|---|---|
| `importa_record` | [`import`](/en-US/corpus/import.html) |
| `ex_field` | [`from`](/en-US/corpus/from.html) |
| `ut_field` | [`as`](/en-US/corpus/as.html) |
| `omnia_field` | [`all`](/en-US/corpus/all.html) |
| `importa_sugar` | [`from`](/en-US/corpus/from.html), [`import`](/en-US/corpus/import.html) |
| `publica` | [`public`](/en-US/corpus/public.html) |
| `named_import` | [`as`](/en-US/corpus/as.html) |
| `wildcard_import` | [`as`](/en-US/corpus/as.html) |
| `selective_import` | [`const`](/en-US/corpus/const.html) |
| `import_value_binding` | [`as`](/en-US/corpus/as.html) |
| `entry_header` | [`args`](/en-US/corpus/args.html), [`exit`](/en-US/corpus/exit.html) |
| `incipit_stmt` | [`main`](/en-US/corpus/main.html) |
| `incipiet_stmt` | [`async_main`](/en-US/corpus/async_main.html) |
| `probandum_decl` | [`describe`](/en-US/corpus/describe.html) |
| `proba_stmt` | [`test`](/en-US/corpus/test.html) |
| `proba_modifier` | [`flaky`](/en-US/corpus/flaky.html), [`todo`](/en-US/corpus/todo.html), [`bench`](/en-US/corpus/bench.html), [`skip`](/en-US/corpus/skip.html), [`repeat`](/en-US/corpus/repeat.html), [`only`](/en-US/corpus/only.html), [`only_in`](/en-US/corpus/only_in.html), [`tag`](/en-US/corpus/tag.html), [`timeout`](/en-US/corpus/timeout.html) |
| `praepara_block` | [`all`](/en-US/corpus/all.html), [`teardown`](/en-US/corpus/teardown.html), [`async_teardown`](/en-US/corpus/async_teardown.html), [`setup`](/en-US/corpus/setup.html), [`async_setup`](/en-US/corpus/async_setup.html) |
