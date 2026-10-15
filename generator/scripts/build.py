#!/usr/bin/env python3
"""Build the faberlang.dev site: `src/en-US` + `static/` + pinned radix inputs -> `dist/`.

One process owns the whole build. Per-page work (staleness, reader-locale
conversion, rendering) runs in-process; only the generators and presentation
passes that already operate on whole trees are spawned. Every output carries
the fingerprint of its inputs in `generator/target/build-manifest.json`, so a
second build with nothing changed renders nothing and an edit to one page
renders that page.

Usage:
    build.py                          incremental build against the pinned radix
    build.py --full                   wipe dist and the manifest, rebuild everything
    build.py --refresh-upstream [REV] re-pin radix (default HEAD), refresh the
                                      explain snapshot and the agent reference,
                                      regenerate everything derived from them

Fallbacks are never silent: each one is recorded in the manifest and in
`generator/target/build-receipt.json`, and the build fails on any that
`generator/degraded.allow.toml` does not list with a reason.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

import corpus_build  # noqa: E402
import diagrams  # noqa: E402
import locales_registry  # noqa: E402
import receipt  # noqa: E402
import speculum_py  # noqa: E402
import upstream  # noqa: E402
from localize import Converter, Localizer  # noqa: E402

GENERATOR = SCRIPTS.parent
REPO = GENERATOR.parent
SRC = REPO / "src" / "en-US"
STATIC = REPO / "static"
DIST = REPO / "dist"
TARGET = GENERATOR / "target"
MANIFEST_PATH = TARGET / "build-manifest.json"
ALLOWLIST_PATH = GENERATOR / "degraded.allow.toml"
RECEIPT_PATH = TARGET / "build-receipt.json"
EXPLAIN_SNAPSHOT = upstream.EXPLAIN_SNAPSHOT

SITE = "en-US"
STYLESHEET = "/speculum.css"
BASE_URL = "https://faberlang.dev"
PYTHON = sys.executable

# Every file whose change can alter a rendered authored page. Listed once; a
# page is stale when any of these or its source or the pinned locale pack move.
PAGE_TOOLCHAIN = [
    "speculum_py.py", "project_reader_terms.py", "localize.py", "receipt.py",
    "locales_registry.py", "site_assets.py", "agent_pass.py",
    "strip-empty-sources.py", "inject-skip-link.py", "inject-chrome.py",
    "localize-spans.py", "highlight-code.py", "matrix-cells.py", "inject-toc.py",
    "tag-glyph-chips.py", "inject-pass.py", "grammar-toggle.py", "diagrams.py",
    "locale-tabs.py",
]
PAGE_DATA = [
    GENERATOR / "www" / "speculum.css",
    GENERATOR / "locales.toml",
    GENERATOR / "locales" / SITE / "chrome.toml",
    GENERATOR / "locale-tabs",
    GENERATOR / "diagrams",
]
CORPUS_TOOLCHAIN = PAGE_TOOLCHAIN + ["corpus_build.py", "corpus_ia.py", "corpus_locale.py", "agent_reference.py"]
CORPUS_DATA = PAGE_DATA + [GENERATOR / "corpus-categories.toml", EXPLAIN_SNAPSHOT]

# Presentation passes over a stage tree, in order. `{tree}` is the stage root.
PAGE_PASSES = [
    ["strip-empty-sources.py", "{tree}"],
    ["inject-skip-link.py", "{tree}"],
    ["inject-chrome.py", "{tree}", SITE],
    ["diagrams.py", "inject", "{tree}"],
    ["locale-tabs.py", "inject", "{tree}"],
    ["localize-spans.py", "{tree}"],
    ["highlight-code.py", "{tree}"],
    ["matrix-cells.py", "{tree}"],
    ["inject-toc.py", "{tree}"],
    ["tag-glyph-chips.py", "{tree}"],
]
AUTHORED_ONLY_PASSES = [["inject-pass.py", "{tree}"]]


class BuildError(RuntimeError):
    pass


# --------------------------------------------------------------------------
# Manifest: output -> {inputs fingerprint, output sha, degradations}
# --------------------------------------------------------------------------

class Manifest:
    def __init__(self, path: Path):
        self.path = path
        try:
            data = json.loads(path.read_text())
            self.entries: dict = data if isinstance(data, dict) else {}
        except (OSError, ValueError):
            self.entries = {}
        self._hashes: dict[Path, str] = {}

    def sha(self, path: Path) -> str:
        cached = self._hashes.get(path)
        if cached is None:
            digest = hashlib.sha256()
            with path.open("rb") as stream:
                for chunk in iter(lambda: stream.read(1 << 20), b""):
                    digest.update(chunk)
            cached = self._hashes[path] = digest.hexdigest()
        return cached

    def forget(self, path: Path) -> None:
        self._hashes.pop(path, None)

    def fingerprint(self, inputs) -> dict[str, str]:
        """Path (file: content hash; directory: every file's hash), or a
        `(key, value)` pair for a virtual input such as a pinned tree id."""
        result: dict[str, str] = {}
        for item in inputs:
            if isinstance(item, tuple):
                result[f"virtual:{item[0]}"] = str(item[1])
                continue
            path = Path(item)
            if path.is_dir():
                for child in sorted(p for p in path.rglob("*") if p.is_file()):
                    result[str(child)] = self.sha(child)
            elif path.is_file():
                result[str(path)] = self.sha(path)
            else:
                result[str(path)] = "MISSING"
        return result

    def current(self, key: str, inputs, outputs: list[Path], check_output_hash: bool = False) -> bool:
        entry = self.entries.get(key)
        if not entry or entry.get("inputs") != self.fingerprint(inputs):
            return False
        if not all(p.is_file() for p in outputs):
            return False
        if check_output_hash:
            return entry.get("output") == self.sha(outputs[0])
        return True

    def record(self, key: str, inputs, outputs: list[Path], degraded: list[dict] | None = None) -> None:
        for path in outputs:
            self.forget(path)
        entry = {"inputs": self.fingerprint(inputs), "degraded": degraded or []}
        if outputs and outputs[0].is_file():
            entry["output"] = self.sha(outputs[0])
            try:
                entry["path"] = str(outputs[0].relative_to(REPO))
            except ValueError:
                entry["path"] = str(outputs[0])
        self.entries[key] = entry

    def refresh_outputs(self) -> None:
        """Re-hash recorded outputs: later passes (canonical tags) may touch them."""
        for entry in self.entries.values():
            path = REPO / entry["path"] if entry.get("path") else None
            if path is not None and path.is_file():
                self.forget(path)
                entry["output"] = self.sha(path)

    def degradations(self) -> list[dict]:
        events = []
        for key, entry in sorted(self.entries.items()):
            for event in entry.get("degraded", []):
                events.append({**event, "output": key})
        return events

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.path.with_suffix(".tmp")
        tmp.write_text(json.dumps(self.entries, sort_keys=True, indent=1) + "\n")
        tmp.replace(self.path)


def listing(directory: Path) -> tuple[str, str]:
    """Virtual input: the set of file paths under a directory, not their bytes."""
    names = sorted(str(p.relative_to(directory)) for p in directory.rglob("*") if p.is_file()) \
        if directory.is_dir() else []
    return (f"listing:{directory.relative_to(REPO)}", hashlib.sha256("\n".join(names).encode()).hexdigest())


# --------------------------------------------------------------------------
# Subprocess helpers
# --------------------------------------------------------------------------

def run_script(script: str, *args: str, label: str | None = None, quiet: bool = False) -> list[dict]:
    """Run one generator script; return the DEGRADED events it reported."""
    cmd = [PYTHON, str(SCRIPTS / script), *map(str, args)]
    proc = subprocess.run(cmd, capture_output=True, text=True, cwd=str(REPO))
    events = []
    passthrough = []
    for line in proc.stderr.splitlines():
        event = receipt.parse_line(line)
        if event:
            events.append(event)
        elif line.strip():
            passthrough.append(line)
    if proc.returncode != 0:
        tail = "\n".join((proc.stdout.splitlines() + passthrough)[-12:])
        raise BuildError(f"{script} {' '.join(map(str, args))} failed (exit {proc.returncode})\n{tail}")
    if not quiet:
        for line in proc.stdout.splitlines()[-3:]:
            if line.strip():
                print(f"    {line.strip()}")
    for line in passthrough[-5:]:
        print(f"    ! {line.strip()[:200]}")
    return events


# --------------------------------------------------------------------------
# The build
# --------------------------------------------------------------------------

class Build:
    def __init__(self, full: bool, refresh: bool, faber: str | None, jobs: int):
        self.full = full
        self.refresh = refresh
        self.jobs = jobs
        self.started = time.monotonic()
        self.faber_arg = faber
        self.manifest = Manifest(MANIFEST_PATH)
        self.trees = upstream.tree_ids()
        self.timings: list[tuple[str, float]] = []
        self.rebuilt: dict[str, int] = {}

    # -- helpers ---------------------------------------------------------
    def timed(self, name: str):
        build = self

        class _Timer:
            def __enter__(self):
                self.t = time.monotonic()

            def __exit__(self, *exc):
                build.timings.append((name, time.monotonic() - self.t))

        return _Timer()

    def tool(self, names: list[str]) -> list[Path]:
        return [SCRIPTS / n for n in names]

    def pin(self, *names: str) -> list[tuple[str, str]]:
        return [(f"radix:{n}", self.trees[n]) for n in names]

    def step(self, name: str, script: str, args: list, *, inputs: list, outputs: list[Path],
             force: bool = False) -> None:
        """Run a whole-tree generator when its declared inputs changed."""
        key = f"step:{name}"
        inputs = [SCRIPTS / script, *inputs]
        if not (self.full or force) and self.manifest.current(key, inputs, outputs):
            print(f"  = {name}")
            return
        print(f"  ↻ {name}")
        t0 = time.monotonic()
        events = run_script(script, *args, quiet=True)
        self.manifest.record(key, inputs, outputs, events)
        self.rebuilt[name] = 1
        self.timings.append((f"step {name}", time.monotonic() - t0))

    # -- phases ----------------------------------------------------------
    def prepare_environment(self) -> None:
        self.faber = self.faber_arg or shutil.which("faber")
        if not self.faber:
            raise BuildError("no faber binary on PATH; pass --faber")
        self.reader = locales_registry.reader_locale(locales_registry.load_registry(), SITE)
        upstream.materialize()
        self.converter = Converter(self.faber, self.reader, self.trees["locale"], TARGET / "convert-cache")
        self.localizer = Localizer(
            self.converter, upstream.radix_root() / "locale" / self.reader / "pack.toml"
        )
        print(f"faber {self.converter.stamp.split('|')[0]} · radix {read_pin_commit()[:10]} "
              f"· reader {self.reader}")

    def refresh_upstream(self, rev: str) -> None:
        commit, trees = upstream.resolve_rev(rev)
        explain_faber = self.faber_arg or radix_dev_binary() or shutil.which("faber")
        if not explain_faber:
            raise BuildError("no faber binary for `faber explain`; pass --faber")
        listing_text = subprocess.run(
            [explain_faber, "explain", "--list"], capture_output=True, text=True, timeout=120,
        )
        if listing_text.returncode != 0 or not listing_text.stdout.strip():
            raise BuildError(f"{explain_faber} explain --list failed: {listing_text.stderr.strip()[:300]}")
        from localize import faber_version

        upstream.write_lock(commit, trees, faber_version(explain_faber))
        EXPLAIN_SNAPSHOT.parent.mkdir(parents=True, exist_ok=True)
        EXPLAIN_SNAPSHOT.write_text(listing_text.stdout, encoding="utf-8")
        self.trees = upstream.tree_ids()
        upstream.materialize()
        print(f"pinned radix {commit[:10]}: " + ", ".join(f"{k} {v[:10]}" for k, v in trees.items()))
        print("  agent reference …")
        events = run_script("generate-agent-reference.py", "--faber", explain_faber, "--strict", quiet=True)
        outputs = [REPO / "static" / "agents" / "reference" / "index.md"]
        self.manifest.record("step:agent-reference", [SCRIPTS / "generate-agent-reference.py",
                                                      *self.pin("locale"), EXPLAIN_SNAPSHOT], outputs, events)

    def generators(self) -> None:
        """Pages assembled from pinned radix inputs and captured panels."""
        g = GENERATOR
        self.step("target-matrix", "generate-target-matrix.py", ["--locale", SITE],
                  inputs=[*self.pin("grammar"), g / "locales" / SITE / "targets.toml"],
                  outputs=[SRC / "toolchain" / "target-matrix.md"], force=self.refresh)
        self.step("target-lanes", "generate-target-lanes.py", ["--output-dir", SRC / "targets"],
                  inputs=[*self.pin("grammar"), g / "target-panels", g / "lanes"],
                  outputs=[SRC / "targets" / "index.md"], force=self.refresh)
        self.step("localization", "generate-localization.py", ["--output", SRC / "localization.md"],
                  inputs=[g / "locales.toml", g / "landing" / "locales"],
                  outputs=[SRC / "localization.md"])
        self.step("overview", "generate-overview.py", ["--output", SRC / "language" / "overview.md"],
                  inputs=[g / "landing"], outputs=[SRC / "language" / "overview.md"])
        self.step("grammar", "generate-grammar.py", ["--locale", SITE],
                  inputs=[*self.pin("grammar", "locale")], outputs=[SRC / "reference" / "grammar.md"],
                  force=self.refresh)
        self.step("agent-locales", "generate-agent-locales.py", ["--strict"],
                  inputs=[SCRIPTS / "agent_locales.py", *self.pin("locale")],
                  outputs=[STATIC / "agents" / "locales.md"], force=self.refresh)
        self.step("locale-reference", "generate-locale-reference.py", ["--check"],
                  inputs=[*self.pin("locale"), g / "locale-captures", g / "locale-tabs"],
                  outputs=[SRC / "language" / "locales" / "keywords.md"], force=self.refresh)

    def grammar_tree(self) -> None:
        """Needs the rendered corpus (term links), so it runs after it."""
        self.step("grammar-tree", "generate-grammar-tree.py", [],
                  inputs=[*self.pin("grammar", "locale"), listing(DIST / SITE / "corpus")],
                  outputs=[SRC / "reference" / "grammar" / "program.md",
                           STATIC / "agents" / "grammar" / "productions.md"], force=self.refresh)

    def copy_static(self) -> None:
        copied = 0
        for path in sorted(STATIC.rglob("*")):
            if not path.is_file():
                continue
            dest = DIST / path.relative_to(STATIC)
            if dest.is_file() and dest.read_bytes() == path.read_bytes():
                continue
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, dest)
            copied += 1
        css = DIST / "speculum.css"
        source = GENERATOR / "www" / "speculum.css"
        if not css.is_file() or css.read_bytes() != source.read_bytes():
            shutil.copy2(source, css)
            copied += 1
        print(f"  static: {copied} file(s) updated")

    def passes(self, tree: Path, authored: bool) -> None:
        sequence = PAGE_PASSES + (AUTHORED_ONLY_PASSES if authored else [])
        for spec in sequence:
            args = [a.replace("{tree}", str(tree)) for a in spec[1:]]
            run_script(spec[0], *args, quiet=True)
        grammar = tree / SITE / "reference" / "grammar.html"
        if authored and grammar.is_file():
            run_script("grammar-toggle.py", tree / SITE / "reference", quiet=True)

    def corpus(self) -> None:
        inputs = [*self.tool(CORPUS_TOOLCHAIN), *CORPUS_DATA, *self.pin("corpus", "locale"),
                  ("faber", self.converter.stamp)]
        sentinel = DIST / SITE / "corpus" / "index.html"
        if not self.full and not self.refresh and self.manifest.current(
                "corpus", inputs, [sentinel], check_output_hash=True):
            print("  = corpus")
            return
        print("  ↻ corpus")
        t0 = time.monotonic()
        stage = TARGET / "corpus-stage"
        if stage.exists():
            shutil.rmtree(stage)
        (stage / SITE).mkdir(parents=True)
        receipt.drain()
        stats = corpus_build.build(
            corpus=upstream.radix_root() / "corpus",
            reader_root=upstream.radix_root() / "locale",
            output=stage / SITE, generator_dir=GENERATOR, site_locale=SITE,
            reader_locale=self.reader, stylesheet=STYLESHEET,
            explain_text=EXPLAIN_SNAPSHOT.read_text(encoding="utf-8"),
            converter=self.converter,
        )
        events = receipt.drain()
        self.passes(stage, authored=False)
        target = DIST / SITE / "corpus"
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(stage / SITE / "corpus", target)
        shutil.rmtree(stage)
        self.manifest.record("corpus", inputs, [sentinel], events)
        self.rebuilt["corpus"] = stats["terms"]
        self.timings.append(("corpus", time.monotonic() - t0))
        print(f"    {stats['terms']} terms, {stats['aliases']} aliases, "
              f"{stats['anatomy_pages']} anatomy pages")

    def authored_pages(self) -> None:
        toolchain = [*self.tool(PAGE_TOOLCHAIN), *PAGE_DATA, *self.pin("locale"),
                     ("faber", self.converter.stamp)]
        stage = TARGET / "page-stage"
        if stage.exists():
            shutil.rmtree(stage)
        stage.mkdir(parents=True)
        pending = []
        for md in sorted(SRC.rglob("*.md")):
            rel = md.relative_to(SRC)
            out = DIST / SITE / rel.with_suffix(".html")
            key = f"{SITE}/{rel.with_suffix('.html')}"
            if not self.full and self.manifest.current(key, [md, *toolchain], [out],
                                                       check_output_hash=True):
                continue
            pending.append((md, rel, key, out))
        receipt.drain()

        def render(item):
            md, rel, key, out = item
            iter_ = str(rel.with_suffix(""))
            text = md.read_text(encoding="utf-8")
            localized = self.localizer.localize_page(text, str(rel))
            html = speculum_py.genera(localized, iter_, SITE, self.reader, STYLESHEET)
            staged = stage / SITE / rel.with_suffix(".html")
            staged.parent.mkdir(parents=True, exist_ok=True)
            staged.write_bytes((html + "\n").encode("utf-8"))
            return item

        if pending:
            with concurrent.futures.ThreadPoolExecutor(max_workers=self.jobs) as pool:
                for item in pool.map(render, pending):
                    print(f"  ↻ {item[1].with_suffix('.html')}")
            events = receipt.drain()
            by_page: dict[str, list[dict]] = {}
            for event in events:
                by_page.setdefault(event["subject"], []).append(event)
            self.passes(stage, authored=True)
            for md, rel, key, out in pending:
                staged = stage / SITE / rel.with_suffix(".html")
                out.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(staged, out)
                self.manifest.record(key, [md, *toolchain], [out], by_page.get(str(rel), []))
        shutil.rmtree(stage, ignore_errors=True)
        self.rebuilt["pages"] = len(pending)
        print(f"  {len(pending)} authored page(s) rendered")

    def derived_surfaces(self) -> None:
        corpus = upstream.radix_root() / "corpus"
        pins = self.pin("corpus", "locale")
        self.step("llms-full", "render-llms.py",
                  ["--corpus", corpus, "--output", DIST / "llms-full.txt"],
                  inputs=[SCRIPTS / "corpus_locale.py", *pins], outputs=[DIST / "llms-full.txt"])
        self.step("search-index", "generate-search-index.py",
                  ["--corpus", corpus, "--output-dir", DIST, "--locale", SITE],
                  inputs=[SCRIPTS / "corpus_locale.py", *pins],
                  outputs=[DIST / "search-index.json", DIST / "search-index.en-US.json"])
        self.step("ia-redirects", "ia-redirects.py", ["stubs"], inputs=[],
                  outputs=[DIST / SITE / "start" / "install.html"])
        self.step("retired-locales", "retired-locales.py",
                  ["stubs", "--dist", DIST],
                  inputs=[GENERATOR / "redirects" / "retired-locales.toml"],
                  outputs=[DIST / "ar" / "404.html"])
        self.step("root-redirects", "generate-redirects.py", [DIST, SITE],
                  inputs=[listing(DIST / SITE), SCRIPTS / "ia-redirects.py"],
                  outputs=[DIST / "start" / "install.html"])
        self.step("landing", "generate-landing.py", [DIST / "index.html"],
                  inputs=[GENERATOR / "landing", SCRIPTS / "site_assets.py", SCRIPTS / "agent_pass.py",
                          GENERATOR / "locales" / SITE / "chrome.toml", *self.pin("grammar")],
                  outputs=[DIST / "index.html"])
        (DIST / "porta").mkdir(parents=True, exist_ok=True)
        self.step("portal", "generate-portal.py", [DIST / "porta" / "index.html"],
                  inputs=[GENERATOR / "portal", GENERATOR / "locales.toml", *self.pin("locale")],
                  outputs=[DIST / "porta" / "index.html"])

    def diagram_cache(self) -> None:
        """A mermaid fence with no cached SVG is a degradation, not a network call."""
        sources = diagrams.collect_sources([SRC])
        missing = [key for key in sources if not diagrams.cache_path(key).exists()]
        for key in missing:
            receipt.degraded("diagram-uncached", key,
                             "no cached SVG; run `diagrams.py render` (installs node deps)")
        self.manifest.entries["diagram-cache"] = {
            "inputs": {}, "degraded": receipt.drain(),
        }
        print(f"  {len(sources)} diagram(s), {len(missing)} uncached")

    def gates(self) -> None:
        checks = [
            ("width", ["check-width-gate.py"]),
            ("links", ["check-internal-links.py", str(DIST)] + sum(
                [["--allow-missing", f"/en-US/language/locales/{loc}.html"]
                 for loc in ("ar", "hi", "th-TH", "vi", "zh-Hans", "zh-Hant")], [])),
            ("retired-locales", ["retired-locales.py", "check", "--dist", str(DIST)]),
            ("leakage", ["check-leakage-gate.py", str(DIST)]),
            ("frontmatter-leak", ["check-frontmatter-leak.py", str(DIST)]),
        ]
        failures = []

        def run(item):
            name, argv = item
            proc = subprocess.run([PYTHON, str(SCRIPTS / argv[0]), *argv[1:]],
                                  capture_output=True, text=True, cwd=str(REPO))
            return name, proc

        with concurrent.futures.ThreadPoolExecutor(max_workers=len(checks)) as pool:
            for name, proc in pool.map(run, checks):
                if proc.returncode != 0:
                    failures.append(f"{name}: " + "\n".join((proc.stdout + proc.stderr).strip().splitlines()[-15:]))
        if failures:
            raise BuildError("gate failure\n" + "\n".join(failures))
        self.step("sitemap", "generate-sitemap.py", [DIST, BASE_URL],
                  inputs=[listing(DIST / SITE)], outputs=[DIST / "sitemap.xml"])
        run_script("inject-canonical.py", DIST, BASE_URL, quiet=True)
        smoke_failures = smoke(DIST, current_release())
        if smoke_failures:
            raise BuildError("smoke checks failed\n" + "\n".join(smoke_failures))

    # -- receipt ---------------------------------------------------------
    def finish(self) -> bool:
        for key in list(self.manifest.entries):
            if key.startswith(("step:", "corpus", "diagram-cache")):
                continue
            if not (DIST / key).is_file():
                del self.manifest.entries[key]
        self.manifest.refresh_outputs()
        self.manifest.save()
        allow = receipt.Allowlist(ALLOWLIST_PATH)
        events = self.manifest.degradations()
        blocked = [e for e in events if not allow.covers(e)]
        # A plain --full cannot reproduce what only --refresh-upstream produces.
        stale_allow = [
            entry for entry in allow.unused()
            if (self.full or self.refresh)
            and (self.refresh or not entry["kind"].startswith("agent-reference"))
        ]
        RECEIPT_PATH.parent.mkdir(parents=True, exist_ok=True)
        RECEIPT_PATH.write_text(json.dumps({
            "degraded": events, "blocked": blocked, "rebuilt": self.rebuilt,
            "timings": [[n, round(t, 2)] for n, t in self.timings],
            "seconds": round(time.monotonic() - self.started, 2),
        }, indent=1) + "\n")
        pages = len(list(DIST.rglob("*.html")))
        print(f"\n=== {pages} HTML pages · {len(events)} degraded "
              f"({len(events) - len(blocked)} allowed, {len(blocked)} blocked) "
              f"· {time.monotonic() - self.started:.1f}s ===")
        for event in blocked[:25]:
            print(f"  BLOCKED {event['kind']} {event['subject']}: {event['detail']}")
        if len(blocked) > 25:
            print(f"  … and {len(blocked) - 25} more (see {RECEIPT_PATH.relative_to(REPO)})")
        for entry in stale_allow:
            print(f"  STALE ALLOW {entry['kind']} {entry['subject']}: nothing matches it any more")
        return not blocked and not stale_allow


# --------------------------------------------------------------------------
# Smoke checks (the shipped bytes)
# --------------------------------------------------------------------------

def current_release() -> str:
    text = (STATIC / "install.md").read_text(encoding="utf-8")
    match = re.search(r"(?m)^Current release: Faber (.*)\.$", text)
    if not match:
        raise BuildError("could not read the current release from static/install.md")
    return match.group(1)


def smoke(dist: Path, release: str) -> list[str]:
    failures: list[str] = []
    cache: dict[Path, str] = {}

    def contains(rel: str, needle: str, label: str) -> None:
        path = dist / rel
        if path not in cache:
            cache[path] = path.read_text(encoding="utf-8") if path.is_file() else ""
        text = cache[path]
        if not path.is_file():
            failures.append(f"missing {label}: {rel}")
        elif needle not in text and needle not in re.sub(r"<[^>]*>", "", text):
            failures.append(f"{label}: {needle!r} not in {rel}")

    def absent(rel: str, needle: str, label: str) -> None:
        path = dist / rel
        if path.is_file() and needle in path.read_text(encoding="utf-8"):
            failures.append(f"{label}: {needle!r} present in {rel}")

    en = "en-US"
    contains(f"{en}/index.html", "<!DOCTYPE html>", "home doctype")
    contains(f"{en}/index.html", "/llms.txt", "home agent link")
    contains("llms-full.txt", "Generated corpus frontmatter reference", "llms-full surface")
    contains("llms.txt", "https://faberlang.dev/install.md", "llms.txt install pointer")
    contains("install.md", f"Current release: Faber {release}.", "install lobby version")
    contains(".well-known/agent-skills/install/SKILL.md", f"faber-v{release}", "install skill release link")
    contains(".well-known/agent-skills/index.json", f'"version": "{release}"', "skill catalog version")
    contains(f"{en}/start/install.html", "url=/en-US/start/", "retired install page redirects")
    contains(f"{en}/cheatsheet/commands.html", "faber check", "cheat sheet commands")
    contains(f"{en}/cheatsheet/index.html", "Cheat sheet", "cheat sheet index")
    contains(f"{en}/cheatsheet/errors.html", "error channel", "cheat sheet errors")
    contains(f"{en}/examples/index.html", "url=/en-US/cheatsheet/", "examples index redirect")
    contains(f"{en}/examples/cat.html", "url=/en-US/cheatsheet/", "example page redirect")
    contains("examples/cat.html", "url=/en-US/examples/cat.html", "root example stub")
    contains(f"{en}/targets/index.html", "Target lanes", "target lanes index")
    contains(f"{en}/404.html", "404", "404 page")
    contains(f"{en}/releases/index.html", f"Faber {release}", "releases index")
    contains(f"{en}/releases/faber-1.4.0.html", "faber-v1.4.0", "pinned release page")
    contains(f"{en}/releases/radix-0.79.0.html", "Release notes", "release notes imported")
    matrix = f"{en}/toolchain/target-matrix.html"
    contains(matrix, "Target compatibility", "targets matrix title")
    contains(matrix, "table-scroll", "targets matrix scroll wrap")
    contains(matrix, "Application lane", "targets HIR summary")
    contains(matrix, "Systems lane", "targets MIR summary")
    contains(f"{en}/index.html", "/toolchain/target-matrix.html", "sidebar target matrix link")
    contains("robots.txt", "Sitemap:", "robots.txt")
    contains("robots.txt", "Allow: /", "robots allow all")
    if (dist / "robots.txt").is_file() and re.search(
            r"(?m)^Disallow: /(ar|th-TH|vi|hi|zh-Hans|zh-Hant)/", (dist / "robots.txt").read_text()):
        failures.append("robots.txt must not disallow locale trees")
    contains("search-index.json", '"t":"redde"', "search index dataset")
    contains("search-index.en-US.json", '"d":"fn"', "search index English slugs")
    contains(f"{en}/corpus/fn.html", "<title>fn — Faber</title>", "localized corpus fn page")
    contains(f"{en}/corpus/functio.html", "url=/en-US/corpus/fn.html", "latin corpus identity redirect")
    for section in ("language", "toolchain", "libraries", "reference"):
        contains(f"{en}/{section}/index.html", "<!DOCTYPE html>", f"{section} index")
    contains(f"{en}/language/index.html", "saturate", "language index shows code")
    for lib in ("norma", "triga", "gradus", "tela", "inferentia"):
        contains(f"{en}/libraries/{lib}.html", "<!DOCTYPE html>", f"library page {lib}")
        contains(f"{en}/libraries/index.html", f"/libraries/{lib}.html", f"libraries index links {lib}")
        contains(f"{en}/index.html", f"/en-US/libraries/{lib}.html", f"sidebar library link {lib}")
    contains(f"{en}/libraries/tela.html", "html_view", "Tela page shows the serializer")
    contains(f"{en}/libraries/inferentia.html", "/generate", "Inferentia page lists the API")
    # `functio` is the Latin spelling of `fn`: it in an en-US body means the
    # transcode step was skipped and English readers decode Latin keywords.
    contains(f"{en}/language/index.html", "fn saturate", "en-US renders English keywords")
    contains(f"{en}/language/types.html", "const int", "en-US types page in English")
    contains(f"{en}/toolchain/index.html", "faber check", "toolchain index shows commands")
    contains(f"{en}/syntax/types.html", 'http-equiv="refresh"', "retired syntax path redirects")
    contains(f"{en}/index.html", "data-search", "renderbar searchbox")
    contains(f"{en}/index.html", "faber-search.js", "search script include")

    landing = "index.html"
    for needle, label in [
        ('class="landing"', "landing body class"),
        ("Written by models,", "landing headline"),
        ("Built for models to write", "landing LLM-first section"),
        ("A mechanical grammar", "landing grammar point"),
        ("Explicit static and generic types", "landing typing point"),
        ("Math-oriented operators", "landing operators point"),
        ("Start in your own language", "landing locale section"),
        ("Write it once. Put it in the project you already have.", "landing cross-compile section"),
        ("Libraries written in Faber", "landing libraries section"),
        ("device inference is not shipped", "landing inference bound"),
        ("fail-closed", "landing device fail-closed bound"),
        ('href="/en-US/language/locales/la.html"', "landing Latin mapping door"),
        ('href="/en-US/"', "landing English docs door"),
        ("let Span bytes ← Span { low = 0.0, high = 255.0 }", "landing English reader panel"),
        ("sit Span bytes ← Span { low = 0.0, high = 255.0 }", "landing Latin reader panel"),
        ("ภาษาไทย", "landing Thai reader panel"),
        ("÷ 2.0", "landing demo shows true division"),
        ("pub struct Span", "landing Rust target panel"),
        ("class Span {", "landing TypeScript/Swift target panel"),
        ("type Span struct", "landing Go target panel"),
        ("radix emit --target swift", "landing Swift target panel"),
        ("<code>faber targets</code>", "landing capability table source"),
        ("grammar productions", "landing grammar size"),
        ("triga-budapest.png", "landing Triga frame"),
        ('href="/porta/"', "landing portal link"),
        ("faber-instrument.js", "landing instrument script include"),
        ('class="channel" href="/install.md"', "landing agent pass install link"),
    ]:
        contains(landing, needle, label)
    for locale in ("ar", "hi", "th-TH", "vi", "zh-Hans", "zh-Hant"):
        door = f'href="/en-US/language/locales/{locale}.html"'
        contains(landing, door, f"landing mapping door {locale}")
        contains("porta/index.html", door, f"portal mapping door {locale}")
    for lib in ("Norma", "Gradus", "Triga", "Tela", "Inferentia", "Cista"):
        contains(landing, f"<strong>{lib}</strong>", f"landing library {lib}")
    landing_text = (dist / landing).read_text(encoding="utf-8") if (dist / landing).is_file() else ""
    if re.search(r'fl-loc-t-en[^>]*>English', landing_text) and re.search(
            r'fl-loc-p-en[^>]*>.*functio ', landing_text):
        failures.append("landing English reader panel is rendering Latin")
    for frame in ("triga-budapest", "triga-terrain", "triga-geometries"):
        path = dist / "images" / f"{frame}.png"
        if not path.is_file() or path.stat().st_size == 0:
            failures.append(f"landing frame asset missing: images/{frame}.png")
    absent(landing, 'http-equiv="refresh"', "landing must not meta-refresh")
    for needle, label in [
        ('class="porta"', "portal body class"), ("ภาษาไทย", "portal Thai native"),
        ("العربية", "portal Arabic native"), ("简体中文", "portal zh-Hans native"),
        ('href="/en-US/"', "portal en-US link"), ("faber-instrument.js", "portal instrument script include"),
    ]:
        contains("porta/index.html", needle, label)
    contains("faber-instrument.js", "data-copy", "instrument script copied to dist")
    contains("start/install.html", "<!DOCTYPE html>", "redirect install doctype")
    contains("start/install.html", "/en-US/start/install.html", "redirect install target")
    contains("sitemap.xml", "<urlset", "sitemap")
    return failures


def read_pin_commit() -> str:
    return str(upstream.read_lock().get("radix", {}).get("commit", "unknown"))


def radix_dev_binary() -> str | None:
    for kind in ("debug", "release"):
        candidate = upstream.radix_checkout() / "target" / kind / "faber"
        if candidate.is_file() and os.access(candidate, os.X_OK):
            return str(candidate)
    return None


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("--full", action="store_true", help="wipe dist and the manifest first")
    parser.add_argument("--refresh-upstream", nargs="?", const="HEAD", metavar="REV",
                        help="re-pin radix at REV (default HEAD) and regenerate what derives from it")
    parser.add_argument("--faber", help="faber binary (default: faber on PATH)")
    parser.add_argument("--jobs", type=int, default=min(8, os.cpu_count() or 4))
    args = parser.parse_args(argv)

    try:
        if args.refresh_upstream is not None and not upstream.LOCK.is_file():
            # First pin: there is no lock to read yet.
            commit, trees = upstream.resolve_rev(args.refresh_upstream)
            upstream.write_lock(commit, trees, "unknown")
        build = Build(args.full, args.refresh_upstream is not None, args.faber, args.jobs)
        if args.full:
            if DIST.exists():
                shutil.rmtree(DIST)
            # The agent reference is regenerated only by --refresh-upstream, so
            # its record (and the fallbacks it took) must survive a wipe.
            kept = {k: v for k, v in build.manifest.entries.items() if k == "step:agent-reference"}
            build.manifest.entries.clear()
            build.manifest.entries.update(kept)
        DIST.mkdir(parents=True, exist_ok=True)
        if build.refresh:
            build.refresh_upstream(args.refresh_upstream)
        build.prepare_environment()
        print("[generators]")
        with build.timed("generators"):
            build.generators()
        print("[static]")
        build.copy_static()
        print("[corpus]")
        with build.timed("corpus"):
            build.corpus()
        build.grammar_tree()
        print("[diagrams]")
        build.diagram_cache()
        print("[pages]")
        with build.timed("pages"):
            build.authored_pages()
        build.copy_static()
        print("[surfaces]")
        build.derived_surfaces()
        print("[gates]")
        with build.timed("gates"):
            build.gates()
        ok = build.finish()
        return 0 if ok else 1
    except (BuildError, upstream.UpstreamError) as failure:
        print(f"\nBUILD FAILED: {failure}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
