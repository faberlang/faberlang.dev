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

A pattern is what a `match` arm accepts. It is not the `match` statement
itself — that lives with [statements](statements.html) — it is the shape
on the left of each `case`: a literal, a type, a binding, or a
destructured object or array.

`and` joins patterns that must all hold; `or` offers alternatives.
`const` / `var` / `as` bind a name to what matched. `rest` keeps the
leftover fields or elements. The same atoms appear when a union-typed
value is read back out by member type.

```faber locale=en
main {
    const i32 ∪ string signum ← 7

    match signum {
        case i32 const n { print "a number" }
        case string const s { print "a text" }
    }
}
```

Return to the [grammar overview](/en-US/reference/grammar.html).

## Terms {#terms}

These are the words you write in this part of the language. Each links to its
page. The second column names the grammar rule the word belongs to.

| Term | Grammar rule |
|---|---|
| [`and`](/en-US/corpus/and.html) | `patterns` |
| [`or`](/en-US/corpus/or.html) | `pattern` |
| [`const`](/en-US/corpus/const.html), [`as`](/en-US/corpus/as.html), [`var`](/en-US/corpus/var.html) | `ut_pattern` |
| [`as`](/en-US/corpus/as.html) | `pattern_binding` |
| [`rest`](/en-US/corpus/rest.html), [`as`](/en-US/corpus/as.html) | `pattern_property` |
| [`rest`](/en-US/corpus/rest.html) | `array_pattern_element` |

## Formal grammar {#formal-grammar}

The rules for this part of the language are the parser's own definition of it.
They are written for models and tools, so this page does not repeat them; the
full list is at [every production](/agents/grammar/productions.md).
