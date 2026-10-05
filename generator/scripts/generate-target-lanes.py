#!/usr/bin/env python3
"""
generate-target-lanes.py — build the By Target section.

The landing page states the compiler's lanes as a flat table. This section
expands that table into something browsable: lane, then targets within the
lane, then — for each target — the Faber source beside what it actually
lowers to.

The comparison is the argument. Reading four lines of kernel next to
thirty-six lines of Metal makes a case that no paragraph does. But the ratio
is not the point everywhere: the Rust emitter is a close structural
projection and lands near 1:1, and a page template that treats "generated is
longer" as the story would make that look like a failure instead of the
expected result. Each target gets its own framing.

Panels come from generator/target-panels/, captured by
capture-target-panels.sh. Nothing here is hand-authored, and a target that
cannot lower a scenario is shown as a gap rather than omitted.

The per-target feature tables are the target's own slice of the measured
grammar×target matrix (faber/docs/EBNF_MATRIX.md, the same source
generate-target-matrix.py reads). The matrix is a sibling checkout; when it
is absent the committed toolchain/target-matrix.md page is used instead, and
when neither is present the feature tables are simply omitted.

Usage:
    generate-target-lanes.py [--output-dir src/en-US/targets]
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
PANELS_DIR = REPO / "generator" / "target-panels"
EXEMPLARS_DIR = PANELS_DIR / "exemplars"
LEGACY_LANES_DIR = REPO / "generator" / "lanes"
LEGACY_OUT = LEGACY_LANES_DIR / "out"
LEGACY_SCENARIOS = LEGACY_LANES_DIR / "scenarios"

SCENARIOS = {
    "tensores": {
        "title": "Typed tensors",
        "blurb": "Builds two shaped matrices, multiplies them, and reduces the "
                 "product to a scalar. Exercises shape-bearing types and a "
                 "reduction.",
    },
    "fallibilis": {
        "title": "The error channel",
        "blurb": "A function that may fail, and a caller that catches. Shows "
                 "how the `⇥` channel becomes each target's own error idiom.",
    },
    "collectiones": {
        "title": "Collections and iteration",
        "blurb": "A list folded to a total with `itera ex`. The plainest "
                 "possible read on how loops lower.",
    },
    "nucleum": {
        "title": "A compute kernel",
        "blurb": "A function marked `@ nucleum`. Device lanes only — this is a "
                 "different kind of source, not a variant of the programs above.",
    },
}

TARGETS = {
    "rust": {
        "label": "Rust",
        "lane": "hir",
        "emits": "Rust source",
        "fence": "rust",
        "note": "HIR projection. The package product path compiles this through "
                "Cargo.",
        "read": "Close to one-for-one with the source. That is the point of this "
                "emitter: generated Rust is meant to be *read* and reviewed, so "
                "it keeps the shape of the Faber it came from rather than "
                "expanding into something unrecognisable.",
    },
    "ts": {
        "label": "TypeScript",
        "lane": "hir",
        "emits": "TypeScript source",
        "fence": "ts",
        "note": "HIR projection with file emission and end-to-end floors.",
        "read": "The largest expansion among the host languages, because Faber's "
                "typed numerics and tensors have no TypeScript counterpart and "
                "arrive as generated runtime scaffolding.",
    },
    "go": {
        "label": "Go",
        "lane": "hir",
        "emits": "Go source",
        "fence": "go",
        "note": "HIR projection with file emission and end-to-end floors.",
        "read": "Go has no generics-free way to express some Faber types, so the "
                "emitter materialises helpers the source never wrote. Borrow "
                "modes (`de` / `in` / `ex`) erase here — they lower, but they do "
                "not survive as distinctions.",
    },
    "faber": {
        "label": "Faber",
        "lane": "hir",
        "emits": "Canonical Faber",
        # Canonical re-emission is itself Faber, so without naming a locale the
        # emitted panel would become a second reader-locale card sitting under
        # the source's — two identical switchers per scenario, and the
        # source-against-output comparison the page exists for stops reading.
        # Naming the locale is also just true: this is the canonical surface.
        "fence": "faber locale=la",
        "note": "Canonical re-emission — the compiler printing the program back.",
        "read": "The round trip. Reader-locale spellings and formatting "
                "normalise to the canonical surface, which is how a program "
                "written in one locale can be reviewed in another.",
    },
    "llvm-text": {
        "label": "LLVM IR",
        "lane": "mir",
        "emits": "LLVM IR text",
        "fence": "llvm-text",
        "note": "MIR staging text for external LLVM tools. Also the route CUDA "
                "device programs take, via NVVM → PTX.",
        "read": "The widest ratio on the site, and the least surprising one: SSA "
                "form names every intermediate. Read it for what the compiler "
                "knows about your program, not as something to maintain.",
    },
    "wasm-text": {
        "label": "WebAssembly text",
        "lane": "mir",
        "emits": "WebAssembly text",
        "fence": "wasm-text",
        "note": "WAT emission from the same MIR.",
        "read": "A stack machine, so the arithmetic reads inside out. Useful as "
                "a check on what actually crosses into a sandboxed runtime.",
    },
    "wgsl-text": {
        "label": "WGSL",
        "lane": "gpu",
        "emits": "WGSL compute shader",
        "fence": "wgsl-text",
        "note": "WebGPU compute shader source.",
        "read": "Bindings, workgroup declarations, and bounds guards that the "
                "kernel never spells out. This is the case for writing kernels "
                "in Faber: the source stays about the computation.",
    },
    "metal-text": {
        "label": "Metal",
        "lane": "gpu",
        "emits": "Metal MSL",
        "fence": "metal-text",
        "note": "Apple GPU compute shader source (MSL).",
        "read": "The same kernel, a different ABI. Compare it against the WGSL "
                "beside it — one Faber function, two unrelated shading "
                "languages, neither written by hand.",
    },
}

LANES = {
    "hir": {
        "title": "HIR — the application lane",
        "short": "HIR",
        "kind": "the application lane",
        "order": 61,
        "blurb": "HIR is the semantic core. Every target in this lane is a "
                 "projection of the meaning held there, emitted as source you "
                 "can read.",
        "detail": "These are host languages. The emitter's job is to produce "
                  "something a human would accept in review, which is why the "
                  "Rust output stays close to the original shape while "
                  "TypeScript expands.",
    },
    "mir": {
        "title": "MIR — the systems lane",
        "short": "MIR",
        "kind": "the systems lane",
        "order": 62,
        "blurb": "MIR is where meaning takes execution-shaped form: lower-level "
                 "targets, validation surfaces, and package runtimes.",
        "detail": "Expect large expansion ratios here and do not read them as "
                  "waste. An IR names every intermediate value on purpose.",
    },
    "gpu": {
        "title": "GPU — the device lane",
        "short": "GPU",
        "kind": "the device lane",
        "order": 63,
        "blurb": "A function marked `@ nucleum` is a compute kernel. The device "
                 "lane links the compiler to real Metal and CUDA execution.",
        "detail": "The shader text below is the lowering surface. Real device "
                  "execution — `faber run --device metal|cuda` — is the "
                  "narrower product proof, recorded in the "
                  "[device kernel support summary]"
                  "(/toolchain/target-matrix.html#device-kernel-support).",
    },
}

# ---------------------------------------------------------------------------
# Measured support — the per-target slice of the grammar×target matrix.
# ---------------------------------------------------------------------------

MATRIX_CANDIDATES = [
    Path(os.environ["FABER_EBNF_MATRIX"]) if os.environ.get("FABER_EBNF_MATRIX") else None,
    REPO.parent / "faber" / "docs" / "EBNF_MATRIX.md",
    REPO.parent.parent / "faber" / "docs" / "EBNF_MATRIX.md",
    Path.home() / "work" / "faberlang" / "faber" / "docs" / "EBNF_MATRIX.md",
    REPO / "src" / "en-US" / "toolchain" / "target-matrix.md",
]

# Glyphs that mean "this term does not fully lower" (the matrix legend).
GAP_GLYPHS = {"◐", "○", "✕"}

# The matrix anchors every term; glyph terms get an empty id. A deep link to a
# glyph is not useful and a repeated empty id is invalid HTML, so drop those
# wrappers from the gap tables.
EMPTY_ANCHOR = re.compile(r'^<a id=""></a>')

# The matrix section each lane is scored in. Device emitters are deliberately
# not scored against the general corpus: they lower a device-safe kernel
# surface and nothing else, so a percentage would read as "2% done".
LANE_SECTIONS = {
    "hir": [
        "Keywords — application lane",
        "Operators — application lane",
        "Types, intrinsics & meta",
    ],
    "mir": [
        "Keywords — systems lane",
        "Operators — systems lane",
    ],
}


def load_matrix() -> str | None:
    for candidate in MATRIX_CANDIDATES:
        if candidate is not None and candidate.is_file():
            return candidate.read_text(encoding="utf-8")
    return None


def extract_gfm_tables(text: str) -> list[str]:
    """Return GFM pipe-table blocks (header + separator + rows) in order."""
    lines = text.splitlines()
    tables: list[str] = []
    i = 0
    while i < len(lines):
        if lines[i].startswith("|") and i + 1 < len(lines):
            rest = lines[i + 1].replace("|", "").replace("-", "").replace(":", "").strip()
            if set(rest) <= {""}:
                block = [lines[i], lines[i + 1]]
                i += 2
                while i < len(lines) and lines[i].startswith("|"):
                    block.append(lines[i])
                    i += 1
                tables.append("\n".join(block))
                continue
        i += 1
    return tables


def cells_of(row: str) -> list[str]:
    return [c.strip() for c in row.strip().strip("|").split("|")]


def parse_summary(text: str) -> dict[str, tuple[str, str, str]]:
    """{target: (capable, analyzable, pct)} from the corpus-wide summary."""
    m = re.search(r"(?ms)^## Corpus-wide summary[^\n]*\n(.*?)(?=^## )", text)
    if not m:
        return {}
    out: dict[str, tuple[str, str, str]] = {}
    for table in extract_gfm_tables(m.group(1)):
        for line in table.splitlines()[2:]:
            cells = cells_of(line)
            if len(cells) != 4 or not cells[1].isdigit():
                continue
            out[cells[0].strip("`")] = (cells[1], cells[2], cells[3])
    return out


def parse_term_tables(text: str) -> dict[str, list[tuple[str, dict[str, str]]]]:
    """{section heading: [(term cell, {target: glyph})]} from the matrix."""
    parts = re.split(r"(?m)^## (.+)$", text)
    sections: dict[str, list[tuple[str, dict[str, str]]]] = {}
    i = 1
    while i + 1 < len(parts):
        heading = parts[i].strip()
        content = parts[i + 1]
        rows: list[tuple[str, dict[str, str]]] = []
        for table in extract_gfm_tables(content):
            lines = table.splitlines()
            header = [c.strip().strip("`") for c in cells_of(lines[0])]
            if not header or header[0] != "term":
                continue
            targets = header[1:]
            for line in lines[2:]:
                cells = cells_of(line)
                if len(cells) != len(header):
                    continue
                rows.append((cells[0], dict(zip(targets, cells[1:]))))
        if rows:
            sections[heading] = rows
        i += 2
    return sections


def section_for(prefix: str, sections: dict) -> str | None:
    return next((k for k in sections if k.startswith(prefix)), None)


def gap_terms(target: str, lane: str, sections: dict) -> list[tuple[str, list[str]]]:
    """[(section heading, [term cell…])] for a target's non-full support."""
    out: list[tuple[str, list[str]]] = []
    for prefix in LANE_SECTIONS.get(lane, []):
        key = section_for(prefix, sections)
        if key is None:
            continue
        terms = [
            EMPTY_ANCHOR.sub("", term)
            for term, glyphs in sections[key]
            if glyphs.get(target) in GAP_GLYPHS
        ]
        out.append((key, terms))
    return out


