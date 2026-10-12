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

Five minutes to the shape of Faber: install the CLI, read one function,
then open a real package. For a sequenced path, follow: [Install](/start/install.html) →
[Hello](/start/hello.html) → [Commands](/start/commands.html) →
[Projects](/start/projects.html).

## 1. Install the CLI {#install}

Download the current release (**1.1.1**) for your platform from the
[install page](/start/install.html), verify the archive checksum, and put the
extracted `faber-v1.1.1-<target-triple>/faber` binary on your `PATH`. Confirm:

<<<FENCE 0>>>

## 2. Shape of a function {#shape}

Type-first parameters, glyph return type, Latin control words, nullable
union:

<<<FENCE 1>>>

| Signal | Meaning |
|---|---|
| `functio` | Function declaration |
| `numerus a` | Type first, then name |
| `→` | Return type |
| `∪ nihil` | Nullable (`T ∪ nihil`) |
| `si … ∴` | Compact branch |
| `redde` | Return |

## 3. Package layout {#package}

A package is a directory with `faber.toml` and `src/`:

<<<FENCE 2>>>

Typical commands:

<<<FENCE 3>>>

Details: [Faber build tool](/tooling/faber-build-tool.html).

## 4. Real applications {#applications}

Do not stop at hello-world. The public **examples** repo has multi-command
CLIs, a local mailspace, GPU workload tracks, and a full language corpus.

| Package | What it shows |
|---|---|
| AI Workbench | Multi-command CLI, model inspect, embeddings |
| ViviLite | File-backed mailspace / agent coordination CLI |
| coreutils | Larger application campaign (parity harnesses) |
| gpu-workload | Systems / GPU rungs |
| corpus | One directory per language construct |

Browse them on the [examples page](/start/examples.html).

## 5. If you are an agent {#agents}

1. Read [`/llms.txt`](/llms.txt).
2. Open [`/agents/index.md`](/agents/index.md).
3. Pick a skill from [`/.well-known/agent-skills/index.json`](/.well-known/agent-skills/index.json).

## Start track {#start-track}

| Step | Page | Outcome |
|---|---|---|
| 1 | [Install & download](/start/install.html) | Put Faber 1.1.1 on `PATH` and verify it |
| 2 | [Hello, Faber](/start/hello.html) | Create and run `salve-munde` |
| 3 | [Commands you will use](/start/commands.html) | Learn `check`, `build`, `run`, `test`, `explain` |
| 4 | [Projects and examples](/start/projects.html) | Move into real packages and corpus pages |

## Next {#next}

| Topic | Link |
|---|---|
| Install & download | [Install](/start/install.html) |
| Hello, Faber | [Hello](/start/hello.html) |
| Commands | [Commands](/start/commands.html) |
| Projects | [Projects](/start/projects.html) |
| Syntax reference | [Syntax](/syntax/) |
| Features (locales, lanes) | [Features](/features/) |
| Ecosystem libraries | [Ecosystem](/ecosystem/) |
| Keyword corpus | [Corpus](/corpus/) |
