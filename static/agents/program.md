# Program

The smallest package that checks. Two files. `faber init` writes this
manifest; the name here is `salve-munde`.

`faber.toml`:

```toml
[package]
name = "salve-munde"
version = "0.1.0"
edition = "2026"

[paths]
source = "src"
entry = "main.fab"

[build]
kind = "bin"
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

`faber check .` exits 0. It is lexing, parsing, and type checking. It does
not build a native binary. `faber run .` prints `Salve, munde!`.

Next: https://faberlang.dev/agents/functions.md
