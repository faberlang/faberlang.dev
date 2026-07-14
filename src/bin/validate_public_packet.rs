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
];

const LOCAL_STATUS_FILES: &[&str] = &[
    "assets/index.html",
    "assets/llms.txt",
    "assets/docs/1.0.0-rc.1/evaluate/index.md",
    "assets/reports/stage-1-leakage-check.md",
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
    verify_local_binary_evidence(&root, &mut failures);
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

fn verify_local_binary_evidence(root: &Path, failures: &mut Vec<String>) {
    let report = read_to_string(
        root,
        Path::new("assets/reports/stage-1-leakage-check.md"),
        failures,
    );
    for expected in [
        "cd24854",
        "cargo build --release --bin faber",
        "faber 1.0.0-rc.1",
        "1e2efc7a85c192aa857dccc4b392b0298d5bc9232593bfbb183bb7b9092c1ee7",
        "pushed tag",
        "deployment",
    ] {
        if !report.contains(expected) {
            failures.push(format!("local binary evidence missing `{expected}`"));
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
