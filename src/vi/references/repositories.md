+++
translation_kind = "translated"

title = "Repositories"
section = "references"
order = 3
sources = [
  "github.com/faberlang",
]


prose_hash = "sha256:1f00ec1ce77844348776b258be2b9246bf876b614a2849a0e8dcbb54a8dc82f0"
code_hash = "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
source_commit = "593544bb65cdafba45a3a2c63b8c66148d65a4b3"
source_locale = "en-US"
+++
Faber được phát triển trên nhiều kho lưu trữ thuộc tổ chức `faberlang`.

## Kho lưu trữ công khai {#public-repositories}

| Kho lưu trữ | Mô tả |
|-----------|-------------|
| `faber` | CLI hướng đến người dùng: kiểm tra, xây dựng, chạy, kiểm thử, định dạng, giải thích |
| `faber-runtime` | Các kiểu runtime cốt lõi (Valor, tensor, frame); tên crate là `faber` |
| `norma` | Mã nguồn thư viện chuẩn (các mô-đun `norma:*`) |
| `triga` | Thư viện đồ họa/hình học tùy chọn |
| `cista` | Trình quản lý gói và kho lưu trữ (đang thử nghiệm) |
| `examples` | Kho ngữ liệu ngôn ngữ, coreutils, AI Workbench, các gói ngôn ngữ đọc |
| `faberlang.dev` | Trang web này |

## Kho lưu trữ riêng tư {#private-repositories}

| Kho lưu trữ | Mô tả |
|-----------|-------------|
| `radix` | Trình biên dịch: phân tích từ vựng, phân tích cú pháp, phân tích ngữ nghĩa, HIR/MIR/AIR, chẩn đoán, sinh mã |

## Kho lưu trữ nền tảng máy chủ {#host-platform-repositories}

| Kho lưu trữ | Mô tả |
|-----------|-------------|
| `host-kernel-rs` | Bộ định tuyến mỏng: Frame, Conversation, điều phối theo tiền tố, lỗi có cấu trúc |
| `host-native-rs` | Kết nối native: worker, hook `register_providers` |
| `host-providers-rs` | Các triển khai provider: solum, processus, consolum, tempus, aleator, http |
