# string (textus)

Primitive string/text type.

**Term** `textus` · **Section** KEYWORDS · **Also** `string`

## Syntax

```
string
```

## What this teaches

- Primitive string/text type.
- Related keywords: string, format, ↦

## Common mistakes

- Using `string` transform methods on non-text types — `.slice()`, `.uppercase()`, `.lowercase()`, `.trim()`, `.split()`, `.replace()` are textus-only compiler intrinsics.

## Grammar

```
s.slice(lo, hi) | s.uppercase() | s.lowercase() | s.trim()
s.split(sep) | s.replace(old, new)
divide returns lista<textus>; pairs with lista/ exempla for collection smoke.
Derived locals use sit so the transform chain needs no type annotations.
Wasm tier Runnable.
```

## Expected output

```
Smoke asserts exit 0 only.
```

## Example

```fab
main {
    let _ nuntius ← " Ave Roma "

    let _ secta ← nuntius.slice(1, 4)
    let _ magna ← nuntius.uppercase()
    let _ parva ← nuntius.lowercase()
    let _ rasa ← nuntius.trim()
    let _ partes ← rasa.split(" ")
    let _ mutata ← rasa.replace("Roma", "Munde")

    print secta, magna, parva
    print rasa, partes, mutata
}
```

See also: [`string`](string.md), [`format`](format.md), [`↦`](↦.md).

Fetch list: https://faberlang.dev/agents/index.md
