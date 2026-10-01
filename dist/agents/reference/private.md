# private

Marks a declaration as module-private (the default tier).

**Term** `privata` · **Section** KEYWORDS · **Also** `private`

## Syntax

```
@ private <declaration>
```

## What this teaches

- Module-level visibility — `@ private` (en spelling `@ private`) restricts a declaration to the current module, keeping it out of the importable surface
- Used as an annotation (`@ private`) on function declarations to control the module boundary; unmarked declarations are module-private by default

## Common mistakes

- Expecting `@ private` to mean anything beyond module-private — it is an explicit marker for the default tier (accepted, no warning).

## Grammar

```
annotatedDecl :← '@' 'privata' funcDecl
```

## Expected output

```
privata
```

## Example

```fab
@ private { }
fn privatum() → string {
    return "private"
}

main {
    print privatum()
}
```

See also: [`public`](public.md), [`import`](import.md).

Fetch list: https://faberlang.dev/agents/index.md
