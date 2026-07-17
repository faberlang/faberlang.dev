---
name: "packages"
description: "Scaffold and drive Faber packages with faber check/build/run/test/format and faber.toml layout."
---

# Faber packages

## Use this skill when

- creating a new Faber package
- running the check/build/test loop
- wiring `faber.toml` and `src/` layout

## Layout

```text
my-package/
  faber.toml
  src/
    main.fab
```

Copy structure from a real package when unsure:

- https://github.com/faberlang/examples/tree/main/ai-workbench
- https://github.com/faberlang/examples/tree/main/vivilite

## Commands

| Command | Purpose |
|---|---|
| `faber check <path>` | Type-check; no emit |
| `faber build <path> -t rust` | Compile (default rust) |
| `faber run <path>` | Build and execute |
| `faber test <path>` | Run proba suites |
| `faber format <path>` | Canonical format |
| `faber explain <code>` | Explain a diagnostic |

## Loop

1. Edit source.
2. `faber check <pkg>` until clean.
3. On errors: `faber explain CODE` and fix source (do not weaken structure).
4. `faber test <pkg>` when suites exist.
5. `faber build <pkg> -t rust` for native output.

## Docs

- https://faberlang.dev/tooling/faber-build-tool.html
- https://faberlang.dev/tooling/radix-compiler.html
- https://faberlang.dev/tooling/codegen-targets.html

## Related

- skill: `install`
- skill: `language`
- skill: `examples`
