#!/usr/bin/env python3
"""
generate-target-lanes.py — build the Target lanes section.

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

Panels come from generator/lanes/out/, captured by capture-lane-panels.sh.
Nothing here is hand-authored, and a target that cannot lower a scenario is
shown as a gap rather than omitted.

Usage:
    generate-target-lanes.py [--output-dir src/en-US/targets]
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
LANES_DIR = REPO / "generator" / "lanes"
SCENARIOS_DIR = LANES_DIR / "scenarios"
OUT_DIR = LANES_DIR / "out"

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
        "fence": "rust",
        "note": "HIR projection. The package product path compiles this through "
                "Cargo.",
        "read": "Close to one-for-one with the source. That is the point of this "
                "emitter: generated Rust is meant to be *read* and reviewed, so "
                "it keeps the shape of the Faber it came from rather than "
                "expanding into something unrecognisable.",
    },
    "go": {
        "label": "Go",
        "lane": "hir",
        "fence": "go",
        "note": "HIR projection with file emission and end-to-end floors.",
        "read": "Go has no generics-free way to express some Faber types, so the "
                "emitter materialises helpers the source never wrote. Borrow "
                "modes (`de` / `in` / `ex`) erase here — they lower, but they do "
                "not survive as distinctions.",
    },
    "ts": {
        "label": "TypeScript",
        "lane": "hir",
        "fence": "ts",
        "note": "HIR projection with file emission and end-to-end floors.",
        "read": "The largest expansion among the host languages, because Faber's "
                "typed numerics and tensors have no TypeScript counterpart and "
                "arrive as generated runtime scaffolding.",
    },
    "faber": {
        "label": "Faber",
        "lane": "hir",
        "fence": "faber",
        "note": "Canonical re-emission — the compiler printing the program back.",
        "read": "The round trip. Reader-locale spellings and formatting "
                "normalise to the canonical surface, which is how a program "
                "written in one locale can be reviewed in another.",
    },
    "llvm-text": {
        "label": "LLVM IR",
        "lane": "mir",
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
        "fence": "wasm-text",
        "note": "WAT emission from the same MIR.",
        "read": "A stack machine, so the arithmetic reads inside out. Useful as "
                "a check on what actually crosses into a sandboxed runtime.",
    },
    "wgsl-text": {
        "label": "WGSL",
        "lane": "gpu",
        "fence": "wgsl-text",
        "note": "WebGPU compute shader source.",
        "read": "Bindings, workgroup declarations, and bounds guards that the "
                "kernel never spells out. This is the case for writing kernels "
                "in Faber: the source stays about the computation.",
    },
    "metal-text": {
        "label": "Metal",
        "lane": "gpu",
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
        "order": 62,
        "blurb": "MIR is where meaning takes execution-shaped form: lower-level "
                 "targets, validation surfaces, and package runtimes.",
        "detail": "Expect large expansion ratios here and do not read them as "
                  "waste. An IR names every intermediate value on purpose.",
    },
    "gpu": {
        "title": "GPU — the device lane",
        "order": 63,
        "blurb": "A function marked `@ nucleum` is a compute kernel. The device "
                 "lane links the compiler to real Metal and CUDA execution.",
        "detail": "The shader text below is the lowering surface. Real device "
                  "execution — `faber run --backend metal|cuda` — is the "
                  "narrower product proof, recorded in the "
                  "[device kernel support summary]"
                  "(/toolchain/target-matrix.html#device-kernel-support).",
    },
}


def read(path: Path) -> str | None:
    return path.read_text(encoding="utf-8").rstrip() if path.is_file() else None


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


def render_target_page(target: str, order: int) -> str | None:
    meta = TARGETS[target]
    lines = frontmatter(meta["label"], order)
    lines += [
        meta["note"],
        "",
        f"Part of the [{LANES[meta['lane']]['title'].split(' — ')[0]} lane]"
        f"(/targets/{meta['lane']}.html). Every panel below is compiler output.",
        "",
        "## How to read it {#reading}",
        "",
        meta["read"],
        "",
    ]

    shown = 0
    for scenario in scenarios_for(target):
        source = read(SCENARIOS_DIR / f"{scenario}.fab")
        emitted = read(OUT_DIR / f"{scenario}.{target}.txt")
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
        "[All lanes](/targets/) · "
        "[Measured support per term](/toolchain/target-matrix.html)",
        "",
    ]
    return "\n".join(lines)


def render_lane_page(lane: str) -> str:
    meta = LANES[lane]
    members = [t for t, m in TARGETS.items() if m["lane"] == lane]
    lines = frontmatter(meta["title"], meta["order"])
    lines += [meta["blurb"], "", meta["detail"], "", "## Targets {#targets}", "",
              "| Target | What it is | Scenarios shown |", "|---|---|---|"]
    for t in members:
        covered = sum(
            1 for s in scenarios_for(t) if (OUT_DIR / f"{s}.{t}.txt").is_file()
        )
        total = len(scenarios_for(t))
        lines.append(
            f"| [{TARGETS[t]['label']}](/targets/{t}.html) "
            f"| {TARGETS[t]['note']} | {covered} of {total} |"
        )
    lines += [
        "",
        "A target showing fewer scenarios than the others is not broken. It "
        "means the emitter declines that shape, which the pages state directly "
        "rather than hiding.",
        "",
        "---",
        "",
        "[All lanes](/targets/) · "
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
        "## The lanes {#lanes}",
        "",
        "| Lane | Carries | Targets |",
        "|---|---|---|",
    ]
    for lane, meta in LANES.items():
        members = ", ".join(
            f"[{TARGETS[t]['label']}](/targets/{t}.html)"
            for t in TARGETS if TARGETS[t]["lane"] == lane
        )
        short = meta["title"].split(" — ")[1] if " — " in meta["title"] else meta["title"]
        lines.append(f"| [{meta['title'].split(' — ')[0]}](/targets/{lane}.html) "
                     f"| {short} | {members} |")

    lines += [
        "",
        "Three more lanes carry no source-text target of their own and so have "
        "no page here: **Locale** renders reader spellings (see "
        "[reader locales](/cheatsheet/locales.html)), **AIR** is the autograd "
        "surface between typed HIR and MIR, and **Packaging** produces the FHIR "
        "and FMIR artifacts a package ships.",
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

    if not OUT_DIR.is_dir():
        print(f"ERROR: no captured panels at {OUT_DIR}; run "
              f"capture-lane-panels.sh first", file=sys.stderr)
        return 1

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
