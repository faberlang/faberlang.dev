+++
title = "Reference"
section = "reference"
order = 0
sources = []
+++

Look-up surfaces. Nothing here teaches — these are the pages you come back to
with a specific question.

## Answering a specific question {#lookup}

| Question | Go to |
|---|---|
| Is this valid syntax? | [Grammar](/reference/grammar.html) — the full EBNF |
| Does target X support construct Y? | [Target matrix](/toolchain/target-matrix.html) — measured, per term |
| How does this keyword behave? | [/corpus/](/corpus/), or `faber explain <term>` |
| What changed in this version? | [Releases](/reference/releases.html) |
| Why is the language like this? | [Design notes](/reference/design.html) |
| Where does the source live? | [Repositories](/reference/repositories.html) |

The fastest of these is usually the CLI:

```bash
faber explain redde
faber explain ⇥
faber targets
```

## From the terminal {#cli-reference}

`faber explain` reads the same corpus that generates these pages, so it will
not drift from the site. `faber targets` prints the live capability notes for
every backend — the same data the target matrix is built from.

## Machine surfaces {#machine}

These are locale-less and live at the site root, not under `/reference/`:

| Surface | Purpose |
|---|---|
| [`/llms.txt`](/llms.txt) | index for models — start here |
| [`/llms-full.txt`](/llms-full.txt) | expanded corpus frontmatter reference |
| [`/agents/index.md`](/agents/index.md) | learning path for agents |
| [`/.well-known/agent-skills/`](/.well-known/agent-skills/index.json) | focused skill guides |

## Pages here {#pages}

| Page | What it is |
|---|---|
| [Grammar](/reference/grammar.html) | formal EBNF for every production |
| [Releases](/reference/releases.html) | generated release inventory with assets and checksums |
| [Design notes](/reference/design.html) | the design laws, deferred features, and how the language got here |
| [Repositories](/reference/repositories.html) | the faberlang organization, repo by repo |
