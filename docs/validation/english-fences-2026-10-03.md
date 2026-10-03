# English fence counts: compiler provenance, not a changed denominator

Measured 2026-10-03 for Vivi task `5452dcf6`, packet `fen2`.
These are observations, not acceptance thresholds or a replacement baseline.
No validator check, reader pack, or documentation fence was changed for this task.

## Result and responsible side

The seven localization failures were **tooling invocation / stale compiler
wiring**, not missing installed packs or a defect in the current reader-pack
validator. The main-checkout `radix/target/debug/radix` was built before K7b's
closure-keyword retirement but loaded the current packs from that checkout.
A fresh packet-local compiler passes all 206 English fences unchanged.

The fix is to build and select the compiler from the source revision being
validated. No pack installation step is needed for this workspace build.
Do not restore the retired keyword to the live packs to accommodate an old
binary. Do not edit localization fences to accommodate a pack-load failure.

## Full diagnostic and lookup

The stale binary prints these complete diagnostics before parsing the source:

```text
error: unknown reader locale 'en' in frontmatter: reader pack validation failed (from --locale 'en')
error: unknown reader locale 'th-TH' in frontmatter: reader pack validation failed (from --locale 'th-TH')
error: unknown reader locale 'zh-Hans' in frontmatter: reader pack validation failed (from --locale 'zh-Hans')
error: unknown reader locale 'zh-Hant' in frontmatter: reader pack validation failed (from --locale 'zh-Hant')
error: unknown reader locale 'vi' in frontmatter: reader pack validation failed (from --locale 'vi')
error: unknown reader locale 'ar' in frontmatter: reader pack validation failed (from --locale 'ar')
error: unknown reader locale 'hi' in frontmatter: reader pack validation failed (from --locale 'hi')
```

There are seven **fences on one page**, `src/en-US/localization.md`, not seven
pages. Fence indices are 0, 2, 3, 4, 5, 6, 7; Latin fence 1 passes.

Lookup is baked into the binary, not controlled by the shell's current directory
or by the validator's preliminary pack-file check:

- `radix/crates/radix-cli/src/commands/check.rs:28-36` resolves `--locale`
  before calling the source-check service and exits on resolution failure.
- `radix/crates/radix-module/src/program/compile.rs:1353` creates the default
  `Config` for explicit locale selection.
- `radix/crates/radix-module/src/driver/session.rs:327` discovers the workspace
  root; `radix/crates/radix-semantic/src/locale.rs:1487` derives it from that
  crate's build-time `CARGO_MANIFEST_DIR`, plus `../../locale`.
- `radix/crates/radix-module/src/driver/mod.rs:3614,3633-3635` joins
  `<root>/<locale>/pack.toml`, loads it, and emits the locale error.
- `radix/crates/radix-semantic/src/locale.rs:1248` renders `Validation` only
  as `reader pack validation failed`. That diagnostic does not list the
  individual validation issues or the path; the path above follows the code.

For the failing main binary the checked path is
`/Users/ianzepp/work/faberlang/radix/locale/<locale>/pack.toml`.
Binary strings also contain the baked main-checkout `radix-semantic` path.

`ls -l /Users/ianzepp/work/faberlang/radix/locale/{en,th-TH,zh-Hans,zh-Hant,vi,ar,hi}/pack.toml`
found all seven regular files, owned by `ianzepp staff`, mode `-rw-r--r--`:

| Locale | Bytes | Modification time (local) |
|---|---:|---|
| en | 194193 | Oct 3 01:02 |
| th-TH | 213030 | Oct 3 01:02 |
| zh-Hans | 123584 | Oct 3 01:02 |
| zh-Hant | 122952 | Oct 3 01:02 |
| vi | 147640 | Oct 3 01:02 |
| ar | 143312 | Oct 3 01:02 |
| hi | 191896 | Oct 3 01:02 |

Each is byte-identical to its passing `fen2/radix/locale/` counterpart.

## Why validation fails in the old binary

Radix commit `7eaf50ee875a6e75db2ae1bad22244f4f390fad8` removed `libera`
from the keyword registry and all eight packs. Its parent has
`CLOSURE_GROUP = ["clausura", "libera", "nucleum"]` at
`crates/radix-lexer/src/keywords.rs:389`; the current group at that line is
`["clausura", "nucleum"]`. Group validation in
`crates/radix-semantic/src/locale.rs:1852-1882` requires every member when
any member is localized and records `MissingKeywordGroupMember` otherwise.

