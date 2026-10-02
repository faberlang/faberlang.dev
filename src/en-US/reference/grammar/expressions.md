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

Rule names (`fab_file`, `itera_stmt`) are the stable Latin grammar identifiers;
the quoted words are the English reader spellings. Return to the
[grammar index](/en-US/reference/grammar.html).

## Productions {#productions}

```ebnf
# [155] expression
expression ::= assignment
# [156] transfer
transfer ::= ternary ('⇇' ternary)*
# [157] assignment
assignment ::= transfer ('←' assignment | '↤' assignment inline_default?)?
# [159] place
place ::= call_expr
# [160] ternary
ternary ::= aut_expr ('✓' expression '✗' aut_expr)?
# [161] aut_expr
aut_expr ::= et_expr (('or') et_expr)*
# [162] et_expr
et_expr ::= equality (('and') equality)*
# [163] equality
equality ::= comparison equality_tail*
# [164] equality_tail
equality_tail ::= ('≡' | '≢' | '≠' | '≅' | '≇' | '≈' | '≉') comparison | ('is' | 'not' 'is') type_annotation
# [165] comparison
comparison ::= format_expr (('≺' | '≻' | '≤' | '≥' | '∈' | '∉') format_expr)*
# [166] format_expr
format_expr ::= bitwise_or_expr ('¶' STRING)?
# [167] bitwise_or_expr
bitwise_or_expr ::= bitwise_xor_expr ('∨' bitwise_xor_expr)*
# [168] bitwise_xor_expr
bitwise_xor_expr ::= bitwise_and_expr ('⊻' bitwise_and_expr)*
# [169] bitwise_and_expr
bitwise_and_expr ::= shift_expr ('∧' shift_expr)*
# [170] shift_expr
shift_expr ::= range_expr (('⇐' | '⇒') range_expr)*
# [171] range_expr
range_expr ::= additive_expr range_tail?
# [172] range_tail
range_tail ::= ('‥' | '…' | 'before' | 'until') additive_expr ('step' additive_expr)?
# [173] additive_expr
additive_expr ::= multiplicative_expr (('+' | '-' | '⤒' | '⤓') multiplicative_expr)*
# [174] multiplicative_expr
multiplicative_expr ::= vel_expr (('*' | '/' | '÷' | '%' | '·' | '×' | '⊗' | '⊙' | '⊘') vel_expr)*
# [175] vel_expr
vel_expr ::= unary_expr ('coalesce' vel_rhs)*
# [176] vel_rhs
vel_rhs ::= unary_expr vel_range_tail?
# [177] vel_range_tail
vel_range_tail ::= ('‥' | '…' | 'before' | 'until') unary_expr ('step' unary_expr)?
# [178] unary_expr
unary_expr ::= ('-' | '¬' | 'not') unary_expr | finge_expr | cast_expr
# [179] gradient_expr
gradient_expr ::= call_expr ('∇' gradient_selection?)?
# [180] gradient_selection
gradient_selection ::= '[' gradient_place (',' gradient_place)* ']'
# [181] gradient_place
gradient_place ::= expression
# [182] cast_expr
cast_expr ::= gradient_expr ('∷' type_annotation | conversio_expr)* inline_default?
# [183] conversio_expr
conversio_expr ::= '↦' (type_annotation | interval_target) via_clause? inline_default?
# [184] interval_target
interval_target ::= range_expr
# [185] via_clause
via_clause ::= 'via' IDENTIFIER
# [186] inline_default
inline_default ::= '⊥' unary_expr
# [187] call_expr
call_expr ::= primary (call_suffix | member_suffix | transpose_suffix | optional_suffix | non_null_suffix)*
# [188] call_suffix
call_suffix ::= call_type_args? '(' argument_list ')'
# [189] member_suffix
member_suffix ::= '.' IDENTIFIER | '[' expression ']'
# [190] transpose_suffix
transpose_suffix ::= 'ᵀ'
# [191] optional_suffix
optional_suffix ::= '?.' IDENTIFIER | '?[' expression ']' | '?(' argument_list ')'
# [192] non_null_suffix
non_null_suffix ::= '!.' IDENTIFIER | '![' expression ']' | '!(' argument_list ')'
# [193] argument_list
argument_list ::= (argument (',' argument)*)?
# [194] argument
argument ::= template_argument | 'spread'? expression
# [195] template_argument
template_argument ::= 'spread'? IDENTIFIER ':' expression
# [196] literal
literal ::= NUMBER | STRING | ASCII_STRING | BACKTICK_STRING | OCTETI_STRING | 'true' | 'false' | 'null' | '∞' | 'nan'
# [197] primary
primary ::= IDENTIFIER | literal | 'self' | array_literal | json_literal | typed_constructor | iuncta_expr | ad_expr | clausura_expr | praefixum_expr | scriptum_expr | lege_expr | first_match_expr | summa_expr | extrema_expr | capta_expr | '(' expression ')'
# [198] ad_expr
ad_expr ::= 'call' ASCII_STRING ad_opener?
# [199] ad_opener
ad_opener ::= '(' expression ')'
# [200] array_literal
array_literal ::= '[' argument_list? ']'
# [201] iuncta_expr
iuncta_expr ::= 'tuple' type_arguments '[' argument_list? ']'
# [202] json_literal
json_literal ::= '{' (json_member (',' json_member)*)? '}'
# [203] json_member
json_member ::= STRING ':' json_value
# [204] typed_constructor
typed_constructor ::= type_annotation '{' field_list? '}' construction_source?
# [205] field_list
field_list ::= field_init (',' field_init)*
# [206] field_init
field_init ::= (field_key '=' expression) | IDENTIFIER
# [207] field_key
field_key ::= IDENTIFIER | STRING | '[' expression ']'
# [208] construction_source
construction_source ::= 'from' call_expr
# [209] json_value
json_value ::= json_object | json_array | json_string | json_number | 'true' | 'false' | 'null'
# [210] json_object
json_object ::= '{' (json_member (',' json_member)*)? '}'
# [211] json_array
json_array ::= '[' (json_value (',' json_value)*)? ']'
# [212] json_string
json_string ::= STRING
# [213] json_number
json_number ::= NUMBER
# [214] finge_expr
finge_expr ::= 'variant' qualified_ident ('{' field_list? '}')? ('∷' type_annotation)?
# [215] qualified_ident
qualified_ident ::= IDENTIFIER ('.' IDENTIFIER)*
# [216] praefixum_expr
praefixum_expr ::= 'comptime' block_stmt
# [217] scriptum_expr
scriptum_expr ::= 'format' '(' STRING (',' expression)* ')'
# [218] lege_expr
lege_expr ::= 'read' 'line'?
# [219] first_match_expr
first_match_expr ::= 'primus_quem' '(' expression apud_clause? ',' 'ubi' IDENTIFIER block_stmt ')'
# [220] summa_expr
summa_expr ::= 'sum' 'from' expression apud_clause? filum_clause? ('const' | 'var') IDENTIFIER block_stmt
# [221] filum_clause
filum_clause ::= 'thread' IDENTIFIER
# [222] extrema_expr
extrema_expr ::= ('max' | 'min') 'from' expression apud_clause? extrema_identity?
# [223] extrema_identity
extrema_identity ::= 'coalesce' expression
# [224] capta_expr
capta_expr ::= 'trap' block_stmt
```

