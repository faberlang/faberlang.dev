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

Write the smallest useful Faber program: a package entry point that formats a
string and prints it.

## Prerequisites {#prerequisites}

Complete [Install and download](/start/install.html) first. You should have a
`faber` binary on your `PATH` and a shell in a working directory where you can
create files.

## Create a package {#create-package}

<<<FENCE 0>>>

## Check it {#check}

<<<FENCE 1>>>

`faber check` runs the front end: lexing, parsing, type checking, and lowering
far enough to catch ordinary package mistakes without building a native binary.
If the command fails, read the diagnostic code first; Faber diagnostics are
intended to be stable search handles.

## Run it {#run}

<<<FENCE 2>>>

Expected output:

<<<FENCE 3>>>

## What you just used {#what-you-used}

| Source | Meaning |
|---|---|
| `functio salve(textus nomen) → textus` | Function named `salve`, type-first parameter, text return |
| `fixum textus msg ← ...` | Immutable binding |
| `"Salve, §!"(nomen)` | Format string with display interpolation |
| `redde msg` | Return |
| `incipit` | Package entry point |
| `nota m` | Print a note/output value |

## Locale proof {#locale-proof}

The program above is the canonical Latin reader rendering. Reader locales can
render the same semantic program with different keyword packs while preserving
glyphs and identifiers. Start with the full proof at
[Reader locale](/features/reader-locale.html) before writing non-Latin packages.

## Next {#next}

| Previous | Next |
|---|---|
| [Install and download](/start/install.html) | [Commands you will use](/start/commands.html) |