Controlled diagnostic experiment: copied each affected pack and its exemplar
files into packet scratch, then added only that locale's former `libera` row
from K7b's parent. The stale binary's `--diagnostics-locale <scratch-pack>`
loader accepted every copy while checking the same extracted Latin fence.
An unchanged complete English pack copy failed; its pre-K7b version passed.
Thus the obsolete closure-group requirement is sufficient to explain every
reported locale-load failure. These scratch controls are not product changes
or accepted packs. Live packs and validator checks remain untouched.

## Count reconciliation

All reported totals are **206**: `197+9 = 190+16 = 199+7 = 206`.
Only the failing set moved. The original finding used a current `site3`
compiler. The old main binary adds seven pack-load failures to the same nine
stale snippets. Repair commit `19e58c25e` fixes those nine snippets but cannot
repair a stale compiler's pack registry.

Reproduction from `/Users/ianzepp/work/faberlang/worktrees/fen2/faberlang.dev`,
with `/opt/homebrew/bin` first on PATH:

```bash
# Restore pre-repair Markdown into packet scratch, not into this checkout.
mkdir -p ../scratch/before
git archive 366e6b884 src/en-US | tar -xf - -C ../scratch/before

# Compiler identities used below:
OLD=/Users/ianzepp/work/faberlang/radix/target/debug/radix
SITE3=/Users/ianzepp/work/faberlang/worktrees/site3/radix/target/debug/radix
FRESH=/Users/ianzepp/work/faberlang/worktrees/fen2/radix/target/debug/radix

# Fresh compiler: built in fen2/radix at 88720e888664d1b8c01b7706e5e47ccc776fa4f6.
(cd ../radix && timeout 100 cargo build --locked -p radix-cli --bin radix)
# Actual cold build: 20.79s, exit 0.
```

Each invocation below was timed with `/usr/bin/time -p` and bounded at 40s.
All skipped counts are zero.

| Exact invocation | Passed / failed | Exit | Seconds |
|---|---|---:|---:|
| `timeout 40 env RADIX="$OLD" bash generator/scripts/validate-fences.sh ../scratch/before/src/en-US` | 190 / 16 | 1 | 3.38 |
| `timeout 40 env RADIX="$SITE3" bash generator/scripts/validate-fences.sh ../scratch/before/src/en-US` | 197 / 9 | 1 | 13.67 |
| `timeout 40 env RADIX="$FRESH" bash generator/scripts/validate-fences.sh ../scratch/before/src/en-US` | 197 / 9 | 1 | 20.07 |
| `timeout 40 env RADIX="$OLD" bash generator/scripts/validate-fences.sh src/en-US` | 199 / 7 | 1 | 2.37 |
| `timeout 40 bash generator/scripts/validate-fences.sh src/en-US` (auto-selects FRESH after build) | 206 / 0 | 0 | 9.90 |

The validator script at `366e6b884` and `19e58c25e` is unchanged.
Both old and fresh binaries report `radix 0.84.0`; version alone cannot
identify a build from this unreleased development interval. Recorded SHA-256:

- OLD: `9a6161bac728185e4207dc852df8b0165627bdb18654ff27a700f1a909c9b006`
- SITE3: `41455a980eb66bac31d37662440cd271d0fdcec5cd4c2ce8b5338bc0a546d3c1`
- FRESH: `1c0e04f360d3bcf2ac452efcddf5e2193d79418d9b52d8cf1c7718ffa4867cf3`

For a future measurement, record Markdown revision, compiler revision/build,
selected executable path/hash, resolved pack root, and exact invocation.
The validator honors `RADIX`, otherwise prefers packet/workspace debug,
then release, then PATH. None of those discovery choices proves freshness.
A fallback or override is a different tool input, not a comparable baseline.

## Timing residual

A later redundant fresh full sweep hit its 40s bound, exit 124, before
reporting a final count. It is not a green result or a new failure count.
The completed 206/0 run above is the acceptance evidence. The slowdown was
reported to Mind; the timed-out command was not rerun unchanged. No broad
compiler, generator, site-render, release, or target-e2e suite was run.