## Terms {#terms}

Keywords in these productions that have a corpus term page. The production id
on the left is the Latin spine name; the links are the English reader spellings
you write.

| Production | Terms |
|---|---|
| `aut_expr` | [`or`](/en-US/corpus/or.html) |
| `et_expr` | [`and`](/en-US/corpus/and.html) |
| `equality_tail` | [`is`](/en-US/corpus/is.html), [`is`](/en-US/corpus/is.html), [`not`](/en-US/corpus/not.html) |
| `range_tail` | [`before`](/en-US/corpus/before.html), [`step`](/en-US/corpus/step.html), [`until`](/en-US/corpus/until.html) |
| `vel_expr` | [`coalesce`](/en-US/corpus/coalesce.html) |
| `vel_range_tail` | [`before`](/en-US/corpus/before.html), [`step`](/en-US/corpus/step.html), [`until`](/en-US/corpus/until.html) |
| `unary_expr` | [`not`](/en-US/corpus/not.html) |
| `argument` | [`spread`](/en-US/corpus/spread.html) |
| `template_argument` | [`spread`](/en-US/corpus/spread.html) |
| `literal` | [`false`](/en-US/corpus/false.html), [`null`](/en-US/corpus/null.html), [`true`](/en-US/corpus/true.html) |
| `primary` | [`self`](/en-US/corpus/self.html) |
| `ad_expr` | [`call`](/en-US/corpus/call.html) |
| `iuncta_expr` | [`tuple`](/en-US/corpus/tuple.html) |
| `construction_source` | [`from`](/en-US/corpus/from.html) |
| `finge_expr` | [`variant`](/en-US/corpus/variant.html) |
| `praefixum_expr` | [`comptime`](/en-US/corpus/comptime.html) |
| `scriptum_expr` | [`format`](/en-US/corpus/format.html) |
| `lege_expr` | [`read`](/en-US/corpus/read.html), [`line`](/en-US/corpus/line.html) |
| `first_match_expr` | [`primus_quem`](/en-US/corpus/primus_quem.html) |
| `summa_expr` | [`from`](/en-US/corpus/from.html), [`const`](/en-US/corpus/const.html), [`sum`](/en-US/corpus/sum.html), [`var`](/en-US/corpus/var.html) |
| `extrema_expr` | [`from`](/en-US/corpus/from.html) |
| `extrema_identity` | [`coalesce`](/en-US/corpus/coalesce.html) |
