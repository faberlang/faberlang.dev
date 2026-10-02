---
name: "packages"
description: "Scaffold and drive Faber packages with the faber init manifest and faber check, build, run, test, and format."
---

# Faber packages

## Use this skill when

- creating a new Faber package
- running the check loop
- wiring `faber.toml` and `src/`

## Scaffold and prove it

Write the smallest useful program: a package entry point that formats a
string and prints it.

```bash
faber init hello
```

`faber init` writes `faber.toml` and a starter `src/main.fab`. Replace
`src/main.fab` with this English-spelling program:

```faber locale=en
fn greet(string name) → string {
    const string msg ← "Hello, §!"(name)
    return msg
}

main {
    const string m ← greet("world")
    print m
}
```

```bash
faber check hello
faber run hello
```

`faber check` runs the front end: lexing, parsing, and type checking, far
enough to catch ordinary package mistakes without building a native binary.
`faber run` interprets the package and prints `Hello, world!`. When a check
fails, read the diagnostic code first. Codes are stable search handles:
`faber explain <CODE>` prints the entry.

One file uses one reader locale. The program above is the English surface.
See https://faberlang.dev/agents/locales.md before writing any other.

## Layout

`faber init` writes this manifest. The canon package name is `salve-munde`.

```text
salve-munde/
  faber.toml
  src/
    main.fab
```

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

A second source file is imported by path. See the modules page.

Libraries (`norma:*` and the others) resolve from the Cista package store
recorded in `faber.lock`. Set `FABER_LIBRARY_HOME` only for an intentional
local library-development override.

## Commands

| Command | Purpose |
|---|---|
| `faber check .` | Type-check. Exits 0 on the canon package. |
| `faber run .` | Interpret. Prints `Salve, munde!` for that package. |
| `faber build . -t rust` | Compile. Listed by `faber --help`. |
| `faber test .` | Run proba suites. Listed by `faber --help`. |
| `faber format .` | Format source. Listed by `faber --help`. |
| `faber explain SEM010` | Explain a diagnostic. |

## Docs

- https://faberlang.dev/agents/packages.md
- https://faberlang.dev/agents/program.md
- https://faberlang.dev/agents/modules.md
- https://faberlang.dev/agents/check.md

## Related

- skill: `install`
- skill: `language`
- skill: `examples`
