# Faber Quickstart

Create, check, build, run, and test your first Faber package.

Version: `__DOCS_VERSION__`.

## Prerequisites

- Faber toolchain installed (`faber --version` to verify).
- A terminal and text editor.

## Create a Package

```sh
faber new hello
cd hello
```

This creates:

```text
hello/
├── faber.toml
├── src/
│   └── main.fb
└── tests/
    └── test_main.fb
```

## Check

Validate syntax and types without a full build:

```sh
faber check
```

This is faster than `faber build` and catches most errors immediately.

## Build

Compile the package:

```sh
faber build
```

The default output is a native binary in the package root.

## Run

Build and execute:

```sh
faber run
```

## Test

Run the test suite:

```sh
faber test
```

Add `-- --nocapture` to see print output:

```sh
faber test -- --nocapture
```

## Format

Apply canonical formatting before committing:

```sh
faber format
faber check
```

## Next Steps

- Read `/docs/__DOCS_VERSION__/language/index.md` for the language reference.
- Read `/docs/__DOCS_VERSION__/effects/index.md` for native effects and providers.
- Read `/docs/__DOCS_VERSION__/diagnostics/index.md` for error codes and repair.
