# Faber Effects Preview

Declarative `ad` routes, runtime builtins, native host, and provider families.

Version: `__DOCS_VERSION__`.

Status: local draft. Provider capability lists require the public language
export before publication.

## Ad Routes

Effects are declared with the `ad` keyword and routed to host providers:

```
ad ConsoleWrite(msg: String)
```

The compiler analyzes `ad` declarations and links only the required providers.

## Runtime Builtins

Builtin effects are always available without provider declaration:

- Arithmetic and comparison operators.
- Memory allocation and deallocation.
- Basic type conversions.

## Native Host

The native host provides the bridge between Faber programs and the operating
system. Public docs should describe user-visible behavior, not private host
implementation paths.

## Provider Families

Five provider crates ship with the Faber toolchain:

| Provider | Domain | Example Routes |
| --- | --- | --- |
| `aleator` | Randomness, entropy | random_int, shuffle |
| `consolum` | Console I/O | write_line, read_line |
| `processus` | Process management | spawn, wait, signal |
| `solum` | Filesystem | read_file, write_file, stat |
| `tempus` | Time, clocks | now, sleep, timer |

Each provider has a draft capability manifest at
`/contracts/__DOCS_VERSION__/providers.json`.

## Constraints

- Do not route to unsupported providers. The five listed families are the
  complete set for `__DOCS_VERSION__`.
- Do not assume a capability is synchronous unless documented.
- Unknown provider capability produces a structured build error.

## Related

- `/contracts/__DOCS_VERSION__/providers.json` — provider manifests.
- `/docs/__DOCS_VERSION__/language/index.md` — `ad` syntax.
- `/.well-known/agent-skills/effects/SKILL.md` — agent skill router.
