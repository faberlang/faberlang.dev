+++
title = "Patterns & destructuring"
section = "grammar-patterns"
order = 8
translate_spans = false  # rule names are the Latin identity, not a spelling
sources = [
  "faber/docs/EBNF.md",
  "faber/docs/grammar/grammar.jsonl",
  "radix/locale/en/pack.toml",
]
+++

Patterns and destructuring: the atoms a match arm accepts, type and alias patterns, and the object and array destructuring forms.

Rule names (`fab_file`, `itera_stmt`) are the stable Latin grammar identifiers;
the quoted words are the English reader spellings. Return to the
[grammar index](/en-US/reference/grammar.html).

## Productions {#productions}

```ebnf
# [128] patterns
patterns ::= pattern ('and' pattern)*
# [129] pattern
pattern ::= pattern_atom ('or' pattern_atom)*
# [130] pattern_atom
pattern_atom ::= '_' | negated_number | literal | type_pattern | (IDENTIFIER ut_pattern?)
# [131] negated_number
negated_number ::= '-' NUMBER
# [132] type_pattern
type_pattern ::= IDENTIFIER type_arguments? ut_pattern?
# [133] ut_pattern
ut_pattern ::= ('as' IDENTIFIER) | (('const' | 'var') pattern_binding (',' pattern_binding)*)
# [134] pattern_binding
pattern_binding ::= IDENTIFIER ('as' IDENTIFIER)?
# [225] object_pattern
object_pattern ::= '{' pattern_property (',' pattern_property)* '}'
# [226] pattern_property
pattern_property ::= 'rest'? IDENTIFIER ('as' IDENTIFIER)?
# [227] array_pattern
array_pattern ::= '[' array_pattern_element (',' array_pattern_element)* ']'
# [228] array_pattern_element
array_pattern_element ::= '_' | 'rest'? IDENTIFIER
```

## Terms {#terms}

Keywords in these productions that have a corpus term page. The production id
on the left is the Latin spine name; the links are the English reader spellings
you write.

| Production | Terms |
|---|---|
| `patterns` | [`and`](/en-US/corpus/and.html) |
| `pattern` | [`or`](/en-US/corpus/or.html) |
| `ut_pattern` | [`const`](/en-US/corpus/const.html), [`as`](/en-US/corpus/as.html), [`var`](/en-US/corpus/var.html) |
| `pattern_binding` | [`as`](/en-US/corpus/as.html) |
| `pattern_property` | [`rest`](/en-US/corpus/rest.html), [`as`](/en-US/corpus/as.html) |
| `array_pattern_element` | [`rest`](/en-US/corpus/rest.html) |
