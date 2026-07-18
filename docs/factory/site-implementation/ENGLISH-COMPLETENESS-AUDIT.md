# English Completeness Audit — faberlang.dev

**Date:** 2026-07-18
**Scope:** Internal-link integrity of English HTML pages in `dist/`
**Tool:** `generator/scripts/check-internal-links.py` (re-runnable)

## Method

`check-internal-links.py` scans every `.html` file under `dist/` (excluding
locale dirs: `ar/`, `th-TH/`, `vi/`, `hi/`, `zh-Hans/`, `zh-Hant/`) for
internal `href="/..."` links and verifies the target exists on disk.

## Results

| Surface | Pages | Links checked | Broken |
|---|---|---|---|
| **Authored English** (start, features, syntax, tooling, ecosystem, references, history) | 40 | ~70 | **0** |
| **Nav / sidebar** (hardcoded in `html.fab`) | — | ~25 | **0** |
| **Corpus index** (`/corpus/index.html`) | 1 | 212 | **0** |
| **Corpus term pages** (`/corpus/*.html`) | 313 | ~5 700 | **73** |
| **Total (non-locale)** | 354 | 6 004 | **73** |

### Nav completeness: clean

All sidebar links, renderbar links, and the corpus index resolve. No
missing section index, no broken nav target.

### Authored English pages: clean

Every manually-authored Markdown page renders and all internal links
resolve.

### Corpus cross-references: 73 broken links, 36 unique missing targets

Corpus term pages auto-generate cross-reference links to related terms.
When a referenced term does not have its own generated page, the link is
dead. This is a **generated-content gap**, not an authored-content error.

**Categorised missing targets (36 unique):**

#### Glyph / symbol pages (14)

| Target | Refs |
|---|---|
| `/corpus/⇥.html` | 10 |
| `/corpus/∷.html` | 5 |
| `/corpus/⊻.html` | 3 |
| `/corpus/¬.html` | 2 |
| `/corpus/….html` | 2 |
| `/corpus/≠.html` | 2 |
| `/corpus/⊖.html` | 2 |
| `/corpus/!(.html` | 1 |
| `/corpus/![.html` | 1 |
| `/corpus/=.html` | 1 |
| `/corpus/⇐.html` | 1 |
| `/corpus/⇒.html` | 1 |
| `/corpus/≤.html` | 1 |
| `/corpus/≥.html` | 1 |

#### Term pages (22)

| Target | Refs |
|---|---|
| `/corpus/annotation-sugar.html` | 7 |
| `/corpus/sermo.html` | 5 |
| `/corpus/arena.html` | 2 |
| `/corpus/imperium.html` | 2 |
| `/corpus/non est.html` | 3 |
| `/corpus/nonnihil.html` | 2 |
| `/corpus/prima.html` | 2 |
| `/corpus/scrinium.html` | 2 |
| `/corpus/ultima.html` | 2 |
| `/corpus/accipe.html` | 1 |
| `/corpus/appende.html` | 1 |
| `/corpus/ab pipeline.html` | 1 |
| `/corpus/filtrata.html` | 1 |
| `/corpus/longitudo.html` | 1 |
| `/corpus/nonnulla.html` | 1 |
| `/corpus/nota.html` | 1 |
| `/corpus/objectum.html` | 1 |
| `/corpus/prae.html` | 1 |
| `/corpus/radix.html` | 1 |
| `/corpus/tempus.html` | 1 |
| `/corpus/typi-parametri.html` | 1 |
| `/corpus/vacua.html` | 1 |

## Leakage check: clean

No English-authored page links to locale-specific draft content
(`/ar/`, `/th-TH/`, etc.). Locale directories are intentionally public
with a visible "Translation status" notice on each page.

## Recommendation

The 36 missing corpus targets fall into two fix paths:

1. **Generate missing term pages** — add corpus definitions for the 22
   terms and 14 glyphs to the corpus source, then re-render. This is
   corpus-authoring work, not site infrastructure.

2. **Suppress dead cross-references** — modify the corpus renderer to
   emit plain text instead of a link when the target term has no page.
   This is a `render-corpus-batch.sh` / generator change.

Either path is a separate unit; this audit establishes the baseline.

## Re-run

```bash
python3 generator/scripts/check-internal-links.py
# Exit 0 = clean; 1 = broken links found

# Include locale dirs:
python3 generator/scripts/check-internal-links.py --include-locales
```
