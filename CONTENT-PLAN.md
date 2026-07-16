# Content Plan — faberlang.dev

Status: **content drafted, framework not yet built.**

The site is Wikipedia-shaped: random-access reference pages, each with one job and a
self-contained lead, linking out rather than teaching in sequence. This document records
the content inventory *and* the architecture the generator must respect, because the
first attempt failed on architecture, not content.

---

## Where the effort stands

An initial pass generated 18 HTML pages directly. It was killed and restarted as Markdown.
The reason, stated concretely so it is not repeated:

- All 18 HTML files defined their own `:root` custom-property block. No two were identical
  (verified by hashing the 8 feature pages — 8 distinct hashes). There was no shared
  stylesheet; every page was a fork of the design system.
- The most common class names site-wide were `m`, `t`, `kw`, `id`, `g`, `p`, `v`, `n`,
  `s`, `l`, `d`, `r` — single letters, redefined per file, meaning different things in
  different files. Presentational, not semantic; unrestylable without rereading.
- This document's own code-block convention (`faber-code`, `data-locale`, plain `<code>`,
  **no syntax spans**) was violated by the output it governed: 218 `kw` spans, 176 `id`
  spans, 145 `g` spans, and zero `<code>` elements inside `faber-code`.

**Diagnosis:** the failure was not insufficient CSS discipline, and — see *Design layer* —
it was not a missing design system either. The system existed the whole time, in
`07-speculum/SPEC.md`, and those `:root` blocks are hand-transcriptions of it. The failure
is that a design system living as **prose in a spec, with no mechanism to share it**, gets
re-implemented per page and drifts a little each time. The rule existed, was written down
in two places, and drifted anyway because nothing enforced it.

**Rule going forward:** conventions survive exactly where a machine checks them.
Everything decorative rots. The generator emits content plus a closed set of named blocks
and has no styling capability at all.

The Markdown rescue preserved the prose but silently dropped two machine contracts that
existed in the HTML — `data-locale` on code blocks, and explicit heading `id`s. Both are
load-bearing for the translation pipeline. See *Machine contracts* below.

---

## Core architecture: generated vs authored

This is the axis the whole site splits on. It determines the multilingual cost, the
staleness strategy, and what an LLM is allowed to touch.

| | Generated | Authored |
|---|---|---|
| **Source** | corpus frontmatter, compiler, EBNF | human/LLM prose |
| **Pages** | ~154 corpus terms, syntax reference, EBNF, targets matrix, `llms.txt` | getting-started, feature explanations, history |
| **Correctness** | correct by construction; a wrong page is a failing test | verified indirectly (see staleness oracle) |
| **Translation cost** | zero *once transcode exists* — see **Blocking dependency** below | LLM pass per locale, must be tracked |
| **Drift** | impossible; source of truth is the compiler's own test corpus | detected, not prevented |

The generated half is the large half. That is the point: it is also the half that becomes
multilingual for free — **conditional on a compiler feature that does not exist yet.**

### Blocking dependency: output reader formatting (in flight)

**Verified against `faber` 1.0.0 (repo build) on 2026-07-15.** The claim "the compiler is
the translator" is *not true today*.

`--reader-locale <LOCALE>` exists on `build`, `check`, `run`, `emit`, `format`, and
`explain`. But it is an **input declaration**, not an output transform — it tells the
compiler what locale the source is *already written in*. Feeding it Latin source:

```
$ faber format --canonical --reader-locale=th-TH --stdout src/main.fab
warning: READER001  (×6)
functio salve(textus nomen) → textus { ... }      ← still Latin
```

Byte-identical output for `th-TH`, `zh-Hans`, and `ar`. `faber explain READER001` confirms
it is a lint:

> `reader locale {pack} used Latin fallback keyword {keyword}; use {localized}`

This is why `examples/reader-locale/th-TH/src/main.fab` is authored directly in Thai
(`ฟังก์ชัน ทักทาย(ข้อความ name)`). Nothing in the CLI parses pack A and emits pack B.

**It is close.** To emit READER001 the compiler already computes the localized spelling —
it knows `functio` → `ฟังก์ชัน` and reaches for it. It uses the mapping to write a warning
rather than to rewrite the token.

**A separate factory goal is implementing output reader formatting.** This plan assumes it
lands. Until it does, treat "zero translation cost" as a projection, not a fact.

#### Requirement on that work: author mode, not canonical-only

`format --reader-locale` currently errors with `requires --canonical`. If that restriction
is lifted by making **canonical** the transcode path, the output is unusable for docs:

| | author mode | `--canonical` |
|---|---|---|
| `# WHY: documents the contract` | preserved | **stripped** (trivia-free) |
| `redde "Salve, §!"(nomen)` | preserved | **`redde scriptum("Salve, §!", nomen)`** |

Thai readers would get desugared, comment-free code while English readers get the sugar
surface — and `features/canonical-vs-sugar`, a page whose entire subject is that
distinction, would render in the wrong surface in six of seven locales.

**The docs pipeline needs: parse pack A → emit pack B, sugar and trivia preserved.**

#### Unresolved: comments inside `.fab` files

A keyword transcode cannot translate comments — they are not keywords. Step 2 maps
keywords; step 3 translates *website* prose. Neither reaches `# WHY: documents the
typecheck contract...` inside a corpus file, and those comments are some of the best
explanatory content in the repo. Options, in preference order:

1. **Generated corpus pages render `summary` from frontmatter and suppress in-code
   comments**, promoting load-bearing comment content up into frontmatter where it is
   already a translatable field. (Recommended, but `summary` is one line and comments
   carry more — e.g. `# EXPECTED OUTPUT: creata`.)
2. Accept English comments inside localized code — cheap, and defensible since comments
   are commentary, not program text.
3. LLM translation reaches *into* code blocks — but then "fluid" means more than keyword
   substitution and step 3 is editing code, which is a much scarier thing to automate.

Decide before 1,170 pages exist.

### The corpus is already a database

`examples/corpus/` is not a pile of examples needing a plan. Measured:

