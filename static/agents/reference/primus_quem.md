# primus_quem

Dedicated total first-match expression: first live element of a source satisfying the owned ubi predicate, none for no-match and empty sources.

**Term** `primus_quem` · **Section** CONCEPTS · **Also** `primus quem`

## Syntax

```
primus_quem(<source>, ubi <binder> { <predicate> })
```

## What this teaches

- dedicated head — `primus_quem(source, ubi x { predicate })` is its own expression (not a `break`/`if` reuse and not a method call); the `ubi` tail is owned by this head
- total evaluation — the predicate is evaluated for EVERY candidate lane (post-match lanes included); selection is dataflow first-live, never an early exit
- `T ∪ none` — no-match and empty sources return `none`, never an error; a predicate ERROR rides the error channel and is never converted to `none`
- first-live — later live lanes never overwrite the first stored match ([1.0, 5.0, 3.0] over `> 2.0` picks 5.0, not 3.0)
- declines — unbounded sources fail closed (SEM059 first_match_unbounded_source, causa not_bounded) and multi-axis `at` coordinates stay unsupported in v1 (SEM059 first_match_expression_unsupported); see primus-quem-decline.fab

## Common mistakes

- expecting an index/value pair — v1 returns only `T ∪ none`; construct the explicit pair yourself if you need the index
- expecting early exit — the predicate still runs after the first match

## Example

```fab
fn elige_litteram() → float ∪ none {
    return primus_quem([1.0, -2.0, 3.0], ubi x { x > 0.0 })
}

# No-match — no live lane yields none, never an error.
fn elige_nullum() → float ∪ none {
    return primus_quem([1.0, 2.0], ubi x { x > 9.0 })
}

# Empty source — a statically zero-length array yields none.
fn elige_vacuum(list<f32> xs) → float ∪ none {
    return primus_quem(xs, ubi x { x > 0.0 })
}

# First-live — with matches at 5.0 and 3.0, the FIRST live lane wins.
fn elige_primum_viventem(list<f32> xs) → float ∪ none {
    return primus_quem(xs, ubi x { x > 2.0 })
}

main {
    const float ∪ none litteram ← elige_litteram()
    const float ∪ none nullum ← elige_nullum()
    const list<f32> vacua_lista ← []
    const float ∪ none void ← elige_vacuum(vacua_lista)
    const list<f32> xs ← [1.0, 5.0, 3.0]
    const float ∪ none primum ← elige_primum_viventem(xs)

    print litteram
    print nullum
    print void
    print primum
}
```

See also: [`none`](nihil.md).

Fetch list: https://faberlang.dev/agents/index.md
