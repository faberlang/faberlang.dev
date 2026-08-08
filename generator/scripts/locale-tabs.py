#!/usr/bin/env python3
"""
locale-tabs.py — turn cheat sheet Faber examples into reader-locale tab cards.

The cheat sheet teaches the language. The single most distinctive thing about
the language is that the same program can be read in eight human languages, and
showing that once on the landing page while every teaching example stays Latin
undersells it. So each example becomes the same tabbed card the landing hero
uses, carrying all eight reader surfaces.

One base source, eight renderings. The Latin fence in the Markdown is the
authority; every other panel is `faber format --locale <X>` output. Nobody
hand-writes Thai or Arabic Faber, and a reader-pack change re-renders them all.

Two subcommands, mirroring diagrams.py:

    render   transcode every cheat sheet fence into the committed cache
    inject   build the tab cards in dist/ from that cache

`render` is an authoring step and needs the toolchain. `inject` only ever reads
the cache, so a build without `faber` still produces a complete site — panels
simply stay as the plain Latin block they started as.

Usage:
    locale-tabs.py render [--src src/en-US/cheatsheet]
    locale-tabs.py inject <dist_dir>
"""

from __future__ import annotations

import hashlib
import html as html_mod
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WORKSPACE = REPO.parent
CACHE = REPO / "generator" / "locale-tabs"

# Same order and notes as the landing hero, so the two surfaces teach the same
# axis in the same sequence.
LOCALES: list[dict[str, str]] = [
    {"id": "en", "name": "English", "script": "",
     "note": "English reader surface"},
    {"id": "la", "name": "Latin", "script": "",
     "note": "canonical Faber"},
    {"id": "th-TH", "name": "ภาษาไทย", "script": "th", "note": "Thai"},
    {"id": "zh-Hans", "name": "简体中文", "script": "zh",
     "note": "Simplified Chinese"},
    {"id": "zh-Hant", "name": "繁體中文", "script": "zh",
     "note": "Traditional Chinese"},
    {"id": "vi", "name": "Tiếng Việt", "script": "", "note": "Vietnamese"},
    {"id": "ar", "name": "العربية", "script": "ar", "note": "Arabic", "rtl": "1"},
    {"id": "hi", "name": "हिन्दी", "script": "hi", "note": "Hindi"},
]

# The Markdown source is Latin, and `la` is rendered through the formatter like
# every other surface rather than copied verbatim. The formatter normalises —
# `si … ergo x` becomes a block — so a verbatim base panel would be the one tab
# out of eight with a different shape, which reads as a difference between the
# languages instead of what it is.
BASE = "la"

# locales.md is already a side-by-side of every reader surface; wrapping its
# panels in another locale switcher would nest the same idea inside itself.
SKIP_FILES = {"locales.md"}

FENCE_RE = re.compile(r"^```faber([^\n]*)\n(.*?)^```", re.S | re.M)
BLOCK_RE = re.compile(
    r'<pre class="faber-code"><code class="lang-faber">(.*?)</code></pre>', re.S
)


def digest(source: str) -> str:
    return hashlib.sha256(source.encode("utf-8")).hexdigest()[:16]


def find_faber() -> str | None:
    for candidate in (
        WORKSPACE / "faber" / "target" / "release" / "faber",
        WORKSPACE / "faber" / "target" / "debug" / "faber",
    ):
        if candidate.is_file():
            return str(candidate)
    return shutil.which("faber")


