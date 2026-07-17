#!/usr/bin/env python3
"""Materialize locale-specific Markdown for Speculum rendering.

For non-Latin locale builds, fluid Faber fences are rendered through the Faber
canonical emitter before the Markdown page reaches the generator. Pinned fences
(`locale=...`) and reject fences are left unchanged because the author declared
that source surface explicitly.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
import tempfile
from pathlib import Path


FENCE = "```"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--locale", required=True)
    parser.add_argument("--faber", default=os.environ.get("FABER", "faber"))
    return parser.parse_args()


def is_fluid_faber(info: str) -> bool:
    tokens = info.split()
    if not tokens or tokens[0] != "faber":
        return False
    for token in tokens[1:]:
        if token.startswith("locale="):
            return False
        if token == "mode=pinned":
            return False
        if token == "outcome=rejects":
            return False
    return True


def transcode_faber(source: str, locale: str, faber: str, label: str) -> str:
    if locale == "la":
        return source

    with tempfile.TemporaryDirectory(prefix="speculum-locale-") as tmp:
        path = Path(tmp) / "fence.fab"
        path.write_text(source)
        proc = subprocess.run(
            [faber, "emit", "-t", "faber", f"--reader-locale={locale}", str(path)],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

    if proc.returncode != 0:
        sys.stderr.write(f"ERROR: failed to transcode {label} for {locale}\n")
        sys.stderr.write(proc.stderr)
        raise SystemExit(proc.returncode)

    return proc.stdout.rstrip("\n")


def localize_text(text: str, locale: str, faber: str, label: str) -> str:
    out: list[str] = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if stripped.startswith(FENCE):
            info = stripped[3:].strip()
            body: list[str] = []
            out.append(line)
            i += 1
            while i < len(lines) and lines[i].strip() != FENCE:
                body.append(lines[i])
                i += 1
            body_text = "\n".join(body)
            if is_fluid_faber(info):
                body_text = transcode_faber(body_text, locale, faber, label)
            if body_text:
                out.extend(body_text.splitlines())
            if i < len(lines):
                out.append(lines[i])
            i += 1
            continue
        out.append(line)
        i += 1
    return "\n".join(out) + ("\n" if text.endswith("\n") else "")


def main() -> int:
    args = parse_args()
    source = args.source.resolve()
    output = args.output.resolve()
    for md in sorted(source.rglob("*.md")):
        rel = md.relative_to(source)
        dest = output / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(localize_text(md.read_text(), args.locale, args.faber, str(rel)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
