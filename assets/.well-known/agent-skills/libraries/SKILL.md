# Faber Libraries

Use this skill to resolve and use external Faber libraries: Norma, Triga, and
Cista.

Version: `__DOCS_VERSION__`.

## Use When

- Adding an external library dependency to a Faber package.
- Understanding what Norma, Triga, or Cista provide.
- Resolving a library version or capability.

## External Projects

| Project | Role | Owns Its Own Docs |
| --- | --- | --- |
| **Norma** | Standard library. Collections, math, strings, I/O abstractions. | Yes |
| **Triga** | GPU/compute host. Shader, tensor, and parallel operations. | Yes |
| **Cista** | Package registry and resolution service. | Yes |

## Canonical Choices

1. Declare external dependencies in `faber.toml` under `[dependencies]`.
2. Import library modules with `import norma.collections` or similar paths.
3. Use Cista to resolve library versions. Do not pin to local paths.
4. Link to each library's own documentation. Do not duplicate their reference
   material in Faber docs.

## Constraints

- Faber documentation explains *how to resolve and use* external libraries. It
  does not absorb their full reference material.
- Do not hand-resolve library versions. Use Cista.
- External libraries may have different release cycles and supported targets.
  Check their documentation for compatibility.

## Related Skills

- `packages` — manifest and dependency management.
- `effects` — provider routing for Triga GPU effects.

## Links

- `/docs/__DOCS_VERSION__/packages/index.md`
