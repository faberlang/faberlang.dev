#!/usr/bin/env python3
"""
locales_registry.py — Load and query the locale registry (locales.toml).

Provides a single source of truth for locale metadata used by other
generator scripts (canonical injection, leakage gate, sitemap, etc.).

Usage:
    locales_registry.py reader <site>   → print reader_locale
    locales_registry.py names           → print all site keys, one per line
    locales_registry.py native <site>   → print native_name
"""

import sys
import tomllib
from pathlib import Path


def _default_path() -> Path:
    """Return the default path to locales.toml, relative to this script."""
    return Path(__file__).resolve().parent.parent / "locales.toml"


def load_registry(path: Path | None = None) -> dict:
    """Load the locale registry from a TOML file.

    Args:
        path: Path to locales.toml. Defaults to ../locales.toml relative
              to this file.

    Returns:
        The parsed [locales.*] section as a nested dict, keyed by site code.
        Example: {"en-US": {"reader_locale": "la", "native_name": "English", ...}}
    """
    if path is None:
        path = _default_path()
    with path.open("rb") as f:
        data = tomllib.load(f)
    return data.get("locales", {})


def site_locales(registry: dict) -> list[str]:
    """Return sorted list of locale site codes."""
    return sorted(registry.keys())


def reader_locale(registry: dict, site: str) -> str:
    """Return the reader_locale for a given site code.

    Falls back to the site code itself if not explicitly configured.
    """
    entry = registry.get(site)
    if entry is None:
        return site
    return entry.get("reader_locale", site)


def native_name(registry: dict, site: str) -> str:
    """Return the native_name for a given site code.

    Raises KeyError if the site is unknown.
    """
    entry = registry.get(site)
    if entry is None:
        raise KeyError(f"Unknown site: {site}")
    return entry["native_name"]


def is_known_site(registry: dict, site: str) -> bool:
    """Return True if the site code exists in the registry."""
    return site in registry


def locale_dir_names(registry: dict) -> set[str]:
    """Return the set of all locale directory names (the registry keys).

    Useful for gate exclusion lists and directory-aware scans.
    """
    return set(registry.keys())


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage:", file=sys.stderr)
        print("  locales_registry.py reader <site>", file=sys.stderr)
        print("  locales_registry.py names", file=sys.stderr)
        print("  locales_registry.py native <site>", file=sys.stderr)
        return 1

    reg = load_registry()
    cmd = sys.argv[1]

    if cmd == "reader":
        if len(sys.argv) < 3:
            print("ERROR: reader requires a site argument", file=sys.stderr)
            return 1
        site = sys.argv[2]
        if not is_known_site(reg, site):
            print(f"ERROR: unknown site '{site}'", file=sys.stderr)
            return 1
        print(reader_locale(reg, site))

    elif cmd == "names":
        for s in site_locales(reg):
            print(s)

    elif cmd == "native":
        if len(sys.argv) < 3:
            print("ERROR: native requires a site argument", file=sys.stderr)
            return 1
        site = sys.argv[2]
        try:
            print(native_name(reg, site))
        except KeyError as e:
            print(f"ERROR: {e}", file=sys.stderr)
            return 1

    else:
        print(f"ERROR: unknown command '{cmd}'", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
