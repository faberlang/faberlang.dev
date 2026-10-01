# write

Writes a value to standard output.

**Term** `scribe` · **Section** KEYWORDS

## Syntax

```
write <expression>
```

## What this teaches

- Standard output — `write` sends values to stdout, the primary output channel.
- Expression evaluation — Any expression can be passed, including variables and literals.

## Common mistakes

- Confusing write (stdout without trailing newline) with print (diagnostic output with trailing newline).

## Grammar

```
outputStmt :← 'nota' expr (',' expr)*
```

## Expected output

```
nota.expected — greeting, variable, formatted strings, sum, coordinates.
```

## Example

```fab
main {
    # Simple string output
    print "Salve, Munde!"

    # Variable output
    const string name ← "Marcus"
    print name

    # Multiple arguments
    const int aetas ← 30
    print "name: §"(name)
    print "aetas: §"(aetas)

    # Expressions
    const int x ← 10
    const int y ← 20
    print "sum: §"(x + y)

    # Multiple values in one statement
    print "coordinata: § §"(x, y)
}
```

See also: [`debug`](debug.md), [`warn`](warn.md).

Fetch list: https://faberlang.dev/agents/index.md
