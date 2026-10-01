# implements

Declares that a type implements one or more interface contracts.

**Term** `implet` · **Section** KEYWORDS · **Also** `implements`

## Syntax

```
class <name> implements <interface-list> <block>
```

## What this teaches

- Declares that a type implements one or more interface contracts.
- Related keywords: class, interface

## Common mistakes

- Declaring `class implements Implendum` without implementing all required methods — every method signature in the interface must have a body in the class.

## Grammar

```
genusDecl :← 'genus' ident 'implet' ident '{' methodDecl* '}'
```

## Expected output

```
implet.expected — Aurelia from implendum plenum().
```

## Example

```fab
interface Nominatum {
    fn plenum() → string
}

class Civis implements Nominatum {
    var string nomen

    fn plenum() → string {
        # satisfies implendum requirement
        return "§"(self.nomen)
    }
}

main {
    const Civis civis ← Civis { nomen = "Aurelia" }
    print civis.plenum()
}
```

See also: [`class`](class.md), [`interface`](interface.md).

Fetch list: https://faberlang.dev/agents/index.md
