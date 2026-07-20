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
