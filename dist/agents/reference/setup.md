# setup

Registers a before-each test hook.

**Term** `praepara` · **Section** KEYWORDS

## Syntax

```
setup <block>
```

## What this teaches

- Testing setup hooks — `setup` registers a block that runs before each test case (`test`) in the suite, ensuring shared state or side effects are prepared
- Works with `teardown` (after-each) for paired setup/teardown

## Common mistakes

- Confusing `setup` (setup) with `teardown` (teardown) — they run at opposite ends of each test.

## Grammar

```
hookDecl :← 'praepara' block
```

## Expected output

```
No incipit — declaration or test-runner surface only.
```

## Backend

```
declaration-only test hook (whitelist: praepara/praepara.fab).
```

## Example

```fab
describe "hooks" {
    setup {
        print "before each"
    }
    test "sample" {
        assert true
    }
}
```

See also: [`teardown`](teardown.md), [`all`](all.md).

Fetch list: https://faberlang.dev/agents/index.md
