# Origin-authoritative site reconciliation

Handle: `ed694435`. Role: Hand. Lane: `factory/siterec`.

This is a reversible source reconciliation, **not render acceptance or a
campaign-completion record**. Main and origin refs were not changed. No push
or merge was performed. The operator owns landing, regeneration acceptance,
and the fate of the 16 dirty files.

## Measured three-way state

- Merge base: `e5fa17f2490dcb4d77b173186f22bd85451f4e65`.
- Origin: `d4de003b0d1b49598995ffdfd76711f8af55eb17`; seven commits
  exclusive of local main. Its net diff from the base is **2,291 files:
  2,227 dist files and 64 other files**. This contradicts the assignment's
  narrower description. All origin changes are the reconciliation base.
- Local main: `19e58c25e7d63e458316afcf44e2651943592410`; two commits
  exclusive of origin: `366e6b884` and `19e58c25e`. Their net diff is seven
  files: three generator scripts and four English source pages.
- Main working tree: 14 tracked source modifications plus two untracked
  diagnostic logs. All 16 live files and all 16 protected copies were
  independently SHA-256 checked against the preservation manifest.
- The dirty-path intersection with origin's net changes is exactly
  `src/en-US/reference/grammar.md`, despite origin's broader actual scope.

The protected directory
`worktrees/site2/scratch/site-dirty-preserved/` was only read. Its files were
not modified or deleted. A second exact copy, including the manifest, is now
in `worktrees/siterec/scratch/reconciliation/dirty-original/`.

## Collision: actual content, not timestamps

The full actual origin-to-dirty diff is attached losslessly compressed as
[collision.diff.gz](collision.diff.gz); the plain diff is also in lane scratch.
Compression preserves ordinary diff context-prefix spaces byte-for-byte.
Origin's grammar page is a 46-line family
overview. The dirty page is a 2,880-line English full grammar reference, with
261 numbered productions and substantial explanatory material.

Origin changed the overview wording from “Each family page lists the words”
to “Each family page explains that part of the language, then lists the
words.” It also added reader prose and examples to the nine family pages
and changed the generator to preserve that prose.

The dirty file removes that overview, its family table, and its agent-reference
route, drops `faber/docs/EBNF.md` from the source list, and installs the full
EBNF plus its surrounding documentation. This is a presentation collision,
not merely a newer rule count. Its production names match the current
sibling EBNF. That does not make it the right English overview.

Resolution in the lane: retain origin's overview, family prose, and routing;
combine the held rule-count change with origin's improved wording. The
held count is 262, but the current EBNF has 261 productions. The failed
partition gate below leaves that count and generated productions snapshot
unaccepted pending the operator-owned follow-up. The dirty full grammar
page was **not** copied over origin.

## Per-commit independent replay onto origin

Each original patch was tested using a separate temporary Git index seeded
with origin/main. The large site patch was additionally tested one file at a
time because the all-files application aborted on direct-apply failures.
These are three-way patch replays, followed by explicit path-limited commits,
not merges. Original held commits and their full binary patches remain intact.

| Original | Independent result on origin | Lane treatment |
|---|---|---|
| `86dc4c846` | 196 of 254 paths clean; 58 conflict/error paths: 52 dist paths, six localized matrix provenance stamps | Replayed 30 compatible source/static paths. Kept origin for the six provenance-only conflicts. Preserved all 218 old dist path changes in the original patch for fresh regeneration; did not install that old render over newer origin output. |
| `366e6b884` | Clean, three paths | Replayed as `bf373659c`. **Already on local main, not on origin; still needs operator-authorized landing.** |
| `c2872e03f` | Conflict only in `src/en-US/reference/grammar.md` | Replayed as `eb8af8c4e`; keep origin prose, apply the four family-map additions and held generated productions. |
| `5afe45cec` | Clean, three paths | Replayed as `8edd30f23`; keep origin's “Faber Romanus” title while adding tutorial routing. |
| `260906fd0` | Clean, two paths | Replayed as `53c1b3892`; keep origin's 1.12.0 documentation pin while adding fence-provenance instructions. |

Exact large-patch conflict paths are attached as
[site3-conflicts.paths](site3-conflicts.paths). All application logs and
per-file results remain under lane scratch `reconciliation/`.

The protected repair `19e58c25e` also conflicts in `language/types.md`, in
both atomic and sparse examples. Origin already repaired them using an
English mutable atomic parameter and English `var` sparse binding. Those
origin examples are retained byte-for-byte. The other seven repair intents
were replayed into three pages as `8e907182c`.

**The original `19e58c25e` remains reachable on untouched local main.** Its
original patch is preserved in lane scratch. Its exact SHA is not an ancestor
of the new linear branch; the repair is represented by the new commit plus
origin's two already-fixed examples. No original repair commit was dropped
or garbage-collected.

## Reconciled code commits

