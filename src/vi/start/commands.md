+++
translation_kind = "translated"

title = "Commands you will use"
section = "commands"
order = 3
sources = []

prose_hash = "sha256:0e56e02cfc5bc616178712a8ff6e3d914b95257913dbd22db2e8e8aac3c0e72e"
code_hash = "sha256:adf615632f084c7edf7f1f0dfc205ee4912e8b497b19c9c96167bf9b97e443cc"
source_commit = "6572815c8c5595e60956471d75c4a60e67cba58f"
source_locale = "en-US"
+++
Đây là bản đồ CLI thực hành cho tuần đầu làm việc với Faber. Hãy dùng trang này làm mục lục lệnh, sau đó mở trang chi tiết [công cụ build Faber](/tooling/faber-build-tool.html) khi cần xem các cờ lệnh và thông tin chi tiết về pipeline biên dịch.

## Vòng lặp hằng ngày {#daily-loop}

| Lệnh | Dùng cho |
|---|---|
| `faber check <package>` | Kiểm tra nhanh phần đầu vào: phân tích từ vựng, phân tích cú pháp, kiểm tra kiểu, hạ cấp |
| `faber build <package> -t rust` | Xuất một dự án Rust để xem xét hoặc biên dịch native |
| `faber run <package>` | Build và thực thi một package ứng dụng |
| `faber test <package>` | Chạy các bài kiểm thử của package khi package định nghĩa các bề mặt kiểm thử |
| `faber explain <code>` | Đọc phần giải thích chẩn đoán ổn định |

Hãy bắt đầu với `check`. Đây là lệnh có chi phí thấp nhất và là lệnh mà các agent nên chạy trước khi đề xuất mã được sinh ra là Faber hợp lệ.

## Check {#check}

```bash
faber check .
faber check examples/ai-workbench/packages/faber-ai
```

Một lần kiểm tra thành công có nghĩa là package được chấp nhận về cú pháp và ngữ nghĩa bởi phần đầu của trình biên dịch. Điều đó không có nghĩa là toolchain native cuối cùng đã được gọi.

## Build {#build}

```bash
faber build . -t rust
```

Đích Rust được thiết kế để dễ xem xét. Rust được sinh ra là một artifact của trình biên dịch, không phải nguồn sự thật; hãy chỉnh sửa package Faber rồi build lại thay vì tự sửa Rust đã xuất bằng tay.

## Run {#run}

```bash
faber run .
```

Dùng `run` cho các package ứng dụng có điểm vào `incipit`. Các package chỉ chứa thư viện nên được kiểm tra và chạy kiểm thử thay thế.

## Giải thích chẩn đoán {#explain}

```bash
faber explain SEM001
faber explain LEX006
```

Các nhóm chẩn đoán là các mã tham chiếu ổn định: `LEX` cho lỗi từ vựng, `PAR` cho lỗi phân tích cú pháp, `SEM` cho lỗi ngữ nghĩa/kiểu. Trong tài liệu và báo cáo của agent, hãy trích dẫn mã chẩn đoán thay vì diễn giải mơ hồ về lỗi của trình biên dịch.

## Lệnh theo locale người đọc {#reader-locale}

```bash
faber format --reader-locale=la path/to/file.fab
faber format --reader-locale=th-TH path/to/file.fab
faber emit -t faber --reader-locale=zh-Hans path/to/file.fab
```

Đầu ra theo locale người đọc là cách biểu diễn mô hình ngữ nghĩa của trình biên dịch, không phải lớp dịch tại thời điểm trình duyệt chạy. Công việc locale nên được thực hiện sau khi package kiểm tra thành công ở dạng chuẩn.

## Tiếp theo {#next}

| Trước | Tiếp theo |
|---|---|
| [Xin chào, Faber](/start/hello.html) | [Các dự án và ví dụ](/start/projects.html) |
