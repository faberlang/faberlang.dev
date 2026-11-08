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
    let string msg ← "Salve, §!"(nomen)
    return msg
}

main {
    let string m ← salve("munde")
    print m
}
```

```bash
faber check .
```

`faber check .` exits 0. It is lexing, parsing, and type checking. It does
not build a native binary. `faber run .` prints `Salve, munde!`.

A source file may also carry its own tests and expected output after the
program, each part under a whole-line marker. `check`, `run` and `build` read
only the program section; `faber test .` runs the `+++ faber test` section,
which sees the program's `@ public` items.

```text
+++ toml
locale = "en"

+++ faber
@ public
fn double(int x) → int {
    return x * 2
}

main {
    print double(21)
}

+++ faber test
test "doubles" {
    assert double(21) ≡ 42
}

+++ text stdout
42
```

Next: https://faberlang.dev/agents/functions.md