- 154 directories, 292 `.fab` files — **100% carry TOML frontmatter**
- 292 have `term`, `kind`, `category`; 291 `summary`; 282 `related`; 276 `syntax`; 92 `aliases`
- **183 distinct `term` values**, of which **167 have canonical examples** (202 files
  `canonical = true`, 75 `canonical = false`)
- paired `.expected` files — examples have verified execution output
- 7 reader packs exist: `ar`, `hi`, `la`, `th-TH`, `vi`, `zh-Hans`, `zh-Hant`

Which maps onto the Wikipedia shape directly: `summary` is the lead, `syntax` is the
infobox, `category` is the section, `related[]` is the wikilink graph, `.expected` is
proof the sample works.

**Corpus term pages are a build target, never authored.** Hand-writing 167 pages that
already exist as structured data is the largest unforced error available here.

### The corpus is not flat — the generator needs a real model

Three structural facts the generator must handle, none of them obvious from the directory
listing:

- **The page unit is the term, not the file.** 292 files across 183 distinct terms (~1.6
  examples per term). A term page carries *several* examples, which is a better page than
  one-sample-per-page anyway.
- **Canonical vs alias.** 167 terms have canonical examples; 41 distinct terms appear only
  as `canonical = false`. Plus 92 `aliases` entries and 5 `canonical_term` back-pointers.
  Aliases should redirect to their canonical term, not get their own page. Note 167 + 41 >
  183: some terms have *both* canonical and non-canonical files.
- **`kind` has 17 values** and they are not all page material: `keyword` (142),
  `operator-group` (31), `existing-home` (28), `type` (25), `concept` (21), `annotation`
  (11), `conversio` (9), `kernel` (6), `method` (5), `legacy` (5), down to `smoke` (1),
  `reject` (1), `pointer` (1). `legacy` and `smoke` are probably not pages;
  `existing-home` looks like a routing hint to content documented elsewhere. This needs a
  decision per `kind`, not a blanket rule.

---

## Decisions (settled)

1. **Markdown is the content source.** HTML generation is dead. The 18 HTML files are
   reference material for content only, not for markup.
2. **Stable English/Latin slugs. Translation lives in the content area only.**
   `/{locale}/syntax/types` in every locale; the Thai page displays a Thai title at a
   Latin path. This makes the language switcher pure path substitution, makes fallback a
   path substitution (matching the `fallback = ["la"]` semantics the reader packs already
   use), makes the `hreflang` alternate graph mechanically derivable, and keeps
   `related[]` locale-independent. The corpus already votes for this: the term *is*
   `functio` in all seven locales.
   → **Consequence:** the file path is authoritative and `title` is free prose. A
   generator must never slugify `title`.
3. **English/Latin ships first**, and defines URL structure, filesystem paths, and the
   generation scripts. Multilingual is deferred but designed for.
4. **The corpus is not merged into the site yet**, pending the generator.
5. **`llms.txt` is deferred**, but see the open decision on generating rather than
   authoring it.

6. **Fence syntax: standard triple backticks. Presence of a locale means pinned.**

   ````
   ```faber          → fluid — translate to the reader's locale
   ```faber th-TH    → pinned — this block IS Thai; leave it alone
   ````

   The rule is "if you named a locale, you meant it." Nobody writes ` ```faber th-TH ` by
   accident. Absence implies `la` and fluid. Standard CommonMark, so raw markdown still
   previews in GitHub and every editor; the existing 72 fences already say ` ```faber `,
   so migration is only adding locales to the pinned ones.

7. **Inline code spans need no annotation.** Plain backticks stay plain backticks. See
   *Machine contracts* §4 — the translatable vocabulary is a closed 48-identifier set and
   everything else is invariant by design, so the renderer resolves spans without help.

8. **Transcode happens at markdown-generation time, not static-build time**
   (`en-US/types.md` → `th-TH/types.md`, materialized into git). Neither is browser-time;
   there is no client-side translation, ever.

   **Rationale:** materialized Thai code is diffable. When a keyword changes, `git diff`
   shows the ripple across all six locales as a reviewable artifact. Transcoding at build
   time would hide the blast radius inside the build. Same philosophy as the staleness
   oracle — drift should be visible, not silently regenerated.

   **Consequence — `en-US` is the sole authority for fluid vs pinned.** Generated `th-TH`
   fences are **output, never input**. The generator reads the *English* fence (where the
   Decision 6 rule is unambiguous) and writes whatever comes out. A generated Thai fence
   that looks identical to a pinned one is harmless because nothing ever reads it back.

   **Consequence — the O7 sync is block-structured, not line-structured:** code blocks
   always regenerate from `en-US`; prose blocks preserve the local translation. Merging
   along block boundaries also lets step 3's LLM be denied write access to code entirely —
   it cannot corrupt a sample it is not allowed to touch.

   **Cost:** `th-TH/*.md` cannot be created until the transcode lands, so step 3 cannot
   start early. Accepted in exchange for the git-diff property.

9. **Fence outcome: positional, closed vocab, `reject`** — matching the corpus's existing
   `kind = "reject"` rather than inventing a parallel word.

   ````
   ```faber                  → fluid, must compile
   ```faber reject           → fluid, must fail to compile
   ```faber th-TH            → pinned Thai, must compile
   ```faber th-TH reject     → pinned Thai, must fail to compile
   ````

   Locale before outcome, enforced by CI so there is one canonical form. The two
   vocabularies are disjoint (pack ids vs `{compiles, reject}`) so parsing is unambiguous.
   Default `compiles`. Two values only — no output-matching, since inline fences have no
   expected output.

10. **Literal code is a fence; transcluded code is a component.** Ratifying O5 means most
    code on the site is a *pointer* to `corpus/{term}/{file}.fab`, not text in a fence.
    Transclusion is one of the O9 components.

    **A transclusion carries no modifiers.** The corpus frontmatter already has them —
    `kind = "reject"` gives the outcome, the file's pack gives the locale. Restating them
    in markdown would be a second source of truth that can drift from the first.

11. **Corpus examples are transcluded, not copied** (O5). Copies drift; transclusions
    inherit the corpus's execution-level verification for free.

