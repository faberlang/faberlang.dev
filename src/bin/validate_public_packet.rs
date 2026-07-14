use std::fs;
use std::path::{Path, PathBuf};

use serde::Deserialize;
use sha2::{Digest, Sha256};

const DOCS_VERSION: &str = "1.0.0-rc.1";
const CANONICAL_PUBLIC_ORIGIN: &str = "https://faberlang.dev";

const REQUIRED_ROUTES: &[&str] = &[
    "/docs/__DOCS_VERSION__/evaluate/index.md",
    "/docs/__DOCS_VERSION__/learn/index.md",
    "/docs/__DOCS_VERSION__/reference/index.md",
    "/docs/__DOCS_VERSION__/targets/index.md",
    "/docs/__DOCS_VERSION__/examples/index.md",
    "/reports/stage-1-leakage-check.md",
    "/reports/rc1-private-preview-checklist.md",
];

const ROOT_DISCOVERY_ROUTES: &[&str] = &[
    "/docs/__DOCS_VERSION__/reference/index.md",
    "/contracts/__DOCS_VERSION__/documents.json",
    "/.well-known/agent-skills/index.json",
    "/.well-known/faber-language.json",
    "/llms.txt",
];

const REMOVED_CONTRACT_ARCHIVE_MARKERS: &[&str] = &[
    "faber-contract.tar.zst",
    "/contracts/<version>/faber-contract.tar.zst",
    "/contracts/__DOCS_VERSION__/faber-contract.tar.zst",
    "/contracts/1.0.0-rc.1/faber-contract.tar.zst",
];

const LOCAL_STATUS_FILES: &[&str] = &[
    "assets/index.html",
    "assets/llms.txt",
    "assets/docs/1.0.0-rc.1/evaluate/index.md",
    "assets/reports/stage-1-leakage-check.md",
    "assets/reports/rc1-private-preview-checklist.md",
];

const PROVENANCE_MANIFEST: &str = "assets/reports/rc1-provenance-manifest.json";
const PROVENANCE_REPORTS: &[(&str, &str)] = &[
    (
        "assets/reports/stage-1-leakage-check.md",
        "local binary evidence",
    ),
    (
        "assets/reports/rc1-private-preview-checklist.md",
        "private-preview checklist",
    ),
];

const EMPTY_PROVIDER_ROUTE_DENIED_PHRASES: &[&str] = &[
    "ad routing and providers",
    "effects route to host providers",
    "effects are declared via the ad keyword and route to host providers",
    "route to host providers",
    "example routes",
    "five provider crates ship",
    "choosing a capability from a host provider",
    "select provider capabilities",
    "documented route name",
    "generated native packages link only",
    "providers selected by analysis",
    "provider capability is a structured build error",
    "unknown provider capability produces",
    "complete set for",
    "provider effects are routed through",
    "faber `ad` routes",
    "faber ad routes",
];

const FORBIDDEN_PRIVATE_TERMS: &[&str] = &[
    "docs/factory",
    "deferred",
    "HIR",
    "MIR",
    "FMIR",
    "lowering",
    "codegen",
    "Radix",
    "private compiler",
];

const DENIED_PUBLIC_CLAIM_PATTERNS: &[&str] = &[
    "Install with one command",
    "public release",
    "install guide",
    "released binary",
    "Build from source",
    "source build",
    "Homebrew",
    "curl",
    "binary download",
    "open source",
    "public repo",
    "public repository",
    "source export",
    "public source export",
    "public deploy",
    "public deployment",
    "deployed site",
    "site is deployed",
    "live site",
    "Package registry live",
    "registry is live",
    "registry live",
    "live registry",
    "cista.dev is live",
    "publish your package",
    "package publishing",
    "published manifest",
    "published manifests",
    "published diagnostic",
    "Only those published",
    "generated autograd",
    "pytorch session",
    "pytorch equivalence",
    "pytorch equivalent",
    "inference runtime",
    "llama.cpp",
    "llama cpp",
    "GGUF",
    "model loading",
    "GPU execution",
    "rendering claim",
    "render pipeline",
    "browser execution",
    "three js",
    "threejs",
    "authoritative syntax reference",
    "authoritative grammar",
    "Go is supported",
    "Full coreutils",
    "multi-backend coreutils",
    "production ready",
    "production ready language",
    "stable language",
];

fn main() {
    let root = PathBuf::from(env!("CARGO_MANIFEST_DIR"));
    let mut failures = Vec::new();

    verify_required_files(&root, &mut failures);
    verify_public_asset_terms(&root, &mut failures);
    verify_local_status_labels(&root, &mut failures);
    verify_removed_fmir_route(&root, &mut failures);
    verify_route_coverage(&root, &mut failures);
    verify_document_catalog_coverage(&root, &mut failures);
    verify_document_catalog_digests(&root, &mut failures);
    verify_contract_checksums(&root, &mut failures);
    verify_empty_provider_route_claim_gate(&root, &mut failures);
    verify_agent_skill_digests(&root, &mut failures);
    verify_internal_route_references(&root, &mut failures);
    verify_root_discovery_links(&root, &mut failures);
    verify_contract_archive_claim_gate(&root, &mut failures);
    verify_local_binary_evidence(&root, &mut failures);
    verify_private_preview_checklist(&root, &mut failures);
    verify_provenance_manifest_contract(&root, &mut failures);
    verify_autograd_boundary(&root, &mut failures);
    verify_json(&root, &mut failures);

    if failures.is_empty() {
        println!("public packet validation passed");
        return;
    }

    eprintln!("public packet validation failed:");
    for failure in failures {
        eprintln!("- {failure}");
    }
    std::process::exit(1);
}

#[derive(Deserialize)]
struct ProvenanceManifest {
    version: String,
    contract: String,
    snapshot_date: String,
    frozen_at: FrozenAt,
    provenance: Provenance,
    local_binary: LocalBinary,
    autograd_proximity: AutogradProximity,
    claim_boundary: Vec<String>,
}

