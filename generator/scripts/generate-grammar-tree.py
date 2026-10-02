#!/usr/bin/env python3
"""generate-grammar-tree.py — split the grammar wall into a navigable tree.

The grammar used to be one page: every production in a single fence, 2,788
Markdown lines with no way to drill in. This emitter groups the productions
into families drawn from the EBNF's own organization and writes one page per
family, then regenerates the grammar index as a short family list. The index
keeps its URL (`/reference/grammar.html`).

Inputs (resolved from a sibling workspace checkout, same convention as
`generate-grammar`):

  faber/docs/EBNF.md                    the production list (canonical Latin)
  faber/docs/grammar/grammar.jsonl      the id spine, anchors, and keywords
  radix/locale/en/pack.toml             the English reader projection

Outputs:

  src/en-US/reference/grammar.md              the family index (URL unchanged)
  src/en-US/reference/grammar/<family>.md     one page per family

Productions render in the English reader spellings: quoted words are projected
through the reader pack, rule names and UPPERCASE terminals stay the stable
Latin identities. Keywords that resolve to an existing canonical corpus page
under `dist/en-US/corpus/` become term links; alias stubs are followed to
their target so only canonical pages are linked.

The script degrades gracefully: when a sibling input is absent it leaves the
committed output alone and exits 0, so a checkout without the compiler tree
still builds.

Usage:
    generate-grammar-tree.py [--ebnf PATH] [--jsonl PATH] [--pack PATH]
                             [--corpus DIR] [--index PATH] [--family-dir DIR]

en-US only for now. The family map and projection are locale-shaped, but a
locale page can be added later by substituting the reader pack and output
directory.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import tomllib
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]

# ---------------------------------------------------------------------------
# Family map — an exact partition of every production in the EBNF.
#
# Families follow the EBNF's own headings (Program Structure, Declarations,
# Types, Control Flow, Error Handling, Expressions, Patterns) plus the two
# clusters the production ids make explicit: the `@` annotation family and the
# lexical terminals. `lexical` is taken from the EBNF's own stated convention —
# an UPPERCASE rule name is a lexical terminal — rather than listed by hand, so
# it tracks the spine. Every other id is named here.
#
# The emitter fails closed on drift: an unlisted production, a duplicate, or
# a stale id aborts the run rather than silently dropping grammar.
# ---------------------------------------------------------------------------

FAMILIES: list[dict] = [
    {
        "slug": "program",
        "title": "Programs, regions & imports",
        "blurb": (
            "The shape of a source file: optional frontmatter, the optional "
            "`module` region, the top-level statement spine, imports, and the "
            "program entry points and test suites."
        ),
        "ids": """
            fab_file frontmatter program regio_decl statement ad_handler_decl
            statement_core importa_decl importa_record import_field_list
            import_field ex_field visibilitas_field nomen_field ut_field
            omnia_field importa_sugar publica named_import wildcard_import
            selective_import import_value_binding entry_header incipit_stmt
            incipiet_stmt probandum_decl probandum_body proba_stmt proba_modifier
            praepara_block
        """.split(),
    },
    {
        "slug": "declarations",
        "title": "Declarations & bindings",
        "blurb": (
            "Bindings, functions, generic parameters, closures, classes, and "
            "the fields and methods a class holds."
        ),
        "ids": """
            binding_decl expr_stmt block_stmt const_init insere_expr fixum_decl
            figendum_decl sit_decl array_destruct object_destruct functio_decl
            param_list generic_params type_param_list size_param_list
            generic_param size_param generic_bound contract_ref
            generic_type_default generic_size_default call_type_args parameter
            func_modifier callable_posture return_clause alternate_exit_clause
            ergo_joint clausura_joint clausura_expr compact_clausura_expr
            clausura_signature closure_modifier fac_block clausura_legacy_expr
            clausura_params clausura_param genus_decl genus_member
            genus_field_decl field_decl functio_method_decl
        """.split(),
    },
    {
        "slug": "annotations",
        "title": "Annotations & directives",
        "blurb": (
            "The `@` annotation family: the generic shape, the kernel "
            "(`@ kernel`), compiler-lane (`@ radix`), and capability "
            "(`@ call`) directives."
        ),
        "ids": """
            annotation annotation_name braced_annotation annotation_field_list
            annotation_field annotation_sugar nucleum_annotation nucleum_sugar
            nucleum_braced nucleum_modifier nucleum_field_list nucleum_field
            radix_annotation radix_directive ad_annotation
        """.split(),
    },
    {
        "slug": "types",
        "title": "Types & contracts",
        "blurb": (
            "Type syntax and the declarations built on it: interfaces, type "
            "aliases, enums, tagged unions, and relational schemas."
        ),
        "ids": """
            implendum_decl implendum_method_decl typus_decl ordo_decl
            enum_member discretio_decl union_fields union_member variant
            variant_fields schema_decl schema_column type_annotation
            concrete_type union_hole_type intersection_type owned_type base_type
            failable_promissum_type ratio_type hole_type qualified_type type_head
            type_arguments type_argument labeled_type_argument width_type_sugar
            shape_suffix figura figura_list function_type type_list
        """.split(),
    },
    {
        "slug": "statements",
        "title": "Statements & control flow",
        "blurb": (
            "Statements and control flow: conditionals, loops, `switch` and "
            "`match`, guards, extraction, loop and function transfer, and the "
            "diagnostic statements."
        ),
        "ids": """
            si_stmt si_tail secus_clause arm else_arm dum_stmt itera_stmt
            itera_binding apud_clause elige_stmt casu_elige_clause
            ceterum_clause discerne_stmt discriminants subject_path
            casu_variant_clause custodi_stmt si_guard_clause ex_stmt
            extract_fields extract_field ceteri_field redde_stmt reddet_stmt
            tacebit_stmt cede_stmt rumpe_stmt perge_stmt tacet_stmt adfirma_stmt
            requirit_stmt reice_stmt inc_dec_stmt nota_stmt fac_stmt
        """.split(),
    },
    {
        "slug": "expressions",
        "title": "Expressions & operators",
        "blurb": (
            "Expressions and the operator stack, from the assignment root down "
            "through the precedence ladder to calls, literals, and the "
            "collection and JSON forms."
        ),
        "ids": """
            expression transfer assignment place ternary aut_expr et_expr
            equality equality_tail comparison format_expr bitwise_or_expr
            bitwise_xor_expr bitwise_and_expr shift_expr range_expr range_tail
            additive_expr multiplicative_expr vel_expr vel_rhs vel_range_tail
            unary_expr gradient_expr gradient_selection gradient_place cast_expr
            conversio_expr interval_target via_clause inline_default call_expr
            call_suffix member_suffix transpose_suffix optional_suffix
            non_null_suffix argument_list argument template_argument literal
            primary ad_expr ad_opener array_literal iuncta_expr json_literal
            json_member typed_constructor field_list field_init field_key
            construction_source json_value json_object json_array json_string
            json_number finge_expr qualified_ident praefixum_expr scriptum_expr
            lege_expr first_match_expr summa_expr filum_clause extrema_expr
            extrema_identity capta_expr
        """.split(),
    },
    {
        "slug": "patterns",
        "title": "Patterns & destructuring",
        "blurb": (
            "Patterns and destructuring: the atoms a match arm accepts, type "
            "and alias patterns, and the object and array destructuring forms."
        ),
        "ids": """
            patterns pattern pattern_atom negated_number type_pattern
            ut_pattern pattern_binding object_pattern pattern_property
            array_pattern array_pattern_element
        """.split(),
    },
    {
        "slug": "errors",
        "title": "Error channel",
        "blurb": (
            "The error channel: throwing, guarded throws, and the local "
            "`catch` handler that recovers an error into a value."
        ),
        "ids": """
            iace_stmt iace_expr iace_guarded_expr cape_clause
        """.split(),
    },
    {
        "slug": "lexical",
        "title": "Lexical structure & glyphs",
        "blurb": (
            "The terminal tokens the lexer produces: identifiers, numbers, "
            "strings, width markers, and the frontmatter delimiter. Uppercase "
            "rule names here are lexical terminals."
        ),
        # Filled from the jsonl `region` field at load time.
        "ids": [],
    },
]

INDEX_TEMPLATE = """\
+++
title = "Grammar"
section = "reference"
order = 1
sources = [
  "faber/docs/EBNF.md",
  "faber/docs/grammar/grammar.jsonl",
  "radix/locale/en/pack.toml",
]
+++

