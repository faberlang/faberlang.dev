# protected

Reserved visibility annotation rejected by semantic analysis.

**Term** `protecta` · **Section** KEYWORDS · **Also** `protected`

## Syntax

```
@ protected
```

## What this teaches

- Reserved keyword — `@ protected` is syntactically valid but semantically rejected; it has no active visibility meaning
- This demonstrates how Faber reserves syntax for future use without committing to semantics

## Common mistakes

- Expecting `@ protected` to provide access control — it is reserved and rejected at compile time (SEM018).

## Grammar

```
annotatedDecl :← '@' 'protecta' funcDecl
```

## Expected error

```
`@ protecta` is reserved and has no active visibility meaning
```

## Example

```fab
@ protected
fn protectum() → string {
    return "protected"
}

main {
    print protectum()
}
```

See also: [`public`](public.md), [`private`](private.md).

Fetch list: https://faberlang.dev/agents/index.md