#[derive(Deserialize)]
struct FrozenAt {
    faber: CommitEvidence,
    faberlang_dev: CommitEvidence,
}

#[derive(Deserialize)]
struct CommitEvidence {
    commit: String,
    subject: String,
}

#[derive(Deserialize)]
struct Provenance {
    compiler: String,
    faber: String,
}

#[derive(Deserialize)]
struct LocalBinary {
    build_command: String,
    version_result: String,
    path: String,
    sha256: String,
    size_observed: String,
}

#[derive(Deserialize)]
struct AutogradProximity {
    faber_runtime: String,
    examples: String,
    fixture_scope: String,
    output_checked_device_autograd_floor: u64,
    boundary_statement: String,
}

fn verify_required_files(root: &Path, failures: &mut Vec<String>) {
    for route in REQUIRED_ROUTES {
        let asset = route_to_asset_path(route);
        if !root.join(&asset).is_file() {
            failures.push(format!(
                "missing required asset for {route}: {}",
                asset.display()
            ));
        }
    }
}

fn verify_public_asset_terms(root: &Path, failures: &mut Vec<String>) {
    let mut files = Vec::new();
    collect_text_assets(&root.join("assets"), &mut files);

    for file in files {
        let text = read_to_string(root, &file, failures);
        for term in FORBIDDEN_PRIVATE_TERMS {
            if text.contains(term) {
                failures.push(format!(
                    "forbidden private term `{term}` in {}",
                    file.display()
                ));
            }
        }
        for claim in DENIED_PUBLIC_CLAIM_PATTERNS {
            if contains_denied_public_claim(&text, claim) {
                failures.push(format!(
                    "forbidden public claim `{claim}` in {}",
                    file.display()
                ));
            }
        }
    }
}

fn normalize_claim_text(text: &str) -> String {
    text.to_lowercase()
        .chars()
        .map(|ch| if ch.is_ascii_alphanumeric() { ch } else { ' ' })
        .collect::<String>()
        .split_whitespace()
        .collect::<Vec<_>>()
        .join(" ")
}

fn contains_denied_public_claim(text: &str, claim: &str) -> bool {
    let normalized_claim = normalize_claim_text(claim);
    for segment in claim_context_segments(text) {
        let normalized_segment = normalize_claim_text(&segment);
        let mut search_from = 0;

        while let Some(relative_start) = normalized_segment[search_from..].find(&normalized_claim) {
            let start = search_from + relative_start;
            let end = start + normalized_claim.len();
            if !is_gated_or_negative_context(&normalized_segment, start, end) {
                return true;
            }
            search_from = end;
        }
    }

    false
}

fn claim_context_segments(text: &str) -> Vec<String> {
    let mut segments = Vec::new();
    let mut paragraph = String::new();
    let mut boundary_intro: Option<String> = None;

    for line in text.lines() {
        let trimmed = line.trim();
        if trimmed.is_empty() {
            push_paragraph_segments(&paragraph, &mut segments);
            paragraph.clear();
            continue;
        }
        if trimmed.starts_with('#') {
            push_paragraph_segments(&paragraph, &mut segments);
            paragraph.clear();
            boundary_intro = boundary_intro_line(trimmed);
            continue;
        }
        if line.contains('|') {
            push_paragraph_segments(&paragraph, &mut segments);
            paragraph.clear();
            segments.push(line.to_owned());
            continue;
        }
        if trimmed.ends_with(':') {
            push_paragraph_segments(&paragraph, &mut segments);
            paragraph.clear();
            boundary_intro = boundary_intro_line(trimmed);
            if boundary_intro.is_none() {
                segments.push(line.to_owned());
            }
            continue;
        }
        if trimmed.starts_with("- ") {
            push_paragraph_segments(&paragraph, &mut segments);
            paragraph.clear();
            if let Some(intro) = &boundary_intro {
                segments.push(format!("{intro} {line}"));
            } else {
                segments.push(line.to_owned());
            }
            continue;
        }
        if line.starts_with(char::is_whitespace) {
            push_paragraph_segments(&paragraph, &mut segments);
            paragraph.clear();
            if let Some(previous) = segments.last_mut() {
                previous.push(' ');
                previous.push_str(line);
            } else if let Some(intro) = &boundary_intro {
                segments.push(format!("{intro} {line}"));
            }
            continue;
        }
        boundary_intro = None;
        paragraph.push(' ');
        paragraph.push_str(line);
    }
    push_paragraph_segments(&paragraph, &mut segments);
    segments
}

fn boundary_intro_line(line: &str) -> Option<String> {
    let normalized = normalize_claim_text(line);
    [
        "do not",
        "do not claim",
        "do not infer",
        "avoid",
        "hard gates",
        "known remaining gates",
        "required before public use",
    ]
    .iter()
    .any(|marker| contains_marker(&normalized, marker))
    .then(|| line.to_owned())
}

fn push_paragraph_segments(paragraph: &str, segments: &mut Vec<String>) {
    for segment in paragraph.split(['.', '!', '?']) {
        if !segment.trim().is_empty() {
            segments.push(segment.to_owned());
        }
    }
}

