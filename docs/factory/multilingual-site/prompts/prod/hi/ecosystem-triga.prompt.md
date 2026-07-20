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

Triga is an optional public source library for geometry, scene, and
GPU-facing type contracts. In normal projects, declare Triga as a Cista
package dependency in `faber.toml`; Cista records the resolved source in
`faber.lock` and the compiler resolves it from the package store.

`FABER_LIBRARY_HOME` is a resolver override for local development when
set. It is not the primary product path for consuming Triga.

Triga provides types and operations for:

- Geometry primitives (points, vectors, matrices, transforms)
- Scene graph structures
- GPU-facing type contracts that align with Faber's systems lane

Triga is not part of Norma. It is an optional dependency that packages
opt into when they need graphics or geometry work.
