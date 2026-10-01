# interface

Declares a behavioral contract with method signatures.

**Term** `implendum` · **Section** KEYWORDS · **Also** `interface`

## Syntax

```
interface <name> [<type-params>] <block>
```

## What this teaches

- Declares a behavioral contract with method signatures.
- Related keywords: class, implements

## Common mistakes

- Declaring a `class implements Implendum` without implementing all required methods — every method signature in the interface must have a body in the class.

## Grammar

```
implendumDecl :← 'implendum' ident '{' methodSig* '}'
genusDecl     :← 'genus' ident 'implet' ident '{' ... '}'
```

## Expected output

```
circulus radius: 25
quadratum latus: 15
```

## Example

```fab
interface Figurabile {
    fn depinge() → void
}

class Circulus implements Figurabile {
    var int radius = 10

    fn depinge() → void {
        print "circulus radius: §"(self.radius)
    }
}

class Quadratum implements Figurabile {
    var int latus = 5

    fn depinge() → void {
        print "quadratum latus: §"(self.latus)
    }
}

main {
    const Circulus circulus ← Circulus { radius = 25 }
    const Quadratum quadratum ← Quadratum { latus = 15 }
    circulus.depinge()
    quadratum.depinge()
}
```

See also: [`class`](class.md), [`implements`](implements.md).

Fetch list: https://faberlang.dev/agents/index.md
