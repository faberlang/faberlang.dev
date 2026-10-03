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
  src/en-US/reference/grammar/<family>.md     one page per family (prose + term tables)
  static/agents/grammar/productions.md        every production, for models
  dist/agents/grammar/productions.md          (same file, when dist/ exists)

The human family pages show no EBNF. Each one opens with an overview of
that part of the language, a short explanation, and one or two checked
English examples, then lists the words you write there, linked to their
corpus term pages, beside the grammar rule each word belongs to. The full
production list is written once, for models and tools, to the agent canon
page above. Its quoted words are projected through the English reader pack;
rule names and UPPERCASE terminals stay the stable Latin identities.
Keywords that resolve to an existing canonical corpus page under
`dist/en-US/corpus/` become term links; alias stubs are followed to their
target so only canonical pages are linked.

The script degrades gracefully: when a sibling input is absent it leaves the
committed output alone and exits 0, so a checkout without the compiler tree
still builds.

Usage:
    generate-grammar-tree.py [--ebnf PATH] [--jsonl PATH] [--pack PATH]
                             [--corpus DIR] [--index PATH] [--family-dir DIR]
                             [--agent-page PATH]...

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
            "strings, width markers, and the frontmatter delimiter."
        ),
        # Filled from the jsonl `region` field at load time.
        "ids": [],
    },
]

