# guillemet

Guillemet string literals: quotes and apostrophes need no escape.

**Term** `guillemet` · **Section** TYPES

## Syntax

```
«<text>»
```

## What this teaches

- a guillemet string needs no escape for a double quote or an apostrophe: «she said "hi" and it's fine»
- template holes apply to guillemets too: «hello, §»("me")
- the literal may span lines; \n and \t still decode
- a raw » closes the literal, so a guillemet cannot contain »

## Common mistakes

- Writing \" or \' inside «...» — neither needs an escape.
- Nesting guillemets — the first » closes the literal.

## Grammar

```
blockStringLit :← '«' ... '»'
```

## Expected output

```
she said "hi" and it's fine
hello, me
line one
line two
tab<TAB>here
```

## Example

```fab
main {
    print «she said "hi" and it's fine»
    print «hello, §»("me")
    print «line one\nline two»
    const string a ← «x "y" z»
    print «tab\there»
}
```

See also: [`string`](string.md), [`block-string`](block-string.md), [`string`](textus.md).

Fetch list: https://faberlang.dev/agents/index.md