12. **One renderer: `faber format` at build time** (O6). tree-sitter stays the editor
    surface its own README says it is. The wasm does not enter the website.

13. **`llms.txt` is generated from corpus frontmatter, not authored** (O8).

14. **The component vocabulary is a closed set, CI-enforced** (O9). The generator cannot
    write CSS.

15. **Translation provenance: schema now, implementation later** (O7). The frontmatter
    field exists from day one; nothing writes it until language #2 needs its first resync.
    One schema line today versus a manual 40-page diff later.

16. **Three page shapes, and a language portal at `/`** (resolves O10).

    ```
    /                       → language portal   (locale-less, generated)
    /{locale}/              → homepage          (encyclopedia lead + on-ramp banner)
    /{locale}/start/*       → tutorial track    (sequenced)
    /{locale}/{section}/*   → reference         (random-access)
    ```

    | shape | model | navigation |
    |---|---|---|
    | **portal** | locale router | lists every locale in its own script |
    | **reference** | Wikipedia — every page an entry point | `related[]`, a graph |
    | **tutorial** | sequenced; page 2 assumes page 1 | `next`/`prev`, a linked list |

    Reference and tutorial are opposite shapes. Wikipedia has no "next page" button and
    that is the design, not an oversight — it is why the model scales to 167 corpus terms
    without a curriculum. The tutorial track is the inverse and needs ordering. In Diátaxis
    terms the site has *reference* (syntax, corpus) and *explanation* (features), and
    currently **zero** of the two sequenced shapes.

    **Structural consequence: the portal lives above the locale segment.** `src/` currently
    holds nothing but `src/en-US/`. The portal is not translated *into* a language — it is
    rendered in all of them at once, the way wikipedia.org shows 日本語 / Deutsch / Русский
    each in its own script. It needs a home above `src/en-US/` and is **generated from the
    locale list**, not authored per-locale.

    **The portal is a demonstration, not just navigation.** A portal normally costs every
    visitor a click before content. Here that click *is* the pitch: pick your language
    first, because that is the entire point of the language. Recommended: show each
    locale's **code**, not just its name — `ฟังก์ชัน` beside ภาษาไทย, `函数` beside 中文,
    `functio` beside Latin. The thesis, legible in five seconds, before a word of prose.
    Cheap: each pack's `[llm] exemplars` already points at a `salve-munde` sample.

    **Today there is one locale**, and a portal offering one choice is a silly page. So:
    `/` redirects to `/en-US/` now, the route exists from day one, the portal goes live
    when locale #2 lands. What must be avoided is `/` meaning "the English homepage" and
    then having to move it.

    **The on-ramp banner is a component** (into the O9 set). Homepage → `start/install`.

17. **Don't hardcode page shape into the generator.** Same seam discipline as locale
    (Decision 3) and `render_example()` (Decision 8). Shape is a parameter from day one;
    otherwise adding the tutorial track is a refactor rather than four pages of content.

---

## Open decisions

**All notation decisions are settled (Decisions 6–15). Nothing below blocks slice 1.**

| # | Status |
|---|---|
| ~~O1~~ fence tag | **Settled** — triple backticks, tag `faber` (Decision 6). *Loose end:* `fab.tmLanguage.json` claims ` ```fab `, so the repo's own grammar will not highlight the repo's own docs. Cheapest fix is adding `faber` as an alias in the tmLanguage — one line upstream, not a blocker. |
| ~~O2~~ pinned vs fluid | **Settled** — Decision 6. |
| ~~O2b~~ fence outcome | **Settled** — Decision 9. |
| ~~O3~~ inline spans | **Settled** — Decision 7, no annotation needed. |
| ~~O4~~ heading anchors | **Settled** — explicit stable ids on all 107 `##` headings. See *Machine contracts* §5. |
| ~~O5~~ transclude vs copy | **Settled** — transclude (Decisions 10, 11). |
| ~~O6~~ one renderer | **Settled** — `faber format` at build time (Decision 12). |
| ~~O7~~ translation provenance | **Settled** — schema now, implementation later (Decision 15). |
| ~~O8~~ `llms.txt` | **Settled** — generated (Decision 13). *Open sub-question:* which locale does it serve? `la` canonical is the likely answer; seven locales would itself be the demonstration. Decide when building it. |
| ~~O9~~ component vocabulary | **Settled** — closed set, CI-enforced (Decision 14). The set is no longer hypothetical: Speculum §"Signature components" specifies it. See *Component vocabulary* below. |
| ~~O10~~ on-ramp | **Settled** — Decisions 16 & 17. Portal at `/`, homepage banner, tutorial track. |

**Nothing is open. The plan is decided.**

### O6 — the two-renderer collision

Two things claim to turn `.fab` into display:

- `faber format` — the compiler; will know all 7 packs once output reader formatting lands
  (see *Blocking dependency*); ground truth by construction
- tree-sitter / Shiki (`grammars/faber.wasm`, `fab.tmLanguage.json`) — browser-capable

But `tree-sitter-faber` has exactly one entry in `languages/` and one in `grammars/`:
`faber`. **The grammar is Latin-only** — its vocabulary is generated from the compiler's
`keywords.rs`, which is the canonical Latin set. Thai `ฟังก์ชัน` is not in it and will not
highlight. Ship the Thai site with Shiki and the code renders as undifferentiated text.

The site is statically generated, so it never needs a browser parser. Render at build
time through the compiler; keep tree-sitter as the editor surface its own README says it
is ("syntax highlighting only — not rendering"); keep the wasm out of the website.

If Shiki is wanted anyway, the fix that preserves the discipline is to extend the existing
generator to emit one keyword vocabulary per reader pack — seven grammars from one source
of truth, rather than two implementations drifting apart.

---

## Design layer — Direction 07, Speculum

