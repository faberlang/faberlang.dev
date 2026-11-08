"""Tests for fab_sections: the site's port of the compiler's section splitter."""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import fab_sections as fs  # noqa: E402

SECTIONED = """+++ toml
term = "sections"
locale = "en"

+++ faber
main {
    print 42
}

+++ faber test
test "t" {
    assert 1 ≡ 1
}

+++ text stdout
42
"""


class SplitTest(unittest.TestCase):
    def test_sectioned_file(self) -> None:
        parts = fs.split(SECTIONED)
        self.assertEqual(parts.header, 'term = "sections"\nlocale = "en"\n')
        self.assertEqual(parts.program, "main {\n    print 42\n}\n")
        self.assertEqual(parts.test, 'test "t" {\n    assert 1 ≡ 1\n}\n')
        self.assertEqual(fs.stream_text(parts, "stdout"), "42\n")
        self.assertIsNone(fs.stream_text(parts, "stderr"))

    def test_legacy_header_is_the_same_format(self) -> None:
        parts = fs.split('+++\nterm = "ab"\n+++\nmain { }\n')
        self.assertEqual(parts.header, 'term = "ab"\n')
        self.assertEqual(parts.program, "main { }\n")
        self.assertEqual(fs.legacy_record(parts), '+++\nterm = "ab"\n+++\nmain { }\n')

    def test_legacy_header_then_sections(self) -> None:
        parts = fs.split('+++\nterm = "ab"\n+++\nmain { }\n\n+++ text stdout\nx\n')
        self.assertEqual(parts.program, "main { }\n")
        self.assertEqual(fs.stream_text(parts, "stdout"), "x\n")

    def test_markers_absent_means_all_program(self) -> None:
        parts = fs.split("main { }\n")
        self.assertIsNone(parts.header)
        self.assertEqual(parts.program, "main { }\n")

    def test_code_first_then_stream(self) -> None:
        parts = fs.split("main { }\n\n+++ text stdout\nok\n")
        self.assertEqual(parts.program, "main { }\n")
        self.assertEqual(fs.stream_text(parts, "stdout"), "ok\n")

    def test_only_one_separator_line_is_dropped(self) -> None:
        parts = fs.split("+++ faber\nmain { }\n\n\n+++ text stdout\nok\n")
        self.assertEqual(parts.program, "main { }\n\n")

    def test_test_only_file_renders_its_tests(self) -> None:
        parts = fs.split('+++ toml\nterm = "t"\n\n+++ faber test\ntest "x" {\n}\n')
        self.assertEqual(parts.program, "")
        self.assertTrue(fs.legacy_record(parts).endswith('test "x" {\n}\n'))

    def test_base64_stream_decodes(self) -> None:
        digest = "a" * 64
        parts = fs.split(f"+++ faber\nmain {{ }}\n\n+++ base64 stdout sha256:{digest}\naGk=\n")
        self.assertEqual(fs.stream_text(parts, "stdout"), "hi")

    def test_marker_lines_split_at_lf_only(self) -> None:
        parts = fs.split('+++ faber\nlet s ← "a +++ b"\n')
        self.assertEqual(parts.program, 'let s ← "a +++ b"\n')

    def test_structural_errors_are_named(self) -> None:
        cases = {
            "+++ faber\nmain { }\n+++\n": "stray_bare_marker",
            "+++ toml\nx = 1\n+++\nmain { }\n": "toml_closed_by_bare_marker",
            "main { }\n+++ toml\n": "toml_not_first_line",
            "+++ faber\nmain { }\n+++ faber\nmain { }\n": "duplicate_section",
            "+++ faber\n\n": "empty_faber_section",
            "+++ yaml stdout\n": "unknown_section_format",
            "+++ text stdlog\n": "unknown_section_name",
            "+++  faber\n": "malformed_section_marker",
            "+++\nx = 1\n": "unterminated_legacy_header",
            "+++ toml\nx = 1\n": "missing_faber_section",
            "+++ faber test\n\n+++\nx = 1\n+++\nmain { }\n": "empty_faber_test_section",
        }
        for source, issue in cases.items():
            with self.subTest(issue=issue):
                with self.assertRaises(fs.SectionError) as caught:
                    fs.split(source)
                self.assertEqual(caught.exception.issue, issue)


class PublishedCorpusTest(unittest.TestCase):
    def test_reference_subtree_from_1_19(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            corpus = Path(tmp) / "corpus"
            corpus.mkdir()
            self.assertEqual(fs.published_corpus(corpus), corpus)
            (corpus / "reference").mkdir()
            self.assertEqual(fs.published_corpus(corpus), corpus / "reference")


if __name__ == "__main__":
    unittest.main()
