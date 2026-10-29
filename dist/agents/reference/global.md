# global

Marks an option or operand as global.

**Term** `global` · **Section** KEYWORDS

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
none — the runner executes the entry and prints nothing; empty golden.
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
