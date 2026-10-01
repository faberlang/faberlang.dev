# selective_import

Selective imports bind exported members by name: one exported value or type per const local, with the imported file interface supplying the complete type.

**Term** `selective_import` · **Section** KEYWORDS · **Also** `selective imports`, `importa fixum`

## Syntax

```
import from <source> [public] const <member> [as <local>]{, <member> [as <local>]}
```

## What this teaches

- Value bindings — `import from "norma:console" const dic as output, funde as output_bytes` imports one exported value member per `const` local; the pre-`as` identifier names an exported value in the imported file, the post-`as` identifier is the caller-owned local binding
- Values and types — functions and constants bind as values; a type export binds the type itself, usable in type positions exactly like its qualified `module.Type` path (it is not a value, and `is` against it is rejected until cross-file type tests are designed)
- Ordinary locals — the bindings obey ordinary local-binding rules (duplicates, shadowing, lints), are locale-resolved through the imported module, and are never re-exports
- No wildcard mixing — wildcard members cannot mix into the selective list; `public` before `const` re-exports each binding
- Trailing comma — the current parser tolerates one trailing comma after the final member; the canonical spine keeps every comma required
- Pairs with ⇇ — import a sink value this way and replace compiler-owned output statements with ordinary typed values

## Common mistakes

- expecting a type binding to be a value — `print Type` or `x est Type` on an imported type is an error
- expecting the bindings to re-export — only `public` bindings do

## Example

```fab
import from "norma:console" const dic as output, funde as output_bytes

fn write((string) → void sink, string name) → void {
    sink ⇇ name
}

main {
    const string name ← "salve"
    print name
}
```

See also: [`import`](import.md), [`from`](from.md), [`⇇`](⇇.md).

Fetch list: https://faberlang.dev/agents/index.md
