Trang này là bản đồ CLI thực hành cho tuần đầu tiên làm việc với Faber. Hãy dùng nó
làm mục lục lệnh, sau đó mở trang [công cụ build Faber](/tooling/faber-build-tool.html)
chi tiết khi bạn cần các cờ và thông tin chi tiết về pipeline của trình biên dịch.

## Vòng lặp hằng ngày {#daily-loop}

| Lệnh | Dùng để làm gì |
|---|---|
| `faber check <package>` | Xác thực front-end nhanh: phân tích từ vựng, phân tích cú pháp, kiểm tra kiểu, hạ cấp |
| `faber build <package> -t rust` | Xuất một dự án Rust để xem xét hoặc biên dịch native |
| `faber run <package>` | Build và thực thi một package ứng dụng |
| `faber test <package>` | Chạy các bài kiểm thử của package khi package định nghĩa các bề mặt kiểm thử |
| `faber explain <code>` | Đọc phần giải thích chẩn đoán ổn định |

Hãy bắt đầu với `check`. Đây là lệnh ít tốn kém nhất và là lệnh mà các agent nên chạy
trước khi đề xuất mã được sinh ra là Faber hợp lệ.

## Kiểm tra {#check}

<<<FENCE 0>>>

Một lần kiểm tra thành công có nghĩa là package được chấp nhận về cú pháp và ngữ nghĩa
bởi front end của trình biên dịch. Điều đó không có nghĩa là bộ công cụ native cuối cùng đã
được gọi.

## Build {#build}

<<<FENCE 1>>>

Đích Rust được thiết kế để có thể xem xét. Rust được sinh ra là một artifact của trình biên dịch,
không phải nguồn chân lý; hãy chỉnh sửa package Faber và build lại thay vì tự sửa Rust đã xuất ra.

## Chạy {#run}

<<<FENCE 2>>>

Dùng `run` cho các package ứng dụng có điểm vào `incipit`. Các package chỉ có thư viện
nên được kiểm tra và chạy kiểm thử thay thế.

## Giải thích chẩn đoán {#explain}

<<<FENCE 3>>>

Các nhóm chẩn đoán là những mã tham chiếu ổn định: `LEX` cho lỗi từ vựng, `PAR` cho
lỗi trình phân tích cú pháp, `SEM` cho lỗi ngữ nghĩa/kiểu. Trong tài liệu và báo cáo của agent,
hãy dẫn mã chẩn đoán thay vì diễn giải mơ hồ một lỗi của trình biên dịch.

## Lệnh theo locale người đọc {#reader-locale}

<<<FENCE 4>>>

Đầu ra theo locale người đọc là cách kết xuất mô hình ngữ nghĩa của trình biên dịch,
không phải lớp dịch tại thời điểm trình duyệt. Công việc về locale thuộc giai đoạn sau khi
package đã kiểm tra ở dạng chuẩn tắc.

## Tiếp theo {#next}

| Trước | Tiếp theo |
|---|---|
| [Xin chào, Faber](/start/hello.html) | [Các dự án và ví dụ](/start/projects.html) |