# Reader prose for each family page. The one-line `blurb` stays on the hub
# table; this is the page body — what the category is, what the table means,
# and one or two English examples. Regeneration must keep this text, so it
# lives here rather than in the Markdown. Examples are `locale=en` and have
# been checked with `faber check --locale=en`.
FAMILY_PROSE: dict[str, str] = {
    "program": """\
A Faber source file is a program. The compiler reads it from the top: an
optional frontmatter header, an optional `module` region, then the
declarations, imports, tests, and the entry point that starts it. There is
no hidden wrapper around those declarations and no separate "program"
object to construct.

The words on this page are the ones that give the file its shape. Imports
bring a name in from another file or a library (`import from`). `main` is
the ordinary entry; `async_main` is the one that may await. Tests are
ordinary declarations in the same file — `describe` names a suite, `test`
names a case — not a second language and not a second compilation target.

A file that does one thing:

```faber locale=en
fn salve(string nomen) → string {
    const string msg ← "Salve, §!"(nomen)
    return msg
}

main {
    const string m ← salve("munde")
    print m
}
```

`faber check` accepts that file. `faber run` prints `Salve, munde!`.

Tests sit beside the code they exercise:

```faber locale=en
fn saturate(int x) → int {
    if x < 0 then return 0
    if x > 255 then return 255
    return x
}

describe "saturate" {
    test "clamps low" {
        assert saturate(-1) ≡ 0
    }
    test "clamps high" {
        assert saturate(300) ≡ 255
    }
}
```
""",
    "declarations": """\
A declaration introduces a name the rest of the file can use. Bindings hold
values: `const` is written once, `var` can be assigned again, and `let` is
the short inferred form of an immutable binding. Functions, closures, and
classes are declarations too — they name a callable or a type, and the
fields and methods it holds.

The type always comes before the name: `int count`, never `count: int`.
`←` stores a value at run time. `=` is for a field's shape inside a
literal, not for binding a local. Generic parameters (`<T>`), `implements`
bounds, and the modifiers on a function (`async`, `throws`, `args`) belong
here because they are part of how the name is declared.

A function and two bindings:

```faber locale=en
fn divide(int a, int b) → int ∪ none {
    if b ≡ 0 then return null
    return a / b
}

main {
    const int seven ← 7
    var int n ← 3
    n ← n + 1
    print divide(seven, n)
}
```

A class names its fields the same way. Methods are functions on the class;
`self` is the instance:

```faber locale=en
class Span {
    const f64 low
    const f64 high

    fn contains(f64 x) → bool {
        return self.low ≤ x and x ≤ self.high
    }
}

main {
    const Span bytes ← Span { low = 0.0, high = 255.0 }
    print bytes.contains(128.0)
}
```
""",
    "annotations": """\
An annotation is a `@` line that attaches to the declaration below it. It
does not run. It tells the compiler a fact about that declaration: that it
is exported, that it is a command-line program, that a kernel, compiler
lane, or capability applies.

The generic shape is `@` plus a name, optionally with fields in braces.
`@ public` marks a function an importer can see. `@ cli` names the binary
a package produces. The same family covers `@ kernel`, `@ radix`, and
`@ call` — specialized directives most source meets later. The table
below lists the words those directives use.

```faber locale=en
@ public
fn saluta(string nomen) → string {
    return "Salve, §!"(nomen)
}
```

A command-line entry uses the same `@` shape above `main args`:

```faber locale=en
@ cli { name = "echo" }
@ description "Prints text"
@ operand { rest = true, type = string, binding = words }
main args argv {
    for from argv.words const word {
        print word
    }
}
```
""",
    "types": """\
A type is what a value is. Faber writes the type before the name, so you
read the kind of thing first. This page is the syntax of types and the
declarations that introduce new ones: `interface` is a contract of
methods, `type` is another name for an existing type, `enum` is a closed
set of named constants, `union` is a tagged choice with variants, and
`schema` describes relational columns.

Absence is a union, not a question mark. A missing integer is
`int ∪ none`; the missing value is `null`. There is no `int?`. Widths are
bare markers — `i32`, `f32` — written in type position.

Everyday types, type first:

```faber locale=en
main {
    const string name ← "Marcus"
    const int age ← 30
    const bool flag ← true
    const list<int> nums ← [1, 2, 3]
    const int ∪ none missing ← null
    print name
    print age
    print flag
    print nums
    print missing
}
```

A `type` alias is a transparent name. It does not create a new kind of
value:

```faber locale=en
type Signum = int
type Nomina = list<string>

main {
    const Signum signum ← 42
    const Nomina sodales ← ["Gaius", "Lucius"]
    print signum
    print sodales
}
```
""",
    "statements": """\
A statement is a step the program takes. This family is how control
moves: `if` / `elif` / `else` choose a branch, `while` repeats while a
condition holds, `for` walks a collection or a range, `switch` selects an
arm by value, and `match` exhausts the variants of a union.

`then` lets a branch be a single statement instead of a block — a common
way to write an early `return`. `guard` groups those checks at the top of
a function. `return` leaves a function; `break` and `continue` leave or
skip a loop; `pass` is the explicit empty body. `assert` and `panic` are
diagnostics. `require` and `reject` are the one-line throws; they need an
error channel, which lives on the [error channel](errors.html) page.

```faber locale=en
main {
    const int score ← 85
    if score ≥ 90 {
        print "A"
    }
    elif score ≥ 80 {
        print "B"
    }
    else {
        print "C"
    }
    const list<int> nums ← [1, 2, 3]
    for from nums const item {
        print item
    }
    var int n ← 0
    while n ≺ 2 {
        n ← n + 1
    }
    print n
}
```

`switch` picks the first matching value. `default` is the fallback:

```faber locale=en
fn describe(int value) → string {
    switch value {
        case 1 { return "one" }
        case 2 { return "two" }
        default { return "many" }
    }
}

main {
    print describe(2)
}
```
""",
    "expressions": """\
An expression produces a value. This family is the operator stack:
assignment at the root, then `or` and `and`, then comparison and
arithmetic, then calls, members, and the literals — numbers, strings,
`true` / `false` / `null`, lists, tuples, and inline JSON.

`←` stores a value at run time. `and` / `or` / `not` are the boolean
words. `coalesce` is the nullish default: if the left side is `null`, the
value is the right side. A `"…"` literal with `§` holes is a template;
the parentheses after it supply the arguments, which is not a function
call.

```faber locale=en
fn greet(string nomen) → string {
    return "Salve, §!"(nomen)
}

main {
    const int a ← 7
    const int b ← 2
    print a / b
    print a ≥ b and b ≠ 0
    print greet("munde")
}
```

`coalesce` fills in a missing value:

```faber locale=en
main {
    const int ∪ none missing ← null
    const int n ← missing coalesce 0
    print n
}
```
""",
    "patterns": """\
A pattern is what a `match` arm accepts. It is not the `match` statement
itself — that lives with [statements](statements.html) — it is the shape
on the left of each `case`: a literal, a type, a binding, or a
destructured object or array.

`and` joins patterns that must all hold; `or` offers alternatives.
`const` / `var` / `as` bind a name to what matched. `rest` keeps the
leftover fields or elements. The same atoms appear when a union-typed
value is read back out by member type.

```faber locale=en
main {
    const int ∪ string signum ← 7

    match signum {
        case int const n { print "a number" }
        case string const s { print "a text" }
    }
}
```
""",
    "errors": """\
Failure is a second channel, not a wrapper type and not an exception that
unwinds past you. A function that can fail writes `⇥` after the success
type: `→ int ⇥ string` returns an int or fails with a string. `throw`
sends a value on that channel. `do` / `catch` is the local boundary
around a call that might fail; `catch` binds the error as an ordinary
value.

`throw if` is the guarded form. `require` and `reject` (listed with
[statements](statements.html)) compile to the same idea: throw when a
condition fails, or when it holds. A call to a `⇥` function sits inside
an active `do` / `catch` (or another statement that carries `catch`).

```faber locale=en
fn divide(int a, int b) → int ⇥ string {
    if b ≡ 0 {
        throw "division by zero"
    }
    return a / b
}

main {
    do {
        print divide(7, 2)
    }
    catch err {
        print err
    }
}
```
""",
    "lexical": """\
The lexer turns a file into tokens before the parser builds a tree. This
page is those tokens: identifiers, numbers, strings, the width markers
(`i32`, `f32`, …), and the frontmatter delimiter.

Identifiers are the names you write — `score`, `divide`, `Span`. Numbers
are the integer and floating literals. A `"…"` string is Unicode text.
Width markers are the bare type tokens for sized numerics. None of these
are keywords. The reserved words on the other family pages are already
known to the parser; everything else that looks like a name is an
identifier.

There is no keyword table here: these productions are the terminal
shapes, not the vocabulary of the language. A short program that is
mostly those tokens:

```faber locale=en
main {
    const i32 narrow ← 7 ∷ i32
    const f32 single ← 1.5 ∷ f32
    const string name ← "Marcus"
    print name
    print narrow
    print single
}
```
""",
}

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

