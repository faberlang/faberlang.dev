"""Tests for the build driver's moving parts: manifest, receipt, converter,
corpus record projection and the radix pin."""
from __future__ import annotations

import os
import stat
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import build  # noqa: E402
import bump_release  # noqa: E402
import corpus_build  # noqa: E402
import receipt  # noqa: E402
import upstream  # noqa: E402
from localize import Converter  # noqa: E402


def fake_faber(directory: Path, *, fail_marker: str = "BROKEN") -> Path:
    """A `faber` stand-in: `--version`, and `convert` that logs each call.

    It exits 1 when the source contains `fail_marker`, else prints the source
    behind the frontmatter stamp the real converter writes."""
    log = directory / "calls.log"
    script = directory / "faber"
    script.write_text(textwrap.dedent(f"""\
        #!{sys.executable}
        import sys, pathlib
        args = sys.argv[1:]
        if args == ["--version"]:
            print("faber 9.9.9")
            raise SystemExit(0)
        if args[0] == "convert":
            path = pathlib.Path(args[-1])
            text = path.read_text()
            with open({str(log)!r}, "a") as handle:
                handle.write(f"{{args[args.index('--from') + 1]}}\\n")
            if {fail_marker!r} in text:
                sys.stderr.write("error[SEM001]: nope\\nsecond line\\n")
                raise SystemExit(1)
            sys.stdout.write("+++\\nlocale = \\"en\\"\\n+++\\n" + text.upper())
            raise SystemExit(0)
        raise SystemExit(2)
    """))
    script.chmod(script.stat().st_mode | stat.S_IEXEC)
    return script


def calls(directory: Path) -> list[str]:
    log = directory / "calls.log"
    return log.read_text().split() if log.is_file() else []


