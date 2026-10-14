#!/usr/bin/env python3
"""Generate grammar reader pages from Radix's identity EBNF and glossary packs."""
from __future__ import annotations

import argparse
import json
import re
import sys
import tomllib
from pathlib import Path

LEAD_EN = """The formal grammar for every Faber production, generated from the compiler's
own specification and shown in the English reader spellings. The words in
quotes are the words you write: a loop is `for`, a class is `class`, a
function is `fn`. Rule names (`itera_stmt`, `genus_decl`) are stable grammar
identifiers. Latin stays the compiler's canonical form; `faber explain <term>`
prints a mapping from the compiler itself.

This page is the authority on whether something is valid syntax. The
[target matrix](/toolchain/target-matrix.html) is the authority on whether
a given target supports it.

Uppercase names in the productions are lexical terminals. Grammar examples
are fragments shown to illustrate a production — they are not standalone
programs and are not expected to compile on their own."""

LEAD_PLAIN = """This page is the formal grammar of Faber, written as EBNF productions. A
production is one rule: it names a piece of the language and says what it is
built from, for example that a loop is a keyword, a binding, and a block.
Quoted words are the words you write, shown in this locale's spellings;
uppercase names are lexical tokens. You do not need to read any of this to
write Faber, because the cheat sheet and the language pages teach each form by
example. The productions are here for tools, models, and anyone checking an
edge case against the parser's own definition."""

IDENTITY_BANNER = ("This file is generated from `grammar/sources/source.fg`, its `sidecar.en.toml`\n"
                   "and its `prose.en.md`; hand edits fail the stage-1 normative-triple gate.")
HOLE = "§{"
IDENT_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
IDENT_TOKEN_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")


def die(message: str, code: int = 1) -> None:
    print(message, file=sys.stderr)
    raise SystemExit(code)


def load_spine(path: Path) -> dict[str, bool]:
    spine: dict[str, bool] = {}
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
        for line in lines:
            if not line:
                continue
            rec = json.loads(line)
            ident = rec.get("id", "")
            if not isinstance(ident, str) or not ident:
                die(f"{path}: record without a string id")
            spine[ident] = True
            keywords = rec.get("keywords", [])
            if not isinstance(keywords, list):
                keywords = []
            for kw in keywords:
                if not isinstance(kw, str) or not kw:
                    die(f"{path}: keyword that is not a string in record {ident}")
                spine[kw] = True
    except OSError as exc:
        die(f"generate-grammar: {exc}")
    return spine


def read_string_table(doc: dict, section: str, path: Path) -> dict[str, str]:
    table = doc.get(section, {})
    if not isinstance(table, dict):
        table = {}
    out = {}
    for key, value in table.items():
        if not isinstance(value, str) or not value:
            die(f"english pack section {section} entry '{key}' is not a string")
        out[key] = value
    return out


def english_projection(path: Path) -> dict[str, str]:
    try:
        doc = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as exc:
        die(f"{path}: {exc}")
    types = read_string_table(doc, "types", path)
    keywords = read_string_table(doc, "keywords", path)
    if not keywords:
        die(f"{path}: no [keywords] table")
    result = dict(types)
    result.update(keywords)
    if types.get("nihil"):
        result["nihil"] = types["nihil"]
    return result


def load_glossary(path: Path, spine: dict[str, bool]) -> dict[str, str]:
    try:
        doc = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as exc:
        die(f"{path}: {exc}")
    table = doc.get("keywords", {})
    if not isinstance(table, dict) or not table:
        die(f"{path}: no [keywords] table")
    extras = [key for key in table if key not in spine]
    mapping = {}
    for key, value in table.items():
        if not isinstance(value, str) or not value:
            die(f"{path}: glossary entry '{key}' is not a string")
        mapping[key] = value
    if extras:
        die(f"{path}: glossary key(s) not in jsonl production/keyword spine: {', '.join(extras)}")
    return mapping


