+++
title = "Examples"
section = "examples"
order = 5
sources = [
  "examples/README.md",
  "examples/ai-workbench/",
  "examples/vivilite/",
  "examples/ai-workbench/ (README.md, package, harness)",
  "examples/coreutils/ (38 packages, README.md, campaign docs)",
  "examples/coreutils/packages/echo/src/main.fab",
]
+++

## Examples

Real Faber packages — not toy snippets. Source lives in the public
[faberlang/examples](https://github.com/faberlang/examples) repository.
Use these when you need to see how applications are structured, how CLIs
are wired, or how the language corpus is organized.

### How to run an example {#how-to-run}

```bash
# CLI on PATH (see Install)
faber --version

# Clone examples
git clone https://github.com/faberlang/examples.git

# Type-check a package; dependencies resolve through faber.lock
# and the Cista package store.
faber check examples/ai-workbench/packages/faber-ai

# Build / run / test when the package supports it
faber build examples/ai-workbench/packages/faber-ai -t rust
faber test examples/ai-workbench/packages/faber-ai
```

Exact entry commands vary by package — read each package `README.md`.

### Application packages {#applications}

| Package | Role | Start here |
|---|---|---|
| **AI Workbench** | Multi-command CLI for local model inventory, embeddings, and inference workflows; Python harness validation | [examples/ai-workbench](https://github.com/faberlang/examples/tree/main/ai-workbench) · site: [AI Workbench](/start/examples.html) |
| **ViviLite** | Faber-native local mailspace CLI (file-backed + optional SQLite lane) for agent coordination commands | [examples/vivilite](https://github.com/faberlang/examples/tree/main/vivilite) |
| **coreutils** | Larger application campaign reimplementing common utilities with parity harnesses | [examples/coreutils](https://github.com/faberlang/examples/tree/main/coreutils) |
| **gpu-workload** | GPU / systems workload rungs and contracts | [examples/gpu-workload](https://github.com/faberlang/examples/tree/main/gpu-workload) |
| **scripta / script-kernel** | Scripting and kernel-facing demos | [examples/scripta](https://github.com/faberlang/examples/tree/main/scripta) |
| **automation** | Automation sketch packages | [examples/automation](https://github.com/faberlang/examples/tree/main/automation) |
| **reader-locale** | Locale pack demos for keyword remapping | [examples/reader-locale](https://github.com/faberlang/examples/tree/main/reader-locale) |
| **cista-lab** | Package-store lab material | [examples/cista-lab](https://github.com/faberlang/examples/tree/main/cista-lab) |

### Language corpus {#corpus}

The **corpus** tree is the keyword and construct reference: one directory
per construct, many small `.fab` programs. It is the source of truth for
the generated [Corpus](/corpus/) pages on this site. Since Radix v0.79.0
the exempla live in `radix/corpus/` (the compiler tree); the public surface
is the generated corpus below.

| Surface | URL |
|---|---|
| Generated docs | [/corpus/](/corpus/) |
| Ecosystem note | [Language corpus](/libraries/corpus.html) |

### Stdlib tours {#stdlib}

Norma standard-library exempla live in the **norma** repo, not under
`examples/`:

- [faberlang/norma](https://github.com/faberlang/norma) — `norma/exempla/` when present
- Site: [Norma](/libraries/norma.html)

### Suggested learning order {#order}

1. [Install](/start/install.html) the CLI.
2. Skim [Quick tour](/start/) for language shape.
3. Open **corpus** pages for any keyword you do not recognize ([Corpus hub](/corpus/)).
4. Read **AI Workbench** or **ViviLite** end-to-end for application shape.
5. Use [Syntax](/language/) and [Tooling](/toolchain/) as references while editing.

### Agent path {#agent-path}

- Skill: [examples](/.well-known/agent-skills/examples/SKILL.md)
- Skill: [corpus](/.well-known/agent-skills/corpus/SKILL.md)
- Index: [`/llms.txt`](/llms.txt)

### Previous {#previous}

| Previous | Next |
|---|---|
| [Projects and examples](/start/projects.html) | [Features](/language/) |

## AI Workbench

The AI Workbench is a Faber CLI application for local model inventory,
metadata inspection, embedding, indexing, and inference workflows. It
demonstrates Faber building a substantial multi-command CLI application
with real I/O, JSON output, and Python harness validation.

### Package {#package}

`examples/ai-workbench/packages/faber-ai/` with CLI subcommands:

- `model inspect` — query local model aliases, routes, and status
- `embed` — generate embeddings from text input

### Commands {#commands}

```bash
faber check examples/ai-workbench/packages/faber-ai
faber test examples/ai-workbench/packages/faber-ai
faber run examples/ai-workbench/packages/faber-ai -- model inspect basic/minilm --format json
```

### Validation {#validation}

The AI Workbench includes 20+ Python harness scripts that compare Faber
output against fixture maps for model inventory, inference, GPU evidence,
session lifecycle, and package reuse — demonstrating cross-language
validation of compiled Faber binaries.

## Coreutils

Faber reimplements GNU coreutils as application-lane proof. These are real
CLI programs demonstrating Faber building working binaries with argv, stdio,
exit codes, and host I/O, verified against host GNU utilities via a parity
harness.

### Implemented utilities {#implemented-utilities}

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

### Example — echo {#example--echo}

The `echo` package demonstrates Faber patterns used throughout coreutils:
CLI annotations, option parsing, inline tests with `probandum`/`proba`/`adfirma`,
and shared common modules:

```faber locale=la
importa ex "norma:consolum" privata consolum

functio echo_textus(lista<textus> words) → textus {
    redde ""
}

functio echo_novam_lineam(lista<textus> words) → bivalens {
    redde falsum
}

probandum "echo formatting" tag "coreutils" {
    proba "empty operands" {
        adfirma echo_textus([]) ≡ ""
    }
    proba "-n suppresses newline" {
        adfirma echo_novam_lineam(["-n", "hello"]) ≡ falsum
    }
}

@ cli "echo"
@ descriptio "GNU coreutils echo parity exemplum"
@ operandus ceteri textus words
incipit argumenta args {
    # ... CLI logic here
}
```

### Running {#running}

```bash
faber check coreutils/packages/echo
faber test coreutils/packages/echo
faber run coreutils/packages/echo -- hello world
```
