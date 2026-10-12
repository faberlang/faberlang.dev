Trang này là bản đồ CLI thực tế cho tuần đầu tiên làm việc với Faber. Hãy dùng
nó như một chỉ mục lệnh, sau đó mở trang chi tiết [Công cụ build Faber](/tooling/faber-build-tool.html)
khi bạn cần cờ và thông tin về pipeline của trình biên dịch.

## Vòng lặp hàng ngày {#daily-loop}

| Lệnh | Dùng để |
|---|---|
| `faber check <package>` | Kiểm tra front-end nhanh: lex, parse, kiểm tra kiểu, lower |
| `faber build <package> -t rust` | Xuất một project Rust để xem lại hoặc biên dịch native |
| `faber run <package>` | Build và thực thi một application package |
| `faber test <package>` | Chạy test của package khi package định nghĩa các bề mặt kiểm thử |
| `faber explain <code>` | Đọc phần giải thích chẩn đoán ổn định |

Bắt đầu với `check`. Đây là lệnh rẻ nhất và là lệnh mà các agent nên chạy
trước khi đề xuất mã đã sinh là Faber hợp lệ.

## Check {#check}

<<<FENCE 0>>>

Việc kiểm tra đạt nghĩa là package được front end của trình biên dịch chấp nhận
về mặt cú pháp và ngữ nghĩa. Nó không có nghĩa là toolchain native cuối cùng đã
được gọi.

## Build {#build}

<<<FENCE 1>>>

Target Rust được cố tình làm cho dễ xem lại. Rust được sinh ra là một artifact
của trình biên dịch, chứ không phải nguồn chân lý; hãy chỉnh sửa package Faber
và rebuild thay vì vá Rust đã xuất bằng tay.

## Run {#run}

<<<FENCE 2>>>

Dùng `run` cho các application package có điểm vào `incipit`. Các package chỉ
thư viện nên được check và test thay thế.

## Giải thích chẩn đoán {#explain}

<<<FENCE 3>>>

Các họ chẩn đoán là các handle ổn định: `LEX` cho lỗi từ vựng, `PAR` cho lỗi
parser, `SEM` cho lỗi ngữ nghĩa/kiểu. Trong tài liệu và báo cáo của agent, hãy
trích dẫn mã chẩn đoán thay vì diễn xuôi lỏng lẻo một lỗi của trình biên dịch.

## Lệnh theo ngôn ngữ đọc {#reader-locale}

<<<FENCE 4>>>

Đầu ra theo ngôn ngữ đọc là một bản dựng của mô hình ngữ nghĩa của trình biên
dịch, chứ không phải một lớp dịch tại thời điểm trình duyệt. Công việc về locale
thuộc về sau khi một package đã check ở dạng chuẩn.

## Tiếp theo {#next}

| Trước | Tiếp |
|---|---|
| [Hello, Faber](/start/hello.html) | [Dự án và ví dụ](/start/projects.html) |
