+++
title = "Errors as values, tests as declarations"
section = "language"
order = 15
sources = [
  "radix/docs/design/failable-conversio.md",
  "radix/corpus/iace/",
  "radix/corpus/fac/",
  "radix/corpus/proba/",
]
+++

Faber keeps failure in the type system instead of in an exception runtime.
Three ideas that many languages collapse into one are written differently:

| Construct | Meaning |
|---|---|
| `→ T` | the normal success channel |
| `T ∪ none` | absence inside the success value domain |
| `⇥ E` | a recoverable alternate exit — the error channel |

A function that can fail declares the second channel after the arrow. It does
not return a wrapper type the caller must unwrap; it returns its value by `→`
and throws by `⇥`. `throw` sends a value on the channel, and the guards
`require` / `reject` are the one-line forms: `require cond throw err` throws
when the condition fails, and `reject` is its boolean opposite. Callers recover
locally with a `do` / `catch` pair, so a failure stays visible at the call site
rather than travelling up an invisible stack.

## What it looks like {#shape}

A fallible division, and two callers — one that succeeds, one that catches:

```faber
functio divide(numerus a, numerus b) → numerus ⇥ textus {
    requirit b ≢ 0 iace "division by zero"
    redde a / b
}

incipit {
    fac {
        nota divide(10, 2)
    }
    cape err {
        nota err
    }
    fac {
        nota divide(1, 0)
    }
    cape err {
        nota err
    }
}
```

```text
$ faber run
5
division by zero
```

Nothing throws past the caller: the error value binds as `err` and the program
keeps going. The compiler knows which call sites can fail, because the `⇥`
channel is part of the function's type.

## Tests are declarations {#testing}

The same "make it explicit" stance applies to tests. There is no separate test
binary and no test module tree. Three keywords declare tests in the same file
as the code — or in colocated `*.proba` sources — and `faber test` runs them on
the MIR stepper, with no Cargo or rustc involved:

| Keyword | Role |
|---|---|
| `describe` | a named test suite, nestable |
| `test` | one test case |
| `assert` | an assertion that must hold |

```faber
functio saturate(numerus x) → numerus {
    si x < 0 ergo redde 0
    si x > 255 ergo redde 255
    redde x
}

probandum "saturate" {
    proba "clamps low" {
        adfirma saturate(-1) ≡ 0
    }
    proba "clamps high" {
        adfirma saturate(300) ≡ 255
    }
}
```

```text
$ faber test .
ok   src/main.fab::saturate/clamps low (0 ms)
ok   src/main.fab::saturate/clamps high (0 ms)
test result: ok. 2 passed; 0 failed; 0 blocked; 0 skipped
```

*(The transcript shortens each case's path to the package root.)*

Tests are type-checked and analysed by the same front end as production code,
and the test blocks are filtered out of a production build. Because the runner
is the stepper, a suite is target-neutral: the same tests run whatever backend
the package is emitted for.

The full treatment — async error channels, inline conversion defaults, the
`faber test` flags — is in [Errors and testing](/language/errors.html).
