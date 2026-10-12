# Production residual English pass

**Date:** 2026-07-20  
**Scope:** all 6 locales × 48 pages (prose outside code fences)

## Method

1. Scan body text **outside** ` ``` ` fences (fence comments stay English by
   design — `sync-translate --merge-en-fences` and EN source comments).
2. Flag English section headings, table chrome, nav labels, pending markers.
3. Fix clear heading leftovers; leave intentional Latin product names
   (`macOS arm64`, `si / sin / secus`, `Lista`, HIR/MIR/WASM, …).

## Intentional English (do not “fix”)

| Class | Examples |
|---|---|
| Code comments in fences | `# Clone examples`, `# shared borrow — caller retains ownership` |
| Product / platform names | `macOS arm64`, `Linux x64`, `GitHub`, `Homebrew` |
| Latin Faber keywords in headings | `si / sin / secus`, `fixum`, `probandum` |
| IR / target names | HIR, MIR, WASM, LLVM, WGSL |
| Package names | Norma, Triga, Coreutils, Cista |

## Fixed this pass

| Locale | File | Fix |
|---|---|---|
| th-TH, zh-Hans, zh-Hant, vi | `start/commands.md` | Localize Check / Build / Run headings |
| zh-Hant | `start/commands.md` | Localize Explain diagnostics, Reader-locale commands |
| th-TH | `features/frames.md` | Compile manifest heading |
| hi | `features/frames.md` | 6 English section headings → Hindi |
| hi | `features/canonical-vs-sugar.md` | 5 English section headings → Hindi |
| hi | `syntax/functions.md` | Entry point headings → Hindi |
| vi | `features/frames.md` | Wrapper Norma → Bao bọc Norma |
| vi | `features/compilation-lanes.md` | Backend HIR-direct → HIR-trực tiếp |

## Residual after pass

Re-scan targets **zero** high-priority prose heading leftovers (product/Latin
allowlisted). Mixed code-switching in body prose (tech loans) remains acceptable
for developer docs.

## Recommended follow-ups (optional)

1. Spot-read `hi/features/frames.md` and `hi/features/canonical-vs-sugar.md` body
   register (headings fixed; some sentences still heavily code-mixed).
2. Optional xhigh polish on start track for Luna locales (th, hi, vi, zh-Hant).
3. Build + visual check locale switcher on live site.