fn is_gated_or_negative_context(normalized_segment: &str, start: usize, end: usize) -> bool {
    let before = &normalized_segment[..start];
    let after = &normalized_segment[end..];

    let prefix_markers = [
        "no",
        "not",
        "do not",
        "does not",
        "did not",
        "did not find",
        "must not",
        "must not be",
        "cannot",
        "without",
        "avoid",
        "avoids",
        "gate",
        "gated",
        "blocker",
        "blocked",
        "require",
        "requires",
        "do not claim",
        "not claim",
        "no claim",
        "no live",
        "no product claim",
        "claim boundary",
        "claims gated",
        "claims remain gated",
        "claims without",
        "boundary statement",
        "not public",
        "not a public",
        "not create",
        "do not publish",
        "before any",
    ];
    let suffix_markers = [
        "remain gated",
        "remains gated",
        "claim remains gated",
        "claims remain gated",
        "claims gated",
        "is gated",
        "are gated",
        "stays gated",
        "remain blocked",
        "remains blocked",
        "is blocked",
        "are blocked",
        "is a blocker",
        "are blockers",
        "without",
        "until",
        "before",
        "gate",
        "gated",
        "blocker",
        "blocked",
        "proof",
        "claim",
        "claims",
    ];

    prefix_markers
        .iter()
        .any(|marker| contains_marker(before, marker))
        || suffix_markers
            .iter()
            .any(|marker| contains_marker(after, marker))
}

fn contains_marker(text: &str, marker: &str) -> bool {
    text.split_whitespace()
        .collect::<Vec<_>>()
        .windows(marker.split_whitespace().count())
        .any(|window| window.join(" ") == marker)
}

fn contains_normalized_phrase(text: &str, phrase: &str) -> bool {
    normalize_claim_text(text).contains(&normalize_claim_text(phrase))
}

fn verify_local_status_labels(root: &Path, failures: &mut Vec<String>) {
    for file in LOCAL_STATUS_FILES {
        let text = read_to_string(root, Path::new(file), failures).to_lowercase();
        if !text.contains("local") {
            failures.push(format!("{file} does not label the packet as local"));
        }
        if !text.contains("gated") {
            failures.push(format!("{file} does not state public claims are gated"));
        }
    }
}

fn verify_removed_fmir_route(root: &Path, failures: &mut Vec<String>) {
    let removed = root.join("assets/.well-known/agent-skills/fmir/SKILL.md");
    if removed.exists() {
        failures.push("removed FMIR public skill file still exists".to_string());
    }

    for file in [
        "assets/.well-known/agent-skills/index.json",
        "assets/contracts/1.0.0-rc.1/documents.json",
        "assets/sitemap.xml",
        "src/main.rs",
    ] {
        let text = read_to_string(root, Path::new(file), failures);
        if text.to_lowercase().contains("fmir") {
            failures.push(format!("removed FMIR route still referenced in {file}"));
        }
    }
}

fn verify_route_coverage(root: &Path, failures: &mut Vec<String>) {
    let documents = read_to_string(
        root,
        Path::new("assets/contracts/1.0.0-rc.1/documents.json"),
        failures,
    );
    let sitemap = read_to_string(root, Path::new("assets/sitemap.xml"), failures);
    let main = read_to_string(root, Path::new("src/main.rs"), failures);

    for route in REQUIRED_ROUTES {
        let versioned = route.replace("__DOCS_VERSION__", DOCS_VERSION);
        let source_route = route.to_string();

        if !documents.contains(&source_route) {
            failures.push(format!("documents.json missing {source_route}"));
        }
        if !sitemap.contains(&source_route) {
            failures.push(format!("sitemap.xml missing {source_route}"));
        }
        if !main.contains(&versioned) {
            failures.push(format!("src/main.rs does not embed {versioned}"));
        }
    }
}

fn verify_document_catalog_coverage(root: &Path, failures: &mut Vec<String>) {
    let routes = document_catalog_routes(root, failures);
    let sitemap = read_to_string(root, Path::new("assets/sitemap.xml"), failures);
    let main = read_to_string(root, Path::new("src/main.rs"), failures);

    for route in routes {
        let asset = route_to_asset_path(&route);
        let versioned = route.replace("__DOCS_VERSION__", DOCS_VERSION);

        if !root.join(&asset).is_file() {
            failures.push(format!(
                "documents.json route {route} has no asset at {}",
                asset.display()
            ));
        }
        if !sitemap.contains(&route) {
            failures.push(format!("sitemap.xml missing cataloged route {route}"));
        }
        if !main.contains(&versioned) {
            failures.push(format!(
                "src/main.rs does not embed cataloged route {versioned}"
            ));
        }
    }
}

fn document_catalog_routes(root: &Path, failures: &mut Vec<String>) -> Vec<String> {
    let text = read_to_string(
        root,
        Path::new("assets/contracts/1.0.0-rc.1/documents.json"),
        failures,
    );
    let Ok(value) = serde_json::from_str::<serde_json::Value>(&text) else {
        failures.push("documents.json is not valid JSON for route coverage".to_string());
        return Vec::new();
    };
    let Some(documents) = value
        .get("documents")
        .and_then(|documents| documents.as_object())
    else {
        failures.push("documents.json missing object field `documents`".to_string());
        return Vec::new();
    };

    let mut routes = documents.keys().cloned().collect::<Vec<_>>();
    routes.sort();
    routes
}

fn verify_document_catalog_digests(root: &Path, failures: &mut Vec<String>) {
    let text = read_to_string(
        root,
        Path::new("assets/contracts/1.0.0-rc.1/documents.json"),
        failures,
    );
    let Ok(value) = serde_json::from_str::<serde_json::Value>(&text) else {
        failures.push("documents.json is not valid JSON for digest validation".to_string());
        return;
    };
    let Some(documents) = value
        .get("documents")
        .and_then(|documents| documents.as_object())
    else {
        failures.push("documents.json missing object field `documents`".to_string());
        return;
    };

    for (route, metadata) in documents {
        let Some(sha256) = metadata.get("sha256").and_then(|value| value.as_str()) else {
            failures.push(format!("documents.json route {route} missing sha256"));
            continue;
        };
        if !is_sha256_hex(sha256) {
            failures.push(format!(
                "documents.json route {route} has invalid sha256 `{sha256}`"
            ));
            continue;
        }
        let Some(actual) = served_asset_sha256(root, route, failures) else {
            continue;
        };
        if sha256 != actual {
            failures.push(format!(
                "documents.json route {route} sha256 mismatch: expected {sha256}, got {actual}"
            ));
        }
    }
}

