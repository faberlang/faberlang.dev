# Faber Targets

Version: `__DOCS_VERSION__`.

Status: local capability draft.

## Capability Labels

Use dimensions instead of a single ambiguous "supported" label.

| Dimension | Meaning |
| --- | --- |
| `parse/check` | Source can be parsed and typechecked. |
| `emit` | The toolchain can produce backend text or artifacts. |
| `validate` | Emitted output can be checked for shape or consistency. |
| `build` | A complete build artifact is produced. |
| `run` | The artifact can be executed by the toolchain. |
| `package` | The artifact can be bundled for distribution. |

## RC1-Era Snapshot

| Lane | Local status | Public wording |
| --- | --- | --- |
| Rust native binary | Product lane in the local contract. | Use only with release evidence. |
| Package binary | Locally evidenced, registry-live claims gated. | "Package binary lane" only. |
| Go CLI | Narrow experimental lane. | Do not say "Go is supported." |
| TypeScript, S-expression | Emit-only research surfaces. | Do not imply runtime support. |
| Wasm, LLVM, Metal, WGSL | Host-backend/compiler lanes. | Do not present as product targets. |
| GPU/browser | Tracked work. | Not RC1 product claims. |

## Rule

If a lane lacks `run` and public run evidence, describe it as tracked,
experimental, or emit-only. Do not turn backend existence into a product claim.
