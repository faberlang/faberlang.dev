#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Speculum site generator — Python port of the Faber generator.

Byte-equivalent port of generator/src/*.fab: main.fab (CLI dispatch +
deriva_iter), types.fab, frontmatter.fab, string_util.fab, span.fab,
anchor.fab, fence.fab, link_prefix.fab, document_ir.fab, markdown.fab,
html.fab, nav.fab, corpus.fab. The Faber sources are the oracle until
unit U3 deletes them; faithful replication includes their quirks (the
one-element `field_lista` sources list, the fence extractor's close_idx
jump, unknown-locale og:locale passthrough, ...).

CLI contract (identical to speculum-run.sh forwarding to main.fab):

    --page <iter> <source.md> <site_locale> [reader_locale] [stylesheet]
    --corpus-markdown <term> <bundle> [display]
    --corpus-bundle <bundle> [site_locale] [reader_locale] [stylesheet] [display]
    --corpus-markdown-bundle <bundle> [display]
    --corpus <term> <bundle> <site_locale> [reader_locale] [stylesheet] [display]
    --alias <alias> <canonical> <site_locale> [stylesheet]
    bare: <source.md> [site_locale] [reader_locale] [stylesheet]

Stdlib only; compatible with Python 3.9. Output goes to stdout exactly as
the Faber binary prints it (the rendered string plus a trailing newline).
"""

from __future__ import annotations

import sys

# ==========================================================================
# string_util.fab
# ==========================================================================


def nl():
    return "\n"


def initium_index(haystack, needle):
    # Find the first index of needle; -1 when absent; 0 for an empty needle.
    return haystack.find(needle)


def initium_index_post(haystack, needle, start):
    # First index of needle at or after start; Faber guards start >= hlen.
    if len(needle) == 0:
        return start
    if start >= len(haystack):
        return -1
    if len(haystack) - start < len(needle):
        return -1
    # find(needle, start) is already absolute (Faber slices then adds start).
    return haystack.find(needle, start)


def initium_cum(text, prefix):
    return text.startswith(prefix)


def divide(text, delim):
    # Faber divide keeps empty parts; str.split has the same shape.
    if len(delim) == 0:
        return [text]
    return text.split(delim)


def recide(text):
    # Trim leading and trailing whitespace.
    return text.strip()


def littera_ad(s, i):
    # Single-character textus at position i.
    return s[i]


def est_digitus(ch):
    return ch in "0123456789"


# ==========================================================================
# frontmatter.fab
# ==========================================================================


def strip_quotes(value):
    # Remove surrounding double quotes only.
    length = len(value)
    if length < 2:
        return value
    if value[0] == '"' and value[length - 1] == '"':
        return value[1:length - 1]
    return value


def parse_toml_lines(toml_text):
    # Line-based key = "value" parsing; later duplicate keys overwrite.
    result = {}
    for linea in divide(toml_text, nl()):
        trimmed = recide(linea)
        if len(trimmed) == 0:
            continue
        if initium_cum(trimmed, "#"):
            continue
        if initium_cum(trimmed, "["):
            continue
        eq_pos = initium_index(trimmed, "=")
        if eq_pos < 0:
            continue
        key = recide(trimmed[0:eq_pos])
        value_raw = recide(trimmed[eq_pos + 1:])
        result[key] = strip_quotes(value_raw)
    return result


def fm_divide(source):
    # Split +++ frontmatter from body. Returns (fields, body).
    plus3 = "+++"
    primus = initium_index(source, plus3)
    if primus < 0:
        return {}, source
    secundus = initium_index_post(source, plus3, primus + 3)
    if secundus < 0:
        return {}, source
    fm_text = source[primus + 3:secundus]
    post_fm = source[secundus + 3:]
    body = recide(post_fm)
    fields = parse_toml_lines(fm_text)
    return fields, body


# ==========================================================================
# types.fab
# ==========================================================================


class Pagina(object):
    def __init__(self, iter_, titulus, section, corpus, metadata, sources,
                 site_locale, reader_locale):
        self.iter = iter_
        self.titulus = titulus
        self.section = section
        self.corpus = corpus
        self.metadata = metadata
        self.sources = sources
        self.site_locale = site_locale
        self.reader_locale = reader_locale


def field_vale(fields, key, fallback):
    if key in fields:
        return fields[key]
    return fallback


def field_lista(fields, key):
    # Quirk ported from types.fab: the value is NOT parsed as an array; the
    # raw (quote-stripped) frontmatter string is wrapped in a one-element list.
    try:
        raw = fields[key]
    except KeyError:
        return []
    return [raw]


def aedifica_paginam(iter_, source, site_locale, reader_locale):
    fields, body = fm_divide(source)
    titulus = field_vale(fields, "title", iter_)
    section = field_vale(fields, "section", "misc")
    sources = field_lista(fields, "sources")
    return Pagina(iter_, titulus, section, body, fields, sources,
                  site_locale, reader_locale)


# ==========================================================================
# document_ir.fab
# ==========================================================================

# Node shapes: ("text", value), ("frag", [children]),
# ("elem", tag, [(name, value), ...], [children]).


def attr(nomen, valor):
    return (nomen, valor)


def ir_text(value):
    return ("text", value)


def ir_frag(children):
    return ("frag", children)


def ir_element(tag, attrs, children):
    return ("elem", tag, attrs, children)


def ir_leaf(tag, attrs, value):
    return ("elem", tag, attrs, [ir_text(value)])


def ir_void(tag, attrs):
    return ("elem", tag, attrs, [])


def ir_is_empty(node):
    kind = node[0]
    if kind == "text":
        return node[1] == ""
    if kind == "frag":
        return len(node[1]) == 0
    return False


def html_escape(value):
    # Escape set is & " < > only; single quotes pass through.
    return (value.replace("&", "&amp;")
                 .replace("\"", "&quot;")
                 .replace("<", "&lt;")
                 .replace(">", "&gt;"))


def attr_html(item):
    nomen, valor = item
    if valor == "":
        return " " + nomen
    return " " + nomen + "=\"" + html_escape(valor) + "\""


def attrs_html(attrs):
    return "".join(attr_html(item) for item in attrs)


VOID_ELEMENTS = ("area", "base", "br", "col", "embed", "hr", "img", "input",
                 "link", "meta", "param", "source", "track", "wbr")


def is_void_element(tag):
    return tag in VOID_ELEMENTS


def node_html(node):
    kind = node[0]
    if kind == "text":
        return html_escape(node[1])
    if kind == "frag":
        return "".join(node_html(child) for child in node[1])
    tag = node[1]
    attrs = node[2]
    children = node[3]
    open_tag = "<" + tag + attrs_html(attrs) + ">"
    if is_void_element(tag):
        return open_tag
    body = "".join(node_html(child) for child in children)
    return open_tag + body + "</" + tag + ">"


def document_html(root):
    return "<!DOCTYPE html>\n" + node_html(root)


# ==========================================================================
# span.fab
# ==========================================================================

# Exact-match classification against the closed identifier set.
SPAN_KEYWORDS = (
    "functio", "fixum", "varia", "genus", "importa", "si", "sin", "secus",
    "dum", "fac", "itera", "perge", "rumpe", "redde", "casu", "ceterum",
    "elige", "discerne", "tempta", "cape", "demum", "falsum", "verum",
    "nihil", "et", "aut", "non", "est", "nota", "mone", "scribe", "vide",
    "incipit", "argumenta", "ex", "de", "in", "ut",
)

SPAN_TYPES = (
    "textus", "numerus", "fractus", "bivalens", "vacuum", "lista", "tabula",
    "copia", "cursor", "instans", "octeti", "json", "regex",
)


def span_classifica(span):
    trimmed = recide(span)
    if trimmed in SPAN_KEYWORDS:
        return "kw"
    if trimmed in SPAN_TYPES:
        return "typ"
    return "code"


def genera_span_node(span):
    cls = span_classifica(span)
    if cls == "kw":
        return ir_leaf("code", [attr("class", "kw")], span)
    if cls == "typ":
        return ir_leaf("code", [attr("class", "typ")], span)
    return ir_leaf("code", [], span)


# ==========================================================================
# anchor.fab
# ==========================================================================


def anchor_parse_heading(level, rest, line_num):
    trimmed = recide(rest)
    brace_start = initium_index(trimmed, "{#")
    if brace_start >= 0:
        brace_end = initium_index_post(trimmed, "}", brace_start)
        if brace_end > brace_start:
            anchor = trimmed[brace_start + 2:brace_end]
            text = recide(trimmed[0:brace_start])
            return (level, text, anchor, line_num)
    return (level, trimmed, "", line_num)


def anchor_extract(source):
    # Note (faithful port): the six checks are independent `si` blocks, so a
    # "###### " line appends both the level-6 and the level-5 heading.
    headings = []
    lines = divide(source, nl())
    line_num = 0
    for linea in lines:
        line_num += 1
        trimmed = recide(linea)
        if initium_cum(trimmed, "###### "):
            headings.append(anchor_parse_heading(6, trimmed[7:], line_num))
        if initium_cum(trimmed, "##### "):
            headings.append(anchor_parse_heading(5, trimmed[6:], line_num))
        if initium_cum(trimmed, "#### "):
            headings.append(anchor_parse_heading(4, trimmed[5:], line_num))
        if initium_cum(trimmed, "### "):
            headings.append(anchor_parse_heading(3, trimmed[4:], line_num))
        if initium_cum(trimmed, "## "):
            headings.append(anchor_parse_heading(2, trimmed[3:], line_num))
        if initium_cum(trimmed, "# "):
            headings.append(anchor_parse_heading(1, trimmed[2:], line_num))
    return headings


# ==========================================================================
# fence.fab
# ==========================================================================


def fence_parse_info(info, source, linea):
    locale = "la"
    modus = "fluid"
    outcome = "compiles"
    if len(info) > 0:
        for token in divide(info, " "):
            if initium_cum(token, "locale="):
                locale = token[7:]
            if token == "pinned":
                modus = "pinned"
            if token == "fluid":
                modus = "fluid"
            if token == "compiles":
                outcome = "compiles"
            if token == "rejects":
                outcome = "rejects"
            if token == "output-matches":
                outcome = "output-matches"
    return {"locale": locale, "modus": modus, "outcome": outcome,
            "source": source, "linea": linea}


def fence_extract(source):
    # Faithful port, including the close_idx jump: once the closing fence is
    # found, close_idx is set to the line count, so the extracted source runs
    # to end-of-file (the fence list is unused by the HTML path).
    fences = []
    lines = divide(source, nl())
    n = len(lines)
    idx = 0
    while idx < n:
        linea = lines[idx]
        trimmed = recide(linea)
        if not initium_cum(trimmed, "```faber"):
            idx += 1
            continue
        info = recide(trimmed[8:])
        close_idx = idx + 1
        found_close = False
        while close_idx < n:
            close_line = lines[close_idx]
            if recide(close_line) == "```":
                found_close = True
                close_idx = n
            if not found_close:
                close_idx += 1
        if not found_close:
            idx += 1
            continue
        code = ""
        j = idx + 1
        while j < close_idx:
            if len(code) > 0:
                code += nl()
            code += lines[j]
            j += 1
        fences.append(fence_parse_info(info, code, idx + 1))
        idx = close_idx + 1
    return fences


# ==========================================================================
# link_prefix.fab
# ==========================================================================


def est_content_path(href):
    if href == "/":
        return True
    if href == "/404.html":
        return True
    if href == "/open-source.html":
        return True
    if href == "/localization.html":
        return True
    if initium_cum(href, "/start/"):
        return True
    if initium_cum(href, "/start") and len(href) == 6:
        return True
    if initium_cum(href, "/cheatsheet/"):
        return True
    if initium_cum(href, "/releases/"):
        return True
    if initium_cum(href, "/targets/"):
        return True
    if initium_cum(href, "/language/"):
        return True
    if initium_cum(href, "/toolchain/"):
        return True
    if initium_cum(href, "/libraries/"):
        return True
    if initium_cum(href, "/reference/"):
        return True
    if initium_cum(href, "/corpus/"):
        return True
    if initium_cum(href, "/syntax/"):
        return True
    if initium_cum(href, "/features/"):
        return True
    if initium_cum(href, "/tooling/"):
        return True
    if initium_cum(href, "/ecosystem/"):
        return True
    if initium_cum(href, "/history/"):
        return True
    if initium_cum(href, "/references/"):
        return True
    return False


def content_href(href, site_locale):
    if len(site_locale) == 0:
        return href
    if not initium_cum(href, "/"):
        return href
    if not est_content_path(href):
        return href
    # Already-locale-absolute hrefs pass through on every locale.
    if initium_cum(href, "/en-US/"):
        return href
    return "/" + site_locale + href


# ==========================================================================
# markdown.fab
# ==========================================================================


def append_text_range(nodes, source, start, end):
    if end > start:
        nodes.append(ir_text(source[start:end]))


def inline_leaf(tag, value):
    return ir_element(tag, [], [ir_text(value)])


def genera_inline(text, site_locale):
    nodes = []
    length = len(text)
    i = 0
    plain_start = 0
    while i < length:
        # Backtick code span.
        if littera_ad(text, i) == "`":
            j = i + 1
            found = False
            while j < length:
                if littera_ad(text, j) == "`":
                    found = True
                    break
                j += 1
            if found:
                append_text_range(nodes, text, plain_start, i)
                nodes.append(genera_span_node(text[i + 1:j]))
                i = j + 1
                plain_start = i
                continue
        # Link span: [label](href); label/href scans stop at a newline.
        if littera_ad(text, i) == "[":
            j = i + 1
            found_label = False
            while j < length:
                if littera_ad(text, j) == "]":
                    found_label = True
                    break
                if littera_ad(text, j) == "\n":
                    break
                j += 1
            if found_label and (j + 1 < length) and littera_ad(text, j + 1) == "(":
                k = j + 2
                found_href = False
                while k < length:
                    if littera_ad(text, k) == ")":
                        found_href = True
                        break
                    if littera_ad(text, k) == "\n":
                        break
                    k += 1
                if found_href:
                    append_text_range(nodes, text, plain_start, i)
                    label = text[i + 1:j]
                    href = content_href(text[j + 2:k], site_locale)
                    nodes.append(ir_element("a", [attr("href", href)],
                                            genera_inline(label, site_locale)))
                    i = k + 1
                    plain_start = i
                    continue
        # Bold span: **text**, scanned from i+2 while j+1 < len.
        if i + 1 < length and littera_ad(text, i) == "*" and littera_ad(text, i + 1) == "*":
            j = i + 2
            found = False
            while j + 1 < length:
                if littera_ad(text, j) == "*" and littera_ad(text, j + 1) == "*":
                    found = True
                    break
                j += 1
            if found:
                append_text_range(nodes, text, plain_start, i)
                nodes.append(inline_leaf("strong", text[i + 2:j]))
                i = j + 2
                plain_start = i
                continue
        # Italic span: *text*; a stranded "**" skips both asterisks.
        if littera_ad(text, i) == "*":
            if i + 1 < length and littera_ad(text, i + 1) == "*":
                i += 2
                continue
            j = i + 1
            found = False
            while j < length:
                if littera_ad(text, j) == "*":
                    found = True
                    break
                j += 1
            if found and j > i + 1:
                append_text_range(nodes, text, plain_start, i)
                nodes.append(inline_leaf("em", text[i + 1:j]))
                i = j + 1
                plain_start = i
                continue
        i += 1
    append_text_range(nodes, text, plain_start, length)
    return nodes


def extract_anchor(heading):
    brace = initium_index(heading, " {#")
    if brace < 0:
        return (heading, "")
    close = initium_index_post(heading, "}", brace + 3)
    if close < 0:
        return (heading, "")
    anchor = heading[brace + 3:close]
    title = recide(heading[0:brace])
    return (title, anchor)


def genera_heading_node(tag, heading, site_locale):
    title, anchor = extract_anchor(heading)
    children = genera_inline(title, site_locale)
    if len(anchor) > 0:
        return ir_element(tag, [attr("id", anchor)], children)
    return ir_element(tag, [], children)


def est_separator(linea):
    if initium_index(linea, "|---") >= 0:
        return True
    if initium_index(linea, "|:--") >= 0:
        return True
    if initium_index(linea, "| ---") >= 0:
        return True
    return False


def split_table_row(row):
    # Leading/trailing delimiters stripped; empty cells skipped; \ escapes |.
    cells = []
    trimmed = recide(row)
    length = len(trimmed)
    if length == 0:
        return cells
    start = 0
    i = 0
    if littera_ad(trimmed, 0) == "|":
        start = 1
        i = 1
    while i < length:
        if littera_ad(trimmed, i) == "|" and not (i > 0 and littera_ad(trimmed, i - 1) == "\\"):
            cell = recide(trimmed[start:i])
            if len(cell) > 0:
                cells.append(cell)
            start = i + 1
        i += 1
    if start < length:
        cell = recide(trimmed[start:length])
        if len(cell) > 0:
            cells.append(cell)
    return cells


def row_cells(tag, cells, site_locale):
    return [ir_element(tag, [], genera_inline(cell, site_locale))
            for cell in cells]


def table_node(headers, rows, site_locale):
    head_row = ir_element("tr", [], row_cells("th", headers, site_locale))
    thead = ir_element("thead", [], [head_row])
    tbody = ir_element("tbody", [], rows)
    table = ir_element("table", [], [thead, tbody])
    return ir_element("div", [attr("class", "table-scroll")], [table])


def est_ordo_libera(linea):
    if len(linea) < 2:
        return False
    if not littera_ad(linea, 0) == "-":
        return False
    return littera_ad(linea, 1) == " "


def longitudo_ordinis(linea):
    # Width of an ordered list marker ("1. ", "12. "), or 0 when none.
    length = len(linea)
    i = 0
    while i < length:
        if not est_digitus(linea[i]):
            break
        i += 1
    if i == 0:
        return 0
    if i + 1 >= length:
        return 0
    if not littera_ad(linea, i) == ".":
        return 0
    if not littera_ad(linea, i + 1) == " ":
        return 0
    return i + 2


def est_citatio(linea):
    if len(linea) < 2:
        return False
    if not littera_ad(linea, 0) == ">":
        return False
    return littera_ad(linea, 1) == " "


def est_initium_blocki(linea):
    if len(linea) == 0:
        return True
    if initium_cum(linea, "#"):
        return True
    if initium_cum(linea, "```"):
        return True
    if est_ordo_libera(linea):
        return True
    if longitudo_ordinis(linea) > 0:
        return True
    if est_citatio(linea):
        return True
    if littera_ad(linea, 0) == "|":
        return True
    return False


def converte_nodes(source, site_locale):
    lines = divide(source, nl())
    n = len(lines)
    result = []
    i = 0
    while i < n:
        linea = recide(lines[i])

        # Blank lines.
        if len(linea) == 0:
            i += 1
            continue

        # Fenced code block.
        if initium_cum(linea, "```"):
            info = recide(linea[3:])
            code = ""
            i += 1
            while i < n:
                fence_check = recide(lines[i])
                if initium_cum(fence_check, "```"):
                    i += 1
                    break
                if len(code) > 0:
                    code += nl()
                code += lines[i]
                i += 1
            code_attrs = []
            if len(info) > 0:
                code_attrs = [attr("class", "lang-" + info)]
            code_node = ir_element("code", code_attrs, [ir_text(code)])
            result.append(ir_element("pre", [attr("class", "faber-code")],
                                     [code_node]))
            continue

        # Headings, h6 first.
        if initium_cum(linea, "###### "):
            result.append(genera_heading_node("h6", linea[7:], site_locale))
            i += 1
            continue
        if initium_cum(linea, "##### "):
            result.append(genera_heading_node("h5", linea[6:], site_locale))
            i += 1
            continue
        if initium_cum(linea, "#### "):
            result.append(genera_heading_node("h4", linea[5:], site_locale))
            i += 1
            continue
        if initium_cum(linea, "### "):
            result.append(genera_heading_node("h3", linea[4:], site_locale))
            i += 1
            continue
        if initium_cum(linea, "## "):
            result.append(genera_heading_node("h2", linea[3:], site_locale))
            i += 1
            continue

        # Pipe table.
        if littera_ad(linea, 0) == "|":
            if i + 1 < n and est_separator(recide(lines[i + 1])):
                headers = split_table_row(linea)
                rows = []
                i += 2
                while i < n:
                    l = recide(lines[i])
                    if len(l) == 0:
                        break
                    if not littera_ad(l, 0) == "|":
                        break
                    rows.append(ir_element("tr", [],
                                           row_cells("td", split_table_row(l),
                                                     site_locale)))
                    i += 1
                result.append(table_node(headers, rows, site_locale))
                continue

        # Unordered list (flat, continuation lines folded in).
        if est_ordo_libera(linea):
            items = []
            while i < n:
                l = recide(lines[i])
                if not est_ordo_libera(l):
                    break
                item = l[2:]
                i += 1
                while i < n:
                    cont = recide(lines[i])
                    if est_initium_blocki(cont):
                        break
                    item = item + nl() + cont
                    i += 1
                items.append(ir_element("li", [], genera_inline(item, site_locale)))
            result.append(ir_element("ul", [], items))
            continue

        # Ordered list (flat, continuation lines folded in).
        if longitudo_ordinis(linea) > 0:
            items = []
            while i < n:
                l = recide(lines[i])
                marker = longitudo_ordinis(l)
                if marker == 0:
                    break
                item = l[marker:]
                i += 1
                while i < n:
                    cont = recide(lines[i])
                    if est_initium_blocki(cont):
                        break
                    item = item + nl() + cont
                    i += 1
                items.append(ir_element("li", [], genera_inline(item, site_locale)))
            result.append(ir_element("ol", [], items))
            continue

        # Blockquote with lazy continuation.
        if est_citatio(linea):
            quote = ""
            while i < n:
                l = recide(lines[i])
                if est_citatio(l):
                    if len(quote) > 0:
                        quote += nl()
                    quote += l[2:]
                    i += 1
                    continue
                if not est_initium_blocki(l):
                    quote = quote + nl() + l
                    i += 1
                    continue
                break
            quote_para = ir_element("p", [], genera_inline(quote, site_locale))
            result.append(ir_element("blockquote", [], [quote_para]))
            continue

        # Paragraph; continuation lines fold in with a literal newline Text node.
        para = genera_inline(linea, site_locale)
        i += 1
        while i < n:
            l = recide(lines[i])
            if est_initium_blocki(l):
                break
            para.append(ir_text(nl()))
            para.extend(genera_inline(l, site_locale))
            i += 1
        result.append(ir_element("p", [], para))
    return result


# ==========================================================================
# nav.fab
# ==========================================================================


def finge_item(label, href, section, children=None):
    return {"label": label, "href": href, "section": section,
            "children": children if children is not None else []}


def finge_en_item(label, href, section):
    # en-US-only families keep absolute /en-US hrefs on every locale.
    return finge_item(label, "/en-US" + href, section)


def finge_branch(label, href, section, children):
    return finge_item(label, href, section, children)


def nav_tree():
    behavior_children = [
        finge_en_item("Types before names", "/language/behavior/type-first.html", "behavior-type-first"),
        finge_en_item("The glyph law", "/language/behavior/glyph-law.html", "behavior-glyph-law"),
        finge_en_item("Math in the ether", "/language/behavior/numeric-widths.html", "behavior-numeric-widths"),
        finge_en_item("Sealed reader locales", "/language/behavior/sealed-locales.html", "behavior-sealed-locales"),
        finge_en_item("A program is a package", "/language/behavior/packages.html", "behavior-packages"),
        finge_en_item("Errors as values, tests as declarations", "/language/behavior/errors-and-tests.html", "behavior-errors-and-tests"),
    ]

    grammar_children = [
        finge_item("Grammar overview", "/reference/grammar.html", "grammar"),
        finge_en_item("Programs, regions & imports", "/reference/grammar/program.html", "grammar-program"),
        finge_en_item("Declarations & bindings", "/reference/grammar/declarations.html", "grammar-declarations"),
        finge_en_item("Annotations & directives", "/reference/grammar/annotations.html", "grammar-annotations"),
        finge_en_item("Types & contracts", "/reference/grammar/types.html", "grammar-types"),
        finge_en_item("Statements & control flow", "/reference/grammar/statements.html", "grammar-statements"),
        finge_en_item("Expressions & operators", "/reference/grammar/expressions.html", "grammar-expressions"),
        finge_en_item("Patterns & destructuring", "/reference/grammar/patterns.html", "grammar-patterns"),
        finge_en_item("Error channel", "/reference/grammar/errors.html", "grammar-errors"),
        finge_en_item("Lexical structure & glyphs", "/reference/grammar/lexical.html", "grammar-lexical"),
    ]

    start_items = [
        finge_item("Start here", "/start/", "start"),
        finge_en_item("Releases", "/releases/", "releases"),
    ]

    language_items = [
        finge_en_item("Overview", "/language/overview.html", "overview"),
        finge_branch("Behavior", "", "", behavior_children),
        finge_branch("Grammar", "", "", grammar_children),
        finge_item("Terms A–Z", "/corpus/az.html", "corpus"),
        finge_item("Cheat sheet", "/cheatsheet/", "cheatsheet"),
    ]

    hir_children = [
        finge_en_item("Rust", "/targets/rust.html", "rust"),
        finge_en_item("TypeScript", "/targets/ts.html", "ts"),
        finge_en_item("Go", "/targets/go.html", "go"),
        finge_en_item("Faber", "/targets/faber.html", "faber"),
    ]

    mir_children = [
        finge_en_item("LLVM IR", "/targets/llvm-text.html", "llvm-text"),
        finge_en_item("WebAssembly text", "/targets/wasm-text.html", "wasm-text"),
    ]

    gpu_children = [
        finge_en_item("Metal", "/targets/metal-text.html", "metal-text"),
        finge_en_item("WGSL", "/targets/wgsl-text.html", "wgsl-text"),
    ]

    targets_items = [
        finge_en_item("All targets", "/targets/", "targets"),
        finge_branch("Application · HIR", "", "", hir_children),
        finge_branch("Systems · MIR", "", "", mir_children),
        finge_branch("Device · GPU", "", "", gpu_children),
        finge_item("Target matrix", "/toolchain/target-matrix.html", "target-matrix"),
    ]

    locales_items = [
        finge_item("Reader locales", "/language/reader-locales.html", "locales"),
        finge_en_item("Keyword reference", "/language/locales/keywords.html", "locales"),
        finge_en_item("Locale examples", "/language/locales/examples.html", "locales"),
        finge_en_item("Diagnostics by locale", "/language/locales/diagnostics.html", "locales"),
    ]

    libraries_items = [
        finge_item("Norma — stdlib", "/libraries/norma.html", "libraries"),
        finge_item("Triga — graphics", "/libraries/triga.html", "libraries"),
        finge_item("Gradus — autograd", "/libraries/gradus.html", "libraries"),
        finge_item("Tela — views", "/libraries/tela.html", "libraries"),
        finge_item("Inferentia — inference", "/libraries/inferentia.html", "libraries"),
        finge_item("The corpus", "/libraries/corpus.html", "libraries"),
    ]

    return [
        {"id": "start", "label": "Start", "items": start_items},
        {"id": "language", "label": "The Language", "items": language_items},
        {"id": "targets", "label": "Targets", "items": targets_items},
        {"id": "locales", "label": "Reader locales", "items": locales_items},
        {"id": "libraries", "label": "Libraries", "items": libraries_items},
    ]


def subtree_habet_sectionem(item, active_section):
    if item["section"] == active_section and len(active_section) > 0:
        return True
    for child in item["children"]:
        if subtree_habet_sectionem(child, active_section):
            return True
    return False


def numerus_sectionis(groups, section):
    # One level of children only (faithful to nav.fab).
    n = 0
    for g in groups:
        for item in g["items"]:
            if item["section"] == section:
                n += 1
            for child in item["children"]:
                if child["section"] == section:
                    n += 1
    return n


def est_pagina(item, pagina_href, site_locale):
    return content_href(item["href"], site_locale) == pagina_href


def pagina_in_arbore(groups, pagina_href, site_locale):
    for g in groups:
        for item in g["items"]:
            if est_pagina(item, pagina_href, site_locale):
                return True
            for child in item["children"]:
                if est_pagina(child, pagina_href, site_locale):
                    return True
    return False


def est_activa(item, active_section, pagina_href, site_locale, section_n):
    if est_pagina(item, pagina_href, site_locale):
        return True
    if section_n == 1 and item["section"] == active_section:
        return True
    return False


def patet_brachium(item, active_section, pagina_href, site_locale):
    if subtree_habet_sectionem(item, active_section):
        return True
    for child in item["children"]:
        if est_pagina(child, pagina_href, site_locale):
            return True
    return False


def nav_link_node(item, active_section, pagina_href, site_locale, section_n):
    href = content_href(item["href"], site_locale)
    if est_activa(item, active_section, pagina_href, site_locale, section_n):
        return ir_leaf("a", [attr("href", href), attr("class", "active")],
                       item["label"])
    return ir_leaf("a", [attr("href", href)], item["label"])


def nav_branch_node(item, active_section, pagina_href, site_locale, section_n):
    attrs = [attr("class", "nav-branch")]
    if patet_brachium(item, active_section, pagina_href, site_locale):
        attrs.append(attr("open", ""))
    child_items = []
    for child in item["children"]:
        child_items.append(ir_element("li", [], [
            nav_link_node(child, active_section, pagina_href, site_locale,
                          section_n)]))
    summary = ir_leaf("summary", [], item["label"])
    listing = ir_element("ul", [], child_items)
    return ir_element("details", attrs, [summary, listing])


def nav_item_node(item, active_section, pagina_href, site_locale, section_n):
    if len(item["children"]) > 0:
        return ir_element("li", [], [
            nav_branch_node(item, active_section, pagina_href, site_locale,
                            section_n)])
    return ir_element("li", [], [
        nav_link_node(item, active_section, pagina_href, site_locale,
                      section_n)])


def nav_group_node(g, active_section, pagina_href, site_locale, section_n):
    items = []
    for item in g["items"]:
        items.append(nav_item_node(item, active_section, pagina_href,
                                   site_locale, section_n))
    heading = ir_leaf("div", [attr("class", "side-h")], g["label"])
    listing = ir_element("ul", [attr("class", "nav")], items)
    return ir_frag([heading, listing])


def genera_nav(active_section, pagina_href, site_locale):
    groups = nav_tree()
    section_n = 0
    if not pagina_in_arbore(groups, pagina_href, site_locale):
        section_n = numerus_sectionis(groups, active_section)
    nodes = []
    for g in groups:
        nodes.append(nav_group_node(g, active_section, pagina_href,
                                    site_locale, section_n))
    return ir_frag(nodes)


# ==========================================================================
# html.fab
# ==========================================================================


def situs_basis():
    return "https://faberlang.dev"


def pagina_rel_url(site_locale, iter_):
    prefix = "/" + site_locale
    if len(iter_) == 0:
        return prefix + "/"
    if iter_ == "index":
        return prefix + "/"
    ilen = len(iter_)
    if ilen >= 6:
        if iter_[ilen - 6:ilen] == "/index":
            return prefix + "/" + iter_[0:ilen - 6] + "/"
    if iter_ == "404":
        return prefix + "/404.html"
    return prefix + "/" + iter_ + ".html"


def pagina_canonical(site_locale, iter_):
    return situs_basis() + pagina_rel_url(site_locale, iter_)


def og_locale(site_locale):
    # Unknown locales return the site_locale string unchanged (faithful to
    # the code, not the comment beside it).
    if site_locale == "en-US":
        return "en_US"
    if site_locale == "th-TH":
        return "th_TH"
    if site_locale == "zh-Hans":
        return "zh_CN"
    if site_locale == "zh-Hant":
        return "zh_TW"
    if site_locale == "ar":
        return "ar_AR"
    if site_locale == "hi":
        return "hi_IN"
    if site_locale == "vi":
        return "vi_VN"
    return site_locale


def brevia_description(text, max_len):
    t = recide(text)
    if len(t) <= max_len:
        return t
    if max_len <= 3:
        return t[0:max_len]
    return t[0:max_len - 3] + "..."


def meta_plain(text):
    out = []
    for ch in text:
        if ch == "*" or ch == "`":
            continue
        out.append(ch)
    return recide("".join(out))


def line_meta_skip(linea):
    if initium_cum(linea, "#"):
        return True
    if initium_cum(linea, "```"):
        return True
    if initium_cum(linea, "|"):
        return True
    if initium_cum(linea, "+++"):
        return True
    return False


def primus_paragraphus(body):
    lines = divide(body, nl())
    acc = ""
    for linea in lines:
        trimmed = recide(linea)
        if len(trimmed) == 0:
            if len(acc) > 0:
                return meta_plain(acc)
        elif line_meta_skip(trimmed):
            if initium_cum(trimmed, "```"):
                if len(acc) > 0:
                    return meta_plain(acc)
        else:
            if len(acc) == 0:
                acc = trimmed
            else:
                acc = acc + " " + trimmed
    if len(acc) > 0:
        return meta_plain(acc)
    return ""


def pagina_description(pag):
    from_fm = field_vale(pag.metadata, "description", "")
    if len(from_fm) > 0:
        return brevia_description(from_fm, 160)
    from_body = primus_paragraphus(pag.corpus)
    if len(from_body) > 0:
        return brevia_description(from_body, 160)
    if pag.titulus == "Faber":
        return ("Faber programming language — package-oriented, Latin "
                "vocabulary, type-first static types. Agent-readable docs, "
                "install, and a cheat sheet.")
    return brevia_description(
        pag.titulus + " — Faber programming language documentation.", 160)


def favicon_href():
    return ("data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'"
            "%20viewBox='0%200%2064%2064'%3E%3Crect%20width='64'%20height='6"
            "4'%20rx='12'%20fill='%23ff5a2c'/%3E%3Cpath%20d='M46%2032H19M31%"
            "2019L18%2032L31%2045'%20fill='none'%20stroke='%230a0c0f'%20stro"
            "ke-width='6'%20stroke-linecap='round'%20stroke-linejoin='round'"
            "/%3E%3C/svg%3E")


def genera_head(pag, stylesheet_link):
    title = pag.titulus
    if not pag.titulus == "Faber":
        title = pag.titulus + " — Faber"
    description = pagina_description(pag)
    canonical = pagina_canonical(pag.site_locale, pag.iter)
    og_loc = og_locale(pag.site_locale)

    children = []
    children.append(ir_void("meta", [attr("charset", "utf-8")]))
    children.append(ir_void("meta", [attr("name", "viewport"),
                                     attr("content", "width=device-width, initial-scale=1")]))
    children.append(ir_void("meta", [attr("name", "description"),
                                     attr("content", description)]))
    children.append(ir_void("meta", [attr("name", "theme-color"),
                                     attr("content", "#e8e5db"),
                                     attr("media", "(prefers-color-scheme: light)")]))
    children.append(ir_void("meta", [attr("name", "theme-color"),
                                     attr("content", "#0a0c0f"),
                                     attr("media", "(prefers-color-scheme: dark)")]))
    children.append(ir_void("meta", [attr("property", "og:site_name"),
                                     attr("content", "Faber")]))
    children.append(ir_void("meta", [attr("property", "og:type"),
                                     attr("content", "website")]))
    children.append(ir_void("meta", [attr("property", "og:title"),
                                     attr("content", title)]))
    children.append(ir_void("meta", [attr("property", "og:description"),
                                     attr("content", description)]))
    children.append(ir_void("meta", [attr("property", "og:url"),
                                     attr("content", canonical)]))
    children.append(ir_void("meta", [attr("property", "og:locale"),
                                     attr("content", og_loc)]))
    children.append(ir_void("link", [attr("rel", "icon"),
                                     attr("href", favicon_href())]))
    children.append(ir_void("link", [attr("rel", "canonical"),
                                     attr("href", canonical)]))
    children.append(ir_void("link", [attr("rel", "alternate"),
                                     attr("type", "text/plain"),
                                     attr("href", "/llms.txt"),
                                     attr("title", "Agent index")]))
    children.append(ir_void("link", [attr("rel", "alternate"),
                                     attr("type", "text/markdown"),
                                     attr("href", "/agents/index.md"),
                                     attr("title", "Agent guide")]))
    children.append(ir_void("link", [attr("rel", "alternate"),
                                     attr("type", "application/json"),
                                     attr("href", "/.well-known/agent-skills/index.json"),
                                     attr("title", "Agent skills")]))
    children.append(ir_leaf("title", [], title))
    children.append(ir_void("link", [attr("rel", "stylesheet"),
                                     attr("href", stylesheet_link)]))
    children.append(ir_element("script", [attr("src", "/faber-search.js"),
                                          attr("defer", "")], []))
    children.append(ir_element("script", [attr("src", "/faber-demo-tabs.js"),
                                          attr("defer", "")], []))
    children.append(ir_element("script", [attr("src", "/faber-instrument.js"),
                                          attr("defer", "")], []))
    return ir_element("head", [], children)


def genera_renderbar(site_locale):
    links = [
        ir_leaf("a", [attr("href", "/llms.txt")], "/llms.txt"),
        ir_leaf("a", [attr("href", "/agents/index.md")], "/agents"),
        ir_leaf("a", [attr("href", "/.well-known/agent-skills/index.json")], "/skills"),
        ir_leaf("a", [attr("href", "/install.md")], "install"),
    ]
    nav = ir_element("nav", [attr("class", "machine-links"),
                             attr("aria-label", "Machine documentation")], links)
    mark = ir_leaf("span", [attr("class", "portal-mark"),
                            attr("aria-hidden", "true")], "←")
    home = ir_element("a", [attr("class", "portal-home"),
                            attr("href", "/"),
                            attr("title", "porta · all languages"),
                            attr("aria-label", "porta · all languages")], [mark])
    loclink = ir_leaf("a", [attr("class", "loclink"),
                            attr("href", "/"),
                            attr("title", "porta · change language"),
                            attr("aria-label", "porta · change language")], site_locale)
    search_input = ir_void("input", [attr("type", "search"),
                                     # html.fab spells "keyword…" (U+2026); the Faber pipeline
                                     # NFKC-normalizes string literals, so the oracle emits "...".
                                     attr("placeholder", "keyword..."),
                                     attr("aria-label", "Search keywords"),
                                     attr("autocomplete", "off"),
                                     attr("spellcheck", "false")])
    search = ir_element("span", [attr("class", "searchbox"),
                                 attr("data-search", ""),
                                 attr("hidden", "")], [search_input])
    inner = ir_element("div", [attr("class", "in")], [
        home,
        ir_leaf("span", [attr("class", "lbl")], "Rendering"),
        loclink,
        search,
        nav,
    ])
    return ir_element("div", [attr("class", "renderbar")], [inner])


def genera_brand(site_locale):
    mark = ir_leaf("span", [attr("class", "brand-mark"),
                            attr("aria-hidden", "true")], "←")
    name = ir_leaf("span", [attr("class", "brand-name")], "Faber")
    tag = ir_leaf("span", [attr("class", "brand-tag")], "language docs")
    text = ir_element("span", [attr("class", "brand-text")], [name, tag])
    return ir_element("a", [attr("class", "brand"),
                            attr("href", content_href("/", site_locale))],
                      [mark, text])


def genera_sidebar(pag):
    children = [
        genera_brand(pag.site_locale),
        genera_nav(pag.section, pagina_rel_url(pag.site_locale, pag.iter),
                   pag.site_locale),
    ]
    return ir_element("aside", [], children)


def code_link(href, label):
    return ir_element("a", [attr("href", href)],
                      [ir_leaf("code", [], label)])


def html_a(href, label):
    return ir_leaf("a", [attr("href", href)], label)


def genera_agent_notice(site_locale):
    p_children = [
        ir_text("If you are an AI agent: start at "),
        code_link("/install.md", "/install.md"),
        ir_text(", then read "),
        code_link("/agents/index.md", "/agents/index.md"),
        ir_text(" and pick a skill from "),
        code_link("/.well-known/agent-skills/index.json", "/.well-known/agent-skills/"),
        ir_text(". Humans: use "),
        html_a(content_href("/start/", site_locale), "Install"),
        ir_text(" and "),
        html_a(content_href("/cheatsheet/", site_locale), "Cheat sheet"),
        ir_text("."),
    ]
    label = ir_leaf("span", [attr("class", "agent-notice-label")], "Agent-ready")
    paragraph = ir_element("p", [], p_children)
    body = ir_element("div", [attr("class", "agent-notice-body")], [paragraph])
    return ir_element("section", [attr("class", "agent-notice"),
                                  attr("aria-label", "Agent-facing notice")],
                      [label, body])


def genera_main(pag):
    h1 = ir_leaf("h1", [], pag.titulus)
    body = ir_element("div", [attr("class", "content")],
                      converte_nodes(pag.corpus, pag.site_locale))
    if pag.section == "":
        return ir_element("main", [], [h1, genera_agent_notice(pag.site_locale), body])
    return ir_element("main", [], [h1, body])


def genera_source_list(sources):
    if len(sources) == 0:
        return ir_text("")
    items = [ir_element("li", [], [ir_text(src)]) for src in sources]
    label = ir_leaf("span", [attr("class", "side-h")], "Sources")
    listing = ir_element("ul", [], items)
    return ir_element("div", [attr("class", "source-list")], [label, listing])


def genera_footer(site_locale, sources):
    children = []
    source_list = genera_source_list(sources)
    if not ir_is_empty(source_list):
        children.append(source_list)
    foot_links = ir_element("nav", [attr("class", "foot-links"),
                                    attr("aria-label", "Site")], [
        html_a(content_href("/releases/", site_locale), "All releases")])
    children.append(foot_links)
    return ir_element("footer", [], children)


def genera_paginam(pag, stylesheet_link):
    body_class = "docs"
    if pag.section == "":
        body_class = "home"

    body_children = [genera_renderbar(pag.site_locale)]
    page_children = [
        genera_sidebar(pag),
        genera_main(pag),
        genera_footer(pag.site_locale, pag.sources),
    ]
    body_children.append(ir_element("div", [attr("class", "page")],
                                    page_children))
    root = ir_element("html", [attr("lang", pag.site_locale)], [
        genera_head(pag, stylesheet_link),
        ir_element("body", [attr("class", body_class)], body_children),
    ])
    return document_html(root)


# ==========================================================================
# corpus.fab
# ==========================================================================

CORPUS_RECORD_MARKER = "\n§§CORPUS_RECORD§§\n"
CORPUS_SOURCE_MARKER = "\n§§CORPUS_SOURCE§§\n"
CORPUS_EXPECTED_MARKER = "\n§§CORPUS_EXPECTED§§\n"


class CorpusExample(object):
    def __init__(self, path, term, kind, category, summary, syntax, related,
                 aliases, canonical, source, expected):
        self.path = path
        self.term = term
        self.kind = kind
        self.category = category
        self.summary = summary
        self.syntax = syntax
        self.related = related
        self.aliases = aliases
        self.canonical = canonical
        self.source = source
        self.expected = expected


def lista_vale(raw):
    # "["a", "b"]" → ["a", "b"]; empty or short raw → [].
    length = len(raw)
    if length < 2:
        return []
    inner = raw[1:length - 1]
    values = []
    for piece in divide(inner, ","):
        value = strip_quotes(recide(piece))
        if len(value) > 0:
            values.append(value)
    return values


def corpus_parse_example(record):
    source_parts = divide(record, CORPUS_SOURCE_MARKER)
    path = recide(source_parts[0])
    source_record = source_parts[1] if len(source_parts) > 1 else ""
    expected_parts = divide(source_record, CORPUS_EXPECTED_MARKER)
    source = expected_parts[0]
    expected = expected_parts[1] if len(expected_parts) > 1 else ""
    fields, body = fm_divide(source)
    canonical = field_vale(fields, "canonical", "false")
    return CorpusExample(
        path=path,
        term=field_vale(fields, "term", ""),
        kind=field_vale(fields, "kind", ""),
        category=field_vale(fields, "category", ""),
        summary=field_vale(fields, "summary", ""),
        syntax=field_vale(fields, "syntax", ""),
        related=field_vale(fields, "related", "[]"),
        aliases=field_vale(fields, "aliases", "[]"),
        canonical=(canonical == "true"),
        source=body,
        expected=expected,
    )


def example_label(example):
    canonical = "supporting"
    if example.canonical:
        canonical = "canonical"
    return ("### " + example.path + " (" + canonical + " · " + example.kind
            + ")\n\n" + example.summary + "\n")


def example_block(example):
    outcome = "compiles"
    if example.kind == "reject":
        outcome = "rejects"
    block = "```faber outcome=" + outcome + "\n" + example.source + "\n```"
    if example.kind == "reject":
        return block + "\n**Expected:** compilation rejects this example.\n"
    if len(example.expected) > 0:
        return (block + "\n**Expected output:**\n\n```\n" + example.expected
                + "\n```\n")
    return block


def related_links(raw):
    related = lista_vale(raw)
    if len(related) == 0:
        return "None."
    result = ""
    for item in related:
        result = result + "- [" + item + "](/corpus/" + item + ".html)\n"
    return result


def aliases_line(raw):
    aliases = lista_vale(raw)
    if len(aliases) == 0:
        return ""
    result = "**Aliases:** "
    first = True
    for alias in aliases:
        if not first:
            result = result + ", "
        result = result + "`" + alias + "`"
        first = False
    return result + "\n\n"


def visum_titulus(term, display):
    if len(display) > 0:
        return display
    return term


def corpus_markdown(term, primary, examples):
    aliases = aliases_line(primary.aliases)
    # The Faber template at corpus.fab:134 is an interpolated raw string:
    # its backslash sequences stay literal (\n and \" are two characters
    # each), so the generated frontmatter never parses as structured
    # fields — title/section/sources fall back to their defaults.
    markdown = ("+++\\ntitle = \\\"" + term + "\\\"\\nsection = \\\"corpus\\\"\\n"
                "sources = [\\\"" + primary.path + "\\\"]\\n+++\\n\\n"
                + primary.summary + "\\n\\n"
                + aliases + "**Syntax:** `" + primary.syntax + "`\\n\\n"
                "## Category\\n\\n`" + primary.category + "`\\n\\n"
                "## Related\\n\\n" + related_links(primary.related) + "\\n\\n"
                "## Examples\\n\\n")
    for example in examples:
        markdown = markdown + example_label(example)
        markdown = markdown + example_block(example) + "\n"
    return markdown


def termen_ex_canonica(bundle):
    records = divide(bundle, CORPUS_RECORD_MARKER)
    for record in records:
        if len(recide(record)) == 0:
            continue
        example = corpus_parse_example(record)
        if example.canonical:
            return example.term
    return ""


def genera_corpus_markdown(term, bundle, display):
    records = divide(bundle, CORPUS_RECORD_MARKER)
    examples = []
    summary = ""
    syntax = ""
    for record in records:
        if len(recide(record)) == 0:
            continue
        example = corpus_parse_example(record)
        if example.term == term:
            if example.canonical:
                summary = example.summary
                syntax = example.syntax
            examples.append(example)
    if len(examples) == 0:
        # Faber traps on the out-of-bounds examples[0]; mirror the failure
        # (no output, nonzero exit) rather than rendering an empty page.
        raise RuntimeError("corpus bundle has no record for term " + repr(term))
    primary = examples[0]
    page_summary = primary.summary
    page_syntax = primary.syntax
    if len(summary) > 0:
        page_summary = summary
    if len(syntax) > 0:
        page_syntax = syntax
    page_primary = CorpusExample(
        path=primary.path,
        term=primary.term,
        kind=primary.kind,
        category=primary.category,
        summary=page_summary,
        syntax=page_syntax,
        related=primary.related,
        aliases=primary.aliases,
        canonical=primary.canonical,
        source=primary.source,
        expected=primary.expected,
    )
    return recide(corpus_markdown(visum_titulus(term, display), page_primary,
                                  examples))


def genera_corpus(term, bundle, site_locale, reader_locale, stylesheet, display):
    markdown = genera_corpus_markdown(term, bundle, display)
    page = aedifica_paginam("corpus/" + visum_titulus(term, display),
                            markdown, site_locale, reader_locale)
    return genera_paginam(page, stylesheet)


def alias_head(alias, canonical, stylesheet, site_locale):
    corpus_href = content_href("/corpus/" + canonical + ".html", site_locale)
    abs_canonical = "https://faberlang.dev" + corpus_href
    children = [
        ir_void("meta", [attr("charset", "utf-8")]),
        ir_void("meta", [attr("name", "viewport"),
                         attr("content", "width=device-width, initial-scale=1")]),
        ir_void("meta", [attr("name", "robots"), attr("content", "noindex")]),
        ir_void("meta", [attr("http-equiv", "refresh"),
                         attr("content", "0; url=" + corpus_href)]),
        ir_void("link", [attr("rel", "canonical"),
                         attr("href", abs_canonical)]),
        ir_void("link", [attr("rel", "stylesheet"),
                         attr("href", stylesheet)]),
        ir_leaf("title", [], alias + " — Faber"),
    ]
    return ir_element("head", [], children)


def alias_body(canonical, site_locale):
    paragraph = [
        ir_text("This term is an alias. Continue to "),
        ir_leaf("a", [attr("href", content_href("/corpus/" + canonical + ".html",
                                                site_locale))], canonical),
        ir_text("."),
    ]
    return ir_element("body", [], [ir_element("p", [], paragraph)])


def genera_alias_redirect(alias, canonical, site_locale, stylesheet):
    root = ir_element("html", [attr("lang", site_locale)], [
        alias_head(alias, canonical, stylesheet, site_locale),
        alias_body(canonical, site_locale),
    ])
    return document_html(root)


# ==========================================================================
# main.fab
# ==========================================================================


def read_source(path):
    # No newline translation: the Faber read serves the bytes as textus.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        return handle.read()


def genera(source, iter_, site_locale, reader_locale, stylesheet_link):
    pag = aedifica_paginam(iter_, source, site_locale, reader_locale)
    return genera_paginam(pag, stylesheet_link)


def deriva_iter(path):
    # Derive the page path from a source file path (main.fab).
    src_pos = initium_index(path, "src/")
    if src_pos >= 0:
        after_src = path[src_pos + 4:]
        slash = initium_index(after_src, "/")
        if slash >= 0:
            after_locale = after_src[slash + 1:]
            dot = initium_index(after_locale, ".md")
            if dot >= 0:
                return after_locale[0:dot]
            return after_locale
        return after_src
    return path


def operandum(operands, index, defectus):
    if index < len(operands):
        return operands[index]
    return defectus


def usus():
    return ("Usage: speculum-gen <source.md> <site_locale> [reader_locale] "
            "[stylesheet] | --page <iter> <source.md> <site_locale> "
            "[reader_locale] [stylesheet] | --corpus <term> <bundle> "
            "<site_locale> [reader_locale] [stylesheet] [display] | "
            "--corpus-markdown <term> <bundle> [display] | --alias <alias> "
            "<canonical> <site_locale> [stylesheet]")


def lege_paginam(source_path, iter_, site_locale, reader_locale, stylesheet):
    source = read_source(source_path)
    return genera(source, iter_, site_locale, reader_locale, stylesheet)


def ex_operands(operands):
    if len(operands) < 1:
        return usus()
    mode = operands[0]
    if mode == "--page":
        if len(operands) < 3:
            return "missing page iter or source"
        site_locale = operandum(operands, 3, "en-US")
        reader_locale = operandum(operands, 4, site_locale)
        return lege_paginam(operands[2], operands[1], site_locale,
                            reader_locale,
                            operandum(operands, 5, "/speculum.css"))
    if mode == "--corpus-markdown":
        if len(operands) < 3:
            return "missing corpus term or bundle"
        return genera_corpus_markdown(operands[1],
                                      read_source(operands[2]),
                                      operandum(operands, 3, ""))
    if mode == "--corpus-bundle":
        if len(operands) < 2:
            return "missing corpus bundle"
        site_locale = operandum(operands, 2, "en-US")
        reader_locale = operandum(operands, 3, site_locale)
        corpus_content = read_source(operands[1])
        termen = termen_ex_canonica(corpus_content)
        return genera_corpus(termen, corpus_content, site_locale,
                             reader_locale,
                             operandum(operands, 4, "/speculum.css"),
                             operandum(operands, 5, ""))
    if mode == "--corpus-markdown-bundle":
        if len(operands) < 2:
            return "missing corpus bundle"
        corpus_content = read_source(operands[1])
        termen = termen_ex_canonica(corpus_content)
        return genera_corpus_markdown(termen, corpus_content,
                                      operandum(operands, 2, ""))
    if mode == "--corpus":
        if len(operands) < 3:
            return "missing corpus term or bundle"
        site_locale = operandum(operands, 3, "en-US")
        reader_locale = operandum(operands, 4, site_locale)
        return genera_corpus(operands[1], read_source(operands[2]),
                             site_locale, reader_locale,
                             operandum(operands, 5, "/speculum.css"),
                             operandum(operands, 6, ""))
    if mode == "--alias":
        if len(operands) < 3:
            return "missing alias or canonical term"
        site_locale = operandum(operands, 3, "en-US")
        return genera_alias_redirect(operands[1], operands[2], site_locale,
                                     operandum(operands, 4, "/speculum.css"))
    site_locale = operandum(operands, 1, "en-US")
    reader_locale = operandum(operands, 2, site_locale)
    return lege_paginam(mode, deriva_iter(mode), site_locale, reader_locale,
                        operandum(operands, 3, "/speculum.css"))


def main(argv):
    try:
        output = ex_operands(argv)
    except (OSError, RuntimeError, IndexError, KeyError) as failure:
        sys.stderr.write("speculum_py: " + str(failure) + "\n")
        return 1
    sys.stdout.buffer.write((output + "\n").encode("utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