fn verify_contract_checksums(root: &Path, failures: &mut Vec<String>) {
    let text = read_to_string(
        root,
        Path::new("assets/contracts/1.0.0-rc.1/checksums.json"),
        failures,
    );
    let Ok(value) = serde_json::from_str::<serde_json::Value>(&text) else {
        failures.push("checksums.json is not valid JSON for digest validation".to_string());
        return;
    };
    let Some(contracts) = value
        .get("contracts")
        .and_then(|contracts| contracts.as_object())
    else {
        failures.push("checksums.json missing object field `contracts`".to_string());
        return;
    };

    for (route, digest) in contracts {
        let Some(sha256) = digest.as_str() else {
            failures.push(format!(
                "checksums.json route {route} sha256 is not a string"
            ));
            continue;
        };
        if !is_sha256_hex(sha256) {
            failures.push(format!(
                "checksums.json route {route} has invalid sha256 `{sha256}`"
            ));
            continue;
        }
        let Some(actual) = served_asset_sha256(root, route, failures) else {
            continue;
        };
        if sha256 != actual {
            failures.push(format!(
                "checksums.json route {route} sha256 mismatch: expected {sha256}, got {actual}"
            ));
        }
    }
}

fn verify_empty_provider_route_claim_gate(root: &Path, failures: &mut Vec<String>) {
    if !provider_contract_has_empty_routes(root, failures) {
        return;
    }

    for route in provider_claim_gate_routes(root, failures) {
        let file = route_to_asset_path(&route);
        let text = read_to_string(root, &file, failures);
        for phrase in empty_provider_route_claim_phrases(&text) {
            failures.push(format!(
                "{} uses provider capability phrase `{phrase}` while providers.json has empty routes",
                file.display()
            ));
        }
    }
}

fn provider_claim_gate_routes(root: &Path, failures: &mut Vec<String>) -> Vec<String> {
    document_catalog_routes(root, failures)
        .into_iter()
        .filter(|route| {
            route.starts_with("/docs/")
                || route.starts_with("/.well-known/agent-skills/")
                || route == "/.well-known/faber-language.json"
        })
        .collect()
}

fn empty_provider_route_claim_phrases(text: &str) -> Vec<&'static str> {
    EMPTY_PROVIDER_ROUTE_DENIED_PHRASES
        .iter()
        .copied()
        .filter(|phrase| contains_normalized_phrase(text, phrase))
        .collect()
}

fn provider_contract_has_empty_routes(root: &Path, failures: &mut Vec<String>) -> bool {
    let text = read_to_string(
        root,
        Path::new("assets/contracts/1.0.0-rc.1/providers.json"),
        failures,
    );
    let Ok(value) = serde_json::from_str::<serde_json::Value>(&text) else {
        failures.push("providers.json is not valid JSON for provider route gate".to_string());
        return false;
    };
    let Some(providers) = value
        .get("providers")
        .and_then(|providers| providers.as_object())
    else {
        failures.push("providers.json missing object field `providers`".to_string());
        return false;
    };

    providers.values().any(|metadata| {
        metadata
            .get("routes")
            .and_then(|routes| routes.as_array())
            .is_none_or(|routes| routes.is_empty())
    })
}

fn verify_agent_skill_digests(root: &Path, failures: &mut Vec<String>) {
    let text = read_to_string(
        root,
        Path::new("assets/.well-known/agent-skills/index.json"),
        failures,
    );
    let Ok(value) = serde_json::from_str::<serde_json::Value>(&text) else {
        failures.push("agent skill index is not valid JSON for digest validation".to_string());
        return;
    };
    let Some(skills) = value.get("skills").and_then(|skills| skills.as_array()) else {
        failures.push("agent skill index missing array field `skills`".to_string());
        return;
    };

    for skill in skills {
        let name = skill
            .get("name")
            .and_then(|value| value.as_str())
            .unwrap_or("<unnamed>");
        let Some(url) = skill.get("url").and_then(|value| value.as_str()) else {
            failures.push(format!("agent skill `{name}` missing url"));
            continue;
        };
        let Some(sha256) = skill.get("sha256").and_then(|value| value.as_str()) else {
            failures.push(format!("agent skill `{name}` missing sha256"));
            continue;
        };
        if !is_sha256_hex(sha256) {
            failures.push(format!(
                "agent skill `{name}` has invalid sha256 `{sha256}`"
            ));
            continue;
        }
        let Some(actual) = served_asset_sha256(root, url, failures) else {
            continue;
        };
        if sha256 != actual {
            failures.push(format!(
                "agent skill `{name}` sha256 mismatch: expected {sha256}, got {actual}"
            ));
        }
    }
}

fn served_asset_sha256(root: &Path, route: &str, failures: &mut Vec<String>) -> Option<String> {
    let asset = route_to_asset_path(route);
    if !root.join(&asset).is_file() {
        failures.push(format!(
            "digest route {route} has no asset at {}",
            asset.display()
        ));
        return None;
    }
    let text = read_to_string(root, &asset, failures);
    Some(sha256_hex(&render_served_text(&text)))
}

fn render_served_text(text: &str) -> String {
    text.replace("__PUBLIC_ORIGIN__", CANONICAL_PUBLIC_ORIGIN)
        .replace("__DOCS_VERSION__", DOCS_VERSION)
}

fn sha256_hex(text: &str) -> String {
    format!("{:x}", Sha256::digest(text.as_bytes()))
}

fn is_sha256_hex(value: &str) -> bool {
    value.len() == 64 && value.chars().all(|ch| ch.is_ascii_hexdigit())
}

