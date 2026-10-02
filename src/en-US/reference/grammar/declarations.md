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

Rule names (`fab_file`, `itera_stmt`) are the stable Latin grammar identifiers;
the quoted words are the English reader spellings. Return to the
[grammar index](/en-US/reference/grammar.html).

## Productions {#productions}

```ebnf
# [008] binding_decl
binding_decl ::= fixum_decl | sit_decl | array_destruct | object_destruct | figendum_decl
# [009] expr_stmt
expr_stmt ::= expression
# [010] block_stmt
block_stmt ::= '{' statement* '}'
# [011] const_init
const_init ::= insere_expr | expression
# [012] insere_expr
insere_expr ::= 'embed' STRING
# [013] fixum_decl
fixum_decl ::= ('const' | 'var') type_annotation IDENTIFIER (('←' expression) | ('=' const_init) | ('↤' assignment inline_default?) | ('↢' expression))?
# [014] figendum_decl
figendum_decl ::= ('await_const' | 'await_var') type_annotation IDENTIFIER '←' expression
# [015] sit_decl
sit_decl ::= 'let' IDENTIFIER (('←' | '↢') expression)?
# [016] array_destruct
array_destruct ::= ('const' | 'var') array_pattern '←' expression
# [017] object_destruct
object_destruct ::= ('const' | 'var') object_pattern '←' expression
# [018] functio_decl
functio_decl ::= 'fn' IDENTIFIER generic_params? '(' param_list ')' func_modifier* callable_posture? return_clause? alternate_exit_clause? block_stmt
# [019] param_list
param_list ::= (parameter (',' parameter)*)?
# [020] generic_params
generic_params ::= '<' (type_param_list (',' size_param_list)? | size_param_list) '>'
# [021] type_param_list
type_param_list ::= generic_param (',' generic_param)*
# [022] size_param_list
size_param_list ::= size_param (',' size_param)*
# [023] generic_param
generic_param ::= IDENTIFIER generic_bound? generic_type_default?
# [024] size_param
size_param ::= 'size' IDENTIFIER generic_size_default?
# [025] generic_bound
generic_bound ::= 'implements' contract_ref ('∩' contract_ref)*
# [026] contract_ref
contract_ref ::= IDENTIFIER ('<' type_annotation (',' type_annotation)* '>')?
# [027] generic_type_default
generic_type_default ::= '=' type_annotation
# [028] generic_size_default
generic_size_default ::= '=' NATURAL
# [029] call_type_args
call_type_args ::= '<' type_annotation (',' type_annotation)* '>'
# [030] parameter
parameter ::= 'rest'? type_annotation IDENTIFIER 'optional'? ('as' IDENTIFIER)? ('coalesce' expression)?
# [031] func_modifier
func_modifier ::= 'args' IDENTIFIER | 'errors' IDENTIFIER | 'exit' (IDENTIFIER | NATURAL) | 'readonly' | 'throws' | 'options' IDENTIFIER
# [032] callable_posture
callable_posture ::= 'async' | 'generator' | 'async_generator'
# [033] return_clause
return_clause ::= '→' type_annotation
# [034] alternate_exit_clause
alternate_exit_clause ::= '⇥' type_annotation
# [035] ergo_joint
ergo_joint ::= 'then'
# [036] clausura_joint
clausura_joint ::= '∴'
# [037] clausura_expr
clausura_expr ::= compact_clausura_expr | clausura_legacy_expr
# [038] compact_clausura_expr
compact_clausura_expr ::= clausura_signature clausura_joint (expression | fac_block)
# [039] clausura_signature
clausura_signature ::= (clausura_param | '(' clausura_params? ')') closure_modifier? return_clause? alternate_exit_clause?
# [040] closure_modifier
closure_modifier ::= 'free' | 'kernel'
# [041] fac_block
fac_block ::= 'do' block_stmt cape_clause?
# [042] clausura_legacy_expr
clausura_legacy_expr ::= 'lambda' clausura_params? closure_modifier? ('→' type_annotation)? (':' expression | block_stmt)
# [043] clausura_params
clausura_params ::= clausura_param (',' clausura_param)*
# [044] clausura_param
clausura_param ::= type_annotation IDENTIFIER
# [045] genus_decl
genus_decl ::= 'class' IDENTIFIER generic_params? ('implements' contract_ref ((',' | '∩') contract_ref)*)? '{' genus_member* '}'
# [046] genus_member
genus_member ::= annotation* (genus_field_decl | functio_method_decl)
# [047] genus_field_decl
genus_field_decl ::= ('const' | 'var' | 'static') type_annotation IDENTIFIER 'optional'? ('=' const_init)?
# [048] field_decl
field_decl ::= ('const' | 'var' | 'static')? type_annotation IDENTIFIER 'optional'? ('=' const_init)?
# [049] functio_method_decl
functio_method_decl ::= 'fn' IDENTIFIER generic_params? '(' param_list ')' func_modifier* callable_posture? return_clause? alternate_exit_clause? block_stmt
```