| Commit | Subject |
|---|---|
| `bf373659c` | generator: preserve projector field-name guard over origin |
| `8e907182c` | docs: preserve fence repairs without reverting origin examples |
| `eb8af8c4e` | grammar: fit family-map repair around origin reader prose |
| `8edd30f23` | docs: replay agent tutorial split over origin |
| `53c1b3892` | docs: retain fence compiler provenance over origin |
| `f9e081fba` | site: reconcile held reference sources without stale render overwrite |

Origin is an ancestor of the branch. Among paths changed by origin, lane
changes touch only AGENTS.md, the grammar-tree generator, glyphs.md, the
grammar overview, and the agent index; their origin edits remain present.
The only committed dist change is the clean held agent grammar productions
file, which origin did not change. There is **no fresh full-site render**.

## Dirty files: measured regeneration and recommendation

None of the 16 original dirty files was admitted to the branch as a dirty
snapshot. They are deliberately set aside, pending the operator's decision.

- Seven matrix candidates were produced using the live Python generator's
  `load_pack`/`build_page` functions and current packet matrix input, with
  scratch destinations. The English candidate is byte-identical to the dirty
  English matrix. The six localized candidates differ from the dirty copies
  **only in `source_commit`**, now stamped `f9e081fba65130c79907dbf02b036c2dee5fdc67`
  rather than `366e6b884f798e2670db95d7961693e5185d9ecf`.
- English grammar-tree generation ran with explicit current packet inputs
  and scratch destinations, but produced no candidate: the partition gate
  rejected `closure_modifier`, absent from the current EBNF.
- The other six grammar pages require the native grammar generator. Their
  exact regeneration is deferred with the native toolchain, not asserted.
- `generator/a2.pkgs.txt` and `generator/b2.pkgs.txt` are identical 153,146-byte,
  1,635-line compiler-diagnostic logs, not package-list build inputs.

Recommendation: do not copy the dirty English full-grammar page onto
origin's overview. Keep the diagnostic logs out of publication commits.
After the partition mismatch is explicitly resolved, regenerate the seven
matrix and six non-English grammar pages from the reconciled inputs, render
fresh dist, and submit the resulting source/output diff for the operator's
choice. The current seven matrix candidates are available now for review.
This is a recommendation, **not a decision to discard or commit the 16 files**.

## Site gates and timing

Measured once on battery, using Homebrew-first PATH. Every subprocess had a
60-second timeout. Exact commands and timings are in
[gate-results.json](gate-results.json).

| Check | Result | Wall seconds |
|---|---|---:|
| Projector unit tests | 13 tests, pass | 0.086 |
| Agent-reference unit tests | 21 tests, pass, one skipped | 0.066 |
| Agent-locales unit tests | 15 tests, pass | 0.167 |
| Corpus-locale unit tests | 6 tests, pass | 0.063 |
| Generator HTML-literal gate | Pass | 0.350 |
| Width gate | Pass | 0.029 |
| Internal-link gate on inherited dist | 24,796 links, 671 agent URLs, zero broken | 0.199 |
| Leakage/honesty gate on inherited dist | Pass | 0.465 |
| Frontmatter-leak gate on inherited dist | Zero affected pages | 0.360 |
| English grammar-tree regeneration | **Fail: family map names productions not in the EBNF: closure_modifier** | 0.064 |
| Seven matrix candidates | Pass; comparisons above | 0.086 |

The inherited-dist gates are not proof that new source changes have rendered.
No checks or acceptance thresholds were weakened.

The full build executable path was inspected first: `build-site.sh` needs
`faber convert`, native `faber run` generators, `faber build ... -t rust`,
and a release Cargo generator build. The packet has no compiler binary and
no compiler or generator target cache. Radix is read-only in this assignment.
The site's recorded powered baseline is about 200 seconds for a full build,
114.7 seconds for the cold generator alone; it is not a battery estimate.
No cold native build was launched or rerun for speed. Current native grammar,
redirect/sitemap generation, fence validation, localization, generator
compilation, and full render/smoke acceptance are explicitly deferred.
The current grammar-tree failure would independently stop the full build
before generator compilation.

Readable packet source revisions:

- Radix: `aa6a818a9d407e7fc39928f6af6c165c9a0c1059`
- Faber: `65721209213f8f42f98ecf74a21f6854c02307d3`
- Norma: `6b070c77f432d52c340607740d508b4b888d73c6`
- Examples: `5900a366d311d4f0d59ed4eeed6e74aa10bae02c`

## Handoff and residual

All branch commits are **UNMERGED**. Mind must retain ownership of
`factory/siterec` as operator-gated integration debt. Do not retire this lane
or the protected backup while the dirty-file decision or deferred render is
outstanding. Landing and push require operator action/authorization.

Residual: the current EBNF/family-map mismatch is a concrete failing gate;
the full native build and new dist render remain unproven. The original old
render patch is not accepted output. No campaign-completion claim is made.