def substitute_holes(text: str, glossary: dict[str, str], area: str, path: str) -> str:
    def replace(match: re.Match) -> str:
        label = match.group(1)
        if not IDENT_RE.fullmatch(label):
            return match.group(0)
        if label not in glossary:
            die(f"unknown glossary key {label} area={area} path={path}")
        return glossary[label]
    out = re.sub(r"§\{([^}]*)\}", replace, text)
    if HOLE in out:
        die(f"zero-residual leftover hole area={area} path={path}")
    return out


def mark_ebnf_keywords(text: str, glossary: dict[str, str]) -> str:
    parts = text.split("'")
    if len(parts) <= 1:
        return text
    out = []
    for i, part in enumerate(parts):
        if i % 2 == 0:
            out.append(part)
        else:
            out.extend(("'", glossary.get(part, part), "'"))
    return "".join(out)


def mark_ident_keywords(text: str, glossary: dict[str, str]) -> str:
    if text in glossary:
        return glossary[text]
    return IDENT_TOKEN_RE.sub(lambda m: glossary.get(m.group(0), m.group(0)), text)


def fill_inline(inner: str, glossary: dict[str, str], path: str, exact_only: bool) -> str:
    if inner in glossary:
        return glossary[inner]
    if exact_only:
        return inner
    out = mark_ident_keywords(inner, glossary)
    if HOLE in out:
        out = substitute_holes(out, glossary, "inline", path)
    return out


def process_inlines(text: str, glossary: dict[str, str], path: str, exact_only: bool) -> str:
    if "`" not in text:
        return text
    # Match the Faber scanner's variable-length backtick delimiters.
    out, cursor = [], 0
    while cursor < len(text):
        start = text.find("`", cursor)
        if start < 0:
            out.append(text[cursor:])
            break
        out.append(text[cursor:start])
        ticks = 1
        while start + ticks < len(text) and text[start + ticks] == "`":
            ticks += 1
        delim = "`" * ticks
        end = text.find(delim, start + ticks)
        if end < 0:
            out.append(text[start:])
            break
        inner = text[start + ticks:end]
        out.extend((delim, fill_inline(inner, glossary, path, exact_only), delim))
        cursor = end + ticks
    return "".join(out)


def apply_glossary(text: str, glossary: dict[str, str], path: str, project_english: bool) -> str:
    delim = "\n```"
    chunks = text.split(delim)
    if len(chunks) <= 1:
        return process_inlines(text, glossary, path, project_english)
    out = []
    for i, chunk in enumerate(chunks):
        if i % 2 == 0:
            out.append(process_inlines(chunk, glossary, path, project_english))
            continue
        nl = chunk.find("\n")
        if nl < 0:
            info, inner = chunk.strip(), ""
        else:
            info, inner = chunk[:nl].strip(), chunk[nl + 1:]
        lang = info.split(" ", 1)[0]
        if lang == "ebnf":
            inner = mark_ebnf_keywords(inner, glossary)
            if HOLE in inner:
                inner = substitute_holes(inner, glossary, "ebnf", path)
        elif project_english and lang == "fab":
            inner = mark_ident_keywords(inner, glossary)
        out.append(delim + info + "\n" + inner)
        if i + 1 < len(chunks):
            out.append(delim)
    return "".join(out)


def collapse_newlines(text: str) -> str:
    return re.sub(r"\n{3,}", "\n\n", text)


def transform(lines: list[str], drop_lead: bool) -> str:
    body, state, in_fence = [], 0, False
    for line in lines:
        stripped = line.strip()
        if state == 0:
            skip = not stripped or stripped.startswith("# ") or stripped.startswith(">")
            if not skip:
                state = 1 if drop_lead else 2
        if state == 1 and not stripped:
            state = 3
        elif state == 3 and stripped:
            state = 2
        if state != 2:
            continue
        if line.strip().startswith("```"):
            in_fence = not in_fence
            body.append("```text\n" if in_fence and line.strip() == "```fab" else line + "\n")
        elif in_fence:
            body.append(line + "\n")
        elif "](./" in line or "](../" in line:
            continue
        else:
            body.append(line + "\n")
    result = collapse_newlines("".join(body).strip())
    if result.startswith("---\n"):
        result = result[3:].lstrip("\n")
    return result + "\n"


