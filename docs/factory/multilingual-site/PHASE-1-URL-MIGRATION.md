# Delivery: Phase 1 — URL migration to portal-at-root foundation

## Interpreted unit

Move all locale content under `/{locale}/...` (English included), introduce
`locales.toml`, thread `site_locale` + `reader_locale` through the build, emit
meta-refresh redirect stubs for retired English-at-root URLs, and leave `/` as a
temporary redirect to `/en-US/` until Phase 2 builds the real portal.

**Unit goal:** After Phase 1, every content page lives under a locale segment;
`<html lang>` is the prose language (`en-US`, not `la`); code still transcodes
via reader-locale (`la` for English); old inbound root paths redirect; full
build gates green.

## Normalized spec

### Functional requirements

1. **URL scheme:** content at `/{site_locale}/...` for all locales including
   `en-US`. English no longer renders at dist root (except redirect stubs +
   global surfaces).
2. **Redirect stubs:** for every previously published English content path under
   `dist/` root (authored pages + corpus paths that were English-at-root), write
   a meta-refresh HTML stub → `/en-US/<same path>`. Mechanism matches existing
   corpus alias pages.
3. **Interim `/`:** redirect to `/en-US/` (Phase 2 replaces with portal).
4. **Dual locale:**
   - `site_locale` = `src/{dir}` name → URL segment + `<html lang>`
   - `reader_locale` = pack id → `faber emit --reader-locale` and corpus
     localization; default = dir name; override `en-US` → `la`
5. **`locales.toml`:** registry at generator root (or repo root under
   `generator/`) mapping each known locale to `reader_locale`, native display
   name, native script label, status. Discovery remains dir-presence; registry
   enriches. Replace hardcoded `LOCALE_NAMES` in `render-corpus-batch.sh`.
6. **Chrome hrefs:** sidebar/renderbar content links prefix with
   `/{site_locale}/`. Locale-less agent surfaces (`/llms.txt`, `/agents/`,
   `/.well-known/`, `/speculum.css`) stay absolute unprefixed.
7. **Markdown content links:** absolute content paths in `src/{locale}/**/*.md`
   rewritten to include that locale segment (or rewritten at render time with
   the same outcome). Agent/static paths unchanged.
8. **Build fan-out:** `build-site.sh` renders every `src/*` locale into
   `dist/{site_locale}/` with correct reader-locale for fences/corpus.
9. **Post-process scripts:** sitemap, canonical, link check, leakage gate
   understand `en-US` as a locale dir (English content under `dist/en-US/`);
   redirect stubs at root remain link-checkable.
10. **Smoke checks:** assert `/en-US/` paths, not root English pages.

### Constraints

- Decision 17: no render-time prose merge
- Decision 8: code still via `faber emit`; not LLM
- Decision 14: no CSS from generator
- Decision 2: Latin slugs only; `title` never slugified
- Shared workspace: no destructive git; leave foreign dirt alone
- No production deploy/push without operator auth

### Non-goals (this phase)

- Real language portal UI (Phase 2)
- Provenance hashes / sync-report (Phase 3)
- Chrome string catalog localization (Phase 4)
- LLM translate tooling (Phase 5)
- Thai prose translation (Phase 6)

## Repo-aware baseline

| Surface | Current | Target |
|---|---|---|
| `build-site.sh` | en-US → `dist/` with `locale=la`; others → `dist/{name}` | all → `dist/{site}/`; reader from registry |
| `types.fab` `Pagina.locale` | single field used for lang + display | split `site_locale` + `reader_locale` (or keep `locale` as site + add reader) |
| `html.fab` | hardcoded `/start/...`, `lang=pag.locale` | prefix content hrefs; `lang=site_locale` |
| `main.fab` CLI | one locale arg | accept site (+ optional reader) or derive reader from registry at shell |
| `localize-markdown.py` | `--locale` = pack | keep pack = reader_locale |
| `render-corpus-batch.sh` | `LOCALE_NAMES` dict; `locale != la` notice | registry names; pass reader + site as needed |
| Python gates | `LOCALE_DIRS` excludes non-en; English = root | English under `en-US`; root = stubs + static + interim redirect |
| `src/**` links | absolute `/start/...` | `/{locale}/start/...` for content |

### Stack / validation

```bash
bash generator/scripts/build-site.sh
python3 generator/scripts/check-internal-links.py dist
python3 generator/scripts/check-leakage-gate.py dist
```

Requires `faber` on PATH (repo build preferred).

