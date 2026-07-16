+++
title = "String and template literals"
section = "syntax"
order = 8
sources = [
  "radix/README.md (String and Template Literals, String-template application, Inline JSON)",
  "examples/corpus/literalia/",
  "examples/corpus/scriptum/",
  "radix/docs/factory/textus-literal-family/",
]
+++

Faber uses delimiter semantics — each quote form means a different source
shape. They are not interchangeable synonyms.

## Literal forms

| Form | Type | Role |
|------|------|------|
| `'…'` | `ascii` | Fixed machine tokens; no `§`; no `(…)` |
| `"…"` | `textus` | Short Unicode line strings; `(…)` renders |
| `«…»` | `textus` | Block/multiline Unicode; `(…)` renders |
| `` `…` `` | `forma` | Captured templates; `(…)` captures |
| `{ … }` | `json` | Compile-time JSON document |
| `|…|` | `octeti` | Compile-time hex bytes |
| `[ … ]` | `lista<T>` | Faber list literal |

## String-template application

Faber formats text with string-template application: a `"…"` or `«…»`
literal with `§` holes, then parenthesised arguments:

```faber
functio greet(textus nomen) → textus {
    redde "Salve, §!"(nomen)
}

fixum _ msg ← "Page § of §"(pagina, totum)
fixum _ block ← «status: § (§)»(code, label)
nota "Value: §"(p.x)
```

Key rules:
- `§` (U+00A7) is the template hole
- Positional holes: `§0`, `§1`, … for explicit ordering
- Trailing `!` selects display formatting: `"Salve, §!"(nomen)`
- The `(args)` suffix is template application, not a function call

## Block strings

Multiline blocks use guillemets `«…»`:

```faber
fixum _ sql ← «
    select id, email
    from accounts
»
```

## Captured templates (forma)

Backtick templates capture text and parameters without rendering.
Safe for bound SQL/URL payloads:

```faber
fixum _ query ← `select * from users where id = §`(user_id)
```

## Inline JSON

A bare `{ … }` is inline JSON: a compile-time `json` document, not an
anonymous Faber object. Keys are quoted strings separated by `:`:

```faber
fixum _ empty ← {}
fixum _ user ← { "name": "Marcus", "age": 30, "active": true }
fixum _ nested ← { "meta": { "version": 1 }, "tags": ["alpha", "beta"] }
```

For typed genus construction, use the type name and `=` field shape:

```faber
fixum _ p ← Point { x = 10, y = 20 }
```