**Source:** `~/design-ideas/directions/07-speculum/` — `SPEC.md`, `faber-porta.html`,
`faber-articulus.html`. One of seven explored directions; the explicit alternate to
`06-sectile` ("Pick Sectile if Faber is being sold. Pick Speculum if Faber is being
*used*"). Speculum's bet — the site is a reference work, not a statement — is the one
Decision 16 already took.

**Provenance and its consequence.** Speculum is a mockup produced without repo access.
The *design* is sound and is adopted. Its *factual claims are stale and understate the
project* — see **Status corrections** below. Treat SPEC.md as authoritative on surface,
never on status.

### The design system already existed — that revises the HTML diagnosis

The `:root` in the generated `features/reader-locale.html` and SPEC.md's token table are
the same values. The 18 HTML files were **hand-transcriptions of Speculum**, which is
exactly why they were similar-but-never-identical.

So the failure was narrower than *Where the effort stands* first recorded. It was not
"there is no design system" — the system is written down and it is good. It is that the
system lived as **prose in a spec with no mechanism to share it**, so each page
re-implemented it by hand and drifted a little each time. The single-letter classes were
compressions of Speculum's real policy-verb vocabulary (`s`/`l`/`d` = Support / Limited /
Defer) — a naming problem, not an architecture problem.

**Consequence for slice 1: the stylesheet does not need designing. It needs transcribing,
once, from SPEC.md's token table.**

### Tokens (authoritative — copy, do not re-derive)

| Token | Value | Use |
|---|---|---|
| `--paper` | `#faf9f6` | page ground |
| `--paper-alt` | `#f0efea` | infobox, code wells, table stripes |
| `--ink` | `#1a1a18` | body and headings |
| `--ink-dim` | `#5f5e58` | secondary, captions |
| `--ink-faint` | `#8c8a82` | metadata, table headers |
| `--rule` | `#dcdad2` | 1px hairlines |
| **`--glyph`** | **`#2f4faa`** | **glyphs only — nothing else, ever** |
| `--glyph-soft` | `#e8ecf8` | glyph highlight ground |
| `--fallback` | `#a8a49a` | Latin fallback tokens (dotted underline) |
| `--support` | `#2f6b4c` | policy verb: Support |
| `--limited` | `#9a7420` | policy verb: Limited / Warn / Erase |
| `--reject` | `#a33f30` | policy verb: Reject |
| `--defer` | `#6b6a64` | policy verb: Defer / Probe |

**The signature rule:** `--glyph` blue is reserved for `← → ∴ ≡ ∪ ⇥` and nothing else.
When the reader switches locale the words change script and the blue does not move. The
invariant is a *color*. Spending it on a button or a link destroys the one idea the page
exists to carry.

> **Vocabulary collision:** `--reject` (policy verb, target support) and Decision 9's
> fence `reject` (expected outcome) are unrelated. Do not let a component conflate them.

### Typography — derived from the content, not chosen

Body/headings `'Noto Serif'`; chrome/labels/tables `'Noto Sans'`; code `'Noto Sans Mono'`
then per-script fallbacks (`Noto Sans Thai` / `Arabic` / `Devanagari` / `SC`). A didone or
Trajan-clone renders Thai and Arabic as tofu and is structurally disqualified.

**Honest consequence — the monospace grid does not exist.** No monospace face covers Thai,
Arabic, Devanagari, and CJK, so a localized code block falls back per-script and cannot
hold a character grid. Leading is generous, alignment is by indent not column, nothing
depends on cell math. **Any ASCII-art diagram inside a localized code block is wrong by
construction.**

### Shape

Body 16.5/28 serif, measure ~72ch. Article is two-column (260px sidebar + main); portal is
centered. 1px hairlines, no border-radius above 2px, no shadows. Density is a feature.

### Status corrections — SPEC.md is stale here, and understates the project

SPEC.md says reader locale is "**proposed** ... The site must never imply the packs ship
today." That quotes a version of `reader-locale.md` that no longer exists. The current doc
(**updated 2026-07-15**) says:

> **Status:** substrate shipped; north-star layers remain explicitly partial — ReaderPack
> loading, localized source analysis, diagnostics, and **seven checked-in packs are live**

Marked **Shipped** upstream: pack schema/aliases/inheritance/fallback/validation/
diagnostics/LLM artifacts; pack-aware lexing and type resolution; manifest and CLI
selection; visible fallback and suggestions; pack-owned diagnostic rendering; `faber
explain`; bidi-isolated source display; canonical formatting.

Marked **Partial / not shipped**: localized Faber re-emission — corroborating this plan's
*Blocking dependency* section and the empirical 1.0.0 testing exactly.

**The honest line for the site: seven packs ship and are live; localized re-emission does
not.** Speculum draws that line in the wrong place and would make the site lie in the
modest direction. Its "non-negotiable honesty" rule is adopted in *spirit* — every
capability claim carries a policy verb and evidence — and rejected on *facts*.

**Binding upstream constraint**, from that same doc's own row for this project:

> Multilingual documentation generation for **Speculum/faberlang.dev** — **Proposed.** No
> live docs generator consumes ReaderPacks; current website assets are static and **must
> not be described as generated multilingual documentation**.

True until slice 1 exists. The site must not claim to be generated multilingual
documentation before it is.

### Amendment: the funnel

SPEC.md's Don't list says *"Don't add a marketing hero, a CTA pill, or a testimonial.
**There is no funnel here.**"* and *"There is no landing page. The docs are the site."*
Decision 16 is portal → homepage → banner → `start/install`. That is a funnel.

**Decision 16 wins; Speculum is amended.** The spirit of the rule is preserved: the banner
is encyclopedic in register — a plainly-worded route to installation, not a CTA pill. A
reference work may say where to obtain the thing it documents. No hero, no testimonial, no
marketing voice anywhere.

### The portal is not blocked on the transcode

Every pack ships a hand-authored exemplar — `salve-munde.{ar,hi,la,th-TH,vi,zh-Hans,
zh-Hant}.fab`, all seven verified present, each declared by its pack's `[llm] exemplars`.
So the Porta can show **real code in every language today**, from data the packs vouch for.

