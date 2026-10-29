# list<b8>

A byte buffer is a list<b8>; hex literals like |ref call be ef| write one.

**Term** `list<b8>` · **Section** KEYWORDS

## Syntax

```
list<b8>
```

## What this teaches

- Buffer type — a byte buffer is `list<b8>`, a list of raw 8-bit values (analogous to `Vec<u8>` in Rust).
- Literal syntax — A `list<b8>` can be written with hex literals like `|ref call be ef|`.

## Common mistakes

- Writing byte-buffer hex literals with an odd digit count — each byte requires two hex digits.

## Grammar

```
typeAliasDecl :← 'typus' ident '=' typeExpr
```

## Expected output

```
octeti.expected — type-known line.
```

## Example

```fab
type Fascis = list<b8>

main {
    let list<b8> sig ← |de ad be ef|
    let list<b8> hello ← |48 65 6c 6c 6f|
    let list<b8> empty ← ||
    print "octeti typus notus"
}
```

See also: [`string (type)`](string (type).md), [`list`](list.md).

Fetch list: https://faberlang.dev/agents/index.md
