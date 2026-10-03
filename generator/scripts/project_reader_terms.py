"""Reader-pack keyword projection for rendered Markdown and corpus examples."""
from __future__ import annotations

import re
import subprocess
import tempfile
import tomllib
from pathlib import Path

SHORT_SAFE = {"si", "sin", "ex", "de", "ab", "dum", "fac", "sit", "ad", "ut", "aut", "non"}
HOMOGRAPHS = {
    "schema", "ratio", "series", "census", "matrix", "vector", "tensor", "cursor",
    "modulus", "fragment", "vertex", "radix", "copy", "own", "tag", "lane",
    "cli", "regex", "json", "atomic", "queue", "stack",
}
WORD = re.compile(r"[^\W_]+", re.UNICODE)


def load_mapping(pack_path: Path) -> dict[str, str]:
    with pack_path.open("rb") as handle:
        pack = tomllib.load(handle)
    types = {str(k): str(v).strip() for k, v in (pack.get("types") or {}).items()}
    mapping = dict(types)
    mapping.update({str(k): str(v).strip() for k, v in (pack.get("keywords") or {}).items()})
    if types.get("nihil"):
        mapping["nihil"] = types["nihil"]
    return {key: value for key, value in mapping.items() if value and value != key}


def _whole_token(text: str, start: int, end: int) -> bool:
    return (start == 0 or not (text[start - 1].isalnum() or text[start - 1] == "_")) and (
        end == len(text) or not (text[end].isalnum() or text[end] == "_")
    )


_PATH_BEFORE = set("/:.#_-")
_GLYPHS = "←→⇥↤∪‥"


def _guarded(text: str, start: int, end: int) -> bool:
    """True when a token is a path segment, an anchor piece, or a joined compound.

    A following '.' or ':' counts only when an identifier continues after it,
    so a sentence period does not glue the last word to a path.
    """
    before = text[start - 1] if start else ""
    after = text[end:end + 1]
    if before in _PATH_BEFORE or after in {"_", "-"}:
        return True
    if after in {".", ":"}:
        nxt = text[end + 1:end + 2]
        return bool(nxt) and (nxt.isalnum() or nxt == "_")
    return False


_IDENT = r"[A-Za-z_][A-Za-z0-9_]*"
_AFTER_DOT = re.compile(r"\.(" + _IDENT + r")")
_BEFORE_DOT = re.compile(r"(" + _IDENT + r")\.(?=[A-Za-z_])")
_DECL_SLOT = re.compile(r"(" + _IDENT + r")[ \t]*(?=[=←])")


def _declined_spellings(text: str, mapping: dict[str, str]) -> set[str]:
    """Keyword spellings a code region uses as identifiers, not as keywords.

    Faber permits a keyword spelling as an identifier, so `nomen` the keyword
    and `nomen` a field cannot be told apart by the token alone. A spelling
    that names a member or a member's receiver (either side of `.`) *and* fills
    a declaration or field-key slot is an identifier: rewriting only some of
    its occurrences would split one example across two spellings, so decline
    every occurrence in the region.
    """
    members = {match.group(1) for match in _AFTER_DOT.finditer(text)}
    members |= {match.group(1) for match in _BEFORE_DOT.finditer(text)}
    if not any(name in mapping for name in members):
        return set()
    slots = {match.group(1) for match in _DECL_SLOT.finditer(text)}
    return {name for name in members if name in slots and name in mapping}


def _compound_at(text: str, end: int, key: str, mapping: dict[str, str]) -> tuple[str, int] | None:
    match = re.match(r"(?:_[^\W_]+)+", text[end:])
    if not match:
        return None
    candidate = key + match.group(0)
    if candidate not in mapping:
        return None
    return candidate, end + match.end()


def _keywordish(text: str, mapping: dict[str, str]) -> bool:
    """True when a code span is Faber source rather than an English phrase."""
    if any(ch in text for ch in _GLYPHS):
        return True
    for match in WORD.finditer(text):
        key = match.group(0)
        if key in {"in", "per", "est"}:
            continue
        if key in mapping or _compound_at(text, match.end(), key, mapping):
            return True
    return False


def _project_compounds(text: str, mapping: dict[str, str]) -> str:
    keys = sorted((key for key in mapping if "_" in key), key=len, reverse=True)
    if not keys:
        return text
    pattern = re.compile("|".join(rf"(?<![\w]){re.escape(key)}(?![\w])" for key in keys))

    def replace(match: re.Match) -> str:
        if _guarded(text, match.start(), match.end()):
            return match.group(0)
        return mapping[match.group(0)]

    return pattern.sub(replace, text)