**Swap Speculum's living sample from `divide()` to `salve-munde`.** There is no `divide()`
exemplar; using it would mean waiting for the transcode or hand-writing seven variants —
which SPEC.md itself forbids ("Don't invent pack vocabulary to make the demo look
complete"). `salve-munde` works now and keeps that rule intact.

**Client-side locale switching in the living sample is compatible with Decision 8.**
Pre-transcoded variants toggled by JS is a carousel of precomputed renderings, not a
compiler in the browser. Distinct from translating pages at load, which is ruled out.

---

## Machine contracts

The things CI enforces. Everything here exists because the unenforced version of it
already failed once.

### 1. Code fences carry their locale, mode, and expected outcome

Every fence declares three things, not one:

| Dimension | Values | Why |
|---|---|---|
| **locale** | `la`, `th-TH`, `ar`, … | which reader pack the source is written in |
| **mode** | pinned \| fluid | whether translation should touch it (§2) |
| **outcome** | compiles \| rejects \| output-matches | what CI should assert (§3) |

CI extracts every fence, reads all three from the fence itself, and asserts accordingly
via the compiler.

**This is the staleness oracle, and it is the load-bearing idea of the whole site:** when
the language moves, the example breaks, CI flags the page — and since the code is wrong,
the prose beside it is probably wrong too. It catches both at once. It is the only
mechanism that verifies authored prose at all.

Restore what the Markdown migration dropped: the HTML had `data-locale` on 6 non-Latin
locales; the bare ` ```faber ` fences have nowhere to put it.

### 2. Pinned vs fluid (O2)

Two kinds of block exist and are currently indistinguishable:

- **Pinned** — `features/reader-locale.html` shows Thai and Arabic samples *to an English
  reader*, to demonstrate what they look like. Translating them destroys the point.
- **Fluid** — `syntax/types.md`'s example should render in the reader's own locale.

Same markup today. This distinction must land before there are 1,000 generated pages.
It is a one-word annotation now.

### 3. Expected outcome — the corpus contains intentionally-invalid examples

A naive contract ("every extracted fence must compile") breaks on the corpus's own
content. `kind = "reject"` exists, and its file says so explicitly:

> `# This exemplum intentionally fails to compile; it is registered in the`
> `# per-backend EXPECTED_FAILURES lists.`

Its frontmatter is written for documentation — *"Tensor arithmetic rejects non-numeric
elements and mixed numeric widths."* That is exactly the content a good reference page
wants: here is what does not work, and why. So reject cases are not junk to filter out;
they are page material whose CI assertion is inverted.

This cuts both ways, and the inverted case is the valuable one: a `rejects` fence that
*starts compiling* is drift too — it means a typecheck contract silently loosened. That is
a class of regression nothing else on the site would catch.

The vocabulary already exists upstream (`kind = "reject"`, per-backend
`EXPECTED_FAILURES`, `.expected` files for output matching). The fence contract should
borrow it rather than invent a parallel one.

### 4. Inline code spans — resolved by lookup, zero annotation

**465 inline spans vs 72 fences** (347 distinct) in `src/en-US/**/*.md`. Latin keywords
fused into English sentences:

> Every declaration places the type before the name: `textus nomen`, not `nomen: textus`.

A fence-shaped pipeline would cover 13% of the code on the site. But these need **no
markup and no annotation pass**, because the translatable vocabulary is closed and
everything outside it is invariant *by design*. The pack says so itself:

> `[llm] system_prompt_snippet = "... Keep Faber glyph syntax unchanged."`  — th-TH pack
> `"... canonical type spellings, and invariant glyph syntax."`  — la pack

**The mappable set is 48 identifiers: `[keywords]` (37) + `[types]` (11).** Nothing else in
Faber translates. So: lex the span, map any token found in those two tables, leave the rest.

| span | th-TH | why |
|---|---|---|
| `` `cape` `` | `จับ` | in `[keywords]` |
| `` `textus` `` | `ข้อความ` | in `[types]` |
| `` `T ∪ nihil` `` | `T ∪ ว่าง` | three tokens; only `nihil` maps |
| `` `←` `` `` `§` `` `` `↦` `` | unchanged | glyph — invariant by design |
| `` `tensor<T, Figura>` `` | unchanged | `tensor` is not in the pack |
| `` `faber check` `` | unchanged | no tokens map |

Only **24 of 347** distinct spans map exactly. That is the correct answer, not a
shortfall — the other 323 are glyphs, compounds, CLI commands, and paths that must survive
untouched.

**Collision risk checked and clear:** no CLI verb (`check`, `build`, `run`, `emit`,
`format`, `test`, `init`, `repl`, `explain`, `targets`, `lex`, `parse`) is a Latin keyword.
The verbs are English, the keywords are Latin; they cannot clash.

Implementation is the same seam as fences, applied to a fragment: `render_inline(span,
to_locale)` beside `render_example()`.

**Open — the inverse case:** English prose that mentions `` `ฟังก์ชัน` `` *as a Thai
example* needs pinning. Rare enough to deserve an ugly syntax. Confirm it actually occurs
on the reader-locale page before designing for it.

### 5. Heading anchors (O4)

The HTML got this right and the Markdown lost it. The HTML had **61 headings with explicit
`id=`** — `why`, `commandments`, `snapshot`, `sample`, `lanes`, `quickstart`, `cli`,
`stdlib` — short, stable, Latin, hand-chosen, with ~23 `href="#..."` links depending on
them. The Markdown has **107 `##` headings and zero explicit anchors.**

Auto-slugified from heading text, the actual headings produce:

- `## Lista — ordered dynamic collection` → `#lista--ordered-dynamic-collection`
- `## Runtime conversion — ↦` → `#runtime-conversion--` (the glyph vanishes)
- `## Nullish coalescing — vel` → `#nullish-coalescing--vel`

Bad in English; in Thai they become percent-encoded and, fatally, they *change*. So
`/th-TH/syntax/conversion#runtime-conversion` does not exist, and the language switcher —
just made trivial by the slug decision — either drops the fragment or lands on a dead
anchor. **The slug decision gets given back one level down.**

Same decision, one layer deeper: explicit stable ids derived from an identifier, never
from translatable prose. 107 annotations now; unfixable in bulk after seven locales.

While in there: em-dashes and glyphs (`↦`) inside headings are hostile to slugs regardless
of locale. The subtitle after the dash probably wants to be a lead sentence.

### 6. Provenance

Already present and worth keeping — every page's frontmatter declares its upstream sources:

```toml
sources = [
  "radix/README.md (Core Type Surfaces, Numeric Widths, Tensors And Sparsa)",
  "radix/docs/design/numeric-type-sugar.md",
  "examples/corpus/typi/",
]
```

When an upstream doc changes, the pages derived from it can be flagged stale. For a site
documenting a moving language this is the highest-value metadata in the repo. The
translation pipeline needs the same trick one layer down (O7).

### 7. No styling in the generator (O9)

Closed vocabulary of named blocks. CI fails on an unknown block name. The generator
cannot write CSS. This is the constraint that makes MediaWiki hold together — authors get
`{{Infobox}}`, `{{Hatnote}}`, `{{Main}}`, and *cannot* reach the stylesheet. That
constraint is the feature.

#### Component vocabulary

Speculum §"Signature components" already specifies most of the set. Union with what the
content model requires (Decision 10):

| Component | Source | Notes |
|---|---|---|
| **porta** | Speculum 1 | the gate; locale ring; honest pack status. Decision 16 |
| **rendering-bar** | Speculum 2 | persistent strip naming the current rendering. Not a footer dropdown |
| **living-sample** | Speculum 3 | one function across locales. Use `salve-munde`, not `divide()` |
| **fallback-token** | Speculum 4 | dimmed, dotted-underlined, **counted** — requirement #10 built as UI |
| **bdi-code** | Speculum 5 | `<bdi>`-wrapped Arabic in LTR code — requirement #7 implemented |
| **policy-table** | Speculum 6 | Support/Erase/Warn/Reject/Defer/Probe/Proof + measured floors |
| **infobox** | Speculum 7 | version, typing, compiler, lanes, targets, license |
| **lane-diagram** | Speculum 8 | HIR/MIR fork. **Not** inside a localized code block — no grid exists |
| **transclusion** | Decision 10 | pointer to `corpus/{term}/{file}.fab`; carries no modifiers |
| **onramp-banner** | Decision 16 | homepage → `start/install`. Encyclopedic register (see *Amendment*) |
| **next-prev** | Decision 16 | tutorial-track sequencing |
| **source-list** | frontmatter `sources` | provenance footer |

**One table component for all three axes.** Speculum is emphatic and it is right: the
down-axis (machine targets) and up-axis (human locales) use the *same* `policy-table`,
because the architecture says they are the same kind of thing — `rendering A → HIR →
rendering B`, no target privileged. Splitting them into two differently-styled components
loses the thesis. This is a CI-checkable constraint, not a preference.

---

## Multilingual pipeline

Adding a target language is three steps:

1. **Regenerate** the target-language site structure as static pages, English content,
   Latin paths.
2. **Convert** every example through the compiler → reader pack for the target language.
   All examples become valid Faber in the target locale, automatically.
3. **Translate** the prose: an LLM iteratively reads the English and produces
   locale-appropriate prose. This is the MVP for that language. Per Decision 8, the LLM
   should be denied write access to code blocks — they are regenerated from `en-US`, not
   translated.

### Step 3's prompt is already written — `[llm]` in each pack

Every reader pack carries an `[llm]` section:

```toml
[llm]
system_prompt_snippet = "Emit Thai reader-locale Faber using Thai keywords for declarations, control flow, loops, returns, booleans, common primitive types, and lista/tabula collections. Keep Faber glyph syntax unchanged."
exemplars = ["./exemplars/salve-munde.th-TH.fab"]
```

The target pack's snippet plus its exemplars are exactly the instruction step 3 needs, and
they are maintained next to the pack they describe rather than in a website config. Use
them; do not write a parallel prompt. This is also a real input to O8 (`llms.txt`) — the
packs already know how to tell a model to emit their locale.

### Correction: step 1 is a fork, and forks need merges (O7)

Step 1 is correct exactly once. Run it a second time — after an LLM has translated 40 Thai
pages — and it either clobbers the translations or skips the pages and loses the English
updates. The plan above describes a bootstrap; what actually gets operated is a recurring
sync.

The fix is the `sources` trick applied one layer down: record the **content hash of the
English source at translation time**. The second run then classifies every page as:

- untranslated
- translated and current
- translated but the English moved ← the only bucket the LLM revisits

Without this, language #2's first update is a manual diff across 40 pages, which is where
multilingual sites get quietly abandoned.

### Fallback

Do not invent a model — one already exists. `th-TH/pack.toml` opens with:

```toml
inherits = "la"
fallback = ["la"]
```

The site copies these semantics exactly: `src/th-TH/` inherits from `src/en-US/`,
untranslated pages fall back with a banner, and translation coverage becomes a measurable
number rather than an all-or-nothing gate.

### Verification asymmetry

Fence CI proves an example lexes and parses. The corpus proves its examples *produce
correct output* (`.expected`). That gap matters for exactly the drift this is meant to
catch: if a function's signature changes but the example still parses, the fence passes CI
and the page is wrong anyway. Hence O5 — transclude corpus examples rather than copy them,
and know which class each block is: transcluded-and-executed, or inline-and-only-parsed.

---

## Page inventory

Status legend: ✅ md drafted · ⬜ not written · 🔁 to be generated · ⚠️ HTML exists but is
debt (content reference only)

### Portal (**missing entirely**) — locale-less, above `src/{locale}/`

| Page | Path | Sources | Status |
|------|------|---------|--------|
| Language portal | `/` | locale list, each pack's `[llm] exemplars` | 🔁 |

Per Decision 16. Redirects to `/en-US/` until locale #2 exists.

### Authored — Getting started / tutorial track (**missing entirely**)

| Page | Path | Sources | Status |
|------|------|---------|--------|
| Install the compiler | `start/install.md` | `faber/`, `radix/`, release artifacts | ⬜ |
| First program | `start/hello.md` | `examples/corpus/`, README Quick Start | ⬜ |
| Basic commands | `start/commands.md` | README (CLI Roles), `faber --help` | ⬜ |
| Project layout & manifest | `start/projects.md` | README (Package Manifest), `cista/` | ⬜ |

Sequenced (Decision 16) — `next`/`prev`, not `related[]`.

This is the genuine outlier in the whole plan. It is the only section that is truly
hand-authored, sequential (not random-access), aimed at a reader with zero context, and
the fastest to go stale — it names versions, install commands, and paths. It cannot
inherit the corpus's correctness guarantee, but it can earn its own: **CI runs the
quickstart end-to-end in a clean container and fails when the instructions lie.** Same
trick as fence extraction, applied to prose.

#### This is the only conversion path the site has

Decision 16 makes the funnel `portal → homepage → banner → start/install`. Everything
that turns a stranger into a user runs through one page, which promotes the container
check from hygiene to a guard on the funnel.

**And that path is currently broken.** `start/install.md` will document Homebrew.
Homebrew ships **faber 0.38.0**, which cannot parse `[reader]` in `faber.toml` at all —
it rejects this repo's own reader-locale examples with a TOML parse error (see *Live
bugs*). So the funnel would read: portal demonstrates that Faber speaks your language →
banner sends you to install → install hands you a compiler that cannot do the thing you
came for.

