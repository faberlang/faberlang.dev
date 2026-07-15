# faberlang.dev

Local RC1 preview site and versioned documentation packet for Faber.

The checked-in `assets/` tree is the canonical local preview surface. It is
served by the Rust/Axum adapter in `src/main.rs` and the Cloudflare Worker in
`cloudflare-worker/src/index.js`. The packet includes HTML homepage content,
Markdown documentation, machine-readable contracts, agent skills, discovery
metadata, and fail-closed public-claim validation.

## Local validation

```sh
cargo test --all-targets
cargo run --bin validate_public_packet
npm ci --ignore-scripts
npm run cf:dry-run
```

Run the Rust preview with `PORT=8080 cargo run`, or the local Worker preview
with `npm run cf:dev`. These commands do not publish the site.

## Publication status

The local implementation is complete and the Cloudflare delivery seam is
validated, but this repository does not prove a public deployment. Release
artifacts, public source/export, DNS, route attachment, analytics, and launch
announcements remain explicit operator gates. See
[`docs/deployment/cloudflare-workers.md`](docs/deployment/cloudflare-workers.md)
for the deployment runbook.

Planned domain: https://faberlang.dev
