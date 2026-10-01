from __future__ import annotations

import unittest
from pathlib import Path

from project_reader_terms import load_mapping, project_markdown


PACK = Path(__file__).resolve().parents[3] / "radix" / "locale" / "en" / "pack.toml"


class ReaderTermProjectionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.mapping = load_mapping(PACK)

    def project(self, text: str, path: str = "page.md") -> str:
        return project_markdown(text, self.mapping, relative_path=path, reader="en")

    def test_prose_and_heading(self) -> None:
        result = self.project("# Values — itera ex\n\nin the signature; nulla\n")
        self.assertIn("# Values — for from", result)
        self.assertIn("in the signature", result)
        self.assertIn("null", result)

    def test_inline_code_and_protected_tokens(self) -> None:
        result = self.project('`in` `norma:textus` `#fixum-decl` `itera_stmt` `non-null` `T ∪ nihil`\n')
        self.assertIn("`mut`", result)
        self.assertIn("`norma:textus`", result)
        self.assertIn("`#fixum-decl`", result)
        self.assertIn("`itera_stmt`", result)
        self.assertIn("`non-null`", result)
        self.assertIn("`T ∪ none`", result)

    def test_code_strings_and_comments(self) -> None:
        result = self.project('```faber\n# itera — Starts\nfixum textus x ← "fixum"\n```\n')
        self.assertIn("# for — Starts", result)
        self.assertIn('const string x ← "fixum"', result)

    def test_other_locale_fence_is_unchanged(self) -> None:
        source = "```faber locale=la\nfixum numerus x\n```\n"
        self.assertEqual(self.project(source), source)

    def test_urls_and_explicit_heading_ids_are_unchanged(self) -> None:
        result = self.project("[itera](/corpus/itera.html) {#fixum-decl}\n")
        self.assertIn("[for](/corpus/itera.html)", result)
        self.assertIn("{#fixum-decl}", result)

    def test_comment_does_not_swallow_the_next_line(self) -> None:
        result = self.project('```faber\n# see radix/corpus/itera/foo.fab\nfixum textus x ← "fixum"\n```\n')
        self.assertIn("radix/corpus/itera/foo.fab", result)
        self.assertIn('const string x ← "fixum"', result)

    def test_prose_keeps_hyphenated_compounds(self) -> None:
        result = self.project("A non-null value.\n")
        self.assertEqual(result, "A non-null value.\n")

    def test_paths_compounds_and_code_keywords(self) -> None:
        result = self.project(
            "See device-summa and solum_in.\n"
            "`in the signature` `in numerus` `solum:lege` `solum.carpe`\n"
            '<a id="ab"></a>`ab`\n'
            "```faber\n"
            "functio duplica(in numerus value) → vacuum {\n"
            '    si linea non est nihil { nota "non est" }\n'
            "}\n"
            "# the value in the list\n"
            "```\n"
        )
        self.assertIn("device-summa", result)
        self.assertNotIn("device-sum\n", result)
        self.assertIn("only_in", result)
        self.assertIn("`in the signature`", result)
        self.assertIn("`mut int`", result)
        self.assertIn("`solum:lege`", result)
        self.assertIn("`solum.carpe`", result)
        self.assertIn('<a id="ab"></a>', result)
        self.assertNotIn('id="range"', result)
        self.assertIn("`range`", result)
        self.assertIn("fn duplica(mut int value)", result)
        self.assertIn("if linea is not none", result)
        self.assertIn('"non est"', result)
        self.assertIn("# the value in the list", result)

    def test_comment_names_short_keywords_in_backticks(self) -> None:
        result = self.project("```faber\n# using `per` and the value in the list\n```\n")
        self.assertIn("`step`", result)
        self.assertIn("in the list", result)

    def test_grammar_is_unchanged(self) -> None:
        source = "# itera ex\n`nihil`\n"
        self.assertEqual(self.project(source, "reference/grammar.md"), source)


if __name__ == "__main__":
    unittest.main()
