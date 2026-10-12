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
```

## Example

```fab
main {
    const string quote ← «he said "salve"»
    print quote
    const string multiline ← «line one
still line one»
    print multiline.slice(0, 8)
}
```

See also: [`string`](string.md), [`string`](textus.md).

Fetch list: https://faberlang.dev/agents/index.md
