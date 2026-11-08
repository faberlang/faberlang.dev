"""Read a `.fab` file's sections the way the compiler's driver does.

Since Faber 1.19 a source file may label its parts with whole-line markers:
`+++ toml` (the header, line 1 only), `+++ faber` (the program),
`+++ faber test` (tests) and `+++ <text|json|jsonl|base64> <stdin|stdout|stderr>`
stream sections. The legacy header, a bare `+++` on line 1 closed by the next
bare `+++`, is part of the same format and stays valid, so every corpus pin the
site has ever used reads through this one splitter.

This is a port of `split_frontmatter` in radix
`crates/radix-module/src/driver/frontmatter.rs` (the reader `faber corpus`,
`check` and `format` share), kept rule for rule so the site never disagrees
with the compiler about where a section starts:

- a marker is any physical line starting with `+++`; anything after `+++ `
  that is not a known marker is an error, never content;
- a section runs to the next marker or end of file, with no closers;
- exactly one empty line before a marker is a separator, not content;
- code before the first marker is the program; a file with no markers is all
  program; once a marker appears a program or test section is required;
- each section, and each stream whatever its format, appears at most once.

The one deliberate gap: `base64` payloads are not decoded or digest-checked
(the compiler's corpus gate already proves them); a `base64` stream's content
is returned as written, and `stream_text` decodes it on demand.
"""
from __future__ import annotations

import base64
import re
import tomllib
from dataclasses import dataclass, field
from pathlib import Path

DELIMITER = "+++"
BOM = "﻿"
FORMATS = ("text", "json", "jsonl", "base64")
STREAMS = ("stdin", "stdout", "stderr")
_SHA256 = re.compile(r"^sha256:[0-9a-f]{64}$")


class SectionError(ValueError):
    """A structural error the compiler reports as `PARSE052 <issue>`."""

    def __init__(self, issue: str, line: int | None = None, detail: str = "") -> None:
        self.issue = issue
        self.line = line
        where = f"line {line}: " if line else ""
        super().__init__(f"{where}{issue}{': ' + detail if detail else ''}")


@dataclass(frozen=True)
class Stream:
    format: str
    stream: str
    content: str


@dataclass
class Split:
    """One file's parts. `header` is the TOML text, `None` when there is none."""

    header: str | None
    program: str
    test: str | None = None
    streams: list[Stream] = field(default_factory=list)

    def stream(self, name: str) -> Stream | None:
        return next((s for s in self.streams if s.stream == name), None)


@dataclass(frozen=True)
class _Marker:
    kind: str  # "bare", "toml", "faber", "test" or "stream"
    start: int  # offset of the marker line's first character
    after_line: int  # offset just past the marker line and its ending
    line: int  # one-based physical line
    format: str = ""
    stream: str = ""

    def section(self) -> str:
        return {"toml": "toml", "faber": "faber", "test": "faber test"}.get(
            self.kind, f"{self.format} {self.stream}")


def _parse_marker(text: str, line: int) -> _Marker:
    if text == DELIMITER:
        return _Marker("bare", 0, 0, line)
    if not text.startswith("+++ "):
        raise SectionError("malformed_section_marker", line, text)
    words = text[4:].split(" ")
    if any(not word or "\t" in word for word in words):
        raise SectionError("malformed_section_marker", line, text)
    if words == ["toml"]:
        return _Marker("toml", 0, 0, line)
    if words == ["faber"]:
        return _Marker("faber", 0, 0, line)
    if words == ["faber", "test"]:
        return _Marker("test", 0, 0, line)
    if words[0] in ("toml", "faber"):
        raise SectionError("unknown_section_name", line, " ".join(words))
    fmt, rest = words[0], words[1:]
    if fmt not in FORMATS:
        raise SectionError("unknown_section_format", line, fmt)
    if not rest:
        raise SectionError("unknown_section_name", line, fmt)
    if fmt == "base64" and len(rest) == 2:
        if not _SHA256.match(rest[1]):
            raise SectionError("malformed_section_marker", line, text)
        name = rest[0]
    elif len(rest) == 1:
        name = rest[0]
    else:
        raise SectionError("malformed_section_marker", line, text)
    if name not in STREAMS:
        raise SectionError("unknown_section_name", line, f"{fmt} {name}")
    return _Marker("stream", 0, 0, line, fmt, name)


def _scan(source: str) -> list[_Marker]:
    markers, start = [], 0
    # Physical lines end at LF only, as in `split_inclusive('\n')`; str.splitlines
    # would also split at U+2028, form feed and friends inside string literals.
    lines = [line + "\n" for line in source.split("\n")]
    lines[-1] = lines[-1][:-1]
    for index, raw in enumerate(line for line in lines if line):
        after = start + len(raw)
        text = raw[:-1] if raw.endswith("\n") else raw
        text = text[:-1] if text.endswith("\r") else text
        if text.startswith(DELIMITER):
            m = _parse_marker(text, index + 1)
            markers.append(_Marker(m.kind, start, after, m.line, m.format, m.stream))
        start = after
    return markers


