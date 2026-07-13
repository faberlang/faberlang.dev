# Faber Diagnostics

Stable diagnostic codes, meanings, and repair workflows.

Version: `__DOCS_VERSION__`.

## Overview

Every `faber check` or `faber build` error carries a stable diagnostic code.
Each code has a documented meaning, common causes, and a corrected example.

## Using Diagnostics

1. Note the diagnostic code (e.g. `E0001`) from the compiler output.
2. Look up the code in `/contracts/__DOCS_VERSION__/diagnostics.json` or browse
   the individual diagnostic pages.
3. Read the meaning, cause, and corrected example.
4. Apply the fix and run `faber check` to verify.

## Diagnostic Format

Each diagnostic includes:

- **Code** — stable identifier (e.g. `E0001`).
- **Meaning** — plain-language description.
- **Likely cause** — common triggers.
- **Invalid example** — source that produces the error.
- **Corrected example** — valid source.
- **Related rule** — grammar, type, or effect reference.
- **Structured arguments** — where applicable.

## Constraints

- Diagnostic codes are stable within a release. Do not reference unreleased
  codes.
- The corrected example is authoritative. Apply it exactly.

## Related

- `/contracts/__DOCS_VERSION__/diagnostics.json` — complete diagnostic catalog.
- `/docs/__DOCS_VERSION__/language/index.md` — grammar and types.
- `/.well-known/agent-skills/diagnostics/SKILL.md` — agent skill router.
