# fn

Declares a named function or method.

**Term** `functio` · **Section** KEYWORDS · **Also** `function`

## Syntax

```
fn <name>(<params>) [modifiers] [→ <type>] [⇥ <error-type>] <block>
```

## What this teaches

- Declares a named function or method.
- Related keywords: →, ⇥, return, optional, rest, prae, future, cursor

## Common mistakes

- Omitting the `→ T` return type annotation — if a function uses `return`, the return type must be declared; `return` outside a function body is also an error (SEM032).

## Grammar

```
funcDecl :← 'functio' ident '(' paramList ')' ('→' type)? block
```

## Expected output

```
functio.expected — four diagnostics (greetings, name, integer).
Function with no parameters, no return
```

## Example

```fab
fn saluta() → void {
    print "Salve, Mundus!"
}

# Function with parameter, no explicit return type
fn dic(string verbum) → void {
    print verbum
}

# Function with return type
fn name() → string {
    return "Marcus Aurelius"
}

# Function with parameter and return type
fn duplica(int n) → int {
    return n * 2
}

main {
    saluta()
    dic("Bonum diem!")
    const string rex ← name()
    print rex
    print duplica(21)
}
```

See also: [`→`](→.md), [`⇥`](⇥.md), [`return`](return.md), [`optional`](optional.md), [`rest`](rest.md), [`prae`](prae.md), [`future`](future.md), [`cursor`](cursor.md).

Fetch list: https://faberlang.dev/agents/index.md
