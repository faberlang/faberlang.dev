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
- optional `[format] width = N` — opt-in line wrapping for `faber format`

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
[format]
width = 100
The [format] table is optional. [format] width = N wraps `faber format` output at N display columns,
indentation included, breaking only between tokens where a newline changes
nothing (an unbreakable span wider than N overflows). It is a positive
integer; zero, a negative number or a non-integer is refused. There is no
built-in width: with neither the key nor the flag, output is not wrapped.
`faber format --width N` wins over the manifest key; `--stdin` has no package,
so only the flag applies.

## Example

```fab
main {
    print "manifest exemplum — configure packages via faber.toml"
}
```

See also: [`targets`](targets.md), [`cli`](cli.md), [`main`](main.md), [`test`](test.md).

Fetch list: https://faberlang.dev/agents/index.md