def _content_end(source: str, start: int, end: int) -> int:
    """`end`, less one trailing empty line: the separator before the next marker."""
    chunk = source[start:end]
    if chunk.endswith("\r\n"):
        ending = 2
    elif chunk.endswith("\n"):
        ending = 1
    else:
        return end
    ending_start = end - ending
    line_start = source.rfind("\n", start, ending_start)
    line_start = start if line_start < 0 else line_start + 1
    line = source[line_start:ending_start].removesuffix("\r")
    return ending_start if line == "" else end


def split(source: str) -> Split:
    """Split `source` into header, program, test and stream sections."""
    if source.startswith(BOM):
        raise SectionError("byte_order_mark")
    markers = _scan(source)
    if not markers:
        return Split(header=None, program=source)

    first = markers[0]
    header: str | None = None
    program: tuple[int, int] | None = None
    test: str | None = None
    streams: list[Stream] = []

    def set_program(marker: _Marker, end: int) -> None:
        nonlocal program
        if not source[marker.after_line:end].strip():
            raise SectionError("empty_faber_section", marker.line)
        program = (marker.after_line, end)

    rest = markers
    if first.kind == "bare" and first.line == 1:
        if len(markers) < 2:
            raise SectionError("unterminated_legacy_header")
        close = markers[1]
        if close.kind != "bare":
            raise SectionError("marker_inside_legacy_header", close.line)
        header = source[first.after_line:_content_end(source, first.after_line, close.start)]
        after = markers[2:]
        end = len(source) if not after else _content_end(source, close.after_line, after[0].start)
        set_program(close, end)
        rest = after
    elif source[:first.start].strip():
        program = (0, _content_end(source, 0, first.start))

    opened_with_toml = first.kind == "toml"
    for index, marker in enumerate(rest):
        nxt = rest[index + 1] if index + 1 < len(rest) else None
        end = len(source) if nxt is None else _content_end(source, marker.after_line, nxt.start)
        kind = marker.kind
        if kind == "bare":
            issue = "toml_closed_by_bare_marker" if opened_with_toml and program is None \
                else "stray_bare_marker"
            raise SectionError(issue, marker.line)
        if kind == "toml":
            if marker.line != 1:
                raise SectionError("toml_not_first_line", marker.line)
            header = source[marker.after_line:end]
        elif kind == "faber":
            if program is not None:
                raise SectionError("duplicate_section", marker.line, marker.section())
            set_program(marker, end)
        elif kind == "test":
            if test is not None:
                raise SectionError("duplicate_section", marker.line, marker.section())
            if not source[marker.after_line:end].strip():
                raise SectionError("empty_faber_test_section", marker.line)
            test = source[marker.after_line:end]
        else:
            if any(s.stream == marker.stream for s in streams):
                raise SectionError("duplicate_section", marker.line, marker.section())
            streams.append(Stream(marker.format, marker.stream, source[marker.after_line:end]))

    if program is None and test is None:
        raise SectionError("missing_faber_section")
    body = source[program[0]:program[1]] if program else ""
    return Split(header=header, program=body, test=test, streams=streams)


def normalize_text(text: str) -> str:
    """The compiler's comparison rule for `text` sections (`normalize_section_text`)."""
    lines = [line.rstrip(" \t") for line in text.replace("\r\n", "\n").split("\n")]
    start = next((i for i, line in enumerate(lines) if line), len(lines))
    end = next((i + 1 for i in range(len(lines) - 1, -1, -1) if lines[i]), start)
    return "\n".join(lines[start:end])


def stream_text(parts: Split, name: str) -> str | None:
    """A stream section as the text a program prints (`stream_section_text`)."""
    section = parts.stream(name)
    if section is None:
        return None
    if section.format == "base64":
        return base64.b64decode("".join(section.content.split())).decode("utf-8", "replace")
    text = normalize_text(section.content)
    return text + "\n" if text else text


def read(path: Path) -> Split:
    return split(path.read_text(encoding="utf-8"))


def header_fields(path: Path) -> dict | None:
    """The TOML header of `path` as a table, `None` when the file has none."""
    parts = read(path)
    return None if parts.header is None else tomllib.loads(parts.header)


def legacy_record(parts: Split) -> str:
    """The `+++`-delimited shape the corpus renderer and projector consume.

    The renderer shows one Faber block per record: the program section, or the
    test section of a test-only file. Stream sections are not source.
    """
    body = parts.program if parts.program.strip() else (parts.test or "")
    header = parts.header or ""
    if header and not header.endswith("\n"):
        header += "\n"
    return "+++\n" + header + "+++\n" + body


def published_corpus(corpus: Path) -> Path:
    """The corpus subtree the site publishes.

    Through 1.18 `corpus/` held only the language exempla. From 1.19 it holds
    every suite, and the exempla are `corpus/reference/`; the other suites
    (product, simulations, norma, acceptance, bench, behavior) were never term
    pages and are not published. The fallback keeps the 1.18 pin building
    until the site is re-pinned.
    """
    reference = corpus / "reference"
    return reference if reference.is_dir() else corpus