fn verify_internal_route_references(root: &Path, failures: &mut Vec<String>) {
    let known_routes = served_asset_routes(root);
    let mut files = Vec::new();
    collect_text_assets(&root.join("assets"), &mut files);

    for file in files {
        let text = read_to_string(root, &file, failures);
        let references = if file
            .extension()
            .is_some_and(|extension| extension == "json")
        {
            json_route_references(&text, failures, &file)
        } else {
            text_route_references(&text)
        };

        for reference in references {
            if !route_reference_resolves(&reference, &known_routes) {
                failures.push(format!(
                    "unresolved internal route reference `{reference}` in {}",
                    file.display()
                ));
            }
        }
    }
}

fn verify_root_discovery_links(root: &Path, failures: &mut Vec<String>) {
    let main = read_to_string(root, Path::new("src/main.rs"), failures);
    let known_routes = served_asset_routes(root);

    for route in ROOT_DISCOVERY_ROUTES {
        let versioned = route.replace("__DOCS_VERSION__", DOCS_VERSION);
        if !known_routes
            .iter()
            .any(|known_route| known_route == &versioned)
        {
            failures.push(format!(
                "root discovery Link target {versioned} is not a served asset route"
            ));
        }
        if !main.contains(&versioned) {
            failures.push(format!(
                "src/main.rs root discovery Link set missing {versioned}"
            ));
        }
    }
}

fn verify_contract_archive_claim_gate(root: &Path, failures: &mut Vec<String>) {
    let stale_archive = root.join("assets/contracts/1.0.0-rc.1/faber-contract.tar.zst");
    if stale_archive.exists() {
        failures.push(format!(
            "contract archive placeholder exists but is not served: {}",
            stale_archive.display()
        ));
    }

    for path in contract_archive_claim_scan_files(root) {
        let text = read_to_string(root, &path, failures);
        for marker in REMOVED_CONTRACT_ARCHIVE_MARKERS {
            if text.contains(marker) {
                failures.push(format!(
                    "unserved contract archive claim `{marker}` in {}",
                    path.display()
                ));
            }
        }
    }
}

fn contract_archive_claim_scan_files(root: &Path) -> Vec<PathBuf> {
    let mut files = Vec::new();
    collect_text_assets(&root.join("assets"), &mut files);
    collect_text_assets(&root.join("docs"), &mut files);
    files.push(root.join("src/main.rs"));
    files
}

fn served_asset_routes(root: &Path) -> Vec<String> {
    let mut files = Vec::new();
    collect_asset_files(&root.join("assets"), &mut files);

    let mut routes = vec!["/".to_string()];
    for file in files {
        if file.extension().is_some_and(|extension| extension == "zst") {
            continue;
        }
        if let Ok(relative) = file.strip_prefix(root.join("assets")) {
            routes.push(format!("/{}", relative.to_string_lossy()));
        }
    }
    routes.sort();
    routes
}

fn text_route_references(text: &str) -> Vec<String> {
    let mut references = Vec::new();
    for line in text.lines() {
        collect_attribute_routes(line, "href=\"", &mut references);
        collect_attribute_routes(line, "src=\"", &mut references);
        collect_markdown_link_routes(line, &mut references);
        collect_backtick_routes(line, &mut references);
    }
    references
}

fn collect_attribute_routes(line: &str, marker: &str, references: &mut Vec<String>) {
    let mut rest = line;
    while let Some(start) = rest.find(marker) {
        rest = &rest[start + marker.len()..];
        let Some(end) = rest.find('"') else {
            break;
        };
        push_internal_route(&rest[..end], references);
        rest = &rest[end + 1..];
    }
}

fn collect_markdown_link_routes(line: &str, references: &mut Vec<String>) {
    let mut rest = line;
    while let Some(start) = rest.find("](") {
        rest = &rest[start + 2..];
        let Some(end) = rest.find(')') else {
            break;
        };
        push_internal_route(&rest[..end], references);
        rest = &rest[end + 1..];
    }
}

fn collect_backtick_routes(line: &str, references: &mut Vec<String>) {
    for (index, segment) in line.split('`').enumerate() {
        if index % 2 == 1 {
            push_internal_route(segment, references);
        }
    }
}

fn json_route_references(text: &str, failures: &mut Vec<String>, file: &Path) -> Vec<String> {
    let Ok(value) = serde_json::from_str::<serde_json::Value>(text) else {
        failures.push(format!(
            "invalid JSON in {} while checking route references",
            file.display()
        ));
        return Vec::new();
    };

    let mut references = Vec::new();
    collect_json_route_strings(&value, &mut references);
    references
}

fn collect_json_route_strings(value: &serde_json::Value, references: &mut Vec<String>) {
    match value {
        serde_json::Value::String(value) => push_internal_route(value, references),
        serde_json::Value::Array(items) => {
            for item in items {
                collect_json_route_strings(item, references);
            }
        }
        serde_json::Value::Object(fields) => {
            for value in fields.values() {
                collect_json_route_strings(value, references);
            }
        }
        _ => {}
    }
}

fn push_internal_route(value: &str, references: &mut Vec<String>) {
    let value = value.trim();
    if value.starts_with('/') || value.starts_with("__PUBLIC_ORIGIN__/") {
        references.push(value.to_string());
    }
}

fn route_reference_resolves(reference: &str, known_routes: &[String]) -> bool {
    let mut route = reference
        .strip_prefix("__PUBLIC_ORIGIN__")
        .unwrap_or(reference)
        .to_string();
    route = route.replace("__DOCS_VERSION__", DOCS_VERSION);

    if route.contains('*') {
        return false;
    }

    known_routes.iter().any(|known_route| known_route == &route)
}

