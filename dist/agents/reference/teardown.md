# teardown

Registers an after-each test hook.

**Term** `postpara` · **Section** KEYWORDS

## Syntax

```
teardown <block>
```

## What this teaches

- Test hooks — `teardown` registers cleanup logic that runs after every test case in a `describe` block.
- Teardown guarantee — The hook runs regardless of whether the test passes or fails.

## Common mistakes

- Confusing `teardown` (teardown) with `setup` (setup) — they run at opposite ends of each test.

## Grammar

```
hookDecl :← 'postpara' block
```

## Expected output

```
No incipit — declaration or test-runner surface only.
```

## Backend

```
declaration-only test hook (whitelist: postpara/postpara.fab).
```

## Example

```fab
describe "hooks" {
    teardown {
        print "after each"
    }
    test "sample" {
        assert true
    }
}
```

See also: [`setup`](setup.md), [`all`](all.md).

Fetch list: https://faberlang.dev/agents/index.md
