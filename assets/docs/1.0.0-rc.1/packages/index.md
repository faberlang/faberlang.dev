# Faber Packages & Tools Preview

Package layout, manifests, imports, dependencies, and tool workflows.

Version: `__DOCS_VERSION__`.

Status: local draft. Public package registry and install claims remain gated.

## Package Layout

```
my-package/
├── faber.toml       # package manifest
├── faber.lock       # resolution lockfile (commit this)
├── src/
│   ├── main.fab     # default entrypoint
│   └── lib.fab      # additional modules
├── tests/           # package tests when present
└── scripts/         # optional build scripts
```

## Manifest

`faber.toml` declares package identity and dependencies:

```toml
[package]
name = "hello"
version = "0.1.0"

[dependencies]
mathesis = "0.1.0"
```

The lockfile `faber.lock` records exact resolved versions. Commit it.

## Imports

Import package-local and library modules through the current Faber import
surface. For example, standard-library modules use the `importa ex` form:

```faber
importa ex "norma:chorda" privata chorda
```

The package source extension is `.fab`. Nested source files under `src/` are
package-local modules; external `norma:*` modules come from the configured
library home or package store.

## Tools

| Command | Purpose |
| --- | --- |
| `faber init <path>` | Scaffold a new package. |
| `faber check <path>` | Fast syntax and type validation for a file or package. |
| `faber build <path>` | Full compile to native binary or selected target artifact. |
| `faber run <path>` | Build and execute a package. |
| `faber test <path>` | Run package tests. |
| `faber format <path>` | Canonical source formatting. |
| `faber explain <target>` | Explain compiler choices. |
| `faber targets` | List target capability dimensions. |
| `faber script <path>` | Interpret a source file, package directory, manifest, or archive. |

## Dependencies

External dependency resolution is part of the package-store direction. Do not
claim a live public registry or public package ecosystem from this local packet.
Declare dependencies in `faber.toml` under `[dependencies]` when the package
workflow is available.

## Constraints

- Do not hand-edit `faber.lock`.
- Do not import from sibling filesystem paths outside the package.
- Run `faber format` before committing.
- Run `faber check <path>` before `faber build <path>`.
- Do not publish Cista registry, login, fetch, or publish claims until the live
  registry gate clears.

## Related

- `/docs/__DOCS_VERSION__/quickstart.md` — create and verify.
- `/docs/__DOCS_VERSION__/effects/index.md` — providers and routing.
- External: Norma, Triga, Cista documentation.
