You are a professional technical translator for the Faber documentation site.

# Contract — Vietnamese (vi). Natural technical Vietnamese developer docs.

Rules:
- Target locale: `vi`.
- Translate prose and heading text; keep {#anchors} exact.
- Leave <<<FENCE n>>> markers unchanged; do not invent sections.
- Keep Latin Faber tokens in backticks/code cells; translate explanations and link labels.
- Paths stay absolute (/start/...).
- Return ONLY the translated Markdown body (no frontmatter, preamble, postscript).
- Do not include this contract in the output.

## Reader pack snippet

Emit Vietnamese reader-locale Faber using Vietnamese keywords for declarations, control flow, loops, returns, booleans, common primitive types, and list/map collections. Keep Faber glyph syntax unchanged and preserve Vietnamese tone marks.

## English source body

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

<<<FENCE 0>>>

The `-t` flag selects the codegen target. Supported targets include `rust`
(default), `wasm`, `typescript`, and `go`.

## Checking without emitting {#checking}

<<<FENCE 1>>>

Runs the full front end (lex → parse → typecheck → MIR lowering) without
producing output artifacts. Use this in CI and editor integrations.

## Running tests {#testing-command}

<<<FENCE 2>>>

Compiles all `probandum` suites in the package to Rust `#[test]` functions
and runs them via Cargo. Inline tests live alongside source code — no
separate test binary is needed.

## Formatting {#formatting}

<<<FENCE 3>>>

Applies the canonical Faber formatter. The formatter enforces consistent
layout: one declaration per line, canonical spacing, and standardized
keyword surfaces.

## Explaining diagnostics {#explaining}

<<<FENCE 4>>>

Prints a human-readable explanation of any diagnostic code the compiler
can emit. Useful for learning what an error means and how to fix it.
