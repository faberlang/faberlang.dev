# Faber Examples

Version: `__DOCS_VERSION__`.

Status: local example index draft. Public examples require source authority,
leakage checks, and run evidence before they can be marked runnable.

## Candidate Families

| Example family | Draft use | Public status label |
| --- | --- | --- |
| Coreutils-style tools | Explain native app, package binary, and narrow Go CLI evidence. | Gated until public source and run proof. |
| Vivilite | Explain readable application code with persistence. | Gated until public source and run proof. |
| Automation | Explain multi-module native application structure. | Gated until public source and run proof. |
| GPU workload | Track future accelerated lane. | Tracked, not RC1 proof. |
| AI workbench | Track future applied tooling. | Tracked, not RC1 proof. |

## Labels

Use one of these labels on every public example:

- `runnable`: public source and current run evidence exist;
- `read-only`: public source exists but no current run evidence is attached;
- `tracked`: useful future example, not part of the current release proof;
- `blocked`: cannot be public until a named gate clears.

This local packet marks all candidate examples as gated, tracked, or blocked.
It does not publish runnable example claims.
