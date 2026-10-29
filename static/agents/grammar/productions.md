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
binding_decl ::= fixum_decl | sit_decl | ref_decl | array_destruct | object_destruct | figendum_decl
# [010] expr_stmt
expr_stmt ::= expression
# [011] block_stmt
block_stmt ::= '{' statement* '}'
# [012] const_init
const_init ::= insere_expr | expression
# [013] insere_expr
insere_expr ::= 'embed' STRING
# [014] fixum_decl
fixum_decl ::= ('const' type_annotation IDENTIFIER '=' const_init) | ('mut' type_annotation IDENTIFIER (('←' value_marker? expression) | ('↤' assignment inline_default?) | ('↢' expression))?)
# [015] figendum_decl
figendum_decl ::= ('await_const' | 'await_var') type_annotation IDENTIFIER '←' expression
# [016] sit_decl
sit_decl ::= 'let' type_annotation IDENTIFIER (('←' value_marker? expression) | ('↤' assignment inline_default?) | ('↢' expression))?
# [017] ref_decl
ref_decl ::= 'ref' concrete_type IDENTIFIER '←' expression
# [018] array_destruct
array_destruct ::= ('let' | 'mut') array_pattern '←' expression
# [019] object_destruct
object_destruct ::= ('let' | 'mut') object_pattern '←' expression
# [020] functio_decl
functio_decl ::= 'fn' IDENTIFIER generic_params? '(' param_list ')' func_modifier* callable_posture? return_clause? alternate_exit_clause? block_stmt
# [021] param_list
param_list ::= (parameter (',' parameter)*)?
# [022] generic_params
generic_params ::= '<' (type_param_list (',' size_param_list)? | size_param_list) '>'
# [023] type_param_list
type_param_list ::= generic_param (',' generic_param)*
# [024] size_param_list
size_param_list ::= size_param (',' size_param)*
# [025] generic_param
generic_param ::= IDENTIFIER generic_bound? generic_type_default?
# [026] size_param
size_param ::= 'size' IDENTIFIER generic_size_default?
# [027] generic_bound
generic_bound ::= 'implements' contract_ref ('∩' contract_ref)*
# [028] contract_ref
contract_ref ::= IDENTIFIER ('<' type_annotation (',' type_annotation)* '>')?
# [029] generic_type_default
generic_type_default ::= '=' type_annotation
# [030] generic_size_default
generic_size_default ::= '=' NATURAL
# [031] call_type_args
call_type_args ::= '<' call_type_arg (',' call_type_arg)* '>'
# [032] call_type_arg
call_type_arg ::= type_annotation | call_size_arg
# [033] call_size_arg
call_size_arg ::= NATURAL dimension_tail? | IDENTIFIER dimension_tail | spelled_lift | '[' figura_list? ']'
# [034] dimension_tail
dimension_tail ::= ('/' NATURAL)+ (('+' | '-') NATURAL)* | (('+' | '-') NATURAL)+
# [035] parameter
parameter ::= 'rest'? 'axis'? type_annotation IDENTIFIER 'optional'? ('as' IDENTIFIER)? ('coalesce' expression)?
# [036] func_modifier
func_modifier ::= 'args' IDENTIFIER | 'errors' IDENTIFIER | 'exit' (IDENTIFIER | NATURAL) | 'readonly' | 'throws' | 'options' IDENTIFIER
# [037] callable_posture
callable_posture ::= 'async' | 'generator' | 'async_generator'
# [038] return_clause
return_clause ::= '→' type_annotation
# [039] alternate_exit_clause
alternate_exit_clause ::= '⇥' type_annotation
# [040] ergo_joint
ergo_joint ::= 'then'
# [041] clausura_joint
clausura_joint ::= '∴'
# [042] clausura_expr
clausura_expr ::= compact_clausura_expr | clausura_legacy_expr
# [043] compact_clausura_expr
compact_clausura_expr ::= clausura_signature clausura_joint (expression | fac_block)
# [044] clausura_signature
clausura_signature ::= (clausura_param | '(' clausura_params? ')') return_clause? alternate_exit_clause?
# [045] fac_block
fac_block ::= 'do' fac_modifier? block_stmt cape_clause?
# [046] clausura_legacy_expr
clausura_legacy_expr ::= 'lambda' clausura_params? ('→' type_annotation)? (':' expression | block_stmt)
# [047] clausura_params
clausura_params ::= clausura_param (',' clausura_param)*
# [048] clausura_param
clausura_param ::= type_annotation IDENTIFIER
# [049] genus_decl
genus_decl ::= 'class' IDENTIFIER generic_params? ('implements' contract_ref ((',' | '∩') contract_ref)*)? '{' genus_member* '}'
# [050] genus_member
genus_member ::= annotation* (genus_field_decl | functio_method_decl) | nondum_method_decl
# [051] nondum_method_decl
nondum_method_decl ::= annotation* nondum_annotation annotation* 'fn' IDENTIFIER generic_params? '(' param_list ')' func_modifier* callable_posture? return_clause? alternate_exit_clause?
# [052] genus_field_decl
genus_field_decl ::= (('let' | 'mut') type_annotation IDENTIFIER 'optional'? ('=' const_init)?) | genus_const_decl
# [053] genus_const_decl
genus_const_decl ::= 'const' type_annotation IDENTIFIER '=' const_init
# [054] field_decl
field_decl ::= (('let' | 'mut')? type_annotation IDENTIFIER 'optional'? ('=' const_init)?) | genus_const_decl
# [055] functio_method_decl
functio_method_decl ::= 'fn' IDENTIFIER generic_params? '(' param_list ')' func_modifier* callable_posture? return_clause? alternate_exit_clause? block_stmt
# [056] annotation
annotation ::= nucleum_annotation | radix_annotation | braced_annotation | annotation_sugar
# [057] annotation_name
annotation_name ::= ANNOTATION_NAME
# [058] braced_annotation
braced_annotation ::= '@' annotation_name '{' annotation_field_list? '}'
# [059] annotation_field_list
annotation_field_list ::= annotation_field (',' annotation_field)*
# [060] annotation_field
annotation_field ::= ANNOTATION_FIELD_NAME '=' (expression | concrete_type)
# [061] annotation_sugar
annotation_sugar ::= '@' annotation_name NON_NEWLINE_TOKEN* NEWLINE
# [062] nucleum_annotation
nucleum_annotation ::= nucleum_sugar | nucleum_braced
# [063] nucleum_sugar
nucleum_sugar ::= '@' 'kernel' nucleum_modifier? NEWLINE
# [064] nucleum_braced
nucleum_braced ::= '@' 'kernel' '{' nucleum_field_list? '}'
# [065] nucleum_modifier
nucleum_modifier ::= 'fragment' | nucleum_tier
# [066] nucleum_tier
nucleum_tier ::= 'relaxed' | 'unsafe'
# [067] nucleum_field_list
nucleum_field_list ::= nucleum_field (',' nucleum_field)*
# [068] nucleum_field
nucleum_field ::= 'fragment' '=' ('true' | 'false')
# [069] radix_annotation
radix_annotation ::= '@' 'radix' radix_directive NEWLINE
# [070] radix_directive
radix_directive ::= 'lane' STRING | 'backward' STRING | 'contract' STRING | 'type' IDENTIFIER 'mut' concrete_type+
# [071] ad_annotation
ad_annotation ::= '@' 'call' ASCII_STRING NEWLINE
# [072] nondum_annotation
nondum_annotation ::= '@' 'unstable' NON_NEWLINE_TOKEN* NEWLINE | '@' 'unstable' '{' annotation_field_list? '}'
# [073] implendum_decl
implendum_decl ::= 'interface' IDENTIFIER generic_params? '{' implendum_method_decl* '}'
# [074] implendum_method_decl
implendum_method_decl ::= annotation* 'fn' IDENTIFIER '(' param_list ')' func_modifier* callable_posture? return_clause? alternate_exit_clause?
# [075] typus_decl
typus_decl ::= 'type' IDENTIFIER generic_params? '=' type_annotation
# [076] ordo_decl
ordo_decl ::= 'enum' IDENTIFIER '{' enum_member (',' enum_member)* '}'
# [077] enum_member
enum_member ::= IDENTIFIER ('=' ('-'? NUMBER | STRING))?
# [078] discretio_decl
discretio_decl ::= 'union' IDENTIFIER generic_params? '{' union_fields? variant (',' variant)* '}'
# [079] union_fields
union_fields ::= annotation+ field_decl union_member*
# [080] union_member
union_member ::= annotation* field_decl
# [081] variant
variant ::= IDENTIFIER ('{' variant_fields '}')?
# [082] variant_fields
variant_fields ::= (type_annotation IDENTIFIER)*
# [083] schema_decl
schema_decl ::= 'schema' IDENTIFIER '{' (schema_column (NEWLINE schema_column)*)? '}'
# [084] schema_column
schema_column ::= 'column' type_annotation IDENTIFIER (':' IDENTIFIER)?
# [085] importa_decl
importa_decl ::= importa_record | importa_sugar
# [086] importa_record
importa_record ::= 'import' '{' import_field_list '}'
# [087] import_field_list
import_field_list ::= import_field (',' import_field)*
# [088] import_field
import_field ::= ex_field | visibilitas_field | nomen_field | ut_field | omnia_field
# [089] ex_field
ex_field ::= 'from' '=' STRING
# [090] visibilitas_field
visibilitas_field ::= 'visibility' '=' publica
# [091] nomen_field
nomen_field ::= 'name' '=' IDENTIFIER
# [092] ut_field
ut_field ::= 'as' '=' IDENTIFIER
# [093] omnia_field
omnia_field ::= 'all' '=' IDENTIFIER
# [094] importa_sugar
importa_sugar ::= 'import' ('from' | import_target) STRING publica? (named_import | wildcard_import | selective_import)?
# [095] import_target
import_target ::= IDENTIFIER
# [096] publica
publica ::= 'public'
# [097] named_import
named_import ::= IDENTIFIER ('as' IDENTIFIER)?
# [098] wildcard_import
wildcard_import ::= '*' 'as' IDENTIFIER
# [099] selective_import
selective_import ::= 'const' import_value_binding (',' import_value_binding)*
# [100] import_value_binding
import_value_binding ::= IDENTIFIER ('as' IDENTIFIER)?
# [101] type_annotation
type_annotation ::= union_hole_type | concrete_type
# [102] concrete_type
concrete_type ::= intersection_type ('∪' intersection_type)*
# [103] union_hole_type
union_hole_type ::= ('ref' | 'mut' | 'own' | 'copy')? '∪'
# [104] intersection_type
intersection_type ::= owned_type ('∩' owned_type)*
# [105] owned_type
owned_type ::= ('ref' | 'mut' | 'own' | 'copy')? base_type
# [106] base_type
base_type ::= hole_type | function_type | width_type_sugar | ratio_type | failable_promissum_type | qualified_type type_arguments?
# [107] failable_promissum_type
failable_promissum_type ::= IDENTIFIER '<' type_annotation alternate_exit_clause '>'
# [108] ratio_type
ratio_type ::= 'record' '<' ('*' | labeled_type_argument (',' labeled_type_argument)*) '>'
# [109] hole_type
hole_type ::= '_'
# [110] qualified_type
qualified_type ::= type_head ('.' IDENTIFIER)*
# [111] type_head
type_head ::= IDENTIFIER | 'wrapping'
# [112] type_arguments
type_arguments ::= '<' type_argument (',' type_argument)* '>'
# [113] type_argument
type_argument ::= labeled_type_argument | range_argument | sized_range_argument | spelled_lift | type_annotation | NATURAL | '[' figura_list? ']'
# [114] labeled_type_argument
labeled_type_argument ::= IDENTIFIER ':' type_annotation
# [115] range_argument
range_argument ::= range_bound range_glyph range_bound
# [116] sized_range_argument
sized_range_argument ::= 'size' range_argument
# [117] range_glyph
range_glyph ::= '‥' | '…'
# [118] range_bound
range_bound ::= '-'? NATURAL | '-'? '∞' | 'size'? IDENTIFIER
# [119] width_type_sugar
width_type_sugar ::= WIDTH_MARKER | LISTA_WIDTH_SUGAR | (TENSOR_WIDTH_SUGAR | SPARSA_WIDTH_SUGAR | VECTOR_WIDTH_SUGAR) shape_suffix? | MATRIX_WIDTH_SUGAR shape_suffix
# [120] shape_suffix
shape_suffix ::= '[' figura_list? ']'
# [121] figura
figura ::= spelled_lift | figura_product (('+' | '-') NATURAL)*
# [122] spelled_lift
spelled_lift ::= 'size' lift_extent
# [123] lift_extent
lift_extent ::= NATURAL | '-' NATURAL | '(' figura ')' | IDENTIFIER | '[' figura_list? ']'
# [124] figura_product
figura_product ::= figura_primary ('/' NATURAL)*
# [125] figura_primary
figura_primary ::= '_' | NATURAL | IDENTIFIER | '[' figura_list? ']' | '(' figura ')'
# [126] figura_list
figura_list ::= figura (',' figura)*
# [127] function_type
function_type ::= '(' type_list? ')' '→' type_annotation alternate_exit_clause?
# [128] type_list
type_list ::= type_annotation (',' type_annotation)*
# [129] si_stmt
si_stmt ::= 'if' si_tail
# [130] si_tail
si_tail ::= expression arm ('elif' si_tail | secus_clause)?
# [131] secus_clause
secus_clause ::= 'else' else_arm
# [132] arm
arm ::= (block_stmt | ergo_joint statement) cape_clause?
# [133] else_arm
else_arm ::= (block_stmt | ergo_joint statement) cape_clause?
# [134] dum_stmt
dum_stmt ::= 'while' expression (block_stmt | ergo_joint statement) cape_clause?
# [135] itera_stmt
itera_stmt ::= 'for' ('from' expression (',' expression)* | 'ref' expression | 'range' expression (',' expression)*) apud_clause? filum_clause? ('let' | 'mut') itera_binding (block_stmt | ergo_joint statement) cape_clause?
# [136] itera_binding
itera_binding ::= array_pattern | object_pattern | IDENTIFIER (',' IDENTIFIER)*
# [137] apud_clause
apud_clause ::= 'at' '[' IDENTIFIER (',' IDENTIFIER)* ']'
# [138] elige_stmt
elige_stmt ::= 'switch' expression '{' casu_elige_clause* ceterum_clause? '}' cape_clause?
# [139] casu_elige_clause
casu_elige_clause ::= 'case' expression (block_stmt | ergo_joint statement)
# [140] ceterum_clause
ceterum_clause ::= 'default' (block_stmt | ergo_joint statement)
# [141] discerne_stmt
discerne_stmt ::= 'match' 'all'? discriminants '{' casu_variant_clause* ceterum_clause? '}'
# [142] discriminants
discriminants ::= subject_path ('and' subject_path)*
# [143] subject_path
subject_path ::= IDENTIFIER ('.' IDENTIFIER)*
# [144] casu_variant_clause
casu_variant_clause ::= 'case' patterns (block_stmt | ergo_joint statement)
# [145] patterns
patterns ::= pattern ('and' pattern)*
# [146] pattern
pattern ::= pattern_atom ('or' pattern_atom)*
# [147] pattern_atom
pattern_atom ::= '_' | negated_number | literal | type_pattern | (IDENTIFIER ut_pattern?)
# [148] negated_number
negated_number ::= '-' NUMBER
# [149] type_pattern
type_pattern ::= IDENTIFIER type_arguments? ut_pattern?
# [150] ut_pattern
ut_pattern ::= ('as' IDENTIFIER) | (('let' | 'mut') pattern_binding (',' pattern_binding)*)
# [151] pattern_binding
pattern_binding ::= IDENTIFIER ('as' IDENTIFIER)?
# [152] custodi_stmt
custodi_stmt ::= 'guard' '{' si_guard_clause+ '}'
# [153] si_guard_clause
si_guard_clause ::= 'if' expression (block_stmt | ergo_joint statement)
# [154] ex_stmt
ex_stmt ::= 'from' expression ('let' | 'mut') extract_fields
# [155] extract_fields
extract_fields ::= extract_field (',' extract_field)* (',' ceteri_field)? | ceteri_field
# [156] extract_field
extract_field ::= IDENTIFIER ('as' IDENTIFIER)?
# [157] ceteri_field
ceteri_field ::= 'rest' IDENTIFIER
# [158] redde_stmt
redde_stmt ::= 'return' ('thread' expression? | expression?)
# [159] reddet_stmt
reddet_stmt ::= 'return_await' expression
# [160] tacebit_stmt
tacebit_stmt ::= 'await' expression
# [161] cede_stmt
cede_stmt ::= 'yield' expression
# [162] rumpe_stmt
rumpe_stmt ::= 'break'
# [163] perge_stmt
perge_stmt ::= 'continue'
# [164] tacet_stmt
tacet_stmt ::= 'pass'
# [165] iace_stmt
iace_stmt ::= iace_expr | iace_guarded_expr
# [166] iace_expr
iace_expr ::= ('throw' | 'panic') expression
# [167] iace_guarded_expr
iace_guarded_expr ::= ('throw' | 'panic') expression NO_NEWLINE 'if' expression
# [168] cape_clause
cape_clause ::= 'catch' IDENTIFIER block_stmt
# [169] adfirma_stmt
adfirma_stmt ::= 'assert' expression ('panic' expression)?
# [170] requirit_stmt
requirit_stmt ::= 'require' expression 'throw' expression
# [171] reice_stmt
reice_stmt ::= 'reject' expression 'throw' expression
# [172] expression
expression ::= assignment
# [173] transfer
transfer ::= ternary ('⇇' ternary)?
# [174] sink_into
sink_into ::= transfer ('⇜' ternary)?
# [175] value_marker
value_marker ::= 'own' | 'copy'
# [176] assignment
assignment ::= sink_into ('←' 'copy'? assignment | '↤' assignment via_clause? inline_default?)?
# [177] inc_dec_stmt
inc_dec_stmt ::= place ('↑' | '↓')
# [178] place
place ::= call_expr
# [179] ternary
ternary ::= aut_expr ('✓' expression '✗' aut_expr)?
# [180] aut_expr
aut_expr ::= et_expr (('or') et_expr)*
# [181] et_expr
et_expr ::= equality (('and') equality)*
# [182] equality
equality ::= comparison equality_tail*
# [183] equality_tail
equality_tail ::= ('≡' | '≢' | '≅' | '≇' | '≈' | '≉') comparison | ('is' | 'not' 'is') type_annotation
# [184] comparison
comparison ::= format_expr (('≺' | '≻' | '≤' | '≥' | '∈' | '∉') format_expr)*
# [185] format_expr
format_expr ::= bitwise_or_expr ('¶' STRING)?
# [186] bitwise_or_expr
bitwise_or_expr ::= bitwise_xor_expr ('∨' bitwise_xor_expr)*
# [187] bitwise_xor_expr
bitwise_xor_expr ::= bitwise_and_expr ('⊻' bitwise_and_expr)*
# [188] bitwise_and_expr
bitwise_and_expr ::= shift_expr ('∧' shift_expr)*
# [189] shift_expr
shift_expr ::= range_expr (('⇐' | '⇒') range_expr)*
# [190] range_expr
range_expr ::= additive_expr range_tail?
# [191] range_tail
range_tail ::= ('‥' | '…' | 'before' | 'until') additive_expr ('step' additive_expr)?
# [192] additive_expr
additive_expr ::= multiplicative_expr (('+' | '-' | '⤒' | '⤓') multiplicative_expr)*
# [193] multiplicative_expr
multiplicative_expr ::= vel_expr (('*' | '/' | '÷' | '%' | '·' | '×' | '⊗' | '⊙' | '⊘') vel_expr)*
# [194] vel_expr
vel_expr ::= unary_expr ('coalesce' vel_rhs)*
# [195] vel_rhs
vel_rhs ::= unary_expr vel_range_tail?
# [196] vel_range_tail
vel_range_tail ::= ('‥' | '…' | 'before' | 'until') unary_expr ('step' unary_expr)?
# [197] unary_expr
unary_expr ::= ('-' | '¬' | 'not' | '√' | '∛' | '∜') unary_expr | rounding_expr | finge_expr | cast_expr
# [198] rounding_expr
rounding_expr ::= '⌊' expression ('⌋' | '⌉') | '⌈' expression '⌉'
# [199] gradient_expr
gradient_expr ::= call_expr ('∇' gradient_selection?)?
# [200] gradient_selection
gradient_selection ::= '[' gradient_place (',' gradient_place)* ']'
# [201] gradient_place
gradient_place ::= expression
# [202] cast_expr
cast_expr ::= gradient_expr ('∷' type_annotation | conversio_expr)* inline_default?
# [203] conversio_expr
conversio_expr ::= '↦' (type_annotation | interval_target) via_clause? inline_default?
# [204] interval_target
interval_target ::= range_expr
# [205] via_clause
via_clause ::= 'via' IDENTIFIER
# [206] inline_default
inline_default ::= '⊥' unary_expr
# [207] call_expr
call_expr ::= primary (call_suffix | member_suffix | transpose_suffix | optional_suffix | non_null_suffix)*
# [208] call_suffix
call_suffix ::= call_type_args? '(' argument_list ')'
# [209] member_suffix
member_suffix ::= '.' IDENTIFIER | '[' expression ']'
# [210] transpose_suffix
transpose_suffix ::= 'ᵀ'
# [211] optional_suffix
optional_suffix ::= '?.' IDENTIFIER | '?[' expression ']' | '?(' argument_list ')'
# [212] non_null_suffix
non_null_suffix ::= '!.' IDENTIFIER | '![' expression ']' | '!(' argument_list ')'
# [213] argument_list
argument_list ::= (argument (',' argument)*)?
# [214] argument
argument ::= template_argument | (call_marker | 'axis')? 'spread'? expression
# [215] call_marker
call_marker ::= 'ref' | 'mut' | 'own' | 'copy'
# [216] template_argument
template_argument ::= 'spread'? IDENTIFIER ':' expression
# [217] literal
literal ::= NUMBER | STRING | ASCII_STRING | BACKTICK_STRING | OCTETI_STRING | 'true' | 'false' | 'null' | '∞' | 'nan'
# [218] regex_literal
regex_literal ::= REGEX_TYPE_WORD REGEX_BODY | '_' REGEX_BODY
# [219] primary
primary ::= IDENTIFIER | literal | regex_literal | 'self' | array_literal | json_literal | typed_constructor | iuncta_expr | ad_expr | clausura_expr | praefixum_expr | scriptum_expr | lege_expr | reducta_expr | scan_expr | sort_expr | capta_expr | '(' expression ')'
# [220] ad_expr
ad_expr ::= 'call' ASCII_STRING ad_opener?
# [221] ad_opener
ad_opener ::= '(' expression ')'
# [222] array_literal
array_literal ::= '[' array_element_list? ']'
# [223] array_element_list
array_element_list ::= array_element (',' array_element)*
# [224] array_element
array_element ::= argument | '_'
# [225] iuncta_expr
iuncta_expr ::= 'tuple' type_arguments '[' argument_list? ']'
# [226] json_literal
json_literal ::= '{' (json_member (',' json_member)*)? '}'
# [227] json_member
json_member ::= STRING ':' json_value
# [228] typed_constructor
typed_constructor ::= type_annotation '{' field_list? '}' construction_source? | hole_type '{' field_list? '}' construction_source? | type_annotation json_literal | hole_type json_literal | '{' field_list '}' construction_source? | type_annotation '[' array_element_list? ']'
# [229] field_list
field_list ::= field_init (',' field_init)*
# [230] field_init
field_init ::= (field_key '=' expression) | IDENTIFIER
# [231] field_key
field_key ::= IDENTIFIER | STRING | '[' expression ']'
# [232] construction_source
construction_source ::= 'from' call_expr
# [233] json_value
json_value ::= json_object | json_array | json_string | json_number | 'true' | 'false' | 'null'
# [234] json_object
json_object ::= '{' (json_member (',' json_member)*)? '}'
# [235] json_array
json_array ::= '[' (json_value (',' json_value)*)? ']'
# [236] json_string
json_string ::= STRING
# [237] json_number
json_number ::= NUMBER
# [238] finge_expr
finge_expr ::= 'variant' qualified_ident ('{' field_list? '}')? ('∷' type_annotation)?
# [239] qualified_ident
qualified_ident ::= IDENTIFIER ('.' IDENTIFIER)*
# [240] praefixum_expr
praefixum_expr ::= 'comptime' block_stmt
# [241] scriptum_expr
scriptum_expr ::= 'format' '(' STRING (',' expression)* ')'
# [242] lege_expr
lege_expr ::= 'read' 'line'?
# [243] reducta_expr
reducta_expr ::= 'reduce' 'via' reducta_op 'from' expression apud_clause? reducta_group? (filum_clause? reducta_body)? reducta_identity?
# [244] reducta_op
reducta_op ::= 'sum' | 'product' | 'max' | 'min' | 'argmax' | 'argmin' | 'all' | 'any' | 'count' | 'first'
# [245] reducta_group
reducta_group ::= 'per' (group_key | '[' expression (',' expression)* ']')
# [246] group_key
group_key ::= unary_expr
# [247] reducta_body
reducta_body ::= ('let' | 'mut') IDENTIFIER block_stmt
# [248] reducta_identity
reducta_identity ::= 'coalesce' expression
# [249] scan_expr
scan_expr ::= 'scan' 'via' scan_op ('total' ('inclusive' | 'exclusive'))? 'from' expression apud_clause scan_group? scan_order_clause? filum_clause 'let' IDENTIFIER block_stmt
# [250] scan_op
scan_op ::= 'sum' | 'product' | 'max' | 'min' | 'all' | 'any' | 'count'
# [251] scan_group
scan_group ::= 'per' expression
# [252] scan_order_clause
scan_order_clause ::= 'order' ('asc' | 'desc')
# [253] sort_expr
sort_expr ::= 'sort' 'via' sort_direction ('from' | 'ref') expression sort_body?
# [254] sort_direction
sort_direction ::= 'asc' | 'desc'
# [255] sort_body
sort_body ::= ('let' | 'mut') IDENTIFIER block_stmt
# [256] filum_clause
filum_clause ::= 'thread' IDENTIFIER
# [257] capta_expr
capta_expr ::= 'trap' block_stmt
# [258] object_pattern
object_pattern ::= '{' pattern_property (',' pattern_property)* '}'
# [259] pattern_property
pattern_property ::= 'rest'? IDENTIFIER ('as' IDENTIFIER)?
# [260] array_pattern
array_pattern ::= '[' array_pattern_element (',' array_pattern_element)* ']'
# [261] array_pattern_element
array_pattern_element ::= '_' | 'rest'? IDENTIFIER
# [262] nota_stmt
nota_stmt ::= ('print' | 'debug' | 'warn' | 'write') expression (',' expression)*
# [263] entry_header
entry_header ::= ('args' IDENTIFIER)? ('exit' expression)?
# [264] incipit_stmt
incipit_stmt ::= 'main' entry_header block_stmt
# [265] incipiet_stmt
incipiet_stmt ::= 'async_main' entry_header block_stmt
# [266] probandum_decl
probandum_decl ::= 'describe' STRING proba_modifier* '{' probandum_body '}'
# [267] probandum_body
probandum_body ::= (praepara_block | probandum_decl | proba_stmt)*
# [268] proba_stmt
proba_stmt ::= 'test' STRING proba_modifier* block_stmt
# [269] proba_modifier
proba_modifier ::= 'expect_failure' | 'skip' STRING | 'todo' STRING | 'only' | 'tag' STRING | 'timeout' NATURAL | 'bench' | 'repeat' NATURAL | 'flaky' NATURAL | 'only_in' STRING
# [270] praepara_block
praepara_block ::= ('setup' | 'async_setup' | 'teardown' | 'async_teardown') 'all'? block_stmt
# [271] fac_stmt
fac_stmt ::= 'do' fac_modifier? block_stmt cape_clause? ('while' expression)?
# [272] fac_modifier
fac_modifier ::= 'all' | 'device'
# [273] IDENTIFIER
IDENTIFIER ::=
# [274] NUMBER
NUMBER ::=
# [275] NATURAL
NATURAL ::=
# [276] STRING
STRING ::=
# [277] ASCII_STRING
ASCII_STRING ::=
# [278] BACKTICK_STRING
BACKTICK_STRING ::=
# [279] OCTETI_STRING
OCTETI_STRING ::=
# [280] REGEX_TYPE_WORD
REGEX_TYPE_WORD ::=
# [281] REGEX_BODY
REGEX_BODY ::=
# [282] NEWLINE
NEWLINE ::=
# [283] WIDTH_MARKER
WIDTH_MARKER ::=
# [284] LISTA_WIDTH_SUGAR
LISTA_WIDTH_SUGAR ::=
# [285] TENSOR_WIDTH_SUGAR
TENSOR_WIDTH_SUGAR ::=
# [286] SPARSA_WIDTH_SUGAR
SPARSA_WIDTH_SUGAR ::=
# [287] VECTOR_WIDTH_SUGAR
VECTOR_WIDTH_SUGAR ::=
# [288] MATRIX_WIDTH_SUGAR
MATRIX_WIDTH_SUGAR ::=
# [289] FRONTMATTER_DELIMITER
FRONTMATTER_DELIMITER ::=
# [290] TOML_LINES
TOML_LINES ::=
# [291] ANNOTATION_NAME
ANNOTATION_NAME ::=
# [292] ANNOTATION_FIELD_NAME
ANNOTATION_FIELD_NAME ::=
# [293] NON_NEWLINE_TOKEN
NON_NEWLINE_TOKEN ::=
# [294] NO_NEWLINE
NO_NEWLINE ::=
```

Fetch list: https://faberlang.dev/agents/index.md