MATRIX_TEXT = load_matrix()
MATRIX_SUMMARY = parse_summary(MATRIX_TEXT) if MATRIX_TEXT else {}
MATRIX_SECTIONS = parse_term_tables(MATRIX_TEXT) if MATRIX_TEXT else {}


def read(path: Path) -> str | None:
    return path.read_text(encoding="utf-8").rstrip() if path.is_file() else None


def read_panel(target: str, scenario: str) -> str | None:
    """The captured emitted output for (target, scenario).

    New cache first; the legacy generator/lanes/out panel is the fallback, so
    a checkout that has not re-run capture-target-panels.sh still builds — and
    the device emitters, which the current workspace toolchain rejects, keep
    their last committed capture instead of losing the whole lane.
    """
    return (
        read(PANELS_DIR / target / f"{scenario}.out.txt")
        or read(LEGACY_OUT / f"{scenario}.{target}.txt")
    )


def read_source(target: str, scenario: str) -> str | None:
    return (
        read(PANELS_DIR / target / f"{scenario}.fab")
        or read(EXEMPLARS_DIR / f"{scenario}.fab")
        or read(LEGACY_SCENARIOS / f"{scenario}.fab")
    )


def scenarios_for(target: str) -> list[str]:
    device = TARGETS[target]["lane"] == "gpu"
    return [s for s in SCENARIOS if (s == "nucleum") == device]


