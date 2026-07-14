# Faber Build and Run Preview

Use this skill to understand build/run workflow shape in an approved local
environment. Do not present these commands as public installation evidence.

Version: `__DOCS_VERSION__`.

## Use When

- Evaluating command semantics from the local packet.
- Running a Faber binary only in an approved local environment.
- Formatting source code.
- Explaining compiler decisions or target selections.
- Scripting build and test workflows.

## Canonical Choices

1. `faber check <path>` — intended fast syntax and type validation.
2. `faber build <path>` — full compile producing native binary output.
3. `faber run <path>` — build and execute the package.
4. `faber test <path>` — run package tests.
5. `faber format <path>` — apply canonical formatting.
6. `faber explain <target>` — explain compiler choices for a target.
7. `faber targets` — list available target dimensions.
8. `faber script <path>` — interpret a source file, package directory, manifest, or archive.

## Workflow

```sh
# Create and verify
faber init hello
cd hello
faber check .

# Build and run
faber build .
faber run .

# Test
faber test .

# Format before commit
faber format .
faber check .
```

## Constraints

- Run `faber check <path>` before `faber build <path>` — faster feedback loop.
- Run `faber format` before committing source changes.
- Public build/run claims require a released binary or operator-approved
  install route.
- The local product-lane draft is native binary output. Do not expect Go,
  TypeScript, or Wasm lanes to produce runnable applications.
- Use `faber explain` when a build result is unexpected — it surfaces
  the compiler's routing decisions.

## Related Skills

- `quickstart` — package creation.
- `packages` — manifest and dependency management.
- `testing` — test patterns.

## Links

- `/docs/__DOCS_VERSION__/packages/index.md`
- `/docs/__DOCS_VERSION__/quickstart.md`
