+++
title = "Faber build tool"
section = "tooling"
order = 1
sources = [
  "faber/README.md",
  "faber/AGENTS.md",
]
+++

The `faber` CLI is the primary entry point for building, checking, running,
formatting, and testing Faber source. It wraps the Radix compiler into an
ergonomic developer tool.

## Core commands {#core-commands}

| Command | Purpose |
|---|---|
| `faber build <path>` | Compile a package to a target backend (default: Rust) |
| `faber check <path>` | Type-check without emitting code |
| `faber run <path>` | Build and execute |
| `faber test <path>` | Run proba test suites |
| `faber format <path>` | Apply canonical formatting |
| `faber explain <code>` | Explain a diagnostic code |
| `faber emit <path>` | Emit source in a target surface |

## Building a package {#building}

```text
faber build my-package/ -t rust
```

The `-t` flag selects the codegen target. Supported targets include `rust`
(default), `wasm`, `typescript`, and `go`.

## Checking without emitting {#checking}

```text
faber check my-package/
```

Runs the full front end (lex → parse → typecheck → MIR lowering) without
producing output artifacts. Use this in CI and editor integrations.

## Running tests {#testing-command}

```text
faber test my-package/
```

Compiles all `probandum` suites in the package to Rust `#[test]` functions
and runs them via Cargo. Inline tests live alongside source code — no
separate test binary is needed.

## Formatting {#formatting}

```text
faber format my-package/
```

Applies the canonical Faber formatter. The formatter enforces consistent
layout: one declaration per line, canonical spacing, and standardized
keyword surfaces.

## Explaining diagnostics {#explaining}

```text
faber explain SEM001
```

Prints a human-readable explanation of any diagnostic code the compiler
can emit. Useful for learning what an error means and how to fix it.
