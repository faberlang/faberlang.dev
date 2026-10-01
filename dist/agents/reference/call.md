# call

call opens a channel endpoint and materializes the stream with an explicit conversion target.

**Term** `ad` · **Section** KEYWORDS

## Syntax

```
call 'runtime:echo' (payload) ↦ string
```

## What this teaches

- Endpoint materialization — `call 'runtime:echo'(payload) ↦ string` opens a channel connection and converts the stream to a concrete type
- The `↦` materialization operator — directs how the inbound frame stream is interpreted

## Common mistakes

- confusing call route syntax — the materialization target type must match the endpoint's actual return shape

## Example

```fab
main {
    const string t ← call 'runtime:echo' ("salve, munde") ↦ string
    assert t ≡ "salve, munde"
}
```

See also: `conversion`.

Fetch list: https://faberlang.dev/agents/index.md