fn verify_local_binary_evidence(root: &Path, failures: &mut Vec<String>) {
    let report = read_to_string(
        root,
        Path::new("assets/reports/stage-1-leakage-check.md"),
        failures,
    );
    let manifest = provenance_manifest(root, failures);
    let mut expected = vec![
        "public release artifact checksum".to_string(),
        "pushed tag".to_string(),
        "deployment".to_string(),
    ];
    if let Some(manifest) = manifest.as_ref() {
        expected.extend(provenance_report_expectations(manifest));
    }
    for expected in expected {
        if !report.contains(&expected) {
            failures.push(format!("local binary evidence missing `{expected}`"));
        }
    }
}

fn verify_private_preview_checklist(root: &Path, failures: &mut Vec<String>) {
    let checklist = read_to_string(
        root,
        Path::new("assets/reports/rc1-private-preview-checklist.md"),
        failures,
    );
    let manifest = provenance_manifest(root, failures);
    let mut expected = vec![
        "private-preview checklist".to_string(),
        "not public launch approval".to_string(),
        "not create a public artifact".to_string(),
        "Required Before Public Use".to_string(),
    ];
    if let Some(manifest) = manifest.as_ref() {
        expected.extend(provenance_report_expectations(manifest));
    }
    for expected in expected {
        if !checklist.contains(&expected) {
            failures.push(format!("private-preview checklist missing `{expected}`"));
        }
    }
}

fn verify_provenance_manifest_contract(root: &Path, failures: &mut Vec<String>) {
    let Some(manifest) = provenance_manifest(root, failures) else {
        return;
    };

    if manifest.version != "__DOCS_VERSION__" {
        failures.push(format!(
            "provenance manifest version must use __DOCS_VERSION__, got `{}`",
            manifest.version
        ));
    }
    if manifest.contract != "frozen_private_preview_snapshot" {
        failures.push(format!(
            "provenance manifest has unsupported contract `{}`",
            manifest.contract
        ));
    }
    if !is_iso_date(&manifest.snapshot_date) {
        failures.push(format!(
            "provenance manifest snapshot_date is not YYYY-MM-DD: `{}`",
            manifest.snapshot_date
        ));
    }
    for (label, commit) in [
        (
            "faber frozen commit",
            manifest.frozen_at.faber.commit.as_str(),
        ),
        (
            "faberlang.dev frozen commit",
            manifest.frozen_at.faberlang_dev.commit.as_str(),
        ),
    ] {
        if !is_git_commit_hex(commit) {
            failures.push(format!("{label} is not a full git commit: `{commit}`"));
        }
    }
    if !is_sha256_hex(&manifest.local_binary.sha256) {
        failures.push(format!(
            "provenance manifest local_binary.sha256 is invalid: `{}`",
            manifest.local_binary.sha256
        ));
    }
    if manifest
        .claim_boundary
        .iter()
        .any(|boundary| boundary.contains("public artifact"))
        && !manifest
            .claim_boundary
            .iter()
            .any(|boundary| boundary.contains("not a public artifact"))
    {
        failures.push(
            "provenance manifest claim boundary mentions public artifact without a negative gate"
                .to_string(),
        );
    }

    let expected = provenance_report_expectations(&manifest);
    for (file, label) in PROVENANCE_REPORTS {
        let text = read_to_string(root, Path::new(file), failures);
        if uses_current_local_evidence_wording(&text) {
            failures.push(format!(
                "{label} uses current/local evidence wording for a frozen snapshot contract"
            ));
        }
        for expected in &expected {
            if !text.contains(expected) {
                failures.push(format!(
                    "{label} missing manifest-backed evidence `{expected}`"
                ));
            }
        }
    }
}

fn provenance_manifest(root: &Path, failures: &mut Vec<String>) -> Option<ProvenanceManifest> {
    let text = read_to_string(root, Path::new(PROVENANCE_MANIFEST), failures);
    match serde_json::from_str(&text) {
        Ok(manifest) => Some(manifest),
        Err(error) => {
            failures.push(format!("invalid provenance manifest: {error}"));
            None
        }
    }
}

fn provenance_report_expectations(manifest: &ProvenanceManifest) -> Vec<String> {
    vec![
        format!("Evidence contract: `{}`", manifest.contract),
        format!("Snapshot date: `{}`", manifest.snapshot_date),
        "Manifest route: `/reports/rc1-provenance-manifest.json`".to_string(),
        format!(
            "Evidence commit: `faber {}`",
            manifest.frozen_at.faber.commit
        ),
        format!("`{}`", manifest.frozen_at.faber.subject),
        "Website sync commit:".to_string(),
        format!(
            "`faberlang.dev {}`",
            manifest.frozen_at.faberlang_dev.commit
        ),
        format!("`{}`", manifest.frozen_at.faberlang_dev.subject),
        format!("Compiler provenance: `{}`", manifest.provenance.compiler),
        format!("Faber provenance: `{}`", manifest.provenance.faber),
        manifest.local_binary.build_command.clone(),
        manifest.local_binary.version_result.clone(),
        manifest.local_binary.path.clone(),
        manifest.local_binary.sha256.clone(),
        manifest.local_binary.size_observed.clone(),
        format!(
            "faber-runtime {}",
            manifest.autograd_proximity.faber_runtime
        ),
        format!("examples {}", manifest.autograd_proximity.examples),
        manifest.autograd_proximity.fixture_scope.clone(),
        format!(
            "Output-checked device/autograd floor: {}",
            manifest
                .autograd_proximity
                .output_checked_device_autograd_floor
        ),
        manifest.autograd_proximity.boundary_statement.clone(),
    ]
}

fn is_iso_date(value: &str) -> bool {
    let bytes = value.as_bytes();
    bytes.len() == 10
        && bytes[4] == b'-'
        && bytes[7] == b'-'
        && bytes
            .iter()
            .enumerate()
            .all(|(index, byte)| matches!(index, 4 | 7) || byte.is_ascii_digit())
}

fn is_git_commit_hex(value: &str) -> bool {
    value.len() == 40 && value.chars().all(|ch| ch.is_ascii_hexdigit())
}

