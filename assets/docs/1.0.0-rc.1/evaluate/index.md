# Evaluate Faber

Version: `__DOCS_VERSION__`.

Status: local RC1 evaluation draft. This page is not a public release
announcement and does not claim installability.

## What Faber Is

Faber is an intent-first application language for readable source that can be
checked, explained, and carried across execution lanes. The evaluation question
is whether the source remains understandable while the toolchain preserves a
clear capability boundary.

## Who This Is For

The first audience is builders who want application code to remain readable
while targeting more than one runtime or deployment environment.

## Honest RC1-Era Capability

| Area | Local packet claim | Public gate |
| --- | --- | --- |
| Native applications | Locally evidenced as the main product lane. | Public example source plus run evidence. |
| Package binaries | Locally evidenced through package-store work. | Public Cista/package evidence; no live registry claim. |
| Go CLI lane | Narrow and experimental. | Must not be described as general Go support. |
| GPU/browser/backend lanes | Tracked or host-backend work. | No product claim for RC1. |
| Installation | Gated. | Released binary or operator-approved route. |
| Public source | Gated. | Licensing and repo publication decisions. |

## Read-It-Out-Loud Example

```faber
functio greet(name: Text) -> Text {
    redit "salve, " + name
}
```

This snippet is illustrative local copy for the language story. Before public
use, examples need source authority, syntax verification against the released
grammar, and runnability labels.

## Do Not Infer

- a public binary;
- a public source-build path;
- a live package registry;
- production readiness;
- GPU or browser execution;
- adoption, benchmarks, roadmap dates, or public launch status.
