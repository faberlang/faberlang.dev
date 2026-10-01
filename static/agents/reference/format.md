# format

Creates a formatted string with `§` placeholders.

**Term** `scriptum` · **Section** KEYWORDS

## Syntax

```
"<template>"(<args>...)
```

## What this teaches

- String template interpolation — `"template § and §"(arg1, arg2)` replaces `§` placeholders with positional arguments
- Templates can contain any expression as an argument, not just variables

## Common mistakes

- Confusing `format` (template desugaring into function calls) with bare `§` interpolation outside of the template syntax.

## Grammar

```
templateExpr :← stringLit '(' exprList ')'
```

## Expected output

```
Salve greeting, persona notice, and computed summa string.
```

## Example

```fab
main {
    const string name ← "Marcus"
    const int aetas ← 30

    # One slot
    const string salutatio ← "Salve, §!"(name)
    print salutatio

    # Multiple slots
    const string notitia ← "§ habet annos §"(name, aetas)
    print notitia

    # With an expression
    const string sum ← "10 + 20 ← §"(10 + 20)
    print sum
}
```

See also: [`read`](read.md), [`line`](line.md).

Fetch list: https://faberlang.dev/agents/index.md
