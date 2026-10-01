#!/usr/bin/env python3
"""Unit tests for agent_locales — no site generator required."""

from __future__ import annotations

import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from agent_locales import (
    IDENTITY_BY_ABSENCE,
    PACK_COLUMNS,
    cell,
    incomplete,
    missing_packs,
    read_packs,
    render,
    rows,
    stale_expectations,
    union_keys,
    unexpected,
)
from corpus_locale import default_reader_root

SYNTHETIC = {
    "en": {"keywords": {"functio": "fn", "si": "if"}, "types": {"nihil": "none"}},
    "la": {"keywords": {"functio": "functio", "si": "si"}, "types": {"nihil": "nihil"}},
    "ar": {"keywords": {"functio": "دالة", "si": "إذا"}, "types": {"nihil": "لا_شيء"}},
}


def render_section(section: str, table: dict[str, str], *, raw: dict[str, str] | None = None) -> str:
    lines = [f"[{section}]"]
    for key, value in table.items():
        lines.append(f'{key} = "{value}"')
    for key, value in (raw or {}).items():
        lines.append(f"{key} = {value}")
    return "\n".join(lines) + "\n"


def write_packs(root: Path, packs: dict[str, dict[str, dict[str, str]]]) -> None:
    for locale, sections in packs.items():
        path = root / locale
        path.mkdir(parents=True, exist_ok=True)
        (path / "pack.toml").write_text(
            "\n".join(render_section(section, table).rstrip("\n") for section, table in sections.items()) + "\n",
            encoding="utf-8",
        )


def add_pack_section(root: Path, locale: str, section: str, table: dict[str, str]) -> None:
    path = root / locale / "pack.toml"
    path.write_text(path.read_text(encoding="utf-8") + render_section(section, table), encoding="utf-8")


class NormalizeTests(unittest.TestCase):
    def test_table_row_takes_the_canonical_spelling_and_keeps_aliases(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "en").mkdir()
            (root / "en" / "pack.toml").write_text(
                '[intrinsics]\napproximata = { canonical = "approx", aliases = ["approximata"] }\n',
                encoding="utf-8",
            )
            packs = read_packs(root)
            self.assertEqual(packs["en"]["intrinsics"]["approximata"], ("approx", ("approximata",)))

    def test_cell_escapes_pipes_and_backticks(self) -> None:
        self.assertEqual(cell("a|b"), "`a\\|b`")
        self.assertEqual(cell("a`b"), "`a'b`")
        self.assertEqual(cell("   "), "")


class IncompleteTests(unittest.TestCase):
    def test_agreeing_packs_report_nothing(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_packs(root, SYNTHETIC)
            packs = read_packs(root)
            self.assertEqual(incomplete(packs), [])
            self.assertEqual(render(packs).count("rows are not declared by every pack"), 0)

    def test_a_key_absent_from_one_pack_is_a_finding(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            packs = {
                locale: {section: dict(table) for section, table in tables.items()}
                for locale, tables in SYNTHETIC.items()
            }
            packs["ar"]["keywords"]["solum_ar"] = "خاص"
            write_packs(root, packs)
            self.assertEqual(
                incomplete(read_packs(root)),
                [("keywords", "solum_ar", ("en", "la"))],
            )

    def test_latin_may_omit_an_identity_by_absence_section(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_packs(root, SYNTHETIC)
            for locale in ("en", "ar"):
                add_pack_section(root, locale, "intrinsics", {"accipe": "get"})
            packs = read_packs(root)
            self.assertIn("intrinsics", IDENTITY_BY_ABSENCE)
            self.assertEqual(incomplete(packs), [])

    def test_an_uninstalled_pack_is_not_incompleteness(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_packs(root, SYNTHETIC)
            packs = read_packs(root)
            self.assertEqual(incomplete(packs), [])
            self.assertEqual(
                missing_packs(packs), ("hi", "th-TH", "vi", "zh-Hans", "zh-Hant")
            )

    def test_unexpected_and_stale_catch_both_directions(self) -> None:
        found = [("keywords", "conversion", ("en", "la")), ("keywords", "brand_new", ("vi",))]
        self.assertEqual(unexpected(found), [("keywords", "brand_new", ("vi",))])
        self.assertEqual(stale_expectations(found), [("keywords", "nihil", ("la",))])


class RenderTests(unittest.TestCase):
    def test_header_leads_with_english_then_latin(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_packs(root, SYNTHETIC)
            text = render(read_packs(root))
            self.assertIn("| English | Latin | ar | hi | th-TH | vi | zh-Hans | zh-Hant |", text)

    def test_latin_intrinsics_column_carries_the_canonical_name(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_packs(root, SYNTHETIC)
            add_pack_section(root, "en", "intrinsics", {"accipe": "get", "addita": "added"})
            packs = read_packs(root)
            for canonical, cells in rows(packs, "intrinsics"):
                self.assertEqual(cells["la"], canonical, canonical)
            self.assertIn("no `[intrinsics]` section", render(packs))

    def test_alias_row_is_called_out(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "en").mkdir()
            (root / "en" / "pack.toml").write_text(
                '[intrinsics]\napproximata = { canonical = "approx", aliases = ["approximata"] }\n',
                encoding="utf-8",
            )
            text = render(read_packs(root))
            self.assertIn("`approximata` in `intrinsics` is also written `approximata`", text)


class RealPackTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.packs = read_packs(default_reader_root())
        if not cls.packs.get("en", {}).get("keywords"):
            raise unittest.SkipTest("no English pack in the workspace checkout")

    def test_every_pack_column_is_installed(self) -> None:
        self.assertEqual(missing_packs(self.packs), ())
        for locale in PACK_COLUMNS:
            self.assertTrue(self.packs[locale]["keywords"], locale)

    def test_english_and_latin_agree_on_the_identity_rows(self) -> None:
        identity = 0
        for section in ("keywords", "types"):
            for _canonical, cells in rows(self.packs, section):
                if cells["en"] and cells["en"] == cells["la"]:
                    identity += 1
        self.assertGreater(identity, 0)

    def test_row_counts_match_the_unions(self) -> None:
        for section in ("keywords", "types", "intrinsics"):
            self.assertEqual(len(rows(self.packs, section)), len(union_keys(self.packs, section)))

    def test_english_approximata_uses_its_canonical_spelling(self) -> None:
        for canonical, cells in rows(self.packs, "intrinsics"):
            if canonical == "approximata":
                self.assertEqual(cells["en"], "approx")
                return
        self.fail("approximata not found in the English intrinsics")

    def test_drift_is_only_what_is_expected(self) -> None:
        found = incomplete(self.packs)
        self.assertEqual(unexpected(found), [])
        self.assertEqual(stale_expectations(found), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
