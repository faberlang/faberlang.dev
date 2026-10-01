#!/usr/bin/env python3
"""Turn the `faber explain` registry into the /agents/reference Markdown tree.

The compiler owns the reference content: `faber explain --list` gives the
sections and terms, and `faber explain <term> --json` gives one entry. The site
renders that; it does not author any of it.

Two body shapes come back from the registry, and both must render the same way:

- a rendered man page — bare `====` banners, `What this teaches:` and
  `Common mistakes:` blocks, then a ```fab example;
- a raw corpus `.fab` file — one fence holding the example and then the same
  prose carried as trailing `#` comments.

The parser normalizes both into labeled blocks, so the page shape does not
depend on which shape the registry happened to return.
"""

from __future__ import annotations

import re

FENCE = re.compile(r"^\s*```")
BANNER = re.compile(r"^\s*(#\s*)?=+\s*$")
COMMENT_BANNER = re.compile(r"^\s*#\s*=+\s*$")
LABEL = re.compile(r"^\s*(?:#\s*)?([A-Z][A-Za-z ]{2,40}):\s*$")
BULLET = re.compile(r"^\s*(?:#\s*)?•\s?(.*)$")
SEE_ALSO = re.compile(r"^\s*(?:#\s*)?See also:\s*(.*)$")

# Registry labels that become a page section. Anything else keeps its own
# label as a heading, so an unfamiliar block is shown rather than dropped.
LABEL_SECTIONS: dict[str, str] = {
    "What this teaches": "What this teaches",
    "Common mistakes": "Common mistakes",
    "GRAMMAR": "Grammar",
    "EXPECTED OUTPUT": "Expected output",
    "EXPECTED stdout": "Expected output",
    "EXPECTED ERROR": "Expected error",
    "BACKEND": "Backend",
}

# Blocks whose content is source-like and reads better in a code fence.
CODE_BLOCKS: frozenset[str] = frozenset({"Grammar", "Expected output", "Expected error", "Backend"})


def parse_list(text: str) -> tuple[list[str], list[dict[str, str]]]:
    """`(sections, entries)` from `faber explain --list` output."""
    sections: list[str] = []
    entries: list[dict[str, str]] = []
    section = ""
    for line in text.splitlines():
        if line.startswith("reference:"):
            continue
        stripped = line.strip()
        if stripped and re.fullmatch(r"[A-Z]+", stripped):
            section = stripped
            if section not in sections:
                sections.append(section)
            continue
        if not line.startswith("  ") or not stripped or not section:
            continue
        parts = re.split(r"\s{2,}", stripped, maxsplit=2)
        if len(parts) != 3:
            continue
        entries.append({"section": section, "term": parts[0], "category": parts[1], "summary": parts[2]})
    return sections, entries


def uncomment(line: str) -> str:
    return re.sub(r"^\s*#\s?", "", line)


def split_body(body: str) -> tuple[list[str], list[str]]:
    """`(prose_lines, fab_examples)`.

    A fenced block whose content carries a trailing comment banner is split:
    the code above the banner is the example, the comments below are prose.
    That is the raw-corpus shape, where the example and its teaching share one
    fence.
    """
    prose: list[str] = []
    examples: list[str] = []
    fenced: list[str] | None = None
    for line in body.split("\n"):
        if FENCE.match(line):
            if fenced is None:
                fenced = []
                continue
            content = "\n".join(fenced)
            fenced = None
            cut = None
            for index, inner in enumerate(content.split("\n")):
                if COMMENT_BANNER.match(inner):
                    cut = index
                    break
            if cut is None:
                examples.append(content.strip("\n"))
            else:
                head = "\n".join(content.split("\n")[:cut]).strip("\n")
                if head.strip():
                    examples.append(head)
                prose.extend(uncomment(inner) for inner in content.split("\n")[cut:])
            continue
        if fenced is not None:
            fenced.append(line)
        else:
            prose.append(line)
    if fenced:
        examples.append("\n".join(fenced).strip("\n"))
    return prose, examples