Faber's grammar is written down as a list of rules, which the compiler calls
productions. Each rule says how one piece of the language is built from
smaller pieces: a loop from a keyword, a binding and a block, a block from
statements. You do not need to read the rules to write Faber. The
[cheat sheet](/cheatsheet/) and the language pages teach every form by
example; this section is for looking up which words belong to which part of
the language.

The {total} rules are grouped into the families below. Each family page
explains that part of the language, then lists the words you write there
and links each one to its [term page](/en-US/corpus/).

## Production families {{#production-families}}

| Family | What it covers |
|---|---|
{rows}

## Formal grammar {{#formal-grammar}}

The rules themselves are the parser's own definition of valid syntax. They are
written for models and tools, in the English reader spellings, and live on one
page: [every production](/agents/grammar/productions.md), with the shorter
[forms the agent pages use](/agents/grammar.md). The
[target matrix](/toolchain/target-matrix.html) is the authority on whether a
given target supports a form. Latin stays the compiler's canonical form, and
`faber explain <term>` prints a mapping from the compiler itself.
"""

FAMILY_FRONT = """\
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
"""

FAMILY_FORMAL = """\
## Formal grammar {#formal-grammar}

The rules for this part of the language are the parser's own definition of it.
They are written for models and tools, so this page does not repeat them; the
full list is at [every production](/agents/grammar/productions.md).
"""

TERMS_SECTION = """
## Terms {{#terms}}

These are the words you write in this part of the language. Each links to its
page. The second column names the grammar rule the word belongs to.

| Term | Grammar rule |
|---|---|
{rows}
"""

AGENT_PAGE_TEMPLATE = """\
# Grammar productions

Every Faber grammar rule, in EBNF, with the words in quotes shown in the
English reader spellings. Rule names and UPPERCASE lexical terminals are the
stable Latin identities. The compiler's own grammar is the authority; this page
is generated from it. Grammar examples are fragments, not standalone programs.
For the short forms the other pages use, read
https://faberlang.dev/agents/grammar.md. The human grammar overview is
https://faberlang.dev/en-US/reference/grammar.html.

```ebnf
{productions}
```

