# GOAL: agent canon — plain Markdown an agent can fetch

**Status**: done — units 1–6 landed. The agent canon is `/agents/index.md`. Install pin is Faber 1.8.0. Publish by pushing `main`.
**Created**: 2026-10-01
**Campaign:** —
**Source:** operator session 2026-10-01. People will hand an agent `faberlang.dev` and say "find the docs," not read the HTML themselves.
**Repos:** `faberlang.dev`
**Related:** `static/llms.txt`, `static/agents/index.md`, `generator/scripts/render-llms.py`, `generator/scripts/check-internal-links.py`

---

## Invariant

An agent that fetches `https://faberlang.dev/llms.txt` is sent to `/agents/index.md` and, from there, only to other `/agents/**/*.md` files. Those files are plain Markdown in the English reader spelling. Each one is a rule, one program, and the forms not to write. HTML documentation stays the human site.

## Problem

The published agent entry teaches the wrong surface and the wrong tree.

- `static/llms.txt` (copied to `dist/llms.txt`) is a map of `/en-US/*.html`. It still calls `/` a compute-first homepage and teaches Latin (`functio`, `T ∪ nihil`, `@ nucleum`).
- `static/agents/index.md` is the same kind of map. Its sample program is Latin. `render-llms.py` and the landing page both send agents there.
- `dist/llms-full.txt` is generated. Its preamble (through the "Language shape" section) says `/` is the locale chooser, tells the agent to read HTML and the corpus catalog first, pins Faber 1.1.1, and teaches `functio` / `T ∪ nihil`. The install page's current release is Faber 1.8.0 (`src/en-US/start/install.md`).
- `src/en-US/**/*.md` is the Latin authoring surface. English spellings are applied at HTML render time. Serving those files raw would teach Latin.
- `check-internal-links.py` scans agent URLs only for a fixed list: `llms.txt`, `llms-full.txt`, `agents/index.md`, and `.well-known/agent-skills/**`. A new file under `/agents/` is invisible to that gate. The gate exists because an earlier information architecture left agent docs citing redirect stubs.

`build-site.sh` copies `static/` onto `dist/` and does not overwrite `llms.txt`. `render-llms.py` writes `llms-full.txt` only.

## Proposal

Locale-less Markdown under `/agents/`, authored in `static/agents/` and copied to `dist/agents/` by the existing static copy.

```text
/agents/index.md                 overviews that exist, in fetch order
/agents/<topic>.md               one rule and one program
/agents/<topic>/<slug>.md        one construct agents copy wrong
```

Agreed tree. A file is added only when the parent lists it, and the parent lists only files that exist.

| Overview | Children | When |
| --- | --- | --- |
| `program.md` | — | unit 1 |
| `functions.md` | `parameters`, `returns`, `borrows`, `async`, `entry` | `parameters` in unit 1; the rest in unit 2 |
| `types.md` | `widths`, `null`, `collections` | unit 3 |
| `errors.md` | `failable`, `recovery`, `guards` | unit 4 |
| `control.md` | — until a second program is required | unit 5 |
| `generics.md` | — | unit 5 |
| `modules.md`, `packages.md`, `check.md`, `locales.md`, `libraries.md`, `grammar.md` | — | unit 5 |

`index.md` lists overviews only. An overview lists its children, one line each, and that line is the child's whole contract. A child links to its parent and to at most one sibling. No `+++` frontmatter, no `{#anchors}`, no links into `/en-US/`.

Fences are English and declared:

