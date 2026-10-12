# Delivery: Phase 2 — Locale-less language portal at `/`

## Interpreted unit

Replace the interim `dist/index.html` redirect with a **generated, locale-less
language portal** at `/`. The portal lists every discovered locale in its own
script, shows a short code sample from that pack's `[llm] exemplars`, and links
into `/{site_locale}/`.

**Unit goal:** `/` demonstrates the multilingual thesis in five seconds; it is
not the English homepage and not a redirect stub.

## Normalized spec

### Functional requirements

1. **Portal owns `/`.** `dist/index.html` is a full Speculum-styled portal page
   (no meta-refresh to `/en-US/`).
2. **Locale list** comes from dir presence under `src/` enriched by
   `generator/locales.toml` (native_name, reader_locale, status).
3. **Each entry shows:**
   - language name in its own script (`native_name`)
   - site locale id (e.g. `th-TH`)
   - status from registry (`complete` / `partial`)
   - a code sample drawn from
     `radix/stdlib/reader/{reader_locale}/exemplars/salve-munde.*.fab`
     (fallback: first file under that pack's `exemplars/` if salve missing)
   - a link to `/{site_locale}/`
4. **English entry** uses site `en-US`, sample from pack `la`, label from
   registry (`English` / complete).
5. **Code samples** are fenced display only (escaped HTML); no client-side
   translation. Use existing `.faber-code` styling.
6. **Chrome:** portal is not a docs page with sidebar. Centered gate layout
   (Speculum porta spirit). Shared tokens via `speculum.css` only (Decision 14).
7. **Agent surfaces** remain linked from the portal (`/llms.txt`, install path
   `/en-US/start/install.html`).
8. **Redirect stubs** still cover retired content paths; they must **not**
   overwrite the portal `index.html`.
9. **Smoke + gates** assert portal content; full build green.

### Non-goals

- Per-locale coverage fractions (deferred; GOAL open question)
- Hexagon geometry as a hard requirement (nice if CSS stays simple; grid OK)
- Localizing portal chrome strings (portal is intentionally multi-script /
  English meta copy is acceptable for the gate)
- Chrome catalog (Phase 4)
- Provenance / sync (Phase 3+)

## Repo-aware baseline

| Surface | Phase 1 | Phase 2 |
|---|---|---|
| `dist/index.html` | redirect → `/en-US/` | portal page |
| `generate-redirects.py` | writes stubs including index | skip `index.html` |
| `build-site.sh` smokes | assert redirect home | assert portal markers |
| `speculum.css` | no porta rules | add `.porta` layout |
| New script | — | `generate-portal.py` |

**Pack samples path (workspace):**  
`/Users/ianzepp/work/faberlang/radix/stdlib/reader/{reader}/exemplars/`

## Stage graph

```text
S1 generate-portal.py + portal CSS
       ↓
S2 generate-redirects skip index; build-site wire + smokes
       ↓
S3 full build + gates
```

## Implementation work

| ID | Work | Files |
|---|---|---|
| W1 | `generate-portal.py` | `generator/scripts/generate-portal.py` |
| W2 | Porta styles | `generator/www/speculum.css` |
| W3 | Redirects skip index; build integration | `generate-redirects.py`, `build-site.sh` |
| W4 | Optional: sitemap include `/` | `generate-sitemap.py` |
| W5 | Regenerate dist; commit | `dist/`, docs |

### Portal copy (defaults)

- Kicker: `Faber · porta · what do you read?`
- Question: one short paragraph on one semantic core, many renderings
- Status note: honest — partial locales are Stage 7 fallback proofs; English is complete
- Do **not** claim packs are unshipped (Speculum mockup is stale)

## Checkpoints and gates

**Acceptance**

- [x] `dist/index.html` has no meta-refresh to `/en-US/` as its only behavior
- [x] Portal lists all 7 locales with `native_name` visible (Thai/Arabic/etc. scripts present)
- [x] Each entry has a non-empty code sample
- [x] Links resolve to `/{locale}/` (en-US homepage exists)
- [x] Retired path stubs still work
- [x] `build-site.sh` green

**Verified 2026-07-20:** full build exit 0; portal has 7 cards; no refresh on `/`;
stubs still redirect content paths; link/leakage gates PASS.

**Validation**

```bash
bash generator/scripts/build-site.sh
# smokes assert portal
rg -n 'porta|ภาษาไทย|العربية|简体中文' dist/index.html
# no: meta refresh only page
! rg -q 'http-equiv="refresh"' dist/index.html || true  # portal must not refresh
```

**Release:** still defer push without operator auth.

## Open questions

| Q | Default |
|---|---|
| Coverage fractions on portal? | No (defer) |
| Hexagon vs card grid? | Card grid first; porta CSS may approximate ring on wide screens |
| English sample pack | `la` via reader_locale |

## Batching

One factory phase. Pattern is a single new script + CSS + wire.
