# exit

Sets the exit code or exit expression for an entry point.

**Term** `exitus` · **Section** KEYWORDS

## Syntax

```
main args <name> exit <expr> <block>
```

## What this teaches

- Sets the exit code or exit expression for an entry point.
- Related keywords: main, async_main, args

## Common mistakes

- Using `throw` without a `⇥` on the enclosing function — `throw` requires an enclosing function with a `⇥` alternate-exit type (SEM010).

## Grammar

```
entryModifier :← 'exitus' integer
```

## Expected output

```
No incipit — declaration or test-runner surface only.
```

## Backend

```
declaration-only entry modifier (whitelist: exitus/exitus.fab).
```

## Example

```fab
@ cli { name = "exitus-smoke" }
main args args exit 1 {
}
```

See also: [`main`](main.md), [`async_main`](async_main.md), [`args`](args.md).

Fetch list: https://faberlang.dev/agents/index.md
