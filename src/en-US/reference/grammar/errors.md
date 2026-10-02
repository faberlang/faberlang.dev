+++
title = "Error channel"
section = "reference"
order = 9
translate_spans = false  # rule names are the Latin identity, not a spelling
sources = [
  "faber/docs/EBNF.md",
  "faber/docs/grammar/grammar.jsonl",
  "radix/locale/en/pack.toml",
]
+++

The error channel: throwing, guarded throws, and the local `catch` handler that recovers an error into a value.

Rule names (`fab_file`, `itera_stmt`) are the stable Latin grammar identifiers;
the quoted words are the English reader spellings. Return to the
[grammar index](/en-US/reference/grammar.html).

## Productions {#productions}

```ebnf
# [148] iace_stmt
iace_stmt ::= iace_expr | iace_guarded_expr
# [149] iace_expr
iace_expr ::= ('throw' | 'panic') expression
# [150] iace_guarded_expr
iace_guarded_expr ::= ('throw' | 'panic') expression NO_NEWLINE 'if' expression
# [151] cape_clause
cape_clause ::= 'catch' IDENTIFIER block_stmt
```

## Terms {#terms}

Keywords in these productions that have a corpus term page. The production id
on the left is the Latin spine name; the links are the English reader spellings
you write.

| Production | Terms |
|---|---|
| `iace_expr` | [`throw`](/en-US/corpus/throw.html), [`panic`](/en-US/corpus/panic.html) |
| `iace_guarded_expr` | [`throw`](/en-US/corpus/throw.html), [`panic`](/en-US/corpus/panic.html), [`if`](/en-US/corpus/if.html) |
| `cape_clause` | [`catch`](/en-US/corpus/catch.html) |
