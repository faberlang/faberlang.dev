# Unit 2 receipt — The Language bucket (seat …c8d2b, deepseek-flash)

Merged: `50bb04267` + `f2bb3b460` → main merge `84c049c1c` (2026-10-02).

- `generate-overview.py` (new): assembles `src/en-US/language/overview.md`
  from the committed `generator/landing/` cache only (Latin program panel +
  real output, Rust emit panel, targets table). Idempotent; no siblings
  required; errors loudly on a missing panel.
- Behavior section, 6 pages on the agreed spine: glyph-law, type-first,
  numeric-widths (store-only law), sealed-locales, packages,
  errors-and-tests. All fences pass validate-fences (Latin-authored fluid
  fences; en build transcodes — verified byte-identical via
  `faber convert --from la --to en`).
- `generator/redirects/language-bucket.toml`: 5 rows (below).

## Nav entries (Language group; Behavior as nested subgroup)

- Overview → `/{l}/language/overview.html` (section `overview`)
- Behavior (subgroup): glyph-law, type-first ("Types before names"),
  numeric-widths ("Math in the ether"), sealed-locales, packages
  ("A program is a package"), errors-and-tests
- Frontmatter `order`: overview 1; behavior 10–15.

Translations for th-TH/zh-Hans/zh-Hant/vi/ar/hi supplied in the seat
report; `overview` label already exists in each chrome.toml — reuse.

## Wiring (parent applies, step 0b, after generate-examples.py)

```bash
    "$PYTHON" "${SCRIPT_DIR}/generate-overview.py"
```

## Redirect rows

```
/en-US/features/latin-and-glyphs.html   → /en-US/language/behavior/glyph-law.html
/en-US/features/canonical-vs-sugar.html → /en-US/language/behavior/glyph-law.html
/en-US/features/commandments.html       → /en-US/language/behavior/glyph-law.html
/en-US/features/reader-locale.html      → /en-US/language/behavior/sealed-locales.html
/en-US/features/testing.html            → /en-US/language/behavior/errors-and-tests.html
```

`features/frames.html` and `features/compilation-lanes.html` stay at their
existing destinations.

## Residuals (parent-tracked)

- **Runner numeric defect (file against radix):** `(a+b)/2` over
  `modulus<u8>` printed **22** — mid-expression reduction, contradicting
  the settled store-only law (exact 300/2 = 150, reduced at the store).
  Docs correctly show only the law + the correct conversion-path behavior.
- `ia-redirects.py` already maps the same `features/` URLs elsewhere —
  closeout must let this fragment supersede (reconcile at unit 6).
- `toolchain/packages.html` still prints the stale `[nomen]/[ingressus]/
  [scopulus]` manifest shape — defect for that page's owner (small fix).
- `locale=X` fences cannot be validated in this environment (radix debug
  fails to load every on-disk pack — same compiler-side defect as unit 5's
  finding); pages therefore use Latin-authored fluid fences + transcode.
- Full render pending the faber-1.11 toolchain; structure verified with
  the prebuilt speculum-gen.
