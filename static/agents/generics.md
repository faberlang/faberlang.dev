# Generics

A function names its type parameter in `<T>` and uses that parameter as a
type. The call writes the type argument.

```faber locale=en
fn identitas<T>(T valor) → T {
    return valor
}

main {
    const int seven ← identitas<int>(7)
    print seven
}
```

Fetch list: https://faberlang.dev/agents/index.md
