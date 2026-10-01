# versio

Attaches a version string to a CLI root.

**Term** `versio` · **Section** ANNOTATIONS

## Syntax

```
@ versio <string>
```

## What this teaches

- the `@versio` annotation — attaches a semantic version string to a CLI application
- combining with `@cli` and `@description` for complete CLI metadata

## Common mistakes

- Applying @ versio without @ cli — @ versio only has meaning when attached to a CLI main.

## Grammar

```
annotation :← '@' 'versio' stringLit
```

## Expected output

```
No incipit runtime — declaration-only CLI metadata.
```

## Backend

```
declaration-only CLI metadata (whitelist: meta/versio.fab).
```

## Example

```fab
@ cli "versio-smoke"
@ versio "0.1.0"
@ description "Version metadata exemplum"
main args args {
}
```

See also: [`cli`](cli.md), [`description`](description.md).

Fetch list: https://faberlang.dev/agents/index.md