def _project_non_est(text: str, mapping: dict[str, str]) -> str:
    """`non est` is the identity-negation phrase; token order in English is `is not`."""
    if mapping.get("non") != "not" or mapping.get("est") != "is":
        return text
    return re.sub(r"(?<![\w_])non(\s+)est(?![\w_])", r"is\1not", text)


def project_prose(text: str, mapping: dict[str, str], *, declined: set[str] | None = None) -> str:
    allowed = {k: v for k, v in mapping.items() if k in SHORT_SAFE or (len(k) >= 4 and k not in HOMOGRAPHS)}
    text = _project_compounds(text, mapping)
    text = _project_non_est(text, mapping)

    def replace(match: re.Match) -> str:
        key = match.group(0)
        if declined and key in declined:
            return key
        if key not in allowed or _guarded(text, match.start(), match.end()):
            return key
        return allowed[key]

    return WORD.sub(replace, text)


def project_code(
    text: str,
    mapping: dict[str, str],
    *,
    exact_short: bool = False,
    declined: set[str] | None = None,
) -> str:
    """Project code tokens, protecting strings, paths, labels, and unsafe comments."""
    if exact_short and text.strip() in {"in", "per", "est"}:
        token = text.strip()
        leading = text[:len(text) - len(text.lstrip())]
        trailing = text[len(text.rstrip()):]
        return leading + mapping.get(token, token) + trailing
    if declined is None:
        declined = _declined_spellings(text, mapping)
    keywordish = _keywordish(text, mapping)
    out: list[str] = []
    i = 0
    quote: str | None = None
    while i < len(text):
        ch = text[i]
        if quote:
            out.append(ch)
            if ch == "\\" and i + 1 < len(text):
                i += 1
                out.append(text[i])
            elif ch == quote:
                quote = None
            i += 1
            continue
        if ch in "\"'":
            quote = ch
            out.append(ch)
            i += 1
            continue
        if ch == "#":
            end = text.find("\n", i)
            if end < 0:
                end = len(text)
            anchor = re.match(r"#[A-Za-z0-9_-]+", text[i:end])
            if anchor and anchor.end() == end - i:
                out.append(text[i:end])
                i = end
                continue
            comment = _project_non_est(_project_compounds(text[i:end], mapping), mapping)

            def comment_replace(m: re.Match) -> str:
                key = m.group(0)
                if key in declined or _guarded(comment, m.start(), m.end()):
                    return key
                if len(key) < 4 and key not in SHORT_SAFE:
                    # `in` / `per` / `est` are English words in a comment, and
                    # keywords when the comment names them as code.
                    if key in {"in", "per", "est"} and comment[m.start() - 1:m.start()] == "`" and comment[m.end():m.end() + 1] == "`":
                        return mapping.get(key, key)
                    return key
                return mapping.get(key, key)

            out.append(WORD.sub(comment_replace, comment))
            i = end
            continue
        match = WORD.match(text, i)
        if match:
            key = match.group(0)
            compound = _compound_at(text, match.end(), key, mapping)
            if compound and compound[0] not in declined and not _guarded(text, i, compound[1]):
                out.append(mapping[compound[0]])
                i = compound[1]
                continue
            replace = _whole_token(text, i, match.end()) and not _guarded(text, i, match.end())
            if key in declined or (key in {"in", "per", "est"} and not keywordish):
                replace = False
            if key == "non" and replace:
                phrase = re.match(r"(\s+)est(?![\w_])", text[match.end():])
                if phrase:
                    out.append("is" + phrase.group(1) + "not")
                    i = match.end() + phrase.end()
                    continue
            out.append(mapping.get(key, key) if replace else key)
            i = match.end()
            continue
        out.append(ch)
        i += 1
    return "".join(out)


def _project_inline(line: str, mapping: dict[str, str], *, declined: set[str] | None = None) -> str:
    protected: list[str] = []
    def hold(match: re.Match) -> str:
        protected.append(match.group(0))
        return f"\x00{len(protected) - 1}\x00"
    line = re.sub(r"\]\([^)]*\)|\{#[^}]*\}|<[^>\n]*>", hold, line)
    parts = re.split(r"(`+[^`]*`+)", line)
    for i, part in enumerate(parts):
        if part.startswith("`") and part.endswith("`"):
            run = len(part) - len(part.lstrip("`"))
            parts[i] = part[:run] + project_code(part[run:-run], mapping, exact_short=True, declined=declined) + part[-run:]
        else:
            parts[i] = project_prose(part, mapping, declined=declined)
    result = "".join(parts)
    return re.sub(r"\x00(\d+)\x00", lambda m: protected[int(m.group(1))], result)


