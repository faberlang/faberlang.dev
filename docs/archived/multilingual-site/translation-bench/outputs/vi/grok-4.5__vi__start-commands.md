Trang này là bản đồ CLI thực dụng cho tuần đầu làm việc với Faber. Hãy dùng như chỉ mục lệnh, rồi mở trang chi tiết [Công cụ build Faber](/tooling/faber-build-tool.html) khi bạn cần cờ và chi tiết pipeline trình biên dịch.

## Vòng lặp hằng ngày {#daily-loop}

| Lệnh | Dùng để |
|---|---|
| `faber check <package>` | Kiểm tra front-end nhanh: lex, parse, type check, lower |
| `faber build <package> -t rust` | Phát ra dự án Rust để xem xét hoặc biên dịch native |
| `faber run <package>` | Build và thực thi gói ứng dụng |
| `faber test <package>` | Chạy test của gói khi gói định nghĩa bề mặt test |
| `faber explain <code>` | Đọc giải thích chẩn đoán ổn định |

Bắt đầu với `check`. Đây là lệnh rẻ nhất và là lệnh mà agent nên chạy trước khi đề xuất mã được sinh ra là Faber hợp lệ.

## Kiểm tra {#check}

<<<FENCE 0>>>

Một lần check pass nghĩa là gói chấp nhận được về cú pháp và ngữ nghĩa với front end của trình biên dịch. Điều đó không có nghĩa toolchain native cuối cùng đã được gọi.

## Build {#build}

<<<FENCE 1>>>

Target Rust được thiết kế cố ý để có thể xem xét. Rust được sinh ra là artifact của trình biên dịch, không phải nguồn chân lý; hãy sửa gói Faber rồi build lại thay vì vá tay Rust đã emit.

## Run {#run}

<<<FENCE 2>>>

Dùng `run` cho gói ứng dụng có entry point `incipit`. Gói chỉ thư viện nên được check và test thay thế.

## Giải thích chẩn đoán {#explain}

<<<FENCE 3>>>

Các họ chẩn đoán là handle ổn định: `LEX` cho lỗi từ vựng, `PAR` cho lỗi parser, `SEM` cho lỗi ngữ nghĩa/kiểu. Trong tài liệu và báo cáo agent, hãy trích dẫn mã chẩn đoán thay vì diễn giải lỏng lẻo một lỗi trình biên dịch.

## Lệnh locale người đọc {#reader-locale}

<<<FENCE 4>>>

Output locale người đọc là một render của mô hình ngữ nghĩa trình biên dịch, không phải lớp dịch lúc runtime trình duyệt. Công việc locale thuộc sau khi gói check ở dạng canonical.

## Tiếp theo {#next}

| Trước | Tiếp |
|---|---|
| [Hello, Faber](/start/hello.html) | [Dự án và ví dụ](/start/projects.html) |
