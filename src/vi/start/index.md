+++
translation_kind = "translated"

title = "Quick tour"
section = "start"
order = 0
sources = []

prose_hash = "sha256:fb6f791ae0e9b73d0c92c2127726f558a2b845351779f80217616b8f55629ff0"
code_hash = "sha256:f9eb22ab8a2408fe0076d846dd4266cff4ded675ad8d63a5b2d9ee59c3e0156f"
source_commit = "6572815c8c5595e60956471d75c4a60e67cba58f"
source_locale = "en-US"
+++
Năm phút để nắm hình dạng của Faber: cài đặt CLI, đọc một hàm,
sau đó mở một gói thực tế. Để đi theo lộ trình tuần tự, hãy xem: [Cài đặt](/start/install.html) →
[Hello](/start/hello.html) → [Các lệnh](/start/commands.html) →
[Dự án](/start/projects.html).

## 1. Cài đặt CLI {#install}

Tải bản phát hành hiện tại (**1.1.1**) cho nền tảng của bạn từ
[trang cài đặt](/start/install.html), xác minh checksum của tệp lưu trữ,
sau đó đặt tệp nhị phân `faber-v1.1.1-<target-triple>/faber` đã giải nén vào
`PATH` của bạn. Xác nhận:

```bash
faber --version
```

## 2. Hình dạng của một hàm {#shape}

Tham số ưu tiên kiểu, kiểu trả về bằng glyph, từ điều khiển Latin, hợp
kiểu có thể là null:

```text
functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ∴ redde nihil
    redde a / b
}
```

| Tín hiệu | Ý nghĩa |
|---|---|
| `functio` | Khai báo hàm |
| `numerus a` | Kiểu trước, tên sau |
| `→` | Kiểu trả về |
| `∪ nihil` | Có thể là null (`T ∪ nihil`) |
| `si … ∴` | Nhánh rút gọn |
| `redde` | Trả về |

## 3. Bố cục gói {#package}

Một gói là một thư mục có `faber.toml` và `src/`:

```text
my-app/
  faber.toml
  src/
    main.fab
```

Các lệnh thường dùng:

```bash
faber check my-app/
faber build my-app/ -t rust
faber run my-app/
faber test my-app/
```

Chi tiết: [Công cụ build Faber](/tooling/faber-build-tool.html).

## 4. Ứng dụng thực tế {#applications}

Đừng dừng lại ở hello-world. Kho **examples** công khai có các CLI nhiều
lệnh, một mailspace cục bộ, các nhánh workload GPU và một corpus ngôn ngữ
đầy đủ.

| Gói | Nội dung minh họa |
|---|---|
| AI Workbench | CLI nhiều lệnh, kiểm tra model, embeddings |
| ViviLite | CLI mailspace / điều phối agent dựa trên tệp |
| coreutils | Chiến dịch ứng dụng lớn hơn (các parity harness) |
| gpu-workload | Các nấc hệ thống / GPU |
| corpus | Mỗi cấu trúc ngôn ngữ một thư mục |

Xem chúng trên [trang examples](/start/examples.html).

## 5. Nếu bạn là agent {#agents}

1. Đọc [`/llms.txt`](/llms.txt).
2. Mở [`/agents/index.md`](/agents/index.md).
3. Chọn một skill từ [`/.well-known/agent-skills/index.json`](/.well-known/agent-skills/index.json).

## Lộ trình bắt đầu {#start-track}

| Bước | Trang | Kết quả |
|---|---|---|
| 1 | [Cài đặt & tải xuống](/start/install.html) | Đặt Faber 1.1.1 vào `PATH` và xác minh |
| 2 | [Hello, Faber](/start/hello.html) | Tạo và chạy `salve-munde` |
| 3 | [Các lệnh bạn sẽ dùng](/start/commands.html) | Tìm hiểu `check`, `build`, `run`, `test`, `explain` |
| 4 | [Dự án và examples](/start/projects.html) | Chuyển sang các gói thực tế và các trang corpus |

## Tiếp theo {#next}

| Chủ đề | Liên kết |
|---|---|
| Cài đặt & tải xuống | [Cài đặt](/start/install.html) |
| Hello, Faber | [Hello](/start/hello.html) |
| Các lệnh | [Các lệnh](/start/commands.html) |
| Dự án | [Dự án](/start/projects.html) |
| Tham chiếu cú pháp | [Cú pháp](/syntax/) |
| Tính năng (locale, lane) | [Tính năng](/features/) |
| Thư viện hệ sinh thái | [Hệ sinh thái](/ecosystem/) |
| Corpus từ khóa | [Corpus](/corpus/) |
