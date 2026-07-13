# Faber FMIR

Use this skill for advanced Faber executable package and runtime paths. FMIR
is the intermediate representation used internally by the Radix compiler; it
is **not** the public release name for Faber.

Version: `__DOCS_VERSION__`.

## Use When

- Working with low-level Faber executable packages.
- Understanding compiler IR transformations.
- Debugging code generation decisions.
- Working with compiler development or integration.

## Canonical Choices

1. FMIR is the compiler's internal intermediate representation. Public docs
   document the *behavior*, not the IR format.
2. Advanced users may inspect FMIR output for debugging, but the format is
   not a stable public contract.
3. Do not use "FMIR" interchangeably with "Faber."

## Constraints

- FMIR is not the public release name. Use "Faber" for public references.
- FMIR format is not a stable contract between releases.
- Do not build tooling that depends on FMIR format stability unless explicitly
  documented.

## Related Skills

- `build-run` — build and execution workflow.
- `targets` — target capability dimensions.
- `effects` — provider routing.

## Links

- `/docs/__DOCS_VERSION__/packages/index.md`
