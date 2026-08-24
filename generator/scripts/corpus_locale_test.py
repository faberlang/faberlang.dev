#!/usr/bin/env python3
"""Unit tests for corpus_locale — no site generator required."""

from __future__ import annotations

import unittest
from pathlib import Path

from corpus_locale import assign_slugs, default_reader_root, display_slug, load_pack


class PackSlugTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        root = default_reader_root()
        cls.pack = load_pack(root, "en")
        if not cls.pack["keywords"]:
            raise unittest.SkipTest(f"no English pack at {root / 'en' / 'pack.toml'}")

    def test_keyword_pack_spelling(self) -> None:
        self.assertEqual(display_slug("functio", "keyword", self.pack), "fn")
        self.assertEqual(display_slug("incipit", "keyword", self.pack), "main")
        self.assertEqual(display_slug("si", "keyword", self.pack), "if")
        self.assertEqual(display_slug("redde", "keyword", self.pack), "return")

    def test_nihil_keyword_is_null_not_null_ty(self) -> None:
        self.assertEqual(display_slug("nihil", "keyword", self.pack), "null")
        self.assertEqual(display_slug("nihil", "type", self.pack), "null_ty")

    def test_type_fallback_when_not_in_keywords(self) -> None:
        self.assertEqual(display_slug("lista", "keyword", self.pack), "list")
        self.assertEqual(display_slug("textus", "keyword", self.pack), "string")

    def test_unmapped_and_identity_stay_put(self) -> None:
        self.assertEqual(display_slug("←", "operator", self.pack), "←")
        self.assertEqual(display_slug("cli", "keyword", self.pack), "cli")
        self.assertEqual(display_slug("tensor", "type", self.pack), "tensor")

    def test_real_pack_assigns_expected_english_slugs(self) -> None:
        slugs, collisions = assign_slugs(
            [
                ("functio", "keyword"),
                ("si", "keyword"),
                ("incipit", "keyword"),
                ("nihil", "keyword"),
                ("lista", "keyword"),
            ],
            self.pack,
        )
        self.assertEqual(slugs["functio"], "fn")
        self.assertEqual(slugs["si"], "if")
        self.assertEqual(slugs["incipit"], "main")
        self.assertEqual(slugs["nihil"], "null")
        self.assertEqual(slugs["lista"], "list")
        self.assertEqual(collisions, [])

    def test_assign_slugs_keeps_first_owner_on_collision(self) -> None:
        fake = {
            "keywords": {"alpha": "same", "beta": "same"},
            "types": {},
        }
        slugs, collisions = assign_slugs(
            [("alpha", "keyword"), ("beta", "keyword")],
            fake,
        )
        self.assertEqual(slugs["alpha"], "same")
        self.assertEqual(slugs["beta"], "beta")
        self.assertEqual(collisions, [("beta", "same", "alpha")])


if __name__ == "__main__":
    unittest.main(verbosity=2)
