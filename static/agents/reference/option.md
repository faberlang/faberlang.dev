# option

Declares a CLI option annotation.

**Term** `optio` · **Section** KEYWORDS

## Syntax

```
@ option <binding> [short "x"] [long "name"] [type <type>] [description "..."] [global] [vel <default>]
```

## What this teaches

- CLI options — `@option` declares named flags (short and long forms) for CLI subcommands.
- Option metadata — Each option specifies binding, type, description, and optional default values.

## Common mistakes

- Declaring a boolean option without at least one of short or long — boolean flags need a flag form to be usable.

## Grammar

```
annotation :← '@' 'optio' optionSpec
```

## Expected output

```
No incipit — declaration or test-runner surface only.
```

## Backend

```
declaration-only CLI metadata (whitelist: optio/optio.fab).
```

## Example

```fab
@ cli "optio-smoke"
@ option verbose short "v" long "verbose" type bool description "Verbose mode"
@ option count long "count" type int description "Repeat count"
main args args {
}
```

See also: [`operand`](operand.md), [`cli`](cli.md), [`command`](command.md), [`global`](global.md), [`vel`](coalesce.md).

Fetch list: https://faberlang.dev/agents/index.md
