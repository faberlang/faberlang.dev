use std::collections::BTreeMap;
use std::net::{Ipv4Addr, SocketAddr};

use axum::extract::OriginalUri;
use axum::http::{HeaderMap, HeaderValue, StatusCode, header};
use axum::response::{IntoResponse, Response};
use axum::routing::get;
use axum::{Router, serve};
use tower_http::trace::TraceLayer;

const PUBLIC_ORIGIN_PLACEHOLDER: &str = "__PUBLIC_ORIGIN__";
const DOCS_VERSION_PLACEHOLDER: &str = "__DOCS_VERSION__";
const DOCS_VERSION: &str = "1.0.0-rc.1";

#[derive(Clone)]
struct AppState {
    assets: BTreeMap<&'static str, Asset>,
}

#[derive(Clone, Copy)]
struct Asset {
    body: &'static str,
    content_type: &'static str,
}

macro_rules! asset {
    ($path:expr, $ct:expr) => {
        (
            $path,
            Asset {
                body: include_str!(concat!("../assets", $path)),
                content_type: $ct,
            },
        )
    };
}

fn assets() -> BTreeMap<&'static str, Asset> {
    BTreeMap::from([
        asset!("/index.html", "text/html; charset=utf-8"),
        asset!("/index.css", "text/css; charset=utf-8"),
        asset!("/llms.txt", "text/markdown; charset=utf-8"),
        asset!("/llms-full.txt", "text/markdown; charset=utf-8"),
        asset!("/robots.txt", "text/plain; charset=utf-8"),
        asset!("/sitemap.xml", "application/xml; charset=utf-8"),
        asset!(
            "/.well-known/agent-skills/index.json",
            "application/json; charset=utf-8"
        ),
        asset!(
            "/.well-known/agent-skills/quickstart/SKILL.md",
            "text/markdown; charset=utf-8"
        ),
        asset!(
            "/.well-known/agent-skills/language-syntax/SKILL.md",
            "text/markdown; charset=utf-8"
        ),
        asset!(
            "/.well-known/agent-skills/packages/SKILL.md",
            "text/markdown; charset=utf-8"
        ),
        asset!(
            "/.well-known/agent-skills/build-run/SKILL.md",
            "text/markdown; charset=utf-8"
        ),
        asset!(
            "/.well-known/agent-skills/testing/SKILL.md",
            "text/markdown; charset=utf-8"
        ),
        asset!(
            "/.well-known/agent-skills/diagnostics/SKILL.md",
            "text/markdown; charset=utf-8"
        ),
        asset!(
            "/.well-known/agent-skills/effects/SKILL.md",
            "text/markdown; charset=utf-8"
        ),
        asset!(
            "/.well-known/agent-skills/targets/SKILL.md",
            "text/markdown; charset=utf-8"
        ),
        asset!(
            "/.well-known/agent-skills/libraries/SKILL.md",
            "text/markdown; charset=utf-8"
        ),
        asset!(
            "/.well-known/agent-skills/fmir/SKILL.md",
            "text/markdown; charset=utf-8"
        ),
        asset!(
            "/.well-known/faber-language.json",
            "application/json; charset=utf-8"
        ),
        asset!(
            "/docs/1.0.0-rc.1/quickstart.md",
            "text/markdown; charset=utf-8"
        ),
        asset!(
            "/docs/1.0.0-rc.1/language/index.md",
            "text/markdown; charset=utf-8"
        ),
        asset!(
            "/docs/1.0.0-rc.1/packages/index.md",
            "text/markdown; charset=utf-8"
        ),
        asset!(
            "/docs/1.0.0-rc.1/effects/index.md",
            "text/markdown; charset=utf-8"
        ),
        asset!(
            "/docs/1.0.0-rc.1/diagnostics/index.md",
            "text/markdown; charset=utf-8"
        ),
        asset!(
            "/contracts/1.0.0-rc.1/grammar.ebnf",
            "text/plain; charset=utf-8"
        ),
        asset!(
            "/contracts/1.0.0-rc.1/keywords.json",
            "application/json; charset=utf-8"
        ),
        asset!(
            "/contracts/1.0.0-rc.1/types.json",
            "application/json; charset=utf-8"
        ),
        asset!(
            "/contracts/1.0.0-rc.1/operators.json",
            "application/json; charset=utf-8"
        ),
        asset!(
            "/contracts/1.0.0-rc.1/targets.json",
            "application/json; charset=utf-8"
        ),
        asset!(
            "/contracts/1.0.0-rc.1/diagnostics.json",
            "application/json; charset=utf-8"
        ),
        asset!(
            "/contracts/1.0.0-rc.1/providers.json",
            "application/json; charset=utf-8"
        ),
        asset!(
            "/contracts/1.0.0-rc.1/documents.json",
            "application/json; charset=utf-8"
        ),
        asset!(
            "/contracts/1.0.0-rc.1/checksums.json",
            "application/json; charset=utf-8"
        ),
        // faber-contract.tar.zst is a build-time artifact; not embedded as source.
    ])
}

