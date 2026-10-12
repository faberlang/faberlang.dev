#!/usr/bin/env python3
"""Input/output SHA-256 manifest helpers for build-site.sh."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "generator" / "target" / "build-manifest.json"


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def hash_inputs(paths):
    """Return stable path->hash map; directories hash sorted file inventories."""
    result = {}
    for raw in sorted(set(map(str, paths))):
        path = Path(raw)
        if path.is_dir():
            for item in sorted(p for p in path.rglob("*") if p.is_file()):
                rel = item.as_posix()
                result[rel] = sha(item)
        elif path.is_file():
            result[path.as_posix()] = sha(path)
        else:
            result[path.as_posix()] = "MISSING"
    return result


def load():
    try:
        value = json.loads(MANIFEST.read_text())
        return value if isinstance(value, dict) else {}
    except (OSError, ValueError):
        return {}


def save(data):
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    tmp = MANIFEST.with_suffix(".tmp")
    tmp.write_text(json.dumps(data, sort_keys=True, indent=2) + "\n")
    tmp.replace(MANIFEST)


def current(data, output, inputs):
    rel = Path(output).as_posix()
    full = ROOT / "dist" / rel
    entry = data.get(rel)
    recorded = entry.get("inputs", {}) if entry else {}
    return bool(full.is_file() and entry and all(recorded.get(k) == v for k, v in inputs.items()) and entry.get("output") == sha(full))


def inputs_current(data, output, inputs):
    rel = Path(output).as_posix()
    entry = data.get(rel, {})
    recorded = entry.get("inputs", {})
    return bool((ROOT / "dist" / rel).is_file() and entry and all(recorded.get(k) == v for k, v in inputs.items()))


def record(data, output, inputs):
    rel = Path(output).as_posix()
    full = ROOT / "dist" / rel
    if full.is_file():
        previous = data.get(rel, {}).get("inputs", {})
        previous.update(inputs)
        data[rel] = {"inputs": previous, "output": sha(full)}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("command", choices=["hash", "current", "inputs-current", "record", "refresh", "prune", "save"])
    p.add_argument("key", nargs="?")
    p.add_argument("paths", nargs="*")
    a = p.parse_args()
    data = load()
    if a.command == "hash":
        paths = ([a.key] if a.key else []) + a.paths
        print(json.dumps(hash_inputs(paths), sort_keys=True))
    elif a.command == "current":
        inputs = hash_inputs(a.paths)
        print("yes" if current(data, a.key, inputs) else "no")
    elif a.command == "inputs-current":
        inputs = hash_inputs(a.paths)
        print("yes" if inputs_current(data, a.key, inputs) else "no")
    elif a.command == "record":
        record(data, a.key, hash_inputs(a.paths)); save(data)
    elif a.command == "refresh":
        for rel in (a.paths or list(data)):
            full = ROOT / "dist" / rel
            if rel in data and full.is_file():
                data[rel]["output"] = sha(full)
        save(data)
    elif a.command == "prune":
        for rel in list(data):
            if not (ROOT / "dist" / rel).is_file():
                del data[rel]
        save(data)
    elif a.command == "save":
        save(data)

if __name__ == "__main__":
    main()
