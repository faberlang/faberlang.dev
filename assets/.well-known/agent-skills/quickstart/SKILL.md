# Faber Quickstart

Use this skill when you need to create, check, build, run, or test a Faber
package from zero context.

Version: `__DOCS_VERSION__`.

## Use When

- An agent is asked to build something with Faber for the first time.
- A new package needs to be created without prior layout knowledge.
- A quick verification of toolchain and package health is needed.

## Canonical Choices

1. Use `faber new <name>` to scaffold a package. Never hand-create layout files.
2. Use `faber check` for fast syntax/type validation without a full build.
3. Use `faber build` for a complete compile. The default output is a native binary.
4. Use `faber run` to build and execute the default binary target.
5. Use `faber test` to run all package tests. Add `-- --nocapture` for output.
6. Use `faber format` to apply the canonical formatter before committing.

## Package Layout

A Faber package created by `faber new hello` contains:

```text
hello/
├── faber.toml
├── src/
│   └── main.fb
└── tests/
    └── test_main.fb
```

`faber.toml` declares the package name, version, and optional dependencies.
`main.fb` is the entrypoint. `tests/` contains test files.

## Constraints

- Do not hand-write `faber.toml` or layout directories. Use `faber new`.
- Do not assume Go, TypeScript, or Wasm packages work like native Rust packages.
  The supported lane is Rust packages producing native binaries.
- Run `faber check` before `faber build` — it is faster and catches more errors.
- Do not invent Capabilities not listed in the providers contract.
- Prefer the versioned docs at `/docs/__DOCS_VERSION__/` over stale cached
  references.

## Related Skills

- `language-syntax` — grammar and types.
- `packages` — layout, manifests, imports.
- `build-run` — build, run, format, explain, script.
- `testing` — test patterns and assertions.
- `diagnostics` — error code reference and repair.

## Links

- `/docs/__DOCS_VERSION__/quickstart.md`
- `/docs/__DOCS_VERSION__/packages/index.md`
- `/contracts/__DOCS_VERSION__/grammar.ebnf`
