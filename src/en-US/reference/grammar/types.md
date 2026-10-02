+++
title = "Types & contracts"
section = "grammar-types"
order = 5
translate_spans = false  # rule names are the Latin identity, not a spelling
sources = [
  "faber/docs/EBNF.md",
  "faber/docs/grammar/grammar.jsonl",
  "radix/locale/en/pack.toml",
]
+++

Type syntax and the declarations built on it: interfaces, type aliases, enums, tagged unions, and relational schemas.

Rule names (`fab_file`, `itera_stmt`) are the stable Latin grammar identifiers;
the quoted words are the English reader spellings. Return to the
[grammar index](/en-US/reference/grammar.html).

## Productions {#productions}

```ebnf
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
figura ::= '_' | NATURAL | IDENTIFIER | '[' figura_list? ']'
# [109] figura_list
figura_list ::= figura (',' figura)*
# [110] function_type
function_type ::= '(' type_list? ')' '→' type_annotation alternate_exit_clause?
# [111] type_list
type_list ::= type_annotation (',' type_annotation)*
```

## Terms {#terms}

Keywords in these productions that have a corpus term page. The production id
on the left is the Latin spine name; the links are the English reader spellings
you write.

| Production | Terms |
|---|---|
| `implendum_decl` | [`interface`](/en-US/corpus/interface.html) |
| `implendum_method_decl` | [`fn`](/en-US/corpus/fn.html) |
| `typus_decl` | [`type`](/en-US/corpus/type.html) |
| `ordo_decl` | [`enum`](/en-US/corpus/enum.html) |
| `discretio_decl` | [`union`](/en-US/corpus/union.html) |
| `union_hole_type` | [`ref`](/en-US/corpus/ref.html), [`mut`](/en-US/corpus/mut.html) |
| `owned_type` | [`ref`](/en-US/corpus/ref.html), [`mut`](/en-US/corpus/mut.html) |
| `ratio_type` | [`record`](/en-US/corpus/record.html) |
