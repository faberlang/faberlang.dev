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
    si x ≺ 0 ergo redde 0
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
    si value ≺ 0 ergo iace "negative value"
}
```

### Guards — requirit / reice {#guards--requirit--reice}

Guard statements pair a condition with a throw in one line. `requirit`
(English reader spelling `require`) throws when the condition **fails** —
it demands that the condition hold:

```faber
functio divide(numerus a, numerus b) → numerus ⇥ textus {
    requirit b ≢ 0 iace "division by zero"
    redde a / b
}
```

`reice` (English reader spelling `reject`) is its boolean opposite: it
throws when the condition **holds**. Read it as an early rejection — the
happy path is whatever the condition rules out:

```faber
functio exigePositivum(numerus value) → numerus ⇥ textus {
    reice value ≺ 0 iace "negative value"
    redde value
}
```

Both compile to the same shape as an `si` around `iace` — `reice cond
iace err` is exactly `si cond { iace err }` — and, like `iace` itself,
they require the enclosing function to declare a `⇥` channel.

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

`⊥` specifies an inline default value on `↦` conversions (`⇥` only ever names
an error type):

```faber
incipit {
    sit textus raw ← "42"
    sit _ n ← raw ↦ numerus ⊥ 0
}
```

### Effect-only failable {#effectonly-failable}

For functions that error but do not return a success value, omit `→ T`:

```faber
functio exigePositivum(numerus value) ⇥ textus {
    si value ≺ 0 ergo iace "negative value"
}
```

### Fault unions {#fault-unions}

The type after `⇥` is not limited to `textus`. Norma's I/O functions fail with
a union: `fs.read_file<T>(path)` is `→ T ⇥ fault.IoFault`, and `IoFault` has one
variant per kind of failure (`NotFound`, `Permission`, `IsADirectory`, and so
on), each carrying the path it failed on. A `cape` binding of that type is
matched with `discerne`:

```faber locale=en
import from "norma:fs" fs

fn read_or_empty(string path) → string {
    do {
        return fs.read_file<string>(path)
    } catch err {
        match err {
            case NotFound let missing {
                print "no such file: §"(missing)
                return ""
            }
            case Permission let denied {
                print "not allowed: §"(denied)
                return ""
            }
            default {
                print "I/O failure"
                return ""
            }
        }
    }
}

main {
    print "read: [§]"(read_or_empty("/no/such/file.txt"))
}
```

```text
$ faber run
no such file: /no/such/file.txt
read: []
```

### Current status {#current-status}

`→`, `redde`, `⇥`, `iace`, and `fac` / `cape` are live grammar and checker
surfaces, and `faber run` executes them. Rust lowers a failable function to a
`Result<T, E>` and handles `fac` / `cape` around it. Go and TypeScript lowering
is partial: Go reports `CODEGEN001 go_structured_cape_handlers_unsupported` for
some `cape` shapes, and the corpus suite pins the remaining failable-call gaps
on those targets as known failures. Check a program with `faber emit -t <target>`
before relying on a target other than Rust.

## Inline testing

Faber has a first-class testing framework built into the language with three
keywords: `probandum` declares a test suite, `proba` declares a single test
case, and `adfirma` asserts a condition. Tests live alongside the code they
test — either in the same `.fab` file or in colocated `*.proba` test-source
files — run through `faber test` on the MIR runner, and support the same
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

```faber mode=pinned
probandum "arithmetica" {
    proba "unum plus unum" {
        adfirma 1 + 1 ≡ 2
    }

    proba "multiplicatio" {
        adfirma 3 * 4 ≡ 12
    }

    probandum "implicata" {
        proba "comparatio" {
            sit _ x ← 10
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
    sit _ x ← 10

    # Simple assertion
    adfirma x ≻ 0

    # With custom message
    adfirma x ≡ 10 mori "x decem esse debet"

    # Multiple assertions in sequence
    sit _ nomen ← "Marcus"
    adfirma nomen ≡ "Marcus"
    adfirma nomen ≢ "" mori "nomen vacuum non sit"
}
```

### Workflow {#workflow}

Tests run through the `faber test` command, which executes proba cases on
the MIR runner — no Cargo or rustc is invoked for the package:

```text
faber test                        # run all tests in the current package
faber test path/to/package        # run tests for a specific package
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
        sit lista<textus> words ← vacua
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
- **Full compiler pipeline.** Tests are type-checked, analysed, and locale-aware — the same `--locale` code-locale flag applies.
- **Runner-executed.** `faber test` runs proba cases on the MIR runner; no generated test crate, Cargo, or Rust toolchain is required.
- **Target-neutral.** The runner analysis is independent of any codegen target.
- **Nested suites.** `probandum` blocks can nest, mirroring the structure of the code they test.

### References {#references}

1. `radix/corpus/probandum/` — probandum exemplar files
2. `radix/corpus/proba/` — proba exemplar files
3. `radix/corpus/adfirma/` — adfirma exemplar files
