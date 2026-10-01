# string

Short quoted string string literals and template application.

**Term** `string` · **Section** TYPES · **Also** `"..."`

## Syntax

```
"<text>"
```

## What this teaches

- double-quoted string literals `"..."` — the standard string syntax
- template application with `§` placeholders — `"Salve, §!"(name)`

## Common mistakes

- Applying template § to ascii or bytes literals — template application works only on string ("...") string literals.

## Grammar

```
stringLit :← '"' ... '"'
templateApp :← stringLit '(' expr (',' expr)* ')'
```

## Expected output

```
Salve, Salve, Mundus!
```

## Example

```fab
main {
    const string greeting ← "Salve"
    print greeting
    const string name ← "Mundus"
    const string message ← "Salve, §!"(name)
    print message
}
```

See also: [`block-string`](block-string.md), [`§`](§.md), [`string`](textus.md).

Fetch list: https://faberlang.dev/agents/index.md
