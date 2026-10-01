#!/usr/bin/env python3
"""Unit tests for agent_reference — no site generator required."""

from __future__ import annotations

import shutil
import subprocess
import unittest
from pathlib import Path

from agent_reference import (
    assign_slugs,
    bullets,
    choose_example,
    fence,
    parse_list,
    parse_prose,
    render_index,
    render_page,
    render_stub,
    slug_for,
    split_body,
)

MAN_PAGE = """\
=============================================================================
cape — Starts a catch block.
=============================================================================
What this teaches:
• Error recovery — `fac { … } cape err { … }` attempts a block and catches
errors with a named handler
• Guarded execution — code inside the `fac` block can `iace` errors
Common mistakes:
• attaching `cape` to a bare `{ }` block
See also: fac, iace, ⇥
=============================================================================
cape — catch handler on fac
GRAMMAR:
facStmt :← 'fac' block 'cape' ident block
EXPECTED OUTPUT:
Scalar stdout smoke (see body).

```fab
main {
    do {
        print "hi"
    }
    catch err {
        print "caught"
    }
}
```
"""

RAW_CORPUS = """\
```fab
test "assertions hold" {
    assert x ≻ 0
}

# =============================================================================
# adfirma — Asserts that a condition is true at runtime.
# =============================================================================
#
# What this teaches:
#   • Runtime assertions — `adfirma <condition>` validates invariants during
#     program execution
#
# Common mistakes:
#   • using `adfirma` outside `proba`
#
# See also: proba, fac
```
"""

LIST = """\
reference: /somewhere/corpus


KEYWORDS
  ab                iteration       Selects numeric range iteration in an itera loop.
  non est           logic           Bitwise or and est-negation operators.

OPERATORS
  ⊜                 assignment      Assigns a value to a binding, field, or assignable expression.
"""

PACK = {
    "keywords": {"functio": "fn", "ab": "range", "genus": "class"},
    "types": {"nihil": "none"},
    "intrinsics": {"accīpe": "get", "unio": "union", "union": "union"},
}


class ParseListTests(unittest.TestCase):
    def test_sections_and_entries(self) -> None:
        sections, entries = parse_list(LIST)
        self.assertEqual(sections, ["KEYWORDS", "OPERATORS"])
        self.assertEqual([entry["term"] for entry in entries], ["ab", "non est", "⊜"])
        self.assertEqual(entries[1]["category"], "logic")
        self.assertEqual(entries[1]["section"], "KEYWORDS")
        self.assertTrue(entries[2]["summary"].startswith("Assigns a value"))

    def test_reference_line_is_not_an_entry(self) -> None:
        _sections, entries = parse_list(LIST)
        self.assertNotIn("reference:", [entry["term"] for entry in entries])


class SplitBodyTests(unittest.TestCase):
    def test_man_page_keeps_its_example_and_its_prose(self) -> None:
        prose, examples = split_body(MAN_PAGE)
        self.assertEqual(len(examples), 1)
        self.assertIn("catch err", examples[0])
        self.assertTrue(any("What this teaches" in line for line in prose))

    def test_raw_corpus_prose_comes_out_of_the_fence(self) -> None:
        prose, examples = split_body(RAW_CORPUS)
        self.assertEqual(len(examples), 1)
        self.assertIn("assert x", examples[0])
        self.assertNotIn("#", examples[0])
        joined = "\n".join(prose)
        self.assertIn("What this teaches:", joined)
        self.assertIn("Runtime assertions", joined)
        self.assertNotIn("# ", joined)

    def test_a_fence_without_trailing_comments_stays_whole(self) -> None:
        prose, examples = split_body("```fab\nmain { print 1 }\n```\n")
        self.assertEqual(examples, ["main { print 1 }"])
        self.assertEqual("".join(prose).strip(), "")


class ParseProseTests(unittest.TestCase):
    def test_labels_become_blocks(self) -> None:
        prose, _examples = split_body(MAN_PAGE)
        _preamble, blocks = parse_prose(prose)
        labels = [label for label, _body in blocks]
        self.assertIn("What this teaches", labels)
        self.assertIn("Common mistakes", labels)
        self.assertIn("See also", labels)
        self.assertIn("GRAMMAR", labels)

    def test_bullets_rejoin_hard_wrapped_lines(self) -> None:
        prose, _examples = split_body(MAN_PAGE)
        _preamble, blocks = parse_prose(prose)
        taught = dict(blocks)["What this teaches"]
        items = bullets(taught)
        self.assertEqual(len(items), 2)
        self.assertIn("catches errors with a named handler", items[0])

    def test_banner_lines_never_reach_a_block(self) -> None:
        prose, _examples = split_body(MAN_PAGE)
        _preamble, blocks = parse_prose(prose)
        for _label, body in blocks:
            for line in body:
                self.assertNotRegex(line, r"^\s*=+\s*$")


class ChooseExampleTests(unittest.TestCase):
    def test_projected_form_is_kept_when_it_compiles(self) -> None:
        text, fell_back = choose_example("functio x", "fn x", lambda _code: True)
        self.assertEqual(text, "fn x")
        self.assertFalse(fell_back)

    def test_registry_text_wins_when_projection_breaks_it(self) -> None:
        # Only the original compiles, which is the keyword-as-identifier case.
        text, fell_back = choose_example("var string nomen", "var string name", lambda code: code == "var string nomen")
        self.assertEqual(text, "var string nomen")
        self.assertTrue(fell_back)

    def test_projected_form_is_kept_when_neither_compiles(self) -> None:
        # Both are fragments; projection still gives the reader English.
        text, fell_back = choose_example("functio x", "fn x", lambda _code: False)
        self.assertEqual(text, "fn x")
        self.assertFalse(fell_back)