def parse_prose(lines: list[str]) -> tuple[list[str], list[tuple[str, list[str]]]]:
    """`(preamble, blocks)` where each block is `(label, lines)`.

    A run of `•` bullets becomes one block body; continuation lines are joined
    back onto their bullet, because the registry hard-wraps at about 80 columns.
    """
    preamble: list[str] = []
    blocks: list[tuple[str, list[str]]] = []
    label: str | None = None
    body: list[str] = []

    def flush() -> None:
        nonlocal label, body
        if label is not None:
            blocks.append((label, body))
        elif body:
            preamble.extend(body)
        label, body = None, []

    for line in lines:
        if BANNER.match(line):
            flush()
            continue
        found = LABEL.match(line)
        if found and not BULLET.match(line):
            flush()
            label = found.group(1).strip()
            continue
        see = SEE_ALSO.match(line)
        if see:
            flush()
            label = "See also"
            body = [see.group(1).strip()]
            continue
        body.append(line)
    flush()
    return preamble, blocks


def bullets(lines: list[str]) -> list[str]:
    """Bullet texts, with hard-wrapped continuations rejoined."""
    out: list[str] = []
    for line in lines:
        found = BULLET.match(line)
        if found:
            out.append(found.group(1).strip())
        elif out and line.strip():
            out[-1] = f"{out[-1]} {line.strip()}"
    return out


def prose_lines(lines: list[str]) -> list[str]:
    """Non-bullet text, blank-line separated, hard wraps left alone."""
    return [line.rstrip() for line in lines]


def choose_example(original: str, projected: str, checks) -> tuple[str, bool]:
    """`(example, fell_back)`.

    Projection is a token rewrite, so it can mangle an example: Faber allows a
    keyword to be used as an identifier, and a field named `nomen` is rewritten
    in its declaration but not in `value.nomen`. When the projected form no
    longer compiles and the registry's own text does, the registry wins.
    """
    if checks(projected) or not checks(original):
        return projected, False
    return original, True


def slug_for(term: str, kind: str, pack: dict[str, dict[str, str]]) -> str:
    """The reader-pack spelling for a term, or the term itself.

    Intrinsics resolve through their own table first: their canonical names are
    Latin-ish (`accīpe`) while the English surface is a word (`get`).
    """
    kind = (kind or "").lower()
    if kind == "type":
        order = ("types", "keywords", "intrinsics")
    elif kind in {"intrinsic", "method", "function"} and term in pack.get("intrinsics", {}):
        order = ("intrinsics", "keywords", "types")
    else:
        order = ("keywords", "types", "intrinsics")
    for section in order:
        native = pack.get(section, {}).get(term)
        if native:
            return native
    return term


def assign_slugs(
    entries: list[dict[str, str]],
    pack: dict[str, dict[str, str]],
) -> tuple[dict[str, str], list[tuple[str, str, str]]]:
    """`({term: slug}, collisions)`.

    The first term in sorted order keeps a contested slug; a later term keeps
    its own name, and if that is taken too it takes a numeric suffix. Without
    the suffix two distinct canonicals that share one English word (`unio` and
    `union`) would overwrite each other's page.
    """
    wanted = {entry["term"]: slug_for(entry["term"], entry.get("kind", ""), pack) for entry in entries}
    taken: dict[str, str] = {}
    slugs: dict[str, str] = {}
    collisions: list[tuple[str, str, str]] = []
    for term in sorted(wanted):
        slug = wanted[term]
        owner = taken.get(slug)
        if owner is None:
            taken[slug] = term
            slugs[term] = slug
            continue
        if owner == term:
            slugs[term] = slug
            continue
        fallback = term
        index = 2
        while fallback in taken:
            fallback = f"{term}-{index}"
            index += 1
        collisions.append((term, slug, owner))
        taken[fallback] = term
        slugs[term] = fallback
    return slugs, collisions


def fence(text: str, language: str = "") -> str:
    """A fenced block whose fence is longer than any backtick run inside it."""
    longest = 0
    for match in re.finditer(r"`+", text):
        longest = max(longest, len(match.group(0)))
    bars = "`" * max(3, longest + 1)
    return f"{bars}{language}\n{text.strip()}\n{bars}"


FOOTER = "Fetch list: https://faberlang.dev/agents/index.md"


