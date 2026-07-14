# Faber Testing

Use this skill to write, run, or interpret Faber tests.

Version: `__DOCS_VERSION__`.

## Use When

- Adding tests to a Faber package.
- Running the test suite.
- Debugging test failures.
- Understanding test patterns and assertions.

## Canonical Choices

1. Place package test files under `tests/` when the package test surface is available.
2. Use `faber test <path>` to run package tests.
3. Add `--nocapture` for output: `faber test <path> --nocapture`.
4. Test functions are annotated with `@test`.
5. Assertions use the builtin `assert` and `assert_eq` forms.
6. Each test function is a self-contained unit with no shared mutable state.
7. Run `faber format` before committing test changes.

## Constraints

- Do not place tests in `src/`. Use the `tests/` directory.
- Tests must not depend on external network or filesystem state unless
  explicitly documented as integration tests.
- Do not ship test-only dependencies through the package manifest.

## Related Skills

- `quickstart` — package creation.
- `build-run` — build and tool workflows.
- `diagnostics` — error code reference.

## Links

- `/docs/__DOCS_VERSION__/quickstart.md`
- `/docs/__DOCS_VERSION__/packages/index.md`
