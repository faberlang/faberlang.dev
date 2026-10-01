# Packages

A package is `faber.toml` plus the source under `src/`. This is the
manifest `faber init` writes. The name here is `salve-munde`. The source
is the program at https://faberlang.dev/agents/program.md.

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

`faber check .` exits 0. `faber run .` prints `Salve, munde!`.

`faber --help` also lists `faber build . -t rust`, `faber test .`,
`faber format .`, and `faber explain SEM010`.

A second source file is https://faberlang.dev/agents/modules.md.

Fetch list: https://faberlang.dev/agents/index.md
