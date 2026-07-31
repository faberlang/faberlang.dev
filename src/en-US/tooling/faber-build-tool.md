+++
title = "Faber build tool"
section = "tooling"
order = 1
sources = [
  "faber/README.md",
  "faber/AGENTS.md",
  "faber/src/cli/mod.rs",
  "faber/docs/release/v1.3.0.md",
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
| `faber run <path>` | Build (if needed) and run a compiled package |
| `faber test <path>` | Run proba cases on the MIR stepper |
| `faber format <path>` | Apply canonical formatting (author mode by default) |
| `faber explain <term>` | Explain a glyph, keyword, grammar term, or diagnostic code |
| `faber emit <path>` | Compile to a target surface for stdout |
| `faber targets` | Show supported targets and capability notes |
| `faber init` | Create a new Faber package |
| `faber install` | Install a library package into the Cista store |
| `faber script <path>` | Run Faber source through the interpreter (never compiles to Rust) |
| `faber repl` | Interactive MIR stepper REPL |
| `faber verify <file>` | Run aspect verification on a single file |
| `faber verify-library <input>` | Verify a library package's target binding manifest |
| `faber model inspect <path>` | Inspect model-file metadata (safetensors) |
| `faber lex` / `parse` / `hir` / `mir` / `cli-ir` | JSON phase dumps (compatibility aliases for `radix <phase>`) |
| `faber host manifest` | Script host introspection (kernel manifest) |

## Building a package {#building}

```text
faber build my-package/ -t rust
```

The `-t` flag selects the codegen target: `rust` (default), `typescript`
(`ts`), `go`, `swift`, `faber` (`fab`, canonical re-emission), `wasm` /
`wasm-text` (`wat`), `llvm-text` (`llvm`), `metal-text` (`metal`),
`wgsl-text` (`wgsl`), and `sexp` (`racket`). Diagnostics can be promoted to
errors with `--deny-warnings` (all warnings) or `--deny <CODE>` (a specific
catalog code, repeatable).

## Checking without emitting {#checking}

```text
faber check my-package/
```

Runs the full front end (lex → parse → typecheck → MIR lowering) without
producing output artifacts. Use this in CI and editor integrations.

## Running tests {#testing-command}

```text
faber test my-package/
faber test . --filter smoke       # substring filter on case path or title
faber test . --include math       # load only *.proba sources matching a path pattern
faber test . --exclude 'nested/*' # skip *.proba sources matching a path pattern
faber test . --name my_case       # select by proba name
faber test . --suite suite/path   # select by probandum suite path
faber test . --tag slow           # select by tag modifier
```

`faber test` runs proba cases on the MIR stepper — no Cargo or rustc is
invoked for the package, so no Rust toolchain is needed. Inline `probandum`
and `proba` suites live alongside source code, and colocated `*.proba`
files are discovered as test-only sources (never imported, excluded from
Cista snapshots). See [Inline testing](/features/testing.html).

## Formatting {#formatting}

```text
faber format my-package/
```

Applies the canonical Faber formatter in author mode by default. The
formatter enforces consistent layout: one declaration per line, canonical
spacing, and standardized keyword surfaces. `--canonical` selects the
canonical re-emit path, `--check` verifies without writing, and
`--reader-locale` formats for a reader pack.

## Explaining diagnostics {#explaining}

```text
faber explain functio     # keyword reference
faber explain SEM001      # diagnostic explanation
faber explain ≡           # glyph reference
faber explain --search query
```

`faber explain` explains a Faber glyph, keyword, or grammar term, with
diagnostic codes as a subset. It reads from the language corpus
(`radix/corpus/`).
