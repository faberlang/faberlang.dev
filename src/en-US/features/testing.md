+++
title = "Inline testing"
section = "features"
order = 7
sources = []
+++

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

```faber
probandum "arithmetica" {
    proba "unum plus unum" {
        adfirma 1 + 1 ≡ 2
    }

    proba "multiplicatio" {
        adfirma 3 * 4 ≡ 12
    }

    probandum "implicata" {
        proba "comparatio" {
            fixum _ x ← 10
            adfirma x ≥ 10
        }
    }
}
```

### proba — test case {#proba-test-case}

A `proba` block contains the test logic. It can use any Faber code —
variable bindings, function calls, control flow — and ends with one or more
`adfirma` assertions. Tests can be tagged with an optional `tag` marker for
selective execution:

```text
proba "echo formats operands with one space" tag "coreutils" {
    adfirma echo_textus(["hello", "world"]) ≡ "hello world"
}
```

### adfirma — assertion {#adfirma-assertion}

`adfirma` evaluates a boolean expression and reports failure if it is false.
An optional message string provides context on failure:

```faber
incipit {
    fixum _ x ← 10

    # Simple assertion
    adfirma x > 0

    # With custom message
    adfirma x ≡ 10, "x decem esse debet"

    # Multiple assertions in sequence
    fixum _ nomen ← "Marcus"
    adfirma nomen ≡ "Marcus"
    adfirma nomen ≠ "", "nomen vacuum non sit"
}
```

## Workflow {#workflow}

Tests run through the `faber test` command:

```text
faber test                        # run all tests in the current package
faber test examples/coreutils/packages/echo  # run tests for a specific package
```

Because tests live alongside source in the same `.fab` file, there is no
separate test directory structure, no test module declaration, and no build
script distinction between test and production builds. The compiler knows
which blocks are test code and which are production code by the keywords used
— `probandum` and `proba` are parsed but excluded from production builds.

## Real-world example {#real-world}

The coreutils `echo` package demonstrates the testing framework in practice.
Tests live in the same file as the implementation, covering option parsing,
escape expansion, and edge cases:

```text
probandum "echo formatting" tag "coreutils" {
    proba "empty operands format as empty text" {
        fixum lista<textus> words ← vacua
        adfirma echo_textus(words) ≡ ""
    }

    proba "single operand is unchanged" {
        adfirma echo_textus(["hello"]) ≡ "hello"
    }

    proba "-E is a leading no-op option" {
        adfirma echo_textus(["-E", "hello", "world"]) ≡ "hello world"
    }

    proba "-n suppresses the trailing newline flag" {
        adfirma echo_novam_lineam(["-n", "hello"]) ≡ falsum
    }

    proba "-e expands the declared escape subset" {
        adfirma echo_textus(["-e", "a\\nb"]) ≡ "a\nb"
        adfirma echo_textus(["-e", "a\\tb"]) ≡ "a\tb"
    }
}
```

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
