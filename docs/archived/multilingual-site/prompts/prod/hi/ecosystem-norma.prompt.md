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

Norma is Faber's standard library. It provides flat Latin-named modules
accessed through `norma:*` paths. Stdlib declarations are Faber source
under the sibling `norma` repository.

## Modules {#modules}

| Module | Domain |
|--------|--------|
| `norma:solum` | Filesystem operations |
| `norma:solum/path` | Pure pathname operations |
| `norma:http` | HTTP client |
| `norma:processus` | Process execution |
| `norma:consolum` | Console I/O (stdin, stdout, stderr) |
| `norma:json` | JSON parsing and serialisation |
| `norma:toml` | TOML parsing |
| `norma:yaml` | YAML parsing |
| `norma:valor` | Codec navigation |
| `norma:tensor` | Tensor bridge helpers |
| `norma:tempus` | Time and duration |
| `norma:aleator` | Randomness |

## Morphologia naming convention {#morphologia-naming-convention}

Norma follows the morphologia policy for all method names. Latin verb
conjugation carries execution mode:

| Stem | Sync | Async | Meaning |
|------|------|-------|---------|
| `leg-` | `lege` | `leget` | Read |
| `scrib-` | `scribe` | `scribet` | Write |
| `quaer-` | — | `quaeret` | Query (finite) |
| `quaer-` | — | `quaerent` | Query (stream) |

Ownership pairs (mutate vs copy-out):

| Mutate | Copy-out | Meaning |
|--------|----------|---------|
| `adde` | `addita` | Add |
| `inverte` | `inversa` | Reverse |
| `filtra` | `filtrata` | Filter |

## Usage {#usage}

<<<FENCE 0>>>
