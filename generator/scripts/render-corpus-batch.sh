#!/usr/bin/env bash
# Render all canonical corpus term pages, aliases, category indexes, and the corpus hub.
#
# The shell/Python wrapper owns filesystem traversal and batch orchestration. The
# Faber generator owns term-page Markdown/HTML rendering and alias bridge HTML.
#
# Usage:
#   render-corpus-batch.sh <output-dir> [locale] [stylesheet]
#
# Environment:
#   PROOF_DIR=<dir>  also write generated term Markdown for fence validation

set -euo pipefail

GENERATOR_DIR="$(cd "$(dirname "$0")/.." && pwd)"
REPO_DIR="$(cd "$GENERATOR_DIR/.." && pwd)"
WORKSPACE_DIR="$(cd "$REPO_DIR/.." && pwd)"
CORPUS_DIR="${WORKSPACE_DIR}/examples/corpus"
BUILD_DIR="${GENERATOR_DIR}/target/faber"
FABER="${FABER:-faber}"

OUTPUT_DIR="${1:-${REPO_DIR}/dist}"
LOCALE="${2:-la}"
STYLESHEET="${3:-/speculum.css}"
PROOF_DIR="${PROOF_DIR:-}"

if [ ! -d "$CORPUS_DIR" ]; then
    echo "ERROR: corpus directory not found: $CORPUS_DIR" >&2
    exit 1
fi

mkdir -p "$OUTPUT_DIR/corpus"
if [ -n "$PROOF_DIR" ]; then
    rm -rf "$PROOF_DIR"
    mkdir -p "$PROOF_DIR"
fi

# Build the pure Faber generator, then inject the file/batch entry point into
# generated Rust. This mirrors render.sh but keeps corpus scale in one compile.
echo "Building generator for corpus batch..." >&2
"$FABER" build "$GENERATOR_DIR" -t rust 2>/dev/null
MAIN_RS="${BUILD_DIR}/src/main.rs"
if [ ! -f "$MAIN_RS" ]; then
    echo "ERROR: generated main.rs not found at $MAIN_RS" >&2
    exit 1
fi

MAIN_RS_PATH="$MAIN_RS" python3 << 'PYEOF'
import os
import sys

path = os.environ["MAIN_RS_PATH"]
src = open(path).read()
new_main = r'''fn main() {
    let args: Vec<String> = std::env::args().collect();
    if args.len() < 2 {
        eprintln!("Usage: speculum-gen --page <iter> <source.md> [locale] [stylesheet] | --corpus <term> <bundle> [locale] [stylesheet] | --corpus-markdown <term> <bundle> | --alias <alias> <canonical> [locale] [stylesheet]");
        std::process::exit(1);
    }
    let mode = &args[1];
    let html = if mode == "--page" {
        if args.len() < 4 { eprintln!("missing page iter or source"); std::process::exit(1); }
        let locale = if args.len() > 4 { args[4].clone() } else { "la".to_string() };
        let stylesheet = if args.len() > 5 { args[5].clone() } else { "/speculum.css".to_string() };
        let iter = args[2].clone();
        let source = std::fs::read_to_string(&args[3]).expect("failed to read page source");
        genera(source, iter, locale, stylesheet)
    } else if mode == "--corpus-markdown" {
        if args.len() < 4 { eprintln!("missing corpus term or bundle"); std::process::exit(1); }
        let term = args[2].clone();
        let bundle = std::fs::read_to_string(&args[3]).expect("failed to read corpus bundle");
        genera_corpus_markdown(term, bundle)
    } else if mode == "--corpus" {
        if args.len() < 4 { eprintln!("missing corpus term or bundle"); std::process::exit(1); }
        let locale = if args.len() > 4 { args[4].clone() } else { "la".to_string() };
        let stylesheet = if args.len() > 5 { args[5].clone() } else { "/speculum.css".to_string() };
        let term = args[2].clone();
        let bundle = std::fs::read_to_string(&args[3]).expect("failed to read corpus bundle");
        genera_corpus(term, bundle, locale, stylesheet)
    } else if mode == "--alias" {
        if args.len() < 4 { eprintln!("missing alias or canonical term"); std::process::exit(1); }
        let locale = if args.len() > 4 { args[4].clone() } else { "la".to_string() };
        let stylesheet = if args.len() > 5 { args[5].clone() } else { "/speculum.css".to_string() };
        genera_alias_redirect(args[2].clone(), args[3].clone(), locale, stylesheet)
    } else {
        eprintln!("unknown mode: {}", mode);
        std::process::exit(1);
    };
    print!("{}", html);
}'''
idx = src.find("fn main()")
if idx < 0:
    print("ERROR: fn main() not found", file=sys.stderr)
    sys.exit(1)
brace_start = src.find("{", idx)
depth = 0
end = brace_start
for i in range(brace_start, len(src)):
    if src[i] == "{":
        depth += 1
    elif src[i] == "}":
        depth -= 1
        if depth == 0:
            end = i + 1
            break
open(path, "w").write(src[:idx] + new_main + src[end:])
PYEOF


echo "Compiling corpus batch generator..." >&2
(cd "$BUILD_DIR" && cargo build --quiet 2>/dev/null)

CORPUS_DIR="$CORPUS_DIR" BUILD_DIR="$BUILD_DIR" OUTPUT_DIR="$OUTPUT_DIR" LOCALE="$LOCALE" STYLESHEET="$STYLESHEET" PROOF_DIR="$PROOF_DIR" python3 << 'PYEOF'
import json
import os
import re
import subprocess
import tomllib
from collections import defaultdict
from pathlib import Path

