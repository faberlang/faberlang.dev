# Program

The smallest package that checks. Two files.

`faber.toml`:

```toml
[package]
name = "salve-munde"
version = "0.1.0"
```

`src/main.fab`:

```faber locale=en
fn salve(string nomen) → string {
    const string msg ← "Salve, §!"(nomen)
    return msg
}

main {
    const string m ← salve("munde")
    print m
}
```

```bash
faber check .
```

`faber check` is lexing, parsing, and type checking. It does not build a
native binary.

Next: https://faberlang.dev/agents/functions.md
