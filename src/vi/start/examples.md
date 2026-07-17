+++
title = "Examples"
section = "examples"
order = 2
sources = [
  "examples/README.md",
  "examples/ai-workbench/",
  "examples/vivilite/",
]
translation_kind = "fallback"
source_locale = "en-US"
source_hash = "sha256:902bb133adf106a6e1ce96c44c872f7b3a912a0c0ddcb54fa36cfd0bfff20543"
+++
**Translation status:** Vietnamese reader-locale proof. Prose falls back to the English source for this Stage 7 slice; Faber code fences pass through the `vi` render step during the site build.


Real Faber packages — not toy snippets. Source lives in the public
[faberlang/examples](https://github.com/faberlang/examples) repository.
Use these when you need to see how applications are structured, how CLIs
are wired, or how the language corpus is organized.

## How to run an example {#how-to-run}

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

## Application packages {#applications}

| Package | Role | Start here |
|---|---|---|
| **AI Workbench** | Multi-command CLI for local model inventory, embeddings, and inference workflows; Python harness validation | [examples/ai-workbench](https://github.com/faberlang/examples/tree/main/ai-workbench) · site: [AI Workbench](/ecosystem/ai-workbench.html) |
| **ViviLite** | Faber-native local mailspace CLI (file-backed + optional SQLite lane) for agent coordination commands | [examples/vivilite](https://github.com/faberlang/examples/tree/main/vivilite) |
| **coreutils** | Larger application campaign reimplementing common utilities with parity harnesses | [examples/coreutils](https://github.com/faberlang/examples/tree/main/coreutils) |
| **gpu-workload** | GPU / systems workload rungs and contracts | [examples/gpu-workload](https://github.com/faberlang/examples/tree/main/gpu-workload) |
| **scripta / script-kernel** | Scripting and kernel-facing demos | [examples/scripta](https://github.com/faberlang/examples/tree/main/scripta) |
| **automation** | Automation sketch packages | [examples/automation](https://github.com/faberlang/examples/tree/main/automation) |
| **reader-locale** | Locale pack demos for keyword remapping | [examples/reader-locale](https://github.com/faberlang/examples/tree/main/reader-locale) |
| **cista-lab** | Package-store lab material | [examples/cista-lab](https://github.com/faberlang/examples/tree/main/cista-lab) |

## Language corpus {#corpus}

The **corpus** tree is the keyword and construct reference: one directory
per construct, many small `.fab` programs. It is the source of truth for
the generated [Corpus](/corpus/) pages on this site.

| Surface | URL |
|---|---|
| Source tree | [examples/corpus](https://github.com/faberlang/examples/tree/main/corpus) |
| Generated docs | [/corpus/](/corpus/) |
| Ecosystem note | [Language corpus](/ecosystem/corpus.html) |

## Stdlib tours {#stdlib}

Norma standard-library exempla live in the **norma** repo, not under
`examples/`:

- [faberlang/norma](https://github.com/faberlang/norma) — `norma/exempla/` when present
- Site: [Norma](/ecosystem/norma.html)

## Suggested learning order {#order}

1. [Install](/start/install.html) the CLI.
2. Skim [Quick tour](/start/) for language shape.
3. Open **corpus** pages for any keyword you do not recognize ([Corpus hub](/corpus/)).
4. Read **AI Workbench** or **ViviLite** end-to-end for application shape.
5. Use [Syntax](/syntax/) and [Tooling](/tooling/) as references while editing.

## Agent path {#agent-path}

- Skill: [examples](/.well-known/agent-skills/examples/SKILL.md)
- Skill: [corpus](/.well-known/agent-skills/corpus/SKILL.md)
- Index: [`/llms.txt`](/llms.txt)
