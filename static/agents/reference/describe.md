# describe

Groups related test cases into a named suite.

**Term** `probandum` · **Section** KEYWORDS · **Also** `describe`, `suite`

## Syntax

```
describe <name> [modifiers] <block>
```

## What this teaches

- Test suite grouping — `describe` organizes related `test` test cases under a descriptive name
- Suites can be nested to create hierarchical test organization

## Common mistakes

- Placing `test` outside a `describe` suite, or forgetting a `tag` modifier on the test case.

## Grammar

```
probandumDecl :← 'probandum' stringLit block
probaDecl     :← 'proba' stringLit block
```

## Expected output

```
No stdout — adfirma cases produce no nota output when run as tests.
BACKEND: No incipit block — test-runner surface; exempla e2e whitelists as
declaration-only (whitelist: probandum/probandum.fab).
```

## Example

```fab
describe "arithmetica" {
    test "unum plus unum" {
        assert 1 + 1 ≡ 2
    }

    test "multiplicatio" {
        assert 3 * 4 ≡ 12
    }

    describe "implicata" {
        test "comparatio" {
            const _ x ← 10
            assert x ≥ 10
        }
    }
}
```

See also: [`test`](test.md), [`assert`](assert.md).

Fetch list: https://faberlang.dev/agents/index.md
