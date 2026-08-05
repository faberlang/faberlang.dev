+++
title = "Errors and testing"
section = "language"
order = 4
sources = [
  "radix/README.md (Return and Error Channels)",
  "radix/corpus/iace/",
  "radix/corpus/fac/",
  "radix/corpus/cape/",
  "radix/docs/design/failable-conversio.md",
]
+++

## Error handling

Faber separates three related ideas that many languages collapse into one
shape:

| Construct | Meaning |
|-----------|---------|
| `→ T` | Normal success return channel |
| `T ∪ nihil` | Absence in the success value domain |
| `⇥ E` | Recoverable alternate-exit channel for errors |

### Normal return {#normal-return}

```faber
functio porta(numerus x) → numerus {
    si x < 0 ergo redde 0
    redde x * 2
}
```

### Failable functions {#failable-functions}

Use `⇥` when a function can leave by an error channel:

```faber
functio divide(numerus a, numerus b) → numerus ⇥ textus {
    si b ≡ 0 ergo iace "division by zero"
    redde a / b
}
```

### Throwing — iace {#throwing--iace}

`iace` sends a value on the error channel:

```faber
functio exigePositivum(numerus value) ⇥ textus {
    si value < 0 ergo iace "negative value"
}
```

### Recovery — fac / cape {#recovery--fac--cape}

Callers recover locally with a `fac` block and a `cape` handler:

```faber
functio divide(numerus a, numerus b) → numerus {
    si b ≡ 0 {
        redde 0
    }
    redde a / b
}

functio tutum(numerus a, numerus b) → numerus {
    fac {
        redde divide(a, b)
    }
    cape err {
        mone err
        redde 0
    }
}
```

A direct failable call is not an ordinary expression. Place calls to
`→ T ⇥ E` functions inside an active `fac` / `cape` boundary.

### The alternate channel in async surfaces {#async-alternate}

The same `⇥ E` channel rides *inside* Faber's async types rather than as a
separate mechanism. A `fiet` function returns `promissum<T>` — the
infallible shorthand for `promissum<T ⇥ numquam>` — and `promissum<T ⇥ E>`
preserves the delayed alternate alongside the eventual value. Awaiting a
failable promise is itself a failable operation: the success value binds
inside a `fac` / `cape` boundary while the failure stays observable, exactly
like a failable sync call.

Async and sync streams carry the channel too: `fient → T ⇥ E` makes every
pull a promise that can yield, end, or fail (the first failure ends the
stream, handled by `itera ex`); `fiunt → T ⇥ E` makes the stream call itself
failable, recovered with `fac` / `cape`.

See [Functions — two-channel promises](/language/functions.html#two-channel-promises)
for the full treatment.

### Inline conversion recovery {#inline-conversion-recovery}

`⇥` can also specify an inline recovery value on `↦` conversions:

```faber
fixum textus raw ← "42"
fixum _ n ← raw ↦ numerus ⇥ 0
```

### Effect-only failable {#effectonly-failable}

For functions that error but do not return a success value, omit `→ T`:

```faber
functio exigePositivum(numerus value) ⇥ textus {
    si value < 0 ergo iace "negative value"
}
```

### Current status {#current-status}

`→`, `redde`, `⇥`, `iace`, and `fac` / `cape` are live grammar and checker
surfaces. Rust and Go lowering for full `⇥` / `iace` / `cape` runtime
behaviour is still a backend gap — these pass type-checking but do not
yet emit failable runtime code to all targets.

## Inline testing

Faber has a first-class testing framework built into the language with three
keywords: `probandum` declares a test suite, `proba` declares a single test
case, and `adfirma` asserts a condition. Tests live alongside the code they
test — either in the same `.fab` file or in colocated `*.proba` test-source
files — run through `faber test` on the MIR stepper, and support the same
compiler pipeline as production code: locale-aware, type-checked, and
target-neutral.

### The three keywords {#keywords}

| Keyword | Role | Approximate equivalent |
|---------|------|------------------------|
| `probandum` | Declares a named test suite | `describe`, `#[cfg(test)] mod` |
| `proba` | Declares a single test case | `it`, `#[test]` |
| `adfirma` | Asserts a condition at runtime | `assert!`, `assert_eq!` |

#### probandum — test suite {#probandum-test-suite}

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

#### proba — test case {#proba-test-case}

A `proba` block contains the test logic. It can use any Faber code —
variable bindings, function calls, control flow — and ends with one or more
`adfirma` assertions. Tests can be tagged with an optional `tag` marker for
selective execution:

```text
proba "echo formats operands with one space" tag "coreutils" {
    adfirma echo_textus(["hello", "world"]) ≡ "hello world"
}
```

#### adfirma — assertion {#adfirma-assertion}

`adfirma` evaluates a boolean expression and reports failure if it is false.
An optional message string provides context on failure:

```faber
incipit {
    fixum _ x ← 10

    # Simple assertion
    adfirma x > 0

    # With custom message
    adfirma x ≡ 10 secus "x decem esse debet"

    # Multiple assertions in sequence
    fixum _ nomen ← "Marcus"
    adfirma nomen ≡ "Marcus"
    adfirma nomen ≠ "" secus "nomen vacuum non sit"
}
```

### Workflow {#workflow}

Tests run through the `faber test` command, which executes proba cases on
the MIR stepper — no Cargo or rustc is invoked for the package:

```text
faber test                        # run all tests in the current package
faber test examples/coreutils/packages/echo  # run tests for a specific package
faber test . --filter smoke       # substring filter on case path or title
faber test . --include math       # load only *.proba sources matching a path pattern
faber test . --exclude 'nested/*' # skip *.proba sources matching a path pattern
faber test . --name my_case       # select by proba name
faber test . --suite suite/path   # select by probandum suite path
faber test . --tag slow           # select by tag modifier
```

Tests can live in the same `.fab` file as the code they test, or in
colocated `*.proba` files (the preferred home for stdlib and public-contract
suites). `.proba` files are test-only: discovered only by `faber test`,
never importable from product modules, and excluded from Cista package
snapshots. There is no separate test directory structure and no test module
declaration. The compiler knows which blocks are test code and which are
production code by the keywords used — `probandum` and `proba` are parsed but
excluded from production builds.

Warnings can be promoted to errors with `--deny-warnings` or
`--deny <CODE>` (repeatable), on `faber test` and `faber build` alike.

### Real-world example {#real-world}

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

### Design notes {#design}

Several design choices distinguish Faber's testing framework from
conventional approaches:

- **No separate test binary.** Tests are declarations in the same source file (or in `*.proba` test sources), not a separate compilation target. The compiler filters test blocks from production output.
- **Tags, not directories.** Tests are organised by `tag` markers rather than directory structure. A test can belong to multiple organisational axes without being moved.
- **Full compiler pipeline.** Tests are type-checked, analysed, and locale-aware — the same `--locale` flag applies to test output.
- **Stepper-executed.** `faber test` runs proba cases on the MIR stepper; no generated test crate, Cargo, or Rust toolchain is required.
- **Target-neutral.** The stepper analysis is independent of any codegen target.
- **Nested suites.** `probandum` blocks can nest, mirroring the structure of the code they test.

### References {#references}

1. `radix/corpus/probandum/` — probandum exemplar files
2. `radix/corpus/proba/` — proba exemplar files
3. `radix/corpus/adfirma/` — adfirma exemplar files
4. `examples/coreutils/packages/echo/src/main.fab` — real-world usage with tags