The formal grammar for every Faber production, generated from the compiler's
own specification and shown in the English reader spellings. The words in
quotes are the words you write: a loop is `for`, a class is `class`, a function
is `fn`. Rule names (`itera_stmt`, `genus_decl`) are stable grammar identifiers.
Latin stays the compiler's canonical form; `faber explain <term>` prints a
mapping from the compiler itself.

This page is the authority on whether something is valid syntax. The
[target matrix](/toolchain/target-matrix.html) is the authority on whether a
given target supports it.

The productions are grouped into families below. Each family page carries its
productions and links the productions whose keywords have a
[corpus term page](/en-US/corpus/). Uppercase names are lexical terminals;
grammar examples are fragments, not standalone programs.

## Production families {{#production-families}}

| Family | Productions | What it covers |
|---|---|---|
{rows}

All {total} productions. Every family page links back here, and rule names stay
stable across the tree so a search for `itera_stmt` finds its one page.
"""

FAMILY_TEMPLATE = """\
+++
title = "{title}"
section = "grammar-{slug}"
order = {order}
translate_spans = false  # rule names are the Latin identity, not a spelling
sources = [
  "faber/docs/EBNF.md",
  "faber/docs/grammar/grammar.jsonl",
  "radix/locale/en/pack.toml",
]
+++

