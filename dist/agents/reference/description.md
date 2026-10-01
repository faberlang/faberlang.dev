# description

Attaches a description string to CLI metadata.

**Term** `descriptio` · **Section** KEYWORDS

## Syntax

```
@ description <string>
```

## What this teaches

- CLI metadata — `@ description <string>` attaches a human-readable description to a CLI command's metadata.
- Annotation syntax — used together with `@ cli` to annotate entry points with metadata for CLI generation.

## Common mistakes

- Using description without a corresponding @cli annotation — `@ description` only has meaning when attached to a `@ cli` entry point.

## Grammar

```
annotation :← '@' 'descriptio' stringLit
```

## Expected output

```
No incipit — declaration or test-runner surface only.
```

## Backend

```
declaration-only CLI metadata (whitelist: descriptio/descriptio.fab).
```

## Example

```fab
@ cli "descriptio-smoke"
@ description "Short CLI description"
main args args {
}
```

See also: [`versio`](versio.md).

Fetch list: https://faberlang.dev/agents/index.md
