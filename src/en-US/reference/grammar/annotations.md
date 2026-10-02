+++
title = "Annotations & directives"
section = "reference"
order = 4
translate_spans = false  # rule names are the Latin identity, not a spelling
sources = [
  "faber/docs/EBNF.md",
  "faber/docs/grammar/grammar.jsonl",
  "radix/locale/en/pack.toml",
]
+++

The `@` annotation family: the generic shape, the kernel (`@ kernel`), compiler-lane (`@ radix`), and capability (`@ call`) directives.

Rule names (`fab_file`, `itera_stmt`) are the stable Latin grammar identifiers;
the quoted words are the English reader spellings. Return to the
[grammar index](/en-US/reference/grammar.html).

## Productions {#productions}

```ebnf
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
```

## Terms {#terms}

Keywords in these productions that have a corpus term page. The production id
on the left is the Latin spine name; the links are the English reader spellings
you write.

| Production | Terms |
|---|---|
| `nucleum_sugar` | [`kernel`](/en-US/corpus/kernel.html) |
| `nucleum_braced` | [`kernel`](/en-US/corpus/kernel.html) |
| `nucleum_field` | [`false`](/en-US/corpus/false.html), [`true`](/en-US/corpus/true.html) |
| `radix_directive` | [`mut`](/en-US/corpus/mut.html), [`type`](/en-US/corpus/type.html) |
| `ad_annotation` | [`call`](/en-US/corpus/call.html) |
