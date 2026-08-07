+++
title = "Testing"
section = "cheatsheet"
order = 40
sources = []
+++

Tests are ordinary Faber source. There is no separate test language and no
external runner to configure.

## A single test {#proba}

`proba` declares one test. `adfirma` asserts.

```faber
proba "additio" {
    adfirma 1 + 1 ≡ 2
}
```

## Grouping tests {#probandum}

`probandum` groups related tests under one name.

```faber
probandum "arithmetica" {
    proba "additio" {
        adfirma 1 + 1 ≡ 2
    }

    proba "multiplicatio" {
        adfirma 2 * 3 ≡ 6
    }
}
```

## Tagging {#tags}

`tag` labels a test so it can be selected or filtered when running.

```faber
probandum "textus" {
    proba "concatenatio" tag "fast" {
        adfirma "a" + "b" ≡ "ab"
    }
}
```

## Modifiers {#modifiers}

Modifiers follow the test name.

```faber
probandum "modifiers" {
    proba "stable" tag "fast" {
        adfirma verum
    }

    proba "flaky guard" repete 3 {
        adfirma verum
    }

    proba "not written yet" futurum "waiting on the parser" {
        adfirma verum
    }
}
```

| Modifier | Meaning |
|---|---|
| `tag "<name>"` | Label for selection and filtering |
| `repete <n>` | Run the test *n* times — catches flakiness |
| `futurum "<reason>"` | Expected-pending; documents why it does not run yet |
| `omitte` | Skip |

`repete` is a test modifier, not a loop. For loops see
[Loops](/cheatsheet/loops.html).

## Asserting {#adfirma}

`adfirma` takes any boolean expression.

```faber
probandum "assertiones" {
    proba "comparisons" {
        adfirma 1 + 1 ≡ 2
        adfirma 3 > 2
        adfirma "abc".longitudo() ≡ 3
    }
}
```

## Where tests live, and running them {#running}

Tests sit beside the code they exercise, inside the package. Run them with:

```bash
faber test <package>
```

Related: [Commands](/cheatsheet/commands.html) ·
[Errors and testing](/language/errors.html)
