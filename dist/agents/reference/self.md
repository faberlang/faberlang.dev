# self

Refers to the current instance inside a method.

**Term** `self` · **Section** KEYWORDS · **Also** `this`

## Syntax

```
self.<member>
```

## What this teaches

- Self-reference — `self.<member>` accesses the current instance's fields and methods inside a class method.
- Method definition — functions defined inside a class block receive the instance as `self`.

## Common mistakes

- Using `self` outside a class method — `self` is only valid inside methods defined on a class (SEM008).

## Grammar

```
memberExpr inside genus method :← 'ego' '.' ident
```

## Expected output

```
capsa: prima
```

## Example

```fab
class Capsa {
    mut string titulus

    fn narra() → string {
        # ego = the receiver instance
        return "capsa: " + self.titulus
    }
}

main {
    let Capsa capsa ← Capsa { titulus = "first" }
    print capsa.narra()
}
```

See also: [`const`](const.md), [`class`](class.md).

Fetch list: https://faberlang.dev/agents/index.md
