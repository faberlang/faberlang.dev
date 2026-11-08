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

```faber locale-tabs
proba "additio" {
    adfirma 1 + 1 ≡ 2
}
```

## Grouping tests {#probandum}

`probandum` groups related tests under one name.

```faber locale-tabs mode=pinned
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

```faber locale-tabs mode=pinned
probandum "textus" {
    proba "concatenatio" tag "fast" {
        adfirma "a" + "b" ≡ "ab"
    }
}
```

## Modifiers {#modifiers}

Modifiers follow the test name.

```faber locale-tabs mode=pinned
probandum "modifiers" {
    proba "stable" tag "fast" {
        adfirma verum
    }

    proba "every run" repete 3 {
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
| `repete <n>` | Run the test *n* times; it passes only if every run passes |
| `fragilis <n>` | Rejected by `faber test`: flaky retries are not run, so the case fails without running its body |
| `futurum "<reason>"` | Expected-pending; documents why it does not run yet |
| `omitte` | Skip |

`repete` is a test modifier, not a loop, and it does not retry until a run
passes. For loops see
[Loops](/cheatsheet/loops.html).

## Asserting {#adfirma}

`adfirma` takes any boolean expression.

```faber locale-tabs mode=pinned
probandum "assertiones" {
    proba "comparisons" {
        adfirma 1 + 1 ≡ 2
        adfirma 3 ≻ 2
        adfirma "abc".longitudo() ≡ 3
    }
}
```

## Tests in the program's own file {#sections}

Since 1.19 a source file can carry its tests, and the output a run should
print, in sections after its program. Each section starts with a whole-line
marker: `+++ toml` for the header, `+++ faber` for the program, `+++ faber
test` for the tests, and `+++ text stdout` (or `stdin`, `stderr`; also `json`,
`jsonl`, `base64`) for streams. A section runs to the next marker.

```text
+++ toml
locale = "en"

+++ faber
@ public
fn double(int x) → int {
    return x * 2
}

main {
    print double(21)
}

+++ faber test
test "doubles" {
    assert double(21) ≡ 42
}

+++ text stdout
42
```

The test section sees the program's `@ public` items, as a sibling file would.
`check`, `run` and `build` compile only the program section; `faber test`
runs the test section, and `faber corpus` compares the program's output with
the stream sections. A file with only a `+++ faber test` section is a test-only
file that `faber test` runs and `faber run` refuses.

## Where tests live, and running them {#running}

Tests sit beside the code they exercise, inside the package. Run them with:

```bash
faber test <package>
```

Related: [Commands](/cheatsheet/commands.html) ·
[Errors and testing](/language/errors.html)
