# Unit 3b receipt — corpus reference rework (seat …e1b5, zai-glm-5.3-flash)

Merged: `928a34ef5` → main merge `fe66ec36b` (2026-10-02).

- `generator/corpus-categories.toml`: 49 mechanical tags → 9 curated buckets
  + catch-all (Declarations 22, Types 52, Control flow 23, Operators 27,
  Functions 21, Conversions 13, Errors 6, Concurrency 21, Testing 18,
  Other 10 — 213 terms total). Validated at load (dup-tag + catch-all).
- `generator/scripts/corpus_ia.py`: taxonomy loader; semantics from
  `faber explain --list` (one call, `agent_reference.parse_list`);
  breadcrumb + semantics insertion; hub/bucket/A–Z builders; faber
  resolution debug-first + pack staging.
- `render-corpus-batch.sh`: hub renders curated buckets + A–Z link only;
  term pages get breadcrumb + semantics; bucket pages + `az.html`; reader
  transcode via workspace faber; anatomy runs LAST post-process
  (translation-notice pass would break otherwise); manifest counters.
- Verified: `match.html` code reads `match s { case Agens {`;
  `discerne.html` → match alias; az.html 23 letter anchors; hub exactly 10
  buckets, zero legacy category links; en + zh-Hans batch runs (~18s each).

## Nav entries

- Corpus (hub) → `/corpus/index.html` (section `corpus`)
- Terms A–Z → `/corpus/az.html` (section `corpus`)
- Bucket pages `/corpus/bucket/<key>.html` reachable via hub.
- Per-locale labels suggested for hub + A–Z (8 locales, in seat report);
  bucket labels are English today (residual).

## Wiring

None — build-site.sh's existing corpus step picks everything up.

## Residuals (parent-tracked)

- **E0425 root cause (radix-side fix):** HEAD emit still spells
  `faber::display_bivalens` while the faber runtime renamed to
  `faber::display::*` (T1-R5/R5b, 2026-10-02 07:26). The **1.11.0 release
  tarball is a consistent pre-rename pair** — integration builds with
  `/tmp/faber-1.11/bin/faber` (confirmed `faber check` clean with
  `FABER_LIBRARY_HOME` set). Workspace-HEAD builds need the radix fix.
- `faber convert` refuses 317/601 corpus records (no corpus mode / relax
  flag) → those fall back to pack token projection (still reader
  spellings). Real fix is a radix-side corpus convert mode.
- `.expected` diagnostics + Latin string-literal contents stay Latin
  (data, out of scope per goal).
- Semantics coverage 158/213; 55 terms (incl. `json`) have no registry
  entry and correctly get no line.
- Per-locale rollout: en-US + zh-Hans verified; remaining locales take the
  same path in the full build.
- Worktree-only env needs (`FABER_SUPPORT_PATH_OVERRIDE`, radix symlink)
  do not apply to the main checkout.