def project_markdown(text: str, mapping: dict[str, str], *, relative_path: str = "", reader: str = "en", example: bool = False) -> str:
    """Project one Markdown document, or one bare Faber example when `example`.

    A Markdown page mixes prose with code regions, so identifier decline is
    scoped to each fence or span. A bare example is all code: its decline is
    computed once over the whole text, so a keyword-shaped field keeps one
    spelling across declaration, construction, and member access.
    """
    rel = relative_path.replace("\\", "/")
    if rel.endswith("reference/grammar.md") or "/reference/grammar/" in rel:
        return text
    lines = text.splitlines(keepends=True)
    declined = _declined_spellings(text, mapping) if example else None
    out: list[str] = []
    fence: str | None = None
    skip_fence = False
    fence_body: list[str] = []
    frontmatter = bool(lines and lines[0].strip() == "+++")
    first_frontmatter = frontmatter
    for line in lines:
        stripped = line.strip()
        if frontmatter:
            if stripped == "+++" and not first_frontmatter:
                frontmatter = False
                out.append(line)
                continue
            first_frontmatter = False
            m = re.match(r"^(\s*(?:description|summary)\s*=\s*)(\"(?:[^\"]|\\.)*\"|'[^']*')(\s*(?:#.*)?\s*)$", line.rstrip("\n"))
            if m:
                quote = m.group(2)[0]
                value = m.group(2)[1:-1]
                out.append(m.group(1) + quote + project_prose(value, mapping) + quote + m.group(3) + ("\n" if line.endswith("\n") else ""))
            else:
                out.append(line)
            continue
        if fence:
            if stripped.startswith(fence):
                if not skip_fence:
                    region_declined = _declined_spellings("".join(fence_body), mapping)
                    for body_line in fence_body:
                        out.append(project_code(body_line.rstrip("\n"), mapping, declined=region_declined) + ("\n" if body_line.endswith("\n") else ""))
                else:
                    out.extend(fence_body)
                out.append(line)
                fence = None
                skip_fence = False
                fence_body = []
            elif skip_fence:
                out.append(line)
            else:
                fence_body.append(line)
            continue
        if stripped.startswith("```"):
            fence = stripped[:len(stripped) - len(stripped.lstrip("`"))]
            info = stripped[len(fence):]
            locale = re.search(r"(?:^|\s)locale=([^\s]+)", info)
            skip_fence = bool(locale and locale.group(1) != reader)
            fence_body = []
            out.append(line)
            continue
        out.append(_project_inline(line, mapping, declined=declined))
    if fence is not None and fence_body:
        # An unterminated fence: project its body the same way a closed one is.
        if skip_fence:
            out.extend(fence_body)
        else:
            region_declined = _declined_spellings("".join(fence_body), mapping)
            for body_line in fence_body:
                out.append(project_code(body_line.rstrip("\n"), mapping, declined=region_declined) + ("\n" if body_line.endswith("\n") else ""))
    return "".join(out)


def project_corpus_source(source: str, mapping: dict[str, str], reader: str, faber: str) -> str:
    """Convert/project one corpus record without changing identity or path fields."""
    parts = source.split("+++", 2)
    if len(parts) != 3:
        return source
    front, body = parts[1], parts[2]
    if reader != "la":
        try:
            with tempfile.TemporaryDirectory(prefix="corpus-reader-") as tmp:
                path = Path(tmp) / "example.fab"
                path.write_text(body.lstrip("\n"), encoding="utf-8")
                result = subprocess.run([faber, "convert", "--from", "la", "--to", reader, "--stdout", str(path)], text=True, capture_output=True)
            if result.returncode == 0:
                body = re.sub(r"\A\+\+\+\n.*?\n\+\+\+\n", "", result.stdout, count=1, flags=re.S)
            else:
                print(f"WARNING: corpus convert failed for {reader}; projecting source tokens", file=__import__("sys").stderr)
        except OSError:
            pass
    def value_replace(match: re.Match) -> str:
        key, quote, value = match.group(1), match.group(2), match.group(3)
        if key == "syntax":
            value = project_code(value, mapping)
            # Generic placeholders such as <name> are not pack terms, but are kept explicit.
            value = re.sub(r"<[^>]+>", lambda m: m.group(0), value)
        else:
            value = project_prose(value, mapping)
        return f"{key} = {quote}{value}{quote}"
    front = re.sub(r'(?m)^(summary|syntax)\s*=\s*(["\'])(.*?)\2\s*$', value_replace, front)
    return "+++" + front + "+++\n" + project_code(body, mapping)
