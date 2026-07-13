# Faber Build and Run

Use this skill when you need to build, run, format, explain, or script Faber
package workflows.

Version: `__DOCS_VERSION__`.

## Use When

- Compiling a Faber package.
- Running a Faber binary.
- Formatting source code.
- Explaining compiler decisions or target selections.
- Scripting build and test workflows.

## Canonical Choices

1. `faber check` — fast syntax and type validation (no codegen).
2. `faber build` — full compile producing native binary output.
3. `faber run` — build and execute the default binary target.
4. `faber test` — run all package tests.
5. `faber format` — apply canonical formatting.
6. `faber explain <target>` — explain compiler choices for a target.
7. `faber targets` — list available target dimensions.
8. `faber script <name>` — run a named build script defined in the package.

## Workflow

```sh
# Create and verify
faber new hello
cd hello
faber check

# Build and run
faber build
faber run

# Test
faber test

# Format before commit
faber format
faber check
```

## Constraints

- Run `faber check` before `faber build` — faster feedback loop.
- Run `faber format` before committing source changes.
- The supported product lane is native binary output. Do not expect Go,
  TypeScript, or Wasm targets to produce runnable applications.
- Use `faber explain` when a build result is unexpected — it surfaces
  the compiler's routing decisions.

## Related Skills

- `quickstart` — package creation.
- `packages` — manifest and dependency management.
- `testing` — test patterns.

## Links

- `/docs/__DOCS_VERSION__/packages/index.md`
- `/docs/__DOCS_VERSION__/quickstart.md`
