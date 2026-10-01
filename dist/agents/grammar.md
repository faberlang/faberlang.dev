# Grammar

These are the forms the other pages check.

- A type stands before the name: `string name`, `int n`.
- A runtime store is `←`. `const` does not change. `var` does.
- A function is `fn name(int a) → int { return a }`. A `void` function uses a bare `return`.
- The entry is `main { }` or `main args argv { }`.
- Branches are `if`, `elif`, and `else`.
- A list walk is `for from nums const item { }`. A condition loop is `while n ≺ 2 { }`.
- Comparisons in these programs are `≺`, `≥`, `≡`, and `≠`.
- A missing `int` is `int ∪ none`. The missing value is `null`.
- A list is `list<int>`. An empty list is `empty`.
- A width is a bare marker, `i32` or `f32`, ascribed with `∷`.
- A recoverable error is `→ int ⇥ string`, sent with `throw`, caught with `do` / `catch`.
- `require b ≠ 0 throw "..."` throws when the condition fails. `reject value ≺ 0 throw "..."` throws when it holds.
- `ref`, `mut`, and `own` sit before the parameter type.
- An async function writes `async` before `→`. The caller is `async_main` and binds with `await_const`.
- A module import is `import from "./greet" greet`. An exported function is marked `@ public`.
- A library import is `import from "norma:text" text`.
- A generic function is `fn identitas<T>(T valor) → T`.
- A comment is a `#` line by itself.

Do not write `name: T`. Do not write `int?`. Do not write `//`. Do not put `#` after code on the same line.

```faber locale=en
# English source.
fn salve(string nomen) → string {
    const string msg ← "Salve, §!"(nomen)
    return msg
}

main {
    const string m ← salve("munde")
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

Fetch list: https://faberlang.dev/agents/index.md
