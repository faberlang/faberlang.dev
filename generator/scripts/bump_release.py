#!/usr/bin/env python3
"""Move every hand-typed release fact to a new Faber release in one step.

The install surface names one published release: the agent lobby
(`static/install.md`), the install skill (version, tag, publish date, bundled
compiler, release page and the four archive URLs) and the skill catalog
(`index.json`). They are the only pages that carry it, so a release is a
mechanical edit, not a content pass:

    generator/scripts/bump_release.py 1.14.0 --published 2026-10-20 --radix 0.85.0
    generator/scripts/bump_release.py --check

`--check` verifies the three files agree and exits 1 if not. The build already
reads the version from `static/install.md`; this keeps the other two from
drifting from it.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
LOBBY = Path("static/install.md")
SKILL = Path("static/.well-known/agent-skills/install/SKILL.md")
CATALOG = Path("static/.well-known/agent-skills/index.json")

LOBBY_RE = re.compile(r"^(Current release: Faber )(\S+?)(\.)$", re.M)
CATALOG_RE = re.compile(r'^(\s*"version": ")([^"]+)(",?)$', re.M)
SKILL_VERSION_RE = re.compile(r"^(- \*\*Version:\*\* )(\S+)$", re.M)
SKILL_PUBLISHED_RE = re.compile(r"^(- \*\*Published:\*\* )(\S+)$", re.M)
SKILL_COMPILER_RE = re.compile(r"^(- \*\*Bundled compiler:\*\* Radix )(\S+)$", re.M)
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def current(root: Path = REPO) -> dict[str, str]:
    """The release each of the three files names (`None` where it is missing)."""
    def first(pattern: re.Pattern, path: Path) -> str | None:
        found = pattern.search((root / path).read_text(encoding="utf-8"))
        return found.group(2) if found else None

    skill = (root / SKILL).read_text(encoding="utf-8")
    tags = set(re.findall(r"faber-v(\d+\.\d+\.\d+)", skill))
    return {
        "lobby": first(LOBBY_RE, LOBBY),
        "catalog": first(CATALOG_RE, CATALOG),
        "skill": first(SKILL_VERSION_RE, SKILL),
        "skill_urls": ",".join(sorted(tags)),
    }


def consistent(root: Path = REPO) -> list[str]:
    """Human-readable disagreements between the three files; empty when they agree."""
    seen = current(root)
    problems = []
    if not all(seen[key] for key in ("lobby", "catalog", "skill")):
        problems.append(f"missing a version: {seen}")
        return problems
    versions = {seen["lobby"], seen["catalog"], seen["skill"]}
    if len(versions) != 1:
        problems.append(
            f"install.md says {seen['lobby']}, index.json says {seen['catalog']}, "
            f"the install skill says {seen['skill']}")
    if seen["skill_urls"] != seen["skill"]:
        problems.append(f"the install skill's tag and URLs name {seen['skill_urls']}, "
                        f"its version line says {seen['skill']}")
    return problems


def bump(root: Path, version: str, published: str, radix: str) -> list[Path]:
    """Rewrite the three files in `root`; returns the files changed."""
    if not VERSION_RE.match(version):
        raise ValueError(f"not a release version: {version!r}")
    if not DATE_RE.match(published):
        raise ValueError(f"not a date (YYYY-MM-DD): {published!r}")
    if not VERSION_RE.match(radix):
        raise ValueError(f"not a Radix version: {radix!r}")
    problems = consistent(root)
    if problems:
        raise ValueError("refusing to bump from an inconsistent state: " + "; ".join(problems))
    old = current(root)["skill"]
    changed: list[Path] = []

    def rewrite(path: Path, edit) -> None:
        target = root / path
        before = target.read_text(encoding="utf-8")
        after = edit(before)
        if after != before:
            target.write_text(after, encoding="utf-8")
            changed.append(path)

    rewrite(LOBBY, lambda t: LOBBY_RE.sub(rf"\g<1>{version}\g<3>", t, count=1))
    rewrite(CATALOG, lambda t: CATALOG_RE.sub(rf"\g<1>{version}\g<3>", t, count=1))

    def skill(t: str) -> str:
        t = t.replace(f"faber-v{old}", f"faber-v{version}")
        t = SKILL_VERSION_RE.sub(rf"\g<1>{version}", t, count=1)
        t = SKILL_PUBLISHED_RE.sub(rf"\g<1>{published}", t, count=1)
        return SKILL_COMPILER_RE.sub(rf"\g<1>{radix}", t, count=1)

    rewrite(SKILL, skill)
    leftover = [p for p in (LOBBY, SKILL, CATALOG) if old in (root / p).read_text(encoding="utf-8")
                and old != version]
    if leftover:
        raise ValueError(f"{old} still appears in: " + ", ".join(str(p) for p in leftover))
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("version", nargs="?", help="new release, e.g. 1.14.0")
    parser.add_argument("--published", help="publish date, YYYY-MM-DD")
    parser.add_argument("--radix", help="bundled Radix version, e.g. 0.85.0")
    parser.add_argument("--check", action="store_true", help="verify the three files agree")
    args = parser.parse_args()
    if args.check or not args.version:
        problems = consistent()
        for problem in problems:
            print(problem, file=sys.stderr)
        if not problems:
            print(f"release facts agree: {current()['lobby']}")
        return 1 if problems else 0
    if not (args.published and args.radix):
        parser.error("--published and --radix are required to bump")
    try:
        changed = bump(REPO, args.version, args.published, args.radix)
    except ValueError as err:
        print(err, file=sys.stderr)
        return 1
    for path in changed:
        print(f"updated {path}")
    print("Next: update the `Binary versions` note in AGENTS.md, run build-site.sh, commit.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
