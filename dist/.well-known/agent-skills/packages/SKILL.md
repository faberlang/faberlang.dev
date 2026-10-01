---
name: "packages"
description: "Scaffold and drive Faber packages with the faber init manifest and faber check, build, run, test, and format."
---

# Faber packages

## Use this skill when

- creating a new Faber package
- running the check loop
- wiring `faber.toml` and `src/`

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
