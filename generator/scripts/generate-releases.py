#!/usr/bin/env python3
"""
generate-releases.py — build the Releases section from tags and release notes.

The Releases section answers two questions the Install page deliberately does
not: *what versions exist*, and *what changed in each one*. Install shows one
binary — the current one — and nothing else.

Two sources, joined on version:

    github faberlang/releases   published tags and downloadable assets
    <sibling repo>/docs/release/v*.md   the release notes themselves

Neither source is complete on its own. A version can have notes but no
published tag (developed, documented, never shipped as an asset), or a tag but
no notes (shipped before the notes practice existed, or notes not yet
backfilled). The union is listed; each page shows whichever halves exist and
says plainly when one is missing. Nothing is invented.

Outputs:

    src/en-US/releases/index.md          the version index, newest first
    src/en-US/releases/<product>-<v>.md  one page per version

Requires `gh` authenticated for public read. Release notes are read from
sibling checkouts beside this repository; a missing checkout degrades to
"tags only" rather than failing.

Usage:
    generate-releases.py [--output-dir src/en-US/releases] [--no-fetch]
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WORKSPACE = REPO.parent

PRODUCTS = {
    "faber": {
        "label": "Faber",
        "blurb": "The user-facing CLI: check, build, run, test, format, explain.",
        "notes_dir": WORKSPACE / "faber" / "docs" / "release",
    },
    "radix": {
        "label": "Radix",
        "blurb": "The compiler. Bundled inside the `faber` CLI; also published "
                 "standalone for anyone who needs it directly.",
        "notes_dir": WORKSPACE / "radix" / "docs" / "release",
    },
}

# Notes files that document something other than a shipped version.
NOTES_SKIP = re.compile(r"(-dev-notes|-sibling-pins)$")


def is_prerelease(version: str) -> bool:
    return "-" in version


@dataclass
class Version:
    product: str
    version: str
    tag: str = ""
    published: str = ""
    assets: list[dict] = field(default_factory=list)
    notes: str = ""

    @property
    def slug(self) -> str:
        return f"{self.product}-{self.version}"

    @property
    def sort_key(self) -> tuple:
        # 1.0.0-rc.2 must sort below 1.0.0; a prerelease suffix ranks first.
        core, _, pre = self.version.partition("-")
        nums = tuple(int(p) if p.isdigit() else 0 for p in core.split("."))
        return nums + ((0, pre) if pre else (1, ""))


def fetch_releases() -> list[dict]:
    raw = subprocess.check_output(
        ["gh", "api", "repos/faberlang/releases/releases?per_page=100", "--paginate"],
        text=True,
    ).strip()
    # `gh --paginate` concatenates one JSON array per page.
    parts: list[list[dict]] = []
    buf, depth = "", 0
    for ch in raw:
        buf += ch
        if ch == "[":
            depth += 1
        elif ch == "]":
            depth -= 1
            if depth == 0:
                parts.append(json.loads(buf))
                buf = ""
    return [item for part in parts for item in part]


def human_size(n: int) -> str:
    size = float(n)
    for unit in ("B", "KB", "MB"):
        if size < 1024:
            return f"{int(size)} B" if unit == "B" else f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} GB"


def platform_label(name: str) -> str:
    n = name.lower()
    if "aarch64-apple-darwin" in n:
        return "macOS arm64"
    if "x86_64-apple-darwin" in n:
        return "macOS x64"
    if "x86_64-unknown-linux-gnu" in n:
        return "Linux x64"
    if "aarch64-unknown-linux-gnu" in n:
        return "Linux arm64"
    return name


def collect() -> dict[str, list[Version]]:
    found: dict[tuple[str, str], Version] = {}

    try:
        releases = fetch_releases()
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        print(f"  warning: no tag data ({exc}); notes only", file=sys.stderr)
        releases = []

    for rel in releases:
        tag = rel.get("tag_name", "")
        m = re.match(r"^(faber|radix)-v(.+)$", tag)
        if not m:
            continue
        product, version = m.group(1), m.group(2)
        found[(product, version)] = Version(
            product=product,
            version=version,
            tag=tag,
            published=(rel.get("published_at") or "")[:10],
            assets=[
                {
                    "name": a["name"],
                    "size": a.get("size", 0),
                    "url": a["browser_download_url"],
                }
                for a in rel.get("assets", [])
            ],
        )

    for product, meta in PRODUCTS.items():
        notes_dir = meta["notes_dir"]
        if not notes_dir.is_dir():
            print(f"  warning: no notes checkout at {notes_dir}", file=sys.stderr)
            continue
        for path in sorted(notes_dir.glob("v*.md")):
            version = path.stem[1:]
            if NOTES_SKIP.search(version):
                continue
            entry = found.get((product, version))
            if entry is None:
                # An untagged prerelease is an internal candidate lock, not a
                # version anyone can install. Its own notes usually say so in
                # as many words ("no tag, no push, no public download"), and
                # listing it puts a version at the top of the table that is
                # newer than anything shipped. Tagged prereleases stay: those
                # were published on purpose.
                if is_prerelease(version):
                    continue
                entry = Version(product=product, version=version)
                found[(product, version)] = entry
            entry.notes = path.read_text(encoding="utf-8")

    grouped: dict[str, list[Version]] = {p: [] for p in PRODUCTS}
    for (product, _), entry in found.items():
        grouped[product].append(entry)
    for product in grouped:
        grouped[product].sort(key=lambda v: v.sort_key, reverse=True)
    return grouped


def _join_wrapped_bold(text: str) -> str:
    lines = text.split("\n")
    out, i, fence = [], 0, False
    while i < len(lines):
        line = lines[i]
        if line.lstrip().startswith("```"):
            fence = not fence
        if not fence and line.count("**") % 2 == 1 and i + 1 < len(lines):
            merged, j = line, i + 1
            while j < len(lines) and merged.count("**") % 2 == 1:
                merged = merged.rstrip() + " " + lines[j].lstrip()
                j += 1
            out.append(merged)
            i = j
            continue
        out.append(line)
        i += 1
    return "\n".join(out)


def prepare_notes(raw: str) -> str:
    """Demote the notes' own H1 and shift every heading one level down.

    The page supplies its own title, so an imported H1 would compete with it.
    Shifting the whole tree keeps the notes' internal hierarchy intact under a
    single `## Release notes` heading.
    """
    # Inline spans render per line, so bold that opens on one line and closes
    # on the next emits literal asterisks. Imported notes are hard-wrapped
    # prose written elsewhere and full of these; join them on the way in.
    raw = _join_wrapped_bold(raw)

    out: list[str] = []
    in_fence = False
    for line in raw.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            # A release note quotes the language as it stood at that version.
            # Old syntax legitimately no longer compiles, so these fences must
            # not be held to the current-language fence contract — the note is
            # a historical record, not a claim about today's grammar.
            if in_fence and line.strip().startswith("```faber"):
                out.append("```text")
                continue
            out.append(line)
            continue
        if not in_fence and line.startswith("#"):
            level = len(line) - len(line.lstrip("#"))
            if level == 1:
                continue  # the page title already says this
            out.append("#" + line if level < 6 else line)
            continue
        out.append(line)
    return "\n".join(out).strip()


def install_block(v: Version) -> list[str]:
    archives = [a for a in v.assets if a["name"].endswith(".tar.gz")]
    if not archives:
        return [
            "## Install this version {#install}",
            "",
            "No prebuilt archives were published for this version. It is listed "
            "here because its release notes are part of the record.",
            "",
        ]

    sums = {a["name"]: a["url"] for a in v.assets if a["name"].endswith(".sha256")}
    lines = [
        "## Install this version {#install}",
        "",
        f"Pinned download for **{PRODUCTS[v.product]['label']} {v.version}**. "
        "For the current release, use [Install](/start/install.html) instead.",
        "",
        "| Platform | Archive | Size | Checksum |",
        "|---|---|---|---|",
    ]
    for a in sorted(archives, key=lambda x: x["name"]):
        checksum = sums.get(a["name"] + ".sha256")
        cell = f"[sha256]({checksum})" if checksum else "—"
        lines.append(
            f"| **{platform_label(a['name'])}** | [{a['name']}]({a['url']}) "
            f"| {human_size(a['size'])} | {cell} |"
        )

    mac = next((a for a in archives if "aarch64-apple-darwin" in a["name"]), None)
    if mac:
        stem = mac["name"][: -len(".tar.gz")]
        lines += [
            "",
            "```bash",
            f"curl -fsSL -o {v.product}.tgz \\",
            f"  {mac['url']}",
            f"tar -xzf {v.product}.tgz",
            f"sudo mv {stem}/{v.product} /usr/local/bin/",
            f"{v.product} --version",
            "```",
        ]
    lines.append("")
    return lines


def render_version_page(v: Version, order: int) -> str:
    label = PRODUCTS[v.product]["label"]
    head = [
        "+++",
        f'title = "{label} {v.version}"',
        'section = "releases"',
        f"order = {order}",
        "sources = []",
        "+++",
        "",
    ]

    facts = [
        "| Field | Value |",
        "|---|---|",
        f"| **Product** | {label} |",
        f"| **Version** | {v.version} |",
    ]
    if v.tag:
        facts.append(f"| **Tag** | `{v.tag}` |")
        facts.append(
            f"| **GitHub** | [{v.tag}]"
            f"(https://github.com/faberlang/releases/releases/tag/{v.tag}) |"
        )
    if v.published:
        facts.append(f"| **Published** | {v.published} |")
    facts.append("| **License** | MIT |" if v.product == "faber"
                 else "| **Source** | Closed for now — see [Open source](/open-source.html) |")
    facts.append("")

    body = head + facts + install_block(v)

    if v.notes:
        body += ["## Release notes {#notes}", "", prepare_notes(v.notes), ""]
    else:
        body += [
            "## Release notes {#notes}",
            "",
            "No release notes were recorded for this version.",
            "",
        ]

    body += [
        "---",
        "",
        "[All releases](/releases/) · [Install the current release](/start/install.html)",
        "",
    ]
    return "\n".join(body)


def render_index(grouped: dict[str, list[Version]]) -> str:
    lines = [
        "+++",
        'title = "Releases"',
        'section = "releases"',
        "order = 4",
        "sources = []",
        "+++",
        "",
        "Every published version of Faber and Radix. Each entry links to a page "
        "with pinned install instructions for that exact version and its full "
        "release notes.",
        "",
        "Installing for the first time? Use [Install](/start/install.html) — it "
        "covers the current release only, which is what almost everyone wants.",
        "",
    ]

    for product, meta in PRODUCTS.items():
        versions = grouped.get(product, [])
        if not versions:
            continue
        lines += [
            f"## {meta['label']} {{#{product}}}",
            "",
            meta["blurb"],
            "",
            "| Version | Published | Downloads | Notes |",
            "|---|---|---|---|",
        ]
        for v in versions:
            archives = sum(1 for a in v.assets if a["name"].endswith(".tar.gz"))
            lines.append(
                f"| [{meta['label']} {v.version}](/releases/{v.slug}.html) "
                f"| {v.published or '—'} "
                f"| {archives if archives else '—'} "
                f"| {'yes' if v.notes else '—'} |"
            )
        lines.append("")

    lines += [
        "## Reading this table {#reading}",
        "",
        "A dash under **Downloads** means no prebuilt archive was published for "
        "that version — it is listed because its release notes are part of the "
        "record. A dash under **Notes** means the version shipped but its notes "
        "have not been backfilled yet.",
        "",
        "Radix source is closed for now; its published artifacts are the compiler "
        "binary and checksums. See [Open source](/open-source.html).",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output-dir", default="src/en-US/releases")
    args = ap.parse_args()

    out = REPO / args.output_dir
    out.mkdir(parents=True, exist_ok=True)

    grouped = collect()
    total = sum(len(v) for v in grouped.values())
    if not total:
        print("ERROR: no versions found from tags or notes", file=sys.stderr)
        return 1

    for existing in out.glob("*.md"):
        existing.unlink()

    (out / "index.md").write_text(render_index(grouped), encoding="utf-8")

    order = 10
    for product in PRODUCTS:
        for v in grouped.get(product, []):
            (out / f"{v.slug}.md").write_text(
                render_version_page(v, order), encoding="utf-8"
            )
            order += 1

    tagged = sum(1 for vs in grouped.values() for v in vs if v.tag)
    noted = sum(1 for vs in grouped.values() for v in vs if v.notes)
    print(f"releases: {total} versions ({tagged} tagged, {noted} with notes) → {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
