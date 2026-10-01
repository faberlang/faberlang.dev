# promise

Promise-like result type associated with async finite functions.

**Term** `promissum` · **Section** KEYWORDS · **Also** `promise`

## Syntax

```
promise<T> | promise<T ⇥ E>
```

## What this teaches

- Async return type — `promise<T>` is the return-type wrapper for `async` functions and compatibility `@ future` functions.
- Failable async return type — `promise<T ⇥ E>` preserves both the resolved value and delayed alternate channel.

## Common mistakes

- Creating a `promise<T>` but never awaiting it with `await_const`, `await_var`, `return_await`, or `await` — the promise goes unobserved.

## Grammar

```
futuraDecl :← funcDecl 'fiet'
```

## Expected output

```
promissum typus notus (promissum.expected).
```

## Example

```fab
fn compute() async → int {
    return 7
}

main {
    print "promise type notus"
}
```

See also: [`async`](async.md), [`future`](future.md), [`await_const`](await_const.md), [`await`](await.md).

Fetch list: https://faberlang.dev/agents/index.md
