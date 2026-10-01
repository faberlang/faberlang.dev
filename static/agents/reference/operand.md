# operand

Declares a CLI operand annotation.

**Term** `operandus` · **Section** KEYWORDS

## Syntax

```
@ operand [rest] <type> <binding> [description "..."] [global] [vel <default>]
```

## What this teaches

- CLI operands — `@operand` declares positional arguments for CLI subcommands.
- Binding and description — Each operand specifies a type, binding name, and description.
- Variadic operands — The `rest` keyword marks an operand that consumes remaining arguments.

## Common mistakes

- Duplicate operand bindings or type mismatches — each operand name must be unique and match its declared type.

## Grammar

```
annotation :← '@' 'operandus' operandSpec
```

## Expected output

```
No incipit — declaration or test-runner surface only.
```

## Backend

```
declaration-only CLI metadata (whitelist: operandus/operandus.fab).
```

## Example

```fab
@ cli "operandus-smoke"
@ operand string input description "Input path"
@ operand rest string files description "Extra files"
main args args {
}
```

See also: [`option`](option.md), [`cli`](cli.md), [`command`](command.md), [`rest`](rest.md), [`global`](global.md).

Fetch list: https://faberlang.dev/agents/index.md
