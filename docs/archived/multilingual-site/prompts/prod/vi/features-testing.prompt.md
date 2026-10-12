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

Faber has a first-class testing framework built into the language with three
keywords: `probandum` declares a test suite, `proba` declares a single test
case, and `adfirma` asserts a condition. Tests live in the same file as the
code they test, run through `faber test`, and support the same compiler
pipeline as production code — locale-aware, type-checked, and multi-target.

## The three keywords {#keywords}

| Keyword | Role | Approximate equivalent |
|---------|------|------------------------|
| `probandum` | Declares a named test suite | `describe`, `#[cfg(test)] mod` |
| `proba` | Declares a single test case | `it`, `#[test]` |
| `adfirma` | Asserts a condition at runtime | `assert!`, `assert_eq!` |

### probandum — test suite {#probandum-test-suite}

A `probandum` block groups related test cases. Suites can be nested to
organise tests hierarchically:

<<<FENCE 0>>>

### proba — test case {#proba-test-case}

A `proba` block contains the test logic. It can use any Faber code —
variable bindings, function calls, control flow — and ends with one or more
`adfirma` assertions. Tests can be tagged with an optional `tag` marker for
selective execution:

<<<FENCE 1>>>

### adfirma — assertion {#adfirma-assertion}

`adfirma` evaluates a boolean expression and reports failure if it is false.
An optional message string provides context on failure:

<<<FENCE 2>>>

## Workflow {#workflow}

Tests run through the `faber test` command:

<<<FENCE 3>>>

Because tests live alongside source in the same `.fab` file, there is no
separate test directory structure, no test module declaration, and no build
script distinction between test and production builds. The compiler knows
which blocks are test code and which are production code by the keywords used
— `probandum` and `proba` are parsed but excluded from production builds.

## Real-world example {#real-world}

The coreutils `echo` package demonstrates the testing framework in practice.
Tests live in the same file as the implementation, covering option parsing,
escape expansion, and edge cases:

<<<FENCE 4>>>

## Design notes {#design}

Several design choices distinguish Faber's testing framework from
conventional approaches:

- **No separate test binary.** Tests are declarations in the same source file, not a separate compilation target. The compiler filters test blocks from production output.
- **Tags, not directories.** Tests are organised by `tag` markers rather than directory structure. A test can belong to multiple organisational axes without being moved.
- **Full compiler pipeline.** Tests are type-checked, analysed, and locale-aware — the same `--reader-locale` flag applies to test output.
- **Multi-target.** Tests run through whichever backend the package targets — MIR stepper for `faber test --interpret`, compiled Rust for `faber test`.
- **Nested suites.** `probandum` blocks can nest, mirroring the structure of the code they test.

## References {#references}

1. `examples/corpus/probandum/` — probandum exemplar files
2. `examples/corpus/proba/` — proba exemplar files
3. `examples/corpus/adfirma/` — adfirma exemplar files
4. `examples/coreutils/packages/echo/src/main.fab` — real-world usage with tags
