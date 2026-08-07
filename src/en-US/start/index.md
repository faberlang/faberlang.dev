+++
title = "Quick tour"
section = "start"
order = 0
sources = []
+++

Five minutes to the shape of Faber: install the CLI, read one function,
then open a real package. For a sequenced path, follow: [Install](/start/install.html) →
[Hello](/start/hello.html) → [Commands](/cheatsheet/commands.html) →
[Projects](/start/projects.html).

## 1. Install the CLI {#install}

Download the current release (**1.4.0**) for your platform from the
[install page](/start/install.html), verify the archive checksum, and put the
extracted `faber-v1.4.0-<target-triple>/faber` binary on your `PATH`. Confirm:

```bash
faber --version
```

## 2. Shape of a function {#shape}

Type-first parameters, glyph return type, Latin control words, nullable
union:

```text
functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ergo redde nihil
    redde a / b
}
```

| Signal | Meaning |
|---|---|
| `functio` | Function declaration |
| `numerus a` | Type first, then name |
| `→` | Return type |
| `∪ nihil` | Nullable (`T ∪ nihil`) |
| `si … ergo` | Compact branch |
| `redde` | Return |

## 3. Package layout {#package}

A package is a directory with `faber.toml` and `src/`:

```text
my-app/
  faber.toml
  src/
    main.fab
```

Typical commands:

```bash
faber check my-app/
faber build my-app/ -t rust
faber run my-app/
faber test my-app/
```

Details: [Faber build tool](/toolchain/cli.html).

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

Browse them on the [examples page](/examples/).

## 5. If you are an agent {#agents}

1. Read [`/llms.txt`](/llms.txt).
2. Open [`/agents/index.md`](/agents/index.md).
3. Pick a skill from [`/.well-known/agent-skills/index.json`](/.well-known/agent-skills/index.json).

## Start track {#start-track}

| Step | Page | Outcome |
|---|---|---|
| 1 | [Install & download](/start/install.html) | Put Faber 1.4.0 on `PATH` and verify it |
| 2 | [Hello, Faber](/start/hello.html) | Create and run `salve-munde` |
| 3 | [Commands you will use](/cheatsheet/commands.html) | Learn `check`, `build`, `run`, `test`, `explain` |
| 4 | [Projects and examples](/start/projects.html) | Move into real packages and corpus pages |

## Next {#next}

| Topic | Link |
|---|---|
| Install & download | [Install](/start/install.html) |
| Hello, Faber | [Hello](/start/hello.html) |
| Commands | [Commands](/cheatsheet/commands.html) |
| Projects | [Projects](/start/projects.html) |
| Syntax reference | [Syntax](/language/) |
| Features (locales, lanes) | [Features](/language/) |
| Ecosystem libraries | [Ecosystem](/libraries/) |
| Keyword corpus | [Corpus](/corpus/) |
