## System prompt snippet (reader pack)

Emit Arabic reader-locale Faber using Arabic keywords for declarations, control flow, loops, returns, booleans, common primitive types, and list/map collections. Keep Faber glyph syntax unchanged and keep source in logical order.

## Instructions

Translate the prose below from English to the target locale. Follow these rules:

- Translate prose only. Do NOT translate code fences.
- Preserve {#anchors} (heading anchors) exactly.
- Preserve markdown structure (headings, paragraphs, lists).
- Preserve table shapes (column count, alignment).
- Preserve links. Paths may stay absolute (/start/...) since the generator prefixes locale paths.
- Fences are shown as "<<<FENCE n>>>" markers. Leave these markers unchanged in your output.
- Return the full body text with markers in place.

## English source body (fences as <<<FENCE n>>>)

This page is the practical CLI map for the first week of Faber work. Use it as
a command index, then open the detailed [Faber build tool](/tooling/faber-build-tool.html)
page when you need flags and compiler pipeline details.

## Daily loop {#daily-loop}

| Command | Use it for |
|---|---|
| `faber check <package>` | Fast front-end validation: lex, parse, type check, lower |
| `faber build <package> -t rust` | Emit a Rust project for review or native compilation |
| `faber run <package>` | Build and execute an application package |
| `faber test <package>` | Run package tests when the package defines test surfaces |
| `faber explain <code>` | Read a stable diagnostic explanation |

Start with `check`. It is the cheapest command and the one agents should run
before proposing generated code as valid Faber.

## Check {#check}

<<<FENCE 0>>>

A passing check means the package is syntactically and semantically acceptable
to the compiler front end. It does not mean the final native toolchain has been
invoked.

## Build {#build}

<<<FENCE 1>>>

The Rust target is intentionally reviewable. Generated Rust is a compiler
artifact, not source of truth; edit the Faber package and rebuild rather than
patching emitted Rust by hand.

## Run {#run}

<<<FENCE 2>>>

Use `run` for application packages with an `incipit` entry point. Library-only
packages should be checked and tested instead.

## Explain diagnostics {#explain}

<<<FENCE 3>>>

Diagnostic families are stable handles: `LEX` for lexical errors, `PAR` for
parser errors, `SEM` for semantic/type errors. In docs and agent reports, cite
the diagnostic code instead of paraphrasing a compiler failure loosely.

## Reader-locale commands {#reader-locale}

<<<FENCE 4>>>

Reader locale output is a rendering of the compiler's semantic model, not a
browser-time translation layer. Locale work belongs after a package checks in
canonical form.

## Next {#next}

| Previous | Next |
|---|---|
| [Hello, Faber](/start/hello.html) | [Projects and examples](/start/projects.html) |
