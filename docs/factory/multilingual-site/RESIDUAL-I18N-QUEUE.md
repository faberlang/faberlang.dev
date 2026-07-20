# Residual i18n Queue — fence comments, corpus summaries, chrome attributes

**Status**: queued — handoff to the translation lane
**Date**: 2026-07-20
**Origin**: faberlang.dev design/usability session (renderbar search +
localized-page review). Related: `radix/docs/factory/reader-locale-coverage-gaps/audit.md`
(pack keyword coverage, being filled via the `EBNF.{locale}.md` glossary →
pack pipeline, e.g. `radix/EBNF.hi.md`).

Three bounded content gaps remain now that the page matrix is complete. All
figures measured against `src/` at the date above.

## Item 1 — English comments in code fences on localized pages

**Scope** (identical in every locale — full-file copies of one English
authority): per locale, **23 fences / 41 comment lines** across **12 files**:

| fence type | fences | comment lines | rule |
|---|---|---|---|
| `faber` | 13 | 23 | translate — comments are prose |
| `text` | 7 | 11 | translate — comments are prose |
| `bash` | 2 | 6 | commands stay English; comments may be translated |
| `toml` | 1 | 1 | translate the comment |

Files (same paths under each `src/{locale}/`):
`features/canonical-vs-sugar.md`, `features/commandments.md`,
`features/frames.md`, `features/reader-locale.md`, `features/testing.md`,
`start/examples.md`, `start/install.md`, `syntax/collections.md`,
`syntax/control-flow.md`, `syntax/conversion.md`, `syntax/functions.md`,
`syntax/variables.md`.

**Translation rules**

- Translate `#` comment lines only. Never string literals (`nota "matched"`
  is code), never commands, never frontmatter, never fence-info flags.
- Skip fences marked `pinned` or `locale=` — deliberately canonical.
- Comments are lexer trivia, so localized comments cannot break compilation;
  still, run `generator/scripts/validate-fences.sh src/{locale}` per locale
  afterward as the gate.
- `prose_hash` drift tracking already watches these files — an English
  comment edit upstream will re-flag the file like any prose change.

**Durable fix**: add "translate `#` comment lines per the rules above" to the
production translation prompts (`PRODUCTION-TRANSLATE.md` job queue) so new
pages arrive with comments localized.

## Item 2 — Corpus term summaries (171 × 6 locales)

The renderbar keyword search (`search-index.{locale}.json`) shows each
term's one-sentence `summary` from `examples/corpus/**` frontmatter. These
exist only in English; locale corpus pages are likewise English-bodied with
the honesty notice. The dropdown currently falls back to English summaries.

**Ask**: translate the 171 canonical-term summaries per locale (single
sentences; keep keyword spellings consistent with the pack glossary from the
`EBNF.{locale}.md` pass).

**Integration contract** (site side, ready to consume): deliver per-locale
overlays as `generator/locales/{locale}/summaries.toml` with
`[summaries] term = "localized sentence"`. `generate-search-index.py` will
merge them into `search-index.{locale}.json` (`"s"` field) at build time;
missing terms fall back to English. (Site-side merge lands when the first
overlay arrives — ping the site lane.)

## Item 3 — Chrome strings in attributes and JS

`inject-chrome.py` rewrites **text nodes only**. Strings that live in
attributes or JS are English on every locale today:

- search box: `placeholder="keyword…"`, `aria-label="Search keywords"`
- demo-tabs card: `Copy` / `Copied` button states
- renderbar wayfinding titles: `porta · all languages`, `porta · change language`
  (deliberately Latin/English per the portal's multi-script stance — decide
  whether these stay or localize)

**Recommended shape** (when a second JS surface justifies it): extend
`chrome.toml` with `[search]` / `[demo_tabs]` sections as the single catalog,
and have the build emit a per-locale `ui.json` for runtime JS consumption.
One authority (chrome.toml), two consumers (inject-chrome static, ui.json
runtime). Not worth building for a single consumer; queue behind Item 2.

## Verification (post-delivery)

```bash
# Item 1: no English comment lines remain in non-pinned faber fences
python3 <audit snippet from session log>   # or eyeball the 12 files
bash generator/scripts/validate-fences.sh src/zh-Hans

# Item 2: zh-Hans dropdown summaries localized
rg -c '"s":"[^"]*[\x{4e00}-\x{9fff}]' dist/search-index.zh-Hans.json

# All: full build green
bash generator/scripts/build-site.sh
```
