+++
title = "History"
section = "history"
order = 0
sources = []
+++

## Origins {#origins}

The first commit to the Radix compiler was made on **December 20, 2025**
as a Bun + TypeScript project with a single `docs/decisions.md` file. The
second commit codified five Architecture Decision Records that still shape
the language today.

**ADR-003**, titled "Case endings carry semantic meaning," established at
the very beginning that Latin morphology would be more than a
keyword-skin — the compiler would understand declension and conjugation
to infer program intent. The original case mappings were:

```text
Nominative  (subject)       →  return value, caller
Accusative  (direct object)  →  primary argument
Dative      (indirect obj.)  →  recipient, callback, destination
Genitive    (possession)     →  property access, "of" relationships
Ablative    (instrument)     →  dependencies, context, "using X"
```

The same document noted: *"Verb conjugation is a natural follow-on
question (future tense → async?)."* This seed grew into the modern
**morphologia** naming convention, where the standard library uses
conjugated Latin verb forms to signal sync vs async and mutate vs
copy-out — without requiring the compiler itself to understand Latin
grammar.

The project began in TypeScript, was later rewritten in Rust, and the
grammar was frozen for the 1.x line with edition 2026. The original five
ADRs (file extension `.fab`, error hints, case endings, recursive descent
parser, custom AST) are still visible in the git history.

## Releases {#releases}

Prebuilt CLI archives — current Faber release at the top, then every published
tag and binary from [faberlang/releases](https://github.com/faberlang/releases):

- **[Releases](/history/releases.html)** — download links and historical inventory
- **[Install and download](/start/install.html)** — PATH setup and first `faber check`
