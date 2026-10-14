# bytes

Primitive byte-buffer type.

**Term** `octeti` · **Section** KEYWORDS · **Also** `bytes`

## Syntax

```
bytes
```

## What this teaches

- Primitive buffer type — `bytes` is the built-in byte buffer, analogous to `Vec<u8>` in Rust.
- Literal syntax — Byte buffers can be written with hex literals like `|ref call be ef|`.

## Common mistakes

- Writing bytes hex literals with an odd digit count — each byte requires two hex digits.

## Grammar

```
typeAliasDecl :← 'typus' ident '=' typeExpr
```

## Expected output

```
octeti.expected — type-known diagnostic.
```

## Example

```fab
type Fascis = list<b8>

main {
    const list<b8> sig ← |de ad be ef|
    const list<b8> hello ← |48 65 6c 6c 6f|
    const list<b8> empty ← ||
    print "octeti typus notus"
}
```

See also: [`string`](textus.md), [`list`](list.md).

Fetch list: https://faberlang.dev/agents/index.md
