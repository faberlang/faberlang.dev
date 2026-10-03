#!/usr/bin/env python3
"""Generate the /agents/reference tree from the `faber explain` registry."""
from __future__ import annotations

import argparse
import itertools
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from agent_locales import read_packs
from agent_reference import (
    assign_slugs,
    choose_example,
    parse_list,
    parse_prose,
    render_index,
    render_page,
    render_stub,
    slug_for,
    split_body,
)
from corpus_locale import default_reader_root
from project_reader_terms import load_mapping, project_markdown

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUTPUTS = (
    REPO_ROOT / "static" / "agents" / "reference",
    REPO_ROOT / "dist" / "agents" / "reference",
)


def find_faber(explicit: str | None) -> str:
    """The explain registry needs a binary that can resolve its reference pack.

    An installed `faber` carries no pack unless one was installed beside it, so
    the workspace development build is preferred and the caller can override.
    """
    if explicit:
        return explicit
    workspace = REPO_ROOT.parent / "radix" / "target" / "debug" / "faber"
    if workspace.is_file():
        return str(workspace)
    found = shutil.which("faber")
    if not found:
        raise SystemExit("no faber binary found; pass --faber")
    return found


def explain(faber: str, *args: str) -> str:
    result = subprocess.run([faber, "explain", *args], capture_output=True, text=True)
    if result.returncode != 0:
        raise SystemExit(f"faber explain {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--faber", default=None, help="faber binary that resolves its reference pack")
    parser.add_argument("--packs", type=Path, default=default_reader_root())
    parser.add_argument("--out", type=Path, action="append", default=None,
                        help="output directory (repeatable); defaults to static/ and dist/")
    parser.add_argument("--strict", action="store_true", help="fail when a registry entry has no page")
    parser.add_argument("--check", action="store_true", help="report without writing")
    args = parser.parse_args()

    faber = find_faber(args.faber)
    sections, listing = parse_list(explain(faber, "--list"))

    # Fetch every entry first: the slug depends on the entry's own kind.
    payloads: dict[str, dict] = {}
    for entry in listing:
        payload = json.loads(explain(faber, entry["term"], "--json"))
        payloads[entry["term"]] = payload
        entry["kind"] = payload.get("kind", "")

    # slug_for wants one spelling per canonical; read_packs carries aliases too.
    pack = {
        section: {canonical: spelling for canonical, (spelling, _aliases) in table.items()}
        for section, table in read_packs(args.packs)["en"].items()
    }
    slugs, collisions = assign_slugs(listing, pack)
    for term, wanted, owner in collisions:
        print(f"collision: '{term}' wanted '{wanted}' (held by '{owner}'), using '{slugs[term]}'", file=sys.stderr)

    mapping = load_mapping(args.packs / "en" / "pack.toml")
    scratch = tempfile.TemporaryDirectory()
    scratch_path = Path(scratch.name)
    counter = itertools.count()

    def project(text: str, name: str = "page", example: bool = False) -> str:
        return project_markdown(text, mapping, relative_path=f"agents/reference/{name}.md", reader="en", example=example)

    def checks(code: str) -> bool:
        path = scratch_path / f"example_{next(counter)}.fab"
        path.write_text(code + "\n", encoding="utf-8")
        return subprocess.run(
            [faber, "check", "--locale=en", str(path)], capture_output=True, text=True
        ).returncode == 0

    def example_for(original: str, name: str) -> str:
        # The registry example is one bare Faber program, not a Markdown page:
        # project it as a single code region so a keyword-shaped field keeps
        # one spelling across declaration, construction, and member access.
        text, fell_back = choose_example(original, project(original, name, example=True), checks)
        if fell_back:
            print(f"WARNING: projection broke the '{name}' example; shipping the registry text", file=sys.stderr)
        return text

    pages: dict[str, str] = {}
    for entry in listing:
        term = entry["term"]
        payload = payloads[term]
        prose, examples = split_body(payload.get("body", ""))
        _preamble, blocks = parse_prose(prose)
        spelling = slug_for(term, payload.get("kind", ""), pack)
        # A term that lost its spelling to a collision names itself in the title,
        # so two entries sharing one English word do not read as the same page.
        title = spelling if slugs[term] == spelling else f"{spelling} ({term})"
        pages[slugs[term]] = render_page(
            term=term,
            title=title,
            section=entry["section"],
            summary=payload.get("summary") or entry["summary"],
            syntax=payload.get("syntax", ""),
            aliases=payload.get("aliases") or [],
            related=payload.get("related") or [],
            blocks=blocks,
            examples=examples,
            link_of=slugs,
            project=lambda text: project(text, slugs[term]),
            project_example=lambda text: example_for(text, slugs[term]),
        )
        for alias in payload.get("aliases") or []:
            if alias in pages or alias in slugs:
                continue
            # The stub's only variable is the registry term, which the reader
            # needs verbatim: projecting it would print a lookup that reads
            # differently from the one in the page it points at.
            pages[alias] = render_stub(slug=alias, target=slugs[term], source=f"`faber explain {term}`")

    index = render_index(sections=sections, entries=listing, slugs=slugs)

    missing = [entry["term"] for entry in listing if slugs[entry["term"]] not in pages]
    for term in missing:
        print(f"MISSING PAGE: {term}", file=sys.stderr)

    if not args.check:
        for directory in args.out or DEFAULT_OUTPUTS:
            directory.mkdir(parents=True, exist_ok=True)
            for name in [path.stem for path in directory.glob("*.md")]:
                if name not in pages and name != "index":
                    (directory / f"{name}.md").unlink()
            (directory / "index.md").write_text(index, encoding="utf-8")
            for slug, text in pages.items():
                (directory / f"{slug}.md").write_text(text, encoding="utf-8")
            print(f"wrote {len(pages) + 1} pages to {directory}")

    if args.strict and missing:
        print("ERROR: reference gate failed", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
