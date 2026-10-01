# manifest

faber.toml package metadata for build, run, and test.

**Term** `manifest` · **Section** CONCEPTS · **Also** `faber.toml`, `package manifest`

## Syntax

```
faber.toml
```

## What this teaches

- the package manifest file `faber.toml` — configures build, run, and test for a Faber package
- key manifest sections: `[package]`, `[paths]`, `[build]`

## Common mistakes

- Omitting the required [package], [paths], or [build] sections — a valid faber.toml must include all three.

## Grammar

```
packageManifest :← toml document (faber tool, not Faber source)
```

## Expected output

```
manifest exemplum
```

## Backend

```
META-only — runnable body is compile smoke only.
```

## Example package layout

faber.toml
src/main.fab
Example faber.toml:
[package]
name = "salve"
version = "0.1.0"
edition = "2026"
[paths]
source = "src"
entry = "main.fab"
[build]
target = "rust"
kind = "bin"

## Example

```fab
main {
    print "manifest exemplum — configure packages via faber.toml"
}
```

See also: [`targets`](targets.md), [`cli`](cli.md), [`main`](main.md), [`test`](test.md).

Fetch list: https://faberlang.dev/agents/index.md
