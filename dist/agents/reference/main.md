# main

Declares the synchronous program entry point.

**Term** `incipit` · **Section** KEYWORDS · **Also** `main`, `entry`

## Syntax

```
main <block>
```

## What this teaches

- Declares the synchronous program entry point.
- Related keywords: fn, import

## Common mistakes

- Attaching `@ cli` to a non-`main` declaration — `@ cli` may only annotate an `main` entry point (SEM009).

## Grammar

```
entryBlock :← 'incipit' block
```

## Expected output

```
none — smoke asserts exit 0; entry diagnostic via nota.
```

## Backend

```
Contrast with salve-munde.fab (module-scope nota), functionibus.fab
  (calls module-level functio), and cli/cli.fab (incipit argumenta).
main {
    print "ingressus"
}
```

## Example

```fab
test "do nothing deliberately" {
    pass
}
```

See also: [`fn`](fn.md), [`import`](import.md).

Fetch list: https://faberlang.dev/agents/index.md
