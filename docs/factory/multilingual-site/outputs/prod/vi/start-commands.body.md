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

<<<FENCE 0>>>

Một lần kiểm tra thành công có nghĩa là package được chấp nhận về cú pháp và ngữ nghĩa bởi phần đầu của trình biên dịch. Điều đó không có nghĩa là toolchain native cuối cùng đã được gọi.

## Build {#build}

<<<FENCE 1>>>

Đích Rust được thiết kế để dễ xem xét. Rust được sinh ra là một artifact của trình biên dịch, không phải nguồn sự thật; hãy chỉnh sửa package Faber rồi build lại thay vì tự sửa Rust đã xuất bằng tay.

## Run {#run}

<<<FENCE 2>>>

Dùng `run` cho các package ứng dụng có điểm vào `incipit`. Các package chỉ chứa thư viện nên được kiểm tra và chạy kiểm thử thay thế.

## Giải thích chẩn đoán {#explain}

<<<FENCE 3>>>

Các nhóm chẩn đoán là các mã tham chiếu ổn định: `LEX` cho lỗi từ vựng, `PAR` cho lỗi phân tích cú pháp, `SEM` cho lỗi ngữ nghĩa/kiểu. Trong tài liệu và báo cáo của agent, hãy trích dẫn mã chẩn đoán thay vì diễn giải mơ hồ về lỗi của trình biên dịch.

## Lệnh theo locale người đọc {#reader-locale}

<<<FENCE 4>>>

Đầu ra theo locale người đọc là cách biểu diễn mô hình ngữ nghĩa của trình biên dịch, không phải lớp dịch tại thời điểm trình duyệt chạy. Công việc locale nên được thực hiện sau khi package kiểm tra thành công ở dạng chuẩn.

## Tiếp theo {#next}

| Trước | Tiếp theo |
|---|---|
| [Xin chào, Faber](/start/hello.html) | [Các dự án và ví dụ](/start/projects.html) |
