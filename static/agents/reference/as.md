# as

Introduces an alias name.

**Term** `ut` · **Section** KEYWORDS · **Also** `as`

## Syntax

```
<name> as <alias>
```

## What this teaches

- Parameter aliasing — `as` renames function parameters for clarity or disambiguation
- Import aliasing — also used in `import` contexts for renamed imports

## Common mistakes

- confusing as (import or parameter alias) with sicut (comparison) or velut (pattern match)

## Grammar

```
alias :← ident 'ut' ident
```

## Expected output

```
Scalar stdout smoke (see body).
```

## Backend

```
Cross-ref: destructura/, importa/, discerne/ (per-field ut).
```

## Example

```fab
fn greet(string location as loc) → string {
    return loc
}

main {
    print greet("Roma")
}
```

See also: [`from`](from.md), [`args`](args.md).

Fetch list: https://faberlang.dev/agents/index.md
