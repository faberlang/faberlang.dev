# static

Marks a class member as belonging to the type itself.

**Term** `generis` · **Section** KEYWORDS

## Syntax

```
static <type> <name> [= <expression>]
```

## What this teaches

- Marks a class member as belonging to the type itself.
- Related keywords: class, ego

## Common mistakes

- Accessing a `static` field on an instance instead of the type — `static` fields are static members accessed via the class name, not via `self`.

## Grammar

```
fieldDecl inside genusDecl :← 'generis'? type ident ('=' expr)?
```

## Expected output

```
ruber
Instance field `nomen` is per-object; `generis ruber` would be accessed on the
genus type in full programs (here only instance fields are read).
```

## Example

```fab
class Color {
    static string ruber = "#ff0000"
    var string nomen = "ruber"
}

main {
    const Color color ← Color {}
    print color.nomen
}
```

See also: [`class`](class.md), [`ego`](self.md).

Fetch list: https://faberlang.dev/agents/index.md
