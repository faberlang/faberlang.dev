# Faber Quickstart Preview

Use this skill to understand the intended create/check/build/run/test workflow.
Do not present it as a public install guide.

Version: `__DOCS_VERSION__`.

## Use When

- An agent is evaluating the local RC1 packet.
- A future package workflow needs layout context.
- A toolchain is available in an approved local environment.

## Canonical Choices

1. Treat `faber new <name>` as intended workflow shape until install gates clear.
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

- Do not claim a public install path or source-build path.
- Do not assume Go, TypeScript, or Wasm packages work like native Rust packages.
  The supported lane is Rust packages producing native binaries.
- Run `faber check` before `faber build` — it is faster and catches more errors.
- Do not invent capabilities not listed in the providers contract.
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
