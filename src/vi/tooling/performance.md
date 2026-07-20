+++
translation_kind = "translated"

title = "Compiler performance"
section = "tooling"
order = 2
sources = [
  "radix/README.md (Compiler Performance section)",
]


prose_hash = "sha256:6202471aeac8f93c0bfc712bbd7449a4303b3bd8da122bb7a91de4af66c343d2"
code_hash = "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
Frontend của Radix tăng gần như tuyến tính theo kích thước mã nguồn, trong cùng một tiến trình và trên một luồng.

## Thời gian biên dịch frontend {#frontend-compile-times}

| Kích thước chương trình | Mã nguồn | Thời gian biên dịch trung vị |
|-------------|--------|---------------|
| 100 hàm / ~650 dòng | ~10 KB | ~0,6 ms |
| 500 hàm / ~3,3K dòng | ~52 KB | ~3 ms |
| 1.000 hàm / ~6,5K dòng | ~105 KB | ~6 ms |
| 5.000 hàm / ~32K dòng | ~530 KB | ~37 ms |

Ví dụ thực tế lớn nhất hiện nay chỉ khoảng 140 dòng, thấp hơn nhiều so với ngưỡng nhiễu.

## Chi phí backend (đích Rust) {#backend-costs-rust-target}

Khi chạy `faber build`, thời gian người dùng cảm nhận chủ yếu do Cargo/rustc chi phối, không phải frontend của Faber:

| Giai đoạn | Chi phí |
|-------|------|
| Biên dịch dependency `faber` lần đầu (một lần cho mỗi thư mục đích) | ~2,8 s |
| Biên dịch dependency `tokio` lần đầu (chỉ khi cần) | ~2,3 s |
| Build từng chương trình khi đã làm nóng bộ nhớ đệm | ~30–110 ms |
| Chi phí gọi Cargo cho từng chương trình | ~400 ms |

## Biên dịch gia tăng {#incremental-compilation}

Crate `faber-runtime` được biên dịch một lần cho mỗi thư mục đích và được lưu trong bộ nhớ đệm dưới dạng các artifact `.rlib`:

| Thành phần bạn thay đổi | Crate faber-runtime | Chương trình của bạn |
|-----------|-------------------|-------------|
| Mã nguồn chương trình của bạn | đã lưu trong bộ nhớ đệm | biên dịch lại |
| `norma/src/*.fab` (mã nguồn Faber) | đã lưu trong bộ nhớ đệm | biên dịch lại |
| `faber-runtime/src/*.rs` | biên dịch lại một lần | biên dịch lại |

Điều cần tránh là build từng chương trình vào một `target/` mới. Hãy dùng lại một `--target-dir` dùng chung để giữ các `.rlib` đã lưu trong bộ nhớ đệm luôn ở trạng thái sẵn sàng.