class ReceiptTests(unittest.TestCase):
    def test_emit_and_parse_round_trip(self):
        line = f"{receipt.PREFIX}transcode language/errors.md: error[SEM001]: nope"
        self.assertEqual(
            receipt.parse_line(line),
            {"kind": "transcode", "subject": "language/errors.md", "detail": "error[SEM001]: nope"},
        )
        self.assertIsNone(receipt.parse_line("WARNING: something"))

    def test_allowlist_matches_kind_and_glob_and_reports_unused(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "allow.toml"
            path.write_text(textwrap.dedent("""\
                [[allow]]
                kind = "transcode"
                subject = "language/*.md"
                why = "fragments"

                [[allow]]
                kind = "corpus-convert"
                subject = "radix/corpus/gone.fab"
                why = "no longer happens"
            """))
            allow = receipt.Allowlist(path)
            self.assertTrue(allow.covers({"kind": "transcode", "subject": "language/types.md"}))
            self.assertFalse(allow.covers({"kind": "transcode", "subject": "cheatsheet/types.md"}))
            self.assertFalse(allow.covers({"kind": "other", "subject": "language/types.md"}))
            self.assertEqual([e["subject"] for e in allow.unused()], ["radix/corpus/gone.fab"])

    def test_allowlist_entry_without_a_reason_is_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "allow.toml"
            path.write_text('[[allow]]\nkind = "transcode"\nsubject = "x"\nwhy = " "\n')
            with self.assertRaises(ValueError):
                receipt.Allowlist(path)

    def test_checked_in_allowlist_is_well_formed(self):
        receipt.Allowlist(build.ALLOWLIST_PATH)


class ManifestTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.manifest = build.Manifest(self.root / "manifest.json")

    def tearDown(self):
        self.tmp.cleanup()

    def test_current_until_an_input_or_the_output_changes(self):
        source = self.root / "page.md"
        output = self.root / "page.html"
        source.write_text("one")
        output.write_text("<p>one</p>")
        self.assertFalse(self.manifest.current("page", [source], [output]))
        self.manifest.record("page", [source], [output])
        self.manifest.save()
        self.assertTrue(self.manifest.current("page", [source], [output], check_output_hash=True))

        fresh = build.Manifest(self.root / "manifest.json")
        source.write_text("two")
        self.assertFalse(fresh.current("page", [source], [output]))

        source.write_text("one")
        fresh = build.Manifest(self.root / "manifest.json")
        output.write_text("<p>edited by hand</p>")
        self.assertFalse(fresh.current("page", [source], [output], check_output_hash=True))
        self.assertTrue(fresh.current("page", [source], [output], check_output_hash=False))

    def test_virtual_inputs_and_missing_outputs(self):
        output = self.root / "out.txt"
        self.manifest.record("step", [("radix:locale", "aaa")], [output])
        output.write_text("x")
        self.assertTrue(self.manifest.current("step", [("radix:locale", "aaa")], [output]))
        self.assertFalse(self.manifest.current("step", [("radix:locale", "bbb")], [output]))
        output.unlink()
        self.assertFalse(self.manifest.current("step", [("radix:locale", "aaa")], [output]))

    def test_degradations_travel_with_the_entry(self):
        output = self.root / "p.html"
        output.write_text("x")
        event = {"kind": "transcode", "subject": "p.md", "detail": "d"}
        self.manifest.record("p", [], [output], [event])
        self.manifest.save()
        reloaded = build.Manifest(self.root / "manifest.json")
        self.assertEqual(reloaded.degradations(), [{**event, "output": "p"}])


class ConverterTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)
        self.faber = fake_faber(self.dir)
        receipt.drain()

    def tearDown(self):
        self.tmp.cleanup()
        receipt.drain()

    def converter(self):
        return Converter(str(self.faber), "en", "tree1", self.dir / "cache")

    def test_success_is_cached_and_strips_the_frontmatter_stamp(self):
        converter = self.converter()
        self.assertEqual(converter.convert("abc", "la", "p.md", "transcode"), "ABC")
        self.assertEqual(converter.convert("abc", "la", "p.md", "transcode"), "ABC")
        self.assertEqual(calls(self.dir), ["la"])

    def test_failure_is_cached_and_reported_every_time(self):
        converter = self.converter()
        self.assertIsNone(converter.convert("BROKEN", "la", "p.md", "transcode"))
        self.assertIsNone(converter.convert("BROKEN", "la", "p.md", "transcode"))
        self.assertEqual(calls(self.dir), ["la"])
        events = receipt.drain()
        self.assertEqual([e["subject"] for e in events], ["p.md", "p.md"])
        self.assertEqual(events[0]["kind"], "transcode")
        self.assertEqual(events[0]["detail"], "error[SEM001]: nope")

    def test_cache_key_covers_the_compiler_build_not_only_its_version(self):
        self.converter().convert("abc", "la", "p.md", "transcode")
        # Same `--version` string, different bytes: a different build.
        script = self.faber
        script.write_text(script.read_text() + "\n# rebuilt\n")
        self.converter().convert("abc", "la", "p.md", "transcode")
        self.assertEqual(calls(self.dir), ["la", "la"])

    def test_cache_key_covers_locale_pack_and_compiler(self):
        self.converter().convert("abc", "la", "p.md", "transcode")
        Converter(str(self.faber), "en", "tree2", self.dir / "cache").convert("abc", "la", "p.md", "transcode")
        self.converter().convert("abc", "en", "p.md", "transcode")
        self.assertEqual(calls(self.dir), ["la", "la", "en"])


class CorpusRecordTests(unittest.TestCase):
    RECORD = '+++\nterm = "x"\nkind = "{kind}"\nlocale = "{locale}"\n+++\nbody\n'

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)
        self.converter = Converter(str(fake_faber(self.dir)), "en", "t", self.dir / "cache")
        receipt.drain()

    def tearDown(self):
        self.tmp.cleanup()
        receipt.drain()

    def project(self, kind, locale):
        record = self.RECORD.format(kind=kind, locale=locale)
        return corpus_build.project_record(record, {}, "en", self.converter, "r.fab")

    def test_record_in_the_reader_locale_is_not_converted(self):
        self.project("keyword", "en")
        self.assertEqual(calls(self.dir), [])

    def test_latin_record_is_converted_from_its_own_locale(self):
        self.assertIn("BODY", self.project("keyword", "la"))
        self.assertEqual(calls(self.dir), ["la"])

    def test_rejection_exemplar_is_never_sent_to_the_compiler(self):
        self.project("reject", "la")
        self.assertEqual(calls(self.dir), [])
        self.assertEqual(receipt.drain(), [])


