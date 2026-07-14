# Faber Quickstart Preview

Preview the package workflow shape for Faber.

Version: `__DOCS_VERSION__`.

Status: local draft. Public installation and runnable quickstart claims are
gated on a released binary or operator-approved install route.

## Prerequisites

- A future Faber toolchain release or approved local evaluation environment.
- A terminal and text editor.

## Create a Package

The intended workflow shape is:

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

Compile the package when the toolchain is available:

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

## Gates

- Do not publish this as an install guide until a binary or approved install
  route exists.
- Do not claim public source-build support.
- Do not mark examples runnable without public source and run evidence.

## Next Steps

- Read `/docs/__DOCS_VERSION__/evaluate/index.md` for the public claim boundary.
- Read `/docs/__DOCS_VERSION__/learn/index.md` for the learning path.
- Read `/docs/__DOCS_VERSION__/targets/index.md` before assuming runtime support.
