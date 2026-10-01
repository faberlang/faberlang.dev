# void

Primitive no-value return type.

**Term** `vacuum` · **Section** KEYWORDS · **Also** `void`, `unit`

## Syntax

```
void
```

## What this teaches

- Void return — `void` for functions that produce no value
- Side-effect functions — functions returning `void` execute for their side effects like `print`

## Common mistakes

- confusing void (void return type) with empty (empty collection initializer) or none (null singleton)

## Grammar

```
returnType :← 'vacuum'
```

## Expected output

```
Scalar stdout smoke (see body).
```

## Example

```fab
fn log(string message) → void {
    print message
}

main {
    log("void smoke")
}
```

See also: [`fn`](fn.md), [`return`](return.md).

Fetch list: https://faberlang.dev/agents/index.md