def frontmatter(title: str, order: int) -> list[str]:
    return [
        "+++",
        f'title = "{title}"',
        'section = "targets"',
        f"order = {order}",
        "sources = []",
        "+++",
        "",
    ]


def support_section(target: str) -> list[str]:
    """The target's own slice of the measured matrix, or the device note."""
    meta = TARGETS[target]
    if meta["lane"] == "gpu":
        return [
            "## Measured support {#support}",
            "",
            f"`{target}` is a **device-kernel emitter**, not a "
            "general-language target. It lowers `@ nucleum` compute kernels "
            "and related GPU views, and deliberately nothing else, so it is "
            "not scored against the general corpus — a percentage there would "
            "read as a completion score it is not. Its measured support is the "
            "[device kernel support summary]"
            "(/toolchain/target-matrix.html#device-kernel-support).",
            "",
        ]

    summary = MATRIX_SUMMARY.get(target)
    if not summary:
        return []
    capable, analyzable, pct = summary
    lines = [
        "## Measured support {#support}",
        "",
        "| Capable | Analyzable | Coverage |",
        "|---|---|---|",
        f"| {capable} | {analyzable} | {pct} |",
        "",
        "From the [target matrix](/toolchain/target-matrix.html): how many "
        "corpus exempla lower to this target. Coverage is not a quality score "
        "— an emitter can lower a term and still erase a distinction.",
        "",
    ]
    gaps = gap_terms(target, meta["lane"], MATRIX_SECTIONS)
    gaps_with_terms = [(heading, terms) for heading, terms in gaps if terms]
    if gaps_with_terms:
        lines += [
            "### Not fully supported {#gaps}",
            "",
            "Terms the matrix records as partial, planned, or unsupported for "
            "this target. A term here is a measured gap, not an omission.",
            "",
            "| Category | Terms |",
            "|---|---|",
        ]
        for heading, terms in gaps_with_terms:
            lines.append(f"| {heading} | {', '.join(terms)} |")
        lines.append("")
    elif gaps:
        lines += ["No measured gaps in the scored sections.", ""]
    return lines


