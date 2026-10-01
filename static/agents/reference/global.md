# global

Marks an option or operand as global.

**Term** `ubique` · **Section** KEYWORDS

## Syntax

```
global
```

## What this teaches

- Global CLI flags — `global` marks options available at any command level
- CLI metadata — combining `@ cli`, `@ option`, and `global` for rich command definitions

## Common mistakes

- confusing global (global CLI flag marker) with operand (positional argument) — global applies only to option declarations

## Grammar

```
annotationFlag :← 'ubique'
```

## Expected output

```
No incipit — declaration or test-runner surface only.
```

## Backend

```
declaration-only CLI metadata (whitelist: ubique/ubique.fab).
```

## Example

```fab
@ cli "ubique-smoke"
@ option verbose short "v" long "verbose" type bool global description "Global verbose flag"
main args args {
}
```

See also: [`option`](option.md), [`operand`](operand.md).

Fetch list: https://faberlang.dev/agents/index.md