fn uses_current_local_evidence_wording(text: &str) -> bool {
    text.contains("Current local evidence") || text.contains("current local tree")
}

fn verify_autograd_boundary(root: &Path, failures: &mut Vec<String>) {
    for (file, label) in [
        (
            "assets/reports/rc1-private-preview-checklist.md",
            "private-preview autograd boundary",
        ),
        (
            "assets/reports/stage-1-leakage-check.md",
            "leakage autograd boundary",
        ),
    ] {
        let text = read_to_string(root, Path::new(file), failures);
        for expected in [
            "faber-runtime 4f8d452",
            "examples 310cef1",
            "rung3 oracle fixtures",
            "no generated-autograd claim",
            "Output-checked device/autograd floor: 0",
        ] {
            if !text.contains(expected) {
                failures.push(format!("{label} missing `{expected}`"));
            }
        }
    }
}

fn verify_json(root: &Path, failures: &mut Vec<String>) {
    let mut files = Vec::new();
    collect_json_assets(&root.join("assets"), &mut files);

    for file in files {
        let text = read_to_string(root, &file, failures);
        if let Err(error) = serde_json::from_str::<serde_json::Value>(&text) {
            failures.push(format!("invalid JSON in {}: {error}", file.display()));
        }
    }
}

fn route_to_asset_path(route: &str) -> PathBuf {
    let route = route
        .strip_prefix("__PUBLIC_ORIGIN__")
        .unwrap_or(route)
        .trim_start_matches('/')
        .replace("__DOCS_VERSION__", DOCS_VERSION);
    PathBuf::from("assets").join(route)
}

fn collect_text_assets(dir: &Path, files: &mut Vec<PathBuf>) {
    let Ok(entries) = fs::read_dir(dir) else {
        return;
    };
    for entry in entries.flatten() {
        let path = entry.path();
        if path.is_dir() {
            collect_text_assets(&path, files);
        } else if is_text_asset(&path) {
            files.push(path);
        }
    }
}

fn collect_json_assets(dir: &Path, files: &mut Vec<PathBuf>) {
    let Ok(entries) = fs::read_dir(dir) else {
        return;
    };
    for entry in entries.flatten() {
        let path = entry.path();
        if path.is_dir() {
            collect_json_assets(&path, files);
        } else if path
            .extension()
            .is_some_and(|extension| extension == "json")
        {
            files.push(path);
        }
    }
}

fn collect_asset_files(dir: &Path, files: &mut Vec<PathBuf>) {
    let Ok(entries) = fs::read_dir(dir) else {
        return;
    };
    for entry in entries.flatten() {
        let path = entry.path();
        if path.is_dir() {
            collect_asset_files(&path, files);
        } else {
            files.push(path);
        }
    }
}

fn is_text_asset(path: &Path) -> bool {
    path.extension().is_some_and(|extension| {
        matches!(
            extension.to_str(),
            Some("html" | "css" | "md" | "txt" | "json" | "xml" | "ebnf")
        )
    })
}

