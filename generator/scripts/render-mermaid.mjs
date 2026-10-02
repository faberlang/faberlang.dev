/* =========================================================================
   render-mermaid.mjs — Mermaid source → theme-aware inline SVG
   =========================================================================
   Called by diagrams.py; not used directly. Reads a JSON job list on stdin:

       [{ "id": "d-ab12cd34", "source": "flowchart LR\n  A --> B" }, ...]

   and writes a JSON result list on stdout:

       [{ "id": "...", "svg": "<svg …>" }, { "id": "...", "error": "…" }]

   Colours are the point. Mermaid bakes literal hex into the SVG it emits,
   which would freeze the diagram into one theme. So every theme variable is
   set to a sentinel colour here, and diagrams.py rewrites those sentinels to
   the site's CSS custom properties. The inlined SVG then follows light/dark
   like the rest of the page, with no second asset and no client-side JS.

   The sentinel list must stay in sync with SENTINELS in diagrams.py.
   ========================================================================= */

import { readFileSync } from 'node:fs';
import { createRequire } from 'node:module';
import { join } from 'node:path';

// Dependencies live in the on-demand tools directory (generator/target/…),
// not next to this script, so resolve from there rather than from import.meta.
const toolsDir = process.env.SPECULUM_DIAGRAM_TOOLS || process.cwd();
const require = createRequire(join(toolsDir, 'package.json'));
const { chromium } = require('playwright');
const mermaidJs = readFileSync(require.resolve('mermaid/dist/mermaid.min.js'), 'utf8');

const S = {
    bg: '#fe0001',
    panel: '#fe0002',
    panelDeep: '#fe0003',
    ink: '#fe0004',
    inkSoft: '#fe0005',
    lineStrong: '#fe0006',
    accent: '#fe0007',
    accentSoft: '#fe0008',
};

const themeVariables = {
    background: S.bg,
    primaryColor: S.panel,
    primaryTextColor: S.ink,
    primaryBorderColor: S.lineStrong,
    secondaryColor: S.accentSoft,
    secondaryTextColor: S.ink,
    secondaryBorderColor: S.lineStrong,
    tertiaryColor: S.panelDeep,
    tertiaryTextColor: S.ink,
    tertiaryBorderColor: S.lineStrong,
    lineColor: S.accent,
    textColor: S.ink,
    mainBkg: S.panel,
    nodeBorder: S.lineStrong,
    nodeTextColor: S.ink,
    arrowheadColor: S.accent,
    edgeLabelBackground: S.bg,
    clusterBkg: S.bg,
    clusterBorder: S.lineStrong,
    titleColor: S.ink,
    // sequence diagrams
    actorBkg: S.panel,
    actorBorder: S.lineStrong,
    actorTextColor: S.ink,
    actorLineColor: S.lineStrong,
    signalColor: S.ink,
    signalTextColor: S.ink,
    labelBoxBkgColor: S.panel,
    labelBoxBorderColor: S.lineStrong,
    labelTextColor: S.ink,
    loopTextColor: S.ink,
    noteBkgColor: S.accentSoft,
    noteBorderColor: S.lineStrong,
    noteTextColor: S.ink,
    activationBkgColor: S.panelDeep,
    activationBorderColor: S.lineStrong,
    sequenceNumberColor: S.bg,
};

function readStdin() {
    return new Promise((resolve, reject) => {
        let buf = '';
        process.stdin.setEncoding('utf8');
        process.stdin.on('data', (c) => (buf += c));
        process.stdin.on('end', () => resolve(buf));
        process.stdin.on('error', reject);
    });
}

const jobs = JSON.parse(await readStdin());
if (!jobs.length) {
    process.stdout.write('[]');
    process.exit(0);
}

const browser = await chromium.launch();
const page = await browser.newPage();
await page.setContent('<!doctype html><html><body></body></html>');
await page.addScriptTag({ content: mermaidJs });

await page.evaluate((themeVariables) => {
    window.mermaid.initialize({
        startOnLoad: false,
        theme: 'base',
        themeVariables,
        securityLevel: 'strict',
        // Real SVG <text>, not foreignObject HTML: the diagram then carries
        // no HTML that the page's prose rules could restyle.
        htmlLabels: false,
        flowchart: { curve: 'basis', useMaxWidth: true, padding: 12, htmlLabels: false },
        sequence: { useMaxWidth: true },
        fontFamily:
            "ui-sans-serif, system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif",
    });
}, themeVariables);

const results = [];
for (const job of jobs) {
    try {
        const svg = await page.evaluate(
            async ({ id, source }) => (await window.mermaid.render(id, source)).svg,
            job,
        );
        results.push({ id: job.id, svg });
    } catch (err) {
        results.push({ id: job.id, error: String(err && err.message ? err.message : err) });
        // A failed render leaves an orphan container in the DOM; clear it so
        // the next diagram starts from a clean slate.
        await page.evaluate((id) => {
            document.getElementById('d' + id)?.remove();
            document.getElementById(id)?.remove();
        }, job.id);
    }
}

await browser.close();
process.stdout.write(JSON.stringify(results));
