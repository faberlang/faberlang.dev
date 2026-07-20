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

Faber reimplements GNU coreutils as application-lane proof. These are real
CLI programs demonstrating Faber building working binaries with argv, stdio,
exit codes, and host I/O, verified against host GNU utilities via a parity
harness.

## Implemented utilities {#implemented-utilities}

**Stage 1 — scaffold + true/false**
`true`, `false`

**Stage 2 — shared common helpers + inline tests**
`echo`, `basename`, `dirname`, `printf`, `seq`

**Stage 3 — nullable-stdin slices**
`cat`, `head`, `tail`, `wc`, `tac`, `uniq`, `fold`, `nl`, `expand`,
`unexpand`, `sort`, `cut`, `grep`, `tr`, `tee`, `paste`

**Scaffolded — Stage 5+**
`rm`, `cp`, `mv`, `mkdir`, `touch`, `pwd`, `readlink`, `realpath`,
`join`, `comm`, `od`, `cksum`, `split`, `yes`, `printenv`

## Example — echo {#example--echo}

The `echo` package demonstrates Faber patterns used throughout coreutils:
CLI annotations, option parsing, inline tests with `probandum`/`proba`/`adfirma`,
and shared common modules:

<<<FENCE 0>>>

## Running {#running}

<<<FENCE 1>>>