corpus = Path(os.environ["CORPUS_DIR"])
build = Path(os.environ["BUILD_DIR"])
output = Path(os.environ["OUTPUT_DIR"])
locale = os.environ["LOCALE"]
stylesheet = os.environ["STYLESHEET"]
proof_dir = os.environ.get("PROOF_DIR")
binary = build / "target/debug/speculum-gen"

marker = "\n§§CORPUS_RECORD§§\n"
source_marker = "\n§§CORPUS_SOURCE§§\n"
expected_marker = "\n§§CORPUS_EXPECTED§§\n"

def slug(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "uncategorized"

def clean_generated(text: str) -> str:
    return "\n".join(line.rstrip() for line in text.splitlines()) + "\n"

records_by_term = defaultdict(list)
canonical = {}
category_terms = defaultdict(list)

for path in sorted(corpus.rglob("*.fab")):
    source = path.read_text()
    parts = source.split("+++", 2)
    if len(parts) != 3:
        continue
    fields = tomllib.loads(parts[1])
    term = fields.get("term")
    if not term:
        continue
    include = bool(fields.get("canonical", False)) or fields.get("kind") == "reject"
    if include:
        expected_path = path.with_suffix(".expected")
        expected = expected_path.read_text() if expected_path.exists() else ""
        rel = path.relative_to(corpus.parent.parent)
        records_by_term[term].append((not fields.get("canonical", False), str(rel), source, expected))
    if fields.get("canonical", False):
        canonical.setdefault(term, fields)

terms = sorted(canonical)
term_set = set(terms)
alias_targets = defaultdict(list)
for term in terms:
    fields = canonical[term]
    category_terms[fields.get("category", "uncategorized")].append(term)
    for alias in fields.get("aliases", []):
        alias_targets[alias].append(term)

bundle_dir = build / "corpus-bundles"
bundle_dir.mkdir(parents=True, exist_ok=True)
corpus_out = output / "corpus"
corpus_out.mkdir(parents=True, exist_ok=True)

for term in terms:
    selected = sorted(records_by_term[term], key=lambda item: (item[0], item[1]))
    bundle = bundle_dir / f"{term}.bundle"
    bundle.write_text(marker.join(path + source_marker + source + expected_marker + expected for _, path, source, expected in selected))
    html_path = corpus_out / f"{term}.html"
    html = subprocess.check_output([str(binary), "--corpus", term, str(bundle), locale, stylesheet], text=True)
    html_path.write_text(clean_generated(html))
    if proof_dir:
        proof_path = Path(proof_dir) / f"{term}.md"
        proof_path.parent.mkdir(parents=True, exist_ok=True)
        markdown = subprocess.check_output([str(binary), "--corpus-markdown", term, str(bundle)], text=True)
        proof_path.write_text(markdown)
written_aliases = set()
skipped_aliases = []
for alias in sorted(alias_targets):
    targets = sorted(alias_targets[alias])
    if alias in term_set:
        skipped_aliases.append((alias, targets, "canonical-term-path"))
        continue
    target = targets[0]
    if len(targets) > 1:
        skipped_aliases.append((alias, targets[1:], f"duplicate-alias-kept:{target}"))
    alias_path = corpus_out / f"{alias}.html"
    alias_html = subprocess.check_output([str(binary), "--alias", alias, target, locale, stylesheet], text=True)
    alias_path.write_text(clean_generated(alias_html))
    written_aliases.add(alias)

if skipped_aliases:
    (build / "corpus-alias-residuals.json").write_text(json.dumps(skipped_aliases, indent=2, sort_keys=True))

# Render category indexes and the corpus hub through the same page generator.
generated_dir = build / "generated-corpus-pages"
generated_dir.mkdir(parents=True, exist_ok=True)

category_index = []
for category in sorted(category_terms):
    terms_in_category = sorted(category_terms[category])
    category_slug = slug(category)
    md = [
        "+++",
        f'title = "Corpus: {category}"',
        'section = "corpus"',
        'sources = []',
        "+++",
        "",
        f"# Corpus category: `{category}`",
        "",
        f"{len(terms_in_category)} canonical terms in this category.",
        "",
    ]
    md.extend(f"- [`{term}`](/corpus/{term}.html)" for term in terms_in_category)
    source = generated_dir / f"category-{category_slug}.md"
    source.write_text("\n".join(md) + "\n")
    out = corpus_out / "category" / f"{category_slug}.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    html = subprocess.check_output([str(binary), "--page", f"corpus/category/{category_slug}", str(source), locale, stylesheet], text=True)
    out.write_text(clean_generated(html))
    category_index.append((category, category_slug, len(terms_in_category)))

hub = [
    "+++",
    'title = "Corpus"',
    'section = "corpus"',
    'sources = []',
    "+++",
    "",
    "# Corpus",
    "",
    f"Generated reference pages for {len(terms)} canonical Faber corpus terms.",
    "",
    "## Categories",
    "",
]
hub.extend(f"- [{category}](/corpus/category/{category_slug}.html) — {count} terms" for category, category_slug, count in category_index)
hub.extend(["", "## Terms", ""])
hub.extend(f"- [`{term}`](/corpus/{term}.html)" for term in terms)
hub_source = generated_dir / "corpus-index.md"
hub_source.write_text("\n".join(hub) + "\n")
hub_html = subprocess.check_output([str(binary), "--page", "corpus/index", str(hub_source), locale, stylesheet], text=True)
(corpus_out / "index.html").write_text(clean_generated(hub_html))

manifest = {
    "terms": len(terms),
    "aliases": len(written_aliases),
    "alias_residuals": len(skipped_aliases),
    "categories": len(category_terms),
}
print(json.dumps(manifest, sort_keys=True))
PYEOF
