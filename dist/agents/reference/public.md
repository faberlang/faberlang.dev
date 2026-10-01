# public

Marks an import as re-exported from the current module.

**Term** `publica` · **Section** KEYWORDS · **Also** `public`

## Syntax

```
import from <source> public <name>
```

## What this teaches

- Module export visibility — `@ public` (en spelling `@ public`) exports a declaration from the current module, making it importable by any consumer
- The opposite of `@ private`; controls the public API surface of a module
- Unmarked top-level declarations are module-private: only `@ public` / `@ internal` declarations appear in the file's importable surface

## Common mistakes

- Leaving a declaration unmarked and expecting it to be importable — the export surface is `@ public` / `@ internal` only.

## Grammar

```
annotatedDecl :← '@' 'publica' funcDecl
```

## Expected output

```
publica
```

## Example

```fab
@ public { }
fn publicum() → string {
    return "public"
}

main {
    print publicum()
}
```

See also: [`private`](private.md), [`import`](import.md).

Fetch list: https://faberlang.dev/agents/index.md
