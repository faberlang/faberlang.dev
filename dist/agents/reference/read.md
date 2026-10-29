# read

Reads input from the active input stream.

**Term** `read` · **Section** KEYWORDS

## Syntax

```
read [line]
```

## What this teaches

- stdin input with `read` — `read` returns all of stdin to end of input, here the one line of the sibling lege.stdin fixture
- the `↦ regex` conversion — compiling a string pattern into a regex value

## Common mistakes

- Not checking `is none` before using the value — `read` may return `null` at end of input.

## Grammar

```
conversio :← stringLit '↦' 'regex'
readExpr :← 'lege'
```

## Expected output

```
lege.expected — the compiled regex pattern, then the fixture text. The text
keeps its own final newline, so `print` leaves a blank line after it.
```

## Backend

```
Targets read the fixture through the case manifest's `stdin` field; the
outcomes row of each target pins how it handles a whole-stream read.
```

## Example

```fab
main {
    let regex pattern ← "(?i)\\d+" ↦ regex
    print pattern
    let string ∪ none input ← read
    print input
}
```

See also: [`line`](line.md), [`write`](write.md).

Fetch list: https://faberlang.dev/agents/index.md
