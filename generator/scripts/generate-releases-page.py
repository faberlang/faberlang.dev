#!/usr/bin/env python3
"""Generate src/en-US/history/releases.md from faberlang/releases GitHub tags.

Requires: gh CLI authenticated with public-read access to faberlang/releases.

Usage:
  python3 generator/scripts/generate-releases-page.py
  python3 generator/scripts/generate-releases-page.py --output path/to/releases.md
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path


def fetch_releases() -> list[dict]:
    raw = subprocess.check_output(
        ["gh", "api", "repos/faberlang/releases/releases?per_page=100", "--paginate"],
        text=True,
    )
    text = raw.strip()
    if "]\n[" in text:
        parts: list[list[dict]] = []
        buf = ""
        depth = 0
        for ch in text:
            buf += ch
            if ch == "[":
                depth += 1
            elif ch == "]":
                depth -= 1
                if depth == 0:
                    parts.append(json.loads(buf))
                    buf = ""
        return [item for part in parts for item in part]
    return json.loads(text)


def human_size(n: int) -> str:
    size = float(n)
    for unit in ("B", "KB", "MB", "GB"):
        if size < 1024 or unit == "GB":
            if unit == "B":
                return f"{int(size)} B"
            if unit == "KB":
                return f"{size:.0f} {unit}"
            return f"{size:.1f} {unit}"
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
    return "Archive"


def is_checksum(name: str) -> bool:
    return name.endswith(".sha256") or name.endswith(".sha256sum")


def version_from_tag(tag: str) -> str:
    m = re.match(r"^(?:faber|radix)-v(.+)$", tag)
    return m.group(1) if m else tag


def asset_rows(assets: list[dict]) -> list[tuple[str, str, str, str]]:
    by_base: dict[str, dict] = {}
    for a in assets:
        name = a["name"]
        url = a["browser_download_url"]
        size = a.get("size") or 0
        if is_checksum(name):
            base = name[: -len(".sha256")] if name.endswith(".sha256") else name
            entry = by_base.setdefault(base, {})
            entry["sha"] = url
        else:
            entry = by_base.setdefault(name, {})
            entry["url"] = url
            entry["size"] = size
            entry["name"] = name
    rows: list[tuple[str, str, str, str]] = []
    for base, info in sorted(by_base.items(), key=lambda kv: kv[0]):
        if "url" not in info:
            continue
        plat = platform_label(info["name"])
        size_s = human_size(int(info.get("size") or 0))
        sha = info.get("sha")
        sha_cell = f"[checksum]({sha})" if sha else "—"
        rows.append((plat, f"[{info['name']}]({info['url']})", size_s, sha_cell))
    return rows


def render(data: list[dict]) -> str:
    data = sorted(
        data,
        key=lambda r: r.get("published_at") or r.get("created_at") or "",
        reverse=True,
    )
    faber = [r for r in data if r["tag_name"].startswith("faber-")]
    primary = faber[0] if faber else data[0]
    primary_tag = primary["tag_name"]
    primary_ver = version_from_tag(primary_tag)
    primary_date = (primary.get("published_at") or "")[:10]
    primary_url = (
        primary.get("html_url")
        or f"https://github.com/faberlang/releases/releases/tag/{primary_tag}"
    )

    lines: list[str] = [
        "+++",
        'title = "Releases"',
        'section = "releases"',
        "order = 1",
        "sources = []",
        "+++",
        "",
        "Download prebuilt Faber CLI archives and browse every published tag in the "
        "[faberlang/releases](https://github.com/faberlang/releases) asset repository. "
        "This page is for **installing** the compiler CLI, not for building the compiler "
        "from source.",
        "",
        "## Getting started {#getting-started}",
        "",
        "| Path | What it covers |",
        "|---|---|",
        "| [Install and download](/start/install.html) | Current release, PATH setup, verify, first `faber check` |",
        "| [Quick tour](/start/) | Language shape in a few minutes |",
        "| [Hello, Faber](/start/hello.html) | First package |",
        "| [Commands](/start/commands.html) | Daily CLI loop |",
        "| [Projects](/start/projects.html) | Real package layout |",
        "| [Examples](/start/examples.html) | Public sample packages |",
        "",
        "Build-from-source instructions are intentionally **not** linked here. "
        "Use the prebuilt archives unless you work on the private compiler tree.",
        "",
        f"## Latest release — Faber {primary_ver} {{#latest}}",
        "",
        "| Field | Value |",
        "|---|---|",
        "| **Product** | Faber CLI |",
        f"| **Version** | {primary_ver} |",
        f"| **Tag** | `{primary_tag}` |",
        f"| **Published** | {primary_date} |",
        f"| **GitHub** | [{primary_tag}]({primary_url}) |",
        "| **License** | MIT |",
        "",
        "### Binaries {#latest-binaries}",
        "",
        "| Platform | Archive | Size | SHA-256 |",
        "|---|---|---|---|",
    ]
    for plat, arch, size, sha in asset_rows(primary.get("assets") or []):
        lines.append(f"| **{plat}** | {arch} | {size} | {sha} |")
    lines.extend(
        [
            "",
            "Extract the archive and put the `faber` binary on your `PATH`. "
            "Step-by-step: [Install and download](/start/install.html).",
            "",
            "## Historical releases {#historical}",
            "",
            "Every tag currently published under "
            "[github.com/faberlang/releases](https://github.com/faberlang/releases/releases), "
            "newest first. **Faber** tags are the user CLI. **Radix** tags are historical "
            "compiler CLI archives (most are macOS arm64 only).",
            "",
            f"_Inventory snapshot from the GitHub Releases API. "
            f"{len(data)} tags, regenerated for this page._",
            "",
        ]
    )

    for r in data:
        tag = r["tag_name"]
        date = (r.get("published_at") or "")[:10]
        url = (
            r.get("html_url")
            or f"https://github.com/faberlang/releases/releases/tag/{tag}"
        )
        if tag.startswith("faber-"):
            kind = "Faber CLI"
        elif tag.startswith("radix-"):
            kind = "Radix compiler"
        else:
            kind = "Release"
        anchor = tag.replace(".", "-")
        lines.append(f"### `{tag}` {{#{anchor}}}")
        lines.append("")
        lines.append(f"**{kind}** · published {date} · [GitHub release]({url})")
        lines.append("")
        assets = r.get("assets") or []
        if not assets:
            lines.append("_No downloadable assets on this tag._")
            lines.append("")
            continue
        lines.append("| Platform | Archive | Size | SHA-256 |")
        lines.append("|---|---|---|---|")
        for plat, arch, size, sha in asset_rows(assets):
            lines.append(f"| {plat} | {arch} | {size} | {sha} |")
        lines.append("")

    lines.extend(
        [
            "## Source of truth {#source-of-truth}",
            "",
            "Assets live in the public "
            "[faberlang/releases](https://github.com/faberlang/releases) repository. "
            "When a new tag is published, regenerate this page with "
            "`generator/scripts/generate-releases-page.py` and rebuild the site.",
            "",
            "## See also {#see-also}",
            "",
            "| Link | Role |",
            "|---|---|",
            "| [Install and download](/start/install.html) | Recommended install path |",
            "| [History](/history/) | Project timeline and origins |",
            "| [faberlang/releases on GitHub](https://github.com/faberlang/releases/releases) | Raw tag list and assets |",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    repo = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=repo / "src/en-US/history/releases.md",
        help="Output Markdown path",
    )
    args = parser.parse_args()
    data = fetch_releases()
    if not data:
        print("error: no releases returned from GitHub API", file=sys.stderr)
        return 1
    text = render(data)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(text, encoding="utf-8")
    print(f"wrote {args.output} ({len(data)} tags)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
