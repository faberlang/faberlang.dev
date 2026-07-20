Năm phút để nắm được hình dáng của Faber: cài đặt CLI, đọc một hàm,
rồi mở một gói thực tế. Để theo một lộ trình có thứ tự, hãy xem: [Cài đặt](/start/install.html) →
[Hello](/start/hello.html) → [Lệnh](/start/commands.html) →
[Dự án](/start/projects.html).

## 1. Cài đặt CLI {#install}

Tải bản phát hành hiện tại (**1.1.1**) cho nền tảng của bạn từ
[trang cài đặt](/start/install.html), kiểm tra checksum của kho nén, và đặt
file nhị phân `faber-v1.1.1-<target-triple>/faber` đã giải nén lên `PATH` của bạn. Xác nhận:

<<<FENCE 0>>>

## 2. Hình dáng của một hàm {#shape}

Tham số đặt kiểu trước, kiểu trả về dùng glyph, từ điều khiển Latin, union nullable:

<<<FENCE 1>>>

| Tín hiệu | Ý nghĩa |
|---|---|
| `functio` | Khai báo hàm |
| `numerus a` | Kiểu trước, rồi đến tên |
| `→` | Kiểu trả về |
| `∪ nihil` | Nullable (`T ∪ nihil`) |
| `si … ∴` | Nhánh gọn |
| `redde` | Trả về |

## 3. Bố cục gói {#package}

Một gói là một thư mục chứa `faber.toml` và `src/`:

<<<FENCE 2>>>

Các lệnh phổ biến:

<<<FENCE 3>>>

Chi tiết: [Công cụ build Faber](/tooling/faber-build-tool.html).

## 4. Ứng dụng thực tế {#applications}

Đừng dừng lại ở hello-world. Kho **examples** công khai có các CLI đa lệnh,
một mailspace cục bộ, các track khối lượng công việc GPU, và một kho ngữ liệu ngôn ngữ đầy đủ.

| Gói | Nội dung thể hiện |
|---|---|
| AI Workbench | CLI đa lệnh, kiểm tra mô hình, embeddings |
| ViviLite | Mailspace dựa trên file / CLI điều phối agent |
| coreutils | Chiến dịch ứng dụng lớn hơn (các bộ so khớp parity) |
| gpu-workload | Các rung hệ thống / GPU |
| corpus | Một thư mục cho mỗi cấu trúc ngôn ngữ |

Duyệt chúng tại [trang examples](/start/examples.html).

## 5. Nếu bạn là một agent {#agents}

1. Đọc [`/llms.txt`](/llms.txt).
2. Mở [`/agents/index.md`](/agents/index.md).
3. Chọn một kỹ năng từ [`/.well-known/agent-skills/index.json`](/.well-known/agent-skills/index.json).

## Track khởi đầu {#start-track}

| Bước | Trang | Kết quả |
|---|---|---|
| 1 | [Cài đặt & tải](/start/install.html) | Đặt Faber 1.1.1 lên `PATH` và xác minh nó |
| 2 | [Hello, Faber](/start/hello.html) | Tạo và chạy `salve-munde` |
| 3 | [Các lệnh bạn sẽ dùng](/start/commands.html) | Học `check`, `build`, `run`, `test`, `explain` |
| 4 | [Dự án và ví dụ](/start/projects.html) | Chuyển vào các gói thực tế và trang corpus |

## Tiếp theo {#next}

| Chủ đề | Liên kết |
|---|---|
| Cài đặt & tải | [Cài đặt](/start/install.html) |
| Hello, Faber | [Hello](/start/hello.html) |
| Lệnh | [Lệnh](/start/commands.html) |
| Dự án | [Dự án](/start/projects.html) |
| Tham chiếu cú pháp | [Cú pháp](/syntax/) |
| Tính năng (locale, lane) | [Tính năng](/features/) |
| Thư viện hệ sinh thái | [Hệ sinh thái](/ecosystem/) |
| Kho từ khóa | [Corpus](/corpus/) |
