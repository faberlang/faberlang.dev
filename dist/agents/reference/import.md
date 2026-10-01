# import

Imports names from another module or package source.

**Term** `importa` · **Section** KEYWORDS · **Also** `import`

## Syntax

```
import from <source> [public] (<name> [as <alias>] | * as <alias>)
```

## What this teaches

- Imports names from another module or package source.
- Related keywords: from, public, as

## Common mistakes

- Missing the `from` source in the import record — an import record requires an `from` source path.

## Grammar

```
importa ex "<path>" <name> [ut <alias>]
importa ex "<path>" publica <name>   (re-export)
Requires module layout: importa/importa.fab imports from importa/auxilium.fab.
Harness compiles single files in isolation — sibling resolution needs package
or module mode (faber check --package), not bare single-file emit.
```

## Expected output

```
"Salve, Marcus!" on successful link.
BACKEND: Rust/Go e2e whitelist — single-file compile cannot resolve sibling.
```

## Example

```fab
import from "./auxilium" auxilium

main {
    print auxilium.saluta("Marcus")
}
```

See also: [`from`](from.md), [`public`](public.md), [`as`](as.md).

Fetch list: https://faberlang.dev/agents/index.md
