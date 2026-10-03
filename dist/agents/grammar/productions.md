# Grammar productions

Every Faber grammar rule, in EBNF, with the words in quotes shown in the
English reader spellings. Rule names and UPPERCASE lexical terminals are the
stable Latin identities. The compiler's own grammar is the authority; this page
is generated from it. Grammar examples are fragments, not standalone programs.
For the short forms the other pages use, read
https://faberlang.dev/agents/grammar.md. The human grammar overview is
https://faberlang.dev/en-US/reference/grammar.html.

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
# [050] annotation
annotation ::= nucleum_annotation | radix_annotation | braced_annotation | annotation_sugar
# [051] annotation_name
annotation_name ::= ANNOTATION_NAME
# [052] braced_annotation
braced_annotation ::= '@' annotation_name '{' annotation_field_list? '}'
# [053] annotation_field_list
annotation_field_list ::= annotation_field (',' annotation_field)*
# [054] annotation_field
annotation_field ::= ANNOTATION_FIELD_NAME '=' (expression | concrete_type)
# [055] annotation_sugar
annotation_sugar ::= '@' annotation_name NON_NEWLINE_TOKEN* NEWLINE
# [056] nucleum_annotation
nucleum_annotation ::= nucleum_sugar | nucleum_braced
# [057] nucleum_sugar
nucleum_sugar ::= '@' 'kernel' nucleum_modifier? NEWLINE
# [058] nucleum_braced
nucleum_braced ::= '@' 'kernel' '{' nucleum_field_list? '}'
# [059] nucleum_modifier
nucleum_modifier ::= 'fragment'
# [060] nucleum_field_list
nucleum_field_list ::= nucleum_field (',' nucleum_field)*
# [061] nucleum_field
nucleum_field ::= 'fragment' '=' ('true' | 'false')
# [062] radix_annotation
radix_annotation ::= '@' 'radix' radix_directive NEWLINE
# [063] radix_directive
radix_directive ::= 'lane' STRING | 'backward' STRING | 'contract' STRING | 'type' IDENTIFIER 'mut' concrete_type+
# [064] ad_annotation
ad_annotation ::= '@' 'call' ASCII_STRING NEWLINE
# [065] implendum_decl
implendum_decl ::= 'interface' IDENTIFIER generic_params? '{' implendum_method_decl* '}'
# [066] implendum_method_decl
implendum_method_decl ::= annotation* 'fn' IDENTIFIER '(' param_list ')' func_modifier* callable_posture? return_clause? alternate_exit_clause?
# [067] typus_decl
typus_decl ::= 'type' IDENTIFIER generic_params? '=' type_annotation
# [068] ordo_decl
ordo_decl ::= 'enum' IDENTIFIER '{' enum_member (',' enum_member)* '}'
# [069] enum_member
enum_member ::= IDENTIFIER ('=' ('-'? NUMBER | STRING))?
# [070] discretio_decl
discretio_decl ::= 'union' IDENTIFIER generic_params? '{' union_fields? variant (',' variant)* '}'
# [071] union_fields
union_fields ::= annotation+ field_decl union_member*
# [072] union_member
union_member ::= annotation* field_decl
# [073] variant
variant ::= IDENTIFIER ('{' variant_fields '}')?
# [074] variant_fields
variant_fields ::= (type_annotation IDENTIFIER)*
# [075] schema_decl
schema_decl ::= 'schema' IDENTIFIER '{' (schema_column (NEWLINE schema_column)*)? '}'
# [076] schema_column
schema_column ::= 'column' type_annotation IDENTIFIER (':' IDENTIFIER)?
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
# [092] type_annotation
type_annotation ::= union_hole_type | concrete_type
# [093] concrete_type
concrete_type ::= intersection_type ('∪' intersection_type)*
# [094] union_hole_type
union_hole_type ::= ('ref' | 'mut' | 'own' | 'copy')? '∪'
# [095] intersection_type
intersection_type ::= owned_type ('∩' owned_type)*
# [096] owned_type
owned_type ::= ('ref' | 'mut' | 'own' | 'copy')? base_type
# [097] base_type
base_type ::= hole_type | function_type | width_type_sugar | ratio_type | failable_promissum_type | qualified_type type_arguments?
# [098] failable_promissum_type
failable_promissum_type ::= IDENTIFIER '<' type_annotation alternate_exit_clause '>'
# [099] ratio_type
ratio_type ::= 'record' '<' labeled_type_argument (',' labeled_type_argument)* '>'
# [100] hole_type
hole_type ::= '_'
# [101] qualified_type
qualified_type ::= type_head ('.' IDENTIFIER)*
# [102] type_head
type_head ::= IDENTIFIER | 'wrapping'
# [103] type_arguments
type_arguments ::= '<' type_argument (',' type_argument)* '>'
# [104] type_argument
type_argument ::= labeled_type_argument | type_annotation | NATURAL | '[' figura_list? ']'
# [105] labeled_type_argument
labeled_type_argument ::= IDENTIFIER ':' type_annotation
# [106] width_type_sugar
width_type_sugar ::= WIDTH_MARKER | LISTA_WIDTH_SUGAR | (TENSOR_WIDTH_SUGAR | SPARSA_WIDTH_SUGAR | VECTOR_WIDTH_SUGAR) shape_suffix? | MATRIX_WIDTH_SUGAR shape_suffix
# [107] shape_suffix
shape_suffix ::= '[' figura_list? ']'
# [108] figura
figura ::= figura_product (('+' | '-') NATURAL)*
# [109] figura_product
figura_product ::= figura_primary ('/' NATURAL)*
# [110] figura_primary
figura_primary ::= '_' | NATURAL | IDENTIFIER | '[' figura_list? ']' | '(' figura ')'
# [111] figura_list
figura_list ::= figura (',' figura)*
# [112] function_type
function_type ::= '(' type_list? ')' '→' type_annotation alternate_exit_clause?
# [113] type_list
type_list ::= type_annotation (',' type_annotation)*
# [114] si_stmt
si_stmt ::= 'if' si_tail
# [115] si_tail
si_tail ::= expression arm ('elif' si_tail | secus_clause)?
# [116] secus_clause
secus_clause ::= 'else' else_arm
# [117] arm
arm ::= (block_stmt | ergo_joint statement) cape_clause?
# [118] else_arm
else_arm ::= (block_stmt | ergo_joint statement) cape_clause?
# [119] dum_stmt
dum_stmt ::= 'while' expression (block_stmt | ergo_joint statement) cape_clause?
# [120] itera_stmt
itera_stmt ::= 'for' ('from' expression (',' expression)* | 'ref' expression | 'range' expression (',' expression)*) apud_clause? ('const' | 'var') itera_binding (block_stmt | ergo_joint statement) cape_clause?
# [121] itera_binding
itera_binding ::= array_pattern | object_pattern | IDENTIFIER (',' IDENTIFIER)*
# [122] apud_clause
apud_clause ::= 'at' '[' IDENTIFIER (',' IDENTIFIER)* ']'
# [123] elige_stmt
elige_stmt ::= 'switch' expression '{' casu_elige_clause* ceterum_clause? '}' cape_clause?
# [124] casu_elige_clause
casu_elige_clause ::= 'case' expression (block_stmt | ergo_joint statement)
# [125] ceterum_clause
ceterum_clause ::= 'default' (block_stmt | ergo_joint statement)
# [126] discerne_stmt
discerne_stmt ::= 'match' 'all'? discriminants '{' casu_variant_clause* ceterum_clause? '}'
# [127] discriminants
discriminants ::= subject_path ('and' subject_path)*
# [128] subject_path
subject_path ::= IDENTIFIER ('.' IDENTIFIER)*
# [129] casu_variant_clause
casu_variant_clause ::= 'case' patterns (block_stmt | ergo_joint statement)
# [130] patterns
patterns ::= pattern ('and' pattern)*
# [131] pattern
pattern ::= pattern_atom ('or' pattern_atom)*
# [132] pattern_atom
pattern_atom ::= '_' | negated_number | literal | type_pattern | (IDENTIFIER ut_pattern?)
# [133] negated_number
negated_number ::= '-' NUMBER
# [134] type_pattern
type_pattern ::= IDENTIFIER type_arguments? ut_pattern?
# [135] ut_pattern
ut_pattern ::= ('as' IDENTIFIER) | (('const' | 'var') pattern_binding (',' pattern_binding)*)
# [136] pattern_binding
pattern_binding ::= IDENTIFIER ('as' IDENTIFIER)?
# [137] custodi_stmt
custodi_stmt ::= 'guard' '{' si_guard_clause+ '}'
# [138] si_guard_clause
si_guard_clause ::= 'if' expression (block_stmt | ergo_joint statement)
# [139] ex_stmt
ex_stmt ::= 'from' expression ('const' | 'var') extract_fields
# [140] extract_fields
extract_fields ::= extract_field (',' extract_field)* (',' ceteri_field)? | ceteri_field
# [141] extract_field
extract_field ::= IDENTIFIER ('as' IDENTIFIER)?
# [142] ceteri_field
ceteri_field ::= 'rest' IDENTIFIER
# [143] redde_stmt
redde_stmt ::= 'return' expression?
# [144] reddet_stmt
reddet_stmt ::= 'return_await' expression
# [145] tacebit_stmt
tacebit_stmt ::= 'await' expression
# [146] cede_stmt
cede_stmt ::= 'yield' expression
# [147] rumpe_stmt
rumpe_stmt ::= 'break'
# [148] perge_stmt
perge_stmt ::= 'continue'
# [149] tacet_stmt
tacet_stmt ::= 'pass'
# [150] iace_stmt
iace_stmt ::= iace_expr | iace_guarded_expr
# [151] iace_expr
iace_expr ::= ('throw' | 'panic') expression
# [152] iace_guarded_expr
iace_guarded_expr ::= ('throw' | 'panic') expression NO_NEWLINE 'if' expression
# [153] cape_clause
cape_clause ::= 'catch' IDENTIFIER block_stmt
# [154] adfirma_stmt
adfirma_stmt ::= 'assert' expression ('panic' expression)?
# [155] requirit_stmt
requirit_stmt ::= 'require' expression 'throw' expression
# [156] reice_stmt
reice_stmt ::= 'reject' expression 'throw' expression
# [157] expression
expression ::= assignment
# [158] transfer
transfer ::= ternary ('⇇' ternary)?
# [159] assignment
assignment ::= transfer ('←' assignment | '↤' assignment inline_default?)?
# [160] inc_dec_stmt
inc_dec_stmt ::= place ('↑' | '↓')
# [161] place
place ::= call_expr
# [162] ternary
ternary ::= aut_expr ('✓' expression '✗' aut_expr)?
# [163] aut_expr
aut_expr ::= et_expr (('or') et_expr)*
# [164] et_expr
et_expr ::= equality (('and') equality)*
# [165] equality
equality ::= comparison equality_tail*
# [166] equality_tail
equality_tail ::= ('≡' | '≢' | '≠' | '≅' | '≇' | '≈' | '≉') comparison | ('is' | 'not' 'is') type_annotation
# [167] comparison
comparison ::= format_expr (('≺' | '≻' | '≤' | '≥' | '∈' | '∉') format_expr)*
# [168] format_expr
format_expr ::= bitwise_or_expr ('¶' STRING)?
# [169] bitwise_or_expr
bitwise_or_expr ::= bitwise_xor_expr ('∨' bitwise_xor_expr)*
# [170] bitwise_xor_expr
bitwise_xor_expr ::= bitwise_and_expr ('⊻' bitwise_and_expr)*
# [171] bitwise_and_expr
bitwise_and_expr ::= shift_expr ('∧' shift_expr)*
# [172] shift_expr
shift_expr ::= range_expr (('⇐' | '⇒') range_expr)*
# [173] range_expr
range_expr ::= additive_expr range_tail?
# [174] range_tail
range_tail ::= ('‥' | '…' | 'before' | 'until') additive_expr ('step' additive_expr)?
# [175] additive_expr
additive_expr ::= multiplicative_expr (('+' | '-' | '⤒' | '⤓') multiplicative_expr)*
# [176] multiplicative_expr
multiplicative_expr ::= vel_expr (('*' | '/' | '÷' | '%' | '·' | '×' | '⊗' | '⊙' | '⊘') vel_expr)*
# [177] vel_expr
vel_expr ::= unary_expr ('coalesce' vel_rhs)*
# [178] vel_rhs
vel_rhs ::= unary_expr vel_range_tail?
# [179] vel_range_tail
vel_range_tail ::= ('‥' | '…' | 'before' | 'until') unary_expr ('step' unary_expr)?
# [180] unary_expr
unary_expr ::= ('-' | '¬' | 'not') unary_expr | finge_expr | cast_expr
# [181] gradient_expr
gradient_expr ::= call_expr ('∇' gradient_selection?)?
# [182] gradient_selection
gradient_selection ::= '[' gradient_place (',' gradient_place)* ']'
# [183] gradient_place
gradient_place ::= expression
# [184] cast_expr
cast_expr ::= gradient_expr ('∷' type_annotation | conversio_expr)* inline_default?
# [185] conversio_expr
conversio_expr ::= '↦' (type_annotation | interval_target) via_clause? inline_default?
# [186] interval_target
interval_target ::= range_expr
# [187] via_clause
via_clause ::= 'via' IDENTIFIER
# [188] inline_default
inline_default ::= '⊥' unary_expr
# [189] call_expr
call_expr ::= primary (call_suffix | member_suffix | transpose_suffix | optional_suffix | non_null_suffix)*
# [190] call_suffix
call_suffix ::= call_type_args? '(' argument_list ')'
# [191] member_suffix
member_suffix ::= '.' IDENTIFIER | '[' expression ']'
# [192] transpose_suffix
transpose_suffix ::= 'ᵀ'
# [193] optional_suffix
optional_suffix ::= '?.' IDENTIFIER | '?[' expression ']' | '?(' argument_list ')'
# [194] non_null_suffix
non_null_suffix ::= '!.' IDENTIFIER | '![' expression ']' | '!(' argument_list ')'
# [195] argument_list
argument_list ::= (argument (',' argument)*)?
# [196] argument
argument ::= template_argument | 'spread'? expression
# [197] template_argument
template_argument ::= 'spread'? IDENTIFIER ':' expression
# [198] literal
literal ::= NUMBER | STRING | ASCII_STRING | BACKTICK_STRING | OCTETI_STRING | 'true' | 'false' | 'null' | '∞' | 'nan'
# [199] primary
primary ::= IDENTIFIER | literal | 'self' | array_literal | json_literal | typed_constructor | iuncta_expr | ad_expr | clausura_expr | praefixum_expr | scriptum_expr | lege_expr | first_match_expr | summa_expr | extrema_expr | capta_expr | '(' expression ')'
# [200] ad_expr
ad_expr ::= 'call' ASCII_STRING ad_opener?
# [201] ad_opener
ad_opener ::= '(' expression ')'
# [202] array_literal
array_literal ::= '[' array_element_list? ']'
# [203] array_element_list
array_element_list ::= array_element (',' array_element)* ','?
# [204] array_element
array_element ::= argument | '_'
# [205] iuncta_expr
iuncta_expr ::= 'tuple' type_arguments '[' argument_list? ']'
# [206] json_literal
json_literal ::= '{' (json_member (',' json_member)*)? '}'
# [207] json_member
json_member ::= STRING ':' json_value
# [208] typed_constructor
typed_constructor ::= type_annotation '{' field_list? '}' construction_source?
# [209] field_list
field_list ::= field_init (',' field_init)*
# [210] field_init
field_init ::= (field_key '=' expression) | IDENTIFIER
# [211] field_key
field_key ::= IDENTIFIER | STRING | '[' expression ']'
# [212] construction_source
construction_source ::= 'from' call_expr
# [213] json_value
json_value ::= json_object | json_array | json_string | json_number | 'true' | 'false' | 'null'
# [214] json_object
json_object ::= '{' (json_member (',' json_member)*)? '}'
# [215] json_array
json_array ::= '[' (json_value (',' json_value)*)? ']'
# [216] json_string
json_string ::= STRING
# [217] json_number
json_number ::= NUMBER
# [218] finge_expr
finge_expr ::= 'variant' qualified_ident ('{' field_list? '}')? ('∷' type_annotation)?
# [219] qualified_ident
qualified_ident ::= IDENTIFIER ('.' IDENTIFIER)*
# [220] praefixum_expr
praefixum_expr ::= 'comptime' block_stmt
# [221] scriptum_expr
scriptum_expr ::= 'format' '(' STRING (',' expression)* ')'
# [222] lege_expr
lege_expr ::= 'read' 'line'?
# [223] first_match_expr
first_match_expr ::= 'primus_quem' '(' expression apud_clause? ',' 'ubi' IDENTIFIER block_stmt ')'
# [224] summa_expr
summa_expr ::= 'sum' 'from' expression apud_clause? filum_clause? ('const' | 'var') IDENTIFIER block_stmt
# [225] filum_clause
filum_clause ::= 'thread' IDENTIFIER
# [226] extrema_expr
extrema_expr ::= ('max' | 'min') 'from' expression apud_clause? extrema_identity?
# [227] extrema_identity
extrema_identity ::= 'coalesce' expression
# [228] capta_expr
capta_expr ::= 'trap' block_stmt
# [229] object_pattern
object_pattern ::= '{' pattern_property (',' pattern_property)* '}'
# [230] pattern_property
pattern_property ::= 'rest'? IDENTIFIER ('as' IDENTIFIER)?
# [231] array_pattern
array_pattern ::= '[' array_pattern_element (',' array_pattern_element)* ']'
# [232] array_pattern_element
array_pattern_element ::= '_' | 'rest'? IDENTIFIER
# [233] nota_stmt
nota_stmt ::= ('print' | 'debug' | 'warn' | 'write') expression (',' expression)*
# [234] entry_header
entry_header ::= ('args' IDENTIFIER)? ('exit' expression)?
# [235] incipit_stmt
incipit_stmt ::= 'main' entry_header block_stmt
# [236] incipiet_stmt
incipiet_stmt ::= 'async_main' entry_header block_stmt
# [237] probandum_decl
probandum_decl ::= 'describe' STRING proba_modifier* '{' probandum_body '}'
# [238] probandum_body
probandum_body ::= (praepara_block | probandum_decl | proba_stmt)*
# [239] proba_stmt
proba_stmt ::= 'test' STRING proba_modifier* block_stmt
# [240] proba_modifier
proba_modifier ::= 'expect_failure' | 'skip' STRING | 'todo' STRING | 'only' | 'tag' STRING | 'timeout' NATURAL | 'bench' | 'repeat' NATURAL | 'flaky' NATURAL | 'only_in' STRING
# [241] praepara_block
praepara_block ::= ('setup' | 'async_setup' | 'teardown' | 'async_teardown') 'all'? block_stmt
# [242] fac_stmt
fac_stmt ::= 'do' block_stmt cape_clause? ('while' expression)?
# [243] IDENTIFIER
IDENTIFIER ::=
# [244] NUMBER
NUMBER ::=
# [245] NATURAL
NATURAL ::=
# [246] STRING
STRING ::=
# [247] ASCII_STRING
ASCII_STRING ::=
# [248] BACKTICK_STRING
BACKTICK_STRING ::=
# [249] OCTETI_STRING
OCTETI_STRING ::=
# [250] NEWLINE
NEWLINE ::=
# [251] WIDTH_MARKER
WIDTH_MARKER ::=
# [252] LISTA_WIDTH_SUGAR
LISTA_WIDTH_SUGAR ::=
# [253] TENSOR_WIDTH_SUGAR
TENSOR_WIDTH_SUGAR ::=
# [254] SPARSA_WIDTH_SUGAR
SPARSA_WIDTH_SUGAR ::=
# [255] VECTOR_WIDTH_SUGAR
VECTOR_WIDTH_SUGAR ::=
# [256] MATRIX_WIDTH_SUGAR
MATRIX_WIDTH_SUGAR ::=
# [257] FRONTMATTER_DELIMITER
FRONTMATTER_DELIMITER ::=
# [258] TOML_LINES
TOML_LINES ::=
# [259] ANNOTATION_NAME
ANNOTATION_NAME ::=
# [260] ANNOTATION_FIELD_NAME
ANNOTATION_FIELD_NAME ::=
# [261] NON_NEWLINE_TOKEN
NON_NEWLINE_TOKEN ::=
# [262] NO_NEWLINE
NO_NEWLINE ::=
```

Fetch list: https://faberlang.dev/agents/index.md