#[tokio::main]
async fn main() {
    tracing_subscriber::fmt()
        .with_env_filter(
            tracing_subscriber::EnvFilter::try_from_default_env()
                .unwrap_or_else(|_| "faber_web=info,tower_http=info".into()),
        )
        .init();

    let bind = SocketAddr::new(Ipv4Addr::new(0, 0, 0, 0).into(), port());
    let state = AppState { assets: assets() };
    let app = Router::new()
        .route("/health", get(health))
        .fallback(get(asset))
        .layer(TraceLayer::new_for_http())
        .with_state(state);

    let listener = tokio::net::TcpListener::bind(bind)
        .await
        .unwrap_or_else(|error| panic!("failed to bind {bind}: {error}"));

    tracing::info!(%bind, "faber-web HTTP server listening");
    serve(listener, app)
        .with_graceful_shutdown(shutdown_signal())
        .await
        .expect("faber-web HTTP server failed");
}

fn port() -> u16 {
    std::env::var("PORT")
        .ok()
        .and_then(|v| v.parse().ok())
        .unwrap_or(8080)
}

async fn health() -> impl IntoResponse {
    (
        StatusCode::OK,
        [(header::CONTENT_TYPE, "application/json; charset=utf-8")],
        r#"{"success":true,"data":{"service":"faber-web","status":"ok"}}"#,
    )
}

async fn asset(
    axum::extract::State(state): axum::extract::State<AppState>,
    OriginalUri(uri): OriginalUri,
    headers: HeaderMap,
) -> Response {
    let path = uri.path();

    // Root content negotiation: serve llms.txt when Accept: text/markdown
    let asset_path = if path == "/" || path == "/index.html" {
        if prefers_markdown(&headers) {
            "/llms.txt"
        } else {
            "/index.html"
        }
    } else {
        path
    };

    let Some(asset) = state.assets.get(asset_path) else {
        return (StatusCode::NOT_FOUND, "Not Found").into_response();
    };

    let public_origin = guess_public_origin(&headers);
    let body = asset
        .body
        .replace(PUBLIC_ORIGIN_PLACEHOLDER, &public_origin)
        .replace(DOCS_VERSION_PLACEHOLDER, DOCS_VERSION);

    let mut response = (StatusCode::OK, body).into_response();
    response.headers_mut().insert(
        header::CONTENT_TYPE,
        HeaderValue::from_static(asset.content_type),
    );

    // Discovery headers for the root response
    if path == "/" {
        inject_discovery_headers(&mut response, &public_origin);
    }
    // Content negotiation header
    if path == "/" {
        response.headers_mut().insert(
            header::VARY,
            HeaderValue::from_static("Accept"),
        );
        response.headers_mut().insert(
            header::LINK,
            link_value(&public_origin),
        );
    }

    response
}

fn prefers_markdown(headers: &HeaderMap) -> bool {
    headers
        .get(header::ACCEPT)
        .and_then(|v| v.to_str().ok())
        .map(|accept| {
            accept.contains("text/markdown") || accept.contains("text/plain")
        })
        .unwrap_or(false)
}

fn inject_discovery_headers(response: &mut Response, public_origin: &str) {
    let headers = response.headers_mut();
    // Link discovery: docs, contracts, agent-skills, llms.txt alternate
    let links = vec![
        format!("<{public_origin}/docs/{DOCS_VERSION}/>; rel=\"documentation\""),
        format!("<{public_origin}/contracts/{DOCS_VERSION}/>; rel=\"contracts\""),
        format!(
            "<{public_origin}/.well-known/agent-skills/index.json>; \
             rel=\"agent-skills\""
        ),
        format!(
            "<{public_origin}/.well-known/faber-language.json>; \
             rel=\"language-catalog\""
        ),
        format!(
            "<{public_origin}/llms.txt>; rel=\"alternate\"; \
             type=\"text/markdown\""
        ),
    ];
    headers.insert(
        header::LINK,
        HeaderValue::from_str(&links.join(", ")).unwrap_or(HeaderValue::from_static("")),
    );
}

fn link_value(public_origin: &str) -> HeaderValue {
    HeaderValue::from_str(&format!(
        "<{public_origin}/llms.txt>; rel=\"alternate\"; type=\"text/markdown\""
    ))
    .unwrap_or(HeaderValue::from_static(""))
}

fn guess_public_origin(headers: &HeaderMap) -> String {
    // Try explicit env var first
    if let Ok(origin) = std::env::var("PUBLIC_ORIGIN") {
        if !origin.is_empty() {
            return origin.trim_end_matches('/').to_string();
        }
    }
    // Try Host header
    if let Some(host) = headers
        .get(header::HOST)
        .and_then(|v| v.to_str().ok())
    {
        let scheme = if headers.get("x-forwarded-proto").map(|v| v.as_bytes()) == Some(b"https") {
            "https"
        } else {
            "http"
        };
        return format!("{scheme}://{host}");
    }
    // Fallback
    format!("http://localhost:{}", port())
}

async fn shutdown_signal() {
    tokio::signal::ctrl_c()
        .await
        .expect("failed to install Ctrl+C handler");
    tracing::info!("shutting down");
}
