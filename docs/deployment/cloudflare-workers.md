# Cloudflare Workers deployment

This document describes the local Cloudflare seam for `faberlang.dev`. It is an
operator runbook, not a deployment approval. The repository currently supports
two delivery adapters over the same checked-in `assets/` tree:

- **Rust/Axum** (`src/main.rs`) serves the local site and its health endpoint.
- **Cloudflare Workers** (`cloudflare-worker/src/index.js`) serves the same
  assets through the `ASSETS` binding and adds the Worker edge behavior.

The Worker design is wired locally by `wrangler.jsonc` and `package.json`; it is
not evidence that an account, domain, route, or public deployment exists.

## Current local configuration

`wrangler.jsonc` currently declares:

- Worker name: `faberlang-dev`.
- Entrypoint: `cloudflare-worker/src/index.js`.
- Compatibility date: `2026-05-01` (the newest local runtime date supported by pinned Wrangler 4.85.0).
- Static asset directory: `./assets`, bound as `ASSETS`, with `run_worker_first: true` so Worker-owned health, negotiation, headers, and placeholder substitution run before static fallback.

The npm scripts are:

```text
npm run cf:dev       # local Wrangler Worker preview
npm run cf:dry-run   # Wrangler package/deploy dry run; no publish
npm run cf:deploy    # publish the Worker (operator-gated)
npm run cf:types     # generate Wrangler types, when needed
```

The Worker currently handles `/health` itself and delegates other paths to
`ASSETS`. It preserves root content negotiation (`Accept: text/markdown` or
`text/plain` selects `llms.txt`), sets `Vary: Accept` for `/` and
`/index.html`, and expands the `__PUBLIC_ORIGIN__` and `__DOCS_VERSION__`
placeholders. `PUBLIC_ORIGIN` and `DOCS_VERSION` may be supplied as Worker
bindings; otherwise the request origin and `1.0.0-rc.1` are used.

The checked-in config has no `routes` entry. A successful Worker publication
therefore does **not** by itself prove that `faberlang.dev` is attached to the
Worker. The account's workers.dev hostname, a custom-domain attachment, or a
route must be selected and verified separately by the operator.

## Local preparation (no login and no deploy)

Run these from `faberlang.dev`:

```bash
# Rust/Axum adapter
cargo build
cargo test
PORT=8080 cargo run

# Cloudflare adapter; npm ci uses the checked-in package-lock.json
npm ci
npm run cf:dev
npm run cf:dry-run
```

For a local Rust smoke check, use a second terminal while `cargo run` is active:

```bash
curl -fsS http://127.0.0.1:8080/health
curl -fsS -H 'Accept: text/markdown' http://127.0.0.1:8080/
curl -i http://127.0.0.1:8080/docs/1.0.0-rc.1/reference/index.md
```

`cf:dry-run` checks the Wrangler package without publishing it. Neither local
preview is a public deployment. Preparation does not authenticate to
Cloudflare, reserve a domain, configure DNS, attach a route, or prove that an
edge deployment is reachable.

## Manual re-authentication and deployment

Only an authorized operator should perform these steps. They are intentionally
not run by routine local preparation.

1. Confirm the intended Cloudflare account and the exact Worker name
   (`faberlang-dev`). If the account is wrong, stop before changing anything.
2. Re-authenticate interactively when required:

   ```bash
   npx wrangler logout
   npx wrangler login
   npx wrangler whoami
   ```

   `wrangler login` opens the browser. Complete the login and account selection
   there; do not put tokens in the repository or shell history.
3. From `faberlang.dev`, reinstall the locked toolchain and inspect the package:

   ```bash
   npm ci
   npm run cf:dry-run
   ```
