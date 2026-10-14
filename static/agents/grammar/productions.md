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
statement ::= annotation* statement_core | ad_handler_decl | nondum_functio_decl
# [006] ad_handler_decl
ad_handler_decl ::= annotation* ad_annotation annotation* functio_decl
# [007] nondum_functio_decl
nondum_functio_decl ::= annotation* nondum_annotation annotation* 'fn' IDENTIFIER generic_params? '(' param_list ')' func_modifier* callable_posture? return_clause? alternate_exit_clause?
# [008] statement_core
statement_core ::= importa_decl | binding_decl | functio_decl | genus_decl | implendum_decl | typus_decl | ordo_decl | discretio_decl | schema_decl | si_stmt | dum_stmt | itera_stmt | elige_stmt | discerne_stmt | custodi_stmt | fac_stmt | redde_stmt | reddet_stmt | tacebit_stmt | cede_stmt | rumpe_stmt | perge_stmt | tacet_stmt | iace_stmt | adfirma_stmt | requirit_stmt | reice_stmt | nota_stmt | incipit_stmt | incipiet_stmt | ex_stmt | probandum_decl | proba_stmt | block_stmt | inc_dec_stmt | expr_stmt
# [009] binding_decl
binding_decl ::= fixum_decl | sit_decl | array_destruct | object_destruct | figendum_decl
# [010] expr_stmt
expr_stmt ::= expression
# [011] block_stmt
block_stmt ::= '{' statement* '}'
# [012] const_init
const_init ::= insere_expr | expression
# [013] insere_expr
insere_expr ::= 'embed' STRING
# [014] fixum_decl
fixum_decl ::= ('const' | 'var') type_annotation IDENTIFIER (('←' value_marker? expression) | ('=' const_init) | ('↤' assignment inline_default?) | ('↢' expression))?
# [015] figendum_decl
figendum_decl ::= ('await_const' | 'await_var') type_annotation IDENTIFIER '←' expression
# [016] sit_decl
sit_decl ::= 'let' IDENTIFIER (('←' | '↢') expression)?
# [017] array_destruct
array_destruct ::= ('const' | 'var') array_pattern '←' expression
# [018] object_destruct
object_destruct ::= ('const' | 'var') object_pattern '←' expression
# [019] functio_decl
functio_decl ::= 'fn' IDENTIFIER generic_params? '(' param_list ')' func_modifier* callable_posture? return_clause? alternate_exit_clause? block_stmt
# [020] param_list
param_list ::= (parameter (',' parameter)*)?
# [021] generic_params
generic_params ::= '<' (type_param_list (',' size_param_list)? | size_param_list) '>'
# [022] type_param_list
type_param_list ::= generic_param (',' generic_param)*
# [023] size_param_list
size_param_list ::= size_param (',' size_param)*
# [024] generic_param
generic_param ::= IDENTIFIER generic_bound? generic_type_default?
# [025] size_param
size_param ::= 'size' IDENTIFIER generic_size_default?
# [026] generic_bound
generic_bound ::= 'implements' contract_ref ('∩' contract_ref)*
# [027] contract_ref
contract_ref ::= IDENTIFIER ('<' type_annotation (',' type_annotation)* '>')?
# [028] generic_type_default
generic_type_default ::= '=' type_annotation
# [029] generic_size_default
generic_size_default ::= '=' NATURAL
# [030] call_type_args
call_type_args ::= '<' call_type_arg (',' call_type_arg)* '>'
# [031] call_type_arg
call_type_arg ::= type_annotation | call_size_arg
# [032] call_size_arg
call_size_arg ::= NATURAL dimension_tail? | IDENTIFIER dimension_tail | spelled_lift | '[' figura_list? ']'
# [033] dimension_tail
dimension_tail ::= ('/' NATURAL)+ (('+' | '-') NATURAL)* | (('+' | '-') NATURAL)+
# [034] parameter
parameter ::= 'rest'? 'axis'? type_annotation IDENTIFIER 'optional'? ('as' IDENTIFIER)? ('coalesce' expression)?
# [035] func_modifier
func_modifier ::= 'args' IDENTIFIER | 'errors' IDENTIFIER | 'exit' (IDENTIFIER | NATURAL) | 'readonly' | 'throws' | 'options' IDENTIFIER
# [036] callable_posture
callable_posture ::= 'async' | 'generator' | 'async_generator'
# [037] return_clause
return_clause ::= '→' type_annotation
# [038] alternate_exit_clause
alternate_exit_clause ::= '⇥' type_annotation
# [039] ergo_joint
ergo_joint ::= 'then'
# [040] clausura_joint
clausura_joint ::= '∴'
# [041] clausura_expr
clausura_expr ::= compact_clausura_expr | clausura_legacy_expr
# [042] compact_clausura_expr
compact_clausura_expr ::= clausura_signature clausura_joint (expression | fac_block)
# [043] clausura_signature
clausura_signature ::= (clausura_param | '(' clausura_params? ')') return_clause? alternate_exit_clause?
# [044] fac_block
fac_block ::= 'do' block_stmt cape_clause?
# [045] clausura_legacy_expr
clausura_legacy_expr ::= 'lambda' clausura_params? ('→' type_annotation)? (':' expression | block_stmt)
# [046] clausura_params
clausura_params ::= clausura_param (',' clausura_param)*
# [047] clausura_param
clausura_param ::= type_annotation IDENTIFIER
# [048] genus_decl
genus_decl ::= 'class' IDENTIFIER generic_params? ('implements' contract_ref ((',' | '∩') contract_ref)*)? '{' genus_member* '}'
# [049] genus_member
genus_member ::= annotation* (genus_field_decl | functio_method_decl) | nondum_method_decl
# [050] nondum_method_decl
nondum_method_decl ::= annotation* nondum_annotation annotation* 'fn' IDENTIFIER generic_params? '(' param_list ')' func_modifier* callable_posture? return_clause? alternate_exit_clause?
# [051] genus_field_decl
genus_field_decl ::= ('const' | 'var' | 'static') type_annotation IDENTIFIER 'optional'? ('=' const_init)?
# [052] field_decl
field_decl ::= ('const' | 'var' | 'static')? type_annotation IDENTIFIER 'optional'? ('=' const_init)?
# [053] functio_method_decl
functio_method_decl ::= 'fn' IDENTIFIER generic_params? '(' param_list ')' func_modifier* callable_posture? return_clause? alternate_exit_clause? block_stmt
# [054] annotation
annotation ::= nucleum_annotation | radix_annotation | braced_annotation | annotation_sugar
# [055] annotation_name
annotation_name ::= ANNOTATION_NAME
# [056] braced_annotation
braced_annotation ::= '@' annotation_name '{' annotation_field_list? '}'
# [057] annotation_field_list
annotation_field_list ::= annotation_field (',' annotation_field)*
# [058] annotation_field
annotation_field ::= ANNOTATION_FIELD_NAME '=' (expression | concrete_type)
# [059] annotation_sugar
annotation_sugar ::= '@' annotation_name NON_NEWLINE_TOKEN* NEWLINE
# [060] nucleum_annotation
nucleum_annotation ::= nucleum_sugar | nucleum_braced
# [061] nucleum_sugar
nucleum_sugar ::= '@' 'kernel' nucleum_modifier? NEWLINE
# [062] nucleum_braced
nucleum_braced ::= '@' 'kernel' '{' nucleum_field_list? '}'
# [063] nucleum_modifier
nucleum_modifier ::= 'fragment'
# [064] nucleum_field_list
nucleum_field_list ::= nucleum_field (',' nucleum_field)*
# [065] nucleum_field
nucleum_field ::= 'fragment' '=' ('true' | 'false')
# [066] radix_annotation
radix_annotation ::= '@' 'radix' radix_directive NEWLINE
# [067] radix_directive
radix_directive ::= 'lane' STRING | 'backward' STRING | 'contract' STRING | 'type' IDENTIFIER 'mut' concrete_type+
# [068] ad_annotation
ad_annotation ::= '@' 'call' ASCII_STRING NEWLINE
# [069] nondum_annotation
nondum_annotation ::= '@' 'unstable' NON_NEWLINE_TOKEN* NEWLINE | '@' 'unstable' '{' annotation_field_list? '}'
# [070] implendum_decl
implendum_decl ::= 'interface' IDENTIFIER generic_params? '{' implendum_method_decl* '}'
# [071] implendum_method_decl
implendum_method_decl ::= annotation* 'fn' IDENTIFIER '(' param_list ')' func_modifier* callable_posture? return_clause? alternate_exit_clause?
# [072] typus_decl
typus_decl ::= 'type' IDENTIFIER generic_params? '=' type_annotation
# [073] ordo_decl
ordo_decl ::= 'enum' IDENTIFIER '{' enum_member (',' enum_member)* '}'
# [074] enum_member
enum_member ::= IDENTIFIER ('=' ('-'? NUMBER | STRING))?
# [075] discretio_decl
discretio_decl ::= 'union' IDENTIFIER generic_params? '{' union_fields? variant (',' variant)* '}'
# [076] union_fields
union_fields ::= annotation+ field_decl union_member*
# [077] union_member
union_member ::= annotation* field_decl
# [078] variant
variant ::= IDENTIFIER ('{' variant_fields '}')?
# [079] variant_fields
variant_fields ::= (type_annotation IDENTIFIER)*
# [080] schema_decl
schema_decl ::= 'schema' IDENTIFIER '{' (schema_column (NEWLINE schema_column)*)? '}'
# [081] schema_column
schema_column ::= 'column' type_annotation IDENTIFIER (':' IDENTIFIER)?
# [082] importa_decl
importa_decl ::= importa_record | importa_sugar
# [083] importa_record
importa_record ::= 'import' '{' import_field_list '}'
# [084] import_field_list
import_field_list ::= import_field (',' import_field)*
# [085] import_field
import_field ::= ex_field | visibilitas_field | nomen_field | ut_field | omnia_field
# [086] ex_field
ex_field ::= 'from' '=' STRING
# [087] visibilitas_field
visibilitas_field ::= 'visibilitas' '=' publica
# [088] nomen_field
nomen_field ::= 'name' '=' IDENTIFIER
# [089] ut_field
ut_field ::= 'as' '=' IDENTIFIER
# [090] omnia_field
omnia_field ::= 'all' '=' IDENTIFIER
# [091] importa_sugar
importa_sugar ::= 'import' 'from' STRING publica? (named_import | wildcard_import | selective_import)?
# [092] publica
publica ::= 'public'
# [093] named_import
named_import ::= IDENTIFIER ('as' IDENTIFIER)?
# [094] wildcard_import
wildcard_import ::= '*' 'as' IDENTIFIER
# [095] selective_import
selective_import ::= 'const' import_value_binding (',' import_value_binding)*
# [096] import_value_binding
import_value_binding ::= IDENTIFIER ('as' IDENTIFIER)?
# [097] type_annotation
type_annotation ::= union_hole_type | concrete_type
# [098] concrete_type
concrete_type ::= intersection_type ('∪' intersection_type)*
# [099] union_hole_type
union_hole_type ::= ('ref' | 'mut' | 'own' | 'copy')? '∪'
# [100] intersection_type
intersection_type ::= owned_type ('∩' owned_type)*
# [101] owned_type
owned_type ::= ('ref' | 'mut' | 'own' | 'copy')? base_type
# [102] base_type
base_type ::= hole_type | function_type | width_type_sugar | ratio_type | failable_promissum_type | qualified_type type_arguments?
# [103] failable_promissum_type
failable_promissum_type ::= IDENTIFIER '<' type_annotation alternate_exit_clause '>'
# [104] ratio_type
ratio_type ::= 'record' '<' ('*' | labeled_type_argument (',' labeled_type_argument)*) '>'
# [105] hole_type
hole_type ::= '_'
# [106] qualified_type
qualified_type ::= type_head ('.' IDENTIFIER)*
# [107] type_head
type_head ::= IDENTIFIER | 'wrapping'
# [108] type_arguments
type_arguments ::= '<' type_argument (',' type_argument)* '>'
# [109] type_argument
type_argument ::= labeled_type_argument | type_annotation | NATURAL | '[' figura_list? ']'
# [110] labeled_type_argument
labeled_type_argument ::= IDENTIFIER ':' type_annotation
# [111] width_type_sugar
width_type_sugar ::= WIDTH_MARKER | LISTA_WIDTH_SUGAR | (TENSOR_WIDTH_SUGAR | SPARSA_WIDTH_SUGAR | VECTOR_WIDTH_SUGAR) shape_suffix? | MATRIX_WIDTH_SUGAR shape_suffix
# [112] shape_suffix
shape_suffix ::= '[' figura_list? ']'
# [113] figura
figura ::= spelled_lift | figura_product (('+' | '-') NATURAL)*
# [114] spelled_lift
spelled_lift ::= 'size' lift_extent
# [115] lift_extent
lift_extent ::= NATURAL | '-' NATURAL | '(' figura ')' | IDENTIFIER
# [116] figura_product
figura_product ::= figura_primary ('/' NATURAL)*
# [117] figura_primary
figura_primary ::= '_' | NATURAL | IDENTIFIER | '[' figura_list? ']' | '(' figura ')'
# [118] figura_list
figura_list ::= figura (',' figura)*
# [119] function_type
function_type ::= '(' type_list? ')' '→' type_annotation alternate_exit_clause?
# [120] type_list
type_list ::= type_annotation (',' type_annotation)*
# [121] si_stmt
si_stmt ::= 'if' si_tail
# [122] si_tail
si_tail ::= expression arm ('elif' si_tail | secus_clause)?
# [123] secus_clause
secus_clause ::= 'else' else_arm
# [124] arm
arm ::= (block_stmt | ergo_joint statement) cape_clause?
# [125] else_arm
else_arm ::= (block_stmt | ergo_joint statement) cape_clause?
# [126] dum_stmt
dum_stmt ::= 'while' expression (block_stmt | ergo_joint statement) cape_clause?
# [127] itera_stmt
itera_stmt ::= 'for' ('from' expression (',' expression)* | 'ref' expression | 'range' expression (',' expression)*) apud_clause? filum_clause? ('const' | 'var') itera_binding (block_stmt | ergo_joint statement) cape_clause?
# [128] itera_binding
itera_binding ::= array_pattern | object_pattern | IDENTIFIER (',' IDENTIFIER)*
# [129] apud_clause
apud_clause ::= 'at' '[' IDENTIFIER (',' IDENTIFIER)* ']'
# [130] elige_stmt
elige_stmt ::= 'switch' expression '{' casu_elige_clause* ceterum_clause? '}' cape_clause?
# [131] casu_elige_clause
casu_elige_clause ::= 'case' expression (block_stmt | ergo_joint statement)
# [132] ceterum_clause
ceterum_clause ::= 'default' (block_stmt | ergo_joint statement)
# [133] discerne_stmt
discerne_stmt ::= 'match' 'all'? discriminants '{' casu_variant_clause* ceterum_clause? '}'
# [134] discriminants
discriminants ::= subject_path ('and' subject_path)*
# [135] subject_path
subject_path ::= IDENTIFIER ('.' IDENTIFIER)*
# [136] casu_variant_clause
casu_variant_clause ::= 'case' patterns (block_stmt | ergo_joint statement)
# [137] patterns
patterns ::= pattern ('and' pattern)*
# [138] pattern
pattern ::= pattern_atom ('or' pattern_atom)*
# [139] pattern_atom
pattern_atom ::= '_' | negated_number | literal | type_pattern | (IDENTIFIER ut_pattern?)
# [140] negated_number
negated_number ::= '-' NUMBER
# [141] type_pattern
type_pattern ::= IDENTIFIER type_arguments? ut_pattern?
# [142] ut_pattern
ut_pattern ::= ('as' IDENTIFIER) | (('const' | 'var') pattern_binding (',' pattern_binding)*)
# [143] pattern_binding
pattern_binding ::= IDENTIFIER ('as' IDENTIFIER)?
# [144] custodi_stmt
custodi_stmt ::= 'guard' '{' si_guard_clause+ '}'
# [145] si_guard_clause
si_guard_clause ::= 'if' expression (block_stmt | ergo_joint statement)
# [146] ex_stmt
ex_stmt ::= 'from' expression ('const' | 'var') extract_fields
# [147] extract_fields
extract_fields ::= extract_field (',' extract_field)* (',' ceteri_field)? | ceteri_field
# [148] extract_field
extract_field ::= IDENTIFIER ('as' IDENTIFIER)?
# [149] ceteri_field
ceteri_field ::= 'rest' IDENTIFIER
# [150] redde_stmt
redde_stmt ::= 'return' expression?
# [151] reddet_stmt
reddet_stmt ::= 'return_await' expression
# [152] tacebit_stmt
tacebit_stmt ::= 'await' expression
# [153] cede_stmt
cede_stmt ::= 'yield' expression
# [154] rumpe_stmt
rumpe_stmt ::= 'break'
# [155] perge_stmt
perge_stmt ::= 'continue'
# [156] tacet_stmt
tacet_stmt ::= 'pass'
# [157] iace_stmt
iace_stmt ::= iace_expr | iace_guarded_expr
# [158] iace_expr
iace_expr ::= ('throw' | 'panic') expression
# [159] iace_guarded_expr
iace_guarded_expr ::= ('throw' | 'panic') expression NO_NEWLINE 'if' expression
# [160] cape_clause
cape_clause ::= 'catch' IDENTIFIER block_stmt
# [161] adfirma_stmt
adfirma_stmt ::= 'assert' expression ('panic' expression)?
# [162] requirit_stmt
requirit_stmt ::= 'require' expression 'throw' expression
# [163] reice_stmt
reice_stmt ::= 'reject' expression 'throw' expression
# [164] expression
expression ::= assignment
# [165] transfer
transfer ::= ternary ('⇇' ternary)?
# [166] value_marker
value_marker ::= 'own' | 'copy'
# [167] assignment
assignment ::= transfer ('←' 'copy'? assignment | '↤' assignment via_clause? inline_default?)?
# [168] inc_dec_stmt
inc_dec_stmt ::= place ('↑' | '↓')
# [169] place
place ::= call_expr
# [170] ternary
ternary ::= aut_expr ('✓' expression '✗' aut_expr)?
# [171] aut_expr
aut_expr ::= et_expr (('or') et_expr)*
# [172] et_expr
et_expr ::= equality (('and') equality)*
# [173] equality
equality ::= comparison equality_tail*
# [174] equality_tail
equality_tail ::= ('≡' | '≢' | '≅' | '≇' | '≈' | '≉') comparison | ('is' | 'not' 'is') type_annotation
# [175] comparison
comparison ::= format_expr (('≺' | '≻' | '≤' | '≥' | '∈' | '∉') format_expr)*
# [176] format_expr
format_expr ::= bitwise_or_expr ('¶' STRING)?
# [177] bitwise_or_expr
bitwise_or_expr ::= bitwise_xor_expr ('∨' bitwise_xor_expr)*
# [178] bitwise_xor_expr
bitwise_xor_expr ::= bitwise_and_expr ('⊻' bitwise_and_expr)*
# [179] bitwise_and_expr
bitwise_and_expr ::= shift_expr ('∧' shift_expr)*
# [180] shift_expr
shift_expr ::= range_expr (('⇐' | '⇒') range_expr)*
# [181] range_expr
range_expr ::= additive_expr range_tail?
# [182] range_tail
range_tail ::= ('‥' | '…' | 'before' | 'until') additive_expr ('step' additive_expr)?
# [183] additive_expr
additive_expr ::= multiplicative_expr (('+' | '-' | '⤒' | '⤓') multiplicative_expr)*
# [184] multiplicative_expr
multiplicative_expr ::= vel_expr (('*' | '/' | '÷' | '%' | '·' | '×' | '⊗' | '⊙' | '⊘') vel_expr)*
# [185] vel_expr
vel_expr ::= unary_expr ('coalesce' vel_rhs)*
# [186] vel_rhs
vel_rhs ::= unary_expr vel_range_tail?
# [187] vel_range_tail
vel_range_tail ::= ('‥' | '…' | 'before' | 'until') unary_expr ('step' unary_expr)?
# [188] unary_expr
unary_expr ::= ('-' | '¬' | 'not') unary_expr | rounding_expr | finge_expr | cast_expr
# [189] rounding_expr
rounding_expr ::= '⌊' expression ('⌋' | '⌉') | '⌈' expression '⌉'
# [190] gradient_expr
gradient_expr ::= call_expr ('∇' gradient_selection?)?
# [191] gradient_selection
gradient_selection ::= '[' gradient_place (',' gradient_place)* ']'
# [192] gradient_place
gradient_place ::= expression
# [193] cast_expr
cast_expr ::= gradient_expr ('∷' type_annotation | conversio_expr)* inline_default?
# [194] conversio_expr
conversio_expr ::= '↦' (type_annotation | interval_target) via_clause? inline_default?
# [195] interval_target
interval_target ::= range_expr
# [196] via_clause
via_clause ::= 'via' IDENTIFIER
# [197] inline_default
inline_default ::= '⊥' unary_expr
# [198] call_expr
call_expr ::= primary (call_suffix | member_suffix | transpose_suffix | optional_suffix | non_null_suffix)*
# [199] call_suffix
call_suffix ::= call_type_args? '(' argument_list ')'
# [200] member_suffix
member_suffix ::= '.' IDENTIFIER | '[' expression ']'
# [201] transpose_suffix
transpose_suffix ::= 'ᵀ'
# [202] optional_suffix
optional_suffix ::= '?.' IDENTIFIER | '?[' expression ']' | '?(' argument_list ')'
# [203] non_null_suffix
non_null_suffix ::= '!.' IDENTIFIER | '![' expression ']' | '!(' argument_list ')'
# [204] argument_list
argument_list ::= (argument (',' argument)*)?
# [205] argument
argument ::= template_argument | (call_marker | 'axis')? 'spread'? expression
# [206] call_marker
call_marker ::= 'ref' | 'mut' | 'own' | 'copy'
# [207] template_argument
template_argument ::= 'spread'? IDENTIFIER ':' expression
# [208] literal
literal ::= NUMBER | STRING | ASCII_STRING | BACKTICK_STRING | OCTETI_STRING | 'true' | 'false' | 'null' | '∞' | 'nan'
# [209] regex_literal
regex_literal ::= REGEX_TYPE_WORD REGEX_BODY | '_' REGEX_BODY
# [210] primary
primary ::= IDENTIFIER | literal | regex_literal | 'self' | array_literal | json_literal | typed_constructor | iuncta_expr | ad_expr | clausura_expr | praefixum_expr | scriptum_expr | lege_expr | first_match_expr | reducta_expr | sort_expr | capta_expr | '(' expression ')'
# [211] ad_expr
ad_expr ::= 'call' ASCII_STRING ad_opener?
# [212] ad_opener
ad_opener ::= '(' expression ')'
# [213] array_literal
array_literal ::= '[' array_element_list? ']'
# [214] array_element_list
array_element_list ::= array_element (',' array_element)*
# [215] array_element
array_element ::= argument | '_'
# [216] iuncta_expr
iuncta_expr ::= 'tuple' type_arguments '[' argument_list? ']'
# [217] json_literal
json_literal ::= '{' (json_member (',' json_member)*)? '}'
# [218] json_member
json_member ::= STRING ':' json_value
# [219] typed_constructor
typed_constructor ::= type_annotation '{' field_list? '}' construction_source? | hole_type '{' field_list? '}' construction_source? | type_annotation json_literal | hole_type json_literal | '{' field_list '}' construction_source? | type_annotation '[' array_element_list? ']'
# [220] field_list
field_list ::= field_init (',' field_init)*
# [221] field_init
field_init ::= (field_key '=' expression) | IDENTIFIER
# [222] field_key
field_key ::= IDENTIFIER | STRING | '[' expression ']'
# [223] construction_source
construction_source ::= 'from' call_expr
# [224] json_value
json_value ::= json_object | json_array | json_string | json_number | 'true' | 'false' | 'null'
# [225] json_object
json_object ::= '{' (json_member (',' json_member)*)? '}'
# [226] json_array
json_array ::= '[' (json_value (',' json_value)*)? ']'
# [227] json_string
json_string ::= STRING
# [228] json_number
json_number ::= NUMBER
# [229] finge_expr
finge_expr ::= 'variant' qualified_ident ('{' field_list? '}')? ('∷' type_annotation)?
# [230] qualified_ident
qualified_ident ::= IDENTIFIER ('.' IDENTIFIER)*
# [231] praefixum_expr
praefixum_expr ::= 'comptime' block_stmt
# [232] scriptum_expr
scriptum_expr ::= 'format' '(' STRING (',' expression)* ')'
# [233] lege_expr
lege_expr ::= 'read' 'line'?
# [234] first_match_expr
first_match_expr ::= 'primus_quem' '(' expression apud_clause? ',' 'ubi' IDENTIFIER block_stmt ')'
# [235] reducta_expr
reducta_expr ::= 'reduce' 'via' reducta_op 'from' expression apud_clause? reducta_group? (filum_clause? reducta_body | reducta_identity)?
# [236] reducta_op
reducta_op ::= 'sum' | 'product' | 'max' | 'min' | 'argmax' | 'argmin' | 'all' | 'any' | 'count'
# [237] reducta_group
reducta_group ::= 'per' expression
# [238] reducta_body
reducta_body ::= ('const' | 'var') IDENTIFIER block_stmt
# [239] reducta_identity
reducta_identity ::= 'coalesce' expression
# [240] sort_expr
sort_expr ::= 'sort' 'via' sort_direction ('from' | 'ref') expression sort_body?
# [241] sort_direction
sort_direction ::= 'asc' | 'desc'
# [242] sort_body
sort_body ::= ('const' | 'var') IDENTIFIER block_stmt
# [243] filum_clause
filum_clause ::= 'thread' IDENTIFIER
# [244] capta_expr
capta_expr ::= 'trap' block_stmt
# [245] object_pattern
object_pattern ::= '{' pattern_property (',' pattern_property)* '}'
# [246] pattern_property
pattern_property ::= 'rest'? IDENTIFIER ('as' IDENTIFIER)?
# [247] array_pattern
array_pattern ::= '[' array_pattern_element (',' array_pattern_element)* ']'
# [248] array_pattern_element
array_pattern_element ::= '_' | 'rest'? IDENTIFIER
# [249] nota_stmt
nota_stmt ::= ('print' | 'debug' | 'warn' | 'write') expression (',' expression)*
# [250] entry_header
entry_header ::= ('args' IDENTIFIER)? ('exit' expression)?
# [251] incipit_stmt
incipit_stmt ::= 'main' entry_header block_stmt
# [252] incipiet_stmt
incipiet_stmt ::= 'async_main' entry_header block_stmt
# [253] probandum_decl
probandum_decl ::= 'describe' STRING proba_modifier* '{' probandum_body '}'
# [254] probandum_body
probandum_body ::= (praepara_block | probandum_decl | proba_stmt)*
# [255] proba_stmt
proba_stmt ::= 'test' STRING proba_modifier* block_stmt
# [256] proba_modifier
proba_modifier ::= 'expect_failure' | 'skip' STRING | 'todo' STRING | 'only' | 'tag' STRING | 'timeout' NATURAL | 'bench' | 'repeat' NATURAL | 'flaky' NATURAL | 'only_in' STRING
# [257] praepara_block
praepara_block ::= ('setup' | 'async_setup' | 'teardown' | 'async_teardown') 'all'? block_stmt
# [258] fac_stmt
fac_stmt ::= 'do' block_stmt cape_clause? ('while' expression)?
# [259] IDENTIFIER
IDENTIFIER ::=
# [260] NUMBER
NUMBER ::=
# [261] NATURAL
NATURAL ::=
# [262] STRING
STRING ::=
# [263] ASCII_STRING
ASCII_STRING ::=
# [264] BACKTICK_STRING
BACKTICK_STRING ::=
# [265] OCTETI_STRING
OCTETI_STRING ::=
# [266] REGEX_TYPE_WORD
REGEX_TYPE_WORD ::=
# [267] REGEX_BODY
REGEX_BODY ::=
# [268] NEWLINE
NEWLINE ::=
# [269] WIDTH_MARKER
WIDTH_MARKER ::=
# [270] LISTA_WIDTH_SUGAR
LISTA_WIDTH_SUGAR ::=
# [271] TENSOR_WIDTH_SUGAR
TENSOR_WIDTH_SUGAR ::=
# [272] SPARSA_WIDTH_SUGAR
SPARSA_WIDTH_SUGAR ::=
# [273] VECTOR_WIDTH_SUGAR
VECTOR_WIDTH_SUGAR ::=
# [274] MATRIX_WIDTH_SUGAR
MATRIX_WIDTH_SUGAR ::=
# [275] FRONTMATTER_DELIMITER
FRONTMATTER_DELIMITER ::=
# [276] TOML_LINES
TOML_LINES ::=
# [277] ANNOTATION_NAME
ANNOTATION_NAME ::=
# [278] ANNOTATION_FIELD_NAME
ANNOTATION_FIELD_NAME ::=
# [279] NON_NEWLINE_TOKEN
NON_NEWLINE_TOKEN ::=
# [280] NO_NEWLINE
NO_NEWLINE ::=
```

Fetch list: https://faberlang.dev/agents/index.md
