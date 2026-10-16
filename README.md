# faberlang.dev

Source for [faberlang.dev](https://faberlang.dev), the documentation site for
the [Faber programming language](https://github.com/faberlang/faber). Faber is
experimental through version 1.

## Layout

- `src/en-US/` Markdown pages (the maintained prose tree)
- `static/` files copied as-is: `install.md`, `llms.txt`, the agent guides in
  `agents/` and the agent skills in `.well-known/agent-skills/`
- `generator/` the site generator (Python) and its stylesheet
- `dist/` the generated site, committed; this is what gets published

Pages generated from the compiler (grammar, locale tables, corpus, agent
reference) come from a pinned Faber commit in `generator/upstream.lock.toml`.

## Build

Needs Python 3.11 or newer and a `faber` binary built from the pinned commit.

```bash
bash generator/scripts/build-site.sh --faber /path/to/faber   # incremental
bash generator/scripts/build-site.sh --full --faber /path/to/faber
```

The build renders `dist/`, runs the link, leakage and width checks and writes
`sitemap.xml`; it stops on any failure. Commit `src/`, `static/` and `dist/`
together. `AGENTS.md` covers the pin, generated pages and checks.

## Deploy

A push to `main` runs `.github/workflows/deploy-pages.yml`, which uploads
`dist/` as a GitHub Pages artifact and publishes it at https://faberlang.dev.
The workflow does not build anything, so `dist/` must be current when you push.

## Licence

This repository has no licence file of its own yet. The Faber compiler, runner
and standard library are `MIT OR Apache-2.0`; see
[faberlang/faber](https://github.com/faberlang/faber).
