# Faber Packages Preview

Use this skill to understand package layout, manifests, imports, dependencies,
and lockfiles without claiming a public package registry.

Version: `__DOCS_VERSION__`.

## Use When

- Creating or modifying a `faber.toml`.
- Adding or resolving dependencies.
- Understanding module and import rules.
- Working with lockfiles (`faber.lock`).
- Configuring package metadata.

## Canonical Choices

1. Use `faber new <name>` to create a package. Never hand-create layout.
2. `faber.toml` declares `[package]` metadata, `[dependencies]`, and optional
   `[targets]` configuration.
3. Dependencies reference external packages by name and version when the
   package workflow is available.
4. Imports use `import module.name` syntax. The module path mirrors the file
   path under `src/`.
5. `faber.lock` is automatically maintained. Commit it to version control.
6. External projects own their own documentation and release gates.

## Layout

```text
my-package/
├── faber.toml       # package manifest
├── faber.lock       # resolution lockfile (committed)
├── src/
│   ├── main.fb      # default entrypoint
│   └── lib.fb       # additional modules
├── tests/
│   └── test_main.fb # test files
└── scripts/         # optional build scripts
```

## Constraints

- Do not hand-edit `faber.lock`.
- Do not import from sibling filesystem paths outside the package.
- Do not claim a live package registry, login, fetch, publish, or ecosystem
  availability from this local packet.
- External libraries own their own documentation. Link to them; do not
  duplicate their reference material.

## Related Skills

- `quickstart` — package creation and verification.
- `build-run` — build, run, and tool workflows.
- `libraries` — external library resolution.

## Links

- `/docs/__DOCS_VERSION__/packages/index.md`
- `/docs/__DOCS_VERSION__/quickstart.md`