**The brew formula needs a 1.0.0 release before this page can be written honestly.**
Blocks the funnel, not slice 1.

### Authored — History

| Page | Path | Sources | Status |
|------|------|---------|--------|
| History hub | `history/index` | TBD — no single history doc exists | ⚠️ HTML (origins note) |
| Influences | `history/influences` | `README.md` (contrasts with AppleScript, COBOL, Rust, Go, TS, JAX), `docs/design/reader-locale.md` | ⬜ |
| Release history | `history/releases` | `radix/docs/release/` | ⬜ |

**Known gap:** no coherent history document exists. Creator attribution, timeline, and
release history need compiling from release notes and git history.

### Authored — Features (explanation)

| Page | Path | Sources | Status |
|------|------|---------|--------|
| Features hub | `features/index` | overview, links | ⚠️ HTML |
| Reader locale | `features/reader-locale` | `docs/design/reader-locale.md` (69 KB), `examples/reader-locale/`, `stdlib/reader/*/pack.toml` | ⚠️ HTML |
| Compilation lanes | `features/compilation-lanes` | `README.md`, `docs/design/lowering-routes.md`, `air-dialect.md`, `semantic-ownership.md` | ⚠️ HTML |
| Latin vocabulary and glyphs | `features/latin-and-glyphs` | `README.md`, `EBNF.md`, `examples/corpus/` | ⚠️ HTML |
| Commandments | `features/commandments` | `README.md` (Commandments) | ⚠️ HTML |
| Canonical vs sugar surfaces | `features/canonical-vs-sugar` | `docs/design/numeric-type-sugar.md`, `annotation-sugar.md`, `faber-canonical-surface.md` | ⚠️ HTML |
| Capability calls and frames | `features/frames` | `docs/design/frame-stream-types.md`, `host-provider-gateway.md`, `examples/corpus/ad/` | ⚠️ HTML |
| Inline testing | `features/testing` | `README.md` (Exempla), `examples/coreutils/packages/echo/` | ⚠️ HTML |