## Stage graph

```text
S1 locales.toml + registry reader helper (Python)
       ↓
S2 types/main/html dual-locale + chrome path prefix
       ↓
S3 build-site.sh fan-out + smoke + redirect stub generation
       ↓
S4 Python post-process/gates (sitemap, canonical, links, leakage)
       ↓
S5 rewrite src/** content absolute links to /{locale}/...
       ↓
S6 full build + gates + interim / redirect
```

S1 and early inventory can parallel; S2–S4 are sequential on shared contracts;
S5 can parallel S2–S3 if link rewrite is pure markdown (no generator deps).

## Implementation work

| ID | Work | Files (primary) | Notes |
|---|---|---|---|
| W1 | Create `generator/locales.toml` for 7 locales | `generator/locales.toml` | en-US→la; others identity; native names/scripts |
| W2 | Split Pagina locale; CLI; html lang + href prefix helper | `types.fab`, `main.fab`, `html.fab`, callers in `corpus.fab` | site for lang/href; reader unused in HTML except optional renderbar |
| W3 | Rewrite `build-site.sh` | `build-site.sh` | all locales under dist/{site}; redirects; smoke |
| W4 | Update gates/sitemap/canonical/leakage/corpus-batch | listed scripts | shared LOCALE set from registry preferred |
| W5 | Bulk rewrite markdown content links | `src/**/*.md` | preserve agent paths |
| W6 | Regenerate `dist/`; fix residual gate failures | `dist/` | committed site artifact |

### Path prefix rules

Prefix with `/{site_locale}` when href starts with `/` and first segment is a
content section: `start`, `syntax`, `features`, `tooling`, `ecosystem`,
`history`, `references`, `corpus`, or is empty home (`/`).

Do **not** prefix: `/llms.txt`, `/llms-full.txt`, `/agents/`, `/.well-known/`,
`/speculum.css`, `/robots.txt`, `/sitemap.xml`, external URLs, fragments.

Brand link: homepage of current locale → `/{site_locale}/` (not bare `/` once
portal owns `/`; during Phase 1 brand → `/{site_locale}/`).

## Checkpoints and gates

**Checkpoint:** Phase 1 complete when acceptance below is green and committed.

**Batching / split decision:** One factory phase. Homogeneous migration; split
only if emit/compiler gap blocks dual-locale (not expected).

**Release decision:** **Defer push/deploy.** Record migration in commit message.
Operator must authorize production deploy (GOAL release posture).

### Acceptance

- [x] Content HTML under `dist/en-US/...` and `dist/{other}/...`
- [x] `dist/index.html` redirects to `/en-US/` (interim)
- [x] Retired paths e.g. `dist/start/install.html` redirect to `/en-US/start/install.html`
- [x] English pages: `<html lang="en-US">` (not `la`)
- [x] English code still Latin (`reader_locale=la`)
- [x] `locales.toml` consumed by build and corpus batch (no `LOCALE_NAMES` hardcode)
- [x] `build-site.sh` green; link check; leakage gate
- [x] Docs: this delivery + FACTORY ledger updated

**Verified 2026-07-20:** full `build-site.sh` exit 0 — 2626 HTML pages; link check 0 broken (718 pages scanned: en-US + root stubs); leakage PASS; sitemap 358 URLs.

### Validation commands

```bash
bash generator/scripts/build-site.sh
python3 generator/scripts/check-internal-links.py dist
# expect 0 broken including stubs
python3 generator/scripts/check-leakage-gate.py dist
# smoke: grep lang= dist/en-US/index.html → en-US
# smoke: head dist/start/install.html → refresh to /en-US/start/install.html
```

## Companion skill plan

| Skill | Use |
|---|---|
| consequences | Blast radius already folded into this spec |
| clean-break | No English-at-root content; stubs only |
| correctness | After build: lang, paths, dual locale |
| polish | Generator sources + scripts touched |
| maid/housekeeping | Format/lint only if phase introduces debt |

## Open questions

| Q | Default if unresolved |
|---|---|
| Portal coverage on `/` | Phase 2 only; Phase 1 `/` → `/en-US/` |
| Sitemap: all locales or en-US only | **en-US primary + later expand**; include `en-US` URLs not root content |
| Brand href during Phase 1 | `/{site_locale}/` |
| Whether corpus English moves under `/en-US/corpus/` | **Yes** — consistent with content locale prefix |

## Deferred to later phases

Portal UI; two-hash provenance; sync tools; chrome.toml; th-TH prose.
