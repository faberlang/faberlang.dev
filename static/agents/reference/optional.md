# optional

Marks a named declaration slot (parameter or class field) as voluntary — the caller or provider may omit the value.

**Term** `sponte` · **Section** KEYWORDS · **Also** `optional`, `voluntary`

## Syntax

```
<type> <name> optional [= default | vel default]
```

## What this teaches

- Voluntary parameter syntax — using `optional` to mark function parameters or class fields as optional
- Default values — combining `optional` with `coalesce` to provide fallbacks when the value is omitted

## Common mistakes

- confusing optional (optional parameter with a default) with ∪ none (nullable type) — optional marks omission, ∪ none marks absence

## Grammar

```
optionalMarker :← 'sponte'
```

## Expected output

```
No incipit — declaration or test-runner surface only.
```

## Backend

```
declaration-only optional slots (whitelist: sponte/sponte.fab). Cross-ref: optionalis/optionalis.fab.
```

## Example

```fab
fn greet(string name, string titulus optional) → string {
    return name
}

fn paginate(int pagina optional coalesce 1) → string {
    return "page"
}

class User {
    var string name
    var string email optional
}
```

See also: [`vel`](coalesce.md), [`none`](nihil.md), [`∪`](∪.md), [`fn`](fn.md), [`class`](class.md).

Fetch list: https://faberlang.dev/agents/index.md
