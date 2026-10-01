# block-string

Block string literals with embedded quotes and newlines.

**Term** `block-string` · **Section** TYPES · **Also** `«...»`

## Syntax

```
«<text>»
```

## What this teaches

- block string literals with `«...»` — embed quotes and newlines without escaping
- multiline content in a single literal value

## Common mistakes

- Using triple-quote """...""" or ❝...❞ instead of «...» — block strings use guillemets only.

## Grammar

```
blockStringLit :← '«' ... '»'
```

## Expected output

```
he said "salve", line one
main {
    const string quote ← «he said "salve"»
    output ⇇ "§\n"(quote)
    const string multiline ← «line one
still line one»
    output ⇇ "§\n"(multiline.slice(0, 8))
}
```

## Example

```fab
import from "norma:console" const write_partial as output
```

See also: [`string`](string.md), [`string`](textus.md).

Fetch list: https://faberlang.dev/agents/index.md
