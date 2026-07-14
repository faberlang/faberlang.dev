# Faber Effects

Use this skill to understand Faber's `ad` effect source shape, runtime
builtins, native host boundary, and the provider family names currently listed
without route entries.

Version: `__DOCS_VERSION__`.

## Use When

- Reading `ad` effect source-shape examples.
- Checking whether provider route entries are published.
- Understanding the difference between runtime builtins and provider effects.
- Avoiding provider capability claims before route manifests are populated.

## Canonical Choices

1. Use the `ad` keyword to declare effect requirements.
2. Runtime builtins are always available and require no provider declaration.
3. The current provider contract lists five provider families:
   `aleator`, `consolum`, `processus`, `solum`, `tempus`.
4. `/contracts/__DOCS_VERSION__/providers.json` currently has empty `routes`
   arrays for those families.
5. Treat provider family names as planning/source-shape context only until a
   future exported manifest publishes route entries.
6. Do not choose or describe provider capabilities from this packet.

## Provider Families

| Provider | Domain |
| --- | --- |
| `aleator` | Randomness, entropy, stochastic operations. |
| `consolum` | Console I/O, terminal interaction, output streams. |
| `processus` | Process management, subprocess spawning, signals. |
| `solum` | Filesystem operations, paths, I/O, permissions. |
| `tempus` | Time, clocks, timers, scheduling. |

Each provider has a draft manifest at
`/contracts/__DOCS_VERSION__/providers.json`; its empty route arrays are the
claim boundary for this packet.

## Constraints

- Do not invent provider capabilities or route names not in the draft manifest.
- Do not assume a capability is synchronous or available unless a future
  provider manifest documents it.
- Do not present provider routing as usable product guidance while routes are
  empty.
- Do not infer shipped-provider behavior from family names alone.

## Related Skills

- `language-syntax` — `ad` keyword and effect syntax.
- `targets` — capability dimensions per target.
- `packages` — provider dependency declaration.

## Links

- `/docs/__DOCS_VERSION__/effects/index.md`
- `/contracts/__DOCS_VERSION__/providers.json`
