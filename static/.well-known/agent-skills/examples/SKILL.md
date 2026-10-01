---
name: "examples"
description: "Open real application packages in faberlang/examples (AI Workbench, ViviLite, coreutils, GPU, corpus)."
---

# Real-world Faber examples

## Use this skill when

- a human wants to see non-toy Faber applications
- you need package layout precedents
- you are teaching application structure

## Write first

Writing Faber starts at https://faberlang.dev/agents/index.md. Follow only the links that page names. The repositories below are applications, not the writing guide.

## Source

- Repo: https://github.com/faberlang/examples

## Open these first

| Order | Path | Why |
|---|---|---|
| 1 | `ai-workbench/packages/faber-ai` | Multi-command CLI; model inspect / embed; harnesses |
| 2 | `vivilite` | Local mailspace / agent coordination CLI |
| 3 | `coreutils` | Larger application campaign + parity harnesses |
| 4 | `gpu-workload` | Systems / GPU rungs |
| 5 | `corpus/` | Construct-level programs |

## How to exercise

```bash
git clone https://github.com/faberlang/examples.git
faber check examples/ai-workbench/packages/faber-ai
faber test examples/ai-workbench/packages/faber-ai
```

Read the package `README.md` for exact run arguments.

## Related

- https://faberlang.dev/agents/index.md
- https://faberlang.dev/agents/packages.md
- https://faberlang.dev/agents/libraries.md
- skill: `packages`
- skill: `corpus`
- skill: `install`
