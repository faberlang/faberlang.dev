# throws

Marks a function as able to throw along a recoverable channel.

**Term** `iacit` · **Section** MODIFIERS

## Syntax

```
fn <name>(...) throws → <type> [⇥ <error-type>]
```

## What this teaches

- the `throws` modifier on function declarations — marks a function as throwable
- the `⇥` error type annotation for specifying the error type contract

## Common mistakes

- Forgetting to declare the ⇥ error type — throws requires an explicit ⇥ error type in the function signature.

## Grammar

```
funcModifier :← 'iacit'
```

## Expected output

```
iacit surface declared
```

## Backend

```
Prefer explicit ⇥ error types for callable contracts; see iace/functio-fallibilis.fab.
```

## Example

```fab
interface Canens {
    fn canta(string vox) throws → void
}

main {
    print "throws modifier declared"
}
```

See also: [`throw`](throw.md), [`catch`](catch.md), [`⇥`](⇥.md), [`errors`](errors.md), [`readonly`](readonly.md).

Fetch list: https://faberlang.dev/agents/index.md