4. Before publishing, configure or explicitly approve the intended
   `PUBLIC_ORIGIN` and `DOCS_VERSION` values. If they are not already Worker
   variables, pass the approved values explicitly:

   ```bash
   npx wrangler deploy \
     --var PUBLIC_ORIGIN:https://faberlang.dev \
     --var DOCS_VERSION:1.0.0-rc.1
   ```

   `npm run cf:deploy` is equivalent when the approved variables and routing
   are already configured. Do not add a custom route or change DNS as an
   unreviewed side effect of this step.
5. Record the resulting deployment identifier, account, hostname/route, and
   source commit in the operator change record.

## External gates

Deployment must stop until each applicable gate is explicit and approved:

- **Account:** `wrangler whoami` identifies the intended account and the
  operator has permission to deploy `faberlang-dev`.
- **Domain:** `faberlang.dev` is an active, operator-controlled Cloudflare zone;
  nameservers/DNS and TLS state are ready if a custom domain is desired.
- **Route:** the exact hostname and path pattern are selected, do not conflict
  with another Worker, and are attached through the approved Cloudflare route
  or custom-domain mechanism. The current `wrangler.jsonc` does not declare
  one.
- **Origin and version:** `PUBLIC_ORIGIN` is the approved canonical origin and
  `DOCS_VERSION` names the asset set being published. Placeholder or fallback
  values are not a release decision.
- **Content gate:** the local public-packet/leakage checks and the relevant
  Rust/Worker checks are green for the commit being published.
- **Rollback:** a known-good prior deployment and its identifier are recorded
  before the first production change.

No login, account mutation, DNS change, route attachment, public preview, or
production deployment is authorized by this document.

## Post-deploy verification

After the operator publishes and attaches the approved route, verify both the
Worker deployment and the intended public hostname. Replace the placeholder
with the actual approved URL:

```bash
export SITE_URL='https://faberlang.dev'
curl -fsS "$SITE_URL/health"
curl -fsS -D - "$SITE_URL/" -o /tmp/faberlang-index.html
curl -fsS -H 'Accept: text/markdown' "$SITE_URL/" | head
curl -fsS "$SITE_URL/.well-known/faber-language.json" >/dev/null
curl -fsS "$SITE_URL/contracts/1.0.0-rc.1/checksums.json" >/dev/null
```

Confirm that:

- `/health` returns the expected `faber-web` success JSON.
- `/` returns HTML by default and Markdown with the negotiated `Accept`
  header; the response varies on `Accept`.
- The documented content types, versioned routes, checksums, and well-known
  assets are reachable from the approved hostname.
- The hostname resolves to the intended Worker route, not merely to an
  unrelated workers.dev deployment or stale origin.
- No response contains unresolved `__PUBLIC_ORIGIN__` or
  `__DOCS_VERSION__` placeholders.

These checks prove the selected route and current asset response only. They do
not prove domain ownership beyond the operator's Cloudflare controls,
long-term availability, caching behavior, analytics/privacy compliance, or
approval for public launch.

## Rollback

If the deployed Worker is incorrect or unhealthy, stop promotion and preserve
the evidence. An authorized operator can list deployments and roll back to the
recorded known-good identifier:

```bash
npx wrangler deployments list
npx wrangler rollback <KNOWN_GOOD_DEPLOYMENT_ID>
```

Re-run the post-deploy checks against the approved hostname, confirm the route
still points at the rolled-back version, and record the rollback identifier,
time, symptoms, and verification results. DNS or route changes are separate
operations; rolling back Worker code does not undo an independently changed
DNS record or route.

## What this preparation does not prove

A passing local build, Rust test suite, `cf:dev`, or `cf:dry-run` does not prove:

- Cloudflare authentication or account authorization;
- ownership or readiness of `faberlang.dev`;
- DNS, TLS, route, custom-domain, or workers.dev availability;
- that the Worker was published or is reachable from the public Internet;
- that the selected route points to this Worker and this asset commit;
- production cache behavior, quotas, limits, observability, or rollback
  readiness; or
- public-launch approval, analytics/privacy decisions, or an external
  announcement.

Those are external operator gates and remain outside the no-login/no-deploy
boundary of this local seam task.