def render_page(body: str, locale: str) -> str:
    page = "+++\n"
    if locale != "en-US":
        page += 'translation_kind = "translated"\n\n'
    page += 'title = "Grammar"\nsection = "reference"\norder = 1\nsources = [\n'
    page += '  "radix/grammar/sources/grammar.jsonl",\n'
    page += ('  "radix/locale/en/pack.toml",\n' if locale == "en-US" else
             f'  "radix/grammar/sources/glossary.{locale}.toml",\n')
    page += "]\n+++\n\n"
    page += (LEAD_EN if locale == "en-US" else LEAD_PLAIN) + "\n\n"
    return page + body


def locale_names() -> list[str]:
    return sorted(p.name for p in Path("src").iterdir() if p.is_dir())


def main() -> None:
    parser = argparse.ArgumentParser(prog="generate-grammar", add_help=True)
    parser.add_argument("--all-locales", action="store_true")
    parser.add_argument("--locale", action="append", default=[])
    import upstream

    grammar = upstream.radix_root() / "grammar"
    parser.add_argument("--jsonl", default=str(grammar / "sources" / "grammar.jsonl"))
    parser.add_argument("--identity", default=str(grammar / "EBNF.md"))
    parser.add_argument("--glossary-dir", default=str(grammar / "sources"))
    args = parser.parse_args()
    jsonl_path, identity_path = Path(args.jsonl), Path(args.identity)
    glossary_dir = Path(args.glossary_dir)
    if not jsonl_path.exists():
        die(f"generate-grammar: missing grammar.jsonl: {jsonl_path}")
    if not identity_path.exists():
        die(f"generate-grammar: missing identity EBNF: {identity_path}")
    spine = load_spine(jsonl_path)
    identity = identity_path.read_text(encoding="utf-8")
    locales = locale_names() if args.all_locales else (args.locale or ["en-US"])
    written = 0
    for locale in locales:
        glossary, path_label, project_english = dict.fromkeys(spine, ""), str(jsonl_path), False
        # The identity mapping uses each key's own spelling, including keys not
        # found in a glossary; this preserves the historical non-English path.
        glossary = {key: key for key in spine}
        if locale == "en-US":
            pack_path = upstream.radix_root() / "locale" / "en" / "pack.toml"
            if not pack_path.exists():
                die(f"generate-grammar: missing English reader pack: {pack_path}")
            glossary, path_label, project_english = english_projection(pack_path), str(pack_path), True
        else:
            gpath = glossary_dir / f"glossary.{locale}.toml"
            if not gpath.exists():
                print(f"  warning: no grammar source for {locale} ({gpath})", file=sys.stderr)
                continue
            glossary, path_label = load_glossary(gpath, spine), str(gpath)
        rendered = apply_glossary(identity, glossary, path_label, project_english)
        if project_english:
            if "the identity rendering" not in rendered:
                die("generate-grammar: English page is missing the identity-rendering sentence")
            rendered = rendered.replace("the identity rendering", "the English reader rendering")
            if "quoted Latin literals" not in rendered:
                die("generate-grammar: English page is missing the Latin-literals sentence")
            rendered = rendered.replace("quoted Latin literals", "English reader spellings")
        else:
            replacement = (f"This file is generated from `grammar/sources/source.fg`, its `sidecar.en.toml` and its `prose.en.md`, and\n"
                           f"`grammar/sources/glossary.{locale}.toml`; hand edits fail the locale-render gate.")
            if IDENTITY_BANNER not in rendered:
                die("identity banner missing; cannot stamp locale render")
            rendered = rendered.replace(IDENTITY_BANNER, replacement)
        page = render_page(transform(rendered.split("\n"), locale == "en-US"), locale)
        output = Path("src") / locale / "reference" / "grammar.md"
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(page, encoding="utf-8")
        print(f"  grammar: {output} ({len(page.splitlines())} lines)")
        written += 1
    if not written:
        die("ERROR: no grammar page written")

if __name__ == "__main__":
    main()
