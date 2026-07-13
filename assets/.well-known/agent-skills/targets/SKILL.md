# Faber Targets

Use this skill to understand Faber target capability dimensions. Never
convert dimensions into one ambiguous "supported" label.

Version: `__DOCS_VERSION__`.

## Use When

- Choosing a compilation target.
- Understanding what a target can and cannot do.
- Interpreting `faber targets` output.
- Explaining why an emit-only target is not a product runtime.

## Capability Dimensions

| Dimension | Meaning |
| --- | --- |
| `parse/check` | Syntax and type validation. |
| `emit` | Code generation to a backend format. |
| `validate` | Emitted output self-verification. |
| `build` | Full compile producing an artifact. |
| `run` | Execute the built artifact. |
| `package` | Bundle for distribution. |

A target may support `emit` without supporting `run`. Never assume `emit`
implies a product runtime.

## Product Lane

- **Rust native binary** supports all six dimensions.
- **Go, TypeScript, S-expression** are emit-only research prototypes.
- **Wasm, LLVM, Metal, WGSL** are host-backend compiler lanes.

## Constraints

- Do not infer runtime support from emit-only capability.
- Do not use an emit-only target as a build or run target.
- The `targets` command shows capability dimensions, not a binary
  "supported/unsupported" label.

## Related Skills

- `build-run` — build and execution workflow.
- `effects` — provider selection per target.

## Links

- `/contracts/__DOCS_VERSION__/targets.json`
- `/docs/__DOCS_VERSION__/packages/index.md`
