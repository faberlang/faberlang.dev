# for

Starts a for-each iteration statement.

**Term** `itera` · **Section** KEYWORDS · **Also** `iterate`

## Syntax

```
for <mode> <expression> <binding> <block>
```

## What this teaches

- for-each iteration using stream functions — consumes values yielded via `yield` from `generator` and `async_generator` functions
- sync and async stream modes — `generator` and `async_generator` function signatures

## Common mistakes

- Forgetting that stream functions must use `generator` or `async_generator` and yield values with `yield`.

## Grammar

```
forInStmt  :← 'itera' 'ex' callExpr 'fixum' ident block
cursorDecl :← funcDecl 'fiunt' | funcDecl 'fient'
```

## Expected output

```
Sync cursor values and collected lista of doubled results.
```

## Backend

```
Rust lowers `fient` through the async-cursor carrier. Go supports the
`fiunt` half and reports `fient` as an explicit target gap.
Multi-value sync stream function that yields values via cede
```

## Example

```fab
fn grena(int n) generator → int {
    for range 0 ‥ n const i {
        yield i
    }
}

# Multi-value async stream function that yields values via yield
fn grena_futurum(int n) async_generator → int {
    for range 0 ‥ n const i {
        yield i
    }
}

async_main {
    # Direct consumption of cursor yield stream
    print "Sync cursor iteration:"
    for from grena(3) const n {
        print "  int: §"(n)
    }

    # Collect all results from cursor function
    var list<int> effecta ← []
    for from grena(5) const n {
        effecta.append(n * 2)
    }
    print "Sync collected:"
    print effecta
    print "Async cursor iteration:"
    for from grena_futurum(3) const n {
        print "  async int: §"(n)
    }
}
```

See also: [`from`](from.md), [`ref`](ref.md), [`range`](range.md).

Fetch list: https://faberlang.dev/agents/index.md
