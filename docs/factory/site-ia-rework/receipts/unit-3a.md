# Unit 3a receipt — grammar family tree (seat …586c, deepseek-flash)

Merged: `54095c9d0` → main merge `343dd137b` (2026-10-02).

- `generate-grammar-tree.py` (644 lines): parses the EBNF fence from
  `faber/docs/EBNF.md`, partitions **all 258 productions into 9 families**,
  fails closed on partition drift, degrades to no-op without siblings.
- `src/en-US/reference/grammar.md` regenerated as the tree index (same URL);
  9 family pages under `src/en-US/reference/grammar/`.
- 138 corpus term links emitted, all verified to exist and be canonical
  (checked against committed `dist/en-US/corpus/`).
- Family pages carry `translate_spans = false` (HTML span pass exempt).

## Families (258 productions)

program 30 · declarations 42 · annotations 15 · types 32 · statements 35 ·
expressions 69 · patterns 11 · errors 4 · lexical 20.

## Nav entries (Grammar children)

Grammar → `/reference/grammar.html` (section `grammar`) with children per
family: `/reference/grammar/{program,declarations,annotations,types,
statements,expressions,patterns,errors,lexical}.html`, sections
`grammar-<slug>`. Per-locale translations supplied in the seat report
(10 keys, 6 locales). NOTE: emitter stamps `section = "reference"` on
family pages today; either nav derives active path from URL or the emitter
stamps `section = "<slug>"` (one-line change) — decide at chrome wiring.

## Wiring (parent applies, build-site.sh step 0b, AFTER generate-grammar)

```bash
    "$PYTHON" "${SCRIPT_DIR}/generate-grammar-tree.py"
```

## Parent patch applied at merge

`project_reader_terms.py` `project_markdown` skip broadened to
`"/reference/grammar/" in rel` (else `publica` production ids get rewritten
by the en projection).

## Residuals

- EBNF non-production sections (Production Index, Lexicon Appendix, Keyword
  Reference, Comma Separator Table, Normative Language Notes) have no home
  in the tree — candidate follow-up (lexical page / index).
- en-US only; other locales keep the single-page grammar until unit 6.
- Corpus-link verification reads committed `dist/en-US/corpus/` at emit
  time (pre-`rm -rf dist`) — a corpus set change in the same build could
  drift one build behind.