fn read_to_string(root: &Path, path: &Path, failures: &mut Vec<String>) -> String {
    let absolute = if path.is_absolute() {
        path.to_path_buf()
    } else {
        root.join(path)
    };

    match fs::read_to_string(&absolute) {
        Ok(text) => text,
        Err(error) => {
            failures.push(format!("failed to read {}: {error}", path.display()));
            String::new()
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn known_routes() -> Vec<String> {
        vec![
            "/".to_string(),
            "/contracts/1.0.0-rc.1/documents.json".to_string(),
            "/contracts/1.0.0-rc.1/grammar.ebnf".to_string(),
            "/docs/1.0.0-rc.1/reference/index.md".to_string(),
        ]
    }

    #[test]
    fn route_reference_resolves_concrete_version_placeholders() {
        assert!(route_reference_resolves(
            "/contracts/__DOCS_VERSION__/documents.json",
            &known_routes()
        ));
    }

    #[test]
    fn route_reference_rejects_wildcard_prefixes() {
        assert!(!route_reference_resolves(
            "/contracts/__DOCS_VERSION__/*",
            &known_routes()
        ));
    }

    #[test]
    fn route_reference_rejects_public_origin_wildcards() {
        assert!(!route_reference_resolves(
            "__PUBLIC_ORIGIN__/contracts/__DOCS_VERSION__/*",
            &known_routes()
        ));
    }

    #[test]
    fn frozen_provenance_contract_rejects_current_local_wording() {
        assert!(uses_current_local_evidence_wording(
            "Current local evidence: commit abc"
        ));
        assert!(uses_current_local_evidence_wording(
            "This evidence supports private review of the current local tree only."
        ));
        assert!(!uses_current_local_evidence_wording(
            "Frozen private-preview evidence snapshot:"
        ));
    }

    #[test]
    fn provenance_manifest_date_and_commit_shapes_are_strict() {
        assert!(is_iso_date("2026-07-14"));
        assert!(!is_iso_date("2026-7-14"));
        assert!(is_git_commit_hex(
            "1a7001fe4bb26b0f20361e12aa4df8f4dcd604d1"
        ));
        assert!(!is_git_commit_hex(
            "1a7001fe4bb26b0f20361e12aa4df8f4dcd604d1x"
        ));
    }

    #[test]
    fn empty_provider_route_gate_matches_claim_phrases() {
        assert!(contains_normalized_phrase(
            "Select provider capabilities by their documented route name.",
            "select provider capabilities"
        ));
        assert!(contains_normalized_phrase(
            "Generated native packages link only the providers selected by analysis.",
            "generated native packages link only"
        ));
        assert!(!contains_normalized_phrase(
            "Do not claim provider capability selection from this packet.",
            "select provider capabilities"
        ));
    }

    #[test]
    fn empty_provider_route_gate_rejects_language_doc_false_pass() {
        let phrases = empty_provider_route_claim_phrases(
            "Declarative effects use the `ad` keyword and route to host providers:",
        );
        assert!(phrases.contains(&"route to host providers"));

        let phrases = empty_provider_route_claim_phrases(
            "Effects are declared via the `ad` keyword and route to host providers.",
        );
        assert!(
            phrases
                .contains(&"effects are declared via the ad keyword and route to host providers"),
            "phrases: {phrases:?}"
        );
    }

    #[test]
    fn empty_provider_route_gate_allows_source_shape_language() {
        assert!(empty_provider_route_claim_phrases(
            "Effects are declared via the `ad` keyword as source-shape declarations."
        )
        .is_empty());
        assert!(empty_provider_route_claim_phrases(
            "Do not infer provider routing from `ad` syntax; provider route entries are not published in this packet."
        )
        .is_empty());
    }

    #[test]
    fn provider_contract_empty_routes_detects_missing_route_coverage() {
        let text = r#"{
            "providers": {
                "aleator": { "routes": [] },
                "consolum": { "routes": ["console.write"] }
            }
        }"#;
        let value = serde_json::from_str::<serde_json::Value>(text).unwrap();
        let providers = value
            .get("providers")
            .and_then(|providers| providers.as_object())
            .unwrap();
        assert!(providers.values().any(|metadata| metadata
            .get("routes")
            .and_then(|routes| routes.as_array())
            .is_none_or(|routes| routes.is_empty())));
    }

    #[test]
    fn denied_claim_matching_normalizes_case_and_separators() {
        let text = normalize_claim_text("Faber has GENERATED-AUTOGRAD support.");
        assert!(contains_denied_public_claim(&text, "generated autograd"));

        let text = normalize_claim_text("Faber is a production-ready language.");
        assert!(contains_denied_public_claim(
            &text,
            "production ready language"
        ));
    }

    #[test]
    fn denied_claim_matching_covers_representative_hard_gates() {
        for (text, claim) in [
            (
                "The compiler has PyTorch-equivalence today.",
                "pytorch equivalence",
            ),
            (
                "The compiler has PyTorch equivalent behavior today.",
                "pytorch equivalent",
            ),
            ("PyTorch sessions are supported today.", "pytorch session"),
            (
                "Faber ships an inference runtime for models.",
                "inference runtime",
            ),
            ("llama.cpp support is ready.", "llama.cpp"),
            ("GGUF models load out of the box.", "gguf"),
            ("Model loading is built in.", "model loading"),
            ("GPU execution is supported.", "gpu execution"),
            ("The rendering claim is public evidence.", "rendering claim"),
            ("Browser execution is supported.", "browser execution"),
            ("Triga mirrors three.js with shipped rendering.", "three js"),
            ("Faber is a public release today.", "public release"),
            ("This page is an install guide.", "install guide"),
            ("Download the released binary.", "released binary"),
            ("Public source export is complete.", "public source export"),
            ("The public deployed site is ready.", "deployed site"),
            ("Public deployment is approved.", "public deployment"),
            ("The live site is ready for launch.", "live site"),
            ("The package registry is live.", "registry is live"),
            (
                "Install with one command using Homebrew or cURL.",
                "homebrew",
            ),
            ("Install with one command using cURL.", "curl"),
            ("Users can build-from-source today.", "build from source"),
        ] {
            assert!(
                contains_denied_public_claim(&normalize_claim_text(text), claim),
                "{text:?} should trip {claim:?}"
            );
        }
    }

    #[test]
    fn denied_claim_matching_rejects_unrelated_nearby_gating() {
        let text = "Install with one command is ready for everyone. Public source remains gated.";
        assert!(contains_denied_public_claim(
            text,
            "Install with one command"
        ));

        let text = "Faber is a public release. Install route approval remains gated.";
        assert!(contains_denied_public_claim(text, "public release"));
    }

    #[test]
    fn denied_claim_matching_allows_explicit_boundary_language() {
        let boundary = "Do not claim generated-autograd, PyTorch-session, \
             PyTorch-equivalence, inference runtime, llama cpp, GGUF, model loading, \
             GPU execution, rendering, source export, public deploy, install route, \
             or live registry from this evidence.";

        for claim in [
            "generated autograd",
            "pytorch session",
            "pytorch equivalence",
            "inference runtime",
            "llama.cpp",
            "gguf",
            "model loading",
            "gpu execution",
            "rendering claim",
            "source export",
            "public deploy",
            "live registry",
        ] {
            assert!(
                !contains_denied_public_claim(boundary, claim),
                "boundary text should not trip {claim:?}"
            );
        }
    }

    #[test]
    fn denied_claim_matching_allows_private_preview_non_claims() {
        for (text, claim) in [
            (
                "This is not a public release announcement.",
                "public release",
            ),
            (
                "Do not publish this as an install guide until a binary or approved install route exists.",
                "install guide",
            ),
            (
                "No released binary is attached to this local packet.",
                "released binary",
            ),
            (
                "This packet makes no PyTorch equivalent claim.",
                "pytorch equivalent",
            ),
        ] {
            assert!(
                !contains_denied_public_claim(text, claim),
                "boundary text should not trip {claim:?}: {text:?}"
            );
        }
    }

    #[test]
    fn removed_contract_archive_markers_cover_versioned_and_placeholder_claims() {
        for claim in [
            "faber-contract.tar.zst",
            "/contracts/<version>/faber-contract.tar.zst",
            "/contracts/__DOCS_VERSION__/faber-contract.tar.zst",
            "/contracts/1.0.0-rc.1/faber-contract.tar.zst",
        ] {
            assert!(
                REMOVED_CONTRACT_ARCHIVE_MARKERS.contains(&claim),
                "missing removed archive marker {claim:?}"
            );
        }
    }
}
