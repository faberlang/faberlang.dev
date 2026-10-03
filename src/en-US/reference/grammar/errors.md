+++
title = "Error channel"
section = "grammar-errors"
order = 9
translate_spans = false  # rule names are the Latin identity, not a spelling
sources = [
  "faber/docs/EBNF.md",
  "faber/docs/grammar/grammar.jsonl",
  "radix/locale/en/pack.toml",
]
+++

Failure is a second channel, not a wrapper type and not an exception that
unwinds past you. A function that can fail writes `⇥` after the success
type: `→ i32 ⇥ string` returns an integer or fails with a string. `throw`
sends a value on that channel. `do` / `catch` is the local boundary
around a call that might fail; `catch` binds the error as an ordinary
value.

`throw if` is the guarded form. `require` and `reject` (listed with
[statements](statements.html)) compile to the same idea: throw when a
condition fails, or when it holds. A call to a `⇥` function sits inside
an active `do` / `catch` (or another statement that carries `catch`).

```faber locale=en
fn divide(i32 a, i32 b) → i32 ⇥ string {
    if b ≡ 0 {
        throw "division by zero"
    }
    return a / b
}

main {
    do {
        print divide(7, 2)
    }
    catch err {
        print err
    }
}
```

Return to the [grammar overview](/en-US/reference/grammar.html).

## Terms {#terms}

These are the words you write in this part of the language. Each links to its
page. The second column names the grammar rule the word belongs to.

| Term | Grammar rule |
|---|---|
| [`throw`](/en-US/corpus/throw.html), [`panic`](/en-US/corpus/panic.html) | `iace_expr` |
| [`throw`](/en-US/corpus/throw.html), [`panic`](/en-US/corpus/panic.html), [`if`](/en-US/corpus/if.html) | `iace_guarded_expr` |
| [`catch`](/en-US/corpus/catch.html) | `cape_clause` |

## Formal grammar {#formal-grammar}

The rules for this part of the language are the parser's own definition of it.
They are written for models and tools, so this page does not repeat them; the
full list is at [every production](/agents/grammar/productions.md).
