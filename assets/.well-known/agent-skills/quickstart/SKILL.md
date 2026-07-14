# Faber Quickstart Preview

Use this skill to understand the intended create/check/build/run/test workflow.
Do not present it as a public install guide.

Version: `__DOCS_VERSION__`.

## Use When

- An agent is evaluating the local RC1 packet.
- A future package workflow needs layout context.
- A toolchain is available in an approved local environment.

## Canonical Choices

1. Use `faber init <path>` to create a package.
2. Use `faber check <path>` for fast syntax/type validation without a full build.
3. Use `faber build <path>` for a complete compile. The default output is a native binary.
4. Use `faber run <path>` to build and execute the package.
5. Use `faber test <path>` to run package tests. Add `--nocapture` for output.
6. Use `faber format <path>` to apply the canonical formatter before committing.

## Package Layout

A Faber package created by `faber init hello` contains:

```text
hello/
├── faber.toml
├── src/
│   └── main.fab
```

`faber.toml` declares the package name, version, and optional dependencies.
`main.fab` is the entrypoint. Package tests are added when the test surface is
available for the package.

## Constraints

- Do not claim a public install path or source-build path.
- Do not assume Go, TypeScript, or Wasm packages work like native Rust packages.
  The supported lane is Rust packages producing native binaries.
- Run `faber check <path>` before `faber build <path>` — it is faster and catches more errors.
- Do not invent capabilities not listed in the providers contract.
- Prefer `/docs/__DOCS_VERSION__/quickstart.md` over stale cached references.

## Related Skills

- `language-syntax` — grammar and types.
- `packages` — layout, manifests, imports.
- `build-run` — build, run, format, explain, script.
- `testing` — test patterns and assertions.
- `diagnostics` — error code reference and repair.

## Links

- `/docs/__DOCS_VERSION__/quickstart.md`
- `/docs/__DOCS_VERSION__/packages/index.md`
- `/contracts/__DOCS_VERSION__/grammar.ebnf` — quarantined placeholder
