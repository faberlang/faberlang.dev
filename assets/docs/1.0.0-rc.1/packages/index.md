# Faber Packages & Tools

Package layout, manifests, imports, dependencies, and tool workflows.

Version: `__DOCS_VERSION__`.

## Package Layout

```
my-package/
├── faber.toml       # package manifest
├── faber.lock       # resolution lockfile (commit this)
├── src/
│   ├── main.fb      # default entrypoint
│   └── lib.fb       # additional modules
├── tests/
│   └── test_main.fb # test files
└── scripts/         # optional build scripts
```

## Manifest

`faber.toml` declares package identity and dependencies:

```toml
[package]
name = "hello"
version = "0.1.0"

[dependencies]
norma = "0.1.0"
```

The lockfile `faber.lock` records exact resolved versions. Commit it.

## Imports

Import modules with `import module.name`:

```
import norma.collections
```

The import path mirrors the file path under `src/`. A file at
`src/utils/math.fb` is imported as `import utils.math`.

## Tools

| Command | Purpose |
| --- | --- |
| `faber new <name>` | Scaffold a new package. |
| `faber check` | Fast syntax and type validation. |
| `faber build` | Full compile to native binary. |
| `faber run` | Build and execute. |
| `faber test` | Run all tests. |
| `faber format` | Canonical source formatting. |
| `faber explain <target>` | Explain compiler choices. |
| `faber targets` | List target capability dimensions. |
| `faber script <name>` | Run a named build script. |

## Dependencies

External dependencies are resolved through Cista, the Faber package registry.
Declare them in `faber.toml` under `[dependencies]`. Do not pin to local
filesystem paths.

## Constraints

- Do not hand-edit `faber.lock`.
- Do not import from sibling filesystem paths outside the package.
- Run `faber format` before committing.
- Run `faber check` before `faber build`.

## Related

- `/docs/__DOCS_VERSION__/quickstart.md` — create and verify.
- `/docs/__DOCS_VERSION__/effects/index.md` — providers and routing.
- External: Norma, Triga, Cista documentation.
