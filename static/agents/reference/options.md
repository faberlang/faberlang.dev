# options

Binds CLI options metadata to a function declaration.

**Term** `optiones` · **Section** KEYWORDS

## Syntax

```
fn <name>(...) options <ident> → <type>
```

## What this teaches

- Options bundle — The `options <ident> → <type>` syntax attaches a CLI options struct to a function.
- Declaration syntax — Options are declared as a modifier on the function signature, after the parameter list.

## Common mistakes

- Duplicate flag definitions in options — each short and long flag must be unique within the CLI surface.

## Grammar

```
funcModifier :← ')' 'optiones' ident '→' type
```

## Expected output

```
No incipit — declaration or test-runner surface only.
```

## Backend

```
declaration-only CLI binding (whitelist: optiones/optiones.fab).
```

## Example

```fab
fn mitte() options Opts → string {
    return "ok"
}
```

See also: [`args`](args.md), [`call`](call.md).

Fetch list: https://faberlang.dev/agents/index.md
