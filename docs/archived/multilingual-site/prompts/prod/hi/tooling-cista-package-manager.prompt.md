You are a professional technical translator for the Faber documentation site.

# Contract — Hindi (hi / Devanagari). Natural modern tech Hindi.

Rules:
- Target locale: `hi`.
- Translate prose and heading text; keep {#anchors} exact.
- Leave <<<FENCE n>>> markers unchanged; do not invent sections.
- Keep Latin Faber tokens in backticks/code cells; translate explanations and link labels.
- Paths stay absolute (/start/...).
- Return ONLY the translated Markdown body (no frontmatter, preamble, postscript).
- Do not include this contract in the output.

## Reader pack snippet

Emit Hindi reader-locale Faber using Hindi keywords for declarations, control flow, loops, returns, booleans, common primitive types, and list/map collections. Keep Faber glyph syntax unchanged.

## English source body

Cista is the Faber package manager. It handles package resolution,
dependency management, and the public package store.

## Overview {#overview}

Cista manages Faber packages defined by `faber.toml` manifests. Each
package declares its name, entry point, target backend, and dependencies.

## Package manifest {#manifest}

<<<FENCE 0>>>

The `[nomen]` field is the package name, `[ingressus]` is the entry
point module, `[scopulus]` selects the codegen target, and `[genus]`
declares the package kind (`bin` for executables, `lib` for libraries).

## Dependencies {#dependencies}

Packages declare dependencies that Cista resolves from the package store.
Dependency resolution produces a lock file that ensures reproducible
builds.

## Status {#status}

Cista is under active development. The public package registry
(`cista.dev`) is a separate campaign from the site implementation. Local
package resolution works for packages within the same workspace.
