use std::fs;
use std::path::{Path, PathBuf};

const DOCS_VERSION: &str = "1.0.0-rc.1";

const REQUIRED_ROUTES: &[&str] = &[
    "/docs/__DOCS_VERSION__/evaluate/index.md",
    "/docs/__DOCS_VERSION__/learn/index.md",
    "/docs/__DOCS_VERSION__/reference/index.md",
    "/docs/__DOCS_VERSION__/targets/index.md",
    "/docs/__DOCS_VERSION__/examples/index.md",
    "/reports/stage-1-leakage-check.md",
    "/reports/rc1-private-preview-checklist.md",
];

const LOCAL_STATUS_FILES: &[&str] = &[
    "assets/index.html",
    "assets/llms.txt",
    "assets/docs/1.0.0-rc.1/evaluate/index.md",
    "assets/reports/stage-1-leakage-check.md",
    "assets/reports/rc1-private-preview-checklist.md",
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

const FORBIDDEN_PUBLIC_CLAIMS: &[&str] = &[
    "Install with one command",
    "Build from source",
    "Homebrew",
    "curl",
    "binary download",
    "open source",
    "public repo",
    "public repository",
    "Package registry live",
    "cista.dev is live",
    "publish your package",
    "published manifest",
    "published manifests",
    "published diagnostic",
    "Only those published",
    "authoritative syntax reference",
    "authoritative grammar",
    "Go is supported",
    "Full coreutils",
    "multi-backend coreutils",
    "production ready",
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
    verify_internal_route_references(&root, &mut failures);
    verify_local_binary_evidence(&root, &mut failures);
    verify_private_preview_checklist(&root, &mut failures);
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
        for claim in FORBIDDEN_PUBLIC_CLAIMS {
            if text.contains(claim) {
                failures.push(format!(
                    "forbidden public claim `{claim}` in {}",
                    file.display()
                ));
            }
        }
    }
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

    if let Some(prefix) = route.strip_suffix("/*") {
        return known_routes
            .iter()
            .any(|known_route| known_route.starts_with(prefix));
    }

    known_routes.iter().any(|known_route| known_route == &route)
}

fn verify_local_binary_evidence(root: &Path, failures: &mut Vec<String>) {
    let report = read_to_string(
        root,
        Path::new("assets/reports/stage-1-leakage-check.md"),
        failures,
    );
    for expected in [
        "Evidence commit: `1a7001f`",
        "Compiler provenance: `82d6230ec`",
        "Faber provenance: `edbb54f496e5`",
        "cargo build --release --bin faber",
        "faber 1.0.0-rc.1",
        "77203c7302eb025bbf3ddd01aae798a96f0ca97cc0219066a6a64a991405700b",
        "public release artifact checksum",
        "pushed tag",
        "deployment",
    ] {
        if !report.contains(expected) {
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
    for expected in [
        "private-preview checklist",
        "not public launch approval",
        "Evidence commit: `1a7001f`",
        "Compiler provenance: `82d6230ec`",
        "Faber provenance: `edbb54f496e5`",
        "faber 1.0.0-rc.1",
        "77203c7302eb025bbf3ddd01aae798a96f0ca97cc0219066a6a64a991405700b",
        "not create a public artifact",
        "Required Before Public Use",
    ] {
        if !checklist.contains(expected) {
            failures.push(format!("private-preview checklist missing `{expected}`"));
        }
    }
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