def lane_support_section(lane: str) -> list[str]:
    lines = ["## Measured support {#support}", ""]
    if lane == "gpu":
        lines += [
            "Device-kernel emitters are not scored against the general corpus "
            "— they lower a kernel surface and nothing else. Their measured "
            "support is the [device kernel support summary]"
            "(/toolchain/target-matrix.html#device-kernel-support).",
            "",
        ]
        return lines

    lines += [
        "| Target | Capable | Analyzable | Coverage |",
        "|---|---|---|---|",
    ]
    page_targets = {t for t, m in TARGETS.items() if m["lane"] == lane}
    for target in (t for t, m in TARGETS.items() if m["lane"] == lane):
        summary = MATRIX_SUMMARY.get(target)
        label = TARGETS[target]["label"]
        if summary:
            capable, analyzable, pct = summary
            lines.append(
                f"| [{label}](/targets/{target}.html) | {capable} "
                f"| {analyzable} | {pct} |"
            )
        else:
            lines.append(f"| [{label}](/targets/{target}.html) | — | — | — |")
    lines.append("")
    if lane == "mir":
        measured: set[str] = set()
        for prefix in LANE_SECTIONS["mir"]:
            key = section_for(prefix, MATRIX_SECTIONS)
            if key:
                for _, glyphs in MATRIX_SECTIONS[key]:
                    measured |= set(glyphs)
        extras = sorted(
            t for t in measured
            if t not in page_targets and t not in {"metal-text", "wgsl-text"}
        )
        if extras:
            listed = ", ".join(f"`{t}`" for t in extras)
            lines += [
                f"The matrix also measures {listed} — MIR emit surfaces with "
                "no page here yet.",
                "",
            ]
    return lines


