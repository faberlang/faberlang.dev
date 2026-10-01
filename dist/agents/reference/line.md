# line

Reads one line of input.

**Term** `lineam` · **Section** KEYWORDS

## Syntax

```
read line
```

## What this teaches

- line-oriented input mode — `read line` reads a single line from stdin

## Common mistakes

- Confusing line (reads one line without trailing newline) with print (writes diagnostic output with newline).

## Grammar

```
readMode :← 'lege' 'lineam'
```

## Expected output

```
Scalar stdout smoke (see body).
```

## Backend

```
Rust/Go/roundtrip whitelist like lege/lege.fab.
```

## Example

```fab
main {
    print "line exemplum — stdin read deferred in harness"
}
```

See also: [`read`](read.md).

Fetch list: https://faberlang.dev/agents/index.md
