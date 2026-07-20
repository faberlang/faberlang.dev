## System prompt snippet (reader pack)

Emit Thai reader-locale Faber using Thai keywords for declarations, control flow, loops, returns, booleans, common primitive types, and lista/tabula collections. Keep Faber glyph syntax unchanged.

## Instructions

Translate the prose below from English to the target locale. Follow these rules:

- Translate prose only. Do NOT translate code fences.
- Preserve {#anchors} (heading anchors) exactly.
- Preserve markdown structure (headings, paragraphs, lists).
- Preserve table shapes (column count, alignment).
- Preserve links. Paths may stay absolute (/start/...) since the generator prefixes locale paths.
- Fences are shown as "<<<FENCE n>>>" markers. Leave these markers unchanged in your output.
- Return the full body text with markers in place.

## English source body (fences as <<<FENCE n>>>)

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

## Notes

Blind trial: no current locale body provided. Translate fresh from English only.

## Output contract

Return ONLY the translated Markdown body (prose + <<<FENCE n>>> markers).
Do not wrap in a code fence.
Do not include +++ frontmatter.
Do not explain your work after the body.
