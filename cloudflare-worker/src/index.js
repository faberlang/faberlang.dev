const PUBLIC_ORIGIN_PLACEHOLDER = "__PUBLIC_ORIGIN__";
const DOCS_VERSION_PLACEHOLDER = "__DOCS_VERSION__";
const DEFAULT_DOCS_VERSION = "1.0.0-rc.1";

const ROOT_DISCOVERY_LINKS = [
  [
    `/docs/${DOCS_VERSION_PLACEHOLDER}/reference/index.md`,
    "documentation",
    "text/markdown",
  ],
  [
    `/contracts/${DOCS_VERSION_PLACEHOLDER}/documents.json`,
    "contracts",
    "application/json",
  ],
  ["/.well-known/agent-skills/index.json", "agent-skills", "application/json"],
  [
    "/.well-known/faber-language.json",
    "language-catalog",
    "application/json",
  ],
  ["/llms.txt", "alternate", "text/markdown"],
];

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname === "/health") {
      return new Response(
        '{"success":true,"data":{"service":"faber-web","status":"ok"}}',
        {
          status: 200,
          headers: { "content-type": "application/json; charset=utf-8" },
        },
      );
    }

    const isNegotiatedPath = url.pathname === "/" || url.pathname === "/index.html";
    const assetUrl = new URL(url);
    if (isNegotiatedPath && prefersMarkdown(request.headers)) {
      assetUrl.pathname = "/llms.txt";
    }

    const assetResponse = await env.ASSETS.fetch(new Request(assetUrl, request));
    const headers = new Headers(assetResponse.headers);
    const contentType = contentTypeFor(assetUrl.pathname, headers.get("content-type"));
    if (contentType) {
      headers.set("content-type", contentType);
    }
    const publicOrigin = guessPublicOrigin(request, env);
    const docsVersion = docsVersionFor(env);

    if (url.pathname === "/") {
      headers.set("link", discoveryLinkValue(publicOrigin, docsVersion));
    }
    if (isNegotiatedPath) {
      headers.set("vary", "Accept");
    }

    const responseInit = {
      status: assetResponse.status,
      statusText: assetResponse.statusText,
      headers,
    };
    if (!isTextual(headers.get("content-type")) || assetResponse.body === null) {
      return new Response(assetResponse.body, responseInit);
    }

    const body = await assetResponse.text();
    return new Response(
      body
        .replaceAll(PUBLIC_ORIGIN_PLACEHOLDER, publicOrigin)
        .replaceAll(DOCS_VERSION_PLACEHOLDER, docsVersion),
      responseInit,
    );
  },
};

function contentTypeFor(path, fallback) {
  if (path.endsWith(".html")) return "text/html; charset=utf-8";
  if (path.endsWith(".css")) return "text/css; charset=utf-8";
  if (path.endsWith(".md") || path === "/llms.txt" || path === "/llms-full.txt") {
    return "text/markdown; charset=utf-8";
  }
  if (path.endsWith(".json")) return "application/json; charset=utf-8";
  if (path.endsWith(".xml")) return "application/xml; charset=utf-8";
  if (path.endsWith(".txt") || path.endsWith(".ebnf")) {
    return "text/plain; charset=utf-8";
  }
  return fallback;
}

function isTextual(contentType) {
  return (
    contentType?.startsWith("text/") ||
    contentType?.includes("application/json") ||
    contentType?.includes("application/xml") ||
    false
  );
}

function prefersMarkdown(headers) {
  const accept = headers.get("accept");
  return accept?.includes("text/markdown") || accept?.includes("text/plain") || false;
}

function docsVersionFor(env) {
  const configured = env.DOCS_VERSION?.trim();
  return configured && !configured.includes(DOCS_VERSION_PLACEHOLDER)
    ? configured
    : DEFAULT_DOCS_VERSION;
}

function guessPublicOrigin(request, env) {
  const configured = env.PUBLIC_ORIGIN?.trim();
  if (configured && !configured.includes(PUBLIC_ORIGIN_PLACEHOLDER)) {
    return configured.replace(/\/$/, "");
  }
  return new URL(request.url).origin;
}

function discoveryLinkValue(publicOrigin, docsVersion) {
  return ROOT_DISCOVERY_LINKS.map(([route, rel, contentType]) => {
    const concreteRoute = route.replaceAll(DOCS_VERSION_PLACEHOLDER, docsVersion);
    return `<${publicOrigin}${concreteRoute}>; rel="${rel}"; type="${contentType}"`;
  }).join(", ");
}
