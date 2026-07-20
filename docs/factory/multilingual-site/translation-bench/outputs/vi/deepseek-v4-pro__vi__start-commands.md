Trang này là bản đồ CLI thực hành cho tuần đầu tiên làm việc với Faber. Dùng nó như
chỉ mục lệnh, sau đó mở trang [công cụ xây dựng Faber](/tooling/faber-build-tool.html)
chi tiết khi bạn cần cờ và chi tiết pipeline biên dịch.

## Vòng lặp hàng ngày {#daily-loop}

| Lệnh | Dùng để |
|---|---|
| `faber check <package>` | Kiểm tra front-end nhanh: lex, parse, type check, lower |
| `faber build <package> -t rust` | Xuất dự án Rust để xem xét hoặc biên dịch native |
| `faber run <package>` | Xây dựng và thực thi gói ứng dụng |
| `faber test <package>` | Chạy test của gói khi gói có định nghĩa bề mặt test |
| `faber explain <code>` | Đọc giải thích chẩn đoán ổn định |

Bắt đầu với `check`. Đây là lệnh nhẹ nhất và là lệnh mà agent nên chạy trước khi
đề xuất mã sinh ra là Faber hợp lệ.

## Check {#check}

<<<FENCE 0>>>

Một lần check đạt nghĩa là gói được chấp nhận về mặt cú pháp và ngữ nghĩa bởi
front-end của trình biên dịch. Điều này không có nghĩa là toolchain native cuối
cùng đã được gọi.

## Build {#build}

<<<FENCE 1>>>

Đầu ra Rust được thiết kế để có thể xem xét. Rust sinh ra là sản phẩm của trình
biên dịch, không phải nguồn chân lý; hãy sửa gói Faber và xây dựng lại thay vì vá
Rust đầu ra bằng tay.

## Run {#run}

<<<FENCE 2>>>

Dùng `run` cho các gói ứng dụng có điểm vào `incipit`. Các gói chỉ-thư-viện nên
được check và test.

## Giải thích chẩn đoán {#explain}

<<<FENCE 3>>>

Các họ chẩn đoán là các handle ổn định: `LEX` cho lỗi từ vựng, `PAR` cho lỗi phân
tích cú pháp, `SEM` cho lỗi ngữ nghĩa/kiểu. Trong tài liệu và báo cáo agent, hãy
trích dẫn mã chẩn đoán thay vì diễn giải lỗi biên dịch một cách lỏng lẻo.

## Lệnh reader-locale {#reader-locale}

<<<FENCE 4>>>

Đầu ra reader locale là một kết xuất của mô hình ngữ nghĩa của trình biên dịch,
không phải một tầng dịch ở thời điểm trình duyệt. Công việc locale nên thực hiện
sau khi gói đã check ở dạng canonical.

## Tiếp theo {#next}

| Trước | Tiếp |
|---|---|
| [Xin chào, Faber](/start/hello.html) | [Dự án và ví dụ](/start/projects.html) |