{blurb}

Rule names (`fab_file`, `itera_stmt`) are the stable Latin grammar identifiers;
the quoted words are the English reader spellings. Return to the
[grammar index](/en-US/reference/grammar.html).

## Productions {{#productions}}

```ebnf
{productions}
```
"""

TERMS_SECTION = """
## Terms {{#terms}}

Keywords in these productions that have a corpus term page. The production id
on the left is the Latin spine name; the links are the English reader spellings
you write.

| Production | Terms |
|---|---|
{rows}
"""


def parse_args(argv: list[str]) -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--ebnf", default=None, help="path to faber/docs/EBNF.md")
    ap.add_argument("--jsonl", default=None, help="path to grammar.jsonl")
    ap.add_argument("--pack", default=None, help="path to the en reader pack")
    ap.add_argument("--corpus", default=None, help="path to dist/en-US/corpus")
    ap.add_argument(
        "--index",
        default="src/en-US/reference/grammar.md",
        help="index output, relative to the repo root",
    )
    ap.add_argument(
        "--family-dir",
        default="src/en-US/reference/grammar",
        help="family page directory, relative to the repo root",
    )
    return ap.parse_args(argv)


def workspace_roots() -> list[Path]:
    """Candidate sibling-workspace roots, nearest first."""
    roots: list[Path] = []
    for env in ("FABER_WORKSPACE", "FABER_LIBRARY_HOME"):
        value = os.environ.get(env)
        if value:
            roots.append(Path(value).expanduser().resolve())
    roots.append(REPO.parent)
    roots.append(REPO.parent.parent)
    unique: list[Path] = []
    for root in roots:
        if root not in unique:
            unique.append(root)
    return unique


def pick(explicit: str | None, roots: list[Path], rel: str) -> Path | None:
    if explicit:
        path = Path(explicit).expanduser().resolve()
        return path if path.is_file() else None
    for root in roots:
        candidate = root / rel
        if candidate.is_file():
            return candidate
    return None


def load_ebnf_productions(ebnf_path: Path) -> list[tuple[int, str, str]]:
    """Return [(number, id, rhs)] from the first ```ebnf fence, in file order."""
    text = ebnf_path.read_text(encoding="utf-8")
    fence = re.search(r"^```ebnf\n(.*?)^```\s*$", text, re.M | re.S)
    if fence is None:
        raise SystemExit(f"generate-grammar-tree: no ```ebnf fence in {ebnf_path}")

    marker = re.compile(r"^#\s*\[(\d+)\]\s+(\S+)\s*$")
    rule = re.compile(r"^(?P<id>[A-Za-z_][A-Za-z0-9_]*) ::=(?: (?P<rhs>.*))?$")

    productions: list[tuple[int, str, str]] = []
    pending: tuple[int, str] | None = None
    for raw in fence.group(1).split("\n"):
        line = raw.rstrip()
        if not line.strip():
            continue
        m = marker.match(line.strip())
        if m:
            pending = (int(m.group(1)), m.group(2))
            continue
        r = rule.match(line)
        if r:
            if pending is None:
                raise SystemExit(
                    f"generate-grammar-tree: production without a marker in "
                    f"{ebnf_path}: {r.group('id')}"
                )
            number, pid = pending
            if pid != r.group("id"):
                raise SystemExit(
                    f"generate-grammar-tree: marker/id mismatch in {ebnf_path}: "
                    f"marker {pid}, rule {r.group('id')}"
                )
            productions.append((number, pid, r.group("rhs") or ""))
            pending = None
            continue
        if line.strip().startswith("#"):
            continue
        raise SystemExit(
            f"generate-grammar-tree: unrecognized line in the ebnf fence of "
            f"{ebnf_path}: {line!r}"
        )
    if not productions:
        raise SystemExit(f"generate-grammar-tree: no productions in {ebnf_path}")
    return productions


