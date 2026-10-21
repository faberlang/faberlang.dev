# Modules

A second source file is imported by its path. `greet.fab` marks `saluta`
with `@ public`. `main.fab` imports that file and calls it.

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

`src/greet.fab`:

```faber locale=en
@ public
fn saluta(string nomen) → string {
    return "Salve, §!"(nomen)
}
```

`src/main.fab`:

```faber locale=en mode=package
import from "./greet" greet

main {
    print greet.saluta("Marcus")
}
```

`faber check .` exits 0 and warns `WARN003` on `saluta`. `faber run .`
prints `Salve, Marcus!`.

A target word in place of `from` imports a module of that target language,
by its own name: `import python "math" m`. The program then builds only for
that target (`faber build -t python`); `faber check`, `faber run` and every
other target refuse it with `SEM017` `import_target_bound`.

Fetch list: https://faberlang.dev/agents/index.md