def render_page(
    *,
    term: str,
    title: str,
    section: str,
    summary: str,
    syntax: str,
    aliases: list[str],
    related: list[str],
    blocks: list[tuple[str, list[str]]],
    examples: list[str],
    link_of: dict[str, str],
    project=lambda text: text,
    project_example=None,
) -> str:
    """One reference page.

    `project` is applied to the fields that carry registry prose — the summary,
    the syntax line, the teaching blocks, the example, and the related names.
    The identity line is written after projection: the registry term is what
    `faber explain` accepts, and projecting it would erase the very string the
    reader needs to reproduce the lookup.
    """
    meta = [f"**Term** `{term}`", f"**Section** {section}"]
    if aliases:
        meta.append("**Also** " + ", ".join(f"`{name}`" for name in aliases))
    lines = [f"# {title}", "", project(summary), "", " · ".join(meta), ""]

    if syntax:
        lines += ["## Syntax", "", fence(project(syntax)), ""]

    for label, body in sorted(blocks, key=lambda pair: _block_rank(pair[0])):
        heading = LABEL_SECTIONS.get(label, label)
        if heading == "See also":
            continue
        if heading in CODE_BLOCKS:
            # The registry's grammar and expectation blocks are production
            # notation and paths; the site's grammar pages keep that form, so
            # they are shown as the compiler emits them.
            text = "\n".join(line for line in body if line.strip())
            if not text:
                continue
            lines += [f"## {heading}", "", fence(text), ""]
            continue
        content = [project(line) for line in body]
        items = bullets(content)
        if items:
            lines += [f"## {heading}", ""] + [f"- {item}" for item in items] + [""]
        else:
            text = "\n".join(prose_lines(content)).strip()
            if text:
                lines += [f"## {heading}", "", text, ""]

    if examples:
        lines += ["## Example", ""]
        for example in examples:
            # Every registry example is a Faber program. It gets its own
            # projection hook because a rewrite can break code that prose
            # survives; the caller resolves which form to ship.
            lines += [fence((project_example or project)(example), "fab"), ""]

    if related:
        rendered = []
        for name in related:
            target = link_of.get(name)
            shown = project(name)
            rendered.append(f"[`{shown}`]({target}.md)" if target else f"`{shown}`")
        lines += ["See also: " + ", ".join(rendered) + ".", ""]

    lines += [FOOTER, ""]
    return "\n".join(lines)


def _block_rank(label: str) -> int:
    order = ["What this teaches", "Common mistakes", "GRAMMAR", "EXPECTED OUTPUT", "EXPECTED stdout", "EXPECTED ERROR", "BACKEND"]
    try:
        return order.index(label)
    except ValueError:
        return len(order)


def render_index(
    *,
    sections: list[str],
    entries: list[dict[str, str]],
    slugs: dict[str, str],
) -> str:
    """The fetch list for the reference tree, grouped by registry section."""
    lines = [
        "# Reference",
        "",
        "One page per `faber explain` entry, generated from the compiler registry so",
        "it cannot drift from it. Fetch a page, or run the same lookup locally:",
        "",
        "```bash",
        "faber explain fn",
        "faber explain fn --json",
        "```",
        "",
        "Each page names its registry term, its section, and any alternate spelling.",
        "Latin spellings are accepted lookups; the documented spelling is English.",
        "",
    ]
    for section in sections:
        rows = [entry for entry in entries if entry["section"] == section]
        if not rows:
            continue
        lines += [f"## {section.title()}", ""]
        for entry in sorted(rows, key=lambda item: slugs[item["term"]].casefold()):
            term = entry["term"]
            slug = slugs[term]
            aliases = entry.get("aliases") or []
            names = []
            if term != slug:
                names.append(f"`{term}`")
            names.extend(f"`{name}`" for name in aliases)
            suffix = f" ({'; also '.join(names)})" if names else ""
            lines.append(f"- [{slug}]({slug}.md){suffix} — {entry['summary']}")
        lines.append("")
    lines += [FOOTER, ""]
    return "\n".join(lines)


def render_stub(*, slug: str, target: str, source: str) -> str:
    """A resolution page for an accepted spelling that is not the canonical slug."""
    return "\n".join(
        [
            f"# {slug}",
            "",
            f"`{slug}` is another spelling of the entry documented at",
            f"[`{target}`]({target}.md).",
            "",
            f"Source: {source}.",
            "",
            FOOTER,
            "",
        ]
    )