## Terms {#terms}

Keywords in these productions that have a corpus term page. The production id
on the left is the Latin spine name; the links are the English reader spellings
you write.

| Production | Terms |
|---|---|
| `insere_expr` | [`embed`](/en-US/corpus/embed.html) |
| `fixum_decl` | [`const`](/en-US/corpus/const.html), [`var`](/en-US/corpus/var.html) |
| `figendum_decl` | [`await_const`](/en-US/corpus/await_const.html), [`await_var`](/en-US/corpus/await_var.html) |
| `sit_decl` | [`let`](/en-US/corpus/let.html) |
| `array_destruct` | [`const`](/en-US/corpus/const.html), [`var`](/en-US/corpus/var.html) |
| `object_destruct` | [`const`](/en-US/corpus/const.html), [`var`](/en-US/corpus/var.html) |
| `functio_decl` | [`fn`](/en-US/corpus/fn.html) |
| `generic_bound` | [`implements`](/en-US/corpus/implements.html) |
| `parameter` | [`rest`](/en-US/corpus/rest.html), [`optional`](/en-US/corpus/optional.html), [`as`](/en-US/corpus/as.html), [`coalesce`](/en-US/corpus/coalesce.html) |
| `func_modifier` | [`args`](/en-US/corpus/args.html), [`errors`](/en-US/corpus/errors.html), [`exit`](/en-US/corpus/exit.html), [`throws`](/en-US/corpus/throws.html), [`readonly`](/en-US/corpus/readonly.html), [`options`](/en-US/corpus/options.html) |
| `callable_posture` | [`async_generator`](/en-US/corpus/async_generator.html), [`async`](/en-US/corpus/async.html), [`generator`](/en-US/corpus/generator.html) |
| `ergo_joint` | [`then`](/en-US/corpus/then.html) |
| `closure_modifier` | [`free`](/en-US/corpus/free.html), [`kernel`](/en-US/corpus/kernel.html) |
| `fac_block` | [`do`](/en-US/corpus/do.html) |
| `clausura_legacy_expr` | [`lambda`](/en-US/corpus/lambda.html) |
| `genus_decl` | [`class`](/en-US/corpus/class.html), [`implements`](/en-US/corpus/implements.html) |
| `genus_field_decl` | [`const`](/en-US/corpus/const.html), [`static`](/en-US/corpus/static.html), [`optional`](/en-US/corpus/optional.html), [`var`](/en-US/corpus/var.html) |
| `field_decl` | [`const`](/en-US/corpus/const.html), [`static`](/en-US/corpus/static.html), [`optional`](/en-US/corpus/optional.html), [`var`](/en-US/corpus/var.html) |
| `functio_method_decl` | [`fn`](/en-US/corpus/fn.html) |
