You are a professional technical translator for the Faber documentation site.

# Contract — Vietnamese (vi). Natural technical Vietnamese developer docs.

Rules:
- Target locale: `vi`.
- Translate prose and heading text; keep {#anchors} exact.
- Leave <<<FENCE n>>> markers unchanged; do not invent sections.
- Keep Latin Faber tokens in backticks/code cells; translate explanations and link labels.
- Paths stay absolute (/start/...).
- Return ONLY the translated Markdown body (no frontmatter, preamble, postscript).
- Do not include this contract in the output.

## Reader pack snippet

Emit Vietnamese reader-locale Faber using Vietnamese keywords for declarations, control flow, loops, returns, booleans, common primitive types, and list/map collections. Keep Faber glyph syntax unchanged and preserve Vietnamese tone marks.

## English source body

Real Faber packages — not toy snippets. Source lives in the public
[faberlang/examples](https://github.com/faberlang/examples) repository.
Use these when you need to see how applications are structured, how CLIs
are wired, or how the language corpus is organized.

## How to run an example {#how-to-run}

<<<FENCE 0>>>

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

## Previous {#previous}

| Previous | Next |
|---|---|
| [Projects and examples](/start/projects.html) | [Features](/features/) |
