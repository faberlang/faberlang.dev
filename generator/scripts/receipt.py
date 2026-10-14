"""Degradation receipt: every fallback the build takes is recorded, not hidden.

A generator that cannot do its job exactly (a fence that will not convert, an
example whose projection breaks) used to print a warning and carry on with a
cruder result, and the build still exited 0. Nothing recorded how many such
results shipped. Each fallback now calls `degraded()`; `build.py` attaches the
events to the output they affected, stores them in the manifest, prints one
summary, and fails on any event that `generator/degraded.allow.toml` does not
list with a reason.

Subprocess generators report in-band: one stderr line per event of the form
`DEGRADED <kind> <subject>: <detail>`, which `parse_line` recovers.
"""
from __future__ import annotations

import fnmatch
import sys
import threading
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - Python < 3.11
    import tomli as tomllib  # type: ignore

_LOCK = threading.Lock()
_EVENTS: list[dict] = []
PREFIX = "DEGRADED "


def degraded(kind: str, subject: str, detail: str = "") -> None:
    """Record one fallback. `kind` is a stable slug; `subject` names what was affected."""
    event = {"kind": kind, "subject": subject, "detail": detail.strip().splitlines()[0][:240] if detail.strip() else ""}
    with _LOCK:
        _EVENTS.append(event)


def emit(kind: str, subject: str, detail: str = "") -> None:
    """Report a fallback from a standalone generator script (stderr, in-band)."""
    first = detail.strip().splitlines()[0][:240] if detail.strip() else ""
    sys.stderr.write(f"{PREFIX}{kind} {subject}: {first}\n")


def parse_line(line: str) -> dict | None:
    if not line.startswith(PREFIX):
        return None
    head, _, detail = line[len(PREFIX):].rstrip("\n").partition(": ")
    kind, _, subject = head.partition(" ")
    if not kind or not subject:
        return None
    return {"kind": kind, "subject": subject, "detail": detail}


def drain() -> list[dict]:
    """Take (and clear) the events recorded since the last drain."""
    with _LOCK:
        taken = list(_EVENTS)
        _EVENTS.clear()
    return taken


class Allowlist:
    """`generator/degraded.allow.toml`: accepted fallbacks, each with its reason."""

    def __init__(self, path: Path):
        self.entries: list[dict] = []
        if path.is_file():
            with path.open("rb") as handle:
                self.entries = list(tomllib.load(handle).get("allow", []))
        for entry in self.entries:
            for key in ("kind", "subject", "why"):
                if not str(entry.get(key, "")).strip():
                    raise ValueError(f"{path.name}: every [[allow]] entry needs kind, subject and why")
        self.used: set[int] = set()

    def covers(self, event: dict) -> bool:
        for index, entry in enumerate(self.entries):
            if entry["kind"] == event["kind"] and fnmatch.fnmatchcase(event["subject"], entry["subject"]):
                self.used.add(index)
                return True
        return False

    def unused(self) -> list[dict]:
        return [entry for index, entry in enumerate(self.entries) if index not in self.used]
