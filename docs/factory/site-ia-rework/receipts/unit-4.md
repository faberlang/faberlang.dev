# Unit 4 receipt — By Target + releases (seat …a3e39, deepseek-flash)

Merged: `6c81ddd5b` + `224ad6a94` → main merge `993f4400b` (2026-10-02).

- By Target hub grouped HIR/MIR/GPU; 12 lane pages regenerated through
  `generate-target-lanes.py`; measured feature tables from the matrix data.
- `capture-target-panels.sh` + committed `generator/target-panels/` cache
  (rust, ts, go, faber, llvm-text, wasm-text panels from 4 exemplars).
- Releases refreshed through **faber 1.11.0** and radix 0.84.0 notes pages.
- Corrections vs the goal sketch: **WGSL is GPU/device, not MIR**; **no
  runner page** (`radix emit --target runner` rejects it — matrix-only).
- No build-site.sh wiring (panels are a committed cache; step 0b already
  runs the lane generator).

## Nav entries (By target group)

- All targets → `/en-US/targets/` (section `targets`)
- HIR — application → `/en-US/targets/hir.html` (section `hir`); children:
  Rust `rust.html`, TypeScript `ts.html`, Go `go.html`, Faber `faber.html`
- MIR — systems → `/en-US/targets/mir.html` (section `mir`); children:
  LLVM IR `llvm-text.html`, WebAssembly text `wasm-text.html`
- GPU — device → `/en-US/targets/gpu.html` (section `gpu`); children:
  WGSL `wgsl-text.html`, Metal `metal-text.html`

Per-locale labels supplied in the seat report (group noun translations for
ar/hi/th-TH/vi/zh-Hans/zh-Hant; product names stay Latin). Page title stays
"Target lanes" (smoke gate).

## Sidebar pin facts

**faber 1.11.0** (published 2026-10-02):
- https://github.com/faberlang/releases/releases/download/faber-v1.11.0/faber-v1.11.0-aarch64-apple-darwin.tar.gz
- https://github.com/faberlang/releases/releases/download/faber-v1.11.0/faber-v1.11.0-x86_64-unknown-linux-gnu.tar.gz

Newest *downloadable* radix stays 0.81.0 (0.82–0.84 are notes-only, no
GitHub release/archives).

## Residuals (parent-tracked)

- Generator rebuild blocked under faber 1.10.0 (`E0425 display_bivalens`);
  needs 1.11.0 toolchain.
- Device emit regression (metal-text/wgsl-text `mir_metal_text_unsupported`
  despite `@ nucleum`) — compiler-side; file against radix.
- `generate-releases.py` `notes_dir` points at the retired
  `faber/docs/release`; notes live in `radix/docs/release/faber/` —
  parent fixes the script.
- Release regen overwrote hand-curated sections in `faber-1.8.0.md`
  (Inference/Language/Formats/Quality/Infrastructure + radix pin) —
  parent verifies whether the imported notes carry the content or ports it.
- Lane set curated: swift/python/haskell/sexp/fhir/llvm-host/fmir remain
  page-less by design (non-goal).