def render_target_page(target: str, order: int) -> str | None:
    meta = TARGETS[target]
    lines = frontmatter(meta["label"], order)
    lines += [
        meta["note"],
        "",
        f"Part of the [{LANES[meta['lane']]['short']} lane]"
        f"(/targets/{meta['lane']}.html). Every panel below is compiler output.",
        "",
        "## How to read it {#reading}",
        "",
        meta["read"],
        "",
    ]
    lines += support_section(target)

    shown = 0
    for scenario in scenarios_for(target):
        source = read_source(target, scenario)
        emitted = read_panel(target, scenario)
        if source is None:
            continue
        info = SCENARIOS[scenario]
        lines += [f"## {info['title']} {{#{scenario}}}", "", info["blurb"], ""]

        if emitted is None:
            lines += [
                f"**{meta['label']} does not lower this scenario.** That is a "
                "measured gap, not an omission — the emitter rejects it rather "
                "than producing something that would not run.",
                "",
            ]
            shown += 1
            continue

        src_lines = source.count("\n") + 1
        out_lines = emitted.count("\n") + 1
        ratio = out_lines / src_lines if src_lines else 0
        lines += [
            "**Faber source**",
            "",
            "```faber",
            source,
            "```",
            "",
            f"**{meta['label']}** — {src_lines} lines in, {out_lines} out "
            f"({ratio:.1f}×)",
            "",
            f"```{meta['fence']}",
            emitted,
            "```",
            "",
        ]
        shown += 1

    if not shown:
        return None

    lines += [
        "---",
        "",
        "[All targets](/targets/) · "
        "[Measured support per term](/toolchain/target-matrix.html)",
        "",
    ]
    return "\n".join(lines)


def render_lane_page(lane: str) -> str:
    meta = LANES[lane]
    members = [t for t, m in TARGETS.items() if m["lane"] == lane]
    lines = frontmatter(meta["title"], meta["order"])
    lines += [meta["blurb"], "", meta["detail"], "", "## Targets {#targets}", ""]
    lines += [
        "| Target | Emits | Scenarios shown |",
        "|---|---|---|",
    ]
    for t in members:
        covered = sum(
            1 for s in scenarios_for(t) if read_panel(t, s) is not None
        )
        total = len(scenarios_for(t))
        lines.append(
            f"| [{TARGETS[t]['label']}](/targets/{t}.html) "
            f"| {TARGETS[t]['emits']} | {covered} of {total} |"
        )
    lines += [
        "",
        "A target showing fewer scenarios than the others is not broken. It "
        "means the emitter declines that shape, which the pages state directly "
        "rather than hiding.",
        "",
    ]
    lines += lane_support_section(lane)
    lines += [
        "---",
        "",
        "[All targets](/targets/) · "
        "[Measured support per term](/toolchain/target-matrix.html)",
        "",
    ]
    return "\n".join(lines)


