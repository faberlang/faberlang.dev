# never

Primitive never type for code paths that do not return normally.

**Term** `numquam` · **Section** KEYWORDS · **Also** `never`

## Syntax

```
never
```

## What this teaches

- Diverging functions — `never` marks functions like `panic` that never return to the caller.
- Type-system bottom — `never` is the bottom type, compatible with any return position.

## Common mistakes

- Using never for functions that might sometimes return normally — never is only for code paths that never return.

## Grammar

```
returnType :← 'numquam'
```

## Expected output

```
Scalar stdout smoke (see body).
```

## Backend

```
Cross-ref: mori/mori.fab.
```

## Example

```fab
fn fail(string message) → never {
    panic message
}
```

See also: [`panic`](panic.md), [`exit`](exit.md).

Fetch list: https://faberlang.dev/agents/index.md
