# Faber — agent guide

You are reading the Markdown agent entry for **Faber**, a package-oriented
programming language. This page is meant for AI agents and automated tools.
Human-oriented HTML starts at https://faberlang.dev/ and
https://faberlang.dev/start/.

## Mission

Help a human (or another agent) **install the CLI**, **understand language
shape**, and **open real application packages** quickly — without inventing
non-canonical syntax.

## Ordered path

1. **Index** — https://faberlang.dev/llms.txt  
2. **This guide** — https://faberlang.dev/agents/index.md  
3. **Skills catalog** — https://faberlang.dev/.well-known/agent-skills/index.json  
4. **Install skill** — https://faberlang.dev/.well-known/agent-skills/install/SKILL.md  
5. **Language skill** — https://faberlang.dev/.well-known/agent-skills/language/SKILL.md  
6. **Examples skill** — https://faberlang.dev/.well-known/agent-skills/examples/SKILL.md  
7. **Expanded map** — https://faberlang.dev/llms-full.txt  

## Install the CLI (current: 1.1.1)

Release: https://github.com/faberlang/releases/releases/tag/faber-v1.1.1

| Platform | Archive |
|---|---|
| macOS arm64 | https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz |
| Linux x64 | https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz |

Extract `faber`, put on `PATH`, run `faber --version`.

HTML install page: https://faberlang.dev/start/install.html

## Minimum language facts

```text
functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ∴ redde nihil
    redde a / b
}
```

- Type-first: `numerus a` not `a: number`.
- Glyphs: `← → ∴ ≡ ∪`.
- Nullable: `T ∪ nihil`.
- Comments: `#` alone on a line only.
- Package: `faber.toml` + `src/`.

## Real-world packages to open first

Repo: https://github.com/faberlang/examples

| Priority | Path | Why |
|---|---|---|
| 1 | `ai-workbench/packages/faber-ai` | Full multi-command CLI application |
| 2 | `vivilite` | Mailspace / agent coordination CLI |
| 3 | `corpus/` | Construct-by-construct programs + docs source |
| 4 | `coreutils` | Larger application campaign |
| 5 | `gpu-workload` | Systems / GPU track |

Site: https://faberlang.dev/start/examples.html

## Commands you will use constantly

```bash
faber check <pkg>
faber build <pkg> -t rust
faber test <pkg>
faber explain <CODE>
faber format <pkg>
```

## Documentation map

| Need | URL |
|---|---|
| Syntax | https://faberlang.dev/syntax/ |
| Tooling | https://faberlang.dev/tooling/ |
| Features | https://faberlang.dev/features/ |
| Corpus pages | https://faberlang.dev/corpus/ |
| Ecosystem | https://faberlang.dev/ecosystem/ |
| EBNF | https://faberlang.dev/references/ebnf.html |

## Skills

| Name | When |
|---|---|
| install | Downloading / verifying the CLI |
| language | Writing or reviewing Faber source |
| packages | Scaffolding or building packages |
| examples | Choosing real apps to study |
| corpus | Looking up a keyword or construct |

## Anti-patterns

- Do not invent C/JS-style type annotations after names.
- Do not use `//` comments.
- Do not invent package layouts when examples already show one.
- Do not claim Radix source is public.
- Do not scrape only the homepage HTML when `/llms.txt` exists.

## Done when

- `faber --version` works on the machine.
- You can name type-first, glyphs, nullable unions, and comment rules.
- You have opened at least one application package under `examples/`.
- You can point a human to install + examples + the skill they need next.