def stage_packs(faber: str) -> bool:
    """Make reader packs resolvable beside the faber binary.

    `faber format --locale` looks for share/faber/locale/<X>/pack.toml relative
    to its own executable. A workspace build has no such directory, so every
    locale fails with a pack-not-found error and the transcode silently
    produces nothing. The packs themselves live in the radix tree; link them
    into place. This writes only inside faber/target/, which is build output.
    """
    src = WORKSPACE / "radix" / "stdlib" / "locale"
    if not src.is_dir():
        print(f"  no reader packs at {src}", file=sys.stderr)
        return False
    dest = Path(faber).resolve().parent.parent / "share" / "faber" / "locale"
    dest.mkdir(parents=True, exist_ok=True)
    linked = 0
    for pack in sorted(src.iterdir()):
        if not (pack / "pack.toml").is_file():
            continue
        link = dest / pack.name
        if not link.exists():
            link.symlink_to(pack, target_is_directory=True)
        linked += 1
    print(f"  reader packs available: {linked} at {dest}")
    return linked > 0


def transcode(faber: str, source: str, locale: str) -> str | None:
    tmp = CACHE / f".transcode-{locale}.fab"
    tmp.write_text(source, encoding="utf-8")
    try:
        proc = subprocess.run(
            [faber, "format", "--locale", locale, "--stdout", str(tmp)],
            text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        )
    finally:
        tmp.unlink(missing_ok=True)
    out = proc.stdout.strip()
    # A pack failure still exits 0 and prints warnings to stderr, so an empty
    # or unchanged body is the real signal that nothing was rendered.
    if proc.returncode != 0 or not out:
        return None
    return out


def cache_vocabularies() -> int:
    """Cache each reader pack's keyword spellings beside the panels.

    highlight-code.py paints keywords from the generated search indexes, but
    those carry Latin canonical terms — the en-US index has all of two
    localized spellings. So an English panel, the first tab most readers see,
    had its keywords left grey. The reader packs are the authority the compiler
    itself uses; cache their vocabulary here so the highlighter can read it
    without needing the radix tree at build time.
    """
    import tomllib

    src = WORKSPACE / "radix" / "stdlib" / "locale"
    written = 0
    for loc in LOCALES:
        pack = src / loc["id"] / "pack.toml"
        if not pack.is_file():
            continue
        with pack.open("rb") as handle:
            data = tomllib.load(handle)
        words = {
            str(v).strip()
            for section in ("keywords", "types", "primitives")
            for v in (data.get(section) or {}).values()
            if str(v).strip()
        }
        if not words:
            continue
        (CACHE / f"vocab.{loc['id']}.json").write_text(
            json.dumps(sorted(words), ensure_ascii=False), encoding="utf-8"
        )
        written += 1
    return written


def cmd_render(src_dir: Path) -> int:
    faber = find_faber()
    if faber is None:
        print("ERROR: no faber binary found; cannot transcode", file=sys.stderr)
        return 1
    print(f"  toolchain: {faber}")
    CACHE.mkdir(parents=True, exist_ok=True)
    if not stage_packs(faber):
        return 1

    wanted: set[str] = set()
    rendered = failed = 0

    for md in sorted(src_dir.glob("*.md")):
        if md.name in SKIP_FILES:
            continue
        text = md.read_text(encoding="utf-8")
        for match in FENCE_RE.finditer(text):
            info, body = match.group(1), match.group(2).rstrip()
            # A fence that already names a locale, or is package-scoped, is not
            # a plain Latin teaching example.
            if "locale=" in info or "mode=package" in info:
                continue
            key = digest(body)
            wanted.add(key)
            for loc in LOCALES:
                out = CACHE / f"{key}.{loc['id']}.fab"
                if out.is_file():
                    continue
                result = transcode(faber, body, loc["id"])
                if result is None:
                    print(f"  {md.name} {key} {loc['id']}: no rendering",
                          file=sys.stderr)
                    failed += 1
                    continue
                out.write_text(result + "\n", encoding="utf-8")
                rendered += 1

    vocabs = cache_vocabularies()

    stale = 0
    for cached in CACHE.glob("*.fab"):
        if cached.name.split(".")[0] not in wanted:
            cached.unlink()
            stale += 1

    print(f"  locale-tabs: {len(wanted)} examples, {rendered} panels rendered, "
          f"{failed} unavailable, {stale} stale removed, {vocabs} vocabularies")
    return 0