def load_jsonl(jsonl_path: Path) -> dict[str, list[str]]:
    """Return {id: [keywords]} from the production spine."""
    import json

    keywords: dict[str, list[str]] = {}
    for line in jsonl_path.read_text(encoding="utf-8").split("\n"):
        if not line.strip():
            continue
        record = json.loads(line)
        pid = record.get("id")
        if not isinstance(pid, str) or not pid:
            raise SystemExit(
                f"generate-grammar-tree: record without a string id in {jsonl_path}"
            )
        kws = record.get("keywords", [])
        if not isinstance(kws, list) or not all(isinstance(k, str) for k in kws):
            raise SystemExit(
                f"generate-grammar-tree: bad keywords for {pid} in {jsonl_path}"
            )
        keywords[pid] = kws
    if not keywords:
        raise SystemExit(f"generate-grammar-tree: no records in {jsonl_path}")
    return keywords


def load_english_projection(pack_path: Path) -> dict[str, str]:
    """Merge the pack's [types] and [keywords] tables, as generate-grammar does."""
    doc = tomllib.loads(pack_path.read_text(encoding="utf-8"))
    projection: dict[str, str] = {}
    for section in ("types", "keywords"):
        table = doc.get(section, {})
        if not isinstance(table, dict):
            raise SystemExit(
                f"generate-grammar-tree: [{section}] is not a table in {pack_path}"
            )
        for key, value in table.items():
            if not isinstance(value, str) or not value:
                raise SystemExit(
                    f"generate-grammar-tree: {pack_path} [{section}].{key} is not a string"
                )
            projection[key] = value
    if not doc.get("keywords"):
        raise SystemExit(f"generate-grammar-tree: no [keywords] table in {pack_path}")
    # generate-grammar also promotes the null *type* row under the `nihil` key.
    nihil = doc.get("types", {}).get("nihil")
    if isinstance(nihil, str) and nihil:
        projection["nihil"] = nihil
    return projection


def project_rhs(rhs: str, projection: dict[str, str]) -> str:
    """Project single-quoted Latin literals to their English reader spellings."""

    def repl(match: re.Match) -> str:
        inner = match.group(1)
        return f"'{projection[inner]}'" if inner in projection else match.group(0)

    return re.sub(r"'([^']*)'", repl, rhs)


def corpus_alias_map(corpus_dir: Path) -> tuple[set[str], dict[str, str]]:
    """Return (canonical slugs, alias slug -> canonical slug)."""
    refresh = re.compile(r'url=/en-US/corpus/([^"<>]+?)\.html')
    canonical: set[str] = set()
    aliases: dict[str, str] = {}
    for page in sorted(corpus_dir.glob("*.html")):
        stem = page.stem
        head = page.read_text(encoding="utf-8", errors="ignore")[:600]
        if 'http-equiv="refresh"' in head:
            match = refresh.search(head)
            if match and match.group(1) != stem:
                aliases[stem] = match.group(1)
            continue
        canonical.add(stem)
    return canonical, aliases


SAFE_SLUG = re.compile(r"^[A-Za-z0-9_.+-]+$")


def resolve_term(
    latin: str,
    projection: dict[str, str],
    canonical: set[str],
    aliases: dict[str, str],
) -> tuple[str, str] | None:
    """Return (english spelling, canonical slug) when the term page exists."""
    english = projection.get(latin)
    if english is None:
        return None
    slug = aliases.get(english, english)
    if slug in canonical and SAFE_SLUG.match(slug):
        return english, slug
    return None


def check_partition(productions: list[tuple[int, str, str]]) -> None:
    """Assign every production to exactly one family; abort on drift.

    Mutates FAMILIES in place so `lexical` carries the uppercase terminals.
    """
    families = {fam["slug"]: list(fam["ids"]) for fam in FAMILIES}
    families["lexical"] = [pid for _, pid, _ in productions if pid.isupper()]

    seen: dict[str, str] = {}
    for slug, ids in families.items():
        for pid in ids:
            if pid in seen:
                raise SystemExit(
                    f"generate-grammar-tree: {pid} assigned to both "
                    f"{seen[pid]} and {slug}"
                )
            seen[pid] = slug

    all_ids = {pid for _, pid, _ in productions}
    unassigned = sorted(all_ids - set(seen))
    stale = sorted(set(seen) - all_ids)
    if unassigned:
        raise SystemExit(
            "generate-grammar-tree: EBNF productions missing from the family "
            "map: " + ", ".join(unassigned)
        )
    if stale:
        raise SystemExit(
            "generate-grammar-tree: family map names productions not in the "
            "EBNF: " + ", ".join(stale)
        )

    for fam in FAMILIES:
        fam["ids"] = families[fam["slug"]]


