# Faber Diagnostics

Use this skill to interpret and repair Faber compiler diagnostic messages.

Version: `__DOCS_VERSION__`.

## Use When

- A `faber check` or `faber build` command produces an error.
- An error code needs to be looked up by its stable identifier.
- A diagnostic message needs repair guidance.

## Canonical Choices

1. Every diagnostic has a stable code (e.g. `E0001`). Search for the code in
   the diagnostics index.
2. Read the full diagnostic page for meaning, cause, and the corrected example.
3. Apply the corrected pattern to the failing source.
4. Run `faber check` to verify the fix.
5. If the diagnostic references a related rule or grammar production, follow
   the link to the language reference.

## Diagnostic Format

Each diagnostic in the approved public export should include:

- **Code** — stable identifier.
- **Meaning** — plain-language description.
- **Likely cause** — common triggers.
- **Invalid example** — source that produces the error.
- **Corrected example** — valid source.
- **Related rule** — grammar, type, or effect reference.
- **Structured arguments** — where the diagnostic carries typed data.

## Constraints

- Do not invent diagnostic codes. Treat codes absent from
  `/contracts/__DOCS_VERSION__/diagnostics.json` as unavailable.
- Do not infer a fix without reading the diagnostic page. The corrected
  example is the authoritative repair.

## Related Skills

- `language-syntax` — grammar and types.
- `build-run` — build and check workflow.

## Links

- `/docs/__DOCS_VERSION__/diagnostics/index.md`
- `/contracts/__DOCS_VERSION__/diagnostics.json`
