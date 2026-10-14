"""Reader-locale materialization of Markdown and corpus source, in-process.

`faber convert --to <reader>` is the only thing that renders source into a
reader locale (`radix emit -t faber` is canonical re-emission and declares the
input's locale, not the output's). `Converter` runs it with a content-addressed
cache: the key is the compiler binary (version and content hash), the reader
pack tree, the source locale and the source text, so an unchanged fence is
never converted twice and a failure is remembered and reported, not retried
silently.

`Localizer` is the page-level pass that used to be `localize-markdown.py`
followed by `project-reader-terms.py`: convert fluid and eligible fences, then
project the remaining prose and inline spans onto the reader pack.
"""
from __future__ import annotations

import hashlib
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

import receipt
from project_reader_terms import load_mapping, project_markdown

FENCE = "```"
FRONTMATTER_STAMP = re.compile(r"\A\+\+\+\n.*?\n\+\+\+\n", re.S)
CONVERT_TIMEOUT = 90


def faber_version(faber: str) -> str:
    result = subprocess.run([faber, "--version"], capture_output=True, text=True, timeout=120)
    if result.returncode != 0:
        raise RuntimeError(f"{faber} --version failed: {result.stderr.strip()}")
    return result.stdout.strip()


def binary_digest(faber: str) -> str:
    """Content hash of the compiler binary.

    `--version` is not an identity: two builds of one release candidate print
    the same string and convert differently, so a cache keyed on it alone
    would serve one build's output as the other's."""
    resolved = shutil.which(faber) or faber
    digest = hashlib.sha256()
    with open(resolved, "rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()[:16]


class Converter:
    """`faber convert --from <locale> --to <reader> --stdout`, cached by content."""

    def __init__(self, faber: str, reader: str, pack_id: str, cache_dir: Path):
        self.faber = faber
        self.reader = reader
        self.cache_dir = cache_dir
        self.stamp = f"{faber_version(faber)}|{binary_digest(faber)}|{reader}|{pack_id}"
        cache_dir.mkdir(parents=True, exist_ok=True)

    def _key(self, source_locale: str, body: str) -> str:
        digest = hashlib.sha256(f"{self.stamp}|{source_locale}|{body}".encode("utf-8"))
        return digest.hexdigest()

    def convert(self, body: str, source_locale: str, label: str, kind: str) -> str | None:
        """Converted source with the frontmatter stamp removed, or None on failure.

        A failure is a degradation (`kind`, `label`) every time it is observed,
        including when it comes back out of the cache.
        """
        key = self._key(source_locale, body)
        ok_path = self.cache_dir / f"{key}.out"
        fail_path = self.cache_dir / f"{key}.fail"
        if ok_path.is_file():
            return ok_path.read_text(encoding="utf-8")
        if fail_path.is_file():
            receipt.degraded(kind, label, fail_path.read_text(encoding="utf-8"))
            return None
        try:
            with tempfile.TemporaryDirectory(prefix="speculum-convert-") as tmp:
                path = Path(tmp) / "fence.fab"
                path.write_text(body, encoding="utf-8")
                proc = subprocess.run(
                    [self.faber, "convert", "--from", source_locale, "--to", self.reader,
                     "--stdout", str(path)],
                    text=True, capture_output=True, timeout=CONVERT_TIMEOUT,
                )
        except subprocess.TimeoutExpired:
            receipt.degraded(kind, label, f"convert timed out after {CONVERT_TIMEOUT}s")
            return None
        if proc.returncode != 0:
            detail = proc.stderr.strip() or f"exit {proc.returncode}"
            fail_path.write_text(detail, encoding="utf-8")
            receipt.degraded(kind, label, detail)
            return None
        converted = FRONTMATTER_STAMP.sub("", proc.stdout, count=1)
        ok_path.write_text(converted, encoding="utf-8")
        return converted


def is_fluid_faber(info: str) -> bool:
    tokens = info.split()
    if not tokens or tokens[0] != "faber":
        return False
    for token in tokens[1:]:
        if token.startswith("locale=") or token == "mode=pinned" or token == "outcome=rejects":
            return False
        if token == "mode=package":
            # One file of a multi-file package: `faber convert` cannot resolve
            # its siblings and would reformat what it does not understand.
            return False
    return True


class Localizer:
    def __init__(self, converter: Converter, pack_path: Path):
        self.converter = converter
        self.reader = converter.reader
        if self.reader != "la" and not pack_path.is_file():
            raise FileNotFoundError(f"reader pack not found: {pack_path}")
        self.mapping = load_mapping(pack_path) if self.reader != "la" else {}

    def _fence_text(self, body_text: str, info: str, label: str) -> str | None:
        converted = self.converter.convert(body_text, "la", label, "transcode")
        return None if converted is None else converted.rstrip("\n")

    def localize_page(self, text: str, rel: str) -> str:
        """Convert transcodable fences, then project terms onto the reader pack."""
        if self.reader == "la":
            return text
        out: list[str] = []
        lines = text.splitlines()
        i = 0
        while i < len(lines):
            line = lines[i]
            stripped = line.strip()
            if not stripped.startswith(FENCE):
                out.append(line)
                i += 1
                continue
            info = stripped[3:].strip()
            body: list[str] = []
            out.append(line)
            i += 1
            while i < len(lines) and lines[i].strip() != FENCE:
                body.append(lines[i])
                i += 1
            body_text = "\n".join(body)
            tokens = info.split()
            pinned = "mode=pinned" in tokens
            eligible_text = tokens and tokens[0] == "text" and (
                "←" in body_text
                or any(
                    re.match(rf"^\s*{re.escape(key)}(?:\b|(?=[<{{(]))", body_text, re.M)
                    for key in self.mapping
                )
            )
            if is_fluid_faber(info) or pinned or bool(eligible_text):
                converted = self._fence_text(body_text, info, rel)
                if converted is not None:
                    body_text = converted
                    if pinned:
                        info = " ".join(token for token in tokens if token != "mode=pinned")
                        out[-1] = line[:line.find(stripped)] + "```" + info
            if body_text:
                out.extend(body_text.splitlines())
            if i < len(lines):
                out.append(lines[i])
            i += 1
        localized = "\n".join(out) + ("\n" if text.endswith("\n") else "")
        # The projection skips the generated grammar pages by path suffix, so it
        # needs a rooted path the way the tree walk used to supply one.
        return project_markdown(localized, self.mapping, relative_path="/" + rel, reader=self.reader)