def render_family(
    family: dict,
    order: int,
    by_id: dict[str, tuple[int, str]],
    keywords: dict[str, list[str]],
    projection: dict[str, str],
    canonical: set[str],
    aliases: dict[str, str],
) -> tuple[str, int]:
    selected = sorted(
        (by_id[pid] for pid in family["ids"]), key=lambda item: item[0]
    )
    fence_lines: list[str] = []
    term_rows: list[str] = []
    for number, pid, rhs in selected:
        fence_lines.append(f"# [{number:03d}] {pid}")
        fence_lines.append(f"{pid} ::= {project_rhs(rhs, projection)}".rstrip())

        terms: list[str] = []
        for latin in keywords.get(pid, []):
            resolved = resolve_term(latin, projection, canonical, aliases)
            if resolved is None:
                continue
            english, slug = resolved
            terms.append(f"[`{english}`](/en-US/corpus/{slug}.html)")
        if terms:
            term_rows.append(f"| `{pid}` | {', '.join(terms)} |")

    page = FAMILY_TEMPLATE.format(
        title=family["title"],
        slug=family["slug"],
        order=order,
        blurb=family["blurb"],
        productions="\n".join(fence_lines),
    )
    if term_rows:
        page += TERMS_SECTION.format(rows="\n".join(term_rows))
    return page, len(selected)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    roots = workspace_roots()

    ebnf_path = pick(args.ebnf, roots, "faber/docs/EBNF.md")
    jsonl_path = pick(args.jsonl, roots, "faber/docs/grammar/grammar.jsonl")
    pack_path = pick(args.pack, roots, "radix/locale/en/pack.toml")

    missing = [
        name
        for name, path in (
            ("faber/docs/EBNF.md", ebnf_path),
            ("faber/docs/grammar/grammar.jsonl", jsonl_path),
            ("radix/locale/en/pack.toml", pack_path),
        )
        if path is None
    ]
    if missing:
        print(
            "  grammar tree skipped (no sibling input: "
            + ", ".join(missing)
            + "); committed output left alone",
            file=sys.stderr,
        )
        return 0

    productions = load_ebnf_productions(ebnf_path)
    keywords = load_jsonl(jsonl_path)
    projection = load_english_projection(pack_path)
    check_partition(productions)
    by_id = {pid: (number, pid, rhs) for number, pid, rhs in productions}

    corpus_dir = (
        Path(args.corpus).expanduser().resolve()
        if args.corpus
        else REPO / "dist/en-US/corpus"
    )
    if corpus_dir.is_dir():
        canonical, aliases = corpus_alias_map(corpus_dir)
    else:
        # The corpus render owns dist/en-US/corpus; when dist is wiped the
        # slug source is gone. Leaving the committed output alone beats
        # emitting family pages without their term links.
        print(
            "  grammar tree skipped (no corpus dir at "
            f"{corpus_dir}; term verification needs the previous render); "
            "committed output left alone",
            file=sys.stderr,
        )
        return 0

    family_dir = REPO / args.family_dir
    index_path = REPO / args.index

    rendered: list[tuple[dict, str, int]] = []
    for offset, family in enumerate(FAMILIES):
        page, count = render_family(
            family,
            order=offset + 2,
            by_id=by_id,
            keywords=keywords,
            projection=projection,
            canonical=canonical,
            aliases=aliases,
        )
        rendered.append((family, page, count))

    rows = [
        f"| [{family['title']}](/en-US/reference/grammar/{family['slug']}.html) "
        f"| {count} | {family['blurb']} |"
        for family, _, count in rendered
    ]
    total = sum(count for _, _, count in rendered)
    index = INDEX_TEMPLATE.format(rows="\n".join(rows), total=total)

    family_dir.mkdir(parents=True, exist_ok=True)
    # The directory holds only generated family pages; clear strays so a
    # renamed or retired family does not leave an orphan.
    for existing in family_dir.glob("*.md"):
        existing.unlink()
    for family, page, _ in rendered:
        (family_dir / f"{family['slug']}.md").write_text(page, encoding="utf-8")
    index_path.write_text(index, encoding="utf-8")

    print(
        f"grammar tree: {len(FAMILIES)} families, {total} productions → {family_dir}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
