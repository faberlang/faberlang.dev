#!/usr/bin/env python3
"""Production translate job queue for Speculum locale matrix.

Builds a manifest of (locale, rel) jobs with preferred models, waves, and
helpers to scaffold missing locale shells and write body-only prompts.

Usage:
  translate-queue.py --write-manifest PATH
  translate-queue.py --wave W1 --list
  translate-queue.py --scaffold [--wave W1|all]
  translate-queue.py --write-prompts [--wave W1]
"""

from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Callable
from pathlib import Path

# Preferred models — keep in sync with translation-bench/PREFERRED-MODELS.md
PREFERRED: dict[str, str] = {
    "th-TH": "gpt-5.6-luna-codex",
    "zh-Hans": "glm-5-2-zai",
    "zh-Hant": "gpt-5.6-luna-codex",
    "ar": "deepseek-v4-pro",
    "hi": "gpt-5.6-luna-codex",
    "vi": "gpt-5.6-luna-codex",
}

LOCALES = list(PREFERRED.keys())

# Wave membership by first path segment (or exact file)
WAVE_RULES: list[tuple[str, Callable[[str], bool]]] = [
    ("W1", lambda rel: rel == "index.md" or rel.startswith("start/")),
    ("W2", lambda rel: rel.startswith("features/")),
    ("W3", lambda rel: rel.startswith("syntax/")),
    ("W4", lambda rel: rel.startswith("tooling/") or rel.startswith("ecosystem/")),
    ("W5", lambda rel: rel.startswith("references/")
     or rel.startswith("history/")
     or rel == "404.md"),
]


def _repo_root() -> Path:
    return Path(__file__).resolve().parent.parent.parent


def _en_pages(repo: Path) -> list[str]:
    en = repo / "src" / "en-US"
    rels = sorted(
        p.relative_to(en).as_posix()
        for p in en.rglob("*.md")
        if p.is_file()
    )
    return rels


def _wave_for(rel: str) -> str:
    for name, pred in WAVE_RULES:
        if pred(rel):
            return name
    return "W9"


def _slug(rel: str) -> str:
    return rel.replace("/", "-").removesuffix(".md")


def build_jobs(repo: Path) -> list[dict]:
    jobs = []
    for rel in _en_pages(repo):
        for loc in LOCALES:
            loc_path = repo / "src" / loc / rel
            jobs.append(
                {
                    "id": f"{loc}__{_slug(rel)}",
                    "locale": loc,
                    "rel": rel,
                    "model": PREFERRED[loc],
                    "effort": "medium",
                    "wave": _wave_for(rel),
                    "locale_exists": loc_path.is_file(),
                    "status": "pending",
                }
            )
    return jobs


def write_manifest(path: Path, repo: Path) -> None:
    jobs = build_jobs(repo)
    doc = {
        "repo": str(repo),
        "preferred": PREFERRED,
        "effort_default": "medium",
        "concurrency_hint": 8,
        "job_count": len(jobs),
        "jobs": jobs,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(doc, indent=2) + "\n", encoding="utf-8")
    by_wave: dict[str, int] = {}
    missing = 0
    for j in jobs:
        by_wave[j["wave"]] = by_wave.get(j["wave"], 0) + 1
        if not j["locale_exists"]:
            missing += 1
    print(f"Wrote {path} ({len(jobs)} jobs, {missing} missing locale files)")
    for w in sorted(by_wave):
        print(f"  {w}: {by_wave[w]}")


def filter_wave(jobs: list[dict], wave: str | None) -> list[dict]:
    if not wave or wave == "all":
        return jobs
    return [j for j in jobs if j["wave"] == wave]


def scaffold(repo: Path, jobs: list[dict]) -> int:
    """Create locale shells from en-US frontmatter for missing files."""
    # local import of split helpers
    scripts = Path(__file__).resolve().parent
    if str(scripts) not in sys.path:
        sys.path.insert(0, str(scripts))
    from sync_lib import load_markdown, split_frontmatter  # noqa: E402

    n = 0
    for j in jobs:
        loc_path = repo / "src" / j["locale"] / j["rel"]
        if loc_path.is_file():
            continue
        en_path = repo / "src" / "en-US" / j["rel"]
        en_text = load_markdown(en_path)
        fm, _body = split_frontmatter(en_text)
        # Keep title/section/order/sources; mark pending
        # fm is inner without +++
        lines = []
        for line in fm.splitlines():
            if line.strip().startswith("translation_kind"):
                continue
            lines.append(line)
        if not any(l.strip().startswith("translation_kind") for l in lines):
            lines.append("")
            lines.append('translation_kind = "pending"')
        shell = "+++\n" + "\n".join(lines).strip() + "\n+++\n\n"
        shell += "<!-- pending translation -->\n"
        loc_path.parent.mkdir(parents=True, exist_ok=True)
        loc_path.write_text(shell, encoding="utf-8")
        n += 1
        print(f"scaffolded {loc_path.relative_to(repo)}")
    print(f"scaffolded {n} files")
    return 0