These 8 need porting to Markdown. The HTML is content reference only — do not carry the
markup across. `reader-locale` is the pinned-block case (O2).

### Reference — Syntax (authored now, candidate for generation)

| Page | Path | Status |
|------|------|--------|
| Syntax hub | `syntax/index` | ⬜ |
| Data types | `syntax/types.md` | ✅ |
| Variables and binding | `syntax/variables.md` | ✅ |
| Functions | `syntax/functions.md` | ✅ |
| Control flow | `syntax/control-flow.md` | ✅ |
| Error handling | `syntax/errors.md` | ✅ |
| Generics | `syntax/generics.md` | ✅ |
| Collections | `syntax/collections.md` | ✅ |
| String and template literals | `syntax/strings.md` | ✅ |
| Conversion operators | `syntax/conversion.md` | ✅ |
| Glyphs and operators | `syntax/glyphs.md` | ✅ |
| Nullability and optionality | `syntax/nullability.md` | ✅ |

Per-page `sources` are in each file's frontmatter (authoritative — this table is the
planning view only). All 11 are the main consumers of the 465 inline spans (O3) and 107
headings (O4). Their examples are the primary transclusion candidates (O5).

### Generated — Corpus (**not yet started; do not author**)

| Page | Path | Sources | Status |
|------|------|---------|--------|
| Corpus hub | `corpus/index` | `examples/corpus/` | 🔁 |
| Term pages (×167 canonical) | `corpus/{term}` | `examples/corpus/**/*.fab` + `.expected` | 🔁 |
| Alias redirects (×41 + 92 `aliases`) | `corpus/{alias}` → canonical | frontmatter `aliases`, `canonical_term` | 🔁 |
| Category indexes | `corpus/category/{category}` | frontmatter `category` | 🔁 |

Generated from frontmatter: `summary` → lead, `syntax` → infobox, `category` → section,
`related[]` → cross-links, `.fab` → samples rendered per locale, `.expected` → verified
output, `kind` → how each example renders and what CI asserts. ~167 canonical terms × 7
locales ≈ 1,170 pages at zero marginal authoring cost.

Open sub-decisions for the generator: which `kind` values become pages (see *The corpus is
not flat*), and how a term page presents multiple examples including reject cases.

### Tooling

| Page | Path | Sources | Status |
|------|------|---------|--------|
| Tooling hub | `tooling/index` | overview | ⬜ |
| Faber Build Tool | `tooling/faber-build-tool` | `README.md` (CLI Roles, Quick Start, Package Manifest), `faber/` | ⚠️ HTML stub |
| Radix Compiler | `tooling/radix-compiler` | `README.md` (Compilation Pipeline, Performance, Codebase Index), `radix/` | ⚠️ HTML stub |
| Cista Package Manager | `tooling/cista-package-manager` | `cista/`, `README.md` | ⚠️ HTML stub |
| Codegen targets | `tooling/codegen-targets.md` | `docs/design/target-capability-matrix.md`, `faber targets` | ✅ (generation candidate) |
| Compiler performance | `tooling/performance.md` | `README.md` (Compiler Performance) | ✅ |
| In-process scripting | `tooling/scripting.md` | `docs/design/faber-scripting.md` | ✅ |
| Editor support | `tooling/editors.md` | `tree-sitter-faber/` | ⬜ (see O6) |

