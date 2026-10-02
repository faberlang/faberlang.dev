+++
title = "Lexical structure & glyphs"
section = "reference"
order = 10
translate_spans = false  # rule names are the Latin identity, not a spelling
sources = [
  "faber/docs/EBNF.md",
  "faber/docs/grammar/grammar.jsonl",
  "radix/locale/en/pack.toml",
]
+++

The terminal tokens the lexer produces: identifiers, numbers, strings, width markers, and the frontmatter delimiter. Uppercase rule names here are lexical terminals.

Rule names (`fab_file`, `itera_stmt`) are the stable Latin grammar identifiers;
the quoted words are the English reader spellings. Return to the
[grammar index](/en-US/reference/grammar.html).

## Productions {#productions}

```ebnf
# [239] IDENTIFIER
IDENTIFIER ::=
# [240] NUMBER
NUMBER ::=
# [241] NATURAL
NATURAL ::=
# [242] STRING
STRING ::=
# [243] ASCII_STRING
ASCII_STRING ::=
# [244] BACKTICK_STRING
BACKTICK_STRING ::=
# [245] OCTETI_STRING
OCTETI_STRING ::=
# [246] NEWLINE
NEWLINE ::=
# [247] WIDTH_MARKER
WIDTH_MARKER ::=
# [248] LISTA_WIDTH_SUGAR
LISTA_WIDTH_SUGAR ::=
# [249] TENSOR_WIDTH_SUGAR
TENSOR_WIDTH_SUGAR ::=
# [250] SPARSA_WIDTH_SUGAR
SPARSA_WIDTH_SUGAR ::=
# [251] VECTOR_WIDTH_SUGAR
VECTOR_WIDTH_SUGAR ::=
# [252] MATRIX_WIDTH_SUGAR
MATRIX_WIDTH_SUGAR ::=
# [253] FRONTMATTER_DELIMITER
FRONTMATTER_DELIMITER ::=
# [254] TOML_LINES
TOML_LINES ::=
# [255] ANNOTATION_NAME
ANNOTATION_NAME ::=
# [256] ANNOTATION_FIELD_NAME
ANNOTATION_FIELD_NAME ::=
# [257] NON_NEWLINE_TOKEN
NON_NEWLINE_TOKEN ::=
# [258] NO_NEWLINE
NO_NEWLINE ::=
```
