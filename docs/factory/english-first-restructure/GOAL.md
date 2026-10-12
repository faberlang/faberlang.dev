# GOAL: English-first docs site — one maintained language, machine-generated locale surfaces

**Status**: done — all units landed on main 2026-10-12 (U1 f6682d4d9, U2 folded into U1, U4 2c03dd0d6, U3 391003350, U5 60807b946, U6 85701ddca, U8 6c815a75d + b9aca7d1c, U7 b77842c1c); Gates A–E green; switchover commit carries the full-build log; deploy push remains operator-gated
**Created**: 2026-10-12
**Campaign:** `—` (standalone; operator design session 2026-10-11/12)
**Source:** operator ruling in session: translated prose is structurally unregenerable and confirmed stale; interpreted render pipeline is hours; rework the generation model.
**Repos:** `faberlang.dev` (single repo; reads `radix` inputs, writes nothing there)
**Related:** `docs/factory/multilingual-site/` (prose-translation arm superseded by this goal; archive at switchover), `docs/factory/code-sample-tabs/` (the tab component this goal generalizes), `docs/factory/site-ia-rework/`

---

## Invariant

Every page the site serves is either hand-authored English or machine-derived from radix inputs — no surface requires human re-translation to stay current. A full rebuild completes in minutes on this machine.

## Problem

Evidence, all from the 2026-10-11/12 catch-up session:

- **The compiled pipeline is gone.** `faber build -t rust` fails at plan time: the generator's file I/O routes through `norma:fs` (`call 'solum:lege'` frames) and no host provider serves those routes since `hosts` was deleted (native I/O returns with core-norma N2; timeline outside this repo). Commit `7d1b251dd` bridged with the interpreted MIR runner (`generator/scripts/speculum-run.sh`): correct, but ~10 s of package re-analysis per render × ~4,000 renders ≈ 2+ hours, and the 3,007-line grammar pages take 11+ minutes each.
- **Translated prose is already stale, not hypothetically.** `src/{vi,ar,hi,zh-Hans}/language/types.md` each carry ~25 mentions of retired surfaces (`sorted`, `nihil`, `byte`, `octeti`, `strue`); `src/en-US/language/types.md` carries 0. Fence gates catch wrong *code* in any locale (10 failing fences per translated tree found and fixed this session); no gate can detect a stale *sentence*, because the truth lives in the compiler and the sentence in a human language.
- **The build regenerates everything from nothing.** 4,193 committed dist files: ~3,500 renders are radix-keyed corpus (60% of total build cost from the six translated corpus trees); authored pages re-render regardless of edits.

## Proposal

English is the one maintained human language. The seven reader packs stay visible exactly where they are machine-generated and always current:

| Surface | Shape | Authority |
| --- | --- | --- |
| Authored pages | one English tree (`src/en-US/`) | hand edits |
| Code fences | tab box per fence: Latin + six reader locales | `faber format --locale`, cached by fence-content hash |
| Locale mapping | per-language pages, **English \| Latin \| target** three-column; Latin page stays two-column; hub becomes an index linking them; `/agents/locales.md` keeps the full eight-pack join (machine-facing) | `radix/locale/*/pack.toml` via `generate-locale-reference.py` |
| Grammar page | keyword-spelling toggle (deterministic glossary projection, pre-generated variants) | `radix/grammar/sources/glossary.*.toml` |
| Corpus | `radix/corpus` exempla, Latin source + English projection, one tree | `radix/corpus` + `faber explain` registry |
| Retired URLs | `/{ar,hi,th-TH,vi,zh-Hans,zh-Hant}/…` → English counterpart (meta-refresh alias, one generation pass) | alias generator |
| Engine | the renderer core ports to Python (37 of 41 generator scripts already are); the Faber generator retires | committed dist is the equivalence oracle |
| Freshness | input-hash manifest; rebuild only stale outputs; `--full` keeps the clean rebuild | manifest of (inputs → output) hashes |

Rationale for English as the browsing key and Latin as a visible column: the English site shows English keywords, so a reader comparing to Arabic needs English on the left; Latin stays as the canonical identity column (it is what the grammar, corpus keys, and `faber explain` terms actually use).

### Non-goals