### Ecosystem

| Page | Path | Sources | Status |
|------|------|---------|--------|
| Ecosystem hub | `ecosystem/index` | overview | ⬜ |
| Norma standard library | `ecosystem/norma.md` | `README.md`, `norma/`, `radix/docs/stdlib/morphologia.md` | ✅ |
| Triga graphics | `ecosystem/triga.md` | `triga/` | ✅ |
| Coreutils | `ecosystem/coreutils.md` | `examples/coreutils/` (38 packages) | ✅ |
| AI Workbench | `ecosystem/ai-workbench.md` | `examples/ai-workbench/` | ✅ |
| Reader-locale packages | `ecosystem/reader-locale-packages.md` | `examples/reader-locale/` (6 locale packages) | ✅ |
| Language corpus | `ecosystem/corpus.md` | `examples/corpus/` | ✅ (should link to generated `corpus/`) |

### References

| Page | Path | Sources | Status |
|------|------|---------|--------|
| References hub | `references/index` | links | ⬜ |
| EBNF grammar | `references/ebnf.md` | `radix/EBNF.md` | ✅ (generation candidate) |
| Design documents | `references/design-docs.md` | `radix/docs/design/` (28 docs) | ✅ (generation candidate) |
| GitHub repositories | `references/repositories.md` | `github.com/faberlang` | ✅ |

### Generated — LLM surface (deferred, see O8)

| Artifact | Path | Sources | Status |
|------|------|---------|--------|
| `llms.txt` | `/llms.txt` | corpus frontmatter | 🔁 |

Faber is an LLM-focused language; the site should be friendly to LLM readers. The corpus
frontmatter — 183 terms with a canonical form, one-line summary, syntax signature, alias
list, and relation graph — is already a language reference in the shape an LLM wants, and
strictly better than the prose pages. Hand-writing this would be worse than emitting it.

---

## Missing sections (O10)

The current cut — history / features / syntax / tooling / ecosystem — is by **subject
matter**, which is the encyclopedia cut and correct for reference. But every path leads to
reference material and there is no on-ramp. Wikipedia gets away with that because nobody
learns a language from Wikipedia. If faberlang.dev is also where someone decides whether
to *try* Faber, that is a different document with a different shape, and it is now
sketched above under *Getting started* — but the decision of whether the site is
reference-only or reference-plus-on-ramp is still open.

---

## Next steps

**Strategy: build the framework in English now; wire up transcode when it lands.**

### English-first does not mean Latin-only

The English site is already multilingual in its code blocks — `features/reader-locale`
shows Thai, Arabic, Hindi, Chinese, and Vietnamese samples *to an English reader*. That is
the page's entire point. The old HTML carried `data-locale` across 6 non-Latin values
because the **English** site needed it.

So of the whole "multilingual" bucket, exactly one item is deferrable:

| | needed for the English site | why |
|---|---|---|
| fence **locale** | **day one** | reader-locale's 6 non-Latin blocks must parse under their own packs |
| fence **mode** (pinned/fluid) | **day one** | those blocks are pinned, the rest are fluid, and nothing distinguishes them today |
| fence **outcome** | **day one** | the homepage's code does not lex — live, in English, right now (see below) |
| **transcode** | deferred | ← the only one |

The contracts are not scaffolding built on spec. They are load-bearing for the English
site and pay off immediately.

### Seams — cheap now, a refactor later

- **`render_example(source, from_locale, to_locale)`** — every generated page calls it.
  Today it asserts `from == to` and returns the source unchanged. When the factory goal
  lands it is one function body, because every call site already passes the right
  arguments. This is the wiring point.
- **Locale stays a parameter everywhere.** `src/{locale}/` is already right — do not let
  `en-US` reach template lookups or path joins.
- **Translation-provenance field in the frontmatter schema** (O7) even though nothing
  writes it yet.

### Order

**Notation is settled. Slice 1 is unblocked and is the next action.**

1. **Slice 1 — `syntax/types.md` end to end.** Component vocabulary (Decision 14), one
   stylesheet, minimal generator, fence extractor in CI, one rendered page. The framework,
   proven at n=1. *Rationale: the HTML attempt failed because 18 pages were built before
   anyone checked the framework. 700 lines of plan and zero pixels is the same mistake
   inverted.*
2. **Annotate the other 23** against a contract a real generator has already consumed.
   **The pass is far smaller than first estimated:** 465 inline spans → **0**; 72 fences →
   locale only where pinned; 107 headings → still needed (Decision/O4).
3. **Slice 2 — one corpus term page.** A different code path, and where the real risk lives
   (`kind` handling, multiple examples per term, reject cases, `related[]`, transclusion).
   ~90% of the eventual site goes through it.
4. Then the rest of the corpus, then getting-started (and O10 with it).

---

## Live bugs found while planning

Concrete, fixable now, and each one is an argument for the contract that would have caught
it.

1. **The homepage's code block does not lex.** `src/en-US/index.html` uses `// Type-first:`
   and three more `//` comments. Faber uses `#`; `//` is `LEX006.c_style_line_comment`. The
   first code a visitor sees is invalid Faber. → the fence extractor catches this on day one.
2. **The documented install path ships a stale compiler.** `/opt/homebrew/bin/faber` is
   **0.38.0** (symlinked 2026-06-29); the repo builds **1.0.0**. 0.38.0 cannot parse
   `[reader]` in `faber.toml` at all — it rejects this repo's own reader-locale examples
   with a TOML parse error. → exactly the class of lie the getting-started container check
   is for. Note for anyone testing compiler behaviour: **use the repo build, not `which
   faber`.**