def write_prompts(repo: Path, jobs: list[dict], out_root: Path) -> int:
    """Write body-only launch prompts (no current-locale chrome)."""
    scripts = Path(__file__).resolve().parent
    if str(scripts) not in sys.path:
        sys.path.insert(0, str(scripts))
    from sync_lib import load_markdown, split_frontmatter, strip_fences_for_prompt  # noqa: E402

    gen = repo / "generator"
    if str(gen) not in sys.path:
        sys.path.insert(0, str(gen))
    from scripts.locales_registry import load_registry, reader_locale  # noqa: E402

    # Reuse pack snippet reader from sync-translate
    sys.path.insert(0, str(scripts))
    import importlib.util

    st_path = scripts / "sync-translate.py"
    spec = importlib.util.spec_from_file_location("sync_translate", st_path)
    st = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(st)

    workspace = repo.parent
    registry = load_registry(repo / "generator" / "locales.toml")

    contracts = {
        "th-TH": "Thai (th-TH). Natural technical Thai developer docs.",
        "zh-Hans": "Simplified Chinese (zh-Hans / 简体). Simplified characters only.",
        "zh-Hant": "Traditional Chinese (zh-Hant / 繁體). Traditional only, never Simplified.",
        "ar": "Arabic (ar). Natural technical Arabic; preserve RTL prose quality.",
        "hi": "Hindi (hi / Devanagari). Natural modern tech Hindi.",
        "vi": "Vietnamese (vi). Natural technical Vietnamese developer docs.",
    }

    n = 0
    for j in jobs:
        loc = j["locale"]
        rel = j["rel"]
        en_path = repo / "src" / "en-US" / rel
        en_text = load_markdown(en_path)
        _, en_body = split_frontmatter(en_text)
        body = strip_fences_for_prompt(en_body).strip()
        reader = reader_locale(registry, loc)
        snippet = st._read_llm_snippet(workspace, reader)

        out_dir = out_root / loc
        out_dir.mkdir(parents=True, exist_ok=True)
        slug = _slug(rel)
        out_path = out_dir / f"{slug}.prompt.md"

        parts = [
            f"You are a professional technical translator for the Faber documentation site.",
            "",
            f"# Contract — {contracts[loc]}",
            "",
            "Rules:",
            f"- Target locale: `{loc}`.",
            "- Translate prose and heading text; keep {#anchors} exact.",
            "- Leave <<<FENCE n>>> markers unchanged; do not invent sections.",
            "- Keep Latin Faber tokens in backticks/code cells; translate explanations and link labels.",
            "- Paths stay absolute (/start/...).",
            "- Return ONLY the translated Markdown body (no frontmatter, preamble, postscript).",
            "- Do not include this contract in the output.",
            "",
        ]
        if snippet:
            parts += ["## Reader pack snippet", "", snippet, ""]
        parts += [
            "## English source body",
            "",
            body,
            "",
        ]
        out_path.write_text("\n".join(parts), encoding="utf-8")
        n += 1
    print(f"wrote {n} prompts under {out_root}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo", type=Path, default=None)
    ap.add_argument("--write-manifest", type=Path, metavar="PATH")
    ap.add_argument("--wave", default=None, help="W1..W5 or all")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--scaffold", action="store_true")
    ap.add_argument("--write-prompts", action="store_true")
    ap.add_argument(
        "--prompt-root",
        type=Path,
        default=None,
        help="Default: docs/factory/multilingual-site/prompts/prod",
    )
    args = ap.parse_args()
    repo = (args.repo or _repo_root()).resolve()
    jobs = build_jobs(repo)
    jobs = filter_wave(jobs, args.wave)

    if args.write_manifest:
        write_manifest(args.write_manifest.resolve(), repo)
        return 0

    if args.list:
        for j in jobs:
            flag = "ok" if j["locale_exists"] else "MISSING"
            print(f"{j['wave']:3} {j['locale']:8} {j['model']:22} {flag:8} {j['rel']}")
        print(f"total {len(jobs)}")
        return 0

    if args.scaffold:
        return scaffold(repo, jobs)

    if args.write_prompts:
        root = args.prompt_root or (
            repo / "docs/factory/multilingual-site/prompts/prod"
        )
        return write_prompts(repo, jobs, root.resolve())

    ap.print_help()
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