class ReleaseFactTests(unittest.TestCase):
    def copy_surface(self, tmp: Path) -> Path:
        for rel in (bump_release.LOBBY, bump_release.SKILL, bump_release.CATALOG):
            target = tmp / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text((bump_release.REPO / rel).read_text(encoding="utf-8"), encoding="utf-8")
        return tmp

    def test_checked_in_release_facts_agree(self):
        self.assertEqual(bump_release.consistent(), [])

    def test_bump_moves_every_fact_and_leaves_them_consistent(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.copy_surface(Path(tmp))
            old = bump_release.current(root)["lobby"]
            changed = bump_release.bump(root, "9.8.7", "2030-01-02", "0.99.0")
            self.assertEqual(len(changed), 3)
            self.assertEqual(bump_release.consistent(root), [])
            skill = (root / bump_release.SKILL).read_text(encoding="utf-8")
            self.assertNotIn(old, skill)
            self.assertIn("faber-v9.8.7-aarch64-apple-darwin.tar.gz.sha256", skill)
            self.assertIn("- **Published:** 2030-01-02", skill)
            self.assertIn("- **Bundled compiler:** Radix 0.99.0", skill)
            self.assertIn('"version": "9.8.7"', (root / bump_release.CATALOG).read_text(encoding="utf-8"))

    def test_bump_refuses_when_the_files_already_disagree(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.copy_surface(Path(tmp))
            lobby = root / bump_release.LOBBY
            lobby.write_text(lobby.read_text(encoding="utf-8").replace("Faber 1.", "Faber 7."), encoding="utf-8")
            with self.assertRaises(ValueError):
                bump_release.bump(root, "9.8.7", "2030-01-02", "0.99.0")


class PinTests(unittest.TestCase):
    def git(self, *args, cwd):
        env = dict(os.environ, GIT_AUTHOR_NAME="a", GIT_AUTHOR_EMAIL="a@x",
                   GIT_COMMITTER_NAME="a", GIT_COMMITTER_EMAIL="a@x")
        return subprocess.run(["git", *args], cwd=cwd, env=env, check=True,
                              capture_output=True, text=True).stdout.strip()

    def test_tree_ids_survive_a_history_rewrite_and_materialize_from_them(self):
        with tempfile.TemporaryDirectory() as tmp:
            radix = Path(tmp) / "radix"
            for name in upstream.PINNED_TREES:
                (radix / name).mkdir(parents=True)
                (radix / name / "f.txt").write_text(f"{name}\n")
            self.git("init", "-q", cwd=radix)
            self.git("add", ".", cwd=radix)
            self.git("commit", "-q", "-m", "one", cwd=radix)

            original = Path(tmp)
            saved_checkout = upstream.radix_checkout
            saved_target = upstream.TARGET
            upstream.radix_checkout = lambda: radix
            upstream.TARGET = original / "target"
            try:
                commit_a, trees_a = upstream.resolve_rev("HEAD")
                self.git("commit", "-q", "--amend", "--author=b <b@x>", "-m", "one", cwd=radix)
                commit_b, trees_b = upstream.resolve_rev("HEAD")
                self.assertNotEqual(commit_a, commit_b)
                self.assertEqual(trees_a, trees_b)

                lock = original / "lock.toml"
                saved_lock = upstream.LOCK
                upstream.LOCK = lock
                try:
                    upstream.write_lock(commit_b, trees_b, "faber 1")
                    root = upstream.materialize()
                    self.assertEqual((root / "locale" / "f.txt").read_text(), "locale\n")
                    # A second call finds the stamp and extracts nothing new.
                    marker = root / "locale" / "marker"
                    marker.write_text("kept")
                    upstream.materialize()
                    self.assertTrue(marker.is_file())
                finally:
                    upstream.LOCK = saved_lock
            finally:
                upstream.radix_checkout = saved_checkout
                upstream.TARGET = saved_target


if __name__ == "__main__":
    unittest.main()
