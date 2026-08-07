# Migrate faberlang.dev from GitHub Pages → Cloudflare Pages

Created: 2026-08-06. See chat session for full diagnosis; this file is self-contained.

## Diagnosis (why we're moving)

Deployments **do** kick off — GitHub Actions is healthy. The failure is the
GitHub Pages **serving backend**: deploys stall at `deployment_queued` and time
out at ~10 minutes. Evidence: the last 3 runs on Aug 6 all failed identically
(`Timeout reached, aborting!` after polling `deployment_queued` for ~10m); the
last green run was Aug 5. This is a GitHub Pages backend queue stall, not an
Actions or build problem.

- `dist/` is committed and already fully generated locally (the Faber-based
  Speculum generator needs the `faber` binary, which is not available in CI).
- Therefore the migration must **not** require Cloudflare to run a build. It
  only needs to serve the committed `dist/` directory.

## Target architecture

Cloudflare Pages, git-connected, **zero build step**:

```
push to main → Cloudflare checks out repo → serves dist/ → edge
               (no build command, no GitHub Actions, no GitHub Pages backend)
```

The only remaining GitHub dependency is git hosting (push + repo read), which is
not failing. Both Actions and the Pages serving queue leave the path entirely.

## Steps

### You drive (external state — needs your Cloudflare / GitHub / registrar auth)

1. **Create the Pages project** — Cloudflare dashboard → Workers & Pages →
   Create → Pages → Connect to Git → select `faberlang/faberlang.dev`.

2. **Build settings (the key part):**
   - Framework preset: **None**
   - Build command: **(leave empty)**
   - Build output directory: **`dist`**
   - Root directory: `/`

3. **First deploy** → verify against `faberlang-dev.pages.dev` before touching DNS.

4. **Custom domains** — add `faberlang.dev` and `www.faberlang.dev` in the
   Pages dashboard (Custom domains tab).

5. **Move DNS to Cloudflare** — change nameservers at the registrar from Google
   Domains (`ns-cloud-b*.googledomains.com`) to Cloudflare's. Cloudflare
   auto-provisions the CNAME to the Pages project. The apex needs CNAME
   flattening, which works cleanly only when Cloudflare manages the zone — so
   this nameserver move is required, not optional.
   - Note: Google Domains sold to Squarespace; confirm registrar access before
     starting.

6. **Verify cutover** — after DNS propagates, confirm `faberlang.dev` and
   `www.faberlang.dev` resolve to Cloudflare and serve the current content.

7. **Leave the GitHub Actions workflow in place** until Cloudflare is confirmed
   live — it's the rollback safety net.

### Agent does (repo-side, safe, reversible — only AFTER Cloudflare verified live)

8. Add a `wrangler.toml` recording the Pages config in-repo:
   ```toml
   name = "faberlang-dev"
   pages_build_output_dir = "dist"
   ```

9. Update `AGENTS.md` deployment section to describe the Cloudflare path and
   fix the stale "dormant Cloudflare Worker" claim (the `cloudflare-worker/`
   dir does not exist; only `.wrangler` in `.gitignore` remains).

10. Remove `.github/workflows/deploy-pages.yml` (or leave it disabled as a
    documented fallback). Do this **last** — the AGENTS.md rule "never merge to
    main without a deploy workflow" exists so the site doesn't go blank.

## Decisions still open

- **Canonical host:** apex (`faberlang.dev`) vs `www`. Both resolve today. Pick
  one as canonical and redirect the other (trivial via Cloudflare `_redirects`
  or the dashboard). Not blocking, but decide before/around cutover.
- **Real redirects:** legacy paths currently use `<meta http-equiv="refresh">`
  stubs in `dist/`. Optionally replace with Cloudflare `_redirects` for real
  301s later. Not required for parity.

## Rollback

Until step 10 runs, GitHub Pages remains a live fallback: revert Cloudflare DNS
and the site is served by GitHub again (assuming its backend recovers). After
step 10, rollback requires restoring the workflow + DNS.
