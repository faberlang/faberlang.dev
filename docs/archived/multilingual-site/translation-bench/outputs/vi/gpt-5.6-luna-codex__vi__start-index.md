Năm phút để nắm hình hài của Faber: cài đặt CLI, đọc một hàm,
rồi mở một gói thực tế. Để đi theo trình tự, hãy theo dõi: [Cài đặt](/start/install.html) →
[Hello](/start/hello.html) → [Các lệnh](/start/commands.html) →
[Dự án](/start/projects.html).

## 1. Cài đặt CLI {#install}

Tải bản phát hành hiện tại (**1.1.1**) cho nền tảng của bạn từ
[trang cài đặt](/start/install.html), xác minh checksum của tệp lưu trữ, rồi đặt tệp nhị phân
`faber-v1.1.1-<target-triple>/faber` đã giải nén vào `PATH`. Xác nhận:

<<<FENCE 0>>>

## 2. Hình hài của một hàm {#shape}

Tham số đặt kiểu trước, kiểu trả về bằng glyph, từ điều khiển Latin,
kiểu hợp nullable:

<<<FENCE 1>>>

| Tín hiệu | Ý nghĩa |
|---|---|
| `functio` | Khai báo hàm |
| `numerus a` | Kiểu trước, rồi đến tên |
| `→` | Kiểu trả về |
| `∪ nihil` | Nullable (`T ∪ nihil`) |
| `si … ∴` | Nhánh rút gọn |
| `redde` | Trả về |

## 3. Bố cục gói {#package}

Một gói là một thư mục chứa `faber.toml` và `src/`:

<<<FENCE 2>>>

Các lệnh điển hình:

<<<FENCE 3>>>

Chi tiết: [công cụ build Faber](/tooling/faber-build-tool.html).

## 4. Ứng dụng thực tế {#applications}

Đừng dừng lại ở hello-world. Kho **examples** công khai có các CLI nhiều lệnh,
mailspace cục bộ, các track workload GPU và một corpus ngôn ngữ đầy đủ.

| Gói | Nội dung minh họa |
|---|---|
| AI Workbench | CLI nhiều lệnh, kiểm tra model, embeddings |
| ViviLite | CLI điều phối agent / mailspace dựa trên tệp |
| coreutils | Chiến dịch ứng dụng lớn hơn (harness kiểm tra tương đương) |
| gpu-workload | Các nấc hệ thống / GPU |
| corpus | Mỗi cấu trúc ngôn ngữ một thư mục |

Duyệt chúng trên [trang examples](/start/examples.html).

## 5. Nếu bạn là một agent {#agents}

1. Đọc [`/llms.txt`](/llms.txt).
2. Mở [`/agents/index.md`](/agents/index.md).
3. Chọn một kỹ năng từ [`/.well-known/agent-skills/index.json`](/.well-known/agent-skills/index.json).

## Lộ trình bắt đầu {#start-track}

| Bước | Trang | Kết quả |
|---|---|---|
| 1 | [Cài đặt & tải xuống](/start/install.html) | Đặt Faber 1.1.1 vào `PATH` và xác minh |
| 2 | [Hello, Faber](/start/hello.html) | Tạo và chạy `salve-munde` |
| 3 | [Các lệnh bạn sẽ dùng](/start/commands.html) | Tìm hiểu `check`, `build`, `run`, `test`, `explain` |
| 4 | [Dự án và ví dụ](/start/projects.html) | Chuyển sang các gói thực tế và các trang corpus |

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
