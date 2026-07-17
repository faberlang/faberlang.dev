+++
title = "Hello, Faber"
section = "hello"
order = 2
sources = []
translation_kind = "fallback"
source_locale = "en-US"
source_hash = "sha256:e21072271fa884c1401230130dfda6fee4fa8ece2a7a6b9b4f6556bf74502860"
+++
**Translation status:** Traditional Chinese reader-locale proof. Prose falls back to the English source for this Stage 7 slice; Faber code fences pass through the `zh-Hant` render step during the site build.


Write the smallest useful Faber program: a package entry point that formats a
string and prints it.

## Prerequisites {#prerequisites}

Complete [Install and download](/start/install.html) first. You should have a
`faber` binary on your `PATH` and a shell in a working directory where you can
create files.

## Create a package {#create-package}

```bash
mkdir salve-munde
cd salve-munde
mkdir src
cat > faber.toml <<'EOF'
[package]
name = "salve-munde"
version = "0.1.0"
EOF
cat > src/main.fab <<'EOF'
functio salve(textus nomen) → textus {
    fixum textus msg ← "Salve, §!"(nomen)
    redde msg
}

incipit {
    fixum textus m ← salve("munde")
    nota m
}
EOF
```

## Check it {#check}

```bash
faber check .
```

`faber check` runs the front end: lexing, parsing, type checking, and lowering
far enough to catch ordinary package mistakes without building a native binary.
If the command fails, read the diagnostic code first; Faber diagnostics are
intended to be stable search handles.

## Run it {#run}

```bash
faber run .
```

Expected output:

```text
Salve, munde!
```

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
