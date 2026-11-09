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
fab_file ::= frontmatter program file_section* | toml_section? file_section* faber_section file_section* | program file_section* | faber_test_section file_section* | toml_section? file_section* faber_section file_section* faber_test_section file_section* | toml_section? file_section* faber_test_section file_section* faber_section file_section* | frontmatter faber_test_section file_section* | program file_section* faber_test_section file_section* | faber_test_section file_section* faber_section file_section*
# [002] frontmatter
frontmatter ::= FRONTMATTER_DELIMITER NEWLINE TOML_LINES FRONTMATTER_DELIMITER NEWLINE?
# [003] toml_section
toml_section ::= TOML_MARKER NEWLINE TOML_LINES
# [004] faber_section
faber_section ::= FABER_MARKER NEWLINE program
# [005] faber_test_section
faber_test_section ::= FABER_TEST_MARKER NEWLINE statement*
# [006] file_section
file_section ::= stream_section
# [007] stream_section
stream_section ::= STREAM_MARKER NEWLINE STREAM_LINES
# [008] program
program ::= regio_decl? statement*
# [009] regio_decl
regio_decl ::= 'module' IDENTIFIER
# [010] statement
statement ::= annotation* statement_core | kernel_decl | ad_handler_decl | nondum_functio_decl
# [011] ad_handler_decl
ad_handler_decl ::= annotation* ad_annotation annotation* functio_decl
# [012] nondum_functio_decl
nondum_functio_decl ::= annotation* nondum_annotation annotation* 'fn' IDENTIFIER generic_params? '(' param_list ')' func_modifier* callable_posture? return_clause? alternate_exit_clause?
# [013] statement_core
statement_core ::= importa_decl | binding_decl | functio_decl | genus_decl | implendum_decl | typus_decl | ordo_decl | discretio_decl | schema_decl | si_stmt | dum_stmt | itera_stmt | elige_stmt | discerne_stmt | custodi_stmt | fac_stmt | redde_stmt | reddet_stmt | tacebit_stmt | cede_stmt | rumpe_stmt | perge_stmt | tacet_stmt | iace_stmt | adfirma_stmt | requirit_stmt | reice_stmt | nota_stmt | incipit_stmt | incipiet_stmt | ex_stmt | probandum_decl | proba_stmt | block_stmt | inc_dec_stmt | expr_stmt
# [014] binding_decl
binding_decl ::= fixum_decl | sit_decl | ref_decl | array_destruct | object_destruct | figendum_decl
# [015] expr_stmt
expr_stmt ::= expression
# [016] block_stmt
block_stmt ::= '{' statement* '}'
# [017] const_init
const_init ::= insere_expr | expression
# [018] insere_expr
insere_expr ::= 'embed' STRING
# [019] fixum_decl
fixum_decl ::= ('const' 'size' IDENTIFIER '=' NATURAL) | ('const' type_annotation IDENTIFIER '=' const_init) | ('mut' type_annotation IDENTIFIER (('←' value_marker? expression) | ('↤' assignment inline_default?) | ('↢' expression))?)
# [020] figendum_decl
figendum_decl ::= ('await_const' | 'await_var') type_annotation IDENTIFIER '←' expression
# [021] sit_decl
sit_decl ::= ('let' 'size' IDENTIFIER '←' expression) | ('let' type_annotation IDENTIFIER (('←' value_marker? expression) | ('↤' assignment inline_default?) | ('↢' expression))?)
# [022] ref_decl
ref_decl ::= 'ref' concrete_type IDENTIFIER '←' expression
# [023] array_destruct
array_destruct ::= ('let' | 'mut') array_pattern '←' expression
# [024] object_destruct
object_destruct ::= ('let' | 'mut') object_pattern '←' expression
# [025] functio_decl
functio_decl ::= 'fn' IDENTIFIER generic_params? '(' param_list ')' func_modifier* callable_posture? return_clause? alternate_exit_clause? block_stmt
# [026] kernel_decl
kernel_decl ::= annotation* 'kernel' IDENTIFIER generic_params? '(' param_list ')' func_modifier* kernel_mode? return_clause? alternate_exit_clause? block_stmt
# [027] kernel_mode
kernel_mode ::= 'relaxed' | 'unsafe' | 'fragment'
# [028] param_list
param_list ::= (parameter (',' parameter)*)?
# [029] generic_params
generic_params ::= '<' (type_param_list (',' size_param_list)? | size_param_list) '>'
# [030] type_param_list
type_param_list ::= generic_param (',' generic_param)*
# [031] size_param_list
size_param_list ::= size_param (',' size_param)*
# [032] generic_param
generic_param ::= IDENTIFIER generic_bound? generic_type_default?
# [033] size_param
size_param ::= 'size' IDENTIFIER generic_size_default?
# [034] generic_bound
generic_bound ::= 'implements' contract_ref ('∩' contract_ref)*
# [035] contract_ref
contract_ref ::= IDENTIFIER ('<' type_annotation (',' type_annotation)* '>')?
# [036] generic_type_default
generic_type_default ::= '=' type_annotation
# [037] generic_size_default
generic_size_default ::= '=' NATURAL
# [038] call_type_args
call_type_args ::= '<' call_type_arg (',' call_type_arg)* '>'
# [039] call_type_arg
call_type_arg ::= type_annotation | call_size_arg
# [040] call_size_arg
call_size_arg ::= NATURAL dimension_tail? | IDENTIFIER dimension_tail | spelled_lift | '[' figura_list? ']'
# [041] dimension_tail
dimension_tail ::= ('/' NATURAL)+ (('+' | '-') NATURAL)* | (('+' | '-') NATURAL)+
# [042] parameter
parameter ::= 'rest'? 'axis'? type_annotation IDENTIFIER 'optional'? ('as' IDENTIFIER)? ('coalesce' expression)?
# [043] func_modifier
func_modifier ::= 'args' IDENTIFIER | 'errors' IDENTIFIER | 'exit' (IDENTIFIER | NATURAL) | 'readonly' | 'throws' | 'options' IDENTIFIER
# [044] callable_posture
callable_posture ::= 'async' | 'generator' | 'async_generator'
# [045] return_clause
return_clause ::= '→' type_annotation
# [046] alternate_exit_clause
alternate_exit_clause ::= '⇥' type_annotation
# [047] ergo_joint
ergo_joint ::= 'then'
# [048] clausura_joint
clausura_joint ::= '∴'
# [049] clausura_expr
clausura_expr ::= compact_clausura_expr | clausura_legacy_expr
# [050] compact_clausura_expr
compact_clausura_expr ::= clausura_signature clausura_joint (expression | fac_block)
# [051] clausura_signature
clausura_signature ::= (clausura_param | '(' clausura_params? ')') return_clause? alternate_exit_clause?
# [052] fac_block
fac_block ::= 'do' fac_modifier? block_stmt cape_clause?
# [053] clausura_legacy_expr
clausura_legacy_expr ::= 'lambda' clausura_params? ('→' type_annotation)? (':' expression | block_stmt)
# [054] clausura_params
clausura_params ::= clausura_param (',' clausura_param)*
# [055] clausura_param
clausura_param ::= type_annotation IDENTIFIER
# [056] genus_decl
genus_decl ::= 'class' IDENTIFIER generic_params? ('implements' contract_ref ((',' | '∩') contract_ref)*)? '{' genus_member* '}'
# [057] genus_member
genus_member ::= annotation* (genus_field_decl | functio_method_decl) | kernel_decl | nondum_method_decl
# [058] nondum_method_decl
nondum_method_decl ::= annotation* nondum_annotation annotation* 'fn' IDENTIFIER generic_params? '(' param_list ')' func_modifier* callable_posture? return_clause? alternate_exit_clause?
# [059] genus_field_decl
genus_field_decl ::= (('let' | 'mut') type_annotation IDENTIFIER 'optional'? ('=' const_init)?) | genus_const_decl
# [060] genus_const_decl
genus_const_decl ::= 'const' type_annotation IDENTIFIER '=' const_init
# [061] field_decl
field_decl ::= (('let' | 'mut')? type_annotation IDENTIFIER 'optional'? ('=' const_init)?) | genus_const_decl
# [062] functio_method_decl
functio_method_decl ::= 'fn' IDENTIFIER generic_params? '(' param_list ')' func_modifier* callable_posture? return_clause? alternate_exit_clause? block_stmt
# [063] annotation
annotation ::= nucleum_annotation | radix_annotation | braced_annotation | annotation_sugar
# [064] annotation_name
annotation_name ::= ANNOTATION_NAME
# [065] braced_annotation
braced_annotation ::= '@' annotation_name '{' annotation_field_list? '}'
# [066] annotation_field_list
annotation_field_list ::= annotation_field (',' annotation_field)*
# [067] annotation_field
annotation_field ::= ANNOTATION_FIELD_NAME '=' (expression | concrete_type)
# [068] annotation_sugar
annotation_sugar ::= '@' annotation_name NON_NEWLINE_TOKEN* NEWLINE
# [069] nucleum_annotation
nucleum_annotation ::= nucleum_sugar | nucleum_braced
# [070] nucleum_sugar
nucleum_sugar ::= '@' 'kernel' nucleum_modifier? NEWLINE
# [071] nucleum_braced
nucleum_braced ::= '@' 'kernel' '{' nucleum_field_list? '}'
# [072] nucleum_modifier
nucleum_modifier ::= 'fragment' | nucleum_tier
# [073] nucleum_tier
nucleum_tier ::= 'relaxed' | 'unsafe'
# [074] nucleum_field_list
nucleum_field_list ::= nucleum_field (',' nucleum_field)*
# [075] nucleum_field
nucleum_field ::= 'fragment' '=' ('true' | 'false')
# [076] radix_annotation
radix_annotation ::= '@' 'radix' radix_directive NEWLINE
# [077] radix_directive
radix_directive ::= 'lane' STRING | 'backward' STRING | 'contract' STRING | 'type' IDENTIFIER 'mut' concrete_type+
# [078] ad_annotation
ad_annotation ::= '@' 'call' ASCII_STRING NEWLINE
# [079] nondum_annotation
nondum_annotation ::= '@' 'unstable' NON_NEWLINE_TOKEN* NEWLINE | '@' 'unstable' '{' annotation_field_list? '}'
# [080] implendum_decl
implendum_decl ::= 'interface' IDENTIFIER generic_params? '{' implendum_method_decl* '}'
# [081] implendum_method_decl
implendum_method_decl ::= annotation* 'fn' IDENTIFIER '(' param_list ')' func_modifier* callable_posture? return_clause? alternate_exit_clause?
# [082] typus_decl
typus_decl ::= 'type' IDENTIFIER generic_params? '=' type_annotation
# [083] ordo_decl
ordo_decl ::= 'enum' IDENTIFIER '{' enum_member (',' enum_member)* '}'
# [084] enum_member
enum_member ::= IDENTIFIER ('=' ('-'? NUMBER | STRING))?
# [085] discretio_decl
discretio_decl ::= 'union' IDENTIFIER generic_params? '{' union_fields? variant (',' variant)* '}'
# [086] union_fields
union_fields ::= annotation+ field_decl union_member*
# [087] union_member
union_member ::= annotation* field_decl
# [088] variant
variant ::= IDENTIFIER ('{' variant_fields '}')?
# [089] variant_fields
variant_fields ::= (type_annotation IDENTIFIER)*
# [090] schema_decl
schema_decl ::= 'schema' IDENTIFIER '{' (schema_column (NEWLINE schema_column)*)? '}'
# [091] schema_column
schema_column ::= 'column' type_annotation IDENTIFIER (':' IDENTIFIER)?
# [092] importa_decl
importa_decl ::= importa_record | importa_sugar
# [093] importa_record
importa_record ::= 'import' '{' import_field_list '}'
# [094] import_field_list
import_field_list ::= import_field (',' import_field)*
# [095] import_field
import_field ::= ex_field | visibilitas_field | nomen_field | ut_field | omnia_field
# [096] ex_field
ex_field ::= 'from' '=' STRING
# [097] visibilitas_field
visibilitas_field ::= 'visibility' '=' publica
# [098] nomen_field
nomen_field ::= 'name' '=' IDENTIFIER
# [099] ut_field
ut_field ::= 'as' '=' IDENTIFIER
# [100] omnia_field
omnia_field ::= 'all' '=' IDENTIFIER
# [101] importa_sugar
importa_sugar ::= 'import' ('from' | import_target) STRING publica? (named_import | wildcard_import | selective_import)?
# [102] import_target
import_target ::= IDENTIFIER
# [103] publica
publica ::= 'public'
# [104] named_import
named_import ::= IDENTIFIER ('as' IDENTIFIER)?
# [105] wildcard_import
wildcard_import ::= '*' 'as' IDENTIFIER
# [106] selective_import
selective_import ::= 'const' import_value_binding (',' import_value_binding)*
# [107] import_value_binding
import_value_binding ::= IDENTIFIER ('as' IDENTIFIER)?
# [108] type_annotation
type_annotation ::= union_hole_type | concrete_type
# [109] concrete_type
concrete_type ::= intersection_type ('∪' intersection_type)*
# [110] union_hole_type
union_hole_type ::= ('ref' | 'mut' | 'own' | 'copy')? '∪'
# [111] intersection_type
intersection_type ::= owned_type ('∩' owned_type)*
# [112] owned_type
owned_type ::= ('ref' | 'mut' | 'own' | 'copy')? base_type
# [113] base_type
base_type ::= hole_type | function_type | width_type_sugar | ratio_type | failable_promissum_type | qualified_type type_arguments?
# [114] failable_promissum_type
failable_promissum_type ::= IDENTIFIER '<' type_annotation alternate_exit_clause '>'
# [115] ratio_type
ratio_type ::= 'record' '<' ('*' | labeled_type_argument (',' labeled_type_argument)*) '>'
# [116] hole_type
hole_type ::= '_'
# [117] qualified_type
qualified_type ::= type_head ('.' IDENTIFIER)*
# [118] type_head
type_head ::= IDENTIFIER | 'wrapping'
# [119] type_arguments
type_arguments ::= '<' type_argument (',' type_argument)* '>'
# [120] type_argument
type_argument ::= labeled_type_argument | range_argument | sized_range_argument | spelled_lift | type_annotation | NATURAL | '[' figura_list? ']'
# [121] labeled_type_argument
labeled_type_argument ::= IDENTIFIER ':' type_annotation
# [122] range_argument
range_argument ::= range_bound range_glyph range_bound
# [123] sized_range_argument
sized_range_argument ::= 'size' range_argument
# [124] range_glyph
range_glyph ::= '‥' | '…'
# [125] range_bound
range_bound ::= '-'? NATURAL | '-'? '∞' | 'size'? IDENTIFIER (('+' | '-') NATURAL)?
# [126] width_type_sugar
width_type_sugar ::= WIDTH_MARKER | LISTA_WIDTH_SUGAR | (TENSOR_WIDTH_SUGAR | SPARSA_WIDTH_SUGAR | VECTOR_WIDTH_SUGAR) shape_suffix? | MATRIX_WIDTH_SUGAR shape_suffix
# [127] shape_suffix
shape_suffix ::= '[' figura_list? ']'
# [128] figura
figura ::= spelled_lift | figura_product (('+' | '-') NATURAL)*
# [129] spelled_lift
spelled_lift ::= 'size' lift_extent
# [130] lift_extent
lift_extent ::= NATURAL | '-' NATURAL | '(' figura ')' | IDENTIFIER | '[' figura_list? ']'
# [131] figura_product
figura_product ::= figura_primary ('/' NATURAL)*
# [132] figura_primary
figura_primary ::= '_' | NATURAL | IDENTIFIER | '[' figura_list? ']' | '(' figura ')'
# [133] figura_list
figura_list ::= figura (',' figura)*
# [134] function_type
function_type ::= '(' type_list? ')' '→' type_annotation alternate_exit_clause?
# [135] type_list
type_list ::= type_annotation (',' type_annotation)*
# [136] si_stmt
si_stmt ::= 'if' si_tail
# [137] si_tail
si_tail ::= expression arm ('elif' si_tail | secus_clause)?
# [138] secus_clause
secus_clause ::= 'else' else_arm
# [139] arm
arm ::= (block_stmt | ergo_joint statement) cape_clause?
# [140] else_arm
else_arm ::= (block_stmt | ergo_joint statement) cape_clause?
# [141] dum_stmt
dum_stmt ::= 'while' expression (block_stmt | ergo_joint statement) cape_clause?
# [142] itera_stmt
itera_stmt ::= 'for' (itera_clause (',' itera_clause)* | 'ref' expression) apud_clause? filum_clause? ('let' | 'mut') itera_binding (block_stmt | ergo_joint statement) cape_clause?
# [143] itera_clause
itera_clause ::= ('from' | 'range') expression ('and' expression)*
# [144] itera_binding
itera_binding ::= array_pattern | object_pattern | IDENTIFIER (('and' IDENTIFIER) | (',' IDENTIFIER))*
# [145] apud_clause
apud_clause ::= 'at' '[' IDENTIFIER (',' IDENTIFIER)* ']'
# [146] elige_stmt
elige_stmt ::= 'switch' expression '{' casu_elige_clause* ceterum_clause? '}' cape_clause?
# [147] casu_elige_clause
casu_elige_clause ::= 'case' expression (block_stmt | ergo_joint statement)
# [148] ceterum_clause
ceterum_clause ::= 'default' (block_stmt | ergo_joint statement)
# [149] discerne_stmt
discerne_stmt ::= 'match' 'all'? discriminants '{' casu_variant_clause* ceterum_clause? '}'
# [150] discriminants
discriminants ::= subject_path ('and' subject_path)*
# [151] subject_path
subject_path ::= IDENTIFIER ('.' IDENTIFIER)*
# [152] casu_variant_clause
casu_variant_clause ::= 'case' patterns (block_stmt | ergo_joint statement)
# [153] patterns
patterns ::= pattern ('and' pattern)*
# [154] pattern
pattern ::= pattern_atom ('or' pattern_atom)*
# [155] pattern_atom
pattern_atom ::= '_' | negated_number | literal | type_pattern | (IDENTIFIER ut_pattern?)
# [156] negated_number
negated_number ::= '-' NUMBER
# [157] type_pattern
type_pattern ::= IDENTIFIER type_arguments? ut_pattern?
# [158] ut_pattern
ut_pattern ::= ('as' IDENTIFIER) | (('let' | 'mut') pattern_binding (',' pattern_binding)*)
# [159] pattern_binding
pattern_binding ::= IDENTIFIER ('as' IDENTIFIER)?
# [160] custodi_stmt
custodi_stmt ::= 'guard' '{' si_guard_clause+ '}'
# [161] si_guard_clause
si_guard_clause ::= 'if' expression (block_stmt | ergo_joint statement)
# [162] ex_stmt
ex_stmt ::= 'from' expression ('let' | 'mut') extract_fields
# [163] extract_fields
extract_fields ::= extract_field (',' extract_field)* (',' ceteri_field)? | ceteri_field
# [164] extract_field
extract_field ::= IDENTIFIER ('as' IDENTIFIER)?
# [165] ceteri_field
ceteri_field ::= 'rest' IDENTIFIER
# [166] redde_stmt
redde_stmt ::= 'return' ('thread' expression? | expression?)
# [167] reddet_stmt
reddet_stmt ::= 'return_await' expression
# [168] tacebit_stmt
tacebit_stmt ::= 'await' expression
# [169] cede_stmt
cede_stmt ::= 'yield' expression
# [170] rumpe_stmt
rumpe_stmt ::= 'break'
# [171] perge_stmt
perge_stmt ::= 'continue'
# [172] tacet_stmt
tacet_stmt ::= 'pass'
# [173] iace_stmt
iace_stmt ::= iace_expr | iace_guarded_expr
# [174] iace_expr
iace_expr ::= ('throw' | 'panic') expression
# [175] iace_guarded_expr
iace_guarded_expr ::= ('throw' | 'panic') expression NO_NEWLINE 'if' expression
# [176] cape_clause
cape_clause ::= 'catch' IDENTIFIER block_stmt
# [177] adfirma_stmt
adfirma_stmt ::= 'assert' expression ('panic' expression)?
# [178] requirit_stmt
requirit_stmt ::= 'require' expression 'throw' expression
# [179] reice_stmt
reice_stmt ::= 'reject' expression 'throw' expression
# [180] expression
expression ::= assignment
# [181] transfer
transfer ::= ternary ('⇇' ternary)?
# [182] sink_into
sink_into ::= transfer ('⇜' ternary)?
# [183] value_marker
value_marker ::= 'own' | 'copy'
# [184] assignment
assignment ::= sink_into ('←' 'copy'? assignment | '↤' assignment via_clause? inline_default?)?
# [185] inc_dec_stmt
inc_dec_stmt ::= place ('↑' | '↓')
# [186] place
place ::= call_expr
# [187] ternary
ternary ::= aut_expr ('✓' expression '✗' aut_expr)?
# [188] aut_expr
aut_expr ::= et_expr (('or') et_expr)*
# [189] et_expr
et_expr ::= equality (('and') equality)*
# [190] equality
equality ::= comparison equality_tail*
# [191] equality_tail
equality_tail ::= ('≡' | '≢' | '≅' | '≇' | '≈' | '≉') comparison | ('is' | 'not' 'is') type_annotation
# [192] comparison
comparison ::= format_expr (('≺' | '≻' | '≤' | '≥' | '∈' | '∉') format_expr)*
# [193] format_expr
format_expr ::= bitwise_or_expr ('¶' STRING)?
# [194] bitwise_or_expr
bitwise_or_expr ::= bitwise_xor_expr ('∨' bitwise_xor_expr)*
# [195] bitwise_xor_expr
bitwise_xor_expr ::= bitwise_and_expr ('⊻' bitwise_and_expr)*
# [196] bitwise_and_expr
bitwise_and_expr ::= shift_expr ('∧' shift_expr)*
# [197] shift_expr
shift_expr ::= range_expr (('⇐' | '⇒') range_expr)*
# [198] range_expr
range_expr ::= additive_expr range_tail?
# [199] range_tail
range_tail ::= ('‥' | '…' | 'before' | 'until') additive_expr ('step' additive_expr)?
# [200] additive_expr
additive_expr ::= multiplicative_expr (('+' | '-' | '⤒' | '⤓') multiplicative_expr)*
# [201] multiplicative_expr
multiplicative_expr ::= vel_expr (('*' | '/' | '÷' | '%' | '·' | '×' | '⊗' | '⊙' | '⊘') vel_expr)*
# [202] vel_expr
vel_expr ::= unary_expr ('coalesce' vel_rhs)*
# [203] vel_rhs
vel_rhs ::= unary_expr vel_range_tail?
# [204] vel_range_tail
vel_range_tail ::= ('‥' | '…' | 'before' | 'until') unary_expr ('step' unary_expr)?
# [205] unary_expr
unary_expr ::= ('-' | '¬' | 'not' | '√' | '∛' | '∜') unary_expr | rounding_expr | finge_expr | cast_expr
# [206] rounding_expr
rounding_expr ::= '⌊' expression ('⌋' | '⌉') | '⌈' expression '⌉'
# [207] gradient_expr
gradient_expr ::= call_expr ('∇' gradient_selection?)?
# [208] gradient_selection
gradient_selection ::= '[' gradient_place (',' gradient_place)* ']'
# [209] gradient_place
gradient_place ::= expression
# [210] cast_expr
cast_expr ::= gradient_expr ('∷' type_annotation | conversio_expr)* inline_default?
# [211] conversio_expr
conversio_expr ::= '↦' (type_annotation | interval_target) via_clause? inline_default?
# [212] interval_target
interval_target ::= range_expr
# [213] via_clause
via_clause ::= 'via' IDENTIFIER
# [214] inline_default
inline_default ::= '⊥' unary_expr
# [215] call_expr
call_expr ::= primary (call_suffix | member_suffix | transpose_suffix | optional_suffix | non_null_suffix)*
# [216] call_suffix
call_suffix ::= call_type_args? '(' argument_list ')'
# [217] member_suffix
member_suffix ::= '.' IDENTIFIER | '[' expression ']'
# [218] transpose_suffix
transpose_suffix ::= 'ᵀ'
# [219] optional_suffix
optional_suffix ::= '?.' IDENTIFIER | '?[' expression ']' | '?(' argument_list ')'
# [220] non_null_suffix
non_null_suffix ::= '!.' IDENTIFIER | '![' expression ']' | '!(' argument_list ')'
# [221] argument_list
argument_list ::= (argument (',' argument)*)?
# [222] argument
argument ::= template_argument | (call_marker | 'axis')? 'spread'? expression
# [223] call_marker
call_marker ::= 'ref' | 'mut' | 'own' | 'copy'
# [224] template_argument
template_argument ::= 'spread'? IDENTIFIER ':' expression
# [225] literal
literal ::= NUMBER | STRING | ASCII_STRING | BACKTICK_STRING | OCTETI_STRING | 'true' | 'false' | 'null' | '∞' | 'nan'
# [226] regex_literal
regex_literal ::= REGEX_TYPE_WORD REGEX_BODY | '_' REGEX_BODY
# [227] primary
primary ::= IDENTIFIER | literal | regex_literal | 'self' | array_literal | json_literal | typed_constructor | iuncta_expr | ad_expr | clausura_expr | praefixum_expr | scriptum_expr | lege_expr | reducta_expr | scan_expr | sort_expr | capta_expr | '(' expression ')'
# [228] ad_expr
ad_expr ::= 'call' ASCII_STRING ad_opener?
# [229] ad_opener
ad_opener ::= '(' expression ')'
# [230] array_literal
array_literal ::= '[' array_element_list? ']'
# [231] array_element_list
array_element_list ::= array_element (',' array_element)*
# [232] array_element
array_element ::= argument | '_'
# [233] iuncta_expr
iuncta_expr ::= 'tuple' type_arguments '[' argument_list? ']'
# [234] json_literal
json_literal ::= '{' (json_member (',' json_member)*)? '}'
# [235] json_member
json_member ::= STRING ':' json_value
# [236] typed_constructor
typed_constructor ::= type_annotation '{' field_list? '}' construction_source? | hole_type '{' field_list? '}' construction_source? | type_annotation json_literal | hole_type json_literal | '{' field_list '}' construction_source? | type_annotation '[' array_element_list? ']'
# [237] field_list
field_list ::= field_init (',' field_init)*
# [238] field_init
field_init ::= (field_key '=' expression) | IDENTIFIER
# [239] field_key
field_key ::= IDENTIFIER | STRING | '[' expression ']'
# [240] construction_source
construction_source ::= 'from' call_expr
# [241] json_value
json_value ::= json_object | json_array | json_string | json_number | 'true' | 'false' | 'null'
# [242] json_object
json_object ::= '{' (json_member (',' json_member)*)? '}'
# [243] json_array
json_array ::= '[' (json_value (',' json_value)*)? ']'
# [244] json_string
json_string ::= STRING
# [245] json_number
json_number ::= NUMBER
# [246] finge_expr
finge_expr ::= 'variant' qualified_ident ('{' field_list? '}')? ('∷' type_annotation)?
# [247] qualified_ident
qualified_ident ::= IDENTIFIER ('.' IDENTIFIER)*
# [248] praefixum_expr
praefixum_expr ::= 'comptime' block_stmt
# [249] scriptum_expr
scriptum_expr ::= 'format' '(' STRING (',' expression)* ')'
# [250] lege_expr
lege_expr ::= 'read' 'line'?
# [251] reducta_expr
reducta_expr ::= 'reduce' 'via' reducta_op 'from' expression apud_clause? reducta_group? (filum_clause? reducta_body)? reducta_identity?
# [252] reducta_op
reducta_op ::= 'sum' | 'product' | 'max' | 'min' | 'argmax' | 'argmin' | 'all' | 'any' | 'count' | 'first'
# [253] reducta_group
reducta_group ::= 'per' (group_key | '[' expression (',' expression)* ']')
# [254] group_key
group_key ::= unary_expr
# [255] reducta_body
reducta_body ::= ('let' | 'mut') IDENTIFIER block_stmt
# [256] reducta_identity
reducta_identity ::= 'coalesce' expression
# [257] scan_expr
scan_expr ::= 'scan' 'via' scan_op ('total' ('inclusive' | 'exclusive'))? 'from' expression apud_clause scan_group? scan_order_clause? filum_clause 'let' IDENTIFIER block_stmt
# [258] scan_op
scan_op ::= 'sum' | 'product' | 'max' | 'min' | 'all' | 'any' | 'count'
# [259] scan_group
scan_group ::= 'per' expression
# [260] scan_order_clause
scan_order_clause ::= 'order' ('asc' | 'desc')
# [261] sort_expr
sort_expr ::= 'sort' 'via' sort_direction ('from' | 'ref') expression sort_body?
# [262] sort_direction
sort_direction ::= 'asc' | 'desc'
# [263] sort_body
sort_body ::= ('let' | 'mut') IDENTIFIER block_stmt
# [264] filum_clause
filum_clause ::= 'thread' IDENTIFIER
# [265] capta_expr
capta_expr ::= 'trap' block_stmt
# [266] object_pattern
object_pattern ::= '{' pattern_property (',' pattern_property)* '}'
# [267] pattern_property
pattern_property ::= 'rest'? IDENTIFIER ('as' IDENTIFIER)?
# [268] array_pattern
array_pattern ::= '[' array_pattern_element (',' array_pattern_element)* ']'
# [269] array_pattern_element
array_pattern_element ::= '_' | 'rest'? IDENTIFIER
# [270] nota_stmt
nota_stmt ::= ('print' | 'debug' | 'warn' | 'write') expression (',' expression)*
# [271] entry_header
entry_header ::= ('args' IDENTIFIER)? ('exit' expression)?
# [272] incipit_stmt
incipit_stmt ::= 'main' entry_header block_stmt
# [273] incipiet_stmt
incipiet_stmt ::= 'async_main' entry_header block_stmt
# [274] probandum_decl
probandum_decl ::= 'describe' STRING proba_modifier* '{' probandum_body '}'
# [275] probandum_body
probandum_body ::= (praepara_block | probandum_decl | proba_stmt)*
# [276] proba_stmt
proba_stmt ::= 'test' STRING proba_modifier* block_stmt
# [277] proba_modifier
proba_modifier ::= 'expect_failure' | 'skip' STRING | 'todo' STRING | 'only' | 'tag' STRING | 'timeout' NATURAL | 'bench' | 'repeat' NATURAL | 'flaky' NATURAL | 'only_in' STRING
# [278] praepara_block
praepara_block ::= ('setup' | 'async_setup' | 'teardown' | 'async_teardown') 'all'? block_stmt
# [279] fac_stmt
fac_stmt ::= 'do' fac_modifier? block_stmt cape_clause? ('while' expression)?
# [280] fac_modifier
fac_modifier ::= 'all' | 'batch' | 'device' | 'eligible'
# [281] IDENTIFIER
IDENTIFIER ::=
# [282] NUMBER
NUMBER ::=
# [283] NATURAL
NATURAL ::=
# [284] STRING
STRING ::=
# [285] ASCII_STRING
ASCII_STRING ::=
# [286] BACKTICK_STRING
BACKTICK_STRING ::=
# [287] OCTETI_STRING
OCTETI_STRING ::=
# [288] REGEX_TYPE_WORD
REGEX_TYPE_WORD ::=
# [289] REGEX_BODY
REGEX_BODY ::=
# [290] NEWLINE
NEWLINE ::=
# [291] WIDTH_MARKER
WIDTH_MARKER ::=
# [292] LISTA_WIDTH_SUGAR
LISTA_WIDTH_SUGAR ::=
# [293] TENSOR_WIDTH_SUGAR
TENSOR_WIDTH_SUGAR ::=
# [294] SPARSA_WIDTH_SUGAR
SPARSA_WIDTH_SUGAR ::=
# [295] VECTOR_WIDTH_SUGAR
VECTOR_WIDTH_SUGAR ::=
# [296] MATRIX_WIDTH_SUGAR
MATRIX_WIDTH_SUGAR ::=
# [297] FRONTMATTER_DELIMITER
FRONTMATTER_DELIMITER ::=
# [298] TOML_LINES
TOML_LINES ::=
# [299] TOML_MARKER
TOML_MARKER ::=
# [300] FABER_MARKER
FABER_MARKER ::=
# [301] FABER_TEST_MARKER
FABER_TEST_MARKER ::=
# [302] STREAM_MARKER
STREAM_MARKER ::=
# [303] STREAM_LINES
STREAM_LINES ::=
# [304] ANNOTATION_NAME
ANNOTATION_NAME ::=
# [305] ANNOTATION_FIELD_NAME
ANNOTATION_FIELD_NAME ::=
# [306] NON_NEWLINE_TOKEN
NON_NEWLINE_TOKEN ::=
# [307] NO_NEWLINE
NO_NEWLINE ::=
```

Fetch list: https://faberlang.dev/agents/index.md
