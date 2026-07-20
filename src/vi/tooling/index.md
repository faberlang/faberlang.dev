+++
translation_kind = "translated"

title = "Tooling and compiler"
section = "tooling"
order = 0
sources = []


prose_hash = "sha256:23ae82d266e39d96b2059d2b97d4b03c5e6efcba389ab0bfb621d32a2e7caad2"
code_hash = "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
Chuỗi công cụ Faber bao gồm ba công cụ: CLI `faber` để xây dựng và
kiểm thử, trình biên dịch Radix để sinh mã, và trình quản lý gói Cista để
phân giải các phần phụ thuộc.

## Công cụ xây dựng Faber {#faber-cli}

Giao diện chính dành cho nhà phát triển. Xây dựng, kiểm tra, chạy, kiểm thử,
định dạng và giải thích — tất cả thông qua một lệnh duy nhất. [Đọc thêm →](/tooling/faber-build-tool.html)

## Trình biên dịch Radix {#radix}

Backend của trình biên dịch. Hạ mã nguồn Faber qua HIR → MIR → AIR đến nhiều
luồng đích. [Đọc thêm →](/tooling/radix-compiler.html)

## Trình quản lý gói Cista {#cista}

Phân giải gói và kho gói công khai. Quản lý các tệp kê khai `faber.toml` và
các khóa phụ thuộc. [Đọc thêm →](/tooling/cista-package-manager.html)

## Các đích sinh mã {#codegen-targets}

Faber biên dịch sang Rust (mặc định), WASM, TypeScript, Go và GPU/WGSL.
Mỗi luồng đích có đường dẫn IR và liên kết runtime riêng.
[Đọc thêm →](/tooling/codegen-targets.html)

## Hiệu năng {#performance}

Hiệu năng biên dịch và thực thi được đo trên nhiều luồng đích.
[Đọc thêm →](/tooling/performance.html)

## Lập trình tập lệnh {#scripting}

Sử dụng Faber như một ngôn ngữ lập trình tập lệnh với lệnh `faber run`.
[Đọc thêm →](/tooling/scripting.html)
