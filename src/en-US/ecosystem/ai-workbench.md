+++
title = "AI Workbench"
section = "ecosystem"
order = 4
sources = [
  "examples/ai-workbench/ (README.md, package, harness)",
]
+++

The AI Workbench is a Faber CLI application for local model inventory,
metadata inspection, embedding, indexing, and inference workflows. It
demonstrates Faber building a substantial multi-command CLI application
with real I/O, JSON output, and Python harness validation.

## Package

`examples/ai-workbench/packages/faber-ai/` with CLI subcommands:

- `model inspect` — query local model aliases, routes, and status
- `embed` — generate embeddings from text input

## Commands

```bash
faber check examples/ai-workbench/packages/faber-ai
faber test examples/ai-workbench/packages/faber-ai
faber run examples/ai-workbench/packages/faber-ai -- model inspect basic/minilm --format json
```

## Validation

The AI Workbench includes 20+ Python harness scripts that compare Faber
output against fixture maps for model inventory, inference, GPU evidence,
session lifecycle, and package reuse — demonstrating cross-language
validation of compiled Faber binaries.
