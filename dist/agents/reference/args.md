# args

Binds command-line arguments for an entry point.

**Term** `argumenta` · **Section** KEYWORDS

## Syntax

```
main args <name> <block> | fn <name>() args <name> <block>
```

## What this teaches

- CLI entry binding — `main args <name>` declares a program entry that receives command-line arguments
- Annotation-driven CLI — `@ cli`, `@ description`, and `main args` work together to define a structured CLI interface

## Common mistakes

- attaching `@ cli` to a `fn` instead of an `main` (SEM009), or forgetting to annotate with `@ cli` before `main args`

## Grammar

```
entryDecl :← 'incipit' 'argumenta' ident block
```

## Expected output

```
No incipit — declaration or test-runner surface only.
```

## Backend

```
declaration-only CLI entry (whitelist: argumenta/argumenta.fab).
```

## Example

```fab
@ cli "argumenta-smoke"
@ description "args exemplum"
main args args {
}
```

See also: [`main`](main.md), [`cli`](cli.md), [`command`](command.md), [`option`](option.md), [`operand`](operand.md).

Fetch list: https://faberlang.dev/agents/index.md
