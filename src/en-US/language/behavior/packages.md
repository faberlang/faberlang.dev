+++
title = "A program is a package"
section = "language"
order = 14
sources = [
  "cista/README.md",
]
+++

Faber has no bare source file as its unit. A program is a **package**: a
`faber.toml` manifest and a source tree, compiled as one analyzed whole. The
manifest names the package, points at the entry module, and selects the target;
the entry module declares `main`, and that is where the program starts.

Making the package the unit has a consequence a reader can rely on: the
compiler always sees the whole program. Imports resolve against real files, and
nothing depends on the order in which a shell happened to pass arguments.
Names are brought in explicitly — `import from "./math" duplica` imports exactly
`duplica`, and `public` re-exports it when the widening is deliberate.

## Module scope is compile-time {#module-scope}

A top-level binding is a compile-time constant. `const LIMIT = 255` at module
scope is known while compiling; **module-level mutable state does not exist**.
Runtime state starts at `main` and lives in functions. This is the glyph law
extended to the module: `=` at the top level is a fact, not an initialization
that runs. Because the top level holds no state, a package can be analyzed,
checked, emitted, or tested without running any of it — which is what lets one
package target many backends.

```toml
faber.toml

[package]
name = "demo"
version = "0.1.0"
edition = "2026"

[paths]
source = "src"
entry = "main.fab"

[build]
kind = "bin"
target = "rust"

[locale]
locale = "en"
```

```faber
functio duplica(numerus n) → numerus {
    redde n * 2
}

incipit {
    nota duplica(21)
}
```

```text
$ faber run
42
```

A mutable binding at module scope is rejected, because there is no run time for
it to belong to:

```faber outcome=rejects
varia numerus counter ← 0
```

See [Packages with Cista](/toolchain/packages.html) for resolution and the
[command line](/toolchain/cli.html) for `faber check`, `faber run` and
`faber test`.