```text
```faber locale=en
```

Produce the source with `faber convert --from la --to en` from a program that already checks (the hello package in `src/en-US/start/hello.md` for unit 1). Paste the converter output. Do not hand-spell keywords.

`/llms.txt` becomes a short pointer: fetch `/agents/index.md`, then a short install block taken from `src/en-US/start/install.md` (Faber 1.8.0, the two archive URLs). It does not list the HTML tree.

The `llms-full.txt` preamble is edited to match that pointer and to stop teaching Latin as the spelling an agent writes. The generated catalog body stays. Do not regenerate the catalog in these units; a corpus drift dump is a different change. Edit `render-llms.py` and the same lines in `dist/llms-full.txt`.

`AGENT_SURFACE_GLOBS` gains `agents/**/*.md` in unit 1, so every new page is scanned.

### Non-goals

- Mirroring `src/en-US/` or the corpus as Markdown.
- Rewriting human HTML pages.
- Translating `/agents/` into other site locales.
- Rewriting `.well-known/agent-skills/` in unit 1. Those skills still teach the old path until unit 6.
- A full `build-site.sh` run. Static Markdown is copied. The catalog body is not regenerated.

## Units

| Unit | Scope | Depends on | Status |
| --- | --- | --- | --- |
| 1 | Spine. See below. | — | done |
| 2 | `functions/{returns,borrows,async,entry}.md`, and the matching lines in `functions.md` | 1 | done |
| 3 | `types.md` plus `types/{widths,null,collections}.md`; `index.md` gains `types.md` | 1 | done |
| 4 | `errors.md` plus `errors/{failable,recovery,guards}.md`; `index.md` gains `errors.md` | 1 | done |
| 5 | The remaining single-file overviews in the table above; `index.md` gains each as it lands. Also the `program.md` manifest, which `faber check .` now requires. | 1 | done |
| 6 | Point `.well-known/agent-skills/` at `/agents/` and remove Latin samples there. Install pin matches Faber 1.8.0. | 1 | done |

Units 2–5 may proceed in parallel after unit 1. They share `index.md` only when a unit adds its own overview line. Unit 2 edits `functions.md`, which unit 1 creates, so unit 2 waits. Units 3–5 do not edit `functions.md`.

### Unit 1 — first implementation piece

One logical change: the fetch entry, one package, and one parent/child pair so the directory pattern is real.

**Write scope**

- `static/agents/index.md` (replace)
- `static/agents/program.md` (new)
- `static/agents/functions.md` (new)
- `static/agents/functions/parameters.md` (new)
- `static/llms.txt` (replace with the short pointer plus the 1.8.0 install block)
- `generator/scripts/render-llms.py` (preamble only: start-here, install version, language shape)
- `dist/llms-full.txt` (the same preamble lines, catalog body untouched)
- `generator/scripts/check-internal-links.py` (`agents/**/*.md` in `AGENT_SURFACE_GLOBS`)
- `dist/llms.txt` and `dist/agents/**` copies of the static files
- `AGENTS.md` layout note for `/agents/`, so the next session does not rebuild the HTML map

**Edit**

`index.md` fetch order is `program.md`, then `functions.md`. `functions.md` lists only `parameters.md`. `program.md` is the hello package in English: `faber.toml` shown as text, `src/main.fab` in one `locale=en` fence. `parameters.md` is one function whose parameters are type-first, plus a "do not write" list (`name: T`, `T?`).

**Done when**

- `index.md` cites no URL except the four `/agents/` pages this unit adds, `/llms.txt`, and the install URLs that `static/llms.txt` keeps.
- No file in the write scope teaches `functio`, `numerus`, `textus`, `nihil` as the spelling to write, or calls `/` compute-first.
- `generator/scripts/validate-fences.sh static/agents` passes.
- `dist/agents` and `dist/llms.txt` match `static/`.
- `python3 generator/scripts/check-internal-links.py dist` reports zero broken and zero stub agent-surface URLs. Pre-existing HTML breakage, if the full script is red for an unrelated page, is reported and not fixed here.

**Out of this unit**

The other function children, `types/`, `errors/`, the single-file overviews, and the skill files.

## Validation

Unit 1 sanity is the done-when list above. Later units run `validate-fences.sh` on the files they add and the agent-surface half of `check-internal-links.py`. A full `build-site.sh` is not a unit gate. It remains the way a later content change republishes `dist/`.

Release: not-applicable. This repo publishes by pushing `main`; this goal does not cut a release.

## Ledger

| Unit | Status | Receipt |
| --- | --- | --- |
| 1 spine | done | `f665e3349` |
| 2 function children | done | 26 fences, 0 failed, with units 3–6 |
| 3 types | done | 26 fences, 0 failed, with units 2 and 4–6 |
| 4 errors | done | 26 fences, 0 failed, with units 2–3 and 5–6 |
| 5 remaining overviews | done | 26 fences passed, 0 failed. Agent-surface URLs 414, 0 broken, 0 stubs. HTML scan 0 broken. `static/agents` matches `dist/agents`. `faber init` manifest: `faber check .` exits 0 and `faber run .` prints `Salve, munde!`. Modules package: check exits 0 with `WARN003`, run prints `Salve, Marcus!`. `norma:text` run prints `ba`. No Triga or Gradus import on `libraries.md`. |
| 6 skills | done | Skills point at `/agents/index.md`. Install pin is Faber 1.8.0 with `bin/faber` and `share/faber`. No Latin sample. Same link gate: 414 URLs, 0 broken, 0 stubs. `static/.well-known/agent-skills` matches `dist/`. |

## Open questions

1. **Install block on `/llms.txt`.** Default: keep it, version read from `src/en-US/start/install.md` (now 1.8.0). An agent that only fetches the pointer still has to install the CLI.
2. **Catalog regen.** Default: do not run `render-llms.py` over the whole corpus in these units. Patch the preamble in the script and in `dist/llms-full.txt` together.
3. **Skill files.** Default: unit 6, after the canon has enough pages that a skill can point at them without sending the agent back into HTML.
