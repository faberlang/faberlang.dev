# version

Attaches a version string to a CLI root.

**Term** `version` · **Section** ANNOTATIONS

## Syntax

```
@ version <string>
```

## What this teaches

- the `@version` annotation — attaches a semantic version string to a CLI application
- combining with `@cli` and `@description` for complete CLI metadata

## Common mistakes

- Applying @ version without @ cli — @ version only has meaning when attached to a CLI main.

## Grammar

```
annotation :← '@' 'version' stringLit
```

## Expected output

```
none — the runner executes the entry and prints nothing; empty golden.
```

## Backend

```
declaration-only CLI metadata (whitelist: meta/versio.fab).
```

## Example

```fab
@ cli "versio-smoke"
@ version "0.1.0"
@ description "Version metadata exemplum"
main args args {
}
```

See also: [`cli`](cli.md), [`description`](description.md).

Fetch list: https://faberlang.dev/agents/index.md
