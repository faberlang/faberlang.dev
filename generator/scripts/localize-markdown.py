#!/usr/bin/env python3
"""Materialize locale-specific Markdown for Speculum rendering.

For non-Latin locale builds, fluid Faber fences are converted to the reader
locale before rendering. Pinned and eligible text fences are also converted
when possible; package and reject fences remain structurally intact.
"""

from __future__ import annotations

import argparse
import os
import re
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
        if token == "mode=package":
            # One file of a multi-file package. `faber convert` cannot resolve
            # its siblings, so it warns LOCALE001 per unresolved import and
            # reformats what it does not understand — on the Examples pages
            # that means the "real package source" stops being the real file.
            # Same rule locale-tabs.py applies, for the same reason.
            return False
    return True


def stage_reader_packs(faber: str) -> None:
    """Make reader packs resolvable beside the faber binary.

    `faber convert --to` looks for share/faber/locale/<X>/pack.toml relative
    to its own executable, and a workspace build has no such directory. The
    packs live in the radix tree; link them into place. Writes only inside
    faber/target/, which is build output.
    """
    binary = Path(faber).resolve()
    if not binary.is_file():
        return
    workspace = binary.parent.parent.parent.parent
    src = workspace / "radix" / "locale"
    if not src.is_dir():
        return
    dest = binary.parent.parent / "share" / "faber" / "locale"
    dest.mkdir(parents=True, exist_ok=True)
    for pack in sorted(src.iterdir()):
        if not (pack / "pack.toml").is_file():
            continue
        link = dest / pack.name
        if not link.exists():
            link.symlink_to(pack, target_is_directory=True)


def transcode_faber(source: str, locale: str, faber: str, label: str) -> str | None:
    if locale == "la":
        return source

    # `faber convert --to` is the only thing that renders source INTO a
    # reader locale. `radix emit -t faber` is *canonical* re-emission — Latin by
    # definition — and its --locale flag declares what the input is written in,
    # not what to print. Routing through radix therefore returned Latin while
    # reporting success, which is why localized doc pages carried untranslated
    # fences for as long as they did.
    args = [faber, "convert", "--from", "la", "--to", locale, "--stdout"]

    with tempfile.TemporaryDirectory(prefix="speculum-locale-") as tmp:
        path = Path(tmp) / "fence.fab"
        path.write_text(source)
        proc = subprocess.run(
            args + [str(path)],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

    if proc.returncode != 0:
        sys.stderr.write(f"WARNING: failed to transcode {label} for {locale}; keeping source\n")
        if proc.stderr:
            sys.stderr.write(proc.stderr)
        return None

    # `faber convert --stdout` stamps the target locale into a TOML frontmatter
    # block. The fence is already inside a Markdown code block that names its
    # locale, so the block would only show up as stray text in the rendered code.
    out = re.sub(r"\A\+\+\+\n.*?\n\+\+\+\n", "", proc.stdout, count=1, flags=re.S)
    return out.rstrip("\n")


def localize_text(text: str, locale: str, faber: str, label: str) -> str:
    out: list[str] = []
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from project_reader_terms import load_mapping
    pack = Path(__file__).resolve().parents[3] / "radix" / "locale" / locale / "pack.toml"
    mapping = load_mapping(pack) if pack.is_file() else {}
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
            tokens = info.split()
            pinned = "mode=pinned" in tokens
            eligible_text = tokens and tokens[0] == "text" and (
                "←" in body_text
                or any(re.match(rf"^\s*{re.escape(key)}(?:\b|(?=[<{{(]))", body_text, re.M) for key in mapping)
            )
            transcode = is_fluid_faber(info) or pinned or bool(eligible_text)
            if transcode:
                converted = transcode_faber(body_text, locale, faber, label)
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
            continue
        out.append(line)
        i += 1
    return "\n".join(out) + ("\n" if text.endswith("\n") else "")


def main() -> int:
    args = parse_args()
    stage_reader_packs(args.faber)
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
