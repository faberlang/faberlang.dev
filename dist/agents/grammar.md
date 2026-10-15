# Grammar

These are the forms the other pages check.

- A type stands before the name: `string name`, `int n`.
- A runtime store is `←`. `let` does not change. `mut` does.
- A function is `fn name(int a) → int { return a }`. A `void` function uses a bare `return`.
- The entry is `main { }` or `main args argv { }`.
- Branches are `if`, `elif`, and `else`.
- A list walk is `for from nums let item { }`. A condition loop is `while n ≺ 2 { }`.
- Comparisons in these programs are `≺`, `≥`, `≡`, and `≢`.
- A missing `int` is `int ∪ none`. The missing value is `null`.
- A list is `list<int>`. An empty list is `empty`.
- A width is a bare marker, `i32` or `f32`, ascribed with `∷`. `b8` to `b64` are raw bits.
- A conversion is `↦`. A float to an integer names its rounding: `x ↦ int via floor`.
- A recoverable error is `→ int ⇥ string`, sent with `throw`, caught with `do` / `catch`.
- `require b ≢ 0 throw "..."` throws when the condition fails. `reject value ≺ 0 throw "..."` throws when it holds.
- `ref`, `mut`, and `own` sit before the parameter type. A call repeats `mut` and `own`: `duplica(mut n)`.
- A `mut` made from a read-only value is `mut list<int> ys ← copy xs`.
- An async function writes `async` before `→`. The caller is `async_main` and binds with `await_const`.
- A module import is `import from "./greet" greet`. An exported function is marked `@ public`.
- A library import is `import from "norma:text" text`.
- A generic function is `fn identitas<T>(T valor) → T`.
- A comment is a `#` line by itself.

Do not write `name: T`. Do not write `int?`. Do not write `//`. Do not put `#` after code on the same line.
Do not write `print(x)`: output is a statement, `print x`. Do not write `≠`: not-equal is `≢`. Do not write `x = 5` as a store: a runtime store is `←`. Do not write Latin type names such as `numerus` or `textus` in an English file: the locales never mix, and that is `PARSE040` `wrong_locale_type`.

```faber locale=en
# English source.
fn salve(string nomen) → string {
    let string msg ← "Salve, §!"(nomen)
    return msg
}

main {
    let string m ← salve("munde")
    print m
}
```

```faber locale=en outcome=rejects
main {
    // no
    print "en"
}
```

```faber locale=en outcome=rejects
main { # trailing
    print "en"
}
```

Detail pages:

- https://faberlang.dev/agents/grammar/productions.md — every grammar rule, in EBNF, for tools that need the formal grammar.

Fetch list: https://faberlang.dev/agents/index.md
