# batch

do batch defers recoverable kernel errors to its owning catch.

**Term** `batch` · **Section** KEYWORDS

## Syntax

```
do batch <block> catch <name> <block>
```

## Example

```fab
fn attempt(bool fail) → int {
    do batch {
        if fail {
            throw "case"
        }
        return 1
    } catch err {
        return 0
    }
}

main {
    print attempt(false)
    print attempt(true)
    do batch {
        print "planum"
    } catch err {
        print "interceptum"
    }
}
```

Fetch list: https://faberlang.dev/agents/index.md
