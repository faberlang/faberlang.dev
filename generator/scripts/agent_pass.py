"""The agent pass: one component, two pages.

The pass is the paper card that hands a reader's model the one install link
(`faberlang.dev/install.md`) and carries the copy buttons. The landing page
(`generate-landing.py`) and the Start page (`inject-pass.py`) both render it
from here, so the markup, the release facts and the strings cannot drift.

Facts are read, never typed: the version from `static/install.md`, the licence
and platform names from the install skill. The visible strings come from the
page locale's `generator/locales/<locale>/chrome.toml` `[pass]` table, so a
translated page never shows English chrome. A missing fact or string fails the
caller instead of printing a guess.
"""

from __future__ import annotations

import html as html_mod
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
GENERATOR = REPO / "generator"

INSTALL_URL = "https://faberlang.dev/install.md"

# Every key the [pass] table must carry. `prompt` is what COPY PROMPT puts on
# the clipboard; the other keys are visible labels or accessible names.
PASS_KEYS = (
    "aria_install", "aria_pass", "label", "title", "version", "platforms",
    "license", "share", "copy_link", "copy_prompt", "copied", "failed", "prompt",
)


def esc(s: str) -> str:
    return html_mod.escape(s)


def read_release(repo: Path = REPO) -> dict[str, object]:
    """The current release, read from the agent lobby and the install skill.

    The version is stated once in static/install.md ("Current release: Faber
    X.Y.Z."), which build-site.sh also reads. The license and the platform
    names come from the install skill's release block and archive table. Any
    shape change fails the build instead of printing a guessed value."""
    lobby = (repo / "static" / "install.md").read_text(encoding="utf-8")
    m = re.search(r"^Current release: Faber (\S+)\.$", lobby, re.M)
    if not m:
        raise SystemExit("could not read the current release from static/install.md")
    skill = (repo / "static" / ".well-known" / "agent-skills" / "install" / "SKILL.md"
             ).read_text(encoding="utf-8")
    lic = re.search(r"^- \*\*License:\*\* (.+?)\s*$", skill, re.M)
    platforms = re.findall(r"^\| ([^|]+?) \| https://", skill, re.M)
    if not lic or not platforms:
        raise SystemExit("could not read license/platforms from the install skill")
    return {"version": m.group(1), "license": lic.group(1), "platforms": platforms}


def load_pass_strings(locale: str, generator: Path = GENERATOR) -> dict[str, str]:
    """The locale's [pass] chrome table; fails if the table or a key is missing."""
    import tomllib

    path = generator / "locales" / locale / "chrome.toml"
    if not path.is_file():
        raise SystemExit(f"no chrome.toml for locale {locale}: {path}")
    with open(path, "rb") as handle:
        table = tomllib.load(handle).get("pass", {})
    missing = [k for k in PASS_KEYS if not isinstance(table.get(k), str) or not table[k].strip()]
    if missing:
        raise SystemExit(f"{path}: [pass] is missing {', '.join(missing)}")
    return {k: table[k] for k in PASS_KEYS}


def render_pass(strings: dict[str, str], release: dict[str, object], hint_html: str = "") -> str:
    """The pass section. `hint_html` is an optional paragraph placed under the
    card (the landing page uses it; the Start page does not)."""
    version = esc(str(release["version"]))
    platforms = esc(" · ".join(release["platforms"]))
    license_name = esc(str(release["license"]))
    copied = esc(strings["copied"])
    failed = esc(strings["failed"])
    hint = f"\n      {hint_html}" if hint_html else ""
    return f"""\
    <section class="pass-wrap" aria-label="{esc(strings['aria_install'])}">
      <article class="pass" aria-label="{esc(strings['aria_pass'])}">
        <div class="pass-main">
          <div class="pass-top"><span>{esc(strings['label'])}</span><span>v{version}</span></div>
          <h2 class="pass-title">{esc(strings['title'])}</h2>
          <a class="channel" href="/install.md">faberlang.dev<wbr>/install.md</a>
          <dl class="fields">
            <div class="row"><dt>{esc(strings['version'])}</dt><i class="ld"></i><dd>{version}</dd></div>
            <div class="row"><dt>{esc(strings['platforms'])}</dt><i class="ld"></i><dd>{platforms}</dd></div>
            <div class="row"><dt>{esc(strings['license'])}</dt><i class="ld"></i><dd>{license_name}</dd></div>
          </dl>
        </div>
        <div class="pass-stub">
          <h2 class="share-title">{esc(strings['share'])}</h2>
          <div class="actions">
            <button type="button" class="btn btn-accent" data-copy="{esc(INSTALL_URL)}" data-copied="{copied}" data-failed="{failed}">{esc(strings['copy_link'])}</button>
            <button type="button" class="btn btn-ghost" data-copy="{esc(strings['prompt'])}" data-copied="{copied}" data-failed="{failed}">{esc(strings['copy_prompt'])}</button>
          </div>
        </div>
      </article>{hint}
    </section>
"""
