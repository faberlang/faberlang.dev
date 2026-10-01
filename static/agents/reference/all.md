# all

Marks a test hook as applying to every case.

**Term** `omnia` · **Section** KEYWORDS

## Syntax

```
all
```

## What this teaches

- Exhaustive matching — `match all` requires every variant of a `union` to have a `case` branch.
- Safety guarantee — The compiler rejects incomplete matches, eliminating forgotten variant bugs.

## Common mistakes

- Using default with match all — all forbids catchall arms; list every variant explicitly.

## Grammar

```
matchStmt :← 'discerne' 'omnia' expr '{' casuClause* '}'
```

## Expected output

```
none — stdout not pinned for this exemplum.
```

## Example

```fab
union Condicio {
    Activa,
    Quietus
}

fn narra(Condicio condicio) → string {
    # every variant must have a case
    match all condicio {
        case Activa {
            return "activa"
        }
        case Quietus {
            return "quietus"
        }
    }
}

main {
    const Condicio condicio ← variant Activa
    print narra(condicio)
}
```

See also: [`setup`](setup.md), [`teardown`](teardown.md).

Fetch list: https://faberlang.dev/agents/index.md
