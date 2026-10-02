# Unit 1 receipt — tree nav engine (seat …bd47b, zai-glm-5.3-flash)

Merged: `d71304b49` → main merge `ffdb50206` (2026-10-02).

- `generator/src/nav.fab` (new, 220 lines): nav tree data (5 buckets + For
  agents compact) + hierarchical renderer — `details.nav-branch`/`summary`
  disclosures, `open` on branches whose subtree carries the active section,
  `active` on the exact item, exact-page vs unique-section mechanics.
- `generator/src/html.fab`: `genera_sidebar` delegates to `nav_mod.genera_nav`;
  grab-bag top block and "Release 1.6.0" block dropped; dead helpers removed.
- 7 × `generator/locales/<locale>/chrome.toml`: `[nav]` flat label table
  (the localization source — `inject-chrome.py` replaces exact strings in
  `<aside>`, longest-first) + `[[nav.group]]` tree schema mirror.
- `generator/www/speculum.css`: `.nav-branch` rules + narrow-width block.

## Consumption path (traced)

html.fab renders from **nav.fab**, not chrome.toml (`norma:toml.parse`
panics; no repo-root anchor in the emitter). chrome.toml `[nav]` labels
drive post-render localization. Adding a sidebar entry = edit nav.fab
(structure + English label) + all 7 chrome.tomls (`[nav]` label +
`[[nav.group]]` mirror). Single-sourcing needs ~6 lines in
`inject-chrome.py::load_chrome` to flatten `[[nav.group]]` labels —
deferred follow-up.

## Measured build baseline (record these in AGENTS.md)

With the pinned toolchain (see below): **cold 114.7 s, warm 112.2 s**,
EXIT=0, all gates green. Also: branch heads are pure disclosures (no
links) — linked branch heads are a polish follow-up.

## Integration toolchain (proven; parent-verified variants)

- **Pinned pair:** `FABER=/tmp/radix-sep30/target/release/faber` (faber
  1.10.0, radix @ 4bf7eee5c Sep 30) + `FABER_SUPPORT_PATH_OVERRIDE=/tmp/container-sep30`
  (+ `FABER_LIBRARY_HOME=/tmp/container-sep30`). Current radix HEAD cannot
  parse the generator (8 PARSE001/PARSE060 — grammar moved after Sep 30);
  1.11.0 parses it but its emit aliases mismatch the post-rename container
  runtime (E0425 ×4, parent-verified 2026-10-02). Quarantine clones:
  `/tmp/radix-sep30`, `/tmp/hosts-sep30`, `/tmp/faber-sep30`; layout
  `/tmp/container-sep30`.
- Step-0 generators resolve CURRENT sibling inputs repo-relatively from
  the main checkout (EBNF, packs, corpus) — the pin only feeds the
  generator build. Parent confirmed `faber check generator` clean under
  1.11.0 with `FABER_LIBRARY_HOME` (useful cross-check, not the build pin).
- Generator manifest: `[target.rust] host = "native"` + `[reader]`
  (renamed from `[locale]`) — parent aligned both during toolchain
  investigation; `host = "native"` is current convention (inferentia
  matches) and resolves only with the support path set.

## Deviations (accepted)

- Runner dropped from MIR (no such page has ever existed — matches unit 4).
- WGSL initially under MIR per the goal sketch — parent moves it under GPU
  at wiring (unit 4 verified the device-lane grouping).
- Old `[sidebar_*]` sections kept (renderbar/agent notice/footer consume).
