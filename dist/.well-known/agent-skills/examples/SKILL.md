---
name: "examples"
description: "Open real application packages in faberlang/examples (AI Workbench, ViviLite, coreutils, GPU, corpus)."
---

# Real-world Faber examples

## Use this skill when

- a human wants to see non-toy Faber applications
- you need package layout precedents
- you are teaching application structure (CLI, I/O, multi-command tools)

## Source

- Repo: https://github.com/faberlang/examples
- Site: https://faberlang.dev/start/examples.html

## Open these first

| Order | Path | Why |
|---|---|---|
| 1 | `ai-workbench/packages/faber-ai` | Multi-command CLI; model inspect / embed; harnesses |
| 2 | `vivilite` | Local mailspace / agent coordination CLI |
| 3 | `coreutils` | Larger application campaign + parity harnesses |
| 4 | `gpu-workload` | Systems / GPU rungs |
| 5 | `corpus/` | Construct-level programs (also drives docs) |

## How to exercise

```bash
git clone https://github.com/faberlang/examples.git
# often also: git clone https://github.com/faberlang/norma.git
faber check examples/ai-workbench/packages/faber-ai
faber test examples/ai-workbench/packages/faber-ai
```

Always read the package `README.md` for exact run arguments.

## Site cross-links

- AI Workbench: https://faberlang.dev/ecosystem/ai-workbench.html
- Corpus hub: https://faberlang.dev/corpus/
- Norma: https://faberlang.dev/ecosystem/norma.html

## Related

- skill: `packages`
- skill: `corpus`
- skill: `install`
