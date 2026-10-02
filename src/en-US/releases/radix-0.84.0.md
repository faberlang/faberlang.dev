+++
title = "Radix 0.84.0"
section = "releases"
order = 24
sources = []
+++

| Field | Value |
|---|---|
| **Product** | Radix |
| **Version** | 0.84.0 |
| **Source** | Closed for now — see [Open source](/open-source.html) |

## Install this version {#install}

No prebuilt archives were published for this version. It is listed here because its release notes are part of the record.

## Release notes {#notes}

> **Status**: final

Minor component release, companion to Faber v1.9.0. Range: `v0.83.0`
(`1eaf4ec68`, 2026-08-18) → `release/1.9.0` tip `e3af59886` + release
commit (2026-08-26). Headline: **MIR completeness** lands (the Faber
release hold condition), the **stage-4b recipe repair** ends the canary
blind spot, and the window carries the kernel/reduction wave, tensor
glyphs, container-bounds law, and the equality ladder.

**Notes provenance:** companion document to
[`faber/v1.9.0.md`](faber/v1.9.0.md); same window, sources, and receipts.
Factual reconstruction per the release-notes skill — see that document's
provenance block.

### Scale

| Signal | Count |
| --- | ---: |
| Commits (no merges) | 2016 |

Reconstruct the full log:

```bash
git log v0.83.0..e3af59886 --oneline --no-merges
```

### Major tracks

Same window as Faber v1.9.0 — MIR completeness (`9518b21c5`), the
stage-4b per-crate `--no-fail-fast` recipe (main `6c5b42528`, branch
cherry-pick `e3af59886`), kernel/reduction wave, tensor glyphs
(tensor-glyphs-3 U1–U4/U6), container-bounds law (B1 `0598206dd`,
B2 `e46e598c0`), equality ladder (archived). See the Faber notes for
citations.

### Binary question

Unchanged since v0.83.0: Radix is source+tag / library; no product radix
binary, no radix archive, workflow retired (2026-08-25 recomposition).
The shipped CLI is `faber 1.9.0`. This tag (`v0.84.0`) is created locally
and **not pushed**.

### Known-issues

Operator-acked known-red releases are legal (`radix/AGENTS.md`). The
1.9.0 known-red record (7-row acked table + the classification-table 7
unit reds) is recorded verbatim in
[`faber/v1.9.0.md`](faber/v1.9.0.md); it applies to this companion
release identically.

### Verification

Companion receipts in [`faber/v1.9.0.md`](faber/v1.9.0.md): version bump
(39 crates 0.83.0→0.84.0), `cargo update`, locked release build,
manifest validation, `faber-regen-lock --pinned-siblings --check`, the
release-boundary ladder, and the artifact install proof.

---

[All releases](/releases/) · [Install the current release](/start/install.html)