def render_index() -> str:
    lines = frontmatter("Target lanes", 60)
    lines += [
        "Faber compiles through lanes, and every target is a **projection** of "
        "the meaning the compiler holds — not a separate implementation. These "
        "pages put the source beside what it becomes.",
        "",
        "Every generated panel is captured compiler output. If a page shows "
        "Rust, that is the Rust the compiler emits for the program above it.",
        "",
    ]

    for lane, meta in LANES.items():
        members = [t for t, m in TARGETS.items() if m["lane"] == lane]
        lines += [
            f"## {meta['title']} {{#{lane}}}",
            "",
            meta["blurb"],
            "",
            f"[{meta['short']} lane overview](/targets/{lane}.html)",
            "",
            "| Target | Emits | Scenarios shown |",
            "|---|---|---|",
        ]
        for t in members:
            covered = sum(
                1 for s in scenarios_for(t) if read_panel(t, s) is not None
            )
            total = len(scenarios_for(t))
            lines.append(
                f"| [{TARGETS[t]['label']}](/targets/{t}.html) "
                f"| {TARGETS[t]['emits']} | {covered} of {total} |"
            )
        lines.append("")

    lines += [
        "## Other lanes {#other-lanes}",
        "",
        "Three more compiler lanes carry no source-text target of their own "
        "and so have no page here: **Locale** renders reader spellings (see "
        "[reader locales](/cheatsheet/locales.html)), **AIR** is the autograd "
        "surface between typed HIR and MIR, and **Packaging** produces the "
        "FHIR and FMIR artifacts a package ships.",
        "",
        "This is the honest target list: a page exists only for a lane the "
        "compiler exposes as a text target. There is no CUDA page — CUDA "
        "device programs are produced on the NVVM → PTX path and run with "
        "`faber run --device cuda`, not emitted as source text. The "
        "[target matrix](/toolchain/target-matrix.html) measures a few more "
        "emit surfaces than the site gives pages to.",
        "",
        "## The scenarios {#scenarios}",
        "",
        "The same small programs run through every lane, so the pages compare "
        "like with like.",
        "",
        "| Scenario | What it exercises |",
        "|---|---|",
    ]
    for name, meta in SCENARIOS.items():
        lines.append(f"| **{meta['title']}** | {meta['blurb']} |")

    lines += [
        "",
        "## Support is measured elsewhere {#support}",
        "",
        "These pages *demonstrate*. For measurement — which grammar terms lower "
        "on which target, across the whole corpus — use the "
        "[target matrix](/toolchain/target-matrix.html). It is the numeric "
        "authority; this section is the worked example.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output-dir", default="src/en-US/targets")
    args = ap.parse_args()

    if not EXEMPLARS_DIR.is_dir() and not LEGACY_OUT.is_dir():
        print(f"ERROR: no captured panels at {PANELS_DIR} or {LEGACY_OUT}; "
              f"run capture-target-panels.sh first", file=sys.stderr)
        return 1
    if not MATRIX_TEXT:
        print("warning: no EBNF matrix found; feature tables omitted",
              file=sys.stderr)

    out = REPO / args.output_dir
    out.mkdir(parents=True, exist_ok=True)
    for existing in out.glob("*.md"):
        existing.unlink()

    (out / "index.md").write_text(render_index(), encoding="utf-8")
    for lane in LANES:
        (out / f"{lane}.md").write_text(render_lane_page(lane), encoding="utf-8")

    written = 0
    order = 70
    for target in TARGETS:
        page = render_target_page(target, order)
        if page is None:
            print(f"  warning: no panels for {target}, page skipped", file=sys.stderr)
            continue
        (out / f"{target}.md").write_text(page, encoding="utf-8")
        written += 1
        order += 1

    print(f"target lanes: {len(LANES)} lanes, {written} target pages → {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