Fetch list: https://faberlang.dev/agents/index.md
"""


def check_prose() -> None:
    """Every family has reader prose; no leftover slugs."""
    slugs = {fam["slug"] for fam in FAMILIES}
    missing = sorted(slugs - set(FAMILY_PROSE))
    extra = sorted(set(FAMILY_PROSE) - slugs)
    empty = sorted(
        slug for slug, text in FAMILY_PROSE.items() if not text.strip()
    )
    problems: list[str] = []
    if missing:
        problems.append("families with no prose: " + ", ".join(missing))
    if extra:
        problems.append("prose for unknown families: " + ", ".join(extra))
    if empty:
        problems.append("empty prose: " + ", ".join(empty))
    if problems:
        raise SystemExit("generate-grammar-tree: " + "; ".join(problems))


def apply_committed_prose(family_dir: Path) -> int:
    """Rewrite the reader body of existing family pages; keep term tables.

    Used when sibling compiler inputs are absent, so a prose edit still
    lands in the committed Markdown. The full emit path rebuilds the page
    from scratch and does not call this.
    """
    marker = "Return to the [grammar overview](/en-US/reference/grammar.html)."
    updated = 0
    for fam in FAMILIES:
        path = family_dir / f"{fam['slug']}.md"
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        if not text.startswith("+++\n"):
            raise SystemExit(
                f"generate-grammar-tree: {path} does not start with frontmatter"
            )
        close = text.find("\n+++\n", 4)
        if close < 0:
            raise SystemExit(
                f"generate-grammar-tree: {path} has no closing frontmatter"
            )
        head = text[: close + 5]
        rest = text[close + 5 :]
        idx = rest.find(marker)
        if idx < 0:
            raise SystemExit(
                f"generate-grammar-tree: {path} has no grammar-overview link"
            )
        prose = FAMILY_PROSE[fam["slug"]].strip()
        path.write_text(head + "\n" + prose + "\n\n" + rest[idx:], encoding="utf-8")
        updated += 1
    return updated


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
    ap.add_argument(
        "--agent-page",
        action="append",
        default=None,
        help="agent productions page output (repeatable); defaults to "
        "static/ and dist/ agents/grammar/productions.md",
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
    term_rows: list[str] = []
    for number, pid, rhs in selected:
        terms: list[str] = []
        for latin in keywords.get(pid, []):
            resolved = resolve_term(latin, projection, canonical, aliases)
            if resolved is None:
                continue
            english, slug = resolved
            terms.append(f"[`{english}`](/en-US/corpus/{slug}.html)")
        if terms:
            term_rows.append(f"| {', '.join(terms)} | `{pid}` |")

    prose = FAMILY_PROSE.get(family["slug"])
    if not prose or not prose.strip():
        raise SystemExit(
            f"generate-grammar-tree: family {family['slug']!r} has no reader prose"
        )

    # Concatenate so Faber fences (which contain `{` / `}`) never go through
    # str.format.
    page = (
        FAMILY_FRONT.format(
            title=family["title"],
            slug=family["slug"],
            order=order,
        )
        + "\n"
        + prose.strip()
        + "\n\nReturn to the [grammar overview](/en-US/reference/grammar.html).\n"
        + (
            TERMS_SECTION.format(rows="\n".join(term_rows))
            if term_rows
            else "\n"
        )
        + FAMILY_FORMAL
    )
    return page, len(selected)


def render_agent_page(
    productions: list[tuple[int, str, str]], projection: dict[str, str]
) -> str:
    """Every production in EBNF file order, for the agent canon."""
    lines: list[str] = []
    for number, pid, rhs in sorted(productions, key=lambda item: item[0]):
        lines.append(f"# [{number:03d}] {pid}")
        lines.append(f"{pid} ::= {project_rhs(rhs, projection)}".rstrip())
    return AGENT_PAGE_TEMPLATE.format(productions="\n".join(lines))


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    check_prose()
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
        family_dir = REPO / args.family_dir
        n = apply_committed_prose(family_dir)
        print(
            "  grammar tree skipped (no sibling input: "
            + ", ".join(missing)
            + f"); applied reader prose to {n} committed family pages",
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
        f"| {family['blurb']} |"
        for family, _, count in rendered
    ]
    total = sum(count for _, _, count in rendered)
    agent_page = render_agent_page(productions, projection)
    index = INDEX_TEMPLATE.format(rows="\n".join(rows), total=total)

    family_dir.mkdir(parents=True, exist_ok=True)
    # The directory holds only generated family pages; clear strays so a
    # renamed or retired family does not leave an orphan.
    for existing in family_dir.glob("*.md"):
        existing.unlink()
    for family, page, _ in rendered:
        (family_dir / f"{family['slug']}.md").write_text(page, encoding="utf-8")
    index_path.write_text(index, encoding="utf-8")
    agent_targets = (
        [Path(p) for p in args.agent_page]
        if args.agent_page
        else [
            REPO / "static/agents/grammar/productions.md",
            REPO / "dist/agents/grammar/productions.md",
        ]
    )
    for target in agent_targets:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(agent_page, encoding="utf-8")

    print(
        f"grammar tree: {len(FAMILIES)} families, {total} productions → {family_dir}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