def esc(s: str) -> str:
    return html_mod.escape(s)


def card(key: str, index: int) -> str | None:
    panels = []
    for loc in LOCALES:
        path = CACHE / f"{key}.{loc['id']}.fab"
        if not path.is_file():
            continue
        panels.append((loc, path.read_text(encoding="utf-8").rstrip()))
    # One surface alone is just the code block it already was.
    if len(panels) < 2:
        return None

    root = f"lt-{key}-{index}"
    tabs = bodies = ""
    for i, (loc, body) in enumerate(panels):
        pid = f"{root}-p-{loc['id']}"
        label = (f'<span class="{loc["script"]}">{esc(loc["name"])}</span>'
                 if loc["script"] else esc(loc["name"]))
        tabs += (
            f'<button class="fdt-tab" role="tab" id="{root}-t-{loc["id"]}" '
            f'data-panel="{pid}" data-name="{esc(loc["name"])}" '
            f'aria-controls="{pid}" title="{esc(loc["id"])}" '
            f'aria-selected="{"true" if i == 0 else "false"}" '
            f'tabindex="{"0" if i == 0 else "-1"}">{label}</button>'
        )
        script_class = f' class="{loc["script"]}"' if loc["script"] else ""
        direction = ' dir="rtl"' if loc.get("rtl") else ""
        bodies += (
            f'<div class="fdt-panel{" active" if i == 0 else ""}" id="{pid}" '
            f'role="tabpanel" aria-labelledby="{root}-t-{loc["id"]}">'
            f'<div class="fdt-panel-label"><code>faber format --locale '
            f'{esc(loc["id"])}</code> <span class="fdt-note">— '
            f'{esc(loc["note"])}</span></div>'
            f'<pre{script_class}{direction}>'
            f'<code class="lang-faber locale={esc(loc["id"])}">{esc(body)}'
            f'</code></pre></div>'
        )

    return (
        '<div class="faber-demo-tabs" data-fdt>'
        '<div class="fdt-bar">'
        '<span class="fdt-mark" aria-hidden="true">f</span>'
        '<span class="fdt-file">reader locale</span>'
        '<button class="fdt-copy" type="button">Copy</button>'
        '</div>'
        f'<div class="fdt-tabs" role="tablist" aria-label="Reader locale">{tabs}</div>'
        f'{bodies}</div>'
    )


def cmd_inject(dist: Path) -> int:
    target = dist / "en-US" / "cheatsheet"
    if not target.is_dir():
        print(f"  locale-tabs: no {target}, nothing to inject")
        return 0
    if not CACHE.is_dir():
        print("  locale-tabs: no cache, panels left as plain blocks")
        return 0

    pages = swapped = 0
    for page in sorted(target.glob("*.html")):
        if page.stem + ".md" in SKIP_FILES:
            continue
        text = page.read_text(encoding="utf-8")
        counter = {"n": 0}

        def replace(match: re.Match) -> str:
            body = html_mod.unescape(match.group(1)).rstrip()
            built = card(digest(body), counter["n"])
            if built is None:
                return match.group(0)
            counter["n"] += 1
            return built

        updated = BLOCK_RE.sub(replace, text)
        if counter["n"]:
            page.write_text(updated, encoding="utf-8")
            pages += 1
            swapped += counter["n"]

    print(f"  [locale-tabs] {swapped} example(s) across {pages} page(s)")
    return 0


def main() -> int:
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "render":
        src = Path(sys.argv[2]) if len(sys.argv) > 2 else REPO / "src" / "en-US" / "cheatsheet"
        return cmd_render(src)
    if cmd == "inject":
        if len(sys.argv) < 3:
            print("Usage: locale-tabs.py inject <dist_dir>", file=sys.stderr)
            return 1
        return cmd_inject(Path(sys.argv[2]))
    print(__doc__)
    return 1


if __name__ == "__main__":
    sys.exit(main())
