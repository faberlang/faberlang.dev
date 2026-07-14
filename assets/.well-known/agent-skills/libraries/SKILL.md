# Faber External Projects

Use this skill to understand external Faber-adjacent projects without claiming
their public release or live service state.

Version: `__DOCS_VERSION__`.

## Use When

- Evaluating how external projects fit into the Faber story.
- Understanding what Norma, Triga, or Cista provide.
- Resolving a library version or capability.

## External Projects

| Project | Role | Owns Its Own Docs |
| --- | --- | --- |
| **Norma** | Standard library. Collections, math, strings, I/O abstractions. | Yes |
| **Triga** | Geometry and compute-oriented project; accelerated lanes are tracked. | Yes |
| **Cista** | Package-store and registry client work; live public registry gated. | Yes |

## Canonical Choices

1. Keep external project claims scoped to their evidence and release gates.
2. Import library modules with the current Faber import surface, for example
   `importa ex "norma:chorda" privata chorda`.
3. Do not claim live Cista registry resolution until the registry gate clears.
4. Link to each library's own documentation. Do not duplicate their reference
   material in Faber docs.

## Constraints

- Faber documentation explains *how to resolve and use* external libraries. It
  does not absorb their full reference material.
- Do not claim package publication or live registry availability.
- External libraries may have different release cycles and supported targets.
  Check their documentation for compatibility.

## Related Skills

- `packages` — manifest and dependency management.
- `effects` — provider routing concepts.

## Links

- `/docs/__DOCS_VERSION__/packages/index.md`
