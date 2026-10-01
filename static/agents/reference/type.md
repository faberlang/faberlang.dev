# type

Declares a type alias.

**Term** `typus` · **Section** KEYWORDS · **Also** `type`

## Syntax

```
type <name> = <type>
```

## What this teaches

- Type aliases — `type` for creating shorthand names for complex types
- Generic aliases — aliases can wrap generic types like `list<T>` and `map<K,V>`

## Common mistakes

- confusing type (type alias) with class (nominal type) — type creates a transparent alias, not a new type

## Grammar

```
typeAliasDecl :← 'typus' ident '=' typeExpr
```

## Expected output

```
42, "Marcus", verum, ["Gaius", "Lucius", "Titus"], [100, 95, 87]
--- Primitive type aliases ---
```

## Example

```fab
type Signum = int
type Cognomen = string
type Viget = bool

# --- Generic type aliases ---

type Nomina = list<string>
type Puncta = list<int>
type Index = map<string, int>

# Nullable type alias (canonical T ∪ none form)
type NomenOptivum = string ∪ none

main {
    # Using primitive aliases
    const Signum signum ← 42
    const Cognomen cognomen ← "Marcus"
    const Viget viget ← true

    print signum
    print cognomen
    print viget

    # Using generic aliases
    const Nomina sodales ← ["Gaius", "Lucius", "Titus"]
    print sodales

    const Puncta puncta ← [100, 95, 87]
    print puncta
}
```

See also: [`class`](class.md), [`interface`](interface.md), [`object`](object.md), [`∪`](∪.md).

Fetch list: https://faberlang.dev/agents/index.md
