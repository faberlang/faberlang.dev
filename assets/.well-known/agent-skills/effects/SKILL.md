# Faber Effects

Use this skill to understand Faber's `ad` effect system, runtime builtins,
native host routing, and the five provider families.

Version: `__DOCS_VERSION__`.

## Use When

- Declaring or routing an effect in Faber source.
- Choosing a capability from a host provider.
- Understanding the difference between runtime builtins and provider effects.
- Diagnosing an effect routing error.

## Canonical Choices

1. Use the `ad` keyword to declare effect requirements.
2. Runtime builtins are always available and require no provider declaration.
3. Provider effects are routed through one of the five provider families:
   `aleator`, `consolum`, `processus`, `solum`, `tempus`.
4. Select provider capabilities by their documented route name and opener type.
5. Generated native packages link only the providers selected by analysis.
6. Unsupported or unknown provider capability is a structured build error.

## Provider Families

| Provider | Domain |
| --- | --- |
| `aleator` | Randomness, entropy, stochastic operations. |
| `consolum` | Console I/O, terminal interaction, output streams. |
| `processus` | Process management, subprocess spawning, signals. |
| `solum` | Filesystem operations, paths, I/O, permissions. |
| `tempus` | Time, clocks, timers, scheduling. |

Each provider has a draft manifest at
`/contracts/__DOCS_VERSION__/providers.json`.

## Constraints

- Do not invent provider capabilities not in the draft manifest.
- Do not assume a capability is synchronous unless documented.
- Do not route effects to unsupported or unknown providers.
- Do not bypass the provider routing layer.

## Related Skills

- `language-syntax` — `ad` keyword and effect syntax.
- `targets` — capability dimensions per target.
- `packages` — provider dependency declaration.

## Links

- `/docs/__DOCS_VERSION__/effects/index.md`
- `/contracts/__DOCS_VERSION__/providers.json`
