+++
translation_kind = "translated"

title = "History"
section = "history"
order = 0
sources = []


prose_hash = "sha256:99390038c112db9d79c728a21f5bc2c804af48f6de648df7e6ff6f2f0bc32a99"
code_hash = "sha256:8cfe9c845ef9a1247454bc890937eafa78a38164428679c7a6981c3c8cf3b9c4"
source_commit = "593544bb65cdafba45a3a2c63b8c66148d65a4b3"
source_locale = "en-US"
+++
## Nguồn gốc {#origins}

Cam kết đầu tiên cho trình biên dịch Radix được thực hiện vào **ngày 20 tháng 12 năm 2025**
dưới dạng một dự án Bun + TypeScript với duy nhất tệp `docs/decisions.md`. Cam kết
thứ hai đã hệ thống hóa năm Hồ sơ Quyết định Kiến trúc vẫn định hình ngôn ngữ cho đến
ngày nay.

**ADR-003**, có tiêu đề "Đuôi cách mang ý nghĩa ngữ nghĩa", ngay từ đầu đã xác lập
rằng hình thái học Latin sẽ không chỉ là một lớp vỏ từ khóa — trình biên dịch sẽ hiểu
sự biến cách và chia động từ để suy luận ý định của chương trình. Các ánh xạ cách ban
đầu là:

```text
Nominative  (subject)       →  return value, caller
Accusative  (direct object)  →  primary argument
Dative      (indirect obj.)  →  recipient, callback, destination
Genitive    (possession)     →  property access, "of" relationships
Ablative    (instrument)     →  dependencies, context, "using X"
```

Tài liệu đó cũng ghi chú: *"Chia động từ là một câu hỏi tiếp nối tự nhiên
(thì tương lai → bất đồng bộ?)."* Hạt giống này đã phát triển thành quy ước đặt tên
**morphologia** hiện đại, trong đó thư viện chuẩn sử dụng các dạng động từ Latin đã
được chia để biểu thị chạy đồng bộ hay bất đồng bộ, cũng như biến đổi hay sao chép dữ
liệu ra — mà không yêu cầu bản thân trình biên dịch phải hiểu ngữ pháp Latin.

Dự án bắt đầu bằng TypeScript, sau đó được viết lại bằng Rust, và ngữ pháp đã được
đóng băng cho dòng 1.x với edition 2026. Năm ADR ban đầu (phần mở rộng tệp `.fab`,
gợi ý lỗi, đuôi cách, trình phân tích cú pháp đệ quy đi xuống, AST tùy chỉnh) vẫn có
thể xem trong lịch sử git.

## Các bản phát hành {#releases}

Các gói CLI dựng sẵn — bản phát hành Faber hiện tại ở trên cùng, sau đó là mọi thẻ
và tệp nhị phân đã được phát hành từ [faberlang/releases](https://github.com/faberlang/releases):

- **[Các bản phát hành](/history/releases.html)** — liên kết tải xuống và danh mục lịch sử
- **[Cài đặt và tải xuống](/start/install.html)** — thiết lập PATH và chạy `faber check` lần đầu
