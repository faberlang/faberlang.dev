# read

Reads input from the active input stream.

**Term** `lege` · **Section** KEYWORDS

## Syntax

```
read [line]
```

## What this teaches

- stdin input with `read` — reads one line from the active input stream
- the `↦ regex` conversion — compiling a string pattern into a regex value

## Common mistakes

- Not checking is null before using the value — read may return null at end of input.

## Grammar

```
conversio :← stringLit '↦' 'regex'
readExpr :← 'lege'
```

## Expected output

```
Regex pattern diagnostic, then one stdin line (no .expected — interactive).
BACKEND: Rust/Go/roundtrip e2e whitelist — lege not yet lowered for Rust/Go
(whitelist: lege/lege.fab).
```

## Example

```fab
main {
    const regex pattern ← "(?g)\d+" ↦ regex
    print pattern
    const string ∪ none input ← read
    print input
}
```

See also: [`line`](line.md), [`write`](write.md).

Fetch list: https://faberlang.dev/agents/index.md
