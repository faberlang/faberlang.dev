# unstable

Marks an interface method as planned but unavailable for a target.

**Term** `nondum` · **Section** ANNOTATIONS

## Syntax

```
@ unstable [target] [reason]
```

## What this teaches

- the `@unstable` annotation — marks interface methods as planned but not yet implemented for a target backend
- target-specific availability annotations with optional reason strings

## Common mistakes

- Calling a method marked @ unstable — the compiler rejects calls to unstable methods for the current target (SEM017).

## Grammar

```
interfaceMethod :← '@' 'nondum' target? stringLit
```

## Expected output

```
nondum implendum declared
```

## Backend

```
Calls to @ nondum methods fail semantic check (SEM017); do not invoke here.
```

## Example

```fab
interface tempus {
    @ unstable { target = rs, ratio = "timer handles are not implemented yet" }
    fn siste(int handle) → void
}

main {
    print "unstable interface declared"
}
```

See also: [`interface`](interface.md), [`@`](@.md).

Fetch list: https://faberlang.dev/agents/index.md
