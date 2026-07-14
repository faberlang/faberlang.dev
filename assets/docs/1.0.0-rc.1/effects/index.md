# Faber Effects Preview

Declarative `ad` shape, runtime builtins, native host boundary, and provider
family planning notes.

Version: `__DOCS_VERSION__`.

Status: local draft. `/contracts/__DOCS_VERSION__/providers.json` currently
lists provider families with empty `routes` arrays. Treat provider family names
as planning/source-shape context only until exported provider manifests populate
route entries.

## Ad Routes

Effects use `ad` route calls in source, but this packet does not publish an
approved effect syntax example.

The public packet does not currently expose provider route coverage or provider
selection rules for `ad` declarations.

## Runtime Builtins

Builtin effects are always available without provider declaration:

- Arithmetic and comparison operators.
- Memory allocation and deallocation.
- Basic type conversions.

## Native Host

The native host provides the bridge between Faber programs and the operating
system. Public docs should describe user-visible behavior, not private host
implementation paths.

## Provider Family Planning

The draft provider contract names five families but exposes no capability
routes for `__DOCS_VERSION__`:

| Provider | Domain | Published routes |
| --- | --- | --- |
| `aleator` | Randomness, entropy | none in this packet |
| `consolum` | Console I/O | none in this packet |
| `processus` | Process management | none in this packet |
| `solum` | Filesystem | none in this packet |
| `tempus` | Time, clocks | none in this packet |

The draft provider manifest is
`/contracts/__DOCS_VERSION__/providers.json`. Its empty route arrays are the
claim boundary for this packet.

## Constraints

- Do not claim provider capability selection from this packet.
- Do not publish example provider route names until exported provider manifests
  include those route entries.
- Do not infer shipped-provider behavior from the provider family table.
- Do not assume a capability is synchronous or available unless a future
  provider manifest documents it.

## Related

- `/contracts/__DOCS_VERSION__/providers.json` — provider manifests.
- `/docs/__DOCS_VERSION__/language/index.md` — `ad` syntax.
- `/.well-known/agent-skills/effects/SKILL.md` — agent skill router.
