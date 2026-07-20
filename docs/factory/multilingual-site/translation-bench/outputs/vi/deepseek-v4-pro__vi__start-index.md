Năm phút để nắm hình dạng của Faber: cài CLI, đọc một hàm, rồi mở một gói thực.
Để theo lộ trình tuần tự, hãy đi theo: [Cài đặt](/start/install.html) →
[Xin chào](/start/hello.html) → [Lệnh](/start/commands.html) →
[Dự án](/start/projects.html).

## 1. Cài đặt CLI {#install}

Tải bản phát hành hiện tại (**1.1.1**) cho nền tảng của bạn từ
[trang cài đặt](/start/install.html), kiểm tra checksum của kho lưu trữ, và đặt
tệp nhị phân `faber-v1.1.1-<target-triple>/faber` đã giải nén vào `PATH` của bạn.
Xác nhận:

<<<FENCE 0>>>

## 2. Hình dạng của một hàm {#shape}

Tham số kiểu-trước, kiểu trả về dạng ký hiệu, từ điều khiển Latin, union nullable:

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

Các lệnh thông dụng:

<<<FENCE 3>>>

Chi tiết: [Công cụ build Faber](/tooling/faber-build-tool.html).

## 4. Ứng dụng thực tế {#applications}

Đừng dừng lại ở hello-world. Repo **examples** công khai có CLI đa lệnh,
mailspace cục bộ, track tác vụ GPU, và toàn bộ corpus ngôn ngữ.

| Gói | Nội dung thể hiện |
|---|---|
| AI Workbench | CLI đa lệnh, kiểm tra model, embeddings |
| ViviLite | Mailspace lưu tệp / CLI điều phối agent |
| coreutils | Chiến dịch ứng dụng lớn hơn (parity harnesses) |
| gpu-workload | Hệ thống / bậc GPU |
| corpus | Một thư mục cho mỗi cấu trúc ngôn ngữ |

Duyệt chúng trên [trang examples](/start/examples.html).

## 5. Nếu bạn là một agent {#agents}

1. Đọc [`/llms.txt`](/llms.txt).
2. Mở [`/agents/index.md`](/agents/index.md).
3. Chọn một kỹ năng từ [`/.well-known/agent-skills/index.json`](/.well-known/agent-skills/index.json).

## Lộ trình bắt đầu {#start-track}

| Bước | Trang | Kết quả |
|---|---|---|
| 1 | [Cài đặt & tải về](/start/install.html) | Đặt Faber 1.1.1 vào `PATH` và xác nhận |
| 2 | [Xin chào, Faber](/start/hello.html) | Tạo và chạy `salve-munde` |
| 3 | [Các lệnh bạn sẽ dùng](/start/commands.html) | Học `check`, `build`, `run`, `test`, `explain` |
| 4 | [Dự án và ví dụ](/start/projects.html) | Chuyển sang các gói thực và trang corpus |

## Tiếp theo {#next}

| Chủ đề | Liên kết |
|---|---|
| Cài đặt & tải về | [Cài đặt](/start/install.html) |
| Xin chào, Faber | [Xin chào](/start/hello.html) |
| Lệnh | [Lệnh](/start/commands.html) |
| Dự án | [Dự án](/start/projects.html) |
| Tham khảo cú pháp | [Cú pháp](/syntax/) |
| Tính năng (locales, lanes) | [Tính năng](/features/) |
| Thư viện hệ sinh thái | [Hệ sinh thái](/ecosystem/) |
| Corpus từ khóa | [Corpus](/corpus/) |