class SlugTests(unittest.TestCase):
    def test_keyword_uses_the_reader_pack(self) -> None:
        self.assertEqual(slug_for("functio", "keyword", PACK), "fn")
        self.assertEqual(slug_for("ab", "keyword", PACK), "range")

    def test_unmapped_term_keeps_its_name(self) -> None:
        self.assertEqual(slug_for("⊜", "operator", PACK), "⊜")

    def test_intrinsic_uses_its_own_table_first(self) -> None:
        self.assertEqual(slug_for("accīpe", "method", PACK), "get")

    def test_two_canonicals_sharing_one_english_word_get_two_pages(self) -> None:
        # unio and union are distinct intrinsics whose English surface is the
        # same word. The fallback for the loser is its own name, which is that
        # same word, so it has to grow a suffix or the pages overwrite.
        entries = [{"term": "unio", "kind": "method"}, {"term": "union", "kind": "method"}]
        slugs, collisions = assign_slugs(entries, PACK)
        self.assertEqual(slugs["unio"], "union")
        self.assertEqual(slugs["union"], "union-2")
        self.assertEqual(collisions, [("union", "union", "unio")])
        self.assertEqual(len(set(slugs.values())), 2)

    def test_loser_of_a_collision_keeps_its_own_name_when_free(self) -> None:
        pack = {"keywords": {"textus": "string"}, "types": {}, "intrinsics": {}}
        entries = [{"term": "string", "kind": "literal"}, {"term": "textus", "kind": "keyword"}]
        slugs, collisions = assign_slugs(entries, pack)
        self.assertEqual(slugs["string"], "string")
        self.assertEqual(slugs["textus"], "textus")
        self.assertEqual(collisions, [("textus", "string", "string")])

    def test_every_entry_gets_a_distinct_slug(self) -> None:
        entries = [
            {"term": "functio", "kind": "keyword"},
            {"term": "genus", "kind": "keyword"},
            {"term": "nihil", "kind": "type"},
            {"term": "⊜", "kind": "operator"},
        ]
        slugs, _collisions = assign_slugs(entries, PACK)
        self.assertEqual(len(set(slugs.values())), len(entries))
        self.assertEqual(slugs["nihil"], "none")


class RenderTests(unittest.TestCase):
    def test_fence_outgrows_backticks_inside_the_body(self) -> None:
        rendered = fence("a ``` b", "fab")
        self.assertTrue(rendered.startswith("````fab"))
        self.assertTrue(rendered.endswith("````"))

    def test_page_shape_and_unprojected_term(self) -> None:
        prose, examples = split_body(MAN_PAGE)
        _preamble, blocks = parse_prose(prose)
        page = render_page(
            term="cape",
            title="catch",
            section="KEYWORDS",
            summary="Starts a catch block.",
            syntax="functio <name>",
            aliases=["catch"],
            related=["fac"],
            blocks=blocks,
            examples=examples,
            link_of={"fac": "do"},
            project=lambda text: text.replace("fac", "do"),
        )
        self.assertTrue(page.startswith("# catch\n"))
        # The identity line is written after projection.
        self.assertIn("**Term** `cape`", page)
        self.assertIn("[`do`](do.md)", page)
        self.assertIn("## Example", page)
        self.assertIn("```fab", page)
        self.assertIn("Fetch list: https://faberlang.dev/agents/index.md", page)

    def test_index_lists_every_entry_with_its_term(self) -> None:
        _sections, entries = parse_list(LIST)
        slugs, _collisions = assign_slugs(entries, PACK)
        index = render_index(sections=["KEYWORDS", "OPERATORS"], entries=entries, slugs=slugs)
        self.assertIn("- [range](range.md)", index)
        self.assertIn("- [⊜](⊜.md)", index)
        self.assertEqual(index.count(".md)"), len(entries))

    def test_stub_points_at_the_canonical_page(self) -> None:
        stub = render_stub(slug="function", target="fn", source="`faber explain functio`")
        self.assertIn("[`fn`](fn.md)", stub)
        self.assertIn("`faber explain functio`", stub)


class RealRegistryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.faber = None
        for candidate in (
            Path(__file__).resolve().parents[2].parent / "radix" / "target" / "debug" / "faber",
            shutil.which("faber"),
        ):
            if candidate and Path(candidate).is_file():
                probe = subprocess.run([str(candidate), "explain", "ab", "--json"], capture_output=True, text=True)
                if probe.returncode == 0 and probe.stdout.strip().startswith("{"):
                    cls.faber = str(candidate)
                    break
        if not cls.faber:
            raise unittest.SkipTest("no faber binary resolves its reference pack")

    def test_list_covers_every_section_and_term(self) -> None:
        result = subprocess.run([self.faber, "explain", "--list"], capture_output=True, text=True)
        sections, entries = parse_list(result.stdout)
        self.assertEqual(len(sections), 8)
        self.assertGreaterEqual(len(entries), 190)
        self.assertIn("non est", [entry["term"] for entry in entries])

    def test_a_real_body_has_an_example_and_parseable_prose(self) -> None:
        import json

        result = subprocess.run([self.faber, "explain", "ab", "--json"], capture_output=True, text=True)
        payload = json.loads(result.stdout)
        prose, examples = split_body(payload["body"])
        _preamble, blocks = parse_prose(prose)
        self.assertEqual(len(examples), 1)
        self.assertTrue(blocks)


if __name__ == "__main__":
    unittest.main(verbosity=2)
