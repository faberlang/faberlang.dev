"""Pinned upstream inputs for the site build.

The site reads three trees from the radix repository: `grammar/`, `locale/`
and `corpus/`. Reading the live checkout ties every build to whatever radix
`main` holds that minute, which moves faster than the site can follow. The
build instead reads a pin: `generator/upstream.lock.toml` records the git tree
id of each of the three directories. Tree ids are content addresses, so the pin
survives history rewrites that only change commits.

`materialize()` extracts the pinned trees to `generator/target/upstream/radix/`
(`git archive`, no checkout and no writes inside the radix working tree) and
every generator reads from there through `radix_root()`.

`build-site.sh --refresh-upstream [REV]` is the only thing that moves the pin.
"""
from __future__ import annotations

import subprocess
import tarfile
import io
import shutil
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - Python < 3.11
    import tomli as tomllib  # type: ignore

GENERATOR_DIR = Path(__file__).resolve().parents[1]
REPO_DIR = GENERATOR_DIR.parent
LOCK = GENERATOR_DIR / "upstream.lock.toml"
EXPLAIN_SNAPSHOT = GENERATOR_DIR / "upstream" / "explain-list.txt"
TARGET = GENERATOR_DIR / "target" / "upstream"
PINNED_TREES = ("grammar", "locale", "corpus")


class UpstreamError(RuntimeError):
    """The pin is missing, unreadable, or cannot be materialized."""


def radix_checkout() -> Path:
    """The radix git checkout used only to read pinned objects and to refresh."""
    return REPO_DIR.parent / "radix"


def read_lock() -> dict:
    if not LOCK.is_file():
        raise UpstreamError(
            f"{LOCK.relative_to(REPO_DIR)} is missing; run "
            "`build-site.sh --refresh-upstream` to pin radix"
        )
    with LOCK.open("rb") as handle:
        data = tomllib.load(handle)
    trees = data.get("trees", {})
    for name in PINNED_TREES:
        if not trees.get(name):
            raise UpstreamError(f"{LOCK.name}: [trees].{name} is not pinned")
    return data


def tree_ids() -> dict[str, str]:
    return dict(read_lock()["trees"])


def radix_root() -> Path:
    """Root holding `grammar/`, `locale/` and `corpus/` at the pinned trees."""
    return TARGET / "radix"


def _git(*args: str) -> bytes:
    result = subprocess.run(
        ["git", "-C", str(radix_checkout()), *args],
        capture_output=True,
    )
    if result.returncode != 0:
        raise UpstreamError(
            f"git {' '.join(args)}: {result.stderr.decode('utf-8', 'replace').strip()}"
        )
    return result.stdout


def resolve_rev(rev: str) -> tuple[str, dict[str, str]]:
    """Full commit id and the tree id of each pinned directory at `rev`."""
    commit = _git("rev-parse", "--verify", f"{rev}^{{commit}}").decode().strip()
    trees = {
        name: _git("rev-parse", "--verify", f"{commit}:{name}").decode().strip()
        for name in PINNED_TREES
    }
    return commit, trees


def write_lock(commit: str, trees: dict[str, str], faber_version: str) -> None:
    lines = [
        "# Pinned radix inputs for the site build. Written by",
        "# `build-site.sh --refresh-upstream`; never edit by hand.",
        "# Tree ids are content addresses, so this survives a history rewrite",
        "# that only changes commits; `commit` is informational.",
        "",
        "[radix]",
        f'commit = "{commit}"',
        "",
        "[trees]",
    ]
    lines += [f'{name} = "{trees[name]}"' for name in PINNED_TREES]
    lines += ["", "[faber]", f'version = "{faber_version}"', ""]
    LOCK.write_text("\n".join(lines), encoding="utf-8")


def _extract(tree: str, dest: Path) -> None:
    archive = _git("archive", "--format=tar", tree)
    dest.mkdir(parents=True, exist_ok=True)
    with tarfile.open(fileobj=io.BytesIO(archive)) as tar:
        kwargs = {"filter": "data"} if hasattr(tarfile, "data_filter") else {}
        tar.extractall(dest, **kwargs)


def materialize() -> Path:
    """Extract the pinned trees if the extraction does not match the lock."""
    ids = tree_ids()
    root = radix_root()
    stamp = TARGET / "extracted.toml"
    want = "\n".join(f"{name} = {ids[name]}" for name in PINNED_TREES) + "\n"
    if stamp.is_file() and stamp.read_text() == want and all(
        (root / name).is_dir() for name in PINNED_TREES
    ):
        return root
    if root.exists():
        shutil.rmtree(root)
    for name in PINNED_TREES:
        try:
            _extract(ids[name], root / name)
        except UpstreamError as exc:
            raise UpstreamError(
                f"pinned {name} tree {ids[name]} is not in the radix object store "
                f"({exc}); run `build-site.sh --refresh-upstream`"
            ) from None
    stamp.parent.mkdir(parents=True, exist_ok=True)
    stamp.write_text(want)
    return root
