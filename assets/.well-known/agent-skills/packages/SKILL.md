# Faber Packages

Use this skill when you need to understand Faber package layout, manifests,
imports, dependencies, or lockfiles.

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
3. Dependencies reference external packages by name and version. They are
   resolved through Cista.
4. Imports use `import module.name` syntax. The module path mirrors the file
   path under `src/`.
5. `faber.lock` is automatically maintained. Commit it to version control.
6. External packages (Norma, Triga) are declared as dependencies. They own
   their own documentation.

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
- Dependencies are resolved through Cista, not local `path = …` overrides.
- External libraries own their own documentation. Link to them; do not
  duplicate their reference material.

## Related Skills

- `quickstart` — package creation and verification.
- `build-run` — build, run, and tool workflows.
- `libraries` — external library resolution.

## Links

- `/docs/__DOCS_VERSION__/packages/index.md`
- `/docs/__DOCS_VERSION__/quickstart.md`