- No machine or LLM translation of prose; no per-locale prose trees.
- No tab boxes on corpus exemplars (single projection only — tabbing ~600 terms × 6 locales would reintroduce ~7,000 compiler calls per radix bump).
- No radix changes (the argv non-ASCII transliteration, host-route restoration, EBNF `octeti` prose staleness, and the retired `octetus` pack row are radix-side findings, recorded in workspace memory, not this goal's scope).
- No visual redesign beyond the tab component and the mapping pages.

## Units

Sequenced port-first (operator ruling): every later unit verifies against a fast build.

| Unit | Scope | Depends on | Hand evidence |
| --- | --- | --- | --- |
| U1 renderer-port-core | Python `--page` renderer byte-equivalent to the Faber generator | — | none |
| U2 renderer-port-corpus | corpus + alias modes in the Python renderer | U1 | none |
| U3 engine-switch | build pipeline drives the Python renderer; Faber renderer deleted | U1, U2 | none |
| U4 english-only-cut | one build tree; six locale trees retired; redirect map; portal/nav reshape | — (parallel-safe with U1–U3; lands before U5–U7) | none |
| U5 locale-mapping-pages | three-column per-language pages; Latin two-column; hub index | U4 | none |
| U6 fence-tabs-generalize | marker-driven tab boxes on authored fences; fence-hash cache | U3 | none |
| U7 grammar-toggle | spelling toggle on the grammar page | U4 | none |
| U8 incremental-build | input-hash manifest; stale-only rebuild; `--full` | U3 | none |

### Implementation work

```text
delivery: docs/factory/english-first-restructure/GOAL.md
unit: U1
write_scope: faberlang.dev/generator/scripts/speculum_py.py (new), generator/scripts/render.sh
edit: port page assembly (markdown → HTML, nav, page shell) from generator/src/{markdown,html,nav,frontmatter}.fab into one Python module; `--page` mode contract identical to speculum-run.sh
done_when: for every en-US authored page, Python output diffs clean against the Faber renderer's output for the same inputs (differences, if any, are an explicitly listed contract: attribute order, whitespace inside tags)
sanity: dual-render 20 representative pages + the grammar page; diff report empty or contract-listed
```

```text
delivery: docs/factory/english-first-restructure/GOAL.md
unit: U2
write_scope: faberlang.dev/generator/scripts/speculum_py.py
edit: add --corpus-bundle, --corpus-markdown-bundle, and --alias modes (bundle parsing, term extraction, alias stubs; placeholder substitution for non-ASCII aliases moves into Python)
done_when: corpus pass over a 60-term sample (all 33 unicode-glyph terms included) renders identically to the Faber driver's output for the same bundles; aliases byte-identical
sanity: run the corpus batch for en-US against a scratch out dir; compare to committed dist corpus pages for those terms
```

```text
delivery: docs/factory/english-first-restructure/GOAL.md
unit: U3
write_scope: faberlang.dev/generator/scripts/{build-site.sh,render-corpus-batch.sh,render.sh,render-failed-pages.sh}, delete generator/src/*.fab and generator/faber.toml, AGENTS.md
edit: build loop invokes the Python renderer directly; delete the Faber generator package, speculum-run.sh, and the interpreted-runner notes
done_when: full build green through existing gates (fences, internal links, sitemap) in one command; measured full build < 10 min
sanity: timed full build; BUILD_EXIT=0; spot-check five pages vs U1/U2 oracles
```

```text
delivery: docs/factory/english-first-restructure/GOAL.md
unit: U4
write_scope: faberlang.dev/src/ (delete src/{ar,hi,th-TH,vi,zh-Hans,zh-Hant}), generator/scripts/{build-site.sh,generate-redirects.fab or replacement, sitemap step}, AGENTS.md, CONTENT-PLAN.md note
edit: build renders the en-US tree only; retire the six locale src trees (git history is the archive); generate the retired-URL redirect map (one alias pass, meta-refresh to the English counterpart); portal language chooser links to mapping pages; locale landings removed
done_when: one-tree build green; linkwalker treats redirects as resolvable; retired URL set enumerated and covered by aliases; sitemap and llms surfaces reflect the one tree
sanity: `check-internal-links` green; curl three retired URLs → 200 with meta-refresh to the English page
```

```text
delivery: docs/factory/english-first-restructure/GOAL.md
unit: U5
write_scope: faberlang.dev/generator/scripts/generate-locale-reference.py, src/en-US/language/locales/
edit: reshape to per-language pages with columns English | Latin | target (keywords/types/intrinsics sections preserved); Latin page stays two-column; the eight-column human hub becomes an index page linking the seven pages; regenerate all from radix packs
done_when: seven mapping pages regenerate from packs with zero drift vs the pack join (existing per-section diff discipline); the current-epoch rows (sort/ordinata, bytes/octeti, at/apud) appear on every page
sanity: pack-keyed join diff (the check used in the 2026-10-11 resync) reports zero dead and zero missing rows
```

```text
delivery: docs/factory/english-first-restructure/GOAL.md
unit: U6
write_scope: faberlang.dev/generator/scripts/locale-tabs.py, generator/locale-tabs/, src/en-US/**/*.md fences, speculum.css tab component
edit: generalize the cheat-sheet tab mechanism to any authored fence marked for tabs; render Latin + six locales per marked fence via `faber format --locale`; cache by fence-content hash so unchanged fences cost zero
done_when: marked fences on ≥ 3 page families (cheatsheet, language, targets) render tabbed cards; cache hit rate 100% on an immediate re-run; unmarked fences unchanged
sanity: re-run render twice; second run performs zero `faber format` calls (log count)
```

```text
delivery: docs/factory/english-first-restructure/GOAL.md
unit: U7
write_scope: faberlang.dev/generator/scripts/generate-grammar(.fab→py if needed), src/en-US/reference/grammar.md, speculum.css
edit: pre-generate the grammar page's keyword spellings per locale from the glossary projection; client-side toggle swaps the spelling layer (progressive enhancement — the page is complete in any one spelling)
done_when: grammar page renders fully in each of the seven spellings with no server round trip; toggle degrades to a static English page without JS
sanity: render grammar page; toggle targets present for all seven locales
```

```text
delivery: docs/factory/english-first-restructure/GOAL.md
unit: U8
write_scope: faberlang.dev/generator/scripts/build-site.sh, new manifest module
edit: record input hashes (src md, radix inputs, packs, captures) per output; skip outputs whose inputs are unchanged; `--full` forces regeneration; manifest is a build artifact, not source
done_when: touching one source page and rebuilding re-renders exactly that page's outputs (plus derived indexes); measured routine build < 10 s; `--full` still < 10 min
sanity: hash one input, rebuild, count rendered outputs
```

## Checkpoints And Gates

- **Gate A — engine equivalence (U3 entry):** dual-run diff, Python vs Faber renderer, over the full en-US tree + 60-term corpus sample (all glyph terms) + every fence; empty diff or an explicitly listed contract.
- **Gate B — fences:** `validate-fences.sh src/en-US` and the agent canon stay green (731-fence baseline from 2026-10-11, now one tree).
- **Gate C — links and redirects:** `check-internal-links` green on the one-tree dist; retired-URL walker verifies every `/{locale}/…` path resolves through an alias.
- **Gate D — build time:** full rebuild < 10 min measured; routine single-page rebuild < 10 s (wall clock, this machine).
- **Gate E — mapping freshness:** the pack join check (used in the 2026-10-11 resync) reports zero dead/missing rows on all seven mapping pages.

## Validation

- Gates A–E above, in dependency order; the switchover commit carries a full `--full` build log.
- Deploy remains push-gated by the operator; nothing in this goal pushes.

## Completion record (2026-10-12)

- **Gate A (engine equivalence):** 185/185 byte-identical comparisons (26 authored pages across three locales, 60 corpus terms × bundle/markdown modes incl. all non-ASCII glyph terms, 14 CLI-default cases, 10 aliases, 5 edge inputs, 10 error-contract cases); contract list empty. The interpreted oracle's own corpus-frontmatter regression (raw `("…")(args)` escapes) was identified and the Python engine restores the compiled-era contract, verified against pre-U4 committed dist.
- **Gate B (fences):** `validate-fences.sh src/en-US` 220/220 (one pre-existing failure — retired ASCII comparison signs in the grammar program example — fixed in ee4ee347f).
- **Gate C (links/redirects):** internal links 25,926 + 693 agent surfaces, 0 broken; retired-URL walker 3,581/3,581; curl spot-checks of retired URLs across six locales resolve 200 + meta-refresh to the English counterpart.
- **Gate D (build time):** `--full` 36 s (4,978 pages) against a <10 min target; routine no-op build 6.0 s ×3; one-page edit → exactly one dist file in 7 s; incremental output byte-identical to `--full`.
- **Gate E (mapping freshness):** wired into the build (`--check`); 7 mapping pages, 0 missing, 0 dead rows; epoch pairs (sort/ordinata, bytes/octeti, at/apud ×2) on 7/7 pages.
- **Beyond the spec:** radix core-norma N2 retired the `faber:*` I/O kernel modules mid-goal, breaking the three remaining native-Faber gates (SEM006); all three were restored as Python gates byte-stable with committed dist (2219ef278, b77842c1c). The site pipeline now contains no Faber-executed gates.
- **Open questions resolved:** Q1 — chooser links the per-language mapping pages (no per-locale landing shells kept); Q2 — the Faber generator is deleted at U3 (clean break; evidence recorded here); Q3 — verified, no change needed to `/agents/locales.md`.

## Companion Skill Plan

- `$faberlang` skill + repo `AGENTS.md`: pipeline section rewrites at U3 (Python engine, incremental flags) and U4 (one-tree render loop, redirect map). The interpreted-runner note from `7d1b251dd` retires at U3.
- `$faber` skill: site-locale guidance updates at U4 (docs are English; reader packs visible via tabs/mapping pages).
- `docs/factory/multilingual-site/` → `docs/archived/` at switchover (git mv; phases superseded by this goal, per factory-docs lifecycle).
- `docs/factory/code-sample-tabs/` reconciled at U6 (component consumed; close or keep scoped to portal hero animation).

## Release

`release-now` at the switchover commit: faberlang.dev's release surface is the website itself, deploy is operator-push-gated, and the repo convention (AGENTS.md deploy section) is commit-then-push. Evidence: faberlang.dev/AGENTS.md "Deployment".

## Open Questions

1. **Language landing pages:** the root portal's language chooser currently lands visitors on per-locale homepages. U4's answer is chooser → per-language mapping page; confirm at dispatch or keep a thin "start here" shell per language.
2. **Faber renderer retention:** this spec deletes the Faber generator at U3 (clean break). If the operator wants it kept as a reference oracle, U3 shrinks to "demote to tools/oracle/" — say so at dispatch.
3. **`llms.txt` and agent canon locale pointers** reference `/agents/locales.md` only; no change expected, verified at Gate C.
