# targets

Compilation backends listed by faber targets or radix targets.

**Term** `targets` · **Section** CONCEPTS · **Also** `target compatibility`, `backends`

## Syntax

```
faber targets
```

## What this teaches

- querying compilation backends via `faber targets` or `radix targets`
- cross-target function compatibility — syntax lowering varies by backend

## Common mistakes

- Assuming all syntax lowers to every backend — target availability varies; use faber targets to query the capability matrix.

## Expected output

```
salve
```

## Backend

```
META prose + minimal cross-target function smoke.
```

## Example

```fab
fn salve() → string {
    return "salve"
}

main {
    print salve()
}
```

See also: [`manifest`](manifest.md), [`cli`](cli.md), [`∷`](∷.md), [`↦`](↦.md).

Fetch list: https://faberlang.dev/agents/index.md
